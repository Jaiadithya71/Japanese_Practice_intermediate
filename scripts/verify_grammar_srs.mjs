#!/usr/bin/env node
/**
 * scripts/verify_grammar_srs.mjs
 * Verification Test Harness for WP-9: Grammar Revision Engine
 * Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §9 and WP-9.
 *
 * Verifies:
 * 1. Composite key generation and bidirectional key parsing for GD, GS, GT.
 * 2. Star question grading logic:
 *    - Full match = Good (3)
 *    - Lucky star = Hard (2) and reveals correct sentence
 *    - Mismatch = Again (1)
 * 3. Contrast "vs" panel retrieval for rival patterns:
 *    - Target pattern details, cluster identification, nearest rivals with 1-line English meanings.
 *    - "You chose X: it means Y" comparison note generation.
 * 4. Cluster session interleaving (ME-16):
 *    - Guarantees no two consecutive cards belong to the same pattern while alternatives exist.
 * 5. Pattern mastery derivation and "Learned" criterion (ME-15):
 *    - Pattern score = mean(scores of tagged cards).
 *    - Pattern counts as "Learned" ONLY when >= 2 distinct cards have been passed.
 *    - Pattern mastery capped at 0.6 until at least 2 cards passed.
 */

import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import {
  FACET_DECISION,
  FACET_STAR,
  FACET_TEXT,
  FACET_CONTRAST,
  formatGrammarKey,
  parseGrammarKey,
  toCompositeKey,
  buildGrammarCard,
  gradeStarQuestion,
  getStarGrade,
  gradeGrammarDecision,
  getContrastVsData,
  renderContrastVsPanel,
  interleaveByPattern,
  buildClusterSession,
  computeCardScore,
  isCardPassed,
  getPatternMastery,
  isPatternLearned,
  setGrammarDatasets,
  getAllClusters,
  getCluster,
  getPatternsInCluster,
  N3GrammarSRS
} from '../js/grammar-srs.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DATA_DIR = path.join(ROOT_DIR, 'data');
const GRAMMAR_DIR = path.join(DATA_DIR, 'grammar');

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
}

console.log('===========================================================');
console.log('NIHONGO INTERMEDIATE — WP-9 Grammar Revision Engine Tests');
console.log('===========================================================\n');

// ---------------------------------------------------------------------
// 1. DATA INGESTION & DATASET SETUP
// ---------------------------------------------------------------------
console.log('--- Step 1: Ingesting Real Grammar Datasets ---');

const drillTags = readJson(path.join(GRAMMAR_DIR, 'drill_tags.json'));
const clustersData = readJson(path.join(GRAMMAR_DIR, 'clusters.json'));
const grammarIndex = readJson(path.join(GRAMMAR_DIR, 'grammar_index.json'));
const p1aData = readJson(path.join(GRAMMAR_DIR, 'part1_sec1_to_6.json'));
const p1bData = readJson(path.join(GRAMMAR_DIR, 'part1_sec7_to_12.json'));
const p2Data = readJson(path.join(GRAMMAR_DIR, 'part2_sentence_grammar2.json'));
const p3Data = readJson(path.join(GRAMMAR_DIR, 'part3_text_grammar.json'));

const clusters = clustersData.clusters || [];
setGrammarDatasets({ grammarIndex, drillTags, clusters });

console.log(`Loaded ${Object.keys(drillTags).length} drill tags, ${clusters.length} clusters, ${grammarIndex.length} grammar patterns.`);
assert.ok(Object.keys(drillTags).length >= 490, 'Drill tags count should be ~495');
assert.ok(clusters.length === 9, 'Expected 9 confusion clusters');
assert.ok(grammarIndex.length >= 83, 'Expected >= 83 grammar patterns');
console.log('✓ Step 1 Passed: Grammar datasets successfully ingested.\n');

// ---------------------------------------------------------------------
// 2. COMPOSITE KEY GENERATION & KEY PARSING (GD, GS, GT)
// ---------------------------------------------------------------------
console.log('--- Step 2: Testing Key Formatting & Bidirectional Parsing ---');

// 2.1 formatGrammarKey
const keyGD = formatGrammarKey('GD', { part: 'p1a', sec: '1', qid: 101 });
assert.strictEqual(keyGD, 'GD:p1a:1:101', 'GD key format must match GD:<part>:<sec>:<qid>');

