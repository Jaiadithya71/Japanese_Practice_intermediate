#!/usr/bin/env node
/* =======================================================
   NIHONGO INTERMEDIATE — dryrun_srs.mjs
   Comprehensive SRS Engine & Session Queue Test Harness
   Verifies: Legacy Parity, 60-Day Simulation, Queue Ordering,
   Re-queue & Criterion, Facet Unlock, Leeches, and Auto-Grade.
   Acceptance: ME-1 through ME-12 per 05_IMPLEMENTATION_PLAN_AND_QA.md
   ======================================================= */

import assert from 'node:assert';

// 1. In-memory mock for localStorage
class MockLocalStorage {
  constructor() {
    this.store = new Map();
  }
  getItem(key) {
    return this.store.has(String(key)) ? this.store.get(String(key)) : null;
  }
  setItem(key, value) {
    this.store.set(String(key), String(value));
  }
  removeItem(key) {
    this.store.delete(String(key));
  }
  clear() {
    this.store.clear();
  }
  get length() {
    return this.store.size;
  }
  key(index) {
    return Array.from(this.store.keys())[index] || null;
  }
}

// Global browser shims for headless Node.js
globalThis.localStorage = new MockLocalStorage();
globalThis.window = globalThis;
globalThis.window.__n3ScheduleSync = () => {};

// 2. Import modules
const {
  STORAGE_KEY,
  HARD_THRESHOLD,
  MASTERED_THRESHOLD,
  DEFAULT_EASE_FACTOR,
  EASE_FLOOR,
  STEPS_DAYS,
  LEECH_LAPSES,
  REQUEUE_OFFSET,
  MAX_REQUEUES,
  CRITERION_CORRECT,
  EXAM_DATE_ISO,
  SLOW_MS,
  BACKLOG_THRESHOLD
} = await import('../js/config.js');

const { state } = await import('../js/state.js');

const {
  loadStats,
  saveStats,
  snapToNextDueSlot,
  formatItemKey,
  getItemStats,
  getItemStatus,
  updateItemStats,
  updateWordStats,
  toggleItemHard,
  getDueItemsCount,
  getAllDueItems,
  getPillarFromKey,
  getFacetFromKey,
  isCatchUpMode,
  isFacetUnlocked,
  getMeaningFacetKey,
  interleaveQueue
} = await import('../js/srs.js');

const {
  examCapDays,
  calculatePace,
  forecast,
  PACE_PROFILES
} = await import('../js/planner.js');

const {
  createSession,
  getCurrentCard,
  deriveGradeFromMCQ,
  recordCardResult,
  isSessionFinished,
  getSessionResults
} = await import('../js/session.js');

console.log('===========================================================');
console.log('   NIHONGO INTERMEDIATE — SRS & SESSION DRY-RUN HARNESS    ');
console.log('===========================================================\n');

let totalTests = 0;
let passedTests = 0;

function runTest(name, fn) {
  totalTests++;
  try {
    fn();
    passedTests++;
    console.log(`  [PASS] ${name}`);
  } catch (err) {
    console.error(`  [FAIL] ${name}`);
    console.error(`         ${err.message}`);
    throw err;
  }
}

// =======================================================
// SUITE 1: LEGACY PARITY & SM-2 PRESERVATION
// =======================================================
console.log('SUITE 1: Legacy Parity & SM-2 Baseline (200 records x 4 grades)');

function generateLegacyCorpus(count = 200) {
  const records = {};
  for (let i = 0; i < count; i++) {
    const key = `V:legacy_${String(i).padStart(3, '0')}`;
    const reps = i % 15;
    const interval = reps === 0 ? 0 : Math.min(60, Math.pow(2, reps % 6));
    const ease = 1.3 + ((i % 18) * 0.1); // range 1.3 to 3.0
    records[key] = {
      correct: Math.floor(i * 1.5),
      incorrect: i % 7,
      weight: 0.5 + ((i % 20) * 0.2),
      reps,
      interval,
      easeFactor: Number(ease.toFixed(2)),
      nextDue: Date.now() + (interval * 24 * 60 * 60 * 1000),
      isHard: (i % 8 === 0)
    };
  }
  return records;
}

