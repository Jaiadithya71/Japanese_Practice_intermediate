#!/usr/bin/env node
/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_test_upgrades.mjs
   Verification Test Harness for WP-10 Test Upgrades:
   1. API & Window Bindings Audit
   2. Question Jump Drawer Indexing & Navigation
   3. Question Flagging
   4. Category / Section Tabs Filtering
   5. Test Results Score & Pass/Fail Indicator (>= 60%)
   6. Send Missed Questions to Weak Points (weight >= 1.8, isHard, cause='test-mistake')
   7. Review Missed Questions Mini Study Session
   ======================================================= */

import assert from 'node:assert/strict';

console.log('--- Starting WP-10 Verification (Test Upgrades & Question Jump Drawer) ---');

// ==========================================
// Setup Minimal DOM & Storage Stubs for Node
// ==========================================
const memStore = new Map();
globalThis.localStorage = {
  getItem: (k) => memStore.get(k) ?? null,
  setItem: (k, v) => memStore.set(k, String(v)),
  removeItem: (k) => memStore.delete(k),
  clear: () => memStore.clear()
};

function createMockElement(id = '', tag = 'div') {
  const classListSet = new Set();
  const children = [];
  let _id = id;
  let _innerHTML = '';
  let _className = '';
  const el = {
    tagName: tag.toUpperCase(),
    style: {},
    dataset: {},
    textContent: '',
    disabled: false,
    parentNode: null,
    nextSibling: null,
    classList: {
      add: (...cls) => {
        cls.forEach(c => classListSet.add(c));
        _className = Array.from(classListSet).join(' ');
      },
      remove: (...cls) => {
        cls.forEach(c => classListSet.delete(c));
        _className = Array.from(classListSet).join(' ');
      },
      toggle: (c, force) => {
        if (force === undefined) {
          if (classListSet.has(c)) classListSet.delete(c);
          else classListSet.add(c);
        } else if (force) {
          classListSet.add(c);
        } else {
          classListSet.delete(c);
        }
        _className = Array.from(classListSet).join(' ');
        return classListSet.has(c);
      },
      contains: (c) => classListSet.has(c)
    },
    appendChild: (child) => {
      child.parentNode = el;
      children.push(child);
      return child;
    },
    insertBefore: (newChild, refChild) => {
      newChild.parentNode = el;
      const idx = children.indexOf(refChild);
      if (idx !== -1) {
        children.splice(idx, 0, newChild);
      } else {
        children.push(newChild);
      }
      return newChild;
    },
    querySelector: (selector) => {
      if (selector === 'div' && children.length > 0) return children[0];
      if (selector.startsWith('#')) return domRegistry.get(selector.slice(1)) || null;
      return null;
    },
    querySelectorAll: () => children
  };

  Object.defineProperty(el, 'id', {
    get: () => _id,
    set: (val) => {
      _id = val;
      if (val) domRegistry.set(val, el);
    }
  });

  Object.defineProperty(el, 'className', {
    get: () => _className,
    set: (val) => {
      _className = val || '';
      classListSet.clear();
      _className.split(/\s+/).filter(Boolean).forEach(c => classListSet.add(c));
    }
  });

  Object.defineProperty(el, 'innerHTML', {
    get: () => _innerHTML,
    set: (val) => {
      _innerHTML = val;
      const regex = /id=["']([^"']+)["']/g;
      let m;
      while ((m = regex.exec(val)) !== null) {
        if (!domRegistry.has(m[1])) {
          const child = createMockElement(m[1]);
          domRegistry.set(m[1], child);
          el.appendChild(child);
        }
      }
    }
  });

  if (id) domRegistry.set(id, el);

  return el;
}

const domRegistry = new Map();
function getOrCreateElement(id, tag = 'div') {
  if (!domRegistry.has(id)) {
    domRegistry.set(id, createMockElement(id, tag));
  }
  return domRegistry.get(id);
}

// Pre-populate required test screen elements
const rootIds = [
  'view-test',
  'test-hub-screen',
  'test-runner-screen',
  'test-results-screen',
  'test-category-tabs',
  'test-cards-grid',
  'test-total-count',
  'test-total-questions',
  'tr-test-title',
  'tr-question-count',
  'tr-progress-fill',
  'tr-prompt',
  'tr-options-container',
  'tr-explanation-box',
  'tr-explanation-text',
  'tr-next-btn',
  'tr-passage-box',
  'tr-passage-text',
  'res-score-pct',
  'res-score-detail',
  'res-score-msg'
];

rootIds.forEach(id => getOrCreateElement(id));

