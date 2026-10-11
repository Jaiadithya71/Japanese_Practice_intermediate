/* =======================================================
   NIHONGO INTERMEDIATE — reader.js
   Dokkai (Reading Comprehension) Reader & Quiz Engine
   ======================================================= */

import { state } from './state.js';
import { updateItemStats, toggleItemHard, updateSidebarStats } from './srs.js';

export function renderReadingView() {
  renderCategoryTabs();
  renderLessonList();
}

export function renderCategoryTabs() {
  const container = document.getElementById('reader-category-tabs');
  if (!container) return;
  container.innerHTML = '';

  const categories = [
    { id: 'all', label: 'All Passages', icon: 'fa-layer-group' },
    { id: 'foundation', label: 'Foundation (基礎編)', icon: 'fa-cube' },
    { id: 'strategy', label: 'Pattern Strategy (対策編)', icon: 'fa-chess' },
    { id: 'real_short', label: 'Real Exam: Short (短文)', icon: 'fa-file-lines' },
    { id: 'real_medium', label: 'Real Exam: Medium (中文)', icon: 'fa-book-open' },
    { id: 'real_long', label: 'Real Exam: Long (長文)', icon: 'fa-scroll' },
    { id: 'info', label: 'Info Retrieval (情報検索)', icon: 'fa-magnifying-glass' }
  ];

  categories.forEach(c => {
    const btn = document.createElement('button');
    const isActive = state.readingCategory === c.id;
    btn.className = `reader-cat-tab${isActive ? ' active' : ''}`;
    btn.innerHTML = `<i class="fa-solid ${c.icon}"></i> ${c.label}`;
    btn.onclick = () => setReadingCategory(c.id);
    container.appendChild(btn);
  });
}

export function setReadingCategory(cat) {
  state.readingCategory = cat;
  renderCategoryTabs();
  renderLessonList();
}