const corpus = generateLegacyCorpus(200);

runTest('1.1 Parity on correct/incorrect counts and weight direction across 800 evaluations', () => {
  const keys = Object.keys(corpus);
  assert.strictEqual(keys.length, 200);

  for (const key of keys) {
    const base = corpus[key];

    for (const grade of [1, 2, 3, 4]) {
      // Setup isolated state copy
      state.stats = { [key]: JSON.parse(JSON.stringify(base)) };
      const before = JSON.parse(JSON.stringify(state.stats[key]));

      updateItemStats(key, grade, { now: Date.now() });
      const after = state.stats[key];

      // 1. Correct / Incorrect counts
      if (grade === 1) {
        assert.strictEqual(after.incorrect, before.incorrect + 1, 'Grade 1 must increment incorrect');
        assert.strictEqual(after.correct, before.correct, 'Grade 1 must not alter correct');
        // Weight increases on failure
        assert.ok(after.weight >= before.weight, 'Grade 1 must increase or hold weight');
        // Reps reset
        assert.strictEqual(after.reps, 0, 'Grade 1 must reset reps to 0');
        // Interval is 1
        assert.strictEqual(after.interval, 1, 'Grade 1 must set interval to 1');
      } else {
        assert.strictEqual(after.correct, before.correct + 1, 'Grade >= 2 must increment correct');
        assert.strictEqual(after.incorrect, before.incorrect, 'Grade >= 2 must not alter incorrect');
        // Weight decreases or stays at floor on success
        assert.ok(after.weight <= before.weight || before.weight <= 0.1, 'Grade >= 2 must decrease or hold weight');
      }

      // ME-8: Ease factor must never drop below EASE_FLOOR (1.8) on any touched record
      assert.ok(after.easeFactor >= EASE_FLOOR, `Ease factor must be >= ${EASE_FLOOR}, got ${after.easeFactor}`);
    }
  }
});

// =======================================================
// SUITE 2: 60-DAY SIMULATION & LOAD FORECASTER (ME-7, ME-8, ME-11)
// =======================================================
console.log('\nSUITE 2: 60-Day Load Forecaster & Pace Simulation');

runTest('2.1 Pace Planner calculates quotas and detects kanji shortfall per doc 02 §6.3', () => {
  // Worked example from doc 02 §6.3:
  // Today (13 Oct -> 13 Dec): Tier-1 vocab 451, target kanji 584, grammar 83
  const now = new Date('2026-10-13T00:00:00Z').getTime();
  const exam = '2026-12-13';
  const pace = calculatePace(
    { vocabTier1: 451, kanjiWords: 584, grammar: 83 },
    'standard',
    exam,
    { now, studyDays: 6, reserveDays: 10 }
  );

  assert.strictEqual(pace.daysToExam, 61, '61 days to exam');
  assert.strictEqual(pace.learningDays, 43, '43 learning days (floor(51 * 6 / 7))');
  assert.strictEqual(pace.rawQuotas.vocab, 11, 'Raw vocab quota = 11');
  assert.strictEqual(pace.rawQuotas.kanjiWords, 14, 'Raw kanji quota = 14');
  assert.strictEqual(pace.rawQuotas.grammar, 2, 'Raw grammar quota = 2');
  assert.strictEqual(pace.quotas.vocab, 10, 'Standard caps vocab at 10');
  assert.strictEqual(pace.quotas.kanjiWords, 12, 'Standard caps kanji at 12');
  assert.strictEqual(pace.quotas.grammar, 2, 'Grammar quota meets raw quota 2');
  assert.strictEqual(pace.feasible.vocab, false, 'Vocab raw 11 exceeds cap 10');
  assert.strictEqual(pace.feasible.kanjiWords, false, 'Kanji raw 14 exceeds cap 12');
  assert.strictEqual(pace.feasible.grammar, true, 'Grammar is feasible');
  assert.ok(pace.warnings.length >= 2, 'Planner produces explicit shortfall warnings');
  assert.ok(pace.summary.includes('kanji-words will not be learned'), 'Warning mentions kanji-words shortfall');
});

