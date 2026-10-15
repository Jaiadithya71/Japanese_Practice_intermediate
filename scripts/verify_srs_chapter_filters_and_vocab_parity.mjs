import assert from 'node:assert';
import { state } from '../js/state.js';
import { getDueItemsCount, resolveItemForKey, getPillarFromKey } from '../js/srs.js';
import { N3BookPlatform } from '../js/book-platform.js';

console.log('===========================================================');
console.log('Verification: SRS Chapter Filters & Elementary App Parity');
console.log('===========================================================');

// Mock DOM elements
const elements = {};
global.document = {
  getElementById: (id) => {
    if (!elements[id]) {
      elements[id] = {
        innerHTML: '',
        style: {},
        classList: {
          add: () => {},
          remove: () => {},
          toggle: () => {},
          contains: () => false
        },
        querySelectorAll: () => []
      };
    }
    return elements[id];
  }
};
global.window = {
  N3BookPlatform,
  startDueReview: (pillar, filter) => {
    state._lastReviewPillar = pillar;
    state._lastReviewFilter = filter;
  }
};

// 1. Setup mock vocab and kanji DB
state.vocabDB = {
  '01': [{ id: 'v01-001', chapter: '01', word_ja: '約束', reading_hiragana: 'やくそく', meaning_en: 'promise' }],
  '02': [{ id: 'v02-001', chapter: '02', word_ja: '家族', reading_hiragana: 'かぞく', meaning_en: 'family' }],
  '03': [{ id: 'v03-001', chapter: '03', word_ja: '友達', reading_hiragana: 'ともだち', meaning_en: 'friend' }]
};

state.chapterMetadata = {
  '01': { chapter: '01', topic_ja: '人間関係1', topic_en: 'Relationships 1' },
  '02': { chapter: '02', topic_ja: '人間関係2', topic_en: 'Relationships 2' },
  '03': { chapter: '03', topic_ja: '生活1', topic_en: 'Life 1' }
};

state.kanjiDB = {
  '政': { kanji: '政', lesson_number: 1, words: [{ term: '政治', reading: 'せいじ', meaning_en: 'politics' }] },
  '治': { kanji: '治', lesson_number: 1, words: [{ term: '政治', reading: 'せいじ', meaning_en: 'politics' }] },
  '経': { kanji: '経', lesson_number: 2, words: [{ term: '経済', reading: 'けいざい', meaning_en: 'economy' }] }
};

const past = Date.now() - 10000;
state.stats = {
  'V:v01-001': { nextDue: past, reps: 1, interval: 1 },
  'V:v02-001': { nextDue: past, reps: 1, interval: 1 },
  'K:政': { nextDue: past, reps: 1, interval: 1 },
  'KWR:経済': { nextDue: past, reps: 1, interval: 1 }
};

// --- TEST 1: Vocab SRS Pane Chapter Filter Grid Rendering ---
console.log('\n--- TEST 1: Vocab SRS Chapter Filter Grid ---');
N3BookPlatform.toggleAllVocabDueChapters();
const vocabContainer = document.getElementById('vocab-srs-container');
assert(vocabContainer.innerHTML.includes('Filter by Chapter:'), 'Should render chapter filter header');
assert(vocabContainer.innerHTML.includes('All'), 'Should include All chip');
assert(vocabContainer.innerHTML.includes('T01'), 'Should include T01 chip');
assert(vocabContainer.innerHTML.includes('T02'), 'Should include T02 chip');
assert(!vocabContainer.innerHTML.includes('T03'), 'T03 has 0 due items and should not be in the filter grid');
console.log('✓ Vocab SRS pane correctly renders interactive filter grid for due chapters only');

// --- TEST 2: Vocab Due Chapter Single & Multi Toggle ---
console.log('\n--- TEST 2: Vocab Due Chapter Toggle ---');
N3BookPlatform.toggleVocabDueChapter('01');
assert(state.selectedDueVocabChapters.has('01'), 'Chapter 01 should be selected');
assert(state.selectedDueVocabChapters.size === 1, 'Only chapter 01 should be selected');
assert(vocabContainer.innerHTML.includes('1 selected'), 'Header should show 1 selected');

// Test launching filtered review
N3BookPlatform.startPillarSRS('vocab');
assert.strictEqual(state._lastReviewPillar, 'vocab');
assert(state._lastReviewFilter.has('01'), 'Should pass selected chapter set to startDueReview');
console.log('✓ Vocab due chapter toggle correctly scopes flashcard session to selected chapter');

// Reset to All
N3BookPlatform.toggleAllVocabDueChapters();
assert.strictEqual(state.selectedDueVocabChapters.size, 0, 'Selection should be cleared on All');
N3BookPlatform.startPillarSRS('vocab');
assert.strictEqual(state._lastReviewFilter, null, 'No filter when All is selected');
console.log('✓ All chip clears filter and launches entire deck');

// --- TEST 3: Kanji SRS Due Lesson Filter Grid & Launch ---
console.log('\n--- TEST 3: Kanji SRS Due Lesson Filter Grid ---');
N3BookPlatform.toggleAllKanjiDueLessons();
const kanjiContainer = document.getElementById('kanji-srs-container');
assert(kanjiContainer.innerHTML.includes('Filter by Lesson:'), 'Should render lesson filter header');
assert(kanjiContainer.innerHTML.includes('L01'), 'Should include L01 chip');
assert(kanjiContainer.innerHTML.includes('L02'), 'Should include L02 chip');

N3BookPlatform.toggleKanjiDueLesson(2);
assert(state.selectedDueKanjiLessons.has(2), 'Lesson 2 should be selected');
N3BookPlatform.startPillarSRS('kanji');
assert.strictEqual(state._lastReviewPillar, 'kanji');
assert(state._lastReviewFilter.has(2), 'Should pass lesson 2 filter to startDueReview');
console.log('✓ Kanji due lesson filter grid renders and filters properly');

console.log('\n===========================================================');
console.log('ALL SRS CHAPTER FILTER & PARITY TESTS PASSED (3/3)!');
console.log('===========================================================');