const keyGS = formatGrammarKey('GS', { part: 'p1a', sec: '2', qid: 216 });
assert.strictEqual(keyGS, 'GS:p1a:2:216', 'GS key format must match GS:<part>:<sec>:<qid>');

const keyGT = formatGrammarKey('GT', { passage_id: 301, qid: 30101 });
assert.strictEqual(keyGT, 'GT:301:30101', 'GT key format must match GT:<passage_id>:<qid>');

const keyGTSec = formatGrammarKey('GT', { part: 'p3', sec: '1', qid: 30101 });
assert.strictEqual(keyGTSec, 'GT:p3:1:30101', 'GT fallback key format must match GT:<part>:<sec>:<qid>');

const keyGC = formatGrammarKey('GC', { patternId: 'P1-1', variantIndex: 2 });
assert.strictEqual(keyGC, 'GC:P1-1:2', 'GC key format must match GC:<patternId>:<variantIndex>');

// 2.2 parseGrammarKey
const parsedGD = parseGrammarKey('GD:p1a:1:101');
assert.strictEqual(parsedGD.facet, 'GD');
assert.strictEqual(parsedGD.part, 'p1a');
assert.strictEqual(parsedGD.sec, '1');
assert.strictEqual(parsedGD.qid, 101);
assert.strictEqual(parsedGD.compositeKey, 'p1a:1:101');

const parsedGS = parseGrammarKey('GS:p2:1:701');
assert.strictEqual(parsedGS.facet, 'GS');
assert.strictEqual(parsedGS.part, 'p2');
assert.strictEqual(parsedGS.sec, '1');
assert.strictEqual(parsedGS.qid, 701);
assert.strictEqual(parsedGS.compositeKey, 'p2:1:701');

const parsedGT = parseGrammarKey('GT:301:30101');
assert.strictEqual(parsedGT.facet, 'GT');
assert.strictEqual(parsedGT.passage_id, 301);
assert.strictEqual(parsedGT.qid, 30101);

const parsedGTSec = parseGrammarKey('GT:p3:1:30101');
assert.strictEqual(parsedGTSec.facet, 'GT');
assert.strictEqual(parsedGTSec.part, 'p3');
assert.strictEqual(parsedGTSec.sec, '1');
assert.strictEqual(parsedGTSec.qid, 30101);

// 2.3 Card Builder on Real Drills
const sampleDrill101 = p1aData.sections[0].drills[0];
const sampleCardGD = buildGrammarCard(sampleDrill101, { part: 'p1a', sec: '1' });
assert.strictEqual(sampleCardGD.key, 'GD:p1a:1:101');
assert.strictEqual(sampleCardGD.facet, 'GD');
assert.strictEqual(sampleCardGD.type, 'grammar_decision');
assert.ok(sampleCardGD.patterns.includes('P1-1'), 'Drill 101 must be tagged with P1-1');
assert.strictEqual(sampleCardGD.cluster, 'time');

const sampleDrill216 = p1aData.sections[1].drills.find(d => d.question_id === 216);
const sampleCardGS = buildGrammarCard(sampleDrill216, { part: 'p1a', sec: '2' });
assert.strictEqual(sampleCardGS.key, 'GS:p1a:2:216');
assert.strictEqual(sampleCardGS.facet, 'GS');
assert.strictEqual(sampleCardGS.type, 'grammar_star');
assert.deepStrictEqual(sampleCardGS.correct_order, [4, 3, 2, 1]);
assert.strictEqual(sampleCardGS.star_slot_index, 2);
assert.strictEqual(sampleCardGS.star_answer, 2);
assert.strictEqual(sampleCardGS.tiles.length, 4);
assert.strictEqual(sampleCardGS.tiles[0].id, 1);
assert.strictEqual(sampleCardGS.tiles[0].text, '歩いたので');

console.log('✓ Step 2 Passed: Composite keys and card structures validated.\n');

// ---------------------------------------------------------------------
// 3. STAR QUESTION GRADING LOGIC (doc 02 §9.5, ME-14)
// ---------------------------------------------------------------------
console.log('--- Step 3: Testing Star Question Grading Logic (Good / Hard / Again) ---');

