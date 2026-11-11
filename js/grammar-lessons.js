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

export function selectGrammarLesson(secId, mode = 'toggle') {
  ensureSelectionState();
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
  state.grammarSelectedSections.clear();
  state.grammarSelectionEmpty = true;
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
  const { secs, patterns, drills } = lessonPool();
  const lessonCount = secs.length;
  const summary = document.getElementById('grammar-picker-summary');
  if (summary) {
    summary.textContent = state.grammarSelectionEmpty
      ? 'Choose a lesson to begin'
      : `${lessonCount} ${lessonCount === 1 ? 'lesson' : 'lessons'} selected · ${patterns.length} patterns · ${drills.length} drill questions${state.grammarHardOnly ? ' · hard only' : ''}`;
  }
  const hint = document.getElementById('grammar-start-hint');
  if (hint) {
    hint.textContent = state.grammarSelectionEmpty
      ? 'Tap a lesson tile above. The groups follow the three source exercise sets.'
      : secs.map(sec => sec.titlePlain).join(' · ') + (!patterns.length && drills.length ? ' · Drill-only lesson: use Start practice.' : '');
  }
  const learnBtn = document.getElementById('btn-grammar-learn');
  if (learnBtn) learnBtn.disabled = patterns.length === 0;
  const practiceBtn = document.getElementById('btn-grammar-practice');
  if (practiceBtn) practiceBtn.disabled = drills.length === 0;
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

export function startGrammarLearn() {
  const { patterns } = lessonPool();
  if (patterns.length === 0) {
    alert(state.grammarHardOnly ? 'No hard patterns in the selected lessons!' : 'Select at least one lesson first.');
    return;
  }
  // Book order: lesson by lesson, pattern by pattern.
  const items = patterns.map(({ sec, pattern }) => ({
    ...pattern,
    type: 'grammar',
    book: 'grammar',
    key: `G:${pattern.id}`,
    sectionLabel: sec.titlePlain,
    reviewPhase: 'test', learnNew: true, learned: false
  }));
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

export function startNextGrammarBatch() {
  if (state.grammarRunQueue?.length) beginGrammarSession([], state.grammarLastRun, true);
}

export function startGrammarAgain() {
  if (state.grammarLastRun === 'practice') startGrammarPractice();
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
  window.selectGrammarLesson = selectGrammarLesson;
  window.clearGrammarLessonSelection = clearGrammarLessonSelection;
  window.setGrammarSessionSize = setGrammarSessionSize;
  window.toggleGrammarHardOnly = toggleGrammarHardOnly;
  window.startGrammarLearn = startGrammarLearn;
  window.startGrammarPractice = startGrammarPractice;
  window.startNextGrammarBatch = startNextGrammarBatch;
  window.startGrammarAgain = startGrammarAgain;
  window.renderGrammarLessonArea = renderGrammarLessonArea;
}
