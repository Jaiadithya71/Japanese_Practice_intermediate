#!/usr/bin/env node
/**
 * scripts/verify_reading_empty_session.mjs
 *
 * Regression tests for the empty-reading-session bug: a strategy-only lesson
 * (dokkai-n3-l03, no passage, no questions) could be run through timed
 * practice, score 0/0 as 100%, pass second-pass criteria and reach
 * "Mastered", persisting false RP:* progress.
 *
 * Verifies:
 * 1. Gradability: lessons need a passage AND questions to be gradable.
 * 2. Start practice skips strategy-only lessons (with a hint) and never opens
 *    them for timed practice; other entry points redirect to the book.
 * 3. Scoring safety net: submitting an empty session records nothing and shows
 *    an honest "nothing to grade" review instead of a pass (source assertion).
 * 4. Migration M5 removes false RP:* records for passage-less/question-less
 *    lessons and keeps genuine records.
 * 5. Regression: a real lesson still grades and schedules its re-read.
 */

import assert from 'node:assert/strict';
import fs from 'node:fs';
import { register } from 'node:module';
register('./strip-query-loader.mjs', import.meta.url);

// ---------- DOM / browser stubs ----------
const elements = new Map();
function makeEl(id = '') {
  return {
    id,
    innerHTML: '',
    textContent: '',
    className: '',
    title: '',
    disabled: false,
    style: {},
    classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
    setAttribute() {},
    scrollIntoView() {},
    appendChild() {},
    append() {},
    addEventListener() {},
    querySelector: () => null,
    querySelectorAll: () => []
  };
}
const memStore = new Map();
globalThis.localStorage = {
  getItem: (k) => (memStore.has(k) ? memStore.get(k) : null),
  setItem: (k, v) => memStore.set(k, String(v)),
  removeItem: (k) => memStore.delete(k),
  clear: () => memStore.clear()
};
globalThis.window = globalThis;
globalThis.scrollTo = () => {};
globalThis.showView = () => {};
if (typeof globalThis.navigator === 'undefined' || !('onLine' in globalThis.navigator)) {
  try { globalThis.navigator = { onLine: false }; } catch { /* node navigator is read-only */ }
}
globalThis.document = {
  getElementById: (id) => {
    if (!elements.has(id)) elements.set(id, makeEl(id));
    return elements.get(id);
  },
  createElement: () => makeEl(),
  querySelector: () => null,
  querySelectorAll: () => [],
  head: { appendChild() {} },
  body: { classList: { add() {}, remove() {} } }
};
globalThis.fetch = async (path) => {
  const raw = fs.readFileSync(path, 'utf8');
  return { ok: true, status: 200, json: async () => JSON.parse(raw), text: async () => raw };
};

// ---------- Imports (after stubs) ----------
const { state } = await import('../js/state.js');
const { loadStats } = await import('../js/srs.js');
const { loadIntermediateReadingDB } = await import('../js/data-loader.js');
const reader = await import('../js/reader.js');
const { countPassageChars } = await import('../js/reading-types.js');
const { STORAGE_KEY } = await import('../js/config.js');

state.currentView = 'reading';

// Seed stats: one provably false record (l03 has never had a passage or
// questions) and one genuine record on a real passage lesson.
memStore.set(STORAGE_KEY, JSON.stringify({
  'RP:dokkai-n3-l03': { reads: 3, step: 2, mastered: true, bestAcc: 1, lastAcc: 1, bestCpm: 0, lastCpm: 0, nextDue: Date.now() + 86400000, interval: 25, lastSeen: Date.now(), weight: 1 },
  'RP:dokkai-n3-l04': { reads: 0, step: 0, mastered: false, bestAcc: 0, lastAcc: 0, bestCpm: 0, lastCpm: 0, nextDue: Date.now() + 86400000, interval: 3, lastSeen: Date.now(), weight: 1 }
}));
loadStats();

const db = await loadIntermediateReadingDB();

