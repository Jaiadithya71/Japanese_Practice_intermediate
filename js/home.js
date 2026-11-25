import { renderActivityDayHtml } from './activity-detail.js';
import { getReviewPhase, setReviewPhasePreference } from './review-phase.js';
/* =======================================================
   NIHONGO INTERMEDIATE — home.js
   5-Pillar Dashboard, Simultaneous Progress & Lesson Selection
   ======================================================= */

import { state } from './state.js';
import { peekItemStatus, getDueItemsCount, getVocabDueSummary } from './srs.js?v=20261116-lag1';
import { startStudy, renderCard, startDueReview, startSavedReviewAgain, startSavedReviewAgainAll } from './study.js?v=20261125-ra-absep';
import { loadSavedReviewAgainByLesson } from './review-again-by-lesson.js?v=20261120-retry-by-lesson';
import { grammarSections } from './grammar-lessons.js';
import { getAllAvailableTests, startTestSession } from './test.js?v=20261119-class-tests';
import { getDay, getHeatmap30, getCurrentStreak } from './daylog.js';
import { istDateKey } from './time.js';
import { renderHeatmapGridHtml } from './today.js';
import { beginGistReviewSession } from './gist-sync.js?v=20261120-sync-retry';
import { showView } from './navigation.js';

export function startSingleChapterStudy(chId) {
  state.selectedChapters.clear();
  state.selectedChapters.add(chId);
  startStudy('flashcard', false, 'home');
}
if (typeof window !== 'undefined') window.startSingleChapterStudy = startSingleChapterStudy;

export function renderHomeView() {
  try { state.studyDirection = localStorage.getItem('n3_home_study_direction') || state.studyDirection; } catch (_) {}
  updateMasteryCounters();
  // Home starts with no lesson selected. Learners choose lessons explicitly or use Select All.
  try {
    const ov = document.getElementById('home-include-overlaps');
    if (ov) ov.checked = localStorage.getItem('n3_home_include_overlaps') === '1';
  } catch (_) {}
  renderHomeReviewDue();
  renderHomeSavedReviewAgain();
  renderLessonGrid();
  renderHomeVocabStatus();
  renderHomeActivity();
  updatePillarCards();
  updateHomeLessonControls();
}

export function updateMasteryCounters() {
  let mastered = 0, learning = 0, hard = 0, unseen = 0;
  let total = 0;

  for (const chId in state.vocabDB) {
    for (const w of state.vocabDB[chId]) {
      total++;
      const st = peekItemStatus(homeWordStatusKey(w.id, state.studyDirection));
      if (st === 'mastered') mastered++;
      else if (st === 'hard') hard++;
      else if (st === 'learning') learning++;
      else unseen++;
    }
  }

  const elTotal = document.getElementById('dash-total-words');
  const elMastered = document.getElementById('dash-mastered-words');
  const elLearning = document.getElementById('dash-learning-words');
  const elHard = document.getElementById('dash-hard-words');

  if (elTotal) elTotal.textContent = total;
  if (elMastered) elMastered.textContent = mastered;
  if (elLearning) elLearning.textContent = learning;
  if (elHard) elHard.textContent = hard;
}

export function updatePillarCards() {
  const vocabCount = Object.values(state.vocabDB).reduce((acc, words) => acc + words.length, 0);
  const readingCount = Object.keys(state.readingDB).length;
  const kanjiCount = Object.keys(state.kanjiDB || {}).length;

  const cardV = document.getElementById('pillar-vocab-count');
  const cardR = document.getElementById('pillar-reading-count');
  const cardK = document.getElementById('pillar-kanji-count');

  if (cardV) cardV.textContent = `${vocabCount} words`;
  if (cardR) cardR.textContent = `${readingCount} lessons`;
  const cardG = document.getElementById('pillar-grammar-count');
  const subK = document.getElementById('pillar-kanji-sub');
  if (cardK) cardK.textContent = `${kanjiCount} Kanji`;
  if (subK) subK.textContent = 'N3 target kanji + exercises';
  if (cardG) cardG.textContent = `${(state.grammarDB.index || []).length} patterns`;
}

export function setHomeGroup(group) {
  // The picker is a single Topics sequence now (1-21, C1-C8, R1-R9, K1-K25); the old
  // Characteristics group is folded in, so any 'characteristics' request - or
  // a stale stored value - lands on the merged tab.
  state.activeChapterGroup = 'topic';
  const tabT = document.getElementById('home-tab-topic');
  const tabC = document.getElementById('home-tab-char');
  if (tabT) tabT.classList.add('active');
  if (tabC) tabC.classList.remove('active');
  if (tabT) tabT.setAttribute('aria-selected', 'true');
  if (tabC) tabC.setAttribute('aria-selected', 'false');
  renderLessonGrid();
  updateHomeLessonControls();
}