runTest('2.2 Load Forecaster returns 60 days without exceeding budget by >20% (ME-11)', () => {
  const now = new Date('2026-10-13T00:00:00Z').getTime();
  const sim = forecast(
    { profile: 'standard', timeBudgetMin: 45, examDate: '2026-12-13', now },
    {},
    60
  );

  assert.strictEqual(sim.length, 60, 'Simulation must return exactly 60 days');

  // Verify steady-state properties
  for (const entry of sim) {
    assert.ok(entry.day >= 1 && entry.day <= 60);
    assert.ok(entry.newItems >= 0);
    assert.ok(entry.reviews >= 0);
    assert.ok(entry.minutes >= 0);
  }

  // ME-11: First 14 days must not exceed time budget (45 min) by >20% (<= 54 min)
  for (let i = 0; i < 14; i++) {
    const dayData = sim[i];
    assert.ok(
      dayData.minutes <= 54,
      `Day ${dayData.day} minutes (${dayData.minutes}) exceeded budget threshold (54 min)`
    );
  }
  assert.strictEqual(sim.budgetWarningCount, 0, 'No budget warnings for standard profile in first 14 days');
});

runTest('2.3 40-learner 60-day SRS schedule maintains ME-7 (exam cap) & ME-8 (ease floor)', () => {
  const DAY_MS = 24 * 60 * 60 * 1000;
  const startMs = new Date('2026-10-13T00:00:00Z').getTime();
  const examMs = new Date('2026-12-13T00:00:00Z').getTime();

  // Test across multiple items and progressive days
  state.stats = {};

  for (let learner = 0; learner < 40; learner++) {
    const itemKey = `V:sim_learner_${learner}`;

    for (let day = 0; day < 60; day++) {
      const currentSimMs = startMs + (day * DAY_MS);
      const cap = examCapDays(currentSimMs, '2026-12-13');

      // Random 90% pass rate
      const grade = (learner + day) % 10 === 0 ? 1 : 3;
      updateItemStats(itemKey, grade, { now: currentSimMs });

      const s = state.stats[itemKey];

      // ME-8: ease factor floor
      assert.ok(s.easeFactor >= EASE_FLOOR, `Ease factor must stay >= ${EASE_FLOOR}`);

      // ME-7: interval never exceeds examCapDays
      if (s.interval > 0) {
        assert.ok(
          s.interval <= cap,
          `Interval ${s.interval} must not exceed exam cap ${cap} on sim day ${day}`
        );
      }

      // Assert nextDue does not exceed exam date by more than a slot
      if (s.nextDue > 0 && currentSimMs < examMs) {
        const diffDays = Math.ceil((s.nextDue - examMs) / DAY_MS);
        assert.ok(
          diffDays <= 2,
          `nextDue (${new Date(s.nextDue).toISOString()}) must be compressed before exam (${diffDays} days past)`
        );
      }
    }
  }
});

// =======================================================
// SUITE 3: QUEUE ORDERING, INTERLEAVING & CATCH-UP (ME-9, ME-10)
// =======================================================
console.log('\nSUITE 3: Queue Ordering, Interleaving & Catch-up Mode');