// 1. Gradability
assert.equal(reader.isGradableReadingLesson(db['dokkai-n3-l03']), false, 'l03 (strategy page) must not be gradable');
assert.equal(reader.isGradableReadingLesson(db['dokkai-n3-l04']), true, 'l04 (passage + question) must be gradable');
assert.equal(reader.isGradableReadingLesson(db['dokkai-n3-part2-prep']), false, 'part2-prep (passage, no questions) must not be gradable');
assert.equal(countPassageChars(db['dokkai-n3-l03'].passage || db['dokkai-n3-l03']), 0);
console.log('1. Gradability checks passed.');

// 4. Migration M5
assert.equal(state.stats['RP:dokkai-n3-l03'], undefined, 'false l03 re-read record must be removed');
assert.ok(state.stats['RP:dokkai-n3-l04'], 'genuine l04 record must be kept');
const persisted = JSON.parse(memStore.get(STORAGE_KEY));
assert.equal(persisted['RP:dokkai-n3-l03'], undefined, 'cleanup must persist to storage');
assert.ok(persisted['RP:dokkai-n3-l04']);
console.log('4. Migration M5 removes false records, keeps genuine ones, persists.');

// 2a. Direct open of a strategy page redirects to the book (no timed flow)
const workspace = document.getElementById('dokkai-workspace-container');
reader.openReadingLesson('dokkai-n3-l03');
assert.ok(state.activeReadingLesson, 'lesson opens');
assert.match(workspace.innerHTML, /book-section-pager|読解ストラテジー/, 'opens in book phase');
assert.doesNotMatch(workspace.innerHTML, /Timer Starts/, 'no timed start offered for strategy page');
assert.equal(state.stats['RP:dokkai-n3-l03'], undefined, 'book browsing must not create re-read records');
reader.closeReadingWorkspace();
console.log('2a. Non-gradable lesson opens in the book; no timer, no records.');

// 2b. Start practice with ONLY the strategy page selected: refuses with hint
state.readingSelectedLessons = new Set(['dokkai-n3-l03']);
state.readingSelectionEmpty = false;
const hint = document.getElementById('reading-start-hint');
hint.textContent = '';
reader.startReadingPractice();
assert.equal(state.activeReadingLesson, null, 'practice must not open a strategy-only selection');
assert.match(hint.textContent, /Read as book/, 'hint points to the book');
console.log('2b. Practice on strategy-only selection refused with guidance.');

// 2c. Mixed selection: strategy page skipped, real lesson practised
state.readingSelectedLessons = new Set(['dokkai-n3-l03', 'dokkai-n3-l04']);
hint.textContent = '';
reader.startReadingPractice();
assert.equal(state.activeReadingLesson?.id, 'dokkai-n3-l04', 'practice opens the gradable lesson');
assert.match(hint.textContent, /skipped/, 'hint reports skipped strategy page');
reader.closeReadingWorkspace();
console.log('2c. Mixed selection skips strategy pages and practises real lessons.');

// 5. Regression: real lesson still grades and schedules a re-read
const l05 = db['dokkai-n3-l05'];
const q = l05.comprehensionQuestions[0];
reader.openReadingLesson('dokkai-n3-l05');
assert.match(workspace.innerHTML, /Timer Starts/, 'gradable lesson still offers timed reading');
reader.startReadingPassage();
reader.goToQuestions();
reader.selectQuizOption(q.id, Number(q.correctAnswer)); // single question auto-submits
assert.match(workspace.innerHTML, /Great Job/, 'correct answer still celebrates');
assert.doesNotMatch(workspace.innerHTML, /Nothing to grade here/);
const rp5 = state.stats['RP:dokkai-n3-l05'];
assert.ok(rp5, 're-read record created for real lesson');
assert.equal(rp5.reads, 1);
assert.equal(rp5.mastered, false, 'one read never masters');
reader.closeReadingWorkspace();
console.log('5. Real lesson flow grades and schedules re-reads unchanged.');

// 3. Safety net present in source (no public path can reach an empty submit now)
const src = fs.readFileSync('js/reader.js', 'utf8');
assert.match(src, /questions\.length === 0 \|\| readerRuntime\.charCount === 0/);
assert.match(src, /ungraded: true/);
assert.match(src, /Nothing to grade here/);
const submitFn = src.slice(src.indexOf('export function submitQuizAnswers()'), src.indexOf('function updateLayerARereadPassage'));
assert.ok(submitFn.indexOf('ungraded: true') < submitFn.indexOf('updateLayerARereadPassage('), 'guard runs before any stat write');
assert.doesNotMatch(src, /accuracy = questions\.length > 0 \? \(correctCount \/ questions\.length\) : 1/, 'vacuous 100% accuracy default removed or unreachable');
console.log('3. Empty-submit safety net verified in source.');


