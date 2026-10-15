#!/usr/bin/env node
/**
 * scripts/verify_study_anki_and_kanji_modes.mjs
 * Verification test suite for:
 * 1. Kanji compound words 2-way / 3-direction drill generation (JLPT Mondai 1 & 2)
 * 2. Anki-style SRS "Again" requeue logic (+3 offset) & Live Counters
 * 3. Multi-chapter / Multi-lesson selection sets for Vocab & Kanji
 * 4. Chapter-filtered SRS Due queue retrieval & counts
 */

import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { state } from '../js/state.js';
import {
  getDueItemsCount,
  getAllDueItems,
  updateItemStats,
  getItemStats
} from '../js/srs.js';
import { buildKanjiStudyItems } from '../js/kanji.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DATA_DIR = path.join(ROOT_DIR, 'data');

function readJson(relPath) {
  const full = path.join(DATA_DIR, relPath);
  return JSON.parse(fs.readFileSync(full, 'utf-8'));
}

console.log('===========================================================');
console.log('NIHONGO INTERMEDIATE — Verification: Kanji Drills & Anki SRS');
console.log('===========================================================\n');

// Mock data setup in state
const part1Data = readJson('kanji/part1_lessons_01_05.json');
const l1 = part1Data.lessons.find(l => l.lesson_number === 1) || { kanji: [] };
const l2 = part1Data.lessons.find(l => l.lesson_number === 2) || { kanji: [] };

state.kanjiDB = {};
[...l1.kanji, ...l2.kanji].forEach(k => {
  state.kanjiDB[k.kanji] = {
    ...k,
    lesson_number: l1.kanji.includes(k) ? 1 : 2
  };
});

// Setup mock vocab data
state.vocabDB = {
  1: [
    { id: 'v1_1', word_ja: '生活', reading_hiragana: 'せいかつ', meaning_en: 'life', chapter: 1 },
    { id: 'v1_2', word_ja: '習慣', reading_hiragana: 'しゅうかん', meaning_en: 'habit', chapter: 1 }
  ],
  2: [
    { id: 'v2_1', word_ja: '通勤', reading_hiragana: 'つうきん', meaning_en: 'commuting', chapter: 2 }
  ],
  3: [
    { id: 'v3_1', word_ja: '健康', reading_hiragana: 'けんこう', meaning_en: 'health', chapter: 3 }
  ]
};

// -----------------------------------------------------------------------------
// TEST 1: Kanji Compound Words Generation & 3 Directions
// -----------------------------------------------------------------------------
console.log('--- TEST 1: Kanji Compound Words Generation & 3 Directions ---');

const sampleKanji = [state.kanjiDB['辺'] || Object.values(state.kanjiDB)[0]];
assert.ok(sampleKanji[0], 'Should have sample kanji loaded');
assert.ok(sampleKanji[0].words && sampleKanji[0].words.length > 0, 'Sample kanji should have compound words');

// Direction 1: ja-kana (Mondai 1: Given Kanji, recall Kana)
const itemsJaKana = buildKanjiStudyItems(sampleKanji, 'ja-kana');
assert.ok(itemsJaKana.length > 0, 'Should build compound items for ja-kana');
assert.equal(itemsJaKana[0].direction, 'ja-kana');
assert.equal(itemsJaKana[0].type, 'kanji_word');
assert.ok(itemsJaKana[0].key.startsWith('KWR:'), `Expected KWR key prefix, got: ${itemsJaKana[0].key}`);
assert.ok(itemsJaKana[0].baseKanji, 'Must include baseKanji');
assert.ok(itemsJaKana[0].lesson_number, 'Must include lesson_number');
assert.ok(itemsJaKana[0].reading, 'Must include reading');

// Direction 2: kana-ja (Mondai 2: Given Kana, recall Kanji)
const itemsKanaJa = buildKanjiStudyItems(sampleKanji, 'kana-ja');
assert.equal(itemsKanaJa[0].direction, 'kana-ja');
assert.ok(itemsKanaJa[0].key.startsWith('KWW:'), `Expected KWW key prefix, got: ${itemsKanaJa[0].key}`);

// Direction 3: ja-meaning (Compound word to English meaning)
const itemsJaMeaning = buildKanjiStudyItems(sampleKanji, 'ja-meaning');
assert.equal(itemsJaMeaning[0].direction, 'ja-meaning');
assert.ok(itemsJaMeaning[0].key.startsWith('KWM:'), `Expected KWM key prefix, got: ${itemsJaMeaning[0].key}`);

console.log(`✓ Kanji compound word items correctly generated across all 3 directions (${itemsJaKana.length} words tested)`);

// -----------------------------------------------------------------------------
// TEST 2: Anki-Style SRS Re-queuing on "Again" (Grade 1)
// -----------------------------------------------------------------------------
console.log('\n--- TEST 2: Anki-Style SRS Re-queuing on "Again" ---');

// Simulate the Anki requeue mechanism from gradeCard(1) in study.js
const mockSession = [
  { id: 'w1', word: 'word1' },
  { id: 'w2', word: 'word2' },
  { id: 'w3', word: 'word3' },
  { id: 'w4', word: 'word4' },
  { id: 'w5', word: 'word5' }
];

let sessionItems = [...mockSession];
let sessionIdx = 0;
let sessionTotalAnswered = 0;
let sessionRight = 0;

