#!/usr/bin/env node
/**
 * scripts/verify_reader_engine.mjs
 * Verification test harness for WP-8 Reading Comprehension Engine.
 * 
 * Verifies:
 * 1. CPM calculation and timer target calculation (target = chars / 330 min).
 * 2. Question keyword matcher and question taxonomy categorization.
 * 3. 区切り chunky connector punctuation regex & chunk split.
 * 4. RP:<lessonId> Layer A re-read scheduling intervals (+3d, +10d, +25d, fail +2d).
 * 5. Question answer evaluation and option shuffling with correctAnswer remapping.
 * 6. Passage genre categorization (short, medium, long, info, foundation, strategy).
 * 7. Vocabulary engine integration with daily cap of 8 words (V:, KWR:, RW:).
 */

import assert from 'node:assert/strict';

// Setup minimal stubs for Node.js environment before importing UI modules
const memStore = new Map();
if (typeof globalThis.localStorage === 'undefined') {
  globalThis.localStorage = {
    getItem: (k) => memStore.get(k) ?? null,
    setItem: (k, v) => memStore.set(k, String(v)),
    removeItem: (k) => memStore.delete(k),
    clear: () => memStore.clear()
  };
}
if (typeof globalThis.window === 'undefined') {
  globalThis.window = globalThis;
}
if (typeof globalThis.document === 'undefined') {
  globalThis.document = {
    getElementById: () => null,
    querySelector: () => null,
    querySelectorAll: () => [],
    head: { appendChild: () => {} },
    createElement: () => ({ setAttribute: () => {}, appendChild: () => {} })
  };
}

// Import reading types engine
import {
  PASSAGE_GENRES,
  GENRE_METADATA,
  categorizePassage,
  countPassageChars,
  DEFAULT_READING_CPM,
  calculateTargetMinutes,
  calculateTargetSeconds,
  calculateCpm,
  formatTime,
  QUESTION_TYPES,
  QUESTION_TYPE_RULES,
  detectQuestionType,
  getQuestionType,
  CHUNK_CONNECTORS,
  CHUNK_CONNECTOR_REGEX,
  CHUNK_CONNECTOR_GLOBAL_REGEX,
  CHUNK_SPLIT_REGEX,
  insertChunkDividers,
  splitIntoChunks,
  isSecondPassPassed,
  evaluateSecondPass,
  REREAD_INTERVALS_DAYS,
  REREAD_FAIL_REPEAT_DAYS,
  calculateRereadSchedule,
  shuffleQuestionOptions,
  evaluateQuestionAnswer
} from '../js/reading-types.js';

// Import reader module
import {
  addWordToMyWords
} from '../js/reader.js';

import { state } from '../js/state.js';

let totalTests = 0;
let passedTests = 0;

function runTest(name, fn) {
  totalTests++;
  try {
    fn();
    passedTests++;
    console.log(`  ✓ ${name}`);
  } catch (err) {
    console.error(`  ✗ FAIL: ${name}`);
    console.error(err);
    process.exitCode = 1;
  }
}

console.log('=====================================================');
console.log(' RUNNING READING COMPREHENSION ENGINE VERIFICATION');
console.log('=====================================================');

// -----------------------------------------------------------------
// 1. CPM & TIMER TARGET CALCULATION
// -----------------------------------------------------------------
console.log('\n[Suite 1] CPM & Reading Speed Target Calculations');

runTest('Character counting across string, array, and passage object', () => {
  const str = '日本語の 勉強を\nしています。';
  assert.equal(countPassageChars(str), 13, 'Excludes whitespace and newlines');

  const sentences = [
    { text_ja: 'これは短文です。' }, // 8
    { text_ja: '二つ目の文です。' }   // 8
  ];
  assert.equal(countPassageChars(sentences), 16);

  const passageObj = { sentences };
  assert.equal(countPassageChars(passageObj), 16);
});

runTest('Target minutes calculation (target = chars / 330 min)', () => {
  assert.equal(DEFAULT_READING_CPM, 330);
  assert.equal(calculateTargetMinutes(330, 330), 1.0);
  assert.equal(calculateTargetMinutes(660, 330), 2.0);
  assert.equal(calculateTargetMinutes(495, 330), 1.5);
  assert.equal(calculateTargetMinutes(0, 330), 0);
  assert.equal(calculateTargetMinutes(-10, 330), 0);
});