export function chapterKeysForGroup() {
  // One merged sequence: textbook Topics 1-21, then the Part 2 characteristics
  // lessons shown as C1-C8, then the Reading-sourced lessons shown as R1-R9,
  // then the kanji-book lessons shown as K1-K25 (K number = kanji book lesson).
  // Chapter ids themselves are unchanged so progress, selection persistence
  // and the Test hub keep working.
  const keys = Object.keys(state.vocabDB).filter(k => /^\d+$/.test(k) || k.startsWith('part2_'));
  // Display order: 1-21, C1-C8, R1-R9, K1-K25 (chapter ids unchanged).
  const rank = k => {
    if (k.startsWith('part2_')) return 21 + parseInt(k.slice(6), 10);
    const n = parseInt(k, 10);
    if (n <= 21) return n;
    return n <= 30 ? 30 + (n - 21) : n + 9;
  };
  return keys.sort((a, b) => rank(a) - rank(b));
}

// Live element refs for the picker tiles, keyed by chapter id, so a tap can
// update one tile in place instead of rebuilding all 63 (the per-tap rebuild
// was the lesson-picker lag).
const homeTileEls = new Map();

function homeIncludeOverlapsChecked() {
  return Boolean(document.getElementById('home-include-overlaps')?.checked);
}

export function toggleHomeIncludeOverlaps() {
  try { localStorage.setItem('n3_home_include_overlaps', homeIncludeOverlapsChecked() ? '1' : '0'); } catch (_) {}
  renderLessonGrid();
  updateHomeLessonControls();
}
if (typeof window !== 'undefined') window.toggleHomeIncludeOverlaps = toggleHomeIncludeOverlaps;

// Words drilled for a Home lesson. R (reading) and K (kanji) lessons were
// deduplicated against earlier lessons, so chapter-wise class-test prep can
// miss words; with "All lesson words (incl. overlaps)" on, the lesson's own
// full source list is restored. Overlap entries reuse the original word id,
// so SRS progress stays per-word.
function homeChapterWords(chId) {
  const base = state.vocabDB[chId] || [];
  if (!homeIncludeOverlapsChecked()) return base;
  const extra = (state.vocabLessonOverlaps || {})[chId] || [];
  return extra.length ? base.concat(extra) : base;
}

function homeTileCountText(chId) {
  const words = homeChapterWords(chId);
  if (!homeHardOnlyChecked()) return `${words.length}w`;
  const aSel = state.selectedChapters.has(chId);
  const bSel = state.selectedChapters.has(`${chId}|B`);
  if (aSel || bSel) {
    let n = 0;
    if (aSel) n += homeHardWordCount(words, state.studyDirection);
    if (bSel) n += homeHardWordCount(words, 'kana-en');
    return `${n}w`;
  }
  return `${homeHardWordCount(words, state.studyDirection)}w`;
}

function updateHomeTileSelection(chId) {
  const refs = homeTileEls.get(chId);
  if (!refs) return;
  const aSel = state.selectedChapters.has(chId);
  const bSel = state.selectedChapters.has(`${chId}|B`);
  refs.tile.classList.toggle('selected', aSel || bSel);
  for (const [sel, seg] of [[aSel, refs.segA], [bSel, refs.segB]]) {
    if (!seg) continue;
    seg.classList.toggle('selected', sel);
    seg.setAttribute('aria-pressed', String(sel));
  }
  refs.countEl.textContent = homeTileCountText(chId);
}

export function toggleChapterSelection(chId) {
  if (state.selectedChapters.has(chId)) state.selectedChapters.delete(chId);
  else state.selectedChapters.add(chId);
  updateHomeTileSelection(String(chId).split('|')[0]);
  updateHomeLessonControls();
}

export function selectAllChaptersInGroup() {
  chapterKeysForGroup().forEach(k => state.selectedChapters.add(k));
  chapterKeysForGroup().forEach(k => updateHomeTileSelection(k));
  updateHomeLessonControls();
}

export function clearChapterSelection() {
  // Clear only the visible group's selections; picks made in the other group
  // stay intact for when the user switches back.
  for (const selKey of homeActiveGroupSelKeys()) state.selectedChapters.delete(selKey);
  chapterKeysForGroup().forEach(k => updateHomeTileSelection(k));
  updateHomeLessonControls();
}


function homeActiveGroupSelKeys() {
  // Only selection entries that belong to the group currently shown in the
  // picker. The selection Set is shared across the Topics/Characteristics
  // tabs (and other views write into it too), so entries from the other group
  // must not count toward - or be drilled from - this tab, where they are
  // invisible. Entries are `chId` (part A) or `chId|B` (kana-first part B).
  return Array.from(state.selectedChapters).filter(k => {
    const base = String(k).split('|')[0];
    return base.startsWith('part2_') || /^\d+$/.test(base);
  });
}


function homeWordStatusKey(wordId, direction) {
  // Mirrors getWordStatus keying, but non-mutating (peek) for display counts.
  return `V:${wordId}${direction === 'en-ja' ? ':rev' : (direction === 'kana-en' ? ':kana' : '')}`;
}

function homeHardWordCount(words, direction) {
  let n = 0;
  for (const w of words) if (peekItemStatus(homeWordStatusKey(w.id, direction)) === 'hard') n++;
  return n;
}

function homeHardOnlyChecked() {
  return Boolean(document.getElementById('home-hard-only')?.checked);
}