const testStarCard = {
  key: 'GS:test:1:999',
  correct_order: [4, 3, 2, 1],
  star_slot_index: 2, // 3rd position (0-based index 2)
  correct_answer: 2,  // tile at index 2 is tile 2
  full_sentence: '朝からずっと立ちっぱなしで歩いたので疲れてしまった。',
  full_sentence_en: 'I was tired from standing all day and walking since morning.'
};

// 3.1 Full Match -> Grade 3 (Good)
const resultFullMatch = gradeStarQuestion([4, 3, 2, 1], testStarCard);
assert.strictEqual(resultFullMatch.grade, 3, 'Full match must be Grade 3 (Good)');
assert.strictEqual(resultFullMatch.gradeName, 'Good');
assert.strictEqual(resultFullMatch.isFullMatch, true);
assert.strictEqual(resultFullMatch.isStarCorrect, true);
assert.strictEqual(getStarGrade([4, 3, 2, 1], testStarCard), 3);

// 3.2 Lucky Star -> Grade 2 (Hard) and reveals correct sentence
// User placed [1, 3, 2, 4]: full order is wrong, but slot index 2 has tile 2 (correct star tile!)
const resultLuckyStar = gradeStarQuestion([1, 3, 2, 4], testStarCard);
assert.strictEqual(resultLuckyStar.grade, 2, 'Lucky star must be Grade 2 (Hard)');
assert.strictEqual(resultLuckyStar.gradeName, 'Hard');
assert.strictEqual(resultLuckyStar.isFullMatch, false);
assert.strictEqual(resultLuckyStar.isStarCorrect, true);
assert.strictEqual(getStarGrade([1, 3, 2, 4], testStarCard), 2);
assert.ok(resultLuckyStar.fullSentence.length > 0, 'Must include full correct sentence on lucky star');
assert.strictEqual(resultLuckyStar.fullSentence, testStarCard.full_sentence);

// 3.3 Mismatch -> Grade 1 (Again)
// User placed [1, 2, 3, 4]: slot index 2 has tile 3, which is NOT star tile 2
const resultMismatch = gradeStarQuestion([1, 2, 3, 4], testStarCard);
assert.strictEqual(resultMismatch.grade, 1, 'Mismatch must be Grade 1 (Again)');
assert.strictEqual(resultMismatch.gradeName, 'Again');
assert.strictEqual(resultMismatch.isFullMatch, false);
assert.strictEqual(resultMismatch.isStarCorrect, false);
assert.strictEqual(getStarGrade([1, 2, 3, 4], testStarCard), 1);

// 3.4 Verification with actual Part 2 Star drill (Drill 701)
let drill701 = null;
let sec701 = '7';
for (const s of p2Data.sections) {
  const d = (s.drills || []).find(dr => dr.question_id === 701);
  if (d) {
    drill701 = d;
    sec701 = String(s.section_number);
    break;
  }
}
assert.ok(drill701 !== null, 'Drill 701 must be found in Part 2 data');
const card701 = buildGrammarCard(drill701, { part: 'p2', sec: sec701 });
// drill 701: correct_order = [2, 1, 4, 3], correct_answer = "4", star is at index 2 (tile 4)
assert.strictEqual(card701.star_slot_index, 2);
assert.strictEqual(card701.star_answer, 4);

assert.strictEqual(gradeStarQuestion([2, 1, 4, 3], card701).grade, 3);
assert.strictEqual(gradeStarQuestion([1, 2, 4, 3], card701).grade, 2); // lucky star: tile 4 in slot 2
assert.strictEqual(gradeStarQuestion([1, 2, 3, 4], card701).grade, 1); // mismatch: tile 3 in slot 2

console.log('✓ Step 3 Passed: Star grading logic conforms to doc 02 §9.5 (Good: 3, Hard: 2, Again: 1).\n');

// ---------------------------------------------------------------------
// 4. CONTRAST "VS" PANEL RETRIEVAL (doc 02 §9.6)
// ---------------------------------------------------------------------
console.log('--- Step 4: Testing Contrast "vs" Panel Retrieval ---');

