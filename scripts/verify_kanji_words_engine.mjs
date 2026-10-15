#!/usr/bin/env node
/**
 * scripts/verify_kanji_words_engine.mjs
 * Verification test harness for WP-5: Kanji Word Drills & Runner Engine
 * Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §1, §2, §7 and WP-5.
 *
 * Tests:
 * 1. Reading distractor generation (asserts okurigana matching rule).
 * 2. Writing distractor generation.
 * 3. Facet unlocking rule (KWW requires KWR reps >= 2; KWM only if not in vocab DB).
 * 4. Kanji mastery score derivation from words (grey, amber, blue, green, hasLeech).
 * 5. S0–S6 lesson runner chunking (chunks of 3 kanji) and lifecycle flow.
 */

import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import {
  FACET_READING,
  FACET_WRITING,
  FACET_MEANING,
  OKURIGANA_REGEX,
  SOUND_FAMILIES,
  getFacetKey,
  getOkurigana,
  generateDistractors,
  buildWordCard,
  isFacetUnlocked,
  calculateKanjiMastery,
  N3KanjiWords
} from '../js/kanji-words.js';

import {
  CHUNK_KANJI,
  CRITERION_CORRECT,
  REQUEUE_OFFSET,
  MAX_REQUEUES,
  MIN_FIRST_GAP_MS,
  KanjiLessonRunner,
  createLessonRunner,
  N3KanjiRunner
} from '../js/kanji-runner.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DATA_DIR = path.join(ROOT_DIR, 'data');

function readJson(relPath) {
  const full = path.join(DATA_DIR, relPath);
  return JSON.parse(fs.readFileSync(full, 'utf-8'));
}

console.log('===========================================================');
console.log('NIHONGO INTERMEDIATE — WP-5 Kanji Words & Runner Test Suite');
console.log('===========================================================\n');

// 1. Ingest Kanji Data from Lesson 1–5
const kanjiPart1 = readJson('kanji/part1_lessons_01_05.json');
const lesson1 = kanjiPart1.lessons.find(l => l.lesson_number === 1);

assert.ok(lesson1, 'Lesson 1 must exist in part1_lessons_01_05.json');
const lesson1Kanji = lesson1.kanji;
assert.ok(lesson1Kanji.length >= 18, `Lesson 1 contains ${lesson1Kanji.length} kanji (expected >= 18)`);

const kanjiDB = {};
for (const k of lesson1Kanji) {
  kanjiDB[k.kanji] = {
    ...k,
    part: 1,
    lesson_number: 1
  };
}

// Ingest vocabulary to test vocab DB overlap
let vocabDB = {};
try {
  const vocabJson = readJson('vocabulary.json');
  for (const w of vocabJson) {
    const ch = w.chapter || 'unknown';
    if (!vocabDB[ch]) vocabDB[ch] = [];
    vocabDB[ch].push(w);
  }
} catch (_) {
  vocabDB = {};
}

// Extract all target words for Lesson 1
const lesson1Words = [];
for (const k of lesson1Kanji) {
  for (const w of (k.words || [])) {
    if (w.is_target) {
      lesson1Words.push({
        ...w,
        homeKanji: k.kanji,
        lesson: 1,
        part: 1
      });
    }
  }
}

// =========================================================================
// TEST 1: Reading Distractor Generation & Okurigana Matching Rule
// =========================================================================
console.log('[TEST 1/5] Testing Reading Distractor Generation & Okurigana Rule...');

// 1.1 Test word with okurigana: "辺り" (あたり) -> okurigana is "り"
const targetOkuri = { term_ja: '辺り', reading: 'あたり', meaning_en: 'Surroundings', lesson: 1 };
const okuriDistractors = generateDistractors(targetOkuri, FACET_READING, lesson1Words, lesson1Words);

assert.equal(okuriDistractors.length, 3, 'Must return exactly 3 distractors');
assert.ok(!okuriDistractors.includes('あたり'), 'Distractors must never include correct reading');
assert.equal(new Set(okuriDistractors).size, 3, 'All 3 distractors must be distinct');

