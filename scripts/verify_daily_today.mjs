/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_daily_today.mjs
   Test Harness for Habit Engine (daily.js) & Today Dashboard (today.js)
   WP-6 Verification Suite
   ======================================================= */

import assert from 'assert';
import {
  buildDailySession,
  nextBestAction,
  getDailyPlanStatus,
  findNextKanjiChunk,
  findNextVocabBatch,
  findWeakestGrammarCluster,
  buildMiniCheckQuestions
} from '../js/daily.js';
import {
  renderHeatmapGridHtml,
  renderForecastBarsHtml,
  getReadinessStats
} from '../js/today.js';
import { getHeatmap30, getCurrentStreak, logActivity, clearDaylog } from '../js/daylog.js';
import { istNow, istDateKey } from '../js/time.js';
import { forecast } from '../js/planner.js';
import { BACKLOG_THRESHOLD } from '../js/config.js';

let passedTests = 0;
let totalTests = 0;

function it(name, fn) {
  totalTests++;
  try {
    fn();
    console.log(`  ✓ ${name}`);
    passedTests++;
  } catch (err) {
    console.error(`  ✗ ${name}`);
    console.error(err);
    process.exitCode = 1;
  }
}

console.log('========================================================');
console.log('Running Habit Engine & Today Dashboard Verification (WP-6)');
console.log('========================================================\n');

// -----------------------------------------------------------------
// 1. nextBestAction() Tests
// -----------------------------------------------------------------
console.log('[1/4] Testing nextBestAction() recommendations...');

it('Recommends Morning Review when time < 12:00 IST and reviews due', () => {
  // 09:00 AM IST (UTC 03:30)
  const morningDate = new Date('2026-10-14T03:30:00Z');
  const action = nextBestAction({
    now: morningDate,
    dueCount: 28,
    planStatus: { hasUnfinishedNew: true, items: [] }
  });

  assert.strictEqual(action.type, 'morning-review');
  assert.strictEqual(action.action, 'review');
  assert.strictEqual(action.dueCount, 28);
  assert.ok(action.estMinutes > 0, 'Estimated minutes should be > 0');
  assert.ok(action.label.includes('28 due'), 'Label should mention due count');
});

it('Recommends Evening Intake when time >= 12:00 IST and plan has unfinished new items', () => {
  // 18:00 PM IST (UTC 12:30)
  const eveningDate = new Date('2026-10-14T12:30:00Z');
  const mockPlan = {
    hasUnfinishedNew: true,
    items: [
      { id: 'review', completed: true, target: 10 },
      { id: 'kanji', completed: false, target: 12, label: 'Chunk 1', detail: 'Lesson 1', handler: 'startKanjiRunner(1)' },
      { id: 'vocab', completed: false, target: 10 },
      { id: 'grammar', completed: false, target: 2 },
      { id: 'reading', completed: false, target: 1 }
    ]
  };

  const action = nextBestAction({
    now: eveningDate,
    dueCount: 15,
    planStatus: mockPlan
  });

  assert.strictEqual(action.type, 'evening-intake');
  assert.strictEqual(action.action, 'kanji');
  assert.ok(action.handler.includes('startKanjiRunner'), 'Should provide kanji handler');
});

it('Recommends Review Due when evening intake is finished but reviews remain', () => {
  // 19:30 PM IST (UTC 14:00)
  const eveningDate = new Date('2026-10-14T14:00:00Z');
  const mockPlan = {
    hasUnfinishedNew: false, // all new items completed
    items: [
      { id: 'review', completed: false, target: 14 },
      { id: 'kanji', completed: true },
      { id: 'vocab', completed: true },
      { id: 'grammar', completed: true },
      { id: 'reading', completed: true }
    ]
  };

  const action = nextBestAction({
    now: eveningDate,
    dueCount: 14,
    planStatus: mockPlan
  });

  assert.strictEqual(action.type, 'review-due');
  assert.strictEqual(action.action, 'review');
  assert.strictEqual(action.dueCount, 14);
  assert.ok(action.label.includes('14 due'));
});