export function toggleHomeHardOnly() {
  renderLessonGrid();
  updateHomeLessonControls();
}
if (typeof window !== 'undefined') window.toggleHomeHardOnly = toggleHomeHardOnly;

export function renderLessonGrid() {
  const container = document.getElementById('home-lesson-grid');
  if (!container) return;
  // One pass over the word list with non-mutating peeks gives every tile its
  // A and B tallies. The old per-tile filter/some loops ran getWordStatus
  // (which creates a full empty SRS record per unseen word) ~8,800 times per
  // render, polluting state.stats with thousands of placeholder records.
  const counts = {};
  for (const chId of chapterKeysForGroup()) {
    let am = 0, ah = false, bm = 0, bh = false;
    const words = homeChapterWords(chId);
    const aKeySuffix = state.studyDirection === 'en-ja' ? ':rev' : '';
    for (const w of words) {
      const a = peekItemStatus(`V:${w.id}${aKeySuffix}`);
      if (a === 'mastered') am++; else if (a === 'hard') ah = true;
      const b = peekItemStatus(`V:${w.id}:kana`);
      if (b === 'mastered') bm++; else if (b === 'hard') bh = true;
    }
    counts[chId] = { am, ah, bm, bh, total: words.length };
  }
  container.innerHTML = '';
  homeTileEls.clear();
  chapterKeysForGroup().forEach(chId => {
    const meta = state.chapterMetadata[chId] || {};
    const words = state.vocabDB[chId] || [];
    const label = chId.startsWith('part2_')
      ? 'C' + Number(chId.slice(6))
      : (Number(chId) > 30 ? 'K' + (Number(chId) - 30)
        : (Number(chId) > 21 ? 'R' + (Number(chId) - 21) : String(Number(chId))));
    // One compact tile per lesson with small A/B selectors inside, so the
    // list stays short. A: kanji-first (the existing track). B: kana-first -
    // the same words shown by their kana reading, tracked separately from A.
    const parts = [
      { selKey: chId, suffix: 'A', direction: state.studyDirection, partLabel: 'kanji front' },
      { selKey: `${chId}|B`, suffix: 'B', direction: 'kana-en', partLabel: 'かな kana front', segClass: ' home-lesson-ab-seg-b' }
    ];
    const topic = meta.topic_en || meta.topic_ja || label;
    const tile = document.createElement('div');
    tile.className = 'home-lesson-tile home-lesson-tile-ab';
    if (parts.some(part => state.selectedChapters.has(part.selKey))) tile.classList.add('selected');
    const segHtml = [];
    for (const part of parts) {
      const selected = state.selectedChapters.has(part.selKey);
      const c = counts[chId];
      const mastered = part.suffix === 'A' ? c.am : c.bm;
      const hasHard = part.suffix === 'A' ? c.ah : c.bh;
      const allDone = mastered === words.length && words.length;
      segHtml.push(`<button type="button" class="home-lesson-ab-seg${part.segClass || ''}${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${allDone ? ' all-done' : ''}" aria-pressed="${selected}" aria-label="Lesson ${label} part ${part.suffix} (${part.partLabel})${selected ? ', selected' : ''}" title="${topic} part ${part.suffix} (${part.partLabel}) · ${words.length} words · ${mastered} mastered" data-selkey="${part.selKey}">${part.suffix}<span class="home-lesson-ab-dot" aria-hidden="true"></span></button>`);
    }
    tile.innerHTML = `<span class="home-lesson-tile-num">${label}</span><span class="home-lesson-tile-count">${homeTileCountText(chId)}</span><span class="home-lesson-ab">${segHtml.join('')}</span>`;
    const segs = tile.querySelectorAll('.home-lesson-ab-seg');
    segs.forEach(seg => {
      seg.onclick = () => toggleChapterSelection(seg.dataset.selkey);
    });
    homeTileEls.set(chId, { tile, segA: segs[0], segB: segs[1], countEl: tile.querySelector('.home-lesson-tile-count') });
    container.appendChild(tile);
  });
  updateHomeLessonControls();
}

function homeRunSize() {
  try {
    // Apply the new default once on existing devices, then keep later choices.
    if (localStorage.getItem('n3_home_session_size_default_v2') !== 'all') {
      localStorage.setItem('n3_home_session_size', 'all');
      localStorage.setItem('n3_home_session_size_default_v2', 'all');
    }
    const size = localStorage.getItem('n3_home_session_size');
    return ['10', '20', '50', 'all'].includes(size) ? size : 'all';
  } catch (_) { return 'all'; }
}

export function setHomeSessionSize(value) {
  const allowed = ['10', '20', '50', 'all'];
  const selected = allowed.includes(String(value).toLowerCase()) ? String(value).toLowerCase() : 'all';
  try { localStorage.setItem('n3_home_session_size', selected); } catch (_) {}
  updateHomeLessonControls();
}

export function setHomeStudyDirection(direction) {
  if (direction !== 'ja-en' && direction !== 'en-ja') return;
  state.studyDirection = direction;
  try { localStorage.setItem('n3_home_study_direction', direction); } catch (_) {}
  renderLessonGrid();
}