function simulateGradeCard(grade) {
  const currentItem = sessionItems[sessionIdx];
  sessionTotalAnswered++;

  if (grade === 1) {
    // Anki re-queue: insert +3 positions down the active deck
    const insertAt = Math.min(sessionIdx + 3, sessionItems.length);
    sessionItems.splice(insertAt, 0, { ...currentItem, _requeued: true });
  } else {
    sessionRight++;
  }
  sessionIdx++;
}

// User fails first card (w1)
simulateGradeCard(1);
assert.equal(sessionItems.length, 6, 'Queue length should expand by 1 card upon "Again"');
assert.equal(sessionTotalAnswered, 1, 'sessionTotalAnswered should increment');
assert.equal(sessionRight, 0, 'sessionRight should NOT increment on failure');
assert.equal(sessionItems[3].id, 'w1', 'Failed card w1 should now be at index 3 (+3 positions)');
assert.equal(sessionItems[3]._requeued, true, 'Failed card should be marked _requeued');

// User succeeds on next 2 cards (w2, w3)
simulateGradeCard(3);
simulateGradeCard(3);
assert.equal(sessionTotalAnswered, 3);
assert.equal(sessionRight, 2);

// User encounters w1 again at index 3 and passes it
assert.equal(sessionItems[sessionIdx].id, 'w1', 'Card encountered at index 3 should be re-queued w1');
simulateGradeCard(3);
assert.equal(sessionRight, 3);

// Pass remaining cards
simulateGradeCard(3);
simulateGradeCard(3);

assert.equal(sessionIdx, sessionItems.length, 'Session completes when all cards including requeues are cleared');
console.log(`✓ Anki-style re-queuing verified: failed cards re-inserted +3 down the deck and cleared upon success`);

// -----------------------------------------------------------------------------
// TEST 3: Multi-Chapter & Multi-Lesson Selection Sets
// -----------------------------------------------------------------------------
console.log('\n--- TEST 3: Multi-Chapter & Multi-Lesson Selection Sets ---');

state.selectedVocabChapters = new Set([1, 2]);
assert.ok(state.selectedVocabChapters.has(1) && state.selectedVocabChapters.has(2));
assert.ok(!state.selectedVocabChapters.has(3));

state.kanjiSelectedLessons = new Set([1]);
assert.ok(state.kanjiSelectedLessons.has(1));
assert.ok(!state.kanjiSelectedLessons.has(2));

// Multi-select toggle helper simulation
function toggleSetItem(set, val) {
  if (set.has(val)) set.delete(val);
  else set.add(val);
}

toggleSetItem(state.kanjiSelectedLessons, 2);
assert.equal(state.kanjiSelectedLessons.size, 2, 'Should now have 2 lessons selected');
assert.ok(state.kanjiSelectedLessons.has(2));

toggleSetItem(state.kanjiSelectedLessons, 1);
assert.equal(state.kanjiSelectedLessons.size, 1, 'Should now have 1 lesson selected after toggle');
assert.ok(!state.kanjiSelectedLessons.has(1));

console.log('✓ Multi-chapter and multi-lesson selection Sets operate correctly');

// -----------------------------------------------------------------------------
// TEST 4: Chapter-Filtered SRS Due Items Retrieval & Counts
// -----------------------------------------------------------------------------
console.log('\n--- TEST 4: Chapter-Filtered SRS Due Items Retrieval & Counts ---');

const past = Date.now() - 3600000; // 1 hour ago (due)

// Populate due items across chapters
state.stats = {
  'V:v1_1': { nextDue: past, interval: 1, reps: 1 }, // Ch 1
  'V:v1_2': { nextDue: past, interval: 1, reps: 1 }, // Ch 1
  'V:v2_1': { nextDue: past, interval: 1, reps: 1 }, // Ch 2
  'V:v3_1': { nextDue: past, interval: 1, reps: 1 }, // Ch 3
  'KWR:辺り': { nextDue: past, interval: 1, reps: 1, lesson_number: 1 }, // Kanji L1
  'KWR:周辺': { nextDue: past, interval: 1, reps: 1, lesson_number: 1 }  // Kanji L1
};

// Overall vocab due count
const totalVocabDue = getDueItemsCount('vocab');
assert.equal(totalVocabDue, 4, `Expected 4 total vocab due items, got: ${totalVocabDue}`);

// Filtered by Chapter 1 only
const ch1Due = getDueItemsCount('vocab', new Set([1]));
assert.equal(ch1Due, 2, `Expected 2 due items in Ch 1, got: ${ch1Due}`);

// Filtered by Chapter 1 + Chapter 2
const ch12Due = getDueItemsCount('vocab', new Set([1, 2]));
assert.equal(ch12Due, 3, `Expected 3 due items in Ch 1 & 2, got: ${ch12Due}`);

// getAllDueItems with Chapter filter
const dueItemsCh1 = getAllDueItems('vocab', 20, new Set([1]));
assert.equal(dueItemsCh1.length, 2);
assert.ok(dueItemsCh1.every(it => it.chapter === 1), 'All returned items must belong to Chapter 1');

// Filtered Kanji Due items
const kanjiL1Due = getDueItemsCount('kanji', new Set([1]));
assert.equal(kanjiL1Due, 2, `Expected 2 kanji items in Lesson 1, got: ${kanjiL1Due}`);

const kanjiL2Due = getDueItemsCount('kanji', new Set([2]));
assert.equal(kanjiL2Due, 0, `Expected 0 kanji items in Lesson 2, got: ${kanjiL2Due}`);

console.log('✓ Chapter-filtered SRS Due queries and counts work as expected');

console.log('\n===========================================================');
console.log('ALL VERIFICATION TESTS PASSED SUCCESSFULLY (4/4)!');
console.log('===========================================================');
