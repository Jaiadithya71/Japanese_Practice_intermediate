/* =======================================================
   NIHONGO INTERMEDIATE — test.js
   Full Chapter Tests, Review Exams & Practice Simulator
   Faithfully matching Nihongo Trainer (4Q/5Q) with Poco M7 Mobile Tuning
   Enhanced with Question Jump Drawer, Flagging, Category Tabs,
   Pass/Fail Metrics, Weak Points Integration & Missed Review
   ======================================================= */

import { state } from './state.js';
import { updateItemStats, saveStats, getItemStats, updateSidebarStats } from './srs.js';
import { beginGistReviewSession, endGistReviewSession } from './gist-sync.js';

let activeTestSession = null;
let activeTestCategory = 'all';
let testSearchQuery = '';

export function getActiveTestSession() {
  return activeTestSession;
}

export function getActiveTestCategory() {
  return activeTestCategory;
}

export function setActiveTestCategory(cat) {
  activeTestCategory = cat;
}

// -------------------------------------------------------
// Dynamic Style Injection for Jump Drawer & Results UI
// -------------------------------------------------------
function ensureStylesInjected() {
  if (typeof document === 'undefined') return;
  if (document.getElementById('test-upgrades-styles')) return;

  const style = document.createElement('style');
  style.id = 'test-upgrades-styles';
  style.textContent = `
    /* Each test screen uses hide to switch between hub, runner and results. */
    #test-hub-screen.hide, #test-runner-screen.hide, #test-results-screen.hide {
      display: none !important;
    }
    /* Header Action Buttons */
    .tr-header-actions {
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }
    .tr-action-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.75rem;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.18s ease;
      touch-action: manipulation;
    }
    .tr-action-btn:hover {
      border-color: var(--accent);
      color: var(--text);
    }
    .tr-action-btn.flagged {
      background: rgba(245, 166, 35, 0.15) !important;
      border-color: var(--amber) !important;
      color: var(--amber) !important;
    }

    /* Jump Drawer Modal Overlay & Sheet */
    .test-jump-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 1000;
      display: flex;
      align-items: flex-end;
      justify-content: center;
      transition: opacity 0.2s ease;
    }
    .test-jump-overlay.hide {
      display: none;
    }
    .test-jump-sheet {
      background: var(--bg2, #161a23);
      border: 1px solid var(--border-strong, rgba(255, 255, 255, 0.12));
      border-radius: 24px 24px 0 0;
      width: 100%;
      max-width: 680px;
      max-height: 80vh;
      display: flex;
      flex-direction: column;
      padding: 1.25rem 1.25rem max(1.25rem, env(safe-area-inset-bottom, 1rem));
      box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.6);
      animation: jumpSheetSlideUp 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes jumpSheetSlideUp {
      from { transform: translateY(100%); }
      to { transform: translateY(0); }
    }
    .test-jump-sheet-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.75rem;
    }
    .test-jump-sheet-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text, #fff);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .test-jump-close-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
    }
    .test-jump-legend {
      display: flex;
      gap: 0.85rem;
      flex-wrap: wrap;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
      padding-bottom: 0.6rem;
      border-bottom: 1px solid var(--border);
    }
    .legend-item {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }
    .legend-dot {
      width: 10px;
      height: 10px;
      border-radius: 3px;
    }
    .legend-dot.current { background: var(--accent); }
    .legend-dot.answered { background: var(--green); }
    .legend-dot.unanswered { border: 1px dashed var(--text-muted); background: transparent; }
    .legend-dot.flagged { background: var(--amber); border-radius: 50%; }

    .test-jump-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(46px, 1fr));
      gap: 8px;
      overflow-y: auto;
      max-height: 52vh;
      padding: 4px;
    }
    .test-jump-btn {
      position: relative;
      height: 46px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
      touch-action: manipulation;
      user-select: none;
    }
    .test-jump-btn.unanswered {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
    }
    .test-jump-btn.unanswered:hover {
      border-color: var(--text);
      color: var(--text);
    }
    .test-jump-btn.answered {
      background: rgba(34, 211, 164, 0.16);
      border: 1px solid var(--green);
      color: var(--green);
    }
    .test-jump-btn.current {
      background: var(--accent) !important;
      border: 2px solid #fff !important;
      color: #fff !important;
      box-shadow: 0 0 12px var(--accent-light);
    }
    .test-jump-btn.flagged::after {
      content: '';
      position: absolute;
      top: 4px;
      right: 4px;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--amber);
      box-shadow: 0 0 4px var(--amber);
    }
    .jump-check-icon {
      font-size: 0.72rem;
      line-height: 1;
      margin-top: 2px;
    }

    /* Results Screen Upgrades */
    .test-pass-fail-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 1.25rem;
      border-radius: 999px;
      font-size: 0.95rem;
      font-weight: 800;
      margin: 0.5rem 0 1rem;
      letter-spacing: 0.02em;
    }
    .test-pass-fail-badge.pass {
      background: rgba(34, 211, 164, 0.15);
      border: 1px solid var(--green);
      color: var(--green);
    }
    .test-pass-fail-badge.fail {
      background: rgba(249, 92, 92, 0.15);
      border: 1px solid var(--red);
      color: var(--red);
    }
    .test-results-action-grid {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      max-width: 380px;
      margin: 1.25rem auto 0;
      width: 100%;
    }
    .test-results-action-grid .btn {
      width: 100%;
      min-height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      font-weight: 700;
      border-radius: 14px;
    }
  `;
  document.head.appendChild(style);
}