export function setHomeReviewPhase(phase) {
  setReviewPhasePreference(phase);
  updateHomeLessonControls();
}

function updateHomeLessonControls() {
  const phase = getReviewPhase();
  document.querySelectorAll('#home-review-phase button').forEach(button => {
    button.setAttribute('aria-pressed', String(button.dataset.phase === phase));
  });
  const phaseHint = document.getElementById('home-review-phase-hint');
  if (phaseHint) phaseHint.textContent = phase === 'learn' ? 'Reading, meaning & examples. No grading.' : 'Recall first, then reveal and grade.';

  const selKeys = homeActiveGroupSelKeys();
  // With "Drill hard words only" on, the pool is just the hard words the drill
  // will draw (same per-part filter as startSelectedLessonRun); otherwise the
  // normal full count. Each selected part (A and B) contributes the chapter's
  // words, matching the cards the run actually draws.
  let wordCount;
  if (homeHardOnlyChecked()) {
    wordCount = 0;
    for (const selKey of selKeys) {
      const kanaFirst = selKey.endsWith('|B');
      const chapter = kanaFirst ? selKey.slice(0, -2) : selKey;
      wordCount += homeHardWordCount(homeChapterWords(chapter), kanaFirst ? 'kana-en' : state.studyDirection);
    }
  } else {
    wordCount = selKeys.reduce((sum, selKey) => sum + homeChapterWords(String(selKey).split('|')[0]).length, 0);
  }
  const lessonCount = new Set(selKeys.map(k => String(k).split('|')[0])).size;
  const summary = document.getElementById('home-lessons-count');
  if (summary) summary.textContent = lessonCount
    ? `${lessonCount} lesson${lessonCount === 1 ? '' : 's'} selected · ${wordCount.toLocaleString()} words in pool`
    : '0 lessons selected';
  const size = document.querySelector('[aria-label="Session size"]');
  if (size) size.value = homeRunSize();
  const direction = document.querySelector('[aria-label="Study direction"]');
  if (direction) direction.value = state.studyDirection;
  const topic = document.getElementById('home-tab-topic');
  if (topic) topic.textContent = `Topics · ${Object.keys(state.vocabDB).filter(k => /^\d+$/.test(k) || k.startsWith('part2_')).length || 38}`;
  const canStart = selKeys.length > 0;
  const flashcards = document.getElementById('btn-start-selected-study');
  const tests = document.getElementById('btn-start-selected-test');
  if (flashcards) flashcards.disabled = !canStart;
  if (tests) tests.disabled = !canStart;
}

export function startSelectedLessonTestRun() {
  const selected = new Set(homeActiveGroupSelKeys());
  if (!selected.size) { alert('Select at least one lesson first.'); return null; }
  const baseIds = new Set(Array.from(selected, k => String(k).split('|')[0]));
  const tests = getAllAvailableTests().filter(test => test.pillar === 'vocab' && test.category !== 'vocab_reviews' && test.category !== 'mock_exams' && baseIds.has(String(test.id).replace(/^vocab-/, '')));
  const questions = tests.flatMap(test => test.questions || []).filter(question =>
    Array.isArray(question.options) && question.options.length >= 2 &&
    Number.isInteger(question.correct) && question.correct >= 1 && question.correct <= question.options.length);
  if (!questions.length) { alert('No multiple-choice tests are available for these lessons.'); return null; }
  // The test runner is inside the Test view, not the Home lesson picker.
  showView('test');
  return startTestSession('home-vocab-selected', { id: 'home-vocab-selected', category: 'vocab_topics', catLabel: 'Vocabulary Lessons', badgeClass: 'badge-n4', title: `${selected.size} selected lessons`, subTitle: 'Selected textbook lessons', pillar: 'vocab', questionCount: questions.length, questions });
}

function startHomeBatch() {
  const queue = state.homeRunQueue || [];
  if (!queue.length) return;
  const batchSize = state.homeRunBatchSize === 'all' ? queue.length : Number(state.homeRunBatchSize) || 20;
  const batch = queue.splice(0, batchSize);
  state.homeRunQueue = queue;
  state.homeRunBatchRun = true;
  state.studyMode = 'flashcard';
  state.studyIsDrillHard = false;
  state.drillOrigin = 'home';
  state.isDueReviewMode = false;
  state.learnUnit = null;
  state.sessionItems = batch;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = batch.length;
  state.sessionTotal = batch.length;
  state.cardFlipped = false;
  beginGistReviewSession();
  showView('study');
  renderCard();
}