for (const d of okuriDistractors) {
  assert.ok(
    d.endsWith('り'),
    `Okurigana Rule Violation: Distractor "${d}" does not end with required okurigana "り" for target "${targetOkuri.term_ja}"`
  );
  assert.ok(
    Math.abs(d.length - targetOkuri.reading.length) <= 1,
    `Reading Length Rule: Distractor "${d}" (len ${d.length}) exceeds ±1 kana of "${targetOkuri.reading}" (len ${targetOkuri.reading.length})`
  );
}

console.log(`  ✓ '辺り' (あたり) produced distractors: [${okuriDistractors.join(', ')}] — all end with 'り' and within ±1 length`);

// 1.2 Test synthetic/edge case okurigana word: "割る" (わる) -> okurigana "る"
const targetOkuriRu = { term_ja: '割る', reading: 'わる', meaning_en: 'To divide', lesson: 1 };
const ruDistractors = generateDistractors(targetOkuriRu, FACET_READING, [], []);
assert.equal(ruDistractors.length, 3, 'Must return exactly 3 distractors for edge okurigana word');
for (const d of ruDistractors) {
  assert.ok(
    d.endsWith('る'),
    `Okurigana Rule Violation: Distractor "${d}" must end with "る" for "割る"`
  );
}
console.log(`  ✓ '割る' (わる) produced distractors: [${ruDistractors.join(', ')}] — all end with 'る'`);

// 1.3 Test compound kanji word without okurigana: "市場" (いちば)
const targetCompound = { term_ja: '市場', reading: 'いちば', meaning_en: 'Market', lesson: 1 };
const compoundDistractors = generateDistractors(targetCompound, FACET_READING, lesson1Words, lesson1Words);

assert.equal(compoundDistractors.length, 3, 'Must return exactly 3 distractors for compound word');
assert.ok(!compoundDistractors.includes('いちば'), 'Distractors must never include correct reading');
assert.equal(new Set(compoundDistractors).size, 3, 'All 3 distractors must be distinct');
console.log(`  ✓ '市場' (いちば) produced distractors: [${compoundDistractors.join(', ')}]`);

// =========================================================================
// TEST 2: Writing Distractor Generation
// =========================================================================
console.log('\n[TEST 2/5] Testing Writing Distractor Generation...');

const writingDistractors = generateDistractors(targetCompound, FACET_WRITING, lesson1Words, lesson1Words);
assert.equal(writingDistractors.length, 3, 'Writing must return exactly 3 distractors');
assert.ok(!writingDistractors.includes('市場'), 'Writing distractors must not include correct kanji');
assert.equal(new Set(writingDistractors).size, 3, 'All 3 writing distractors must be distinct');

// Check sound family data integrity
assert.ok(SOUND_FAMILIES.length >= 35, `Sound families must contain >= 35 groups (found ${SOUND_FAMILIES.length})`);
const banFamily = SOUND_FAMILIES.find(f => f.includes('反'));
assert.ok(banFamily && banFamily.includes('坂') && banFamily.includes('板') && banFamily.includes('返'), 'Sound family 反/坂/板/返 must be present');

console.log(`  ✓ '市場' writing produced distractors: [${writingDistractors.join(', ')}]`);

// =========================================================================
// TEST 3: Facet Unlocking Rules
// =========================================================================
console.log('\n[TEST 3/5] Testing Facet Unlocking Rules...');

// 3.1 KWR is unlocked at learn time
assert.equal(isFacetUnlocked('市場', FACET_READING, {}), true, 'KWR must be unlocked at learn time');

// 3.2 KWW requires KWR reps >= 2 (doc 02 §1.1, ME-4)
assert.equal(isFacetUnlocked('市場', FACET_WRITING, {}), false, 'KWW must be locked when KWR record does not exist');
assert.equal(isFacetUnlocked('市場', FACET_WRITING, { 'KWR:市場': { reps: 0 } }), false, 'KWW must be locked when reps == 0');
assert.equal(isFacetUnlocked('市場', FACET_WRITING, { 'KWR:市場': { reps: 1 } }), false, 'KWW must be locked when reps == 1');
assert.equal(isFacetUnlocked('市場', FACET_WRITING, { 'KWR:市場': { reps: 2 } }), true, 'KWW must unlock when reps == 2 (ME-4)');
assert.equal(isFacetUnlocked('市場', FACET_WRITING, { 'KWR:市場': { reps: 5 } }), true, 'KWW must stay unlocked when reps > 2');