it('Recommends Quick 5 when all caught up and plan finished', () => {
  const mockPlan = {
    hasUnfinishedNew: false,
    allDone: true,
    items: [
      { id: 'review', completed: true },
      { id: 'kanji', completed: true },
      { id: 'vocab', completed: true },
      { id: 'grammar', completed: true },
      { id: 'reading', completed: true }
    ]
  };

  const action = nextBestAction({
    dueCount: 0,
    planStatus: mockPlan
  });

  assert.strictEqual(action.type, 'caught-up');
  assert.strictEqual(action.action, 'quick5');
  assert.ok(action.label.includes('Quick 5?'), 'Label should offer Quick 5');
});

// -----------------------------------------------------------------
// 2. buildDailySession() Tests
// -----------------------------------------------------------------
console.log('\n[2/4] Testing buildDailySession() 7-step queue construction...');

it('Constructs complete 7-step queue with correct slots and skippable flags', () => {
  const mockDb = {
    stats: {
      'V:v01-001': { reps: 3, interval: 7, nextDue: Date.now() - 1000 },
      'K:日': { reps: 2, interval: 4, nextDue: Date.now() - 5000 },
      'V:bad1': { reps: 5, weight: 2.5, leech: true, lapses: 6 },
      'V:bad2': { reps: 2, weight: 2.1, isHard: true, lapses: 3 }
    },
    vocabDB: {
      part1_01: [
        { id: 'v01-002', japanese: '学校', english: 'school' },
        { id: 'v01-003', japanese: '先生', english: 'teacher' }
      ]
    },
    kanjiDB: {
      '日': { kanji: '日', lesson_number: 1, order: 1, target_words: [{ term_ja: '日曜日', reading: 'にちようび' }] },
      '月': { kanji: '月', lesson_number: 1, order: 2, target_words: [{ term_ja: '月曜日', reading: 'げつようび' }] },
      '火': { kanji: '火', lesson_number: 1, order: 3, target_words: [{ term_ja: '火曜日', reading: 'かようび' }] }
    },
    kanjiLessons: [{ lesson_number: 1, title_ja: '自然' }],
    grammarDB: {
      index: [
        { id: 'P1-1', title_ja: '〜際（に）', meaning_en: 'at the time of' },
        { id: 'P1-2', title_ja: '〜に際して', meaning_en: 'on the occasion of' }
      ]
    },
    readingDB: {
      r01: { id: 'r01', title_ja: '日本の祭り', comprehensionQuestions: [{ id: 'q1', question_ja: '?' }] }
    }
  };

  const session = buildDailySession({ state: mockDb });

  assert.ok(session.steps, 'Should produce steps array');
  assert.strictEqual(session.steps.length, 7, 'Should produce exactly 7 steps');

  // Step 1: Review due (Morning, Not skippable)
  const s1 = session.steps[0];
  assert.strictEqual(s1.step, 1);
  assert.strictEqual(s1.id, 'review-due');
  assert.strictEqual(s1.slot, 'morning');
  assert.strictEqual(s1.skippable, false);

  // Step 2: Weak round (Morning, Skippable, leeches first)
  const s2 = session.steps[1];
  assert.strictEqual(s2.step, 2);
  assert.strictEqual(s2.id, 'weak-round');
  assert.strictEqual(s2.slot, 'morning');
  assert.strictEqual(s2.skippable, true);
  assert.ok(s2.items.length > 0, 'Should find weak items');
  assert.strictEqual(s2.items[0].key, 'V:bad1', 'Leech should be ordered first');

  // Step 3: New kanji chunk (Evening, Skippable)
  const s3 = session.steps[2];
  assert.strictEqual(s3.step, 3);
  assert.strictEqual(s3.id, 'new-kanji');
  assert.strictEqual(s3.slot, 'evening');
  assert.strictEqual(s3.skippable, true);
  assert.strictEqual(s3.count, 3, 'Should chunk 3 kanji');

  // Step 4: New vocab (Evening, Skippable)
  const s4 = session.steps[3];
  assert.strictEqual(s4.step, 4);
  assert.strictEqual(s4.id, 'new-vocab');
  assert.strictEqual(s4.slot, 'evening');
  assert.strictEqual(s4.skippable, true);

  // Step 5: New grammar (Evening, Skippable)
  const s5 = session.steps[4];
  assert.strictEqual(s5.step, 5);
  assert.strictEqual(s5.id, 'new-grammar');
  assert.strictEqual(s5.slot, 'evening');
  assert.strictEqual(s5.skippable, true);
  assert.ok(s5.weakestCluster, 'Should identify weakest cluster');

  // Step 6: Read one passage (Evening, Skippable)
  const s6 = session.steps[5];
  assert.strictEqual(s6.step, 6);
  assert.strictEqual(s6.id, 'reading-passage');
  assert.strictEqual(s6.slot, 'evening');
  assert.strictEqual(s6.skippable, true);

  // Step 7: Mini-check (Evening, Skippable, 6-8 questions)
  const s7 = session.steps[6];
  assert.strictEqual(s7.step, 7);
  assert.strictEqual(s7.id, 'mini-check');
  assert.strictEqual(s7.slot, 'evening');
  assert.strictEqual(s7.skippable, true);
});