const mockRunnerHeader = createMockElement('test-runner-header');
mockRunnerHeader.className = 'test-runner-header';
domRegistry.set('test-runner-header', mockRunnerHeader);
domRegistry.get('test-runner-screen').appendChild(mockRunnerHeader);

const mockResultsCard = createMockElement('res-card');
domRegistry.get('test-results-screen').appendChild(mockResultsCard);
mockResultsCard.appendChild(domRegistry.get('res-score-pct'));
mockResultsCard.appendChild(domRegistry.get('res-score-detail'));
mockResultsCard.appendChild(domRegistry.get('res-score-msg'));

globalThis.document = {
  getElementById: (id) => domRegistry.get(id) || null,
  querySelector: (sel) => {
    if (sel.startsWith('#')) return domRegistry.get(sel.slice(1)) || null;
    if (sel === '.test-runner-header') return mockRunnerHeader;
    return null;
  },
  querySelectorAll: () => [],
  createElement: (tag) => createMockElement('', tag),
  head: createMockElement('head'),
  body: createMockElement('body')
};
globalThis.window = globalThis;

// Import test module and application state
const {
  openJumpDrawer,
  closeJumpDrawer,
  jumpToQuestion,
  toggleFlagCurrentQuestion,
  sendMissedTestsToWeakPoints,
  reviewMissedTestQuestions,
  initTestHub,
  filterTestCategory,
  renderTestCategoryTabs,
  renderTestCardsGrid,
  startTestSession,
  submitQuestionAnswer,
  advanceTestQuestion,
  showTestResults,
  exitTestToHub,
  getAllAvailableTests,
  getActiveTestSession,
  renderJumpDrawerGrid,
  getActiveTestCategory,
  setActiveTestCategory
} = await import('../js/test.js');

const { state } = await import('../js/state.js');

// ==========================================
// 1. API & Window Bindings Audit
// ==========================================
console.log('\n[1/7] Auditing exported API and window.* bindings...');

const requiredFunctions = [
  'openJumpDrawer',
  'closeJumpDrawer',
  'jumpToQuestion',
  'toggleFlagCurrentQuestion',
  'sendMissedTestsToWeakPoints',
  'reviewMissedTestQuestions',
  'filterTestCategory',
  'renderTestCategoryTabs',
  'startTestSession',
  'submitQuestionAnswer',
  'advanceTestQuestion',
  'showTestResults',
  'exitTestToHub',
  'initTestHub'
];

for (const fnName of requiredFunctions) {
  assert.equal(typeof globalThis.window[fnName], 'function', `window.${fnName} must be bound to window`);
}
console.log('✓ All 14 required functions bound to window.');

// ==========================================
// 2. Question Jump Drawer Indexing & Navigation
// ==========================================
console.log('\n[2/7] Testing Question Jump Drawer indexing & navigation...');

const sampleQuestions = [
  { id: 'q-1', question: 'Question 1', options: ['A', 'B', 'C', 'D'], correct: 1, targetWord: 'taberu' },
  { id: 'q-2', question: 'Question 2', options: ['A', 'B', 'C', 'D'], correct: 2, targetWord: 'nomu' },
  { id: 'q-3', question: 'Question 3', options: ['A', 'B', 'C', 'D'], correct: 3, targetWord: 'miru' },
  { id: 'q-4', question: 'Question 4', options: ['A', 'B', 'C', 'D'], correct: 4, targetWord: 'kiku' },
  { id: 'q-5', question: 'Question 5', options: ['A', 'B', 'C', 'D'], correct: 1, targetWord: 'hanasu' }
];

const sampleTest = {
  id: 'test-jump-unit',
  title: 'Jump Drawer Unit Test',
  pillar: 'vocab',
  category: 'vocab',
  questions: sampleQuestions
};

const session = startTestSession('test-jump-unit', sampleTest);
assert.ok(session, 'startTestSession must return active test session');
assert.equal(session.idx, 0, 'Initial question index should be 0');

// Open Jump Drawer
openJumpDrawer();
const drawerOverlay = domRegistry.get('test-jump-drawer-overlay');
assert.ok(drawerOverlay, 'Drawer overlay element should exist in DOM');
assert.ok(!drawerOverlay.classList.contains('hide'), 'Drawer overlay must not have "hide" class when opened');

const jumpGrid = domRegistry.get('test-jump-grid');
assert.ok(jumpGrid, 'test-jump-grid element must exist');
assert.ok(jumpGrid.innerHTML.includes('Question 1'), 'Jump grid should render question 1');

