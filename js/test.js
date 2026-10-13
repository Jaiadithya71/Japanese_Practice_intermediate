/* =======================================================
   NIHONGO INTERMEDIATE — test.js
   Full Chapter Tests, Review Exams & Practice Simulator
   Faithfully matching Nihongo Trainer (4Q/5Q) with Poco M7 Mobile Tuning
   ======================================================= */

import { state } from './state.js';
import { updateItemStats } from './srs.js';

let activeTestSession = null;

export function initTestHub() {
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
            } else if (!isNaN(parseInt(ansText))) {
              correctIdx = parseInt(ansText);
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

  // 2. Kanji Lesson Drills & Mock Tests
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
            correct: parseInt(it.answer) || 1,
            correctAnswerText: (it.options || [])[(parseInt(it.answer) || 1) - 1] || '',
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
          passageText: (les.passage && les.passage.sentences) ? les.passage.sentences.map(s => s.japanese).join('\n') : '',
          question: q.question_ja || q.question || '',
          options: q.options || [],
          correct: q.correctAnswer || q.correct || 1,
          correctAnswerText: (q.options || [])[(q.correctAnswer || 1) - 1] || '',
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

  return tests;
}

let activeTestCategory = 'all';
let testSearchQuery = '';

export function renderTestCategoryTabs() {
  const container = document.getElementById('test-category-tabs');
  if (!container) return;

  const categories = [
    { id: 'all', label: 'All Tests' },
    { id: 'vocab_topics', label: 'Vocab Topics (Ch 1–21)' },
    { id: 'vocab_characteristics', label: 'Characteristics (Ch 1–8)' },
    { id: 'vocab_reviews', label: 'Review Tests' },
    { id: 'kanji_drills', label: 'Kanji Drills' },
    { id: 'reading_tests', label: 'Reading Dokkai' },
    { id: 'mock_exams', label: 'Official Mocks' }
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

window.filterTestCategory = filterTestCategory;

export function renderTestCardsGrid() {
  const grid = document.getElementById('test-cards-grid');
  if (!grid) return;

  const allTests = getAllAvailableTests();
  let filtered = allTests;

  if (activeTestCategory !== 'all') {
    filtered = filtered.filter(t => t.category === activeTestCategory);
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

export function startTestSession(testId) {
  const allTests = getAllAvailableTests();
  const target = allTests.find(t => t.id === testId);
  if (!target || target.questions.length === 0) {
    alert('This test is currently empty or still being processed.');
    return;
  }

  activeTestSession = {
    test: target,
    idx: 0,
    score: 0,
    answers: {}, // idx -> { selected, correct, wasCorrect }
    answered: false
  };

  document.getElementById('test-hub-screen').classList.add('hide');
  document.getElementById('test-results-screen').classList.add('hide');
  document.getElementById('test-runner-screen').classList.remove('hide');

  renderTestQuestion();
}

window.startTestSession = startTestSession;

export function renderTestQuestion() {
  if (!activeTestSession) return;
  const s = activeTestSession;
  const q = s.test.questions[s.idx];

  // Header & Progress
  const titleEl = document.getElementById('tr-test-title');
  const countEl = document.getElementById('tr-question-count');
  const fillEl = document.getElementById('tr-progress-fill');

  if (titleEl) titleEl.textContent = s.test.title;
  if (countEl) countEl.textContent = `${s.idx + 1} / ${s.test.questions.length}`;
  if (fillEl) fillEl.style.width = `${((s.idx) / s.test.questions.length) * 100}%`;

  // Question & Text
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

  // Render Options
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
    document.getElementById('tr-next-btn').style.display = 'none';
  } else {
    // Question already answered (revealed)
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

    // Show Explanation
    const explanationEl = document.getElementById('tr-explanation-box');
    const explText = document.getElementById('tr-explanation-text');
    if (explanationEl && explText) {
      explanationEl.style.display = 'block';
      explText.innerHTML = `
        <strong>${currentAnswer.wasCorrect ? '正解！ (Correct)' : '不正解 (Incorrect)'}</strong> — 
        正解は「${q.correctAnswerText || (q.options || [])[q.correct - 1]}」です。<br>
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

  // If question was missed, flag item in SRS as hard
  if (!wasCorrect && q.targetWord) {
    updateItemStats(`V:${q.targetWord}`, false);
  } else if (wasCorrect && q.targetWord) {
    updateItemStats(`V:${q.targetWord}`, true);
  }

  renderTestQuestion();
}

window.submitQuestionAnswer = submitQuestionAnswer;

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

window.advanceTestQuestion = advanceTestQuestion;

export function showTestResults() {
  if (!activeTestSession) return;
  const s = activeTestSession;
  const total = s.test.questions.length;
  const pct = Math.round((s.score / total) * 100);

  document.getElementById('test-runner-screen').classList.add('hide');
  document.getElementById('test-results-screen').classList.remove('hide');

  const resScore = document.getElementById('res-score-pct');
  const resDetail = document.getElementById('res-score-detail');
  const resMsg = document.getElementById('res-score-msg');

  if (resScore) resScore.textContent = `${pct}%`;
  if (resDetail) resDetail.textContent = `${s.score} / ${total} Correct`;
  if (resMsg) {
    if (pct >= 85) {
      resMsg.innerHTML = '<span style="color:var(--green)">合格圏内！ Outstanding mastery.</span>';
    } else if (pct >= 65) {
      resMsg.innerHTML = '<span style="color:var(--amber)">Good progress! Review the missed questions on your train commute.</span>';
    } else {
      resMsg.innerHTML = '<span style="color:var(--red)">Keep drilling! Missed words have been added to your Weak Points desk.</span>';
    }
  }
}

export function exitTestToHub() {
  activeTestSession = null;
  document.getElementById('test-runner-screen').classList.add('hide');
  document.getElementById('test-results-screen').classList.add('hide');
  document.getElementById('test-hub-screen').classList.remove('hide');
}

window.exitTestToHub = exitTestToHub;