// 3.3 KWM unlocked at learn time ONLY if NOT in vocab DB (doc 02 §1.1 Rule 1, ME-5)
assert.equal(isFacetUnlocked('市場', FACET_MEANING, {}, { vocabId: 'v03-017' }), false, 'KWM must be locked if word has vocabId (credit to V:)');
assert.equal(isFacetUnlocked('毛糸', FACET_MEANING, {}, { vocabId: null }), true, 'KWM must be unlocked if word has no vocabId');

console.log('  ✓ Facet unlock verified: KWR learn-time, KWW reps>=2, KWM non-vocab only');

// =========================================================================
// TEST 4: Derived Kanji Mastery Score and Status
// =========================================================================
console.log('\n[TEST 4/5] Testing Derived Kanji Mastery Score & Status (doc 02 §7.1)...');

const testWord = { term_ja: '市場', isTarget: true, vocabId: 'v03-017' };

// 4.1 Unseen -> score = 0, status = 'grey'
const masteryUnseen = calculateKanjiMastery('市', [testWord], {});
assert.equal(masteryUnseen.score, 0.0, 'Unseen kanji must have score 0.0');
assert.equal(masteryUnseen.status, 'grey', 'Unseen kanji must have status grey');
assert.equal(masteryUnseen.hasLeech, false, 'Unseen kanji must not have leech');

// 4.2 Learning -> score = 0.3, status = 'amber'
const statsLearning = {
  'KWR:市場': { reps: 1, interval: 1, correct: 1 },
  'KWW:市場': { reps: 0, interval: 0, correct: 0 },
  'V:v03-017': { reps: 1, interval: 1, correct: 1 }
};
const masteryLearning = calculateKanjiMastery('市', [testWord], statsLearning);
assert.ok(masteryLearning.score > 0 && masteryLearning.score < 0.4, `Learning score should be < 0.4 (got ${masteryLearning.score})`);
assert.equal(masteryLearning.status, 'amber', 'Learning kanji must have status amber');

// 4.3 Solid Review -> score in 0.4..0.8, status = 'blue'
const statsReview = {
  'KWR:市場': { reps: 2, interval: 6, correct: 2 },
  'KWW:市場': { reps: 2, interval: 6, correct: 2 },
  'V:v03-017': { reps: 2, interval: 6, correct: 2 }
};
const masteryReview = calculateKanjiMastery('市', [testWord], statsReview);
assert.ok(masteryReview.score >= 0.4 && masteryReview.score < 0.8, `Review score should be in 0.4..0.8 (got ${masteryReview.score})`);
assert.equal(masteryReview.status, 'blue', 'Solid review kanji must have status blue');

// 4.4 Mastered -> score >= 0.8 (1.0), status = 'green'
const statsMastered = {
  'KWR:市場': { reps: 4, interval: 21, weight: 0.7, correct: 4 },
  'KWW:市場': { reps: 4, interval: 21, weight: 0.7, correct: 4 },
  'V:v03-017': { reps: 4, interval: 21, weight: 0.7, correct: 4 }
};
const masteryMastered = calculateKanjiMastery('市', [testWord], statsMastered);
assert.equal(masteryMastered.score, 1.0, 'Mastered kanji must have score 1.0');
assert.equal(masteryMastered.status, 'green', 'Mastered kanji must have status green');

// 4.5 Leech / Hard red dot trigger
const statsLeech = {
  'KWR:市場': { reps: 2, interval: 2, weight: 1.9, lapses: 5, leech: true },
  'KWW:市場': { reps: 0 },
  'V:v03-017': { reps: 0 }
};
const masteryLeech = calculateKanjiMastery('市', [testWord], statsLeech);
assert.equal(masteryLeech.hasLeech, true, 'hasLeech must be true when facet has leech/weight>=1.8');

console.log('  ✓ Kanji mastery derived correctly: grey (0.0), amber (0.3), blue (0.7), green (1.0), hasLeech red dot');

// =========================================================================
// TEST 5: S0–S6 Lesson Runner Flow & 3-Kanji Chunking
// =========================================================================
console.log('\n[TEST 5/5] Testing S0–S6 Lesson Runner Flow & 3-Kanji Chunking...');