runTest('Target seconds calculation', () => {
  assert.equal(calculateTargetSeconds(330, 330), 60);
  assert.equal(calculateTargetSeconds(660, 330), 120);
  assert.equal(calculateTargetSeconds(165, 330), 30);
  assert.equal(calculateTargetSeconds(0, 330), 0);
});

runTest('CPM calculation: (chars / elapsedSeconds) * 60', () => {
  // 330 chars in 60s -> 330 CPM
  assert.equal(calculateCpm(330, 60), 330);
  // 330 chars in 30s -> 660 CPM (faster)
  assert.equal(calculateCpm(330, 30), 660);
  // 330 chars in 120s -> 165 CPM (slower)
  assert.equal(calculateCpm(330, 120), 165);
  // 450 chars in 90s -> 300 CPM
  assert.equal(calculateCpm(450, 90), 300);
  // Edge cases
  assert.equal(calculateCpm(0, 60), 0);
  assert.equal(calculateCpm(100, 0), 0);
  assert.equal(calculateCpm(100, -5), 0);
});

runTest('formatTime formatting mm:ss', () => {
  assert.equal(formatTime(0), '0:00');
  assert.equal(formatTime(45), '0:45');
  assert.equal(formatTime(60), '1:00');
  assert.equal(formatTime(125), '2:05');
  assert.equal(formatTime(3600), '60:00');
});

// -----------------------------------------------------------------
// 2. QUESTION TAXONOMY & KEYWORD MATCHER
// -----------------------------------------------------------------
console.log('\n[Suite 2] Question Type Keyword Categorization');

runTest('Matches "筆者の考え" -> author_opinion', () => {
  const q1 = detectQuestionType('この文章で筆者の考えとして最も適切なものはどれか。');
  assert.equal(q1.type, QUESTION_TYPES.AUTHOR_OPINION);
  assert.equal(q1.label_ja, '筆者の考え');

  const q2 = detectQuestionType('筆者が言いたいことは何か。');
  assert.equal(q2.type, QUESTION_TYPES.AUTHOR_OPINION);
});

runTest('Matches "どういう意味" -> meaning', () => {
  const q1 = detectQuestionType('下線部「それ」はどういう意味か。');
  assert.equal(q1.type, QUESTION_TYPES.MEANING);
  assert.equal(q1.label_ja, 'どういう意味');

  const q2 = detectQuestionType('下線部は何を指しているか。');
  assert.equal(q2.type, QUESTION_TYPES.MEANING);
});

runTest('Matches "なぜ" -> reason', () => {
  const q1 = detectQuestionType('筆者はなぜそのように考えたのか。');
  assert.equal(q1.type, QUESTION_TYPES.REASON);
  assert.equal(q1.label_ja, 'なぜ');

  const q2 = detectQuestionType('どうして筆者はそう言ったのか。');
  assert.equal(q2.type, QUESTION_TYPES.REASON);
});

runTest('Matches "内容と合っている" -> content_match', () => {
  const q1 = detectQuestionType('本文の内容と合っているものはどれか。');
  assert.equal(q1.type, QUESTION_TYPES.CONTENT_MATCH);
  assert.equal(q1.label_ja, '内容と合っている');

  const q2 = detectQuestionType('本文の内容について正しく述べているものはどれか。');
  assert.equal(q2.type, QUESTION_TYPES.CONTENT_MATCH);
});

runTest('Matches "〜について" -> topic_detail', () => {
  const q1 = detectQuestionType('A社の新製品について正しいものはどれか。');
  assert.equal(q1.type, QUESTION_TYPES.TOPIC_DETAIL);
  assert.equal(q1.label_ja, '〜について');
});

runTest('Unknown fallback on non-matching questions', () => {
  const q = detectQuestionType('次の文章を読んで答えなさい。');
  assert.equal(q.type, QUESTION_TYPES.UNKNOWN);
  assert.equal(q.label_ja, 'その他');
});

runTest('getQuestionType extracts type from question objects', () => {
  const qObj = {
    id: 'l01_q1',
    question_ja: '筆者の考えに合っているものはどれか。'
  };
  assert.equal(getQuestionType(qObj).type, QUESTION_TYPES.AUTHOR_OPINION);
});