// 4.1 Query by pattern ID 'P1-1'
const vsP1 = getContrastVsData('P1-1');
assert.strictEqual(vsP1.targetPattern.id, 'P1-1');
assert.strictEqual(vsP1.cluster.id, 'time');
assert.strictEqual(vsP1.cluster.name_en, 'Time & Timing');
assert.ok(vsP1.rivals.length > 0, 'Must retrieve rival patterns in cluster');

const rivalIds = vsP1.rivals.map(r => r.id);
assert.ok(rivalIds.includes('P1-2'), 'Rivals must include P1-2 (〜あいだ・〜あいだに)');
assert.ok(rivalIds.includes('P1-3'), 'Rivals must include P1-3 (〜てからでないと)');
assert.ok(rivalIds.includes('P1-4'), 'Rivals must include P1-4 (〜ところだ)');

for (const r of vsP1.rivals) {
  assert.ok(r.meaning_en && r.meaning_en.length > 5, `Rival ${r.id} must have 1-line English meaning`);
}

// 4.2 Query by drill card key
const vsCard = getContrastVsData('GD:p1a:1:101');
assert.strictEqual(vsCard.cluster.id, 'time');
assert.ok(vsCard.rivals.length > 0);

// 4.3 Learner wrong choice comparison note
const vsWithChoice = getContrastVsData('P1-1', { userChoicePattern: 'P1-2' });
assert.ok(vsWithChoice.userChoiceNote !== null);
assert.ok(vsWithChoice.userChoiceNote.includes('P1-2'), 'Note must mention chosen pattern P1-2');
assert.ok(vsWithChoice.userChoiceNote.includes('あいだ'), 'Note must include pattern name');

// 4.4 HTML rendering
const vsHtml = renderContrastVsPanel('P1-1', { userChoicePattern: 'P1-2' });
assert.ok(vsHtml.includes('grammar-vs-panel'), 'HTML must contain .grammar-vs-panel');
assert.ok(vsHtml.includes('Time & Timing'), 'HTML must display cluster title');
assert.ok(vsHtml.includes('grammar-vs-choice-alert'), 'HTML must contain choice alert');
assert.ok(vsHtml.includes('P1-1'), 'HTML must show target pattern');

console.log('✓ Step 4 Passed: Contrast "vs" panel successfully extracts rivals and summaries.\n');

// ---------------------------------------------------------------------
// 5. CLUSTER SESSION INTERLEAVING (doc 02 §9.6, ME-16)
// ---------------------------------------------------------------------
console.log('--- Step 5: Testing Cluster Session Interleaving (ME-16) ---');

// 5.1 Unit test with mock pool of cards across 3 patterns
const mockPool = [
  { id: 'c1', primaryPattern: 'P1-1', prompt: 'Prompt 1' },
  { id: 'c2', primaryPattern: 'P1-1', prompt: 'Prompt 2' },
  { id: 'c3', primaryPattern: 'P1-1', prompt: 'Prompt 3' },
  { id: 'c4', primaryPattern: 'P1-1', prompt: 'Prompt 4' },
  { id: 'c5', primaryPattern: 'P1-2', prompt: 'Prompt 5' },
  { id: 'c6', primaryPattern: 'P1-2', prompt: 'Prompt 6' },
  { id: 'c7', primaryPattern: 'P1-2', prompt: 'Prompt 7' },
  { id: 'c8', primaryPattern: 'P1-3', prompt: 'Prompt 8' },
  { id: 'c9', primaryPattern: 'P1-3', prompt: 'Prompt 9' }
];

const interleavedMock = interleaveByPattern(mockPool);
assert.strictEqual(interleavedMock.length, mockPool.length, 'Interleaved queue must keep all cards');

// Verify: no two consecutive cards share the same pattern
let consecutiveViolations = 0;
for (let i = 0; i < interleavedMock.length - 1; i++) {
  if (interleavedMock[i].primaryPattern === interleavedMock[i + 1].primaryPattern) {
    consecutiveViolations++;
  }
}
assert.strictEqual(consecutiveViolations, 0, 'No two consecutive cards may share the same pattern while alternatives exist');

