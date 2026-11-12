/* =======================================================
   NIHONGO INTERMEDIATE - grammar-lessons.js
   Book 3 lesson-wise parity with the Vocab/Kanji pages:
   - Lesson picker (Select lessons, per Part groups)
   - Learn (flashcards) + Start practice (drill quiz) sessions
   - Grammar status bars, study activity heatmap, progress foldout
   Patterns use G:<patternId>, drills use GD:<source>:<section>:<question>.
   Both use the standard SRS grader, so Due SRS, the pillar banner, the hard
   pane, the streak and the heatmap all stay in sync.
   ======================================================= */

import { grammarDrillContent } from './grammar-card-data.js';
import { GRAMMAR_FURIGANA } from './grammar-furigana.js';
import { state } from './state.js';
import { peekItemStatus } from './srs.js';
import { beginGistReviewSession } from './gist-sync.js';
import { renderCard } from './study.js?v=4.5';
import { showView } from './navigation.js';
import { getDay, getHeatmap30, getCurrentStreak } from './daylog.js';
import { istDateKey } from './time.js';
import { renderHeatmapGridHtml } from './today.js';
import { renderActivityDayHtml } from './activity-detail.js';

const stripHtml = h => String(h || '').replace(/<rt>.*?<\/rt>/g, '').replace(/<[^>]+>/g, '').trim();

// -------------------------------------------------------
// LESSON MODEL
// One lesson per grammar_index section_id, grouped by book part.
// -------------------------------------------------------
export function grammarSections() {
  const idx = (state.grammarDB && state.grammarDB.index) || [];
  const sections = [];
  const bySec = {};
  idx.forEach(p => {
    const secId = p.section_id || 'misc';
    let sec = bySec[secId];
    if (!sec) {
      const part = secId.startsWith('p1-') ? '1' : secId.startsWith('p3-') ? '3' : '2';
      sec = { secId, part, title: p.section_title || secId, titlePlain: stripHtml(p.section_title), patterns: [] };
      bySec[secId] = sec;
      sections.push(sec);
    }
    sec.patterns.push(p);
  });
  // Include drill-only lessons/reviews too. The 83-pattern index covers
  // only some sections of the source files, not the whole exercise bank.
  for (const [part, dbKey, prefix] of [['1','part1_1_6','p1-sec-'],['1','part1_7_12','p1-sec-'],['2','part2','sec-'],['3','part3','p3-sec-']]) {
    for (const raw of (state.grammarDB?.[dbKey]?.sections || [])) {
      const secId = prefix + raw.section_number;
      if (!bySec[secId] && raw.drills?.length) {
        const sec = {secId,part,title:raw.title,titlePlain:stripHtml(raw.title),patterns:[]};
        bySec[secId] = sec; sections.push(sec);
      }
    }
  }
  sections.sort((a,b) => Number(a.part)-Number(b.part) || Number(a.secId.split('-').pop())-Number(b.secId.split('-').pop()));
  sections.forEach(sec => { sec.label = lessonLabel(sec); });
  return sections;
}

// Compact tile label: Part 1 lessons "1".."12", Part 2 まとめ "F".."J",
// Part 2/3 lessons "2-1".."3-3".
function lessonLabel(sec) {
  const t = sec.titlePlain;
  const mPartLesson = t.match(/第(\d+)部[\s\S]*?第(\d+)課/);
  if (mPartLesson) return `${mPartLesson[1]}-${mPartLesson[2]}`;
  const mSummary = t.match(/まとめ\s*([A-Z])/);
  if (mSummary) return mSummary[1];
  if (/まとめ/.test(t)) return 'R' + sec.secId.split('-').pop();
  const mLesson = t.match(/第(\d+)課/);
  if (mLesson) return mLesson[1];
  return sec.secId.replace(/^(p1-|p3-)?sec-/, '');
}

// Textbook drill sections for a grammar lesson, mirroring the data files.
function drillsForSection(sec) {
  const num = parseInt(sec.secId.replace(/^(p1-|p3-)?sec-/, ''), 10);
  if (!Number.isFinite(num)) return { drills: [], tagPrefix: null, num: null };
  if (sec.part === '1') {
    const file = num <= 6 ? state.grammarDB.part1_1_6 : state.grammarDB.part1_7_12;
    const s = (file?.sections || []).find(x => x.section_number === num);
    return { drills: s?.drills || [], tagPrefix: num <= 6 ? 'p1a' : 'p1b', num };
  }
  if (sec.part === '2') {
    const s = (state.grammarDB.part2?.sections || []).find(x => x.section_number === num);
    return { drills: s?.drills || [], tagPrefix: 'p2', num };
  }
  const s = (state.grammarDB.part3?.sections || []).find(x => x.section_number === num);
  return { drills: s?.drills || [], tagPrefix: 'p3', num };
}