// -------------------------------------------------------
// Initialization & Test Collection
// -------------------------------------------------------
export function initTestHub() {
  ensureStylesInjected();
  renderTestCategoryTabs();
  renderTestCardsGrid();
}

export function getAllAvailableTests() {
  const tests = [];

  // 1. Vocabulary Chapter Drills & Review Tests
  if (state.chapterExercises) {
    for (const chId in state.chapterExercises) {
      const exs = state.chapterExercises[chId] || [];
      const meta = (state.chapterMetadata && state.chapterMetadata[chId]) || {};
      const topicJa = meta.topic_ja || chId;
      const topicEn = meta.topic_en || '';
      
      const isReview = chId.startsWith('review_');
      const isPart2 = chId.startsWith('part2_');
      const isMock = chId.startsWith('part3_');

      let category = 'vocab_topics';
      let catLabel = 'Vocab Drills';
      let badgeClass = 'badge-n4';

      if (isReview) {
        category = 'vocab_reviews';
        catLabel = 'Vocab Review Test';
        badgeClass = 'badge-qb';
      } else if (isPart2) {
        category = 'vocab_characteristics';
        catLabel = 'Characteristics Drill';
        badgeClass = 'badge-try';
      } else if (isMock) {
        category = 'mock_exams';
        catLabel = 'Official Mock Exam';
        badgeClass = 'badge-red';
      }

      // Flatten items into test questions
      const questions = [];
      exs.forEach((ex, exIdx) => {
        const exTitle = ex.title_ja || `Exercise ${exIdx + 1}`;
        (ex.items || []).forEach((it, itIdx) => {
          let opts = it.options || [];
          let ansText = it.answer || '';
          let correctIdx = 0;

          // If answer is text matching an option, compute 1-based index
          if (opts.length > 0 && typeof ansText === 'string') {
            const foundIdx = opts.findIndex(o => String(o).trim() === String(ansText).trim());
            if (foundIdx !== -1) {
              correctIdx = foundIdx + 1;
            } else if (it.correctAnswer !== undefined) {
              correctIdx = it.correctAnswer;
            } else if (!isNaN(parseInt(ansText, 10))) {
              correctIdx = parseInt(ansText, 10);
            }
          } else if (it.correctAnswer !== undefined) {
            correctIdx = it.correctAnswer;
          }

          questions.push({
            id: `test-v-${chId}-${exIdx}-${itIdx}`,
            category: 'vocab',
            chapter: chId,
            exerciseTitle: exTitle,
            type: ex.type || 'multiple_choice',
            question: it.question_ja || it.sentence || it.title_ja || '',
            options: opts,
            correct: correctIdx,
            correctAnswerText: ansText,
            explanation: it.explanation || it.explanation_ja || '',
            targetWord: it.target_word || it.answer || ''
          });
        });
      });

      if (questions.length > 0) {
        tests.push({
          id: `vocab-${chId}`,
          category: category,
          catLabel: catLabel,
          badgeClass: badgeClass,
          title: topicJa,
          subTitle: topicEn,
          pillar: 'vocab',
          questionCount: questions.length,
          questions: questions
        });
      }
    }
  }

  // 2. Kanji Lesson Drills & Practice Tests
  if (state.kanjiExercisesDB) {
    for (const lesNum in state.kanjiExercisesDB) {
      const exs = state.kanjiExercisesDB[lesNum] || [];
      const questions = [];

      exs.forEach((ex, exIdx) => {
        (ex.items || []).forEach((it, itIdx) => {
          const opts = it.options || [];
          let ansText = it.answer || (it.answers ? it.answers.join(', ') : '');
          let correctIdx = 1;
          if (opts.length > 0 && ansText) {
            const found = opts.findIndex(o => String(o).trim() === String(ansText).trim());
            if (found !== -1) correctIdx = found + 1;
          }

          questions.push({
            id: `test-k-${lesNum}-${exIdx}-${itIdx}`,
            category: 'kanji',
            exerciseTitle: ex.title_ja || `Kanji Drill ${lesNum}`,
            type: 'multiple_choice',
            question: it.question_ja || it.sentence || it.target_word || '',
            options: opts,
            correct: correctIdx,
            correctAnswerText: ansText,
            explanation: it.explanation || ''
          });
        });
      });

      if (questions.length > 0) {
        tests.push({
          id: `kanji-drill-L${lesNum}`,
          category: 'kanji_drills',
          catLabel: 'Kanji Practice Drill',
          badgeClass: 'badge-n5',
          title: `漢字 第${lesNum}課 練習問題`,
          subTitle: `Lesson ${lesNum} Practice Drills`,
          pillar: 'kanji',
          questionCount: questions.length,
          questions: questions
        });
      }
    }
  }

  // 3. Kanji Mock Tests
  if (state.kanjiMockTests && state.kanjiMockTests.length > 0) {
    state.kanjiMockTests.forEach((m, mIdx) => {
      const questions = [];
      (m.exercises || []).forEach((ex, exIdx) => {
        (ex.items || []).forEach((it, itIdx) => {
          questions.push({
            id: `test-kmock-${mIdx}-${exIdx}-${itIdx}`,
            category: 'kanji_mock',
            exerciseTitle: ex.title_ja || '',
            type: 'multiple_choice',
            question: it.question_ja || '',
            options: it.options || [],
            correct: parseInt(it.answer, 10) || 1,
            correctAnswerText: (it.options || [])[(parseInt(it.answer, 10) || 1) - 1] || '',
            explanation: it.explanation || ''
          });
        });
      });

      if (questions.length > 0) {
        tests.push({
          id: `kanji-mock-${mIdx + 1}`,
          category: 'mock_exams',
          catLabel: 'Kanji Mock Exam',
          badgeClass: 'badge-red',
          title: m.topic_ja || `漢字 実力テスト ${mIdx + 1}`,
          subTitle: m.topic_en || `Kanji Mock Test ${mIdx + 1}`,
          pillar: 'kanji',
          questionCount: questions.length,
          questions: questions
        });
      }
    });
  }

  // 4. Reading Comprehension Passages as Tests
  if (state.readingDB) {
    const readingQuestions = [];
    for (const rId in state.readingDB) {
      const les = state.readingDB[rId];
      const qs = les.comprehensionQuestions || les.questions || [];
      qs.forEach((q, qIdx) => {
        readingQuestions.push({
          id: `test-r-${rId}-${qIdx}`,
          category: 'reading',
          passageTitle: les.title_ja || 'Passage',
          passageText: (les.passage && les.passage.sentences) ? les.passage.sentences.map(s => s.japanese || s.text_ja || '').join('\n') : '',
          question: q.question_ja || q.question || '',
          options: q.options || [],
          correct: q.correctAnswer || q.correct || 1,
          correctAnswerText: (q.options || [])[(q.correctAnswer || q.correct || 1) - 1] || '',
          explanation: q.explanation_ja || q.explanation || ''
        });
      });
    }

    if (readingQuestions.length > 0) {
      tests.push({
        id: 'reading-all-comprehension',
        category: 'reading_tests',
        catLabel: 'Dokkai Question Bank',
        badgeClass: 'badge-green',
        title: '読解 実戦問題集 (All Dokkai)',
        subTitle: 'Complete Reading Comprehension Bank',
        pillar: 'reading',
        questionCount: readingQuestions.length,
        questions: readingQuestions
      });
    }
  }

  // 5. Grammar Drills & Mock Tests
  if (state.grammarDB) {
    const sec1to6 = state.grammarDB.part1_1_6?.sections || [];
    const sec7to12 = state.grammarDB.part1_7_12?.sections || [];
    const allGrammarSections = [...sec1to6, ...sec7to12];

    allGrammarSections.forEach((sec, sIdx) => {
      const questions = [];
      (sec.drills || []).forEach((d, dIdx) => {
        questions.push({
          id: d.id || `test-g-sec-${sec.id || sIdx}-${dIdx}`,
          category: 'grammar',
          exerciseTitle: sec.title || `Grammar Section ${sIdx + 1}`,
          type: 'multiple_choice',
          question: d.prompt || d.sentence || '',
          options: d.options || [],
          correct: Number(d.correct_answer || d.correct) || 1,
          correctAnswerText: (d.options || [])[(Number(d.correct_answer || d.correct) || 1) - 1] || '',
          explanation: d.explanation || ''
        });
      });

      if (questions.length > 0) {
        tests.push({
          id: `grammar-drill-${sec.id || sIdx + 1}`,
          category: 'grammar',
          catLabel: 'Grammar Drill',
          badgeClass: 'badge-try',
          title: sec.title ? `${sec.title} 練習問題` : `文法 第${sIdx + 1}課 練習問題`,
          subTitle: `Grammar Drill · ${sec.title || `Section ${sIdx + 1}`}`,
          pillar: 'grammar',
          questionCount: questions.length,
          questions: questions
        });
      }
    });

    // Grammar Part 2 Star Blanks
    const part2Secs = state.grammarDB.part2?.sections || [];
    const part2Questions = [];
    part2Secs.forEach((sec, sIdx) => {
      (sec.drills || []).forEach((d, dIdx) => {
        part2Questions.push({
          id: d.id || `test-g-star-${sec.id || sIdx}-${dIdx}`,
          category: 'grammar',
          exerciseTitle: '文の組み立て (★問題)',
          type: 'multiple_choice',
          question: d.prompt || '',
          options: d.options || [],
          correct: Number(d.correct_answer || d.correct) || 1,
          correctAnswerText: (d.options || [])[(Number(d.correct_answer || d.correct) || 1) - 1] || '',
          explanation: d.explanation || ''
        });
      });
    });

    if (part2Questions.length > 0) {
      tests.push({
        id: 'grammar-star-composition',
        category: 'grammar',
        catLabel: 'Grammar Star Blank',
        badgeClass: 'badge-qb',
        title: '第2部 文の組み立て (★に入るもの)',
        subTitle: 'Sentence Composition Star Drills',
        pillar: 'grammar',
        questionCount: part2Questions.length,
        questions: part2Questions
      });
    }

    // Grammar Mock Tests
    const mockTests = state.grammarDB.mock?.mock_tests || [];
    mockTests.forEach((m, mIdx) => {
      const questions = [];
      (m.questions || []).forEach((q, qIdx) => {
        questions.push({
          id: q.id || `test-g-mock-${mIdx}-${qIdx}`,
          category: 'grammar_mock',
          exerciseTitle: m.title || `Grammar Mock ${mIdx + 1}`,
          type: 'multiple_choice',
          question: q.prompt || '',
          options: q.options || [],
          correct: Number(q.correct_answer || q.correct) || 1,
          correctAnswerText: (q.options || [])[(Number(q.correct_answer || q.correct) || 1) - 1] || '',
          explanation: q.explanation || ''
        });
      });

      if (questions.length > 0) {
        tests.push({
          id: `grammar-mock-${mIdx + 1}`,
          category: 'mock_exams',
          catLabel: 'Grammar Mock Exam',
          badgeClass: 'badge-red',
          title: m.title || `文法 実力模擬テスト ${mIdx + 1}`,
          subTitle: `Grammar Official Mock Test ${mIdx + 1}`,
          pillar: 'grammar',
          questionCount: questions.length,
          questions: questions
        });
      }
    });
  }

  return tests;
}

