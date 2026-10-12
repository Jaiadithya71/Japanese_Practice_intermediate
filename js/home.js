/* =======================================================
   NIHONGO INTERMEDIATE — home.js
   5-Pillar Dashboard, Simultaneous Progress & Lesson Selection
   ======================================================= */

import { state } from './state.js';
import { getWordStatus } from './srs.js';
import { startStudy } from './study.js';

export function startSingleChapterStudy(chId) {
  state.selectedChapters.clear();
  state.selectedChapters.add(chId);
  startStudy('flashcard', false, 'home');
}
window.startSingleChapterStudy = startSingleChapterStudy;

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
  const kanjiCount = Object.keys(state.kanjiDB || {}).length;

  const cardV = document.getElementById('pillar-vocab-count');
  const cardR = document.getElementById('pillar-reading-count');
  const cardK = document.getElementById('pillar-kanji-count');

  if (cardV) cardV.textContent = `${vocabCount} words (29 units)`;
  if (cardR) cardR.textContent = `${readingCount} lessons (88 Qs)`;
  if (cardK) cardK.textContent = `654 Kanji (443 N3 + 300 Review)`;
}

export function setHomeGroup(group) {
  state.activeChapterGroup = group;
  const tabT = document.getElementById('home-tab-topic');
  const tabC = document.getElementById('home-tab-char');
  if (tabT) tabT.classList.toggle('active', group === 'topic');
  if (tabC) tabC.classList.toggle('active', group === 'characteristics');
  renderLessonGrid();
}

export function chapterKeysForGroup() {
  const isChar = state.activeChapterGroup !== 'topic';
  const keys = Object.keys(state.vocabDB).filter(k => k.startsWith('part2_') === isChar);
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
}

export function selectAllChaptersInGroup() {
  chapterKeysForGroup().forEach(k => state.selectedChapters.add(k));
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