// -------------------------------------------------------
// SELECTION STATE
// -------------------------------------------------------
function ensureSelectionState() {
  if (!(state.grammarSelectedSections instanceof Set)) state.grammarSelectedSections = new Set();
  if (typeof state.grammarSelectionEmpty !== 'boolean') state.grammarSelectionEmpty = true;
  if (!state.grammarLessonGroup) state.grammarLessonGroup = '1';
  if (!state.grammarSessionSize) state.grammarSessionSize = 'all';
  if (!state.grammarPickerMode) state.grammarPickerMode = 'learn';
  if (!(state.grammarSelectedGroups instanceof Set)) state.grammarSelectedGroups = new Set();
  if (typeof state.grammarGroupSelectionEmpty !== 'boolean') state.grammarGroupSelectionEmpty = true;
  if (!(state.grammarSelectedTests instanceof Set)) state.grammarSelectedTests = new Set();
  if (typeof state.grammarTestSelectionEmpty !== 'boolean') state.grammarTestSelectionEmpty = true;
}

// -------------------------------------------------------
// LEARN GROUPS (his ask 2026-11-12): learn in chunks of ~35-40
// grammar points instead of 3-5 per textbook lesson. Book order,
// split at lesson boundaries; 83 patterns -> two ~41-pattern groups
// (a strict 40 cap would leave a tiny 7-pattern tail group).
// -------------------------------------------------------
export function learnGroups() {
  const secs = grammarSections();
  const groups = [];
  let cur = null;
  secs.forEach(sec => {
    if (!sec.patterns.length) return;
    if (cur && cur.patterns.length + sec.patterns.length > 42) { groups.push(cur); cur = null; }
    if (!cur) cur = { id: `learn-g${groups.length + 1}`, secs: [], patterns: [] };
    cur.secs.push(sec);
    cur.patterns.push(...sec.patterns.map(pattern => ({ sec, pattern })));
  });
  if (cur) groups.push(cur);
  groups.forEach(g => {
    const first = g.secs[0], last = g.secs[g.secs.length - 1];
    g.label = first.part === last.part && first.part === '1' ? `${first.label}-${last.label}` : `${first.label}+`;
    g.title = g.secs.map(sec => sec.titlePlain).join(' · ');
  });
  return groups;
}

// Mock exam list from the loaded grammar DB.
function mockTests() {
  const mock = state.grammarDB?.mock;
  if (!mock) return [];
  const tests = mock.mock_tests || [];
  const questions = mock.questions || [];
  return tests.map(t => ({
    n: t.test_number,
    title: (t.title_en || `Mock Test ${t.test_number}`),
    questions: questions.filter(q => String(q.category || '').startsWith(`第${t.test_number}回`))
  })).filter(t => t.questions.length);
}

export function setGrammarPickerMode(mode) {
  if (!['learn', 'drill', 'test'].includes(mode)) return;
  ensureSelectionState();
  state.grammarPickerMode = mode;
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
  if (typeof window !== 'undefined') window.renderGrammarPatternsList?.();
}

function selectedSections() {
  ensureSelectionState();
  const all = grammarSections();
  if (state.grammarSelectionEmpty) return [];
  if (state.grammarSelectedSections.size === 0) return all; // empty set = All
  const sel = state.grammarSelectedSections;
  return all.filter(sec => sec.part === state.grammarLessonGroup && sel.has(sec.secId));
}

export function setGrammarLessonGroup(group) {
  ensureSelectionState();
  state.grammarLessonGroup = group;
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
  if (typeof window !== 'undefined') window.renderGrammarPatternsList?.();
}

export function selectGrammarLearnGroup(groupId) {
  ensureSelectionState();
  const sel = state.grammarSelectedGroups;
  if (sel.has(groupId)) sel.delete(groupId); else sel.add(groupId);
  state.grammarGroupSelectionEmpty = sel.size === 0;
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
}

export function selectGrammarTest(testN) {
  ensureSelectionState();
  const sel = state.grammarSelectedTests;
  if (sel.has(testN)) sel.delete(testN); else sel.add(testN);
  state.grammarTestSelectionEmpty = sel.size === 0;
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
}