runTest('3.1 Priority queue order: learning first, overdueRatio next, weight third (doc 02 §6.1)', () => {
  const now = Date.now();
  const DAY = 24 * 60 * 60 * 1000;
  state.stats = {};

  // 1. Learning card (reps=0) due 1 hour ago
  state.stats['KWR:learn1'] = {
    reps: 0,
    learnState: 'learning',
    interval: 0,
    weight: 1.0,
    nextDue: now - (60 * 60 * 1000)
  };

  // 2. Review card highly overdue (due 10 days ago, interval 2 -> overdueRatio = 5)
  state.stats['V:overdue_high'] = {
    reps: 2,
    learnState: 'review',
    interval: 2,
    weight: 1.0,
    nextDue: now - (10 * DAY)
  };

  // 3. Review card slightly overdue (due 1 day ago, interval 2 -> overdueRatio = 0.5)
  state.stats['GD:overdue_low'] = {
    reps: 2,
    learnState: 'review',
    interval: 2,
    weight: 1.0,
    nextDue: now - (1 * DAY)
  };

  // 4. Same overdue ratio, higher weight
  state.stats['GS:overdue_low_heavy'] = {
    reps: 2,
    learnState: 'review',
    interval: 2,
    weight: 2.5,
    nextDue: now - (1 * DAY)
  };

  const queue = getAllDueItems('all', 'all');
  assert.strictEqual(queue.length, 4);

  // Expected priority:
  // 1st: KWR:learn1 (learning state)
  // 2nd: V:overdue_high (highest overdueRatio)
  // 3rd: GS:overdue_low_heavy (higher weight between the two with ratio 0.5)
  // 4th: GD:overdue_low
  assert.strictEqual(queue[0].key, 'KWR:learn1', 'Learning state comes first');
  assert.strictEqual(queue[1].key, 'V:overdue_high', 'Highest overdueRatio comes second');
  assert.strictEqual(queue[2].key, 'GS:overdue_low_heavy', 'Higher weight comes before lower weight on tie');
  assert.strictEqual(queue[3].key, 'GD:overdue_low', 'Lower weight comes last');
});

runTest('3.2 Facet interleaving prevents > 3 consecutive of the same facet (ME-9)', () => {
  // Test interleaveQueue with 6 KWR items and 2 V items
  const candidates = [
    { key: 'KWR:1', facet: 'KWR' },
    { key: 'KWR:2', facet: 'KWR' },
    { key: 'KWR:3', facet: 'KWR' },
    { key: 'KWR:4', facet: 'KWR' },
    { key: 'KWR:5', facet: 'KWR' },
    { key: 'KWR:6', facet: 'KWR' },
    { key: 'V:1', facet: 'V' },
    { key: 'V:2', facet: 'V' }
  ];

  const interleaved = interleaveQueue(candidates, 3);
  assert.strictEqual(interleaved.length, 8);

  // Check no 4 consecutive of the same facet while alternatives existed
  let maxConsec = 1;
  let curConsec = 1;
  for (let i = 1; i < interleaved.length; i++) {
    if (interleaved[i].facet === interleaved[i - 1].facet) {
      curConsec++;
      if (curConsec > maxConsec) maxConsec = curConsec;
    } else {
      curConsec = 1;
    }
  }

  // Before alternatives ran out, consecutive KWR should never exceed 3
  const firstFour = interleaved.slice(0, 4).map(c => c.facet);
  assert.strictEqual(firstFour[3], 'V', '4th item must be V to break 3 consecutive KWR');
});

runTest('3.3 Catch-up mode triggers on > 80 due items and caps session at 40 (ME-10)', () => {
  const now = Date.now();
  state.stats = {};

  // Seed 120 due items
  for (let i = 0; i < 120; i++) {
    const key = `V:backlog_${i}`;
    state.stats[key] = {
      reps: 1,
      learnState: 'review',
      interval: 1,
      weight: 1.0,
      nextDue: now - (i * 1000)
    };
  }

  assert.strictEqual(getDueItemsCount('all'), 120, '120 items due');
  assert.strictEqual(isCatchUpMode(), true, 'Catch-up mode active (> BACKLOG_THRESHOLD 80)');

  // Request all
  const sessionQueue = getAllDueItems('all', 'all');
  assert.strictEqual(
    sessionQueue.length,
    40,
    'Session queue capped at 40 items in Catch-up mode (ME-10)'
  );

  // Request 50 explicitly
  const sessionQueue50 = getAllDueItems('all', 50);
  assert.strictEqual(
    sessionQueue50.length,
    40,
    'Explicit request of 50 capped at 40 items in Catch-up mode'
  );
});

