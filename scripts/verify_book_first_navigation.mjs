/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_book_first_navigation.mjs
   Verification Test Harness for Book-First Navigation & Sub-Tabs
   ======================================================= */

import assert from 'assert';

// 1. Setup minimal DOM mock for headless Node.js
if (typeof globalThis.window === 'undefined') {
  globalThis.window = globalThis;
}
if (typeof globalThis.document === 'undefined') {
  const makeEl = () => ({
    style: {},
    classList: {
      add: () => {},
      remove: () => {},
      toggle: () => {}
    },
    appendChild: () => {},
    setAttribute: () => {},
    getAttribute: () => '',
    addEventListener: () => {},
    querySelectorAll: () => []
  });

  globalThis.document = {
    createElement: makeEl,
    querySelectorAll: () => [],
    getElementById: (id) => makeEl()
  };
}

// 2. Dynamic imports after DOM mock setup
const { VIEW_TO_TAB } = await import('../js/navigation.js');
const {
  activeSubTabs,
  activeBatches,
  setVocabSubTab,
  setKanjiSubTab,
  setGrammarSubTab,
  setReadingSubTab,
  openSettingsDrawer,
  closeSettingsDrawer,
  N3BookPlatform
} = await import('../js/book-platform.js');
const { getPillarFromKey } = await import('../js/srs.js');

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
console.log('Running Book-First Navigation & Pillar Hubs Verification');
console.log('========================================================\n');

// -----------------------------------------------------------------
// 1. VIEW_TO_TAB Mappings
// -----------------------------------------------------------------
console.log('[1/4] Testing VIEW_TO_TAB mappings...');

it('Maps all 5 primary book-first dock tabs directly', () => {
  assert.strictEqual(VIEW_TO_TAB['today'], 'today');
  assert.strictEqual(VIEW_TO_TAB['vocab'], 'vocab');
  assert.strictEqual(VIEW_TO_TAB['kanji'], 'kanji');
  assert.strictEqual(VIEW_TO_TAB['grammar'], 'grammar');
  assert.strictEqual(VIEW_TO_TAB['reading'], 'reading');
});

it('Maps legacy routes backwards-compatibly', () => {
  assert.strictEqual(VIEW_TO_TAB['home'], 'today');
  assert.strictEqual(VIEW_TO_TAB['read'], 'reading');
  assert.strictEqual(VIEW_TO_TAB['learn'], 'kanji');
  assert.strictEqual(VIEW_TO_TAB['me'], 'today');
  assert.strictEqual(VIEW_TO_TAB['hard-words'], 'today');
});

// -----------------------------------------------------------------
// 2. Pillar Sub-Tabs State Machine
// -----------------------------------------------------------------
console.log('\n[2/4] Testing pillar sub-tabs state switching...');

it('Switches Vocab sub-tabs cleanly', () => {
  setVocabSubTab('srs');
  assert.strictEqual(activeSubTabs.vocab, 'srs');

  setVocabSubTab('hard');
  assert.strictEqual(activeSubTabs.vocab, 'hard');

  setVocabSubTab('tests');
  assert.strictEqual(activeSubTabs.vocab, 'tests');

  setVocabSubTab('units');
  assert.strictEqual(activeSubTabs.vocab, 'units');
});

it('Switches Kanji sub-tabs cleanly', () => {
  setKanjiSubTab('srs');
  assert.strictEqual(activeSubTabs.kanji, 'srs');

  setKanjiSubTab('hard');
  assert.strictEqual(activeSubTabs.kanji, 'hard');

  setKanjiSubTab('exercises');
  assert.strictEqual(activeSubTabs.kanji, 'exercises');

  setKanjiSubTab('target');
  assert.strictEqual(activeSubTabs.kanji, 'target');
});

it('Switches Grammar sub-tabs cleanly', () => {
  setGrammarSubTab('srs');
  assert.strictEqual(activeSubTabs.grammar, 'srs');

  setGrammarSubTab('hard');
  assert.strictEqual(activeSubTabs.grammar, 'hard');

  setGrammarSubTab('drills');
  assert.strictEqual(activeSubTabs.grammar, 'drills');

  setGrammarSubTab('patterns');
  assert.strictEqual(activeSubTabs.grammar, 'patterns');
});

it('Switches Reading sub-tabs cleanly', () => {
  setReadingSubTab('srs');
  assert.strictEqual(activeSubTabs.reading, 'srs');

  setReadingSubTab('hard');
  assert.strictEqual(activeSubTabs.reading, 'hard');

  setReadingSubTab('tests');
  assert.strictEqual(activeSubTabs.reading, 'tests');

  setReadingSubTab('passages');
  assert.strictEqual(activeSubTabs.reading, 'passages');
});

// -----------------------------------------------------------------
// 3. Pillar Scoped Key Partitioning
// -----------------------------------------------------------------
console.log('\n[3/4] Testing pillar-scoped key partitioning for self-contained SRS...');

it('Identifies pillar prefix correctly for every card type', () => {
  assert.strictEqual(getPillarFromKey('V:v2-01-001'), 'vocab');
  assert.strictEqual(getPillarFromKey('VC:v2-01-001:1'), 'vocab');

  assert.strictEqual(getPillarFromKey('K:合'), 'kanji');
  assert.strictEqual(getPillarFromKey('KWR:場合'), 'kanji');
  assert.strictEqual(getPillarFromKey('KWW:場合'), 'kanji');
  assert.strictEqual(getPillarFromKey('KWM:場合'), 'kanji');
  assert.strictEqual(getPillarFromKey('K_EX:l1_q1'), 'kanji');

  assert.strictEqual(getPillarFromKey('G:g_01'), 'grammar');
  assert.strictEqual(getPillarFromKey('GD:p1:1:q1'), 'grammar');
  assert.strictEqual(getPillarFromKey('GS:p1:1:q2'), 'grammar');
  assert.strictEqual(getPillarFromKey('GT:p3:1:q3'), 'grammar');

  assert.strictEqual(getPillarFromKey('RP:part1_les1'), 'reading');
  assert.strictEqual(getPillarFromKey('R_Q:part1_les1_q1'), 'reading');
});

// -----------------------------------------------------------------
// 4. Batch Sizes & Settings Controls
// -----------------------------------------------------------------
console.log('\n[4/4] Testing batch adjustments and settings drawer...');

it('Updates batch size per pillar independently', () => {
  N3BookPlatform.setBatch('vocab', '40');
  assert.strictEqual(activeBatches.vocab, '40');

  N3BookPlatform.setBatch('kanji', '10');
  assert.strictEqual(activeBatches.kanji, '10');

  assert.strictEqual(activeBatches.vocab, '40', 'Vocab batch was not overwritten');
});

it('Exports all required globals and functions on window object', () => {
  assert.strictEqual(typeof N3BookPlatform.setVocabSubTab, 'function');
  assert.strictEqual(typeof N3BookPlatform.setKanjiSubTab, 'function');
  assert.strictEqual(typeof N3BookPlatform.setGrammarSubTab, 'function');
  assert.strictEqual(typeof N3BookPlatform.setReadingSubTab, 'function');
  assert.strictEqual(typeof N3BookPlatform.openSettings, 'function');
  assert.strictEqual(typeof N3BookPlatform.closeSettings, 'function');
});

console.log('\n========================================================');
console.log(`Results: ${passedTests}/${totalTests} tests passed`);
console.log('========================================================\n');
