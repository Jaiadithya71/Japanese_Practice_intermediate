/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_class_curriculum.mjs
   Verification Test Harness for Class Track Curriculum
   Validates independent pillar progression & multi-speed class pacing
   ======================================================= */

import assert from 'assert';
import {
  DEFAULT_CLASS_PROGRESS,
  CLASS_STORAGE_KEY,
  loadClassProgress,
  saveClassProgress,
  setPillarLesson,
  stepPillarLesson,
  adjustReadingSpan,
  getActiveLessonPackage,
  buildClassCombinedTest
} from '../js/class-curriculum.js';
import { state } from '../js/state.js';

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
console.log('Running Class Track & Multi-Speed Curriculum Verification');
console.log('========================================================\n');

// Mock localStorage in Node environment if missing
if (typeof globalThis.localStorage === 'undefined') {
  const store = new Map();
  globalThis.localStorage = {
    getItem: (key) => store.get(key) || null,
    setItem: (key, val) => store.set(key, String(val)),
    removeItem: (key) => store.delete(key),
    clear: () => store.clear()
  };
}

// -----------------------------------------------------------------
// 1. Storage & Default Progression
// -----------------------------------------------------------------
console.log('[1/4] Testing default progress and state initialization...');

it('Loads default progress on fresh state', () => {
  localStorage.clear();
  const prog = loadClassProgress();
  assert.strictEqual(prog.vocab, 1, 'Default vocab should be 1');
  assert.strictEqual(prog.kanji, 1, 'Default kanji should be 1');
  assert.strictEqual(prog.grammar, 1, 'Default grammar should be 1');
  assert.strictEqual(prog.readingStart, 1, 'Default readingStart should be 1');
  assert.strictEqual(prog.readingEnd, 1, 'Default readingEnd should be 1');
});

it('Saves and retrieves progress correctly from storage', () => {
  const custom = {
    vocab: 5,
    kanji: 3,
    grammar: 2,
    readingStart: 4,
    readingEnd: 5
  };
  saveClassProgress(custom);
  const reloaded = loadClassProgress();
  assert.strictEqual(reloaded.vocab, 5);
  assert.strictEqual(reloaded.kanji, 3);
  assert.strictEqual(reloaded.grammar, 2);
  assert.strictEqual(reloaded.readingStart, 4);
  assert.strictEqual(reloaded.readingEnd, 5);
  assert.ok(reloaded.updatedAt > 0);
});

// -----------------------------------------------------------------
// 2. Independent Stepping & Asymmetric Speeds
// -----------------------------------------------------------------
console.log('\n[2/4] Testing independent pillar stepping & asymmetric lesson speeds...');

it('Advances kanji by 1 lesson while reading advances by 2 lessons', () => {
  // Reset to chapter 1
  saveClassProgress(DEFAULT_CLASS_PROGRESS);

  // Class covers 1 kanji lesson
  stepPillarLesson('kanji', 1);

  // Class covers 2 reading lessons (e.g. Lesson 1 and Lesson 2)
  adjustReadingSpan(1); // readingEnd becomes 2

  const current = loadClassProgress();
  assert.strictEqual(current.kanji, 2, 'Kanji advanced to lesson 2');
  assert.strictEqual(current.vocab, 1, 'Vocab stayed at chapter 1');
  assert.strictEqual(current.grammar, 1, 'Grammar stayed at section 1');
  assert.strictEqual(current.readingStart, 1, 'Reading start stayed at lesson 1');
  assert.strictEqual(current.readingEnd, 2, 'Reading end expanded to lesson 2 (2 passages covered)');
});

it('Shifts reading window forward preserving multi-lesson span', () => {
  // We are at reading 1..2. Next class session moves to next reading block.
  stepPillarLesson('reading', 2);
  const current = loadClassProgress();
  assert.strictEqual(current.readingStart, 3, 'Reading start stepped +2');
  assert.strictEqual(current.readingEnd, 4, 'Reading end stepped +2 maintaining 2-passage span');
});