const sharedStats = {};
const runner = createLessonRunner(1, {
  db: { kanjiDB },
  stats: sharedStats
});

// 5.1 Assert Chunking: chunks of 3 kanji (doc 02 §2.1)
assert.equal(CHUNK_KANJI, 3, 'CHUNK_KANJI constant must be 3');

// Test 18 kanji split into exactly 6 chunks of 3 kanji
const kanji18DB = {};
for (const k of lesson1Kanji.slice(0, 18)) {
  kanji18DB[k.kanji] = { ...k, part: 1, lesson_number: 101 };
}
const runner18 = createLessonRunner(101, { db: { kanjiDB: kanji18DB } });
assert.equal(runner18.chunks.length, 6, `18 kanji must be partitioned into exactly 6 chunks (18 / 3 = 6). Got ${runner18.chunks.length}`);
for (let i = 0; i < runner18.chunks.length; i++) {
  assert.equal(runner18.chunks[i].kanjiList.length, 3, `Chunk ${i} of 18-kanji runner must have exactly 3 kanji`);
}
console.log('  ✓ 18 kanji correctly partitioned into 6 chunks of 3 kanji');

// Test full lesson runner chunking
const expectedChunks = Math.ceil(lesson1Kanji.length / CHUNK_KANJI);
assert.equal(runner.chunks.length, expectedChunks, `Lesson 1 (${lesson1Kanji.length} kanji) partitioned into ${expectedChunks} chunks`);
for (let i = 0; i < runner.chunks.length; i++) {
  const ch = runner.chunks[i];
  const expectedLen = (i === runner.chunks.length - 1 && lesson1Kanji.length % CHUNK_KANJI !== 0) ? (lesson1Kanji.length % CHUNK_KANJI) : CHUNK_KANJI;
  assert.equal(ch.kanjiList.length, expectedLen, `Chunk ${i} must have ${expectedLen} kanji`);
  assert.ok(ch.targetWords.length > 0, `Chunk ${i} must contain target words`);
}
console.log(`  ✓ Lesson 1 (${lesson1Kanji.length} kanji) correctly partitioned into ${expectedChunks} chunks of 3 kanji`);

// 5.2 S0 Placement: test marking kanji known
assert.equal(runner.currentStage, 'S0', 'Runner must begin at S0 (Placement)');
runner.submitPlacement(['辺', '市']);

assert.ok(runner.knownKanjiSet.has('辺') && runner.knownKanjiSet.has('市'), 'Placement must record known kanji');
assert.ok(sharedStats['KWR:辺り'], 'KWR record must be created for target word of known kanji');
assert.equal(sharedStats['KWR:辺り'].reps, 2, 'KWR record for known kanji must have reps=2');
assert.equal(sharedStats['KWR:辺り'].interval, 4, 'KWR record for known kanji must have interval=4');
console.log('  ✓ S0 Placement creates verified KWR records (reps=2, interval=4d)');

// 5.3 S1 Meet the chunk
assert.equal(runner.currentStage, 'S1', 'After S0 placement, runner must advance to S1');
runner.advanceFromMeet();

// 5.4 S2 Recognise (Reading MCQ) & first-try tracking
assert.equal(runner.currentStage, 'S2', 'Runner must advance to S2');
const s2Card = runner.getCurrentCard();
assert.ok(s2Card, 'S2 must present a card');
assert.equal(s2Card.facet, FACET_READING, 'S2 card must be Reading facet');

// Submit correct answer
const firstWord = s2Card.term_ja;
runner.submitAnswer(s2Card.correctIndex);
assert.ok(runner.firstTryCorrectS2.has(firstWord), 'First try correct answer in S2 must be remembered for S5');

// Clear rest of S2
while (runner.currentStage === 'S2') {
  const c = runner.getCurrentCard();
  runner.submitAnswer(c.correctIndex);
}

// 5.5 S3 Recall (Flashcard)
assert.equal(runner.currentStage, 'S3', 'Runner must advance to S3 Recall');
while (runner.currentStage === 'S3') {
  runner.submitAnswer(3); // Grade Good
}

// 5.6 S4 Criterion (Loop until every word has 2 correct, wrong -> +3 requeue)
assert.equal(runner.currentStage, 'S4', 'Runner must advance to S4 Criterion');