export function startSelectedLessonRun() {
  const chapters = homeActiveGroupSelKeys();
  if (!chapters.length) { alert('Select at least one lesson first.'); return; }
  const pool = [];
  const seenKeys = new Set();
  for (const selKey of chapters) {
    const kanaFirst = selKey.endsWith('|B');
    const chapter = kanaFirst ? selKey.slice(0, -2) : selKey;
    for (const word of homeChapterWords(chapter)) {
      if (document.getElementById('home-hard-only')?.checked && peekItemStatus(homeWordStatusKey(word.id, kanaFirst ? 'kana-en' : state.studyDirection)) !== 'hard') continue;
      const key = kanaFirst ? `V:${word.id}:kana` : `V:${word.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
      if (seenKeys.has(key)) continue; // overlap word already in the pool via its original lesson
      seenKeys.add(key);
      pool.push({ ...word, type: 'vocab', key, book: 'vocab', kanaFirst });
    }
  }
  if (!pool.length) { alert('No vocabulary items found in this selection.'); return; }
  pool.sort(() => Math.random() - 0.5);
  state.homeRunBatchSize = homeRunSize();
  state.homeRunQueue = pool;
  startHomeBatch();
}

export function startNextHomeBatch() {
  if (!state.homeRunQueue || !state.homeRunQueue.length) return;
  startHomeBatch();
}

export function renderHomeActivity() {
  const grid = document.getElementById('home-activity-heatmap');
  if (!grid) return;
  const byDate = new Map(getHeatmap30().map(day => [day.date, day]));
  const reviewsOnly = Array.from(byDate.values(), day => {
    const reviews = getDay(day.date).reviews;
    const level = reviews <= 0 ? 0 : reviews < 50 ? 1 : reviews < 100 ? 2 : reviews < 150 ? 3 : reviews < 200 ? 4 : reviews < 300 ? 5 : reviews < 400 ? 6 : reviews < 500 ? 7 : 8;
    return { date: day.date, count: reviews, level };
  });
  // Reuse the existing 30-day layout while preserving this card's reviews-only scale.
  const html = renderHeatmapGridHtml(reviewsOnly).replace(/: (\d+) items/g, ': $1 reviews');
  grid.innerHTML = html + `<div class="home-heatmap-legend"><span>0</span><i class="heatmap-cell level-0" title="0 reviews"></i><i class="heatmap-cell level-1" title="1-49 reviews"></i><i class="heatmap-cell level-2" title="50-99 reviews"></i><i class="heatmap-cell level-3" title="100-149 reviews"></i><i class="heatmap-cell level-4" title="150-199 reviews"></i><i class="heatmap-cell level-5" title="200-299 reviews"></i><i class="heatmap-cell level-6" title="300-399 reviews"></i><i class="heatmap-cell level-7" title="400-499 reviews"></i><i class="heatmap-cell level-8" title="500+ reviews"></i><span>500+</span></div>`;
  const detail = document.getElementById('home-activity-detail');
  grid.querySelectorAll('.heatmap-cell[data-date]').forEach(cell => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = cell.className;
    button.dataset.date = cell.dataset.date;
    button.title = cell.title;
    button.setAttribute('aria-label', `${cell.dataset.date}: ${cell.dataset.count} reviews. View day details`);
    button.setAttribute('aria-controls', 'home-activity-detail');
    button.setAttribute('aria-pressed', 'false');
    button.onclick = () => {
      grid.querySelectorAll('button[data-date]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      if (detail) {
        detail.hidden = false;
        detail.innerHTML = renderActivityDayHtml(getDay(button.dataset.date));
      }
      const hint = document.getElementById('home-activity-hint');
      if (hint) hint.hidden = true;
    };
    cell.replaceWith(button);
  });
  if (detail) { detail.hidden = false; detail.innerHTML = renderActivityDayHtml(getDay(istDateKey())); }
  const hint = document.getElementById('home-activity-hint');
  if (hint) hint.hidden = false;
  const streak = document.getElementById('home-review-streak');
  const today = document.getElementById('home-reviews-today');
  if (streak) streak.textContent = getCurrentStreak();
  if (today) today.textContent = getDay(istDateKey()).reviews;
}


/* Compact vocab status above Study activity. A (meaning/kanji front) and B (kana front,
   :kana keys) are counted separately per word; nothing is merged or written. */
export function renderHomeVocabStatus() {
  const el = document.getElementById('hvs-rows');
  if (!el) return;
  const tracks = [['A', state.studyDirection, 'Part A'], ['B', 'kana-en', 'Part B \u00b7 kana']];
  el.innerHTML = tracks.map(([id, dir, label]) => {
    const c = { mastered: 0, learning: 0, hard: 0, unseen: 0 };
    let total = 0;
    for (const chId in state.vocabDB) for (const w of state.vocabDB[chId]) {
      total++;
      const st = peekItemStatus(homeWordStatusKey(w.id, dir));
      c[st === 'mastered' || st === 'hard' || st === 'learning' ? st : 'unseen']++;
    }
    const pct = n => (total ? (n / total) * 100 : 0).toFixed(2);
    const seg = k => `<span class="hvs-seg hvs-${k}" style="width:${pct(c[k])}%"></span>`;
    return `<div class="hvs-row" aria-label="${label}: ${c.mastered} mastered, ${c.learning} learning, ${c.hard} hard, ${c.unseen} new of ${total}">
      <div class="hvs-label">${label}</div>
      <div class="hvs-main"><div class="hvs-bar">${seg('mastered')}${seg('learning')}${seg('hard')}</div>
      <div class="hvs-counts"><span class="hvs-mastered"><b>${c.mastered}</b> mastered</span><span class="hvs-learning"><b>${c.learning}</b> learning</span><span class="hvs-hard"><b>${c.hard}</b> hard</span><span class="hvs-unseen"><b>${c.unseen}</b> new</span></div></div>
    </div>`;
  }).join('');
}

/* =======================================================
   Home "Review due" entry (2026-11-15, his ask):
   one compact bar - due count, per-pillar breakdown, Start - plus a
   collapsible lesson grid (elementary-app pattern) that doubles as the
   review lesson picker. Selection and grid open state are remembered.
   The grid lists only lessons with due cards (his 14:17 ask; the full
   list is the Select lessons section below), plus any still-picked
   lesson so it can be unpicked; a picked lesson with nothing due is said out
   loud on the bar ("0 due in picked lessons") and Start stays off rather
   than failing silently. Vocab chapters 31-55 are the kanji-book lessons
   (K1-K25) and also filter kanji-pillar due for the matching kanji
   lesson. Reading and grammar due cards have no lesson picker here and
   stay in every round, so the count on the bar always equals the cards
   Start will serve.
   ======================================================= */
const HRD_SEL_KEY = 'n3_home_review_lessons';
const HRD_PILLAR = 'vocab';
const HRD_OPEN_KEY = 'n3_home_review_grid_open';
const HRD_PART_KEY = 'n3_home_review_part';

// Global A / B / Both switch (his 14:35 ask: "Yes, but let's not make it
// lesson wise"). A = kanji-front cards, B = kana-front cards, Both = both.
// One switch for the whole box: it filters the due count, the chips' counts
// and the round, so the bar count always equals the cards Start serves.
function homeReviewPart() {
  try {
    const p = localStorage.getItem(HRD_PART_KEY);
    return (p === 'A' || p === 'B') ? p : 'both';
  } catch (_) { return 'both'; }
}

function homeReviewPartOpts() {
  const p = homeReviewPart();
  // uncapped: Review due runs every due card (no batch size, no catch-up cap)
  return p === 'both' ? { uncapped: true } : { part: p, uncapped: true };
}

export function setHomeReviewPart(part) {
  try { localStorage.setItem(HRD_PART_KEY, (part === 'A' || part === 'B') ? part : 'both'); } catch (_) {}
  renderHomeReviewDue();
}
if (typeof window !== 'undefined') window.setHomeReviewPart = setHomeReviewPart;

function homeReviewSelection() {
  try {
    const arr = JSON.parse(localStorage.getItem(HRD_SEL_KEY) || '[]');
    return new Set(Array.isArray(arr) ? arr.map(String) : []);
  } catch (_) { return new Set(); }
}

function saveHomeReviewSelection(sel) {
  try { localStorage.setItem(HRD_SEL_KEY, JSON.stringify([...sel])); } catch (_) {}
}

function homeReviewEffectiveFilter(sel) {
  if (!sel.size) return null;
  // Words only (his 14:18 ask): vocab chapters, K1-K25 included. To bring
  // kanji/reading/grammar back, set HRD_PILLAR to 'all' and restore the
  // kanji/grammar additions from commit 2931060.
  return new Set(sel);
}

export function renderHomeReviewDue() {
  const root = document.getElementById('home-review-due');
  if (!root || !state.stats) return;
  let sel = homeReviewSelection();
  const part = homeReviewPart();
  const partOpts = part === 'both' ? {} : { part };
  const summary = getVocabDueSummary(partOpts);
  const total = summary.total;

  const partWrap = document.getElementById('hrd-part');
  if (partWrap) {
    partWrap.querySelectorAll('button[data-part]').forEach(b => {
      b.classList.toggle('selected', b.dataset.part === part);
    });
  }

  // Per-lesson due counts, computed once for the bar and the grid. Vocab
  // chapters 31-55 (K1-K25) also count kanji-pillar due for their kanji lesson.
  const keys = chapterKeysForGroup();
  const dueMap = {};
  for (const chId of keys) {
    const n = Number(chId);
    const due = (summary.byChapter.get(String(chId)) || 0) + summary.unassigned;
    dueMap[chId] = due;
  }

  // Drop picked lessons that have nothing due left (e.g. right after their
  // review round), so the box never comes back showing 0 on the picked chips;
  // with no picks left it returns to the All view.
  if (sel.size) {
    const kept = new Set([...sel].filter(chId => (dueMap[chId] || 0) > 0));
    if (kept.size !== sel.size) {
      sel = kept;
      saveHomeReviewSelection(kept);
    }
  }

  const filter = homeReviewEffectiveFilter(sel);
  const count = filter ? summary.unassigned + [...filter].reduce((n, ch) => n + (summary.byChapter.get(String(ch)) || 0), 0) : total;
  let pickedDue = 0;
  for (const chId of sel) pickedDue += dueMap[chId] || 0;

  const countEl = document.getElementById('hrd-count');
  const startBtn = document.getElementById('hrd-start');
  const breakdownEl = document.getElementById('hrd-breakdown');
  if (countEl) countEl.textContent = count;
  if (startBtn) {
    startBtn.disabled = count === 0;
    startBtn.classList.toggle('hrd-caught-up', total === 0);
  }
  if (breakdownEl) {
    if (total === 0) {
      breakdownEl.textContent = part === 'both' ? 'All caught up' : 'No ' + part + ' cards due';
    } else if (filter && pickedDue === 0 && count === 0) {
      // Picked lessons have nothing due and there is no always-included
      // grammar/reading due either: say so instead of letting Start fail
      // (startDueReview would only alert).
      breakdownEl.textContent = '0 due in picked lesson' + (sel.size === 1 ? '' : 's') + ' · ' + total + ' due elsewhere';
    } else if (filter && pickedDue === 0) {
      // Nothing due in the picked lessons. Due grammar/reading cards stay
      // in every round, so the button count may still be non-zero; the hint
      // line under the grid says they are always included.
      breakdownEl.textContent = '0 due in picked lesson' + (sel.size === 1 ? '' : 's');
    } else if (filter) {
      breakdownEl.textContent = count + ' of ' + total + ' due · ' + sel.size + ' lesson' + (sel.size === 1 ? '' : 's');
    } else {
      breakdownEl.textContent = total + ' word' + (total === 1 ? '' : 's') + ' due' + (part === 'both' ? '' : ' · ' + part);
    }
  }

  const wrap = document.getElementById('hrd-grid-wrap');
  const toggle = document.getElementById('hrd-toggle');
  let open = false;
  try { open = localStorage.getItem(HRD_OPEN_KEY) === '1'; } catch (_) {}
  if (wrap) wrap.hidden = !open;
  if (toggle) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.classList.toggle('open', open);
  }
  if (!open) return;

  const grid = document.getElementById('hrd-grid');
  if (!grid) return;
  const chips = [];
  chips.push('<button type="button" class="due-chip' + (sel.size === 0 ? ' selected' : '') + '" onclick="window.clearHomeReviewLessons()">All<span class="due-chip-count">' + total + '</span></button>');
  for (const chId of keys) {
    const n = Number(chId);
    const due = dueMap[chId];
    const isSel = sel.has(chId);
    if (!due) continue; // box lists only lessons with due cards; picked lessons with 0 left were already unpicked above
    const label = chId.startsWith('part2_') ? 'C' + Number(chId.slice(6))
      : (n > 30 ? 'K' + (n - 30) : (n > 21 ? 'R' + (n - 21) : String(n)));
    const topic = (state.chapterMetadata[chId] || {}).topic_en || '';
    const cls = 'due-chip' + (isSel ? ' selected' : '') + (due ? ' has-due' : ' no-due');
    chips.push('<button type="button" class="' + cls + '" title="' + (topic ? topic.replace(/&/g, '&amp;').replace(/"/g, '&quot;') + ' · ' : '') + due + ' due" onclick="window.toggleHomeReviewLesson(\'' + chId + '\')">' + label + '<span class="due-chip-count">' + due + '</span></button>');
  }
  grid.innerHTML = chips.join('');
}

const HRA_OPEN_KEY = 'n3_home_review_again_open';

// A = kanji-front word (V:<id>), B = kana-front (V:<id>:kana); other key
// shapes (collocations, :rev) belong to neither and count toward both views.
function hraPartMatch(key, part) {
  if (part !== 'A' && part !== 'B') return true;
  const isV = key.startsWith('V:') && !key.endsWith(':rev');
  const isB = isV && key.endsWith(':kana');
  return part === 'A' ? (isV && !isB) : isB;
}

export function renderHomeSavedReviewAgain() {
  const due = document.getElementById('home-review-due');
  if (!due) return;
  let section = document.getElementById('home-review-again-saved');
  const saved = loadSavedReviewAgainByLesson();
  const entries = Object.entries(saved)
    .filter(([, value]) => Array.isArray(value?.items) && value.items.length)
    .sort((a, b) => Number(b[1].updatedAt || 0) - Number(a[1].updatedAt || 0));
  if (!entries.length) { section?.remove(); return; }
  if (!section) {
    section = document.createElement('section');
    section.id = 'home-review-again-saved';
    section.className = 'home-review-again-saved';
    section.setAttribute('aria-label', 'Saved words to review again');
    due.before(section);
  }
  section.replaceChildren();
  const totalWords = entries.reduce((sum, [, entry]) => sum + entry.items.length, 0);

  const row = document.createElement('div');
  row.className = 'hra-row';
  const start = document.createElement('button');
  start.type = 'button';
  start.className = 'hra-start';
  start.innerHTML = '<i class="fa-solid fa-rotate-left"></i><span>Review again</span><strong class="hra-count"></strong>';
  start.querySelector('.hra-count').textContent = totalWords;
  start.title = 'Retry everything saved, all lessons together';
  start.addEventListener('click', () => startSavedReviewAgainAll());
  const breakdown = document.createElement('span');
  breakdown.className = 'hra-breakdown';
  breakdown.textContent = entries.length + ' lesson' + (entries.length === 1 ? '' : 's') + ' saved';
  let open = false;
  try { open = localStorage.getItem(HRA_OPEN_KEY) === '1'; } catch (_) {}
  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'hra-toggle' + (open ? ' open' : '');
  toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  toggle.setAttribute('aria-label', 'Show saved lessons');
  toggle.innerHTML = 'Lessons <i class="fa-solid fa-chevron-down"></i>';
  toggle.addEventListener('click', () => {
    let now = false;
    try {
      now = localStorage.getItem(HRA_OPEN_KEY) !== '1';
      localStorage.setItem(HRA_OPEN_KEY, now ? '1' : '0');
    } catch (_) {}
    renderHomeSavedReviewAgain();
  });
  row.append(start, breakdown, toggle);
  section.append(row);
  if (!open) return;
  const list = document.createElement('div');
  list.className = 'hra-list';
  section.append(list);
  const grid = document.createElement('div');
  grid.className = 'home-lesson-grid';
  list.append(grid);
  const dueA = getVocabDueSummary({ part: 'A' }).byChapter;
  const dueB = getVocabDueSummary({ part: 'B' }).byChapter;
  const age = ts => {
    if (!ts) return 'saved earlier';
    const mins = Math.max(0, Math.round((Date.now() - ts) / 60000));
    if (mins < 60) return `${mins}m ago`;
    const hours = Math.round(mins / 60);
    if (hours < 48) return `${hours}h ago`;
    return `${Math.round(hours / 24)}d ago`;
  };
  for (const [chapter, entry] of entries) {
    const n = Number(chapter);
    const label = chapter.startsWith('part2_') ? 'C' + Number(chapter.slice(6))
      : n > 30 ? 'K' + (n - 30) : n > 21 ? 'R' + (n - 21) : String(n || chapter);
    const a = dueA.get(String(chapter)) || 0;
    const b = dueB.get(String(chapter)) || 0;
    const aSaved = entry.items.filter(it => hraPartMatch(it?.key || '', 'A')).length;
    const bSaved = entry.items.filter(it => hraPartMatch(it?.key || '', 'B')).length;
    const bits = [`${entry.items.length} saved (A ${aSaved} \u00b7 B ${bSaved})`];
    if (a + b > 0) bits.push(`${a + b} due today (A ${a} \u00b7 B ${b})`);
    bits.push(age(entry.updatedAt));
    // One full-size box per lesson part, both always visible (2026-11-25, his
    // ask: "make them separate boxes - the A and B").
    for (const [part, partCount] of [['A', aSaved], ['B', bSaved]]) {
      const tile = document.createElement('button');
      tile.type = 'button';
      tile.className = 'home-lesson-tile hra-tile-part';
      tile.disabled = partCount === 0;
      tile.title = bits.join(' \u00b7 ') + ` \u00b7 retry lesson ${label} part ${part} (${part === 'A' ? 'kanji front' : 'kana front'})`;
      tile.setAttribute('aria-label', tile.title);
      const num = document.createElement('span');
      num.className = 'home-lesson-tile-num';
      num.textContent = label;
      const partEl = document.createElement('span');
      partEl.className = 'hra-part-label ' + (part === 'A' ? 'hra-part-a' : 'hra-part-b');
      partEl.textContent = part;
      const count = document.createElement('span');
      count.className = 'home-lesson-tile-count';
      count.textContent = partCount + ' saved';
      tile.append(num, partEl, count);
      tile.addEventListener('click', () => startSavedReviewAgain(chapter, { part }));
      grid.append(tile);
    }
  }
  const hint = document.createElement('p');
  hint.className = 'hrd-grid-hint';
  hint.textContent = 'A = kanji front, B = kana front. Tap a box to retry that part of that lesson; the gold button retries everything together.';
  list.append(hint);
}

export function toggleHomeReviewLesson(chId) {
  const sel = homeReviewSelection();
  chId = String(chId);
  if (sel.has(chId)) sel.delete(chId); else sel.add(chId);
  saveHomeReviewSelection(sel);
  renderHomeReviewDue();
}
if (typeof window !== 'undefined') window.toggleHomeReviewLesson = toggleHomeReviewLesson;

export function clearHomeReviewLessons() {
  saveHomeReviewSelection(new Set());
  renderHomeReviewDue();
}
if (typeof window !== 'undefined') window.clearHomeReviewLessons = clearHomeReviewLessons;

export function toggleHomeReviewGrid() {
  let open = false;
  try {
    open = localStorage.getItem(HRD_OPEN_KEY) !== '1';
    localStorage.setItem(HRD_OPEN_KEY, open ? '1' : '0');
  } catch (_) {}
  renderHomeReviewDue();
}
if (typeof window !== 'undefined') window.toggleHomeReviewGrid = toggleHomeReviewGrid;

export function startHomeDueReview() {
  const sel = homeReviewSelection();
  const filter = homeReviewEffectiveFilter(sel);
  startDueReview(HRD_PILLAR, filter || new Set(), homeReviewPartOpts());
}
if (typeof window !== 'undefined') window.startHomeDueReview = startHomeDueReview;