export function renderLessonList() {
  const container = document.getElementById('dokkai-grid-container');
  if (!container) return;
  container.innerHTML = '';

  let list = Object.values(state.readingDB);

  if (state.readingCategory !== 'all') {
    list = list.filter(l => l.category === state.readingCategory);
  }

  const countBadge = document.getElementById('dokkai-count-badge');
  if (countBadge) countBadge.textContent = `${list.length} Lessons`;

  if (list.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-book-open-reader"></i>
        <h3>No lessons in this category</h3>
      </div>`;
    return;
  }

  list.forEach(l => {
    const qCount = (l.comprehensionQuestions || l.questions || l.drills || []).length;
    const card = document.createElement('div');
    card.className = 'dokkai-card';
    card.onclick = () => openReadingLesson(l.id);

    const genreText = l.genre || (l.category === 'foundation' ? '文法基礎' : '実戦問題');
    const pagesText = l.pages ? `pp. ${l.pages.join('–')}` : '';

    card.innerHTML = `
      <div class="dokkai-card-top">
        <span class="dokkai-genre-pill">${genreText}</span>
        <span style="font-size: 0.8rem; color: var(--text-dim);">${pagesText}</span>
      </div>
      <div>
        <h4 class="dokkai-card-title font-ja">${l.title_ja || l.title}</h4>
        <p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.35rem;">${l.title_en || ''}</p>
      </div>
      <div class="dokkai-card-meta">
        <span><i class="fa-solid fa-list-check"></i> ${qCount} Questions</span>
        <span><i class="fa-solid fa-clock"></i> ~${Math.max(4, Math.round(qCount * 2.5))} mins</span>
      </div>
    `;
    container.appendChild(card);
  });
}

// =======================================================
// READING WORKSPACE LOGIC
// =======================================================

export function openReadingLesson(lessonId) {
  const lesson = state.readingDB[lessonId];
  if (!lesson) return;

  state.activeReadingLesson = lesson;
  state.readingAnswers = {};
  state.readingQuizSubmitted = false;

  const listSection = document.getElementById('dokkai-list-section');
  const workspaceSection = document.getElementById('dokkai-workspace-section');

  if (listSection) listSection.style.display = 'none';
  if (workspaceSection) workspaceSection.style.display = 'block';

  renderWorkspace(lesson);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

export function closeReadingWorkspace() {
  state.activeReadingLesson = null;
  const listSection = document.getElementById('dokkai-list-section');
  const workspaceSection = document.getElementById('dokkai-workspace-section');

  if (listSection) listSection.style.display = 'block';
  if (workspaceSection) workspaceSection.style.display = 'none';
}

function renderWorkspace(lesson) {
  const container = document.getElementById('dokkai-workspace-container');
  if (!container) return;

  const questions = lesson.comprehensionQuestions || lesson.questions || [];
  const sentences = lesson.passage ? (lesson.passage.sentences || []) : [];

  container.innerHTML = `
    <div class="reading-workspace ${state.showSentenceTranslations ? 'show-translations' : ''}">
      <div class="reading-header">
        <div class="reading-title-area">
          <div style="display: flex; gap: 0.6rem; align-items: center; margin-bottom: 0.4rem;">
            <span class="dokkai-genre-pill">${lesson.genre || '読解問題'}</span>
            <span style="font-size: 0.82rem; color: var(--text-dim);">${lesson.pages ? `pp. ${lesson.pages.join('–')}` : ''}</span>
          </div>
          <h2 class="font-ja">${lesson.title_ja || lesson.title}</h2>
          <p>${lesson.title_en || ''}</p>
        </div>
        <div style="display: flex; gap: 0.6rem;">
          <button class="btn btn-sm btn-ghost" onclick="toggleSentenceTranslations()">
            <i class="fa-solid fa-language"></i> Translations: ${state.showSentenceTranslations ? 'ON' : 'OFF'}
          </button>
          <button class="btn btn-sm btn-ghost" onclick="closeReadingWorkspace()">
            <i class="fa-solid fa-arrow-left"></i> Passages List
          </button>
        </div>
      </div>

      ${lesson.passageInstructions ? `
        <div class="reading-instructions-box font-ja">
          <strong><i class="fa-solid fa-circle-info"></i> 指示:</strong> ${lesson.passageInstructions.instruction_ja || ''}
          <div style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.2rem;">${lesson.passageInstructions.instruction_en || ''}</div>
        </div>` : ''}

      <!-- Passage Content -->
      <div class="passage-container font-ja">
        ${sentences.length > 0 ? sentences.map(s => `
          <div class="passage-sentence">
            <div>${state.showFurigana ? (s.ruby_html || s.text_ja) : s.text_ja}</div>
            <div class="sentence-trans">${s.text_en || ''}</div>
          </div>
        `).join('') : `
          <div style="color: var(--text-muted); font-size: 1rem;">
            ${lesson.readingStrategy ? `<strong>Reading Strategy:</strong><br>${lesson.readingStrategy.point_ja || ''}<br><small>${lesson.readingStrategy.point_en || ''}</small>` : ''}
          </div>
        `}
      </div>

      <!-- Comprehension Quiz Section -->
      ${questions.length > 0 ? `
        <div class="quiz-section">
          <h3><i class="fa-solid fa-clipboard-question" style="color: var(--accent);"></i> Comprehension Quiz (${questions.length} Questions)</h3>
          
          <div id="dokkai-quiz-questions">
            ${questions.map((q, qIdx) => renderQuestionHTML(lesson.id, q, qIdx)).join('')}
          </div>

          <div style="display: flex; gap: 1rem; align-items: center; margin-top: 2rem;">
            <button class="btn btn-primary" id="btn-submit-dokkai-quiz" onclick="submitQuizAnswers()">
              <i class="fa-solid fa-check"></i> Submit Answers
            </button>
            <button class="btn btn-ghost" id="btn-add-missed-srs" onclick="addMissedQuestionsToSRS()" style="display: none;">
              <i class="fa-solid fa-fire"></i> Add Missed to Exam SRS
            </button>
          </div>
        </div>
      ` : ''}
    </div>
  `;
}

function renderQuestionHTML(lessonId, q, qIdx) {
  const qId = q.id || `${lessonId}_q${qIdx + 1}`;
  const options = q.options || [];

  return `
    <div class="question-block" id="qblock-${qId}">
      <div class="question-prompt font-ja">
        ${qIdx + 1}. ${q.question_ja || q.instruction_ja || ''}
        ${q.question_en ? `<div style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.2rem;">${q.question_en}</div>` : ''}
      </div>

      <div class="options-list">
        ${options.map((opt, optIdx) => {
          const optVal = optIdx + 1;
          const isSelected = state.readingAnswers[qId] === optVal;
          return `
            <div class="option-item font-ja${isSelected ? ' selected' : ''}" 
                 id="opt-${qId}-${optVal}"
                 onclick="selectQuizOption('${qId}', ${optVal})">
              <span class="badge" style="background: var(--surface); color: var(--text-dim);">${optVal}</span>
              <span>${opt}</span>
            </div>
          `;
        }).join('')}
      </div>

      <div class="quiz-explanation-box" id="exp-${qId}" style="display: none;">
        <strong style="color: var(--green);"><i class="fa-solid fa-check-circle"></i> Correct Answer: Option ${q.correctAnswer}</strong>
        <p style="margin-top: 0.35rem; color: var(--text);">${q.explanation_ja || ''}</p>
        ${q.explanation_en ? `<p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.25rem;">${q.explanation_en}</p>` : ''}
      </div>
    </div>
  `;
}

export function selectQuizOption(qId, optVal) {
  if (state.readingQuizSubmitted) return;
  state.readingAnswers[qId] = optVal;

  // Visual selection
  const block = document.getElementById(`qblock-${qId}`);
  if (block) {
    block.querySelectorAll('.option-item').forEach(el => el.classList.remove('selected'));
    const target = document.getElementById(`opt-${qId}-${optVal}`);
    if (target) target.classList.add('selected');
  }
}

export function toggleSentenceTranslations() {
  state.showSentenceTranslations = !state.showSentenceTranslations;
  const workspace = document.querySelector('.reading-workspace');
  if (workspace) {
    workspace.classList.toggle('show-translations', state.showSentenceTranslations);
  }
}

export function submitQuizAnswers() {
  if (!state.activeReadingLesson) return;
  state.readingQuizSubmitted = true;

  const lesson = state.activeReadingLesson;
  const questions = lesson.comprehensionQuestions || lesson.questions || [];
  let correctCount = 0;
  let hasMissed = false;

  questions.forEach((q, qIdx) => {
    const qId = q.id || `${lesson.id}_q${qIdx + 1}`;
    const userAns = state.readingAnswers[qId];
    const correctAns = parseInt(q.correctAnswer, 10);
    const srsKey = `R_Q:${qId}`;

    const expBox = document.getElementById(`exp-${qId}`);
    if (expBox) expBox.style.display = 'block';

    const correctOptEl = document.getElementById(`opt-${qId}-${correctAns}`);
    if (correctOptEl) correctOptEl.classList.add('correct');

    if (userAns === correctAns) {
      correctCount++;
      updateItemStats(srsKey, 3); // Good (SM-2)
    } else {
      hasMissed = true;
      if (userAns) {
        const wrongOptEl = document.getElementById(`opt-${qId}-${userAns}`);
        if (wrongOptEl) wrongOptEl.classList.add('incorrect');
      }
      updateItemStats(srsKey, 1); // Missed (priority surge)
      toggleItemHard(srsKey);     // Flag for Weak Points Desk
    }
  });

  const btnSubmit = document.getElementById('btn-submit-dokkai-quiz');
  if (btnSubmit) {
    btnSubmit.innerHTML = `<i class="fa-solid fa-circle-check"></i> Score: ${correctCount} / ${questions.length}`;
    btnSubmit.disabled = true;
  }

  const btnAddMissed = document.getElementById('btn-add-missed-srs');
  if (btnAddMissed && hasMissed) {
    btnAddMissed.style.display = 'inline-flex';
  }

  updateSidebarStats();
}

export function addMissedQuestionsToSRS() {
  alert('Missed comprehension questions have been added to your Exam SRS queue and Weak Points Desk for daily review!');
  const btn = document.getElementById('btn-add-missed-srs');
  if (btn) btn.disabled = true;
}