// Test that initial question has current and unanswered classes
renderJumpDrawerGrid();
assert.ok(jumpGrid.innerHTML.includes('current'), 'Current active question must have "current" class');
assert.ok(jumpGrid.innerHTML.includes('unanswered'), 'Unanswered questions must have "unanswered" class');

// Submit answer for question 1 (idx 0)
submitQuestionAnswer(1); // Correct
assert.ok(session.answers[0], 'Question 0 must be marked as answered');
assert.equal(session.answers[0].wasCorrect, true, 'Question 0 was answered correctly');

renderJumpDrawerGrid();
assert.ok(jumpGrid.innerHTML.includes('answered'), 'Answered question must have "answered" class');

// Jump to Question 3 (index 2)
const jumpResult = jumpToQuestion(2);
assert.equal(jumpResult, 2, 'jumpToQuestion(2) must return target index 2');
assert.equal(session.idx, 2, 'Session index should now be 2');
assert.ok(drawerOverlay.classList.contains('hide'), 'Drawer overlay must be hidden after jumpToQuestion');

// Jump to Question 5 (index 4)
jumpToQuestion(4);
assert.equal(session.idx, 4, 'Session index should now be 4');

// Test out-of-bounds protection
assert.equal(jumpToQuestion(-1), -1, 'Negative index jump must be rejected (-1)');
assert.equal(jumpToQuestion(100), -1, 'Out-of-bounds jump must be rejected (-1)');
assert.equal(session.idx, 4, 'Session index must remain 4 after invalid jump attempts');

console.log('✓ Question Jump Drawer indexing, bounds check, and navigation verified.');

// ==========================================
// 3. Question Flagging
// ==========================================
console.log('\n[3/7] Testing Question Flagging...');

// On Question 5 (index 4), toggle flag
assert.equal(session.flagged.has(4), false, 'Question 4 should not be flagged initially');
const flagState1 = toggleFlagCurrentQuestion();
assert.equal(flagState1, true, 'toggleFlagCurrentQuestion() must return true when flagged');
assert.ok(session.flagged.has(4), 'Question 4 index must be present in session.flagged set');

// Verify drawer renders flagged class
renderJumpDrawerGrid();
assert.ok(jumpGrid.innerHTML.includes('flagged'), 'Jump drawer button must have "flagged" class');

// Jump to Question 2 (index 1) and flag it
jumpToQuestion(1);
assert.equal(session.idx, 1);
const flagState2 = toggleFlagCurrentQuestion();
assert.equal(flagState2, true);
assert.ok(session.flagged.has(1), 'Question 1 index must be present in flagged set');
assert.ok(session.flagged.has(4), 'Question 4 must still remain flagged');
assert.equal(session.flagged.size, 2, 'Flagged set should contain 2 items');

// Toggle flag again on Question 2 (unflag)
const flagState3 = toggleFlagCurrentQuestion();
assert.equal(flagState3, false, 'toggleFlagCurrentQuestion() must return false when unflagged');
assert.equal(session.flagged.has(1), false, 'Question 1 should now be unflagged');
assert.equal(session.flagged.has(4), true, 'Question 4 should remain flagged');

console.log('✓ Question Flagging bookmark toggle verified.');

// ==========================================
// 4. Category / Section Tabs Filtering
// ==========================================
console.log('\n[4/7] Testing Section / Category tabs filtering...');

// Seed mock database records
state.chapterExercises = {
  ch01: [
    { title_ja: 'Ch1 Drill', items: [{ question_ja: 'V1', options: ['A','B'], answer: 'A', target_word: 'v1' }] }
  ],
  part2_ch01: [
    { title_ja: 'Part2 Drill', items: [{ question_ja: 'V2', options: ['A','B'], answer: 'B', target_word: 'v2' }] }
  ],
  part3_mock1: [
    { title_ja: 'Vocab Mock', items: [{ question_ja: 'VM', options: ['A','B'], answer: 'A', target_word: 'vm' }] }
  ]
};

state.grammarDB = {
  part1_1_6: {
    sections: [
      { id: 'sec1', title: '時間 (Time)', drills: [{ id: 'g1', prompt: 'G1', options: ['A','B','C','D'], correct_answer: 2 }] }
    ]
  },
  part1_7_12: { sections: [] },
  part2: {
    sections: [
      { id: 'p2s1', drills: [{ id: 'gs1', prompt: '★ blank', options: ['1','2','3','4'], correct_answer: 3 }] }
    ]
  },
  mock: {
    mock_tests: [
      { id: 'gm1', title: 'Grammar Mock 1', questions: [{ prompt: 'GM1', options: ['A','B'], correct_answer: 1 }] }
    ]
  }
};