// -----------------------------------------------------------------
// 3. 区切り CHUNKY CONNECTOR PUNCTUATION REGEX
// -----------------------------------------------------------------
console.log('\n[Suite 3] 区切り Chunk Connectors & Division Engine');

runTest('Contains all connectors from Foundation lesson (が、ので、から、と、ば、たら、なら、ても、のに、、)', () => {
  const expected = ['ので', 'から', 'たら', 'なら', 'ても', 'のに', 'が', 'と', 'ば', '、'];
  for (const c of expected) {
    assert.ok(CHUNK_CONNECTORS.includes(c), `Missing connector ${c}`);
    assert.ok(CHUNK_CONNECTOR_REGEX.test(c), `Regex does not match connector ${c}`);
  }
});

runTest('insertChunkDividers inserts slash ／ after connectors and punctuation', () => {
  const text = '本を読んだが、面白かったので、友達に勧めた。';
  const divided = insertChunkDividers(text);
  // Should produce "本を読んだが、／面白かったので、／友達に勧めた。"
  assert.ok(divided.includes('が、／'), 'Divider placed after が、');
  assert.ok(divided.includes('ので、／'), 'Divider placed after ので、');
  assert.equal(divided, '本を読んだが、／面白かったので、／友達に勧めた。');
});

runTest('insertChunkDividers handles standalone connectors without commas', () => {
  const text = '雨が降れば中止になる。';
  const divided = insertChunkDividers(text);
  // 'が' and 'ば' get dividers
  assert.ok(divided.includes('が／'), 'Divider placed after が');
  assert.ok(divided.includes('ば／'), 'Divider placed after ば');
});

runTest('splitIntoChunks splits text cleanly at chunk boundaries', () => {
  const text = '朝起きたら、天気が良かったので、散歩に行った。';
  const chunks = splitIntoChunks(text);
  assert.ok(Array.isArray(chunks));
  assert.equal(chunks.length, 4);
  assert.equal(chunks[0], '朝起きたら、');
  assert.equal(chunks[1], '天気が');
  assert.equal(chunks[2], '良かったので、');
  assert.equal(chunks[3], '散歩に行った。');
});

// -----------------------------------------------------------------
// 4. SECOND-PASS CRITERIA & LAYER A RE-READ SCHEDULING (+3d, +10d, +25d)
// -----------------------------------------------------------------
console.log('\n[Suite 4] Second-Pass Criteria & Layer A Re-read Scheduler');

runTest('isSecondPassPassed pass criteria: accuracy >= 0.8 and elapsed <= 1.3 * target', () => {
  const target = 100; // seconds

  // Passed: acc = 0.80, elapsed = 100 (<= 130)
  assert.equal(isSecondPassPassed(0.80, 100, target), true);
  // Passed: acc = 1.0, elapsed = 130 (<= 130)
  assert.equal(isSecondPassPassed(1.0, 130, target), true);

  // Failed: accuracy < 0.8
  assert.equal(isSecondPassPassed(0.75, 90, target), false);

  // Failed: elapsed > 1.3 * target (131 > 130)
  assert.equal(isSecondPassPassed(1.0, 131, target), false);

  // Failed: both fail
  assert.equal(isSecondPassPassed(0.5, 150, target), false);
});

runTest('evaluateSecondPass provides detailed breakdown', () => {
  const res = evaluateSecondPass({ accuracy: 0.85, elapsedSeconds: 110, targetSeconds: 100 });
  assert.equal(res.passed, true);
  assert.equal(res.meetsAccuracy, true);
  assert.equal(res.meetsTime, true);
  assert.equal(res.maxAllowedSeconds, 130);
});

runTest('Initial read schedules second pass at +3 days (step 0)', () => {
  const now = 1700000000000;
  const sched = calculateRereadSchedule({ reads: 0, currentStep: 0, passed: false, now });
  assert.equal(sched.intervalDays, 3);
  assert.equal(sched.nextStep, 0);
  assert.equal(sched.nextDue, now + 3 * 86400000);
  assert.equal(sched.mastered, false);
});