export function selectGrammarLesson(secId, mode = 'toggle') {
  ensureSelectionState();
  if (secId === 'all' && state.grammarPickerMode === 'learn') {
    state.grammarGroupSelectionEmpty = false;
    learnGroups().forEach(g => state.grammarSelectedGroups.add(g.id));
    renderGrammarLessonChips();
    updateGrammarActionButtonLabels();
    return;
  }
  if (secId === 'all' && state.grammarPickerMode === 'test') {
    state.grammarTestSelectionEmpty = false;
    mockTests().forEach(t => state.grammarSelectedTests.add(t.n));
    renderGrammarLessonChips();
    updateGrammarActionButtonLabels();
    return;
  }
  const sel = state.grammarSelectedSections;
  if (secId === 'all') {
    // Select every lesson in the active group.
    state.grammarSelectionEmpty = false;
    grammarSections().filter(sec => sec.part === state.grammarLessonGroup).forEach(sec => sel.add(sec.secId));
  } else if (mode === 'toggle') {
    if (sel.has(secId)) sel.delete(secId); else sel.add(secId);
    state.grammarSelectionEmpty = sel.size === 0;
  } else {
    sel.clear();
    sel.add(secId);
    state.grammarLessonGroup = grammarSections().find(sec => sec.secId === secId)?.part || state.grammarLessonGroup;
    state.grammarSelectionEmpty = false;
  }
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
  if (typeof window !== 'undefined') window.renderGrammarPatternsList?.();
}

export function clearGrammarLessonSelection() {
  ensureSelectionState();
  if (state.grammarPickerMode === 'learn') {
    state.grammarSelectedGroups.clear();
    state.grammarGroupSelectionEmpty = true;
  } else if (state.grammarPickerMode === 'test') {
    state.grammarSelectedTests.clear();
    state.grammarTestSelectionEmpty = true;
  } else {
    state.grammarSelectedSections.clear();
    state.grammarSelectionEmpty = true;
  }
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
  if (typeof window !== 'undefined') window.renderGrammarPatternsList?.();
}

export function setGrammarSessionSize(size) {
  state.grammarSessionSize = size;
  updateGrammarActionButtonLabels();
  if (typeof window !== 'undefined') window.renderGrammarPatternsList?.();
}

export function toggleGrammarHardOnly() {
  state.grammarHardOnly = !state.grammarHardOnly;
  updateGrammarActionButtonLabels();
  if (typeof window !== 'undefined') window.renderGrammarPatternsList?.();
}

