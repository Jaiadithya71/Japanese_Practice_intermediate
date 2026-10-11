/* =======================================================
   NIHONGO INTERMEDIATE — home.js
   5-Pillar Dashboard, Simultaneous Progress & Lesson Selection
   ======================================================= */

import { state } from './state.js';
import { getWordStatus } from './srs.js';

export function renderHomeView() {
  updateMasteryCounters();
  renderLessonGrid();
  updatePillarCards();
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

  const cardV = document.getElementById('pillar-vocab-count');
  const cardR = document.getElementById('pillar-reading-count');

  if (cardV) cardV.textContent = `${vocabCount} words (29 units)`;
  if (cardR) cardR.textContent = `${readingCount} lessons (88 Qs)`;
}

export function setHomeGroup(group) {
  state.activeChapterGroup = group;
  const tabT = document.getElementById('home-tab-topic');
  const tabC = document.getElementById('home-tab-char');
  if (tabT) tabT.classList.toggle('active', group === 'topic');
  if (tabC) tabC.classList.toggle('active', group === 'characteristics');
  renderLessonGrid();
}

export function toggleChapterSelection(chId) {
  if (state.selectedChapters.has(chId)) {
    state.selectedChapters.delete(chId);
  } else {
    state.selectedChapters.add(chId);
  }
  renderLessonGrid();
  updateStudyButtonState();
}

export function selectAllChaptersInGroup() {
  const prefix = state.activeChapterGroup === 'topic' ? 'part1_' : 'part2_';
  Object.keys(state.vocabDB).forEach(k => {
    if (k.startsWith(prefix)) {
      state.selectedChapters.add(k);
    }
  });
  renderLessonGrid();
  updateStudyButtonState();
}

export function clearChapterSelection() {
  state.selectedChapters.clear();
  renderLessonGrid();
  updateStudyButtonState();
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

  const prefix = state.activeChapterGroup === 'topic' ? 'part1_' : 'part2_';
  const chapterKeys = Object.keys(state.vocabDB)
    .filter(k => k.startsWith(prefix))
    .sort();

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
    const shortLabel = chId.replace('part1_', 'T').replace('part2_', 'C');

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
    `;
    container.appendChild(card);
  });
}