it('Pauses intake steps when catch-up mode is triggered (> 80 due)', () => {
  const hugeStats = {};
  for (let i = 0; i < 90; i++) {
    hugeStats[`V:w${i}`] = { reps: 1, interval: 1, nextDue: Date.now() - 10000 };
  }
  const mockDb = { stats: hugeStats };

  const session = buildDailySession({ state: mockDb });
  assert.strictEqual(session.isCatchUp, true, 'isCatchUp should be true');
  assert.strictEqual(session.steps[2].paused, true, 'New kanji step should be paused');
  assert.strictEqual(session.steps[3].paused, true, 'New vocab step should be paused');
  assert.strictEqual(session.steps[4].paused, true, 'New grammar step should be paused');
});

// -----------------------------------------------------------------
// 3. getDailyPlanStatus() Checklist Tests
// -----------------------------------------------------------------
console.log('\n[3/4] Testing getDailyPlanStatus() checklist matching...');

it('Generates status checklist matching daylog activities against quotas', () => {
  clearDaylog();

  // Fresh day with 0 activity
  const emptyStatus = getDailyPlanStatus({
    dueCount: 15,
    profile: 'standard',
    dayRecord: {
      reviews: 0,
      newCards: 0,
      pillars: { vocab: 0, kanji: 0, grammar: 0, reading: 0 }
    }
  });

  assert.strictEqual(emptyStatus.totalCount, 5);
  assert.strictEqual(emptyStatus.completedCount, 0);
  assert.strictEqual(emptyStatus.hasUnfinishedNew, true);
  assert.strictEqual(emptyStatus.allDone, false);

  // Simulate full completion in daylog
  const completeStatus = getDailyPlanStatus({
    dueCount: 0,
    profile: 'standard',
    dayRecord: {
      reviews: 20,
      newCards: 25,
      pillars: { vocab: 10, kanji: 12, grammar: 2, reading: 1 }
    }
  });

  assert.strictEqual(completeStatus.completedCount, 5);
  assert.strictEqual(completeStatus.hasUnfinishedNew, false);
  assert.strictEqual(completeStatus.allDone, true);

  const ids = completeStatus.items.map(it => it.id);
  assert.deepStrictEqual(ids, ['review', 'kanji', 'vocab', 'grammar', 'reading']);
});

// -----------------------------------------------------------------
// 4. Heatmap & UI Data Formatting Tests
// -----------------------------------------------------------------
console.log('\n[4/4] Testing Heatmap grid, readiness and forecast formatting...');