// -------------------------------------------------------
// PICKER + ACTION LABELS
// -------------------------------------------------------
export function renderGrammarLessonChips() {
  const container = document.getElementById('grammar-lesson-chips-row');
  if (!container) return;
  ensureSelectionState();
  container.innerHTML = '';

  // Keep the pillar banner directly under the picker, like the Kanji page.
  const banner = document.getElementById('pb-grammar');
  const picker = document.querySelector('#view-grammar .home-lessons-card');
  if (banner && picker && picker.nextElementSibling !== banner) picker.after(banner);

  const mode = state.grammarPickerMode;
  ['learn', 'drill', 'test'].forEach(m => {
    const tab = document.getElementById(`grammar-mode-${m}`);
    if (tab) { tab.classList.toggle('active', m === mode); tab.setAttribute('aria-selected', String(m === mode)); }
  });
  const partTabs = document.getElementById('grammar-part-tabs');
  if (partTabs) partTabs.style.display = mode === 'drill' ? '' : 'none';
  const hardSetting = document.getElementById('grammar-setting-hard');
  if (hardSetting) hardSetting.style.display = mode === 'test' ? 'none' : '';
  const learnBtn0 = document.getElementById('btn-grammar-learn');
  if (learnBtn0) learnBtn0.style.display = mode === 'learn' ? '' : 'none';
  const practiceBtn0 = document.getElementById('btn-grammar-practice');
  if (practiceBtn0) practiceBtn0.style.display = mode === 'drill' ? '' : 'none';
  const testBtn0 = document.getElementById('btn-grammar-test');
  if (testBtn0) testBtn0.style.display = mode === 'test' ? '' : 'none';

  if (mode === 'learn') {
    const selG = state.grammarSelectedGroups;
    learnGroups().forEach(g => {
      const selected = !state.grammarGroupSelectionEmpty && selG.has(g.id);
      let hasHard = false;
      let allMastered = true;
      g.patterns.forEach(({ pattern }) => {
        const st = peekItemStatus(`G:${pattern.id}`);
        if (st === 'hard') hasHard = true;
        if (st !== 'mastered') allMastered = false;
      });
      const tile = document.createElement('button');
      tile.type = 'button';
      tile.className = `home-lesson-tile${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${allMastered ? ' all-done' : ''}`;
      tile.setAttribute('aria-pressed', String(selected));
      tile.setAttribute('aria-label', `${g.title}, ${g.patterns.length} patterns${selected ? ', selected' : ''}`);
      tile.title = `${g.title} · ${g.patterns.length} patterns`;
      tile.innerHTML = `<span class="home-lesson-tile-num">${g.label}</span><span class="home-lesson-tile-count">${g.patterns.length}p</span>`;
      tile.onclick = () => selectGrammarLearnGroup(g.id);
      container.appendChild(tile);
    });
    const selectAllBtnL = document.getElementById('grammar-select-all');
    if (selectAllBtnL) selectAllBtnL.onclick = () => selectGrammarLesson('all');
    const clearBtnL = document.getElementById('grammar-clear-selection');
    if (clearBtnL) clearBtnL.onclick = () => clearGrammarLessonSelection();
    return;
  }

  if (mode === 'test') {
    const selT = state.grammarSelectedTests;
    mockTests().forEach(t => {
      const selected = !state.grammarTestSelectionEmpty && selT.has(t.n);
      let hasHard = false;
      let allMastered = true;
      t.questions.forEach(q => {
        const st = peekItemStatus(`GM:${q.question_id}`);
        if (st === 'hard') hasHard = true;
        if (st !== 'mastered') allMastered = false;
      });
      const tile = document.createElement('button');
      tile.type = 'button';
      tile.className = `home-lesson-tile${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${allMastered ? ' all-done' : ''}`;
      tile.setAttribute('aria-pressed', String(selected));
      tile.setAttribute('aria-label', `${t.title}, ${t.questions.length} questions${selected ? ', selected' : ''}`);
      tile.title = `${t.title} · ${t.questions.length} questions`;
      tile.innerHTML = `<span class="home-lesson-tile-num">${t.n}</span><span class="home-lesson-tile-count">${t.questions.length}q</span>`;
      tile.onclick = () => selectGrammarTest(t.n);
      container.appendChild(tile);
    });
    const selectAllBtnT = document.getElementById('grammar-select-all');
    if (selectAllBtnT) selectAllBtnT.onclick = () => selectGrammarLesson('all');
    const clearBtnT = document.getElementById('grammar-clear-selection');
    if (clearBtnT) clearBtnT.onclick = () => clearGrammarLessonSelection();
    return;
  }

  const group = state.grammarLessonGroup;
  const sel = state.grammarSelectedSections;
  const isAll = !state.grammarSelectionEmpty && sel.size === 0;

  ['1', '2', '3'].forEach(g => {
    const tab = document.getElementById(`grammar-tab-part${g}`);
    if (tab) {
      tab.textContent = `${{1:'Lessons 1-12',2:'Summary + structure',3:'Text grammar'}[g]} · ${grammarSections().filter(sec => sec.part === g).length}`;
      tab.classList.toggle('active', g === group);
      tab.setAttribute('aria-selected', String(g === group));
    }
  });

  grammarSections().filter(sec => sec.part === group).forEach(sec => {
    const selected = isAll || sel.has(sec.secId);
    let hasHard = false;
    let allMastered = sec.patterns.length > 0;
    const d = drillsForSection(sec);
    if (d.drills.some(q => peekItemStatus(`GD:${d.tagPrefix}:${d.num}:${q.question_id}`) === 'hard')) hasHard = true;
    sec.patterns.forEach(p => {
      const st = peekItemStatus(`G:${p.id}`);
      if (st === 'hard') hasHard = true;
      if (st !== 'mastered') allMastered = false;
    });
    const tile = document.createElement('button');
    tile.type = 'button';
    tile.className = `home-lesson-tile${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${allMastered ? ' all-done' : ''}`;
    tile.setAttribute('aria-pressed', String(selected));
    tile.setAttribute('aria-label', `${sec.titlePlain}, ${sec.patterns.length} patterns${selected ? ', selected' : ''}`);
    tile.title = `${sec.titlePlain} · ${sec.patterns.length} patterns`;
    tile.innerHTML = `<span class="home-lesson-tile-num">${sec.label}</span><span class="home-lesson-tile-count">${sec.patterns.length ? sec.patterns.length+'p' : drillsForSection(sec).drills.length+'q'}</span>`;
    tile.onclick = () => selectGrammarLesson(sec.secId, 'toggle');
    container.appendChild(tile);
  });

  const selectAllBtn = document.getElementById('grammar-select-all');
  if (selectAllBtn) selectAllBtn.onclick = () => selectGrammarLesson('all');
  const clearBtn = document.getElementById('grammar-clear-selection');
  if (clearBtn) clearBtn.onclick = () => clearGrammarLessonSelection();
}

