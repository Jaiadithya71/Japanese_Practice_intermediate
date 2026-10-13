/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_me_fixit.mjs
   Test Harness for Me Tab & Leech Fix-It Engine (WP-11 & WP-12)
   Tests:
   1. Weak points query & leech prioritization (leeches first).
   2. Leech Fix-It sheet note saving (s.note) and 1-day interval scheduling.
   3. Settings save and retrieval in nihongo_intermediate_settings_v1.
   4. Window global bindings & pillar filtering.
   ======================================================= */

import assert from 'node:assert';

// 1. In-memory Mock for localStorage
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

// 2. Setup Globals before importing app modules
const mockStorage = new MockLocalStorage();
globalThis.localStorage = mockStorage;
globalThis.window = globalThis;
globalThis.window.localStorage = mockStorage;
globalThis.window.__n3ScheduleSync = () => {};
globalThis.window.updateSidebarStats = () => {};

// 3. Import modules
const { state } = await import('../js/state.js');
const {
  loadSettings,
  saveSettings,
  getWeakPoints,
  isItemWeak,
  isItemLeech,
  resolveWeakItem,
  saveLeechMnemonic,
  scheduleLeechInOneDay,
  SETTINGS_STORAGE_KEY,
  DEFAULT_SETTINGS
} = await import('../js/me-tab.js');

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
console.log('Running Me Tab & Leech Fix-It Verification (WP-11 & WP-12)');
console.log('========================================================\n');

// -----------------------------------------------------------------
// Test Suite 1: Weak Points Query & Leech Prioritization
// -----------------------------------------------------------------
console.log('[1/4] Testing Weak Points query and Leech prioritization...');

it('Correctly identifies weak items and leeches', () => {
  assert.strictEqual(isItemWeak({ weight: 1.0, isHard: false, leech: false, lapses: 0 }), false);
  assert.strictEqual(isItemWeak({ weight: 1.8, isHard: false }), true);
  assert.strictEqual(isItemWeak({ weight: 1.0, isHard: true }), true);
  assert.strictEqual(isItemWeak({ weight: 1.0, isHard: false, leech: true }), true);
  assert.strictEqual(isItemWeak({ weight: 1.0, isHard: false, lapses: 5 }), true);

  assert.strictEqual(isItemLeech({ lapses: 4, leech: false }), false);
  assert.strictEqual(isItemLeech({ lapses: 5, leech: false }), true);
  assert.strictEqual(isItemLeech({ lapses: 2, leech: true }), true);
});

it('Prioritizes leeches first, ordered by lapse count and weight', () => {
  // Seed state.stats with controlled test records
  state.stats = {
    // Normal stable word -> should NOT be weak
    'V:word_stable': {
      reps: 4,
      interval: 14,
      weight: 0.7,
      isHard: false,
      leech: false,
      lapses: 0,
      incorrect: 0
    },
    // Non-leech weak word 1 (weight 2.0)
    'V:word_weak_1': {
      reps: 2,
      interval: 3,
      weight: 2.0,
      isHard: false,
      leech: false,
      lapses: 2,
      incorrect: 3
    },
    // Non-leech weak word 2 (weight 2.4)
    'KWR:案内': {
      reps: 1,
      interval: 1,
      weight: 2.4,
      isHard: false,
      leech: false,
      lapses: 1,
      incorrect: 2
    },
    // Leech 1: Moderate lapses (6 lapses)
    'K:持': {
      reps: 0,
      interval: 1,
      weight: 1.5,
      isHard: false,
      leech: true,
      lapses: 6,
      incorrect: 8
    },
    // Leech 2: Severe lapses (10 lapses)
    'GD:p1a:1:101': {
      reps: 0,
      interval: 1,
      weight: 3.0,
      isHard: true,
      leech: true,
      lapses: 10,
      incorrect: 12
    },
    // Reading weak question (marked hard)
    'R_Q:short1_q1': {
      reps: 1,
      interval: 1,
      weight: 1.9,
      isHard: true,
      leech: false,
      lapses: 1,
      incorrect: 2
    }
  };

  const weakList = getWeakPoints('all', state.stats);

  // Stable item must be excluded
  assert.strictEqual(weakList.some(item => item.key === 'V:word_stable'), false, 'Stable word must not be in weak points');
  assert.strictEqual(weakList.length, 5, 'Exactly 5 weak items should be returned');

  // Leeches MUST come first
  assert.strictEqual(weakList[0].key, 'GD:p1a:1:101', 'Severe leech with 10 lapses must be #1');
  assert.strictEqual(weakList[0].isLeech, true);
  assert.strictEqual(weakList[1].key, 'K:持', 'Leech with 6 lapses must be #2');
  assert.strictEqual(weakList[1].isLeech, true);

  // Non-leeches follow leeches, sorted by weight descending
  assert.strictEqual(weakList[2].key, 'KWR:案内', 'Highest weight non-leech (2.4) must be #3');
  assert.strictEqual(weakList[2].isLeech, false);
  assert.strictEqual(weakList[3].key, 'V:word_weak_1', 'Weight 2.0 non-leech must be #4');
  assert.strictEqual(weakList[4].key, 'R_Q:short1_q1', 'Weight 1.9 non-leech must be #5');
});