// 5.2 Build real cluster session for 'time'
// Construct all available cards from p1a, p1b, p2
const allDrillCards = [];
for (const sec of p1aData.sections) {
  for (const dr of (sec.drills || [])) {
    allDrillCards.push(buildGrammarCard(dr, { part: 'p1a', sec: sec.section_number }));
  }
}
for (const sec of p1bData.sections) {
  for (const dr of (sec.drills || [])) {
    allDrillCards.push(buildGrammarCard(dr, { part: 'p1b', sec: sec.section_number }));
  }
}
for (const sec of p2Data.sections) {
  for (const dr of (sec.drills || [])) {
    allDrillCards.push(buildGrammarCard(dr, { part: 'p2', sec: sec.section_number }));
  }
}

const timeSession = buildClusterSession('time', { cardPool: allDrillCards, maxCards: 15 });
assert.ok(timeSession.length >= 5, 'Time session should contain at least 5 cards');
assert.ok(timeSession.length <= 15, 'Time session should respect maxCards limit');

const timePatterns = new Set(getPatternsInCluster('time'));
for (const card of timeSession) {
  const hasClusterPat = (card.patterns || []).some(p => timePatterns.has(p)) || card.cluster === 'time';
  assert.ok(hasClusterPat, `Card ${card.key} must belong to 'time' cluster`);
}

// Check interleaving on real session
let realConsecutiveViolations = 0;
for (let i = 0; i < timeSession.length - 1; i++) {
  const patA = timeSession[i].primaryPattern || timeSession[i].patterns[0];
  const patB = timeSession[i + 1].primaryPattern || timeSession[i + 1].patterns[0];
  if (patA && patB && patA === patB) {
    realConsecutiveViolations++;
  }
}
assert.strictEqual(realConsecutiveViolations, 0, 'Cluster session should interleave patterns without consecutive duplicates');

console.log('✓ Step 5 Passed: Interleaving logic guarantees pattern separation.\n');

// ---------------------------------------------------------------------
// 6. PATTERN MASTERY & "LEARNED" CRITERIA (doc 02 §9.2, §9.8, ME-15)
// ---------------------------------------------------------------------
console.log('--- Step 6: Testing Pattern Mastery & "Learned" Criteria (ME-15) ---');

const testPatternId = 'P1-TEST';
const testCards = [
  { key: 'GD:test:1:101', compositeKey: 'test:1:101', patterns: [testPatternId] },
  { key: 'GD:test:1:102', compositeKey: 'test:1:102', patterns: [testPatternId] },
  { key: 'GS:test:1:103', compositeKey: 'test:1:103', patterns: [testPatternId] }
];

// 6.1 Zero cards passed
const statsEmpty = {};
const mastery0 = getPatternMastery(testPatternId, statsEmpty, testCards);
assert.strictEqual(mastery0.isLearned, false);
assert.strictEqual(mastery0.score, 0.0);
assert.strictEqual(mastery0.passedCount, 0);
assert.strictEqual(isPatternLearned(testPatternId, statsEmpty, testCards), false);

// 6.2 Exactly 1 card passed (even with Mastered 1.0 status)
const statsOnePassed = {
  'GD:test:1:101': { reps: 4, interval: 25, weight: 0.75, correct: 5, incorrect: 0, status: 'mastered' },
  'GD:test:1:102': { reps: 0, interval: 0, weight: 1.0, correct: 0, incorrect: 0 },
  'GS:test:1:103': { reps: 0, interval: 0, weight: 1.0, correct: 0, incorrect: 0 }
};

const mastery1 = getPatternMastery(testPatternId, statsOnePassed, testCards);
assert.strictEqual(mastery1.passedCount, 1);
assert.strictEqual(mastery1.isLearned, false, 'Pattern must NOT count as learned with only 1 card passed');
assert.strictEqual(isPatternLearned(testPatternId, statsOnePassed, testCards), false);

// 6.3 Repeated reviews on the SAME card only
const statsOneCardManyReps = {
  'GD:test:1:101': { reps: 12, interval: 60, weight: 0.5, correct: 20, incorrect: 0, status: 'mastered' },
  'GD:test:1:102': { reps: 0, interval: 0, weight: 1.0, correct: 0, incorrect: 0 },
  'GS:test:1:103': { reps: 0, interval: 0, weight: 1.0, correct: 0, incorrect: 0 }
};
const masteryOneCardMany = getPatternMastery(testPatternId, statsOneCardManyReps, testCards);
assert.strictEqual(masteryOneCardMany.passedCount, 1, 'Multiple passes on the same card must count as 1 distinct card');
assert.strictEqual(masteryOneCardMany.isLearned, false);