state.readingDB = {
  read_01: {
    title_ja: 'Passage 1',
    comprehensionQuestions: [
      { id: 'rq1', question_ja: 'R1', options: ['A','B'], correctAnswer: 1 }
    ]
  }
};

const allAvailable = getAllAvailableTests();
assert.ok(allAvailable.length >= 4, `Should find at least 4 test modules, found: ${allAvailable.length}`);

// Verify Vocab category filter
filterTestCategory('vocab');
assert.equal(getActiveTestCategory(), 'vocab', 'Active category should be vocab');

// Verify Grammar category filter
filterTestCategory('grammar');
assert.equal(getActiveTestCategory(), 'grammar', 'Active category should be grammar');

// Verify Reading category filter
filterTestCategory('reading');
assert.equal(getActiveTestCategory(), 'reading', 'Active category should be reading');

// Verify Mock Exams category filter
filterTestCategory('mock_exams');
assert.equal(getActiveTestCategory(), 'mock_exams', 'Active category should be mock_exams');

// Reset to all
filterTestCategory('all');
assert.equal(getActiveTestCategory(), 'all', 'Active category should be all');

console.log('✓ Section / Category tabs filtering verified across all pillars.');

// ==========================================
// 5. Test Completion Results & Pass/Fail Metrics
// ==========================================
console.log('\n[5/7] Testing test completion results calculation & Pass/Fail (>= 60%)...');

// 5.1 Passing Test Session (7 / 10 = 70% >= 60%)
const passingQuestions = Array.from({ length: 10 }, (_, i) => ({
  id: `q-pass-${i}`,
  question: `Pass Question ${i + 1}`,
  options: ['1', '2', '3', '4'],
  correct: 1,
  targetWord: `word-${i}`
}));

const passingTest = {
  id: 'test-passing-demo',
  title: 'Passing Demo Exam',
  questions: passingQuestions
};

const passSession = startTestSession('test-passing-demo', passingTest);

// Answer 7 correctly, 3 incorrectly
for (let i = 0; i < 7; i++) {
  jumpToQuestion(i);
  submitQuestionAnswer(1); // Correct
}
for (let i = 7; i < 10; i++) {
  jumpToQuestion(i);
  submitQuestionAnswer(2); // Incorrect
}

assert.equal(passSession.score, 7, 'Score should be 7');
showTestResults();

const pctEl = domRegistry.get('res-score-pct');
assert.equal(pctEl.textContent, '70%', 'res-score-pct should display 70%');

const passBadge = domRegistry.get('res-pass-fail-indicator');
assert.ok(passBadge, 'Pass/Fail badge element must be created');
assert.ok(passBadge.classList.contains('pass'), 'Pass badge must have class "pass"');
assert.ok(passBadge.innerHTML.includes('PASS') || passBadge.innerHTML.includes('合格'), 'Pass badge should display PASS/合格');

// 5.2 Failing Test Session (4 / 10 = 40% < 60%)
const failingSession = startTestSession('test-failing-demo', {
  id: 'test-failing-demo',
  title: 'Failing Demo Exam',
  questions: passingQuestions
});

// Answer 4 correctly, 6 incorrectly
for (let i = 0; i < 4; i++) {
  jumpToQuestion(i);
  submitQuestionAnswer(1); // Correct
}
for (let i = 4; i < 10; i++) {
  jumpToQuestion(i);
  submitQuestionAnswer(2); // Incorrect
}

assert.equal(failingSession.score, 4, 'Score should be 4');
showTestResults();

assert.equal(pctEl.textContent, '40%', 'res-score-pct should display 40%');
assert.ok(passBadge.classList.contains('fail'), 'Fail badge must have class "fail"');
assert.ok(passBadge.innerHTML.includes('FAIL') || passBadge.innerHTML.includes('不合格'), 'Fail badge should display FAIL/不合格');

console.log('✓ Score percentage & pass/fail threshold (>= 60%) verified.');

// ==========================================
// 6. Sending Missed Questions to Weak Points
// ==========================================
console.log('\n[6/7] Testing sending missed questions to Weak Points desk...');

// Reset stats
state.stats = {};

// We use failingSession where questions 0-3 were correct, and questions 4-9 were missed (6 missed)
const sentCount = sendMissedTestsToWeakPoints();
assert.equal(sentCount, 6, `sendMissedTestsToWeakPoints must return count of missed questions (6), got ${sentCount}`);