// -------------------------------------------------------
// Category Tabs & Filtering
// -------------------------------------------------------
export function renderTestCategoryTabs() {
  const container = document.getElementById('test-category-tabs');
  if (!container) return;

  const categories = [
    { id: 'all', label: 'All Tests' },
    { id: 'vocab', label: 'Vocab' },
    { id: 'kanji', label: 'Kanji' },
    { id: 'grammar', label: 'Grammar' },
    { id: 'reading', label: 'Reading' },
    { id: 'mock_exams', label: 'Mock Exams' }
  ];

  container.innerHTML = categories.map(cat => `
    <button class="test-cat-tab${activeTestCategory === cat.id ? ' active' : ''}" onclick="window.filterTestCategory('${cat.id}')">
      ${cat.label}
    </button>
  `).join('');
}

export function filterTestCategory(catId) {
  activeTestCategory = catId;
  renderTestCategoryTabs();
  renderTestCardsGrid();
}

export function renderTestCardsGrid() {
  const grid = document.getElementById('test-cards-grid');
  if (!grid) return;

  const allTests = getAllAvailableTests();
  let filtered = allTests;

  if (activeTestCategory !== 'all') {
    if (activeTestCategory === 'vocab') {
      filtered = filtered.filter(t => t.pillar === 'vocab' || t.category === 'vocab' || t.category.startsWith('vocab_'));
    } else if (activeTestCategory === 'grammar') {
      filtered = filtered.filter(t => t.pillar === 'grammar' || t.category === 'grammar' || t.category.startsWith('grammar_'));
    } else if (activeTestCategory === 'reading') {
      filtered = filtered.filter(t => t.pillar === 'reading' || t.category === 'reading' || t.category.startsWith('reading_'));
    } else if (activeTestCategory === 'mock_exams') {
      filtered = filtered.filter(t => t.category === 'mock_exams' || t.pillar === 'mock');
    } else if (activeTestCategory === 'kanji') {
      filtered = filtered.filter(t => t.pillar === 'kanji' || t.category.startsWith('kanji_'));
    } else {
      filtered = filtered.filter(t => t.category === activeTestCategory || t.pillar === activeTestCategory);
    }
  }

  if (testSearchQuery.trim()) {
    const q = testSearchQuery.toLowerCase();
    filtered = filtered.filter(t => t.title.toLowerCase().includes(q) || t.subTitle.toLowerCase().includes(q));
  }

  // Update counter badges
  const totalCountEl = document.getElementById('test-total-count');
  if (totalCountEl) totalCountEl.textContent = allTests.length;

  const totalQuestionsEl = document.getElementById('test-total-questions');
  if (totalQuestionsEl) {
    totalQuestionsEl.textContent = allTests.reduce((acc, t) => acc + t.questionCount, 0);
  }

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--text-muted);">
        <i class="fa-solid fa-file-circle-question" style="font-size: 2.5rem; margin-bottom: 0.75rem; color: var(--text-dim);"></i>
        <p style="font-size: 1rem; font-weight: 600;">No test questions match your search filter.</p>
      </div>
    `;
    return;
  }

  grid.innerHTML = filtered.map(t => {
    let icon = 'fa-file-lines';
    if (t.pillar === 'kanji') icon = 'fa-shapes';
    if (t.pillar === 'reading') icon = 'fa-book-open-reader';
    if (t.pillar === 'grammar') icon = 'fa-diagram-project';
    if (t.category === 'mock_exams') icon = 'fa-award';

    const estMins = Math.max(3, Math.round(t.questionCount * 0.8));

    return `
      <div class="test-card" onclick="window.startTestSession('${t.id}')">
        <div class="test-card-top">
          <span class="test-cat-badge ${t.badgeClass}">
            ${t.catLabel}
          </span>
          <div class="test-card-icon-bubble">
            <i class="fa-solid ${icon}"></i>
          </div>
        </div>
        <h3 class="test-card-title">${t.title}</h3>
        <div class="test-card-subinfo">
          <span class="test-subinfo-item"><i class="fa-solid fa-bookmark"></i> ${t.subTitle}</span>
          <span class="test-subinfo-item"><i class="fa-regular fa-clock"></i> ~${estMins}m</span>
        </div>
        <div class="test-card-meta">
          <span class="test-meta-tag tag-qcount"><strong>${t.questionCount}</strong> Questions</span>
          <span class="test-feature-tag tag-instant"><i class="fa-solid fa-bolt"></i> Instant Feedback</span>
        </div>
      </div>
    `;
  }).join('');
}

// -------------------------------------------------------
// Test Runner & Active Session
// -------------------------------------------------------
export function startTestSession(testId, customTest = null) {
  let target = customTest;
  if (!target) {
    const allTests = getAllAvailableTests();
    target = allTests.find(t => t.id === testId);
  }
  if (!target || !target.questions || target.questions.length === 0) {
    if (typeof alert === 'function') alert('This test is currently empty or still being processed.');
    return null;
  }

  beginGistReviewSession();
  activeTestSession = {
    test: target,
    idx: 0,
    score: 0,
    answers: {}, // idx -> { selected, correct, wasCorrect }
    flagged: new Set(),
    answered: false
  };
  state.activeTestSession = activeTestSession;

  const hubScreen = document.getElementById('test-hub-screen');
  const resultsScreen = document.getElementById('test-results-screen');
  const runnerScreen = document.getElementById('test-runner-screen');

  if (hubScreen) hubScreen.classList.add('hide');
  if (resultsScreen) resultsScreen.classList.add('hide');
  if (runnerScreen) runnerScreen.classList.remove('hide');

  ensureStylesInjected();
  ensureJumpDrawerDOM();
  renderTestQuestion();

  return activeTestSession;
}

export function renderTestQuestion() {
  if (!activeTestSession) return;
  const s = activeTestSession;
  if (s.idx < 0 || s.idx >= s.test.questions.length) return;
  const q = s.test.questions[s.idx];

  // Header & Progress
  const titleEl = document.getElementById('tr-test-title');
  const countEl = document.getElementById('tr-question-count');
  const fillEl = document.getElementById('tr-progress-fill');

  if (titleEl) titleEl.textContent = s.test.title;
  if (countEl) countEl.textContent = `${s.idx + 1} / ${s.test.questions.length}`;
  if (fillEl) fillEl.style.width = `${((s.idx) / s.test.questions.length) * 100}%`;

  // Dynamic Header Action Controls: Flag & [# Jump]
  const runnerHeader = document.querySelector('.test-runner-header');
  if (runnerHeader) {
    let actions = document.getElementById('tr-header-actions');
    if (!actions) {
      actions = document.createElement('div');
      actions.id = 'tr-header-actions';
      actions.className = 'tr-header-actions';
      runnerHeader.appendChild(actions);
    }
    const isFlagged = Boolean(s.flagged && s.flagged.has(s.idx));
    actions.innerHTML = `
      <button id="tr-flag-btn" class="tr-action-btn ${isFlagged ? 'flagged' : ''}" onclick="window.toggleFlagCurrentQuestion()" title="Bookmark Question">
        <i class="fa-${isFlagged ? 'solid' : 'regular'} fa-bookmark"></i> ${isFlagged ? 'Flagged' : 'Flag'}
      </button>
      <button id="tr-jump-btn" class="tr-action-btn" onclick="window.openJumpDrawer()" title="Jump to Question">
        <i class="fa-solid fa-hashtag"></i> Jump
      </button>
    `;
  }

  // Reading Passage Box (if applicable)
  const promptEl = document.getElementById('tr-prompt');
  const passageBox = document.getElementById('tr-passage-box');
  const passageTextEl = document.getElementById('tr-passage-text');

  if (q.passageText && passageBox && passageTextEl) {
    passageBox.style.display = 'block';
    passageTextEl.textContent = q.passageText;
  } else if (passageBox) {
    passageBox.style.display = 'none';
  }

  if (promptEl) {
    promptEl.innerHTML = `<span style="font-family: var(--font-japanese); font-size: 1.25rem; line-height: 1.7; font-weight: 600;">${q.question}</span>`;
  }

  // Options Container
  const optsContainer = document.getElementById('tr-options-container');
  if (!optsContainer) return;

  const currentAnswer = s.answers[s.idx];

  if (!currentAnswer) {
    // Unanswered question
    optsContainer.innerHTML = (q.options || []).map((opt, i) => `
      <button class="test-opt-btn" onclick="window.submitQuestionAnswer(${i + 1})">
        <span class="test-opt-badge">${i + 1}</span>
        <span class="test-opt-text font-ja">${opt}</span>
      </button>
    `).join('');

    const explanationEl = document.getElementById('tr-explanation-box');
    if (explanationEl) explanationEl.style.display = 'none';

    const nextBtn = document.getElementById('tr-next-btn');
    if (nextBtn) nextBtn.style.display = 'none';
  } else {
    // Answered question (revealed)
    optsContainer.innerHTML = (q.options || []).map((opt, i) => {
      const optNum = i + 1;
      let optClass = 'test-opt-btn';
      if (optNum === q.correct) {
        optClass += ' opt-correct';
      } else if (optNum === currentAnswer.selected) {
        optClass += ' opt-wrong';
      }

      return `
        <button class="${optClass}" disabled>
          <span class="test-opt-badge">${optNum}</span>
          <span class="test-opt-text font-ja">${opt}</span>
          ${optNum === q.correct ? '<i class="fa-solid fa-circle-check" style="margin-left:auto; color:var(--green)"></i>' : ''}
          ${(optNum === currentAnswer.selected && optNum !== q.correct) ? '<i class="fa-solid fa-circle-xmark" style="margin-left:auto; color:var(--red)"></i>' : ''}
        </button>
      `;
    }).join('');

    // Explanation Box
    const explanationEl = document.getElementById('tr-explanation-box');
    const explText = document.getElementById('tr-explanation-text');
    if (explanationEl && explText) {
      explanationEl.style.display = 'block';
      explText.innerHTML = `
        <strong>${currentAnswer.wasCorrect ? '正解！ (Correct)' : '不正解 (Incorrect)'}</strong> — 
        正解は「${q.correctAnswerText || (q.options || [])[q.correct - 1] || ''}」です。<br>
        ${q.explanation ? `<div style="margin-top:0.4rem; color:var(--text-muted); font-size:0.85rem;">${q.explanation}</div>` : ''}
      `;
    }

    const nextBtn = document.getElementById('tr-next-btn');
    if (nextBtn) {
      nextBtn.style.display = 'flex';
      nextBtn.textContent = (s.idx + 1 >= s.test.questions.length) ? 'View Results' : 'Next Question';
    }
  }
}

export function submitQuestionAnswer(optNum) {
  if (!activeTestSession) return;
  const s = activeTestSession;
  if (s.answers[s.idx]) return; // already answered

  const q = s.test.questions[s.idx];
  const wasCorrect = (optNum === q.correct);

  if (wasCorrect) s.score++;

  s.answers[s.idx] = {
    selected: optNum,
    correct: q.correct,
    wasCorrect: wasCorrect
  };

  // Immediate SRS integration for known vocabulary items
  const grade = wasCorrect ? 3 : 1;
  if (q.targetWord) {
    const key = q.targetWord.startsWith('V:') ? q.targetWord : `V:${q.targetWord}`;
    updateItemStats(key, grade, { cause: wasCorrect ? undefined : 'test-mistake' });
  } else if (q.key) {
    updateItemStats(q.key, grade, { cause: wasCorrect ? undefined : 'test-mistake' });
  }

  renderTestQuestion();
}

export function advanceTestQuestion() {
  if (!activeTestSession) return;
  const s = activeTestSession;

  if (s.idx + 1 < s.test.questions.length) {
    s.idx++;
    renderTestQuestion();
  } else {
    showTestResults();
  }
}

// -------------------------------------------------------
// Question Flagging
// -------------------------------------------------------
export function toggleFlagCurrentQuestion() {
  if (!activeTestSession) return false;
  const s = activeTestSession;
  if (!s.flagged) {
    s.flagged = new Set();
  }

  const isFlagged = s.flagged.has(s.idx);
  if (isFlagged) {
    s.flagged.delete(s.idx);
  } else {
    s.flagged.add(s.idx);
  }

  const flagBtn = document.getElementById('tr-flag-btn');
  if (flagBtn) {
    const nowFlagged = s.flagged.has(s.idx);
    flagBtn.classList.toggle('flagged', nowFlagged);
    flagBtn.innerHTML = `<i class="fa-${nowFlagged ? 'solid' : 'regular'} fa-bookmark"></i> ${nowFlagged ? 'Flagged' : 'Flag'}`;
  }

  const drawerOverlay = document.getElementById('test-jump-drawer-overlay');
  if (drawerOverlay && !drawerOverlay.classList.contains('hide')) {
    renderJumpDrawerGrid();
  }

  return s.flagged.has(s.idx);
}

// -------------------------------------------------------
// Question Jump Drawer
// -------------------------------------------------------
function ensureJumpDrawerDOM() {
  if (typeof document === 'undefined') return null;
  let overlay = document.getElementById('test-jump-drawer-overlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.id = 'test-jump-drawer-overlay';
    overlay.className = 'test-jump-overlay hide';
    overlay.onclick = (e) => {
      if (e.target === overlay) closeJumpDrawer();
    };
    overlay.innerHTML = `
      <div class="test-jump-sheet" onclick="event.stopPropagation()">
        <div class="test-jump-sheet-header">
          <div class="test-jump-sheet-title">
            <i class="fa-solid fa-hashtag"></i> Jump to Question
          </div>
          <button class="test-jump-close-btn" onclick="window.closeJumpDrawer()" aria-label="Close">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>
        <div class="test-jump-legend">
          <span class="legend-item"><span class="legend-dot current"></span> Current</span>
          <span class="legend-item"><span class="legend-dot answered"></span> Answered</span>
          <span class="legend-item"><span class="legend-dot unanswered"></span> Unanswered</span>
          <span class="legend-item"><span class="legend-dot flagged"></span> Flagged</span>
        </div>
        <div id="test-jump-grid" class="test-jump-grid">
          <!-- Populated by renderJumpDrawerGrid -->
        </div>
      </div>
    `;
    const runner = document.getElementById('test-runner-screen') || document.body;
    runner.appendChild(overlay);
  }
  return overlay;
}

export function openJumpDrawer() {
  if (!activeTestSession) return;
  ensureJumpDrawerDOM();
  const overlay = document.getElementById('test-jump-drawer-overlay');
  if (!overlay) return;

  renderJumpDrawerGrid();
  overlay.classList.remove('hide');
}

export function closeJumpDrawer() {
  const overlay = document.getElementById('test-jump-drawer-overlay');
  if (overlay) {
    overlay.classList.add('hide');
  }
}

export function renderJumpDrawerGrid() {
  const grid = document.getElementById('test-jump-grid');
  if (!grid || !activeTestSession) return;
  const s = activeTestSession;

  grid.innerHTML = s.test.questions.map((q, i) => {
    const isCurrent = i === s.idx;
    const isAnswered = Boolean(s.answers && s.answers[i]);
    const isFlagged = Boolean(s.flagged && s.flagged.has(i));

    const classes = ['test-jump-btn'];
    if (isCurrent) classes.push('current');
    if (isAnswered) classes.push('answered');
    else classes.push('unanswered');
    if (isFlagged) classes.push('flagged');

    return `
      <button class="${classes.join(' ')}" onclick="window.jumpToQuestion(${i})" aria-label="Question ${i + 1}">
        <span>${i + 1}</span>
        ${isAnswered ? '<i class="fa-solid fa-check jump-check-icon"></i>' : ''}
      </button>
    `;
  }).join('');
}

export function jumpToQuestion(idx) {
  if (!activeTestSession) return -1;
  const targetIdx = parseInt(idx, 10);
  if (isNaN(targetIdx) || targetIdx < 0 || targetIdx >= activeTestSession.test.questions.length) {
    return -1;
  }
  activeTestSession.idx = targetIdx;
  closeJumpDrawer();
  renderTestQuestion();
  return activeTestSession.idx;
}

// -------------------------------------------------------
// Test Results Screen & Upgrades
// -------------------------------------------------------
export function showTestResults() {
  if (!activeTestSession) return;
  const s = activeTestSession;
  const total = s.test.questions.length;
  const pct = total > 0 ? Math.round((s.score / total) * 100) : 0;
  const isPass = pct >= 60;

  const runnerScreen = document.getElementById('test-runner-screen');
  const resultsScreen = document.getElementById('test-results-screen');
  if (runnerScreen) runnerScreen.classList.add('hide');
  if (resultsScreen) resultsScreen.classList.remove('hide');

  const resScore = document.getElementById('res-score-pct');
  const resDetail = document.getElementById('res-score-detail');
  const resMsg = document.getElementById('res-score-msg');

  if (resScore) resScore.textContent = `${pct}%`;
  if (resDetail) resDetail.textContent = `${s.score} / ${total} Correct`;

  // Pass / Fail indicator
  let passFailBadge = document.getElementById('res-pass-fail-indicator');
  if (!passFailBadge && resDetail && resDetail.parentNode) {
    passFailBadge = document.createElement('div');
    passFailBadge.id = 'res-pass-fail-indicator';
    resDetail.parentNode.insertBefore(passFailBadge, resDetail.nextSibling);
  }
  if (passFailBadge) {
    passFailBadge.className = `test-pass-fail-badge ${isPass ? 'pass' : 'fail'}`;
    passFailBadge.innerHTML = isPass
      ? '<i class="fa-solid fa-circle-check"></i> 合格 (PASS — 60%+)'
      : '<i class="fa-solid fa-circle-xmark"></i> 不合格 (FAIL — Below 60%)';
  }

  endGistReviewSession();

  if (resMsg) {
    if (pct >= 85) {
      resMsg.innerHTML = '<span style="color:var(--green); font-weight:700;">合格圏内！ Outstanding mastery.</span>';
    } else if (pct >= 60) {
      resMsg.innerHTML = '<span style="color:var(--green); font-weight:700;">合格！ Passed. Good progress, keep drilling.</span>';
    } else {
      resMsg.innerHTML = '<span style="color:var(--red); font-weight:700;">不合格。 Keep drilling! Review missed items below.</span>';
    }
  }

  // Missed Questions Actions
  const missedCount = s.test.questions.filter((q, idx) => !s.answers[idx] || !s.answers[idx].wasCorrect).length;
  let actionContainer = document.getElementById('test-results-actions');
  if (!actionContainer) {
    const parentCard = resultsScreen ? resultsScreen.querySelector('div') : null;
    if (parentCard) {
      const oldBtnContainer = parentCard.querySelector('div[style*="justify-content:center"]');
      if (oldBtnContainer) oldBtnContainer.style.display = 'none';

      actionContainer = document.createElement('div');
      actionContainer.id = 'test-results-actions';
      actionContainer.className = 'test-results-action-grid';
      parentCard.appendChild(actionContainer);
    }
  }

  if (actionContainer) {
    actionContainer.innerHTML = `
      ${missedCount > 0 ? `
        <button id="btn-review-missed" class="btn btn-primary" onclick="window.reviewMissedTestQuestions()">
          <i class="fa-solid fa-rotate"></i> Review Missed Questions (${missedCount})
        </button>
        <button id="btn-send-missed-weak" class="btn btn-secondary" onclick="window.sendMissedTestsToWeakPoints()">
          <i class="fa-solid fa-fire"></i> Send Missed to Weak Points (${missedCount})
        </button>
      ` : `
        <div style="color:var(--green); font-size:0.95rem; font-weight:700; margin-bottom:0.5rem;">
          <i class="fa-solid fa-star"></i> Perfect score! No missed questions.
        </div>
      `}
      <button class="btn btn-ghost" onclick="window.exitTestToHub()">
        <i class="fa-solid fa-arrow-left"></i> Return to Tests
      </button>
    `;
  }
}

export function exitTestToHub() {
  endGistReviewSession();
  closeJumpDrawer();
  activeTestSession = null;
  state.activeTestSession = null;
  const runner = document.getElementById('test-runner-screen');
  const results = document.getElementById('test-results-screen');
  const hub = document.getElementById('test-hub-screen');

  if (runner) runner.classList.add('hide');
  if (results) results.classList.add('hide');
  if (hub) hub.classList.remove('hide');
}

// -------------------------------------------------------
// Send Missed Questions to Weak Points
// -------------------------------------------------------
export function sendMissedTestsToWeakPoints() {
  if (!activeTestSession) return 0;
  const s = activeTestSession;
  const missed = s.test.questions.filter((q, idx) => !s.answers[idx] || !s.answers[idx].wasCorrect);
  if (missed.length === 0) return 0;

  if (!state.stats) state.stats = {};

  missed.forEach(q => {
    let key = q.key;
    if (!key && q.targetWord) {
      key = q.targetWord.startsWith('V:') ? q.targetWord : `V:${q.targetWord}`;
    }
    if (!key && q.id) {
      key = q.id;
    }

    if (key) {
      const rec = getItemStats(key);
      rec.weight = Math.max(Number(rec.weight) || 1.0, 1.8);
      rec.isHard = true;
      rec.cause = 'test-mistake';
      rec.lastSeen = Date.now();
    }

    if (q.id && q.id !== key) {
      const idRec = getItemStats(q.id);
      idRec.weight = Math.max(Number(idRec.weight) || 1.0, 1.8);
      idRec.isHard = true;
      idRec.cause = 'test-mistake';
      idRec.lastSeen = Date.now();
    }
  });

  saveStats();
  if (typeof updateSidebarStats === 'function') {
    try { updateSidebarStats(); } catch {}
  }

  const btn = document.getElementById('btn-send-missed-weak');
  if (btn) {
    btn.innerHTML = `<i class="fa-solid fa-check"></i> Sent ${missed.length} Missed to Weak Points`;
    btn.disabled = true;
    btn.style.opacity = '0.8';
  }

  return missed.length;
}

// -------------------------------------------------------
// Review Missed Questions (Mini Study Session)
// -------------------------------------------------------
export function reviewMissedTestQuestions() {
  if (!activeTestSession) return [];
  const s = activeTestSession;
  const missed = s.test.questions.filter((q, idx) => !s.answers[idx] || !s.answers[idx].wasCorrect);
  if (missed.length === 0) {
    return [];
  }

  state.studyMode = 'flashcard';
  state.studyIsDrillHard = false;
  state.isDueReviewMode = false;
  state.drillOrigin = 'test';
  state.learnUnit = null;
  state.sessionItems = missed.map(q => ({
    ...q,
    type: q.category === 'kanji' ? 'kanji_exercise' : 'reading_question',
    question_ja: q.question,
    options: q.options || [],
    correctAnswer: q.correct,
    explanation_ja: q.explanation || (q.correctAnswerText ? `Correct: ${q.correctAnswerText}` : ''),
    lessonTitle: q.exerciseTitle || q.passageTitle || q.chapter || s.test.title || 'Missed Questions Review',
    answer: q.correctAnswerText || (q.options ? q.options[q.correct - 1] : '')
  }));
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = state.sessionItems.length;
  state.cardFlipped = false;

  const resultsScreen = document.getElementById('test-results-screen');
  const runnerScreen = document.getElementById('test-runner-screen');
  if (resultsScreen) resultsScreen.classList.add('hide');
  if (runnerScreen) runnerScreen.classList.add('hide');

  if (typeof window !== 'undefined' && typeof window.showView === 'function') {
    try { window.showView('study'); } catch {}
  }
  if (typeof window !== 'undefined' && typeof window.renderCard === 'function') {
    try { window.renderCard(); } catch {}
  }

  return state.sessionItems;
}

// -------------------------------------------------------
// Global Window Bindings
// -------------------------------------------------------
if (typeof window !== 'undefined') {
  window.initTestHub = initTestHub;
  window.getAllAvailableTests = getAllAvailableTests;
  window.renderTestCategoryTabs = renderTestCategoryTabs;
  window.filterTestCategory = filterTestCategory;
  window.renderTestCardsGrid = renderTestCardsGrid;
  window.startTestSession = startTestSession;
  window.renderTestQuestion = renderTestQuestion;
  window.submitQuestionAnswer = submitQuestionAnswer;
  window.advanceTestQuestion = advanceTestQuestion;
  window.showTestResults = showTestResults;
  window.exitTestToHub = exitTestToHub;
  window.openJumpDrawer = openJumpDrawer;
  window.closeJumpDrawer = closeJumpDrawer;
  window.jumpToQuestion = jumpToQuestion;
  window.toggleFlagCurrentQuestion = toggleFlagCurrentQuestion;
  window.renderJumpDrawerGrid = renderJumpDrawerGrid;
  window.sendMissedTestsToWeakPoints = sendMissedTestsToWeakPoints;
  window.reviewMissedTestQuestions = reviewMissedTestQuestions;
  window.getActiveTestSession = getActiveTestSession;
  window.getActiveTestCategory = getActiveTestCategory;
  window.setActiveTestCategory = setActiveTestCategory;
}