it('Filters weak items accurately by pillar', () => {
  const vocabWeak = getWeakPoints('vocab', state.stats);
  assert.strictEqual(vocabWeak.length, 1);
  assert.strictEqual(vocabWeak[0].key, 'V:word_weak_1');

  const kanjiWeak = getWeakPoints('kanji', state.stats);
  assert.strictEqual(kanjiWeak.length, 2);
  assert.deepStrictEqual(kanjiWeak.map(i => i.key), ['K:持', 'KWR:案内']);

  const grammarWeak = getWeakPoints('grammar', state.stats);
  assert.strictEqual(grammarWeak.length, 1);
  assert.strictEqual(grammarWeak[0].key, 'GD:p1a:1:101');

  const readingWeak = getWeakPoints('reading', state.stats);
  assert.strictEqual(readingWeak.length, 1);
  assert.strictEqual(readingWeak[0].key, 'R_Q:short1_q1');
});

// -----------------------------------------------------------------
// Test Suite 2: Leech Fix-It Sheet (Note saving & 1-day interval)
// -----------------------------------------------------------------
console.log('\n[2/4] Testing Leech Fix-It Sheet note saving and 1-day interval...');

it('Saves personal mnemonic/hook into s.note and persists to storage', () => {
  const targetKey = 'KWR:案内';
  const mnemonic = '案 (plan) + 内 (inside) -> Tour guide who plans from the inside';

  saveLeechMnemonic(targetKey, mnemonic);

  const s = state.stats[targetKey];
  assert.strictEqual(s.note, mnemonic, 's.note must contain the saved mnemonic');

  // Check persistence in localStorage
  const rawStats = JSON.parse(mockStorage.getItem('nihongo_intermediate_stats_v1') || '{}');
  assert.strictEqual(rawStats[targetKey]?.note, mnemonic, 's.note must be persisted to localStorage');
});

it('Schedules leech review in 1 day with interval = 1, reps = 0, and relearning state', () => {
  const targetKey = 'K:持';
  const beforeTime = Date.now();

  scheduleLeechInOneDay(targetKey);

  const s = state.stats[targetKey];
  assert.strictEqual(s.interval, 1, 'Interval must be reset to 1 day');
  assert.strictEqual(s.reps, 0, 'Reps must be reset to 0');
  assert.strictEqual(s.learnState, 'relearning', 'learnState must be relearning');
  assert.strictEqual(s.streak, 0, 'Streak must be reset to 0');

  const expectedDue = beforeTime + (24 * 60 * 60 * 1000);
  assert.ok(Math.abs(s.nextDue - expectedDue) < 2000, `nextDue (${s.nextDue}) must be ~24h from now (${expectedDue})`);

  // Verify persistence
  const rawStats = JSON.parse(mockStorage.getItem('nihongo_intermediate_stats_v1') || '{}');
  assert.strictEqual(rawStats[targetKey]?.interval, 1);
  assert.strictEqual(rawStats[targetKey]?.reps, 0);
});

// -----------------------------------------------------------------
// Test Suite 3: Settings Storage (nihongo_intermediate_settings_v1)
// -----------------------------------------------------------------
console.log('\n[3/4] Testing Settings save and retrieval in nihongo_intermediate_settings_v1...');

it('Loads defaults when no settings are saved in storage', () => {
  mockStorage.removeItem(SETTINGS_STORAGE_KEY);
  state.settings = null;

  const settings = loadSettings();
  assert.strictEqual(settings.examDate, '2026-12-13', 'Default examDate should be 2026-12-13');
  assert.strictEqual(settings.profile, 'standard', 'Default pace profile should be standard');
  assert.strictEqual(settings.studyDays, 6, 'Default studyDays should be 6');
  assert.strictEqual(state.settings.profile, 'standard');
});

it('Saves and retrieves exam date, pace profile, and study days in nihongo_intermediate_settings_v1', () => {
  const updated = saveSettings({
    examDate: '2026-12-20',
    profile: 'intensive',
    studyDays: 5
  });

  assert.strictEqual(updated.examDate, '2026-12-20');
  assert.strictEqual(updated.profile, 'intensive');
  assert.strictEqual(updated.studyDays, 5);

  // Assert raw localStorage payload
  const raw = mockStorage.getItem(SETTINGS_STORAGE_KEY);
  assert.ok(raw, 'localStorage must contain serialized settings');
  const parsed = JSON.parse(raw);
  assert.strictEqual(parsed.examDate, '2026-12-20');
  assert.strictEqual(parsed.profile, 'intensive');
  assert.strictEqual(parsed.studyDays, 5);

  // Assert subsequent loadSettings returns the persisted values
  state.settings = null;
  const reloaded = loadSettings();
  assert.strictEqual(reloaded.examDate, '2026-12-20');
  assert.strictEqual(reloaded.profile, 'intensive');
  assert.strictEqual(reloaded.studyDays, 5);
});

// -----------------------------------------------------------------
// Test Suite 4: Window Global Bindings & Exports
// -----------------------------------------------------------------
console.log('\n[4/4] Testing Window global bindings and exports...');

it('Exports all required functions and binds them to window', () => {
  const expectedBindings = [
    'renderMeTab',
    'switchMeTabSegment',
    'openLeechFixItSheet',
    'saveLeechMnemonic',
    'closeLeechFixItSheet',
    'drillAllWeak',
    'quick5Weak'
  ];

  for (const fnName of expectedBindings) {
    assert.strictEqual(
      typeof globalThis.window[fnName],
      'function',
      `window.${fnName} must be bound as a function`
    );
  }
});

console.log('\n========================================================');
console.log(`Verification Complete: ${passedTests}/${totalTests} tests passed`);
console.log('========================================================');

if (passedTests === totalTests) {
  process.exit(0);
} else {
  process.exit(1);
}