runTest('Passing second pass 1 advances to +10 days (step 0 -> 1)', () => {
  const now = 1700000000000;
  const sched = calculateRereadSchedule({ reads: 1, currentStep: 0, passed: true, now });
  assert.equal(sched.intervalDays, 10);
  assert.equal(sched.nextStep, 1);
  assert.equal(sched.nextDue, now + 10 * 86400000);
  assert.equal(sched.mastered, false);
});

runTest('Passing second pass 2 advances to +25 days and sets mastered (step 1 -> 2)', () => {
  const now = 1700000000000;
  const sched = calculateRereadSchedule({ reads: 2, currentStep: 1, passed: true, now });
  assert.equal(sched.intervalDays, 25);
  assert.equal(sched.nextStep, 2);
  assert.equal(sched.nextDue, now + 25 * 86400000);
  assert.equal(sched.mastered, true, 'Mastered after 2 successful second passes');
});

runTest('Failing second pass repeats same step in 2 days (+2d)', () => {
  const now = 1700000000000;
  // Failed at step 1
  const sched = calculateRereadSchedule({ reads: 2, currentStep: 1, passed: false, now });
  assert.equal(sched.intervalDays, 2, 'Repeats in 2 days on failure');
  assert.equal(sched.nextStep, 1, 'Does not advance step');
  assert.equal(sched.nextDue, now + 2 * 86400000);
  assert.equal(sched.mastered, false);
});

runTest('calculateRereadSchedule respects snapFn alignment', () => {
  const now = 1700000000000;
  const mockSnap = (ms) => ms + 1000;
  const sched = calculateRereadSchedule({ reads: 0, currentStep: 0, passed: false, now, snapFn: mockSnap });
  assert.equal(sched.nextDue, now + 3 * 86400000 + 1000);
});

// -----------------------------------------------------------------
// 5. QUESTION ANSWER EVALUATION & OPTION SHUFFLING
// -----------------------------------------------------------------
console.log('\n[Suite 5] Question Evaluation & Option Shuffling');

runTest('evaluateQuestionAnswer correctly evaluates 1-based choices', () => {
  const q = { id: 'q1', correctAnswer: 3 };
  assert.equal(evaluateQuestionAnswer(q, 3).isCorrect, true);
  assert.equal(evaluateQuestionAnswer(q, '3').isCorrect, true);
  assert.equal(evaluateQuestionAnswer(q, 1).isCorrect, false);
  assert.equal(evaluateQuestionAnswer(q, 2).isCorrect, false);
});

runTest('shuffleQuestionOptions remaps correctAnswer and keeps options_en in sync', () => {
  const q = {
    id: 'q_test',
    question_ja: 'テスト問題',
    options: ['選択肢A', '選択肢B', '選択肢C', '選択肢D'],
    options_en: ['Opt A', 'Opt B', 'Opt C', 'Opt D'],
    correctAnswer: 2 // '選択肢B'
  };

  // Run 20 iterations of shuffle to test multiple permutations
  for (let i = 0; i < 20; i++) {
    const shuffled = shuffleQuestionOptions(q);

    // Option length preserved
    assert.equal(shuffled.options.length, 4);
    assert.equal(shuffled.options_en.length, 4);

    // Set of options is unchanged
    assert.deepEqual(new Set(shuffled.options), new Set(q.options));

    // The new correctAnswer (1-based) points to '選択肢B'
    const newCorrectIdx = shuffled.correctAnswer - 1;
    assert.equal(shuffled.options[newCorrectIdx], '選択肢B', 'Correct answer text must remain 選択肢B');
    assert.equal(shuffled.options_en[newCorrectIdx], 'Opt B', 'Correct answer English text must remain Opt B');

    // evaluateQuestionAnswer with shuffled.correctAnswer passes
    assert.equal(evaluateQuestionAnswer(shuffled, shuffled.correctAnswer).isCorrect, true);

    // Any other choice fails
    const wrongChoice = shuffled.correctAnswer === 1 ? 2 : 1;
    assert.equal(evaluateQuestionAnswer(shuffled, wrongChoice).isCorrect, false);
  }
});

// -----------------------------------------------------------------
// 6. GENRE CATEGORIZATION
// -----------------------------------------------------------------
console.log('\n[Suite 6] Passage Genre Categorization');

