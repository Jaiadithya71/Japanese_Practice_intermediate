// Verifies the coverage-aware single-kanji serving dedup (user ask 2026-11-01).
// A K:<char> review card is held back only when EVERY listed on/kun reading of
// the kanji is demonstrably exercised by a recorded KWR (reading-direction)
// word card. Matching is validated against the book's explicit per-kanji ruby
// annotations - never bare substring: 押す must not cover お・さえる.
// This is serving dedup, not completion: zero stats records are read
// differently, created, or modified.
import assert from 'node:assert/strict';
import { state } from '../js/state.js';
import { getDueItemsCount, getAllDueItems, isKanjiReadingCovered } from '../js/srs.js';
import { kanjiReviewPlan } from '../js/kanji-review-options.js';

const past = Date.now() - 1000;
const rec = (extra = {}) => ({ nextDue: past, reps: 1, correct: 1, interval: 1, ...extra });

state.kanjiDB = {
  '市': { kanji: '市', lesson_number: 1, onyomi: ['シ'], kunyomi: ['いち'],
    words: [{ term_ja: '市場', reading: 'いちば', meaning_en: 'market' }, { term_ja: '市民', reading: 'しみん', meaning_en: 'citizen' }] },
  '命': { kanji: '命', lesson_number: 1, onyomi: [], kunyomi: ['いのち'],
    words: [{ term_ja: '命', reading: 'いのち', meaning_en: 'life' }] },
  '語': { kanji: '語', lesson_number: 1, onyomi: ['ゴ'], kunyomi: ['かた・る'],
    words: [{ term_ja: '日本語', reading: 'にほんご', meaning_en: 'Japanese' }, { term_ja: '物語', reading: 'ものがたり', meaning_en: 'tale' }] },
  '押': { kanji: '押', lesson_number: 2, onyomi: [], kunyomi: ['お・す', 'お・さえる'],
    words: [{ term_ja: '押す', reading: 'おす', meaning_en: 'push' }, { term_ja: '押さえる', reading: 'おさえる', meaning_en: 'hold down' }] },
  '供': { kanji: '供', lesson_number: 2, onyomi: [], kunyomi: ['とも'],
    words: [{ term_ja: '子供', reading: 'こども', meaning_en: 'child' }] }
};
state.vocabDB = {};
state.readingDB = {};
state.stats = {
  'K:市': rec({ reps: 2, correct: 2 }),
  'K:命': rec({ reps: 2, correct: 2 }),
  'K:語': rec({ reps: 2, correct: 2 }),
  'K:押': rec({ reps: 2, correct: 2 }),
  'K:供': rec({ reps: 2, correct: 2 }),
  'K:孤立': rec(),
  'KWR:市場': rec(),
  'KWR:市民': rec({ correct: 0, incorrect: 1, reps: 0 }),  // missed, still in the loop
  'KWR:日本語': rec(),
  'KWR:物語': rec(),
  'KWR:命': rec(),
  'KWR:押す': rec(),
  'KWW:押さえる': rec()  // writing direction only - NOT reading coverage evidence
};
const before = JSON.stringify(state.stats);

assert.equal(isKanjiReadingCovered('市'), true, 'いち via 市場 + シ via 市民 (missed record still trains the reading)');
assert.equal(isKanjiReadingCovered('命'), true, 'standalone word covers its own reading');
assert.equal(isKanjiReadingCovered('語'), false, 'かた・る uncovered: 物語 (がたり) is a derived noun, not the verb reading');
assert.equal(isKanjiReadingCovered('押'), false, '押す must not cover お・さえる; KWW:押さえる is not reading evidence');
assert.equal(isKanjiReadingCovered('供'), false, 'no recorded words -> retained');
assert.equal(isKanjiReadingCovered('孤立'), false, 'unknown kanji -> retained');

state.stats['KWR:押さえる'] = rec();
assert.equal(isKanjiReadingCovered('押'), true, 'a real KWR:押さえる record covers お・さえる');
delete state.stats['KWR:押さえる'];

const keys = getAllDueItems('kanji', 'all', null, { uncapped: true }).map(i => i.key);
assert(!keys.includes('K:市') && !keys.includes('K:命'), 'covered singles not double-served');
assert(keys.includes('K:語') && keys.includes('K:押') && keys.includes('K:供') && keys.includes('K:孤立'), 'uncovered/untrained/legacy singles still served');
assert(keys.includes('KWR:市場'), 'word cards unaffected');
assert.equal(getDueItemsCount('kanji'), keys.length, 'count matches items');

// One failed word never retires an inventory by itself.
delete state.stats['KWR:市民'];
assert.equal(isKanjiReadingCovered('市'), false, 'シ uncovered once 市民 record removed');
state.stats['KWR:市民'] = rec({ correct: 0, incorrect: 1, reps: 0 });
assert.equal(isKanjiReadingCovered('市'), true, 'coverage restored with the record back in the loop');

// Review plan per-lesson counts follow the same rule.
state.selectedDueKanjiLessons = new Set();
state.kanjiDueDirection = 'both';
state.kanjiDueSingle = true;
state.dueBatchSize = 'all';
const plan = kanjiReviewPlan();
assert(plan.pool.every(i => i.key !== 'K:市' && i.key !== 'K:命'), 'plan excludes covered singles');
assert(plan.pool.some(i => i.key === 'K:語' || i.key === 'K:押'), 'plan keeps uncovered singles');
assert.equal(plan.byLesson[1], 6, 'L1: 5 word cards + 1 uncovered single (語)');
assert.equal(plan.byLesson[2], 4, 'L2: 2 word cards + 2 uncovered/untrained singles (押, 供)');
state.kanjiDueSingle = false;
assert(kanjiReviewPlan().pool.every(i => i.facet !== 'K'), 'single-off still hides all K: cards');

assert.deepEqual(JSON.parse(JSON.stringify(state.stats)), JSON.parse(before), 'no stats record created or modified');
console.log('coverage-aware single-kanji dedup: validated matching, KWR-only evidence, collision-safe, zero record writes.');