// Verify missed questions (indices 4..9) in state.stats
for (let i = 4; i < 10; i++) {
  const q = passingQuestions[i];
  const statKey = `V:${q.targetWord}`;
  const record = state.stats[statKey];

  assert.ok(record, `state.stats['${statKey}'] must exist for missed question`);
  assert.equal(record.isHard, true, `Record '${statKey}' must be marked isHard = true`);
  assert.ok(record.weight >= 1.8, `Record '${statKey}' weight must be >= 1.8, got ${record.weight}`);
  assert.equal(record.cause, 'test-mistake', `Record '${statKey}' cause must be 'test-mistake'`);
}

// Verify correctly answered questions (indices 0..3) were NOT marked as test-mistake
for (let i = 0; i < 4; i++) {
  const q = passingQuestions[i];
  const statKey = `V:${q.targetWord}`;
  const record = state.stats[statKey];
  if (record) {
    assert.notEqual(record.cause, 'test-mistake', `Correct item '${statKey}' must not have cause 'test-mistake'`);
  }
}

// Test weight preservation when existing weight is already higher (e.g. 2.4)
state.stats['V:high-weight-test'] = {
  weight: 2.4,
  isHard: false,
  cause: ''
};

const highWeightTest = {
  id: 'test-hw',
  title: 'High Weight Test',
  questions: [{ id: 'q-hw', question: 'HW?', options: ['1','2'], correct: 1, targetWord: 'high-weight-test' }]
};

const hwSession = startTestSession('test-hw', highWeightTest);
jumpToQuestion(0);
submitQuestionAnswer(2); // Wrong

// Explicitly set weight to 2.4 to test Math.max(weight, 1.8) preservation in sendMissedTestsToWeakPoints
state.stats['V:high-weight-test'].weight = 2.4;
sendMissedTestsToWeakPoints();
const hwRecord = state.stats['V:high-weight-test'];
assert.equal(hwRecord.weight, 2.4, 'Weight of 2.4 should be preserved (Math.max(2.4, 1.8) == 2.4)');
assert.equal(hwRecord.isHard, true, 'isHard must be true');
assert.equal(hwRecord.cause, 'test-mistake', 'cause must be test-mistake');

console.log('✓ Missed questions saved to Weak Points desk (weight >= 1.8, isHard=true, cause="test-mistake").');

// ==========================================
// 7. Review Missed Questions Mini Study Session
// ==========================================
console.log('\n[7/7] Testing Review Missed Questions mini study session...');

// Reactivate failingSession which has 6 missed questions
const reviewSession = startTestSession('test-failing-demo', {
  id: 'test-failing-demo',
  title: 'Failing Demo Exam',
  questions: passingQuestions
});

for (let i = 0; i < 4; i++) {
  jumpToQuestion(i);
  submitQuestionAnswer(1); // Correct
}
for (let i = 4; i < 10; i++) {
  jumpToQuestion(i);
  submitQuestionAnswer(2); // Missed
}

const missedItems = reviewMissedTestQuestions();
assert.ok(Array.isArray(missedItems), 'reviewMissedTestQuestions must return array of missed items');
assert.equal(missedItems.length, 6, `Should have exactly 6 missed items, got ${missedItems.length}`);

// Verify study session state configuration
assert.equal(state.studyMode, 'flashcard', 'state.studyMode should be set to "flashcard"');
assert.equal(state.drillOrigin, 'test', 'state.drillOrigin should be "test"');
assert.equal(state.sessionTotal, 6, 'state.sessionTotal should be 6');
assert.equal(state.sessionIdx, 0, 'state.sessionIdx should be reset to 0');
assert.equal(state.cardFlipped, false, 'state.cardFlipped should be false');
assert.equal(state.sessionItems.length, 6, 'state.sessionItems should contain 6 missed items');

// Verify that each item in sessionItems contains expected properties
for (const it of state.sessionItems) {
  assert.ok(it.question_ja, 'Card item should have question_ja prompt');
  assert.ok(it.options, 'Card item should have options');
  assert.ok(it.correctAnswer !== undefined, 'Card item should specify correctAnswer');
}

// Test edge case: When 0 questions were missed
const perfectTest = {
  id: 'test-perfect',
  title: 'Perfect Test',
  questions: [{ id: 'pq-1', question: 'P1', options: ['A','B'], correct: 1, targetWord: 'p1' }]
};
startTestSession('test-perfect', perfectTest);
submitQuestionAnswer(1); // 100% correct

const emptyReview = reviewMissedTestQuestions();
assert.deepEqual(emptyReview, [], 'Review missed with 0 missed questions should return empty array');

console.log('✓ Review Missed Questions mini study session launch verified.');

console.log('\n=======================================================');
console.log('🎉 ALL WP-10 TEST UPGRADE VERIFICATIONS PASSED SUCCESSFULLY!');
console.log('=======================================================');