// ---------- Furigana toggle + book section changes (2026-11-03 asks) ----------
// Strategy ruby data present and text-preserving
const stripRuby = (h) => h.replace(/<rt>[^<]*<\/rt>/g, '').replace(/<\/?ruby>/g, '');
for (const [file, ids] of [['data/reading/part1_foundation.json', ['dokkai-n3-l03','dokkai-n3-l04','dokkai-n3-l05','dokkai-n3-l06','dokkai-n3-l07','dokkai-n3-l08','dokkai-n3-l09']], ['data/reading/passages.json', ['dokkai-n3-l03','dokkai-n3-l04','dokkai-n3-l05','dokkai-n3-l06']]]) {
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  for (const l of data.lessons) {
    if (!ids.includes(l.id) || !l.readingStrategy) continue;
    assert.ok(l.readingStrategy.rule_ja_ruby, `${l.id} rule ruby missing in ${file}`);
    assert.equal(stripRuby(l.readingStrategy.rule_ja_ruby), l.readingStrategy.rule_ja, `${l.id} ruby must preserve text`);
    for (const kp of l.readingStrategy.keyPoints || []) {
      if (kp.point_ja_ruby) assert.equal(stripRuby(kp.point_ja_ruby), kp.point_ja, `${l.id} keypoint ruby must preserve text`);
    }
  }
}
console.log('6. Strategy furigana data present and text-preserving in both files.');

// Toggle defaults off; strategy section renders plain, then ruby after toggle
elements.get('dokkai-workspace-container') && (workspace.innerHTML = '');
reader.openReadingLesson('dokkai-n3-l04', { startPhase: 'book' });
assert.match(workspace.innerHTML, /toggleStrategyFurigana/, 'furigana toggle offered on strategy section');
assert.doesNotMatch(workspace.innerHTML, /<ruby>/, 'furigana hidden by default');
reader.toggleStrategyFurigana();
assert.match(workspace.innerHTML, /<ruby>前後関係<rt>ぜんごかんけい<\/rt><\/ruby>/, 'toggle shows accurate ruby');
assert.match(workspace.innerHTML, /ふりがな/, 'toggle persists on section');
reader.toggleStrategyFurigana();
assert.doesNotMatch(workspace.innerHTML, /<ruby>/, 'toggle back off hides ruby');
const savedSettings = JSON.parse(memStore.get('n3_reader_settings'));
assert.equal(savedSettings.showStrategyFurigana, false, 'setting persisted');

// Key Vocabulary book section removed; strategy/drills/tough sections intact
const sectionPicker = workspace.innerHTML;
assert.doesNotMatch(sectionPicker, /重要語彙 Key Vocabulary/, 'Key Vocabulary section removed from book');
assert.doesNotMatch(sectionPicker, /bookVocabChipHtml\(v\) \)\?/, '');
reader.openReadingLesson('dokkai-n3-l04', { startPhase: 'book', bookSectionIndex: 99 });
const sectionsShown = workspace.innerHTML;
assert.match(sectionsShown, /Strategy/, 'strategy section kept');
reader.closeReadingWorkspace();

// Section list itself: vocab gone, tough kept (source-level)
const sectionsSrc = src.slice(src.indexOf('function getBookSections'), src.indexOf('function bookNavSection'));
assert.ok(!sectionsSrc.includes("id: 'vocab'"), 'vocab book section no longer registered');
assert.ok(sectionsSrc.includes("id: 'tough'"), 'tough-words section kept');

// Home drills still pool full lesson vocabulary (drill access not lost)
const drillSrc = src.slice(src.indexOf('export function startReadingWordDrill'), src.indexOf('export function restartReadingWordDrill'));
assert.match(drillSrc, /l\.vocabulary|lesson\.vocabulary|vocabulary/, 'home word drill pools lesson vocabulary');
console.log('7. Furigana toggle works (default off, persisted); Key Vocabulary book section removed; home drills intact.');

console.log('All reading checks passed.');