it('Generates 30-day heatmap with 7-column calendar layout and streak badge', () => {
  clearDaylog();
  logActivity({ pillar: 'vocab', count: 12, type: 'review' });
  logActivity({ pillar: 'kanji', count: 5, isNew: true });

  const heatmap = getHeatmap30();
  assert.strictEqual(heatmap.length, 30, 'Heatmap must contain exactly 30 chronological days');
  assert.ok(heatmap[29].count >= 17, 'Today must reflect logged activity');
  assert.ok(heatmap[29].level >= 2, 'Level should match count threshold');

  const streak = getCurrentStreak();
  assert.strictEqual(streak, 1, 'Current streak should be 1');

  // Test HTML layout generator
  const html = renderHeatmapGridHtml(heatmap);
  assert.ok(html.includes('heatmap-weekdays'), 'Must render weekday headers');
  assert.ok(html.includes('heatmap-col-head'), 'Must contain 7 column headers');
  assert.ok(html.includes('is-today'), 'Must mark today with is-today class');
  assert.ok(html.includes('level-'), 'Must assign intensity level classes');
});

it('Computes readiness percentages and renders 14-day projection bars', () => {
  const mockDb = {
    stats: {
      'V:w1': { reps: 5, interval: 25, correct: 4, weight: 0.7 },
      'K:木': { reps: 4, interval: 22, correct: 3, weight: 0.6 }
    },
    vocabDB: {
      p1: [{ id: 'w1' }, { id: 'w2' }]
    },
    kanjiDB: {
      '木': { kanji: '木' },
      '林': { kanji: '林' }
    },
    grammarDB: { index: [{ id: 'g1' }] },
    readingDB: { r1: { id: 'r1' } }
  };

  const readiness = getReadinessStats(mockDb);
  assert.strictEqual(readiness.vocab.mastered, 1);
  assert.strictEqual(readiness.vocab.total, 2);
  assert.strictEqual(readiness.vocab.pct, 50);

  assert.strictEqual(readiness.kanji.mastered, 1);
  assert.strictEqual(readiness.kanji.pct, 50);

  // 14-day load forecaster
  const f14 = forecast({ profile: 'standard' }, mockDb.stats, 14);
  assert.strictEqual(f14.length, 14, 'Forecast must return 14 days');

  const forecastHtml = renderForecastBarsHtml(f14);
  assert.ok(forecastHtml.includes('forecast-bar-col'), 'Must contain bar column elements');
  assert.ok(forecastHtml.includes('forecast-bar-fill'), 'Must contain bar fills');
  assert.ok(forecastHtml.includes('d14'), 'Must label day 14');
});

it('Renders Today Dashboard inside container with all spec components', async () => {
  const { renderToday, setDueBatch } = await import('../js/today.js');
  const mockContainer = { innerHTML: '' };

  globalThis.document = {
    getElementById: (id) => {
      if (id === 'view-today') return mockContainer;
      return null;
    },
    createElement: () => ({ id: '', rel: '', href: '' }),
    head: { appendChild: () => {} }
  };

  renderToday();

  assert.ok(mockContainer.innerHTML.includes('today-exam-kicker'), 'Must render countdown kicker');
  assert.ok(mockContainer.innerHTML.includes('today-hero-card'), 'Must render hero card');
  assert.ok(mockContainer.innerHTML.includes('today-due-pills'), 'Must render due pills');
  assert.ok(mockContainer.innerHTML.includes('today-batch-selector'), 'Must render batch selector');
  assert.ok(mockContainer.innerHTML.includes('today-plan-card'), 'Must render plan card');
  assert.ok(mockContainer.innerHTML.includes('today-heatmap-card'), 'Must render heatmap card');
  assert.ok(mockContainer.innerHTML.includes('today-readiness-card'), 'Must render readiness card');
  assert.ok(mockContainer.innerHTML.includes('today-forecast-card'), 'Must render forecast card');

  // Test setDueBatch
  setDueBatch('40');
  assert.ok(mockContainer.innerHTML.includes('batch-chip active'), 'Batch chip 40 should be active');
});

console.log('\n========================================================');
console.log(`Summary: ${passedTests} / ${totalTests} tests passed cleanly.`);
console.log('========================================================');

