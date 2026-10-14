/* =======================================================
   NIHONGO INTERMEDIATE — home.js
   5-Pillar Dashboard, Simultaneous Progress & Lesson Selection
   ======================================================= */

import { state } from './state.js';
import { getWordStatus } from './srs.js';
import { startStudy, renderCard } from './study.js';
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
}

export function chapterKeysForGroup() {
  const isChar = state.activeChapterGroup !== 'topic';
  const keys = Object.keys(state.vocabDB).filter(k => !k.startsWith('review_') && !k.startsWith('part3_mock') && k.startsWith('part2_') === isChar);
  const rank = k => (k.startsWith('review_') ? 1000 + parseInt(k.slice(7), 10) : parseInt(k.replace('part2_', ''), 10));
  return keys.sort((a, b) => rank(a) - rank(b));
}

export function toggleChapterSelection(chId) {
  if (state.selectedChapters.has(chId)) {
    state.selectedChapters.delete(chId);
  } else {
    state.selectedChapters.add(chId);
  }
  renderLessonGrid();
  updateStudyButtonState();
  updateHomeLessonControls();
}

export function selectAllChaptersInGroup() {
  chapterKeysForGroup().forEach(k => state.selectedChapters.add(k));
  renderLessonGrid();
  updateStudyButtonState();
  updateHomeLessonControls();
}

export function clearChapterSelection() {
  state.selectedChapters.clear();
  renderLessonGrid();
  updateStudyButtonState();
  updateHomeLessonControls();
}

function updateStudyButtonState() {
  const btn = document.getElementById('btn-start-selected-study');
  const count = state.selectedChapters.size;
  if (btn) {
    btn.innerHTML = `<i class="fa-solid fa-play"></i> Study Selected (${count > 0 ? count : 'All'})`;
  }
}

export function renderLessonGrid() {
  const container = document.getElementById('home-lesson-grid');
  if (!container) return;
  container.innerHTML = '';

  const chapterKeys = chapterKeysForGroup();

  chapterKeys.forEach(chId => {
    const meta = state.chapterMetadata[chId] || {};
    const words = state.vocabDB[chId] || [];
    const isSelected = state.selectedChapters.has(chId);

    let mastered = 0;
    words.forEach(w => {
      if (getWordStatus(w.id, state.studyDirection) === 'mastered') {
        mastered++;
      }
    });

    const pct = words.length > 0 ? Math.round((mastered / words.length) * 100) : 0;
    const shortLabel = chId.startsWith('part2_') ? 'C' + chId.slice(6) : chId.startsWith('review_') ? 'R' + chId.slice(7) : 'T' + chId;

    const card = document.createElement('div');
    card.className = `lesson-card${isSelected ? ' selected' : ''}`;
    card.onclick = () => toggleChapterSelection(chId);
    card.innerHTML = `
      <div class="lesson-card-header">
        <span class="lesson-badge">${shortLabel}</span>
        <span style="font-size: 0.8rem; color: var(--text-dim); font-weight: 600;">${words.length} words</span>
      </div>
      <div>
        <div class="lesson-card-title font-ja">${meta.topic_ja || chId}</div>
        <div class="lesson-card-subtitle">${meta.topic_en || ''}</div>
      </div>
      <div class="lesson-card-progress">
        <div class="progress-bar-track">
          <div class="progress-bar-fill" style="width: ${pct}%;"></div>
        </div>
        <span>${pct}%</span>
      </div>
      <div style="display:flex; gap:0.4rem; margin-top:0.4rem;" onclick="event.stopPropagation()">
        <button class="btn btn-ghost btn-xs" style="flex:1; font-size:0.72rem; padding:0.25rem 0.4rem; border-radius:8px;" onclick="window.startSingleChapterStudy('${chId}')">
          <i class="fa-solid fa-play"></i> Flashcards
        </button>
        <button class="btn btn-ghost btn-xs" style="flex:1; font-size:0.72rem; padding:0.25rem 0.4rem; border-radius:8px; color:var(--accent);" onclick="window.startTestSession('vocab-${chId}')">
          <i class="fa-solid fa-file-pen"></i> Test
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}


function homeRunSize() {
  try { return localStorage.getItem('n3_home_session_size') || '20'; } catch (_) { return '20'; }
}

export function setHomeSessionSize(value) {
  const allowed = ['10', '20', '50', 'all'];
  const selected = allowed.includes(String(value).toLowerCase()) ? String(value).toLowerCase() : '20';
  try { localStorage.setItem('n3_home_session_size', selected); } catch (_) {}
  updateHomeLessonControls();
}

export function setHomeStudyDirection(direction) {
  if (direction !== 'ja-en' && direction !== 'en-ja') return;
  state.studyDirection = direction;
  try { localStorage.setItem('n3_home_study_direction', direction); } catch (_) {}
  document.querySelectorAll('[data-home-direction]').forEach(button => button.classList.toggle('active', button.dataset.homeDirection === direction));
  renderLessonGrid();
}

function updateHomeLessonControls() {
  const size = homeRunSize();
  document.querySelectorAll('[data-home-size]').forEach(button => button.classList.toggle('active', button.dataset.homeSize === size));
  document.querySelectorAll('[data-home-direction]').forEach(button => button.classList.toggle('active', button.dataset.homeDirection === state.studyDirection));
  const count = state.selectedChapters.size;
  const title = document.getElementById('home-lessons-count');
  if (title) title.textContent = count ? `${count} lesson${count === 1 ? '' : 's'} selected · next batches continue automatically` : 'No lessons selected · all vocabulary lessons will be included';
  const btn = document.getElementById('btn-start-selected-study');
  if (btn) btn.innerHTML = `<i class="fa-solid fa-play"></i> Start ${count ? `${count} selected lesson${count === 1 ? '' : 's'}` : 'all lessons'}`;
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
  const chapters = state.selectedChapters.size ? Array.from(state.selectedChapters) : Object.keys(state.vocabDB);
  const pool = [];
  for (const chapter of chapters) for (const word of (state.vocabDB[chapter] || [])) {
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
  const streak = document.getElementById('home-review-streak');
  const today = document.getElementById('home-reviews-today');
  if (streak) streak.textContent = getCurrentStreak();
  if (today) today.textContent = getDay(istDateKey()).reviews;
}