// 6.4 Score capping at 0.6 when raw mean > 0.6 on only 1 passed card
const singleCardPool = [
  { key: 'GD:single:1:101', compositeKey: 'single:1:101', patterns: ['P1-SINGLE'] }
];
const statsSingleMastered = {
  'GD:single:1:101': { reps: 4, interval: 25, weight: 0.75, correct: 4, incorrect: 0, status: 'mastered' }
};
const masteryCapped = getPatternMastery('P1-SINGLE', statsSingleMastered, singleCardPool);
assert.strictEqual(masteryCapped.rawMean, 1.0);
assert.strictEqual(masteryCapped.isLearned, false);
assert.strictEqual(masteryCapped.score, 0.6, 'Mastery score MUST be capped at 0.6 when < 2 distinct cards passed');
assert.strictEqual(masteryCapped.capped, true);

// 6.5 Exactly 2 DISTINCT cards passed -> Counts as Learned!
const statsTwoPassed = {
  'GD:test:1:101': { reps: 3, interval: 14, weight: 0.8, correct: 3, incorrect: 0, status: 'review' }, // score 0.7
  'GD:test:1:102': { reps: 2, interval: 7, weight: 0.9, correct: 2, incorrect: 0, status: 'review' },  // score 0.7
  'GS:test:1:103': { reps: 0, interval: 0, weight: 1.0, correct: 0, incorrect: 0 }                     // score 0.0
};
const mastery2 = getPatternMastery(testPatternId, statsTwoPassed, testCards);
assert.strictEqual(mastery2.passedCount, 2);
assert.strictEqual(mastery2.isLearned, true, 'Pattern counts as Learned when >= 2 distinct cards passed');
assert.strictEqual(isPatternLearned(testPatternId, statsTwoPassed, testCards), true);

// 6.6 Two distinct cards passed with high scores (> 0.6) -> Uncapped!
const statsTwoMastered = {
  'GD:test:1:101': { reps: 4, interval: 25, weight: 0.75, correct: 4, incorrect: 0, status: 'mastered' }, // 1.0
  'GD:test:1:102': { reps: 4, interval: 25, weight: 0.75, correct: 4, incorrect: 0, status: 'mastered' }, // 1.0
  'GS:test:1:103': { reps: 2, interval: 7, weight: 0.9, correct: 2, incorrect: 0, status: 'review' }     // 0.7
};
const masteryUncapped = getPatternMastery(testPatternId, statsTwoMastered, testCards);
assert.strictEqual(masteryUncapped.isLearned, true);
assert.strictEqual(masteryUncapped.capped, false);
assert.strictEqual(masteryUncapped.score, 0.9); // (1.0 + 1.0 + 0.7) / 3 = 0.9
assert.ok(masteryUncapped.score > 0.6, 'Score can exceed 0.6 once >= 2 distinct cards passed');

console.log('✓ Step 6 Passed: Pattern mastery and "Learned" criterion (ME-15) strictly verified.\n');

// ---------------------------------------------------------------------
// 7. AUTO-GRADE DECISION MCQ TEST
// ---------------------------------------------------------------------
console.log('--- Step 7: Testing Decision MCQ Auto-grading (ME-6) ---');

assert.strictEqual(gradeGrammarDecision(false), 1, 'Wrong -> 1 (Again)');
assert.strictEqual(gradeGrammarDecision(true, 15000, false), 2, 'Slow (>SLOW_MS) -> 2 (Hard)');
assert.strictEqual(gradeGrammarDecision(true, 3000, true), 2, 'Used hint -> 2 (Hard)');
assert.strictEqual(gradeGrammarDecision(true, 3000, false), 3, 'Correct fast -> 3 (Good)');

console.log('✓ Step 7 Passed: MCQ auto-grading rules verified.\n');

console.log('===========================================================');
console.log('ALL VERIFICATION CHECKS PASSED (WP-9 COMPLETE)');
console.log('===========================================================');