runTest('categorizePassage categorizes short, medium, long, info, foundation', () => {
  assert.equal(categorizePassage({ category: 'real_short' }), PASSAGE_GENRES.SHORT);
  assert.equal(categorizePassage({ genre: '短文' }), PASSAGE_GENRES.SHORT);
  assert.equal(categorizePassage({ problemNumber: 15 }), PASSAGE_GENRES.SHORT);

  assert.equal(categorizePassage({ category: 'real_medium' }), PASSAGE_GENRES.MEDIUM);
  assert.equal(categorizePassage({ genre: '中文' }), PASSAGE_GENRES.MEDIUM);
  assert.equal(categorizePassage({ problemNumber: 35 }), PASSAGE_GENRES.MEDIUM);

  assert.equal(categorizePassage({ category: 'real_long' }), PASSAGE_GENRES.LONG);
  assert.equal(categorizePassage({ genre: '長文' }), PASSAGE_GENRES.LONG);
  assert.equal(categorizePassage({ problemNumber: 55 }), PASSAGE_GENRES.LONG);

  assert.equal(categorizePassage({ category: 'info' }), PASSAGE_GENRES.INFO);
  assert.equal(categorizePassage({ genre: '情報検索' }), PASSAGE_GENRES.INFO);
  assert.equal(categorizePassage({ problemNumber: 63 }), PASSAGE_GENRES.INFO);

  assert.equal(categorizePassage({ category: 'foundation' }), PASSAGE_GENRES.FOUNDATION);
  assert.equal(categorizePassage({ category: 'strategy' }), PASSAGE_GENRES.STRATEGY);
});

// -----------------------------------------------------------------
// 7. VOCABULARY ENGINE INTEGRATION & DAILY CAP (RD-10)
// -----------------------------------------------------------------
console.log('\n[Suite 7] Vocabulary Engine Integration & 8-Word Daily Cap');

runTest('addWordToMyWords creates right key types and enforces daily cap of 8', () => {
  // Clear test storage
  localStorage.clear();
  state.stats = {};
  state.vocabDB = {
    ch1: [{ id: 'w101', term_ja: '約束', meaning: 'promise' }]
  };
  state.idx = {
    words: {
      '発達': { reading: 'はったつ', meaning: 'development' }
    }
  };

  // 1. Matches vocabDB -> V:w101
  const res1 = addWordToMyWords({ term: '約束', reading: 'やくそく', meaning: 'promise' });
  assert.equal(res1.success, true);
  assert.equal(res1.key, 'V:w101');
  assert.ok(state.stats['V:w101']);

  // 2. Matches state.idx.words -> KWR:発達 and KWM:発達
  const res2 = addWordToMyWords({ term: '発達', reading: 'はったつ', meaning: 'development' });
  assert.equal(res2.success, true);
  assert.equal(res2.key, 'KWR:発達');
  assert.ok(state.stats['KWR:発達']);
  assert.ok(state.stats['KWM:発達']);

  // 3. Custom term -> RW:<term>
  const res3 = addWordToMyWords({ term: '希少', reading: 'きしょう', meaning: 'scarce' });
  assert.equal(res3.success, true);
  assert.equal(res3.key, 'RW:希少');
  assert.ok(state.stats['RW:希少']);

  // Add 5 more words to reach cap of 8 (currently 3 added)
  for (let i = 4; i <= 8; i++) {
    const res = addWordToMyWords({ term: `単語_${i}`, reading: `たんご${i}`, meaning: `Word ${i}` });
    assert.equal(res.success, true, `Word ${i} should be successfully added`);
  }

  // 9th word should hit cap
  const res9 = addWordToMyWords({ term: '超過単語', reading: 'ちょうか', meaning: 'excess word' });
  assert.equal(res9.success, false, 'Word 9 must not be added to active deck today');
  assert.equal(res9.capped, true, 'Word 9 must be flagged as capped');
  assert.ok(res9.message.includes('Daily limit of 8 words reached'));
});

// -----------------------------------------------------------------
// SUMMARY
// -----------------------------------------------------------------
console.log('\n=====================================================');
console.log(` SUMMARY: ${passedTests} / ${totalTests} TESTS PASSED`);
console.log('=====================================================');

if (passedTests === totalTests) {
  console.log('All Reading Engine verification checks passed successfully!\n');
  process.exit(0);
} else {
  console.error(`Failed ${totalTests - passedTests} tests.`);
  process.exit(1);
}