function lessonPool() {
  const secs = selectedSections();
  const patterns = [];
  const drills = [];
  secs.forEach(sec => {
    const { drills: secDrills, tagPrefix, num } = drillsForSection(sec);
    sec.patterns.forEach(p => patterns.push({ sec, pattern: p }));
    secDrills.forEach(drill => {
      const key = `GD:${tagPrefix}:${num}:${drill.question_id}`;
      drills.push({ sec, drill, key });
    });
  });
  if (state.grammarHardOnly) {
    const isHard = pid => peekItemStatus(`G:${pid}`) === 'hard';
    return {
      secs,
      patterns: patterns.filter(x => isHard(x.pattern.id)),
      drills: drills.filter(x => peekItemStatus(x.key) === 'hard')
    };
  }
  return { secs, patterns, drills };
}

export function updateGrammarActionButtonLabels() {
  ensureSelectionState();
  const mode = state.grammarPickerMode;
  const summary = document.getElementById('grammar-picker-summary');
  const hint = document.getElementById('grammar-start-hint');

  if (mode === 'learn') {
    const groups = learnGroups();
    const chosen = state.grammarGroupSelectionEmpty ? [] : groups.filter(g => state.grammarSelectedGroups.has(g.id));
    let patterns = chosen.flatMap(g => g.patterns);
    if (state.grammarHardOnly) patterns = patterns.filter(({ pattern }) => peekItemStatus(`G:${pattern.id}`) === 'hard');
    if (summary) {
      summary.textContent = state.grammarGroupSelectionEmpty
        ? 'Choose a learn group to begin'
        : `${chosen.length} ${chosen.length === 1 ? 'group' : 'groups'} selected · ${patterns.length} patterns${state.grammarHardOnly ? ' · hard only' : ''}`;
    }
    if (hint) {
      hint.textContent = state.grammarGroupSelectionEmpty
        ? 'Groups bundle the small textbook lessons into about 35-40 patterns each.'
        : chosen.map(g => `${g.label}: ${g.title}`).join('  |  ');
    }
    const learnBtn = document.getElementById('btn-grammar-learn');
    if (learnBtn) learnBtn.disabled = patterns.length === 0;
  } else if (mode === 'test') {
    const tests = mockTests();
    const chosen = state.grammarTestSelectionEmpty ? [] : tests.filter(t => state.grammarSelectedTests.has(t.n));
    const count = chosen.reduce((n, t) => n + t.questions.length, 0);
    if (summary) {
      summary.textContent = state.grammarTestSelectionEmpty
        ? 'Choose a mock test to begin'
        : `${chosen.length} ${chosen.length === 1 ? 'test' : 'tests'} selected · ${count} questions`;
    }
    if (hint) {
      hint.textContent = state.grammarTestSelectionEmpty
        ? 'Full JLPT N3 grammar mock exams, in exam order.'
        : chosen.map(t => t.title).join(' · ');
    }
    const testBtn = document.getElementById('btn-grammar-test');
    if (testBtn) testBtn.disabled = count === 0;
  } else {
    const { secs, patterns, drills } = lessonPool();
    const lessonCount = secs.length;
    if (summary) {
      summary.textContent = state.grammarSelectionEmpty
        ? 'Choose a lesson to begin'
        : `${lessonCount} ${lessonCount === 1 ? 'lesson' : 'lessons'} selected · ${patterns.length} patterns · ${drills.length} drill questions${state.grammarHardOnly ? ' · hard only' : ''}`;
    }
    if (hint) {
      hint.textContent = state.grammarSelectionEmpty
        ? 'Tap a lesson tile above. The groups follow the three source exercise sets.'
        : secs.map(sec => sec.titlePlain).join(' · ') + (!patterns.length && drills.length ? ' · Drill-only lesson.' : '');
    }
    const practiceBtn = document.getElementById('btn-grammar-practice');
    if (practiceBtn) practiceBtn.disabled = drills.length === 0;
  }
  const sizeSel = document.getElementById('grammar-session-size');
  if (sizeSel) sizeSel.value = state.grammarSessionSize;
  const hardCheck = document.getElementById('grammar-picker-hard');
  if (hardCheck) hardCheck.checked = Boolean(state.grammarHardOnly);
}