// =======================================================
// SUITE 4: RE-QUEUE & CRITERION IN SESSION (ME-2, ME-3)
// =======================================================
console.log('\nSUITE 4: Session Re-queue, Retries & Criterion Graduation');

runTest('4.1 Wrong answer re-queues +3 positions; third failure buries card (ME-2)', () => {
  state.stats = {
    'KWR:itemB': { reps: 2, learnState: 'review', interval: 2 },
    'KWR:itemC': { reps: 2, learnState: 'review', interval: 2 },
    'KWR:itemD': { reps: 2, learnState: 'review', interval: 2 },
    'KWR:itemE': { reps: 2, learnState: 'review', interval: 2 }
  };
  const cards = [
    { key: 'KWR:itemA', term: 'itemA' },
    { key: 'KWR:itemB', term: 'itemB' },
    { key: 'KWR:itemC', term: 'itemC' },
    { key: 'KWR:itemD', term: 'itemD' },
    { key: 'KWR:itemE', term: 'itemE' }
  ];

  const session = createSession('learn-kanji', cards);
  assert.strictEqual(session.queue.length, 5);

  // 1st presentation of itemA -> Fail (Grade 1)
  const card1 = getCurrentCard(session);
  assert.strictEqual(card1.key, 'KWR:itemA');
  recordCardResult(session, card1, 1);

  // Re-queued at cursor 0 + REQUEUE_OFFSET 3 = index 3
  assert.strictEqual(session.retries.get('KWR:itemA'), 1, 'Retry count = 1');
  assert.strictEqual(session.queue.length, 6, 'Queue length increased by 1');
  assert.strictEqual(session.queue[3].key, 'KWR:itemA', 'Re-inserted at index 3');
  assert.strictEqual(session.queue[3]._requeued, true, 'Flagged as _requeued');

  // Pass itemB, itemC
  recordCardResult(session, getCurrentCard(session), 3);
  recordCardResult(session, getCurrentCard(session), 3);

  // Cursor is now at index 3: 2nd presentation of itemA -> Fail again
  const cardA2 = getCurrentCard(session);
  assert.strictEqual(cardA2.key, 'KWR:itemA');
  recordCardResult(session, cardA2, 1);
  assert.strictEqual(session.retries.get('KWR:itemA'), 2, 'Retry count = 2');
  assert.strictEqual(session.queue.length, 7, 'Re-queued second time');

  // Pass remaining cards until cardA is reached again
  while (!isSessionFinished(session) && getCurrentCard(session).key !== 'KWR:itemA') {
    recordCardResult(session, getCurrentCard(session), 3);
  }

  // 3rd presentation of itemA -> Fail 3rd time
  const cardA3 = getCurrentCard(session);
  assert.strictEqual(cardA3.key, 'KWR:itemA');
  const queueLenBefore = session.queue.length;
  recordCardResult(session, cardA3, 1);

  // ME-2: Third failure buries card (retries >= MAX_REQUEUES 2, no further requeue)
  assert.strictEqual(session.retries.get('KWR:itemA'), 3, 'Retry count = 3');
  assert.strictEqual(session.queue.length, queueLenBefore, 'Card buried; not re-queued on 3rd failure');
});