it('Clamps values within proper textbook boundaries', () => {
  // Test lower bound clamp
  setPillarLesson('vocab', -5);
  let p = loadClassProgress();
  assert.strictEqual(p.vocab, 1, 'Vocab cannot be < 1');

  // Test upper bound clamp (vocab max 29)
  setPillarLesson('vocab', 999);
  p = loadClassProgress();
  assert.strictEqual(p.vocab, 29, 'Vocab cannot exceed 29');

  // Kanji max 25
  setPillarLesson('kanji', 50);
  p = loadClassProgress();
  assert.strictEqual(p.kanji, 25, 'Kanji cannot exceed 25');

  // Grammar max 12
  setPillarLesson('grammar', 20);
  p = loadClassProgress();
  assert.strictEqual(p.grammar, 12, 'Grammar cannot exceed 12');

  // Reading max 58
  setPillarLesson('reading', 60);
  p = loadClassProgress();
  assert.strictEqual(p.readingStart, 58, 'Reading start cannot exceed 58');
  assert.strictEqual(p.readingEnd, 58, 'Reading end cannot exceed 58');
});

// -----------------------------------------------------------------
// 3. Package Resolution & Metadata Matching
// -----------------------------------------------------------------
console.log('\n[3/4] Testing getActiveLessonPackage() metadata resolution...');

it('Resolves correct chapter keys and structure for active targets', () => {
  // Set targets
  setPillarLesson('vocab', 2);
  setPillarLesson('kanji', 4);
  setPillarLesson('grammar', 3);
  setPillarLesson('reading', 5, 6);

  // Setup mock state metadata
  state.chapterMetadata = {
    part1_02: { chapter: 2, topic_ja: '町で', topic_en: 'In Town' }
  };
  state.kanjiLessons = [
    { lesson_number: 4, title_ja: '第4課 交通', kanji: ['車', '駅', '道'] }
  ];
  state.grammarDB = {
    part1_1_6: {
      sections: [
        { section_id: 'p1_sec_3', title: '第3課 比較・選択', drills: [] }
      ]
    }
  };
  state.readingDB = {
    part1_les5: { id: 'part1_les5', title: 'Lesson 5 Reading' },
    part1_les6: { id: 'part1_les6', title: 'Lesson 6 Reading' }
  };

  const pkg = getActiveLessonPackage();
  assert.strictEqual(pkg.vocab.key, 'part1_02');
  assert.strictEqual(pkg.vocab.meta.topic_ja, '町で');
  assert.strictEqual(pkg.kanji.lessonNum, 4);
  assert.strictEqual(pkg.kanji.lesson.title_ja, '第4課 交通');
  assert.strictEqual(pkg.grammar.sectionNum, 3);
  assert.strictEqual(pkg.grammar.section.title, '第3課 比較・選択');
  assert.strictEqual(pkg.reading.start, 5);
  assert.strictEqual(pkg.reading.end, 6);
  assert.strictEqual(pkg.reading.passages.length, 2, '2 reading passages loaded');
});

// -----------------------------------------------------------------
// 4. Combined Class Sync Test Generation
// -----------------------------------------------------------------
console.log('\n[4/4] Testing buildClassCombinedTest() question aggregation...');

it('Creates consolidated test bundle matching exact current lesson targets', () => {
  const p = {
    vocab: 2,
    kanji: 4,
    grammar: 3,
    readingStart: 5,
    readingEnd: 6
  };

  const testBundle = buildClassCombinedTest(p);
  assert.ok(testBundle.id.includes('class-combined'));
  assert.ok(testBundle.title.includes('学級同期総合演習'));
  assert.strictEqual(testBundle.pillar, 'class_sync');
  assert.ok(testBundle.subTitle.includes('Vocab Ch 2'));
  assert.ok(testBundle.subTitle.includes('Kanji L 4'));
  assert.ok(testBundle.subTitle.includes('Grammar Sec 3'));
  assert.ok(testBundle.subTitle.includes('Reading L 5–6'));
});

console.log('\n========================================================');
console.log(`Results: ${passedTests}/${totalTests} tests passed`);
console.log('========================================================\n');