// -------------------------------------------------------
// SESSIONS (study runner)
// -------------------------------------------------------
function beginGrammarSession(items, kind, nextBatch = false) {
  if (!nextBatch) state.grammarRunQueue = items.slice();
  const size = state.grammarSessionSize === 'all' ? state.grammarRunQueue.length : Number(state.grammarSessionSize) || 10;
  items = state.grammarRunQueue.splice(0, size);
  state.studyMode = 'flashcard';
  state.studyIsDrillHard = false;
  state.drillOrigin = 'grammar';
  state.isDueReviewMode = false;
  state.learnUnit = null;
  state.grammarLastRun = kind;
  state.sessionItems = items;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = items.length;
  state.sessionTotal = items.length;
  state.cardFlipped = false;
  beginGistReviewSession();
  showView('study');
  renderCard();
}

// First textbook example per pattern, joined from the part source files by
// section + pattern name (tags stripped, whitespace ignored). Cached on state.
function grammarPatternExamples() {
  if (state.grammarPatternExampleMap) return state.grammarPatternExampleMap;
  const norm = s => String(s || '').replace(/<[^>]+>/g, '').replace(/[\s　]/g, '');
  const map = {};
  for (const [dbKey, prefix] of [['part1_1_6', 'p1-sec-'], ['part1_7_12', 'p1-sec-'], ['part2', 'sec-'], ['part3', 'p3-sec-']]) {
    for (const raw of (state.grammarDB?.[dbKey]?.sections || [])) {
      const secId = prefix + raw.section_number;
      (raw.patterns || []).forEach(p => { const ex = (p.example_sentences || [])[0]; if (ex?.japanese) map[`${secId}|${norm(p.pattern_name)}`] = ex; });
      (raw.points || []).forEach(pt => (pt.patterns || []).forEach(p => { const ex = (p.examples || [])[0]; if (ex?.japanese) map[`${secId}|${norm(p.pattern)}`] = ex; }));
    }
  }
  state.grammarPatternExampleMap = map;
  return map;
}

export function startGrammarLearn() {
  ensureSelectionState();
  const groups = learnGroups();
  const chosen = state.grammarGroupSelectionEmpty ? [] : groups.filter(g => state.grammarSelectedGroups.has(g.id));
  let patterns = chosen.flatMap(g => g.patterns);
  if (state.grammarHardOnly) patterns = patterns.filter(({ pattern }) => peekItemStatus(`G:${pattern.id}`) === 'hard');
  if (patterns.length === 0) {
    alert(state.grammarHardOnly ? 'No hard patterns in the selected groups!' : 'Select at least one learn group first.');
    return;
  }
  const exMap = grammarPatternExamples();
  const normEx = s => String(s || '').replace(/<[^>]+>/g, '').replace(/[\s　]/g, '');
  // Book order: lesson by lesson, pattern by pattern.
  const items = patterns.map(({ sec, pattern }) => {
    const ex = exMap[`${sec.secId}|${normEx(pattern.pattern)}`] || {};
    return {
      ...pattern,
      type: 'grammar',
      book: 'grammar',
      key: `G:${pattern.id}`,
      sectionLabel: sec.titlePlain,
      example_ja: ex.japanese || '',
      example_en: ex.english || '',
      pattern_ruby: GRAMMAR_FURIGANA[pattern.id]?.title || pattern.pattern_ruby || pattern.pattern,
      meaning_ja_ruby: GRAMMAR_FURIGANA[pattern.id]?.gloss || '',
      reviewPhase: 'test', learnNew: true, learned: false
    };
  });
  beginGrammarSession(items, 'learn');
}

export async function startGrammarPractice() {
  const { drills } = lessonPool();
  if (drills.length === 0) {
    alert(state.grammarHardOnly ? 'No hard drill questions in the selected lessons!' : 'Select at least one lesson first.');
    return;
  }
  // Shuffle so repeated runs of the same lesson feel fresh (vocab practice does the same).
  const pool = drills.slice();
  pool.sort(() => Math.random() - 0.5);
  const items = pool.map(({ sec, drill, key }) => {
    return {
      type: 'grammar_quiz',
      book: 'grammar',
      key,
      qid: drill.question_id,
      ...grammarDrillContent(drill),
      sectionLabel: sec.titlePlain,
      reviewPhase: 'test'
    };
  });
  beginGrammarSession(items, 'practice');
}