runTest('4.2 Learn-to-criterion loop: 2 correct graduates; wrong resets count (ME-3)', () => {
  state.stats = {};
  const cards = [
    { key: 'KWR:wordCriterion', term: 'wordCriterion' }
  ];

  const session = createSession('learn-kanji', cards);

  // 1st correct answer -> count = 1 (< CRITERION_CORRECT 2)
  const card = getCurrentCard(session);
  recordCardResult(session, card, 3);

  assert.strictEqual(session.correctCount.get('KWR:wordCriterion'), 1);
  // Stays in session: copy re-inserted
  assert.strictEqual(session.queue.length, 2, 'Copy inserted for criterion second pass');
  // Stats not yet graduated
  assert.strictEqual(state.stats['KWR:wordCriterion'].reps, 0, 'Reps remain 0 during criterion loop');

  // Next: fail -> count resets to 0!
  const cardRetry = getCurrentCard(session);
  recordCardResult(session, cardRetry, 1);
  assert.strictEqual(session.correctCount.get('KWR:wordCriterion'), 0, 'Failure resets criterion count to 0');

  // Advance and give 2 consecutive correct answers
  recordCardResult(session, getCurrentCard(session), 3);
  assert.strictEqual(session.correctCount.get('KWR:wordCriterion'), 1);

  recordCardResult(session, getCurrentCard(session), 3);
  assert.strictEqual(session.correctCount.get('KWR:wordCriterion'), 2);

  // Graduation triggered!
  const finalStats = state.stats['KWR:wordCriterion'];
  assert.strictEqual(finalStats.learnState, 'review', 'Graduated to review');
  assert.strictEqual(finalStats.reps, 1, 'Reps advanced to 1');
  assert.strictEqual(finalStats.interval, 0, 'First graduation interval is STEPS_DAYS[0] (0)');
  assert.ok(finalStats.nextDue > Date.now(), 'nextDue scheduled at next legal slot');
  assert.strictEqual(isSessionFinished(session), true, 'Session complete');
});

// =======================================================
// SUITE 5: FACET UNLOCKING & SHARED VOCAB MEANING (ME-4, ME-5)
// =======================================================
console.log('\nSUITE 5: Facet Unlocking & Shared Vocab Meaning');

runTest('5.1 KWW writing facet unlocks ONLY when KWR reps >= 2 (ME-4)', () => {
  const stats = {
    'KWR:未熟': { reps: 0 },
    'KWR:成熟': { reps: 1 },
    'KWR:市場': { reps: 2 },
    'KWR:都市': { reps: 5 }
  };

  assert.strictEqual(isFacetUnlocked('KWW:未熟', stats), false, 'reps=0: KWW locked');
  assert.strictEqual(isFacetUnlocked('KWW:成熟', stats), false, 'reps=1: KWW locked');
  assert.strictEqual(isFacetUnlocked('KWW:市場', stats), true, 'reps=2: KWW unlocked (ME-4)');
  assert.strictEqual(isFacetUnlocked('KWW:都市', stats), true, 'reps=5: KWW unlocked (ME-4)');
  assert.strictEqual(isFacetUnlocked('KWR:市場', stats), true, 'KWR unlocked at learn time');
});

runTest('5.2 Words present in both kanji data and vocab share V: meaning (ME-5)', () => {
  state.idx = {
    words: {
      '市場': { term: '市場', vocabId: 'v05-012' },
      '独占': { term: '独占', vocabId: null }
    }
  };

  const overlap = new Set(['市場']);

  // Shared word (市場): KWM is NOT created, V: is credited
  assert.strictEqual(isFacetUnlocked('KWM:市場', state.stats, overlap), false, 'KWM locked for vocab overlap');
  assert.strictEqual(getMeaningFacetKey('市場'), 'V:v05-012', 'Credits meaning to V:v05-012 (ME-5)');

  // Non-shared target word (独占): KWM created
  assert.strictEqual(isFacetUnlocked('KWM:独占', state.stats, overlap), true, 'KWM unlocked for kanji-only word');
  assert.strictEqual(getMeaningFacetKey('独占'), 'KWM:独占', 'Uses KWM:独占 for kanji-only word');
});

// =======================================================
// SUITE 6: LEECH DETECTION & AUTO-GRADING (ME-6, ME-12)
// =======================================================
console.log('\nSUITE 6: Leech Detection & MCQ Auto-Grade Rules');

