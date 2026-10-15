import { renderActivityDayHtml } from './activity-detail.js?v=2';
import { getReviewPhase, setReviewPhasePreference } from './review-phase.js';
/* =======================================================
   NIHONGO INTERMEDIATE — home.js
   5-Pillar Dashboard, Simultaneous Progress & Lesson Selection
   ======================================================= */

import { state } from './state.js';
import { getWordStatus } from './srs.js';
import { startStudy, renderCard } from './study.js?v=3.4';
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
    if (!state.selectedChapters.size && state.vocabDB['01']) state.selectedChapters.add('01');
    state.homePickerInitialized = true;
  }
  renderLessonGrid();
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
  state.activeChapterGroup = group;
  const tabT = document.getElementById('home-tab-topic');
  const tabC = document.getElementById('home-tab-char');
  if (tabT) tabT.classList.toggle('active', group === 'topic');
  if (tabC) tabC.classList.toggle('active', group === 'characteristics');
  if (tabT) tabT.setAttribute('aria-selected', String(group === 'topic'));
  if (tabC) tabC.setAttribute('aria-selected', String(group === 'characteristics'));
  renderLessonGrid();
  updateHomeLessonControls();
}

export function chapterKeysForGroup() {
  const isChar = state.activeChapterGroup !== 'topic';
  const keys = Object.keys(state.vocabDB).filter(k => { const isCharacteristics = k.startsWith('part2_'); return isCharacteristics === isChar && (isCharacteristics || /^\d+$/.test(k)); });
  const rank = k => (k.startsWith('review_') ? 1000 + parseInt(k.slice(7), 10) : parseInt(k.replace('part2_', ''), 10));
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
  state.selectedChapters.clear();
  renderLessonGrid();
  updateHomeLessonControls();
}

function textbookChapterKeys() {
  return Object.keys(state.vocabDB).filter(k => /^\d+$/.test(k) || k.startsWith('part2_'));
}
function homeSelectedChapterKeys() {
  return state.selectedChapters.size ? Array.from(state.selectedChapters) : textbookChapterKeys();
}

export function renderLessonGrid() {
  const container = document.getElementById('home-lesson-grid');
  if (!container) return;
  container.innerHTML = '';
  chapterKeysForGroup().forEach(chId => {
    const meta = state.chapterMetadata[chId] || {};
    const words = state.vocabDB[chId] || [];
    const selected = state.selectedChapters.has(chId);
    const mastered = words.filter(w => getWordStatus(w.id, state.studyDirection) === 'mastered').length;
    const hasHard = words.some(w => getWordStatus(w.id, state.studyDirection) === 'hard');
    const label = String(Number(chId.startsWith('part2_') ? chId.slice(6) : chId));
    const tile = document.createElement('button');
    tile.type = 'button';
    tile.className = `home-lesson-tile${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${mastered === words.length && words.length ? ' all-done' : ''}`;
    tile.setAttribute('aria-pressed', String(selected));
    tile.title = `${meta.topic_en || meta.topic_ja || label} · ${words.length} words · ${mastered} mastered`;
    tile.innerHTML = `<span class="home-lesson-tile-num">${label}</span><span class="home-lesson-tile-count">${words.length}w</span><span class="home-lesson-tile-dot" aria-hidden="true"></span>`;
    tile.onclick = () => toggleChapterSelection(chId);
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

  const chapters = homeSelectedChapterKeys();
  const wordCount = chapters.reduce((sum, id) => sum + (state.vocabDB[id] || []).length, 0);
  const summary = document.getElementById('home-lessons-count');
  if (summary) summary.textContent = state.selectedChapters.size
    ? `${state.selectedChapters.size} lesson${state.selectedChapters.size === 1 ? '' : 's'} selected · ${wordCount.toLocaleString()} words in pool`
    : '0 lessons selected';
  const size = document.querySelector('[aria-label="Session size"]');
  if (size) size.value = homeRunSize();
  const direction = document.querySelector('[aria-label="Study direction"]');
  if (direction) direction.value = state.studyDirection;
  const topic = document.getElementById('home-tab-topic');
  const characteristic = document.getElementById('home-tab-char');
  if (topic) topic.textContent = `Topics · ${Object.keys(state.vocabDB).filter(k => /^\d+$/.test(k)).length || 21}`;
  if (characteristic) characteristic.textContent = `Characteristics · ${Object.keys(state.vocabDB).filter(k => k.startsWith('part2_')).length || 8}`;
  const canStart = state.selectedChapters.size > 0;
  const flashcards = document.getElementById('btn-start-selected-study');
  const tests = document.getElementById('btn-start-selected-test');
  if (flashcards) flashcards.disabled = !canStart;
  if (tests) tests.disabled = !canStart;
}

export function startSelectedLessonTestRun() {
  const selected = new Set(state.selectedChapters);
  const tests = getAllAvailableTests().filter(test => test.pillar === 'vocab' && test.category !== 'vocab_reviews' && test.category !== 'mock_exams' && selected.has(String(test.id).replace(/^vocab-/, '')));
  const questions = tests.flatMap(test => test.questions || []);
  if (!questions.length) { alert('No multiple-choice tests are available for these lessons.'); return null; }
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
  state.sessionSkipped = 0;
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
  if (!state.selectedChapters.size) { alert('Select at least one lesson first.'); return; }
  const chapters = Array.from(state.selectedChapters);
  const pool = [];
  for (const chapter of chapters) for (const word of (state.vocabDB[chapter] || [])) {
    if (document.getElementById('home-hard-only')?.checked && getWordStatus(word.id, state.studyDirection) !== 'hard') continue;
    const key = `V:${word.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
    pool.push({ ...word, type: 'vocab', key, book: 'vocab' });
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
    return { date: day.date, count: reviews, level: reviews <= 0 ? 0 : reviews < 10 ? 1 : reviews < 50 ? 2 : reviews < 200 ? 3 : reviews < 500 ? 4 : 5 };
  });
  // Reuse the existing 30-day layout while preserving this card's reviews-only scale.
  const html = renderHeatmapGridHtml(reviewsOnly).replace(/: (\d+) items/g, ': $1 reviews');
  grid.innerHTML = html + `<div class="home-heatmap-legend"><span>0</span><i class="heatmap-cell level-0"></i><i class="heatmap-cell level-1"></i><i class="heatmap-cell level-2"></i><i class="heatmap-cell level-3"></i><i class="heatmap-cell level-4"></i><i class="heatmap-cell level-5"></i><span>500+</span></div>`;
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
  if (detail) detail.hidden = true;
  const hint = document.getElementById('home-activity-hint');
  if (hint) hint.hidden = false;
  const streak = document.getElementById('home-review-streak');
  const today = document.getElementById('home-reviews-today');
  if (streak) streak.textContent = getCurrentStreak();
  if (today) today.textContent = getDay(istDateKey()).reviews;
}