// Mock exam run: full test in exam order, graded through the standard SRS
// grader under additive GM:<qid> keys (existing G:/GD: progress untouched).
export function startGrammarTest() {
  ensureSelectionState();
  const tests = mockTests();
  const chosen = state.grammarTestSelectionEmpty ? [] : tests.filter(t => state.grammarSelectedTests.has(t.n));
  if (chosen.length === 0) {
    alert('Select at least one mock test first.');
    return;
  }
  const items = [];
  chosen.forEach(t => {
    t.questions.forEach(q => {
      items.push({
        type: 'grammar_quiz',
        book: 'grammar',
        key: `GM:${q.question_id}`,
        qid: q.question_id,
        ...grammarDrillContent(q),
        sectionLabel: t.title,
        reviewPhase: 'test'
      });
    });
  });
  beginGrammarSession(items, 'test');
}

// Graded test over the patterns from the learn run that just finished: same
// cards, now front-first with reveal + the four grade buttons, SRS-graded
// under the same G: keys as before.
export function startGrammarPatternTest() {
  const learned = (state.sessionItems || []).filter(item => item.type === 'grammar');
  if (learned.length === 0) { startGrammarLearn(); return; }
  const items = learned.map(item => ({ ...item, learnNew: false, learned: true, reviewPhase: 'test' }));
  beginGrammarSession(items, 'patternTest');
}

export function startNextGrammarBatch() {
  if (state.grammarRunQueue?.length) beginGrammarSession([], state.grammarLastRun, true);
}

export function startGrammarAgain() {
  if (state.grammarLastRun === 'practice') startGrammarPractice();
  else if (state.grammarLastRun === 'test') startGrammarTest();
  else if (state.grammarLastRun === 'patternTest') startGrammarPatternTest();
  else startGrammarLearn();
}

// -------------------------------------------------------
// STATUS BOX (mirrors the Kanji status card)
// -------------------------------------------------------
export function renderGrammarStatus() {
  const el = document.getElementById('gst-rows');
  if (!el) return;
  const sections = grammarSections();
  const tracks = [['1', 'Lessons'], ['2', 'Structure'], ['3', 'Text'], ['drills','Drills']];
  el.innerHTML = tracks.map(([part, label]) => {
    const patterns = part === 'drills' ? sections.flatMap(sec => { const d=drillsForSection(sec); return d.drills.map(q => ({key:`GD:${d.tagPrefix}:${d.num}:${q.question_id}`})); }) : sections.filter(sec => sec.part === part).flatMap(sec => sec.patterns);
    const total = patterns.length;
    const c = { mastered: 0, learning: 0, hard: 0, unseen: 0 };
    patterns.forEach(p => {
      const st = peekItemStatus(p.key || `G:${p.id}`);
      c[st === 'mastered' || st === 'hard' || st === 'learning' ? st : 'unseen']++;
    });
    const pct = n => (total ? (n / total) * 100 : 0).toFixed(2);
    const seg = k => `<span class="hvs-seg hvs-${k}" style="width:${pct(c[k])}%"></span>`;
    return `<div class="hvs-row" aria-label="${label}: ${c.mastered} mastered, ${c.learning} learning, ${c.hard} hard, ${c.unseen} new of ${total}">
      <div class="hvs-label">${label}</div>
      <div class="hvs-main"><div class="hvs-bar">${seg('mastered')}${seg('learning')}${seg('hard')}</div>
      <div class="hvs-counts"><span class="hvs-mastered"><b>${c.mastered}</b> mastered</span><span class="hvs-learning"><b>${c.learning}</b> learning</span><span class="hvs-hard"><b>${c.hard}</b> hard</span><span class="hvs-unseen"><b>${c.unseen}</b> new</span></div></div>
    </div>`;
  }).join('');
}

// -------------------------------------------------------
// PROGRESS FOLDOUT
// -------------------------------------------------------
export function updateGrammarProgress() {
  const sections = grammarSections();
  const all = sections.flatMap(sec => sec.patterns);
  let mastered = 0, learning = 0, hard = 0, unseen = 0;
  all.forEach(p => {
    const st = peekItemStatus(`G:${p.id}`);
    if (st === 'mastered') mastered++;
    else if (st === 'hard') hard++;
    else if (st === 'learning') learning++;
    else unseen++;
  });
  const startedSections = sections.filter(sec => sec.patterns.some(p => peekItemStatus(`G:${p.id}`) !== 'unseen') || drillsForSection(sec).drills.some(q => { const d = drillsForSection(sec); return peekItemStatus(`GD:${d.tagPrefix}:${d.num}:${q.question_id}`) !== 'unseen'; })).length;
  const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };
  set('grammar-prog-mastered', mastered);
  set('grammar-prog-learning', learning);
  set('grammar-prog-hard', hard);
  set('grammar-prog-unseen', unseen);
  const note = document.getElementById('grammar-prog-note');
  if (note) note.textContent = `${all.length} patterns · ${Object.entries(state.stats || {}).filter(([k,s]) => k.startsWith('GD:') && ((s.correct || 0) + (s.incorrect || 0) > 0)).length} drill questions practised · ${startedSections} / ${sections.length} lessons started`;
}