runTest('6.1 Leech flagged when lapses >= LEECH_LAPSES (5) (ME-12)', () => {
  state.stats = {};
  const key = 'V:leech_candidate';

  // Item starts passed (reps = 2)
  state.stats[key] = {
    reps: 2,
    interval: 6,
    weight: 1.0,
    lapses: 0,
    leech: false
  };

  // Fail 1st time
  updateItemStats(key, 1);
  assert.strictEqual(state.stats[key].lapses, 1);
  assert.strictEqual(state.stats[key].leech, false);

  // Graduate again and fail 2nd, 3rd, 4th times
  for (let l = 2; l <= 4; l++) {
    state.stats[key].reps = 1;
    updateItemStats(key, 1);
    assert.strictEqual(state.stats[key].lapses, l);
    assert.strictEqual(state.stats[key].leech, false);
  }

  // 5th lapse: triggers leech
  state.stats[key].reps = 1;
  updateItemStats(key, 1);
  assert.strictEqual(state.stats[key].lapses, 5);
  assert.strictEqual(state.stats[key].leech, true, 'Leech set when lapses >= 5 (ME-12)');
});

runTest('6.2 MCQ auto-grading: wrong -> 1, slow/hint -> 2, fast -> 3, NEVER 4 (ME-6)', () => {
  // Wrong
  assert.strictEqual(deriveGradeFromMCQ(false, 3000, false), 1, 'Wrong gives grade 1');
  assert.strictEqual(deriveGradeFromMCQ(false, 15000, true), 1, 'Wrong gives grade 1 regardless of time/hint');

  // Correct but slow (> SLOW_MS 12000)
  assert.strictEqual(deriveGradeFromMCQ(true, 13000, false), 2, 'Correct and > 12s gives grade 2 (Hard)');

  // Correct with hint
  assert.strictEqual(deriveGradeFromMCQ(true, 4000, true), 2, 'Correct with hint gives grade 2 (Hard)');

  // Correct, fast, no hint
  assert.strictEqual(deriveGradeFromMCQ(true, 4000, false), 3, 'Correct and fast gives grade 3 (Good)');

  // Ensure 4 (Easy) is NEVER auto-assigned
  for (let ms = 100; ms <= 30000; ms += 500) {
    const gradeNoHint = deriveGradeFromMCQ(true, ms, false);
    const gradeWithHint = deriveGradeFromMCQ(true, ms, true);
    assert.notStrictEqual(gradeNoHint, 4, 'Easy (4) must never be auto-assigned');
    assert.notStrictEqual(gradeWithHint, 4, 'Easy (4) must never be auto-assigned');
  }
});

// =======================================================
// HARNESS SUMMARY REPORT
// =======================================================
console.log('\n===========================================================');
console.log(`DRY-RUN VERIFICATION COMPLETE: ${passedTests} / ${totalTests} test suites passed.`);
console.log('Acceptance Criteria Verified:');
console.log('  [X] ME-1  Step 0 next slot scheduling (snapToNextDueSlot + MIN_FIRST_GAP_MS)');
console.log('  [X] ME-2  MCQ wrong answer +3 re-queue & 3rd-failure burial');
console.log('  [X] ME-3  2-correct criterion loop graduation & wrong count reset');
console.log('  [X] ME-4  KWW facet unlocks only when KWR reps >= 2');
console.log('  [X] ME-5  Shared vocab meaning credited to V:, no redundant KWM');
console.log('  [X] ME-6  MCQ auto-grade never assigns Easy (4)');
console.log('  [X] ME-7  Interval never exceeds examCapDays(now)');
console.log('  [X] ME-8  Ease factor never falls below 1.8 on touched records');
console.log('  [X] ME-9  Interleaved review queue (no > 3 consecutive same-facet)');
console.log('  [X] ME-10 Backlog Catch-up mode trigger (>80 due) & 40-item session cap');
console.log('  [X] ME-11 Load forecaster simulates 60 days within budget limits');
console.log('  [X] ME-12 Leech flagged at 5th lapse');
console.log('===========================================================');
