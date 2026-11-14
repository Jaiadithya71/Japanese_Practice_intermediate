import { renderActivityDayHtml } from './activity-detail.js?v=4';
import { getReviewPhase, setReviewPhasePreference } from './review-phase.js';
/* =======================================================
   NIHONGO INTERMEDIATE — home.js
   5-Pillar Dashboard, Simultaneous Progress & Lesson Selection
   ======================================================= */

import { state } from './state.js';
import { getWordStatus, peekItemStatus } from './srs.js';
import { startStudy, renderCard } from './study.js?v=4.5';
import { getAllAvailableTests, startTestSession } from './test.js';
import { getDay, getHeatmap30, getCurrentStreak } from './daylog.js';
import { istDateKey } from './time.js';
import { renderHeatmapGridHtml } from './today.js';
import { beginGistReviewSession } from './gist-sync.js';
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
  if (!state.homePickerInitialized) {
    // Suggested first step for brand-new sessions, Topics tab only - adding it
    // while another group is showing would be an invisible selection.
    if (!state.selectedChapters.size && state.activeChapterGroup === 'topic' && state.vocabDB['01']) state.selectedChapters.add('01');
    state.homePickerInitialized = true;
  }
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
      const st = getWordStatus(w.id, state.studyDirection);
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

export function toggleChapterSelection(chId) {
  if (state.selectedChapters.has(chId)) state.selectedChapters.delete(chId);
  else state.selectedChapters.add(chId);
  renderLessonGrid();
  updateHomeLessonControls();
}

export function selectAllChaptersInGroup() {
  chapterKeysForGroup().forEach(k => state.selectedChapters.add(k));
  renderLessonGrid();
  updateHomeLessonControls();
}

export function clearChapterSelection() {
  // Clear only the visible group's selections; picks made in the other group
  // stay intact for when the user switches back.
  for (const selKey of homeActiveGroupSelKeys()) state.selectedChapters.delete(selKey);
  renderLessonGrid();
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
  container.innerHTML = '';
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
      const mastered = words.filter(w => getWordStatus(w.id, part.direction) === 'mastered').length;
      const hasHard = words.some(w => getWordStatus(w.id, part.direction) === 'hard');
      const allDone = mastered === words.length && words.length;
      segHtml.push(`<button type="button" class="home-lesson-ab-seg${part.segClass || ''}${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${allDone ? ' all-done' : ''}" aria-pressed="${selected}" aria-label="Lesson ${label} part ${part.suffix} (${part.partLabel})${selected ? ', selected' : ''}" title="${topic} part ${part.suffix} (${part.partLabel}) · ${words.length} words · ${mastered} mastered" data-selkey="${part.selKey}">${part.suffix}<span class="home-lesson-ab-dot" aria-hidden="true"></span></button>`);
    }
    // With "Drill hard words only" on, the tile count shows how many words the
    // drill would actually draw from this lesson (per selected A/B part, like
    // the pool); unselected lessons show the count for the current direction.
    let tileCount = words.length;
    if (homeHardOnlyChecked()) {
      const picked = parts.filter(part => state.selectedChapters.has(part.selKey));
      tileCount = picked.length
        ? picked.reduce((sum, part) => sum + homeHardWordCount(words, part.direction), 0)
        : homeHardWordCount(words, state.studyDirection);
    }
    tile.innerHTML = `<span class="home-lesson-tile-num">${label}</span><span class="home-lesson-tile-count">${tileCount}w</span><span class="home-lesson-ab">${segHtml.join('')}</span>`;
    tile.querySelectorAll('.home-lesson-ab-seg').forEach(seg => {
      seg.onclick = () => toggleChapterSelection(seg.dataset.selkey);
    });
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
      wordCount += homeHardWordCount(state.vocabDB[chapter] || [], kanaFirst ? 'kana-en' : state.studyDirection);
    }
  } else {
    wordCount = selKeys.reduce((sum, selKey) => sum + (state.vocabDB[String(selKey).split('|')[0]] || []).length, 0);
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
  for (const selKey of chapters) {
    const kanaFirst = selKey.endsWith('|B');
    const chapter = kanaFirst ? selKey.slice(0, -2) : selKey;
    for (const word of (state.vocabDB[chapter] || [])) {
      if (document.getElementById('home-hard-only')?.checked && getWordStatus(word.id, kanaFirst ? 'kana-en' : state.studyDirection) !== 'hard') continue;
      const key = kanaFirst ? `V:${word.id}:kana` : `V:${word.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
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
      const st = getWordStatus(w.id, dir);
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