// -------------------------------------------------------
// STUDY ACTIVITY HEATMAP (same 500/day scale as Vocab/Kanji)
// -------------------------------------------------------
export function renderGrammarActivity() {
  const grid = document.getElementById('grammar-activity-heatmap');
  if (!grid) return;
  const days = getHeatmap30().map(day => {
    const reviews = getDay(day.date).pillars.grammar || 0;
    const level = reviews <= 0 ? 0 : reviews < 50 ? 1 : reviews < 100 ? 2 : reviews < 150 ? 3 : reviews < 200 ? 4 : reviews < 300 ? 5 : reviews < 400 ? 6 : reviews < 500 ? 7 : 8;
    return { date: day.date, count: reviews, level };
  });
  const legendSteps = [[0, '0'], [1, '1-49'], [2, '50-99'], [3, '100-149'], [4, '150-199'], [5, '200-299'], [6, '300-399'], [7, '400-499'], [8, '500+']];
  const legend = `<div class="home-heatmap-legend"><span>0</span>${legendSteps.map(([l, t]) => `<i class="heatmap-cell level-${l}" title="${t} grammar reviews"></i>`).join('')}<span>500+</span></div>`;
  grid.innerHTML = renderHeatmapGridHtml(days).replace(/: (\d+) items/g, ': $1 grammar reviews') + legend;
  const detail = document.getElementById('grammar-activity-detail');
  const grammarDay = date => { const d = getDay(date); return { ...d, reviews: d.pillars.grammar || 0 }; };
  grid.querySelectorAll('.heatmap-cell[data-date]').forEach(cell => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = cell.className;
    button.dataset.date = cell.dataset.date;
    button.title = cell.title;
    button.setAttribute('aria-label', `${cell.dataset.date}: ${cell.dataset.count} grammar reviews. View day details`);
    button.setAttribute('aria-controls', 'grammar-activity-detail');
    button.setAttribute('aria-pressed', 'false');
    button.onclick = () => {
      grid.querySelectorAll('button[data-date]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      if (detail) { detail.hidden = false; detail.innerHTML = renderActivityDayHtml(grammarDay(button.dataset.date)); }
      const hint = document.getElementById('grammar-activity-hint');
      if (hint) hint.hidden = true;
    };
    cell.replaceWith(button);
  });
  if (detail) { detail.hidden = false; detail.innerHTML = renderActivityDayHtml(grammarDay(istDateKey())); }
  const hint = document.getElementById('grammar-activity-hint');
  if (hint) hint.hidden = false;
  const streak = getCurrentStreak(undefined, 'grammar');
  const streakEl = document.getElementById('grammar-review-streak');
  const todayEl = document.getElementById('grammar-reviews-today');
  if (streakEl) streakEl.textContent = streak;
  if (todayEl) todayEl.textContent = getDay(istDateKey()).pillars.grammar || 0;
}

// -------------------------------------------------------
// ONE ENTRY POINT, called by renderGrammarView()
// -------------------------------------------------------
export function renderGrammarLessonArea() {
  if (!state.grammarDB || !(state.grammarDB.index || []).length) return;
  renderGrammarLessonChips();
  updateGrammarActionButtonLabels();
  renderGrammarStatus();
  updateGrammarProgress();
  renderGrammarActivity();
}

if (typeof window !== 'undefined') {
  window.grammarHardOnlyEnabled = () => Boolean(state.grammarHardOnly);
  window.setGrammarLessonGroup = setGrammarLessonGroup;
  window.setGrammarPickerMode = setGrammarPickerMode;
  window.selectGrammarLearnGroup = selectGrammarLearnGroup;
  window.selectGrammarTest = selectGrammarTest;
  window.selectGrammarLesson = selectGrammarLesson;
  window.startGrammarTest = startGrammarTest;
  window.clearGrammarLessonSelection = clearGrammarLessonSelection;
  window.setGrammarSessionSize = setGrammarSessionSize;
  window.toggleGrammarHardOnly = toggleGrammarHardOnly;
  window.startGrammarLearn = startGrammarLearn;
  window.startGrammarPractice = startGrammarPractice;
  window.startNextGrammarBatch = startNextGrammarBatch;
  window.startGrammarPatternTest = startGrammarPatternTest;
  window.startGrammarAgain = startGrammarAgain;
  window.renderGrammarLessonArea = renderGrammarLessonArea;
     }