// Test S4 wrong answer requeue (+3 positions later, ME-2, ME-3)
const cCard = runner.getCurrentCard();
const testTerm = cCard.term_ja;
const initialQueueLen = runner.queue.length;

// Submit wrong answer
runner.submitAnswer(false);
const trackerAfterWrong = runner.criterionTracker.get(testTerm);
assert.equal(trackerAfterWrong.correctCount, 0, 'ME-3: Wrong answer must reset correct count to 0');
assert.equal(trackerAfterWrong.requeues, 1, 'ME-2: Wrong answer must increment requeue count');
assert.ok(runner.queue.length > initialQueueLen, 'ME-2: Wrong card must be re-inserted into queue');

// Complete S4 criterion loop (all words reach 2 correct)
let s4Safety = 0;
while (runner.currentStage === 'S4' && s4Safety < 100) {
  s4Safety++;
  const c = runner.getCurrentCard();
  if (!c) break;
  runner.submitAnswer(c.correctIndex);
}
assert.ok(s4Safety < 100, 'S4 must terminate cleanly once criterion is reached');

// Assert ME-1: Graduation at end of chunk's S4
const chunk0Words = runner.chunks[0].targetWords;
for (const w of chunk0Words) {
  const k = `KWR:${w.term_ja}`;
  assert.ok(sharedStats[k], `ME-1: Target word ${k} must exist in stats after chunk S4`);
  assert.equal(sharedStats[k].reps, 1, `ME-1: Graduated card ${k} must have reps=1`);
}
console.log('  ✓ S4 Criterion loop verified (ME-2 requeue, ME-3 reset on wrong, ME-1 graduation reps=1)');

// 5.7 S5 Writing (only first-try S2 words)
assert.equal(runner.currentStage, 'S5', 'Runner must advance to S5 Writing');
while (runner.currentStage === 'S5') {
  const c = runner.getCurrentCard();
  runner.submitAnswer(c.correctIndex);
}

// Advance through remaining chunks directly to S6
while (runner.currentStage !== 'S6' && runner.currentStage !== 'COMPLETE') {
  if (runner.currentStage === 'S1') {
    runner.advanceFromMeet();
  } else {
    const c = runner.getCurrentCard();
    if (c) {
      runner.submitAnswer(runner.currentStage === 'S3' ? 3 : c.correctIndex);
    }
  }
}

// 5.8 S6 Lesson Test (all lesson words, mixed reading + writing)
assert.equal(runner.currentStage, 'S6', 'Runner must reach S6 Lesson Test');
const s6Card = runner.getCurrentCard();
assert.ok(s6Card, 'S6 must present exam questions');

// Finish S6 with 1 simulated error to test lapse and weak queue
let firstMissed = null;
while (runner.currentStage === 'S6') {
  const c = runner.getCurrentCard();
  if (!firstMissed) {
    firstMissed = c.term_ja;
    // Intentionally miss the first question
    runner.submitAnswer(-1);
  } else {
    runner.submitAnswer(c.correctIndex);
  }
}

assert.equal(runner.currentStage, 'COMPLETE', 'Runner must reach COMPLETE state');
const summary = runner.getSummary();

assert.equal(summary.lessonNumber, 1, 'Summary must report correct lesson number');
assert.ok(summary.missedWords.includes(firstMissed), 'Missed word must be tracked in summary weak list');
assert.ok(summary.accuracyPct > 0 && summary.accuracyPct <= 100, 'Accuracy percentage must be valid');
console.log(`  ✓ S6 Lesson Test complete: accuracy ${summary.accuracyPct}%, missed words recorded in Weak queue`);

// =========================================================================
// SUMMARY
// =========================================================================
console.log('\n===========================================================');
console.log('SUCCESS: All 5 test suites passed cleanly!');
console.log('  1. Reading Distractor Generator & Okurigana Rule: PASSED');
console.log('  2. Writing Distractor Generator & Sound Families: PASSED');
console.log('  3. Facet Unlocking (ME-4, ME-5): PASSED');
console.log('  4. Derived Kanji Mastery Score & Status: PASSED');
console.log('  5. S0–S6 Lesson Runner & Chunking (ME-1, ME-2, ME-3): PASSED');
console.log('===========================================================');
process.exit(0);
