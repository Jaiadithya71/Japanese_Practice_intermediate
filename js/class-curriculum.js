/* =======================================================
   NIHONGO INTERMEDIATE — class-curriculum.js
   Synchronized Class Track with Independent Pillar Progress
   Handles fluctuating, asynchronous lesson pacing across 5 books
   ======================================================= */

import { state } from './state.js';
import { getAllAvailableTests } from './test.js';

export const CLASS_STORAGE_KEY = 'nihongo_intermediate_class_progress_v1';

export const DEFAULT_CLASS_PROGRESS = {
  vocab: 1,        // Chapter 1..21
  kanji: 1,        // Lesson 1..25
  grammar: 1,      // Section 1..12
  readingStart: 1, // Lesson 1..58
  readingEnd: 1,   // Supports multi-lesson range e.g. 1..2
  updatedAt: Date.now()
};

/**
 * Loads class progress from localStorage or state
 */
export function loadClassProgress() {
  try {
    if (typeof localStorage !== 'undefined') {
      const raw = localStorage.getItem(CLASS_STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        return { ...DEFAULT_CLASS_PROGRESS, ...parsed };
      }
    }
  } catch (e) {
    console.warn('Failed to parse class progress, using defaults', e);
  }
  return { ...DEFAULT_CLASS_PROGRESS };
}

/**
 * Saves class progress to localStorage
 */
export function saveClassProgress(progress) {
  const updated = {
    ...progress,
    updatedAt: Date.now()
  };
  try {
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem(CLASS_STORAGE_KEY, JSON.stringify(updated));
    }
  } catch (e) {
    console.warn('Failed to persist class progress', e);
  }
  if (!state.ui) state.ui = {};
  state.ui.classProgress = updated;
  return updated;
}

/**
 * Sets a specific pillar's lesson target
 */
export function setPillarLesson(pillar, value, endValue = null) {
  const current = loadClassProgress();
  const val = Math.max(1, parseInt(value, 10) || 1);

  if (pillar === 'vocab') {
    current.vocab = Math.min(29, val);
  } else if (pillar === 'kanji') {
    current.kanji = Math.min(25, val);
  } else if (pillar === 'grammar') {
    current.grammar = Math.min(12, val);
  } else if (pillar === 'reading') {
    current.readingStart = Math.min(58, val);
    current.readingEnd = endValue !== null ? Math.min(58, Math.max(current.readingStart, parseInt(endValue, 10) || val)) : current.readingStart;
  }

  saveClassProgress(current);
  return current;
}

/**
 * Increments or decrements a pillar's lesson target
 */
export function stepPillarLesson(pillar, delta = 1) {
  const current = loadClassProgress();
  if (pillar === 'vocab') {
    return setPillarLesson('vocab', current.vocab + delta);
  } else if (pillar === 'kanji') {
    return setPillarLesson('kanji', current.kanji + delta);
  } else if (pillar === 'grammar') {
    return setPillarLesson('grammar', current.grammar + delta);
  } else if (pillar === 'reading') {
    const span = Math.max(0, current.readingEnd - current.readingStart);
    const newStart = Math.max(1, Math.min(58, current.readingStart + delta));
    return setPillarLesson('reading', newStart, newStart + span);
  }
  return current;
}

/**
 * Extends the reading lesson range (e.g. 1 lesson -> 2 lessons)
 */
export function adjustReadingSpan(delta = 1) {
  const current = loadClassProgress();
  const newEnd = Math.max(current.readingStart, Math.min(58, current.readingEnd + delta));
  return setPillarLesson('reading', current.readingStart, newEnd);
}

/**
 * Resolves metadata and entities for the active class progress
 */
export function getActiveLessonPackage(progress = null) {
  const p = progress || loadClassProgress();

  // 1. Vocab chapter data
  const chKey = p.vocab <= 21 
    ? `part1_${String(p.vocab).padStart(2, '0')}`
    : `part2_${String(p.vocab - 21).padStart(2, '0')}`;
  
  const vocabMeta = state.chapterMetadata?.[chKey] || {
    chapter: p.vocab,
    topic_ja: `第${p.vocab}課`,
    topic_en: `Chapter ${p.vocab}`
  };
  const vocabWords = (state.vocabDB?.[chKey]?.sections || []).flatMap(s => s.vocabulary || []);

  // 2. Kanji lesson data
  const kanjiLes = (state.kanjiLessons || []).find(l => (l.lesson_number || l.lesson) === p.kanji) || {
    lesson_number: p.kanji,
    title_ja: `第${p.kanji}課`,
    title_en: `Lesson ${p.kanji}`,
    kanji: []
  };

  // 3. Grammar section data
  let grammarSec = null;
  const secId = `p1_sec_${p.grammar}`;
  const allSecs = [
    ...(state.grammarDB?.part1_1_6?.sections || []),
    ...(state.grammarDB?.part1_7_12?.sections || [])
  ];
  grammarSec = allSecs.find(s => s.section_id === secId || s.id === secId) || allSecs[p.grammar - 1] || {
    title: `第${p.grammar}課`,
    drills: [],
    patterns: []
  };

  // 4. Reading passages (supports range readingStart .. readingEnd)
  const readingList = [];
  const rKeys = Object.keys(state.readingDB || {});
  for (let rNum = p.readingStart; rNum <= p.readingEnd; rNum++) {
    // Try to match by lessonId or index
    let rMatch = state.readingDB?.[`lesson_${rNum}`] || state.readingDB?.[`part1_les${rNum}`] || state.readingDB?.[`part2_short_${rNum}`] || null;
    if (!rMatch && rNum <= rKeys.length) {
      rMatch = state.readingDB[rKeys[rNum - 1]];
    }
    if (rMatch) {
      readingList.push({
        num: rNum,
        lesson: rMatch
      });
    }
  }

  return {
    progress: p,
    vocab: { key: chKey, meta: vocabMeta, words: vocabWords },
    kanji: { lessonNum: p.kanji, lesson: kanjiLes },
    grammar: { sectionNum: p.grammar, section: grammarSec },
    reading: { start: p.readingStart, end: p.readingEnd, passages: readingList }
  };
}

/**
 * Gathers all practice test questions matching the current class targets
 */
export function buildClassCombinedTest(progress = null) {
  const p = progress || loadClassProgress();
  const allTests = getAllAvailableTests();
  const matchedTests = [];
  const questions = [];

  // 1. Vocab Tests for current chapter
  const vocabTargetId = `vocab-part1_${String(p.vocab).padStart(2, '0')}`;
  const vMatch = allTests.find(t => t.id === vocabTargetId || t.id.includes(`_${String(p.vocab).padStart(2, '0')}`));
  if (vMatch) {
    matchedTests.push(vMatch);
    questions.push(...(vMatch.questions || []));
  }

  // 2. Kanji Tests for current lesson
  const kMatch = allTests.find(t => t.id === `kanji-drill-L${p.kanji}` || t.title.includes(`第${p.kanji}課`));
  if (kMatch) {
    matchedTests.push(kMatch);
    questions.push(...(kMatch.questions || []));
  }

  // 3. Grammar Tests for current section
  const gMatch = allTests.find(t => t.id.includes(`sec-${p.grammar}`) || t.title.includes(`第${p.grammar}課`));
  if (gMatch) {
    matchedTests.push(gMatch);
    questions.push(...(gMatch.questions || []));
  }

  // 4. Reading questions for current range
  for (let rNum = p.readingStart; rNum <= p.readingEnd; rNum++) {
    const rTest = allTests.find(t => t.pillar === 'reading');
    if (rTest && rTest.questions) {
      // Pick matching questions or slice
      const matchingQ = rTest.questions.filter(q => q.id.includes(`_${rNum}_`) || q.id.includes(`-${rNum}-`));
      if (matchingQ.length > 0) {
        questions.push(...matchingQ);
      }
    }
  }

  return {
    id: `class-combined-v${p.vocab}-k${p.kanji}-g${p.grammar}-r${p.readingStart}_${p.readingEnd}`,
    title: `学級同期総合演習 (Class Sync Test)`,
    subTitle: `Vocab Ch ${p.vocab} · Kanji L ${p.kanji} · Grammar Sec ${p.grammar} · Reading L ${p.readingStart === p.readingEnd ? p.readingStart : `${p.readingStart}–${p.readingEnd}`}`,
    pillar: 'class_sync',
    category: 'class_sync',
    questionCount: questions.length,
    questions,
    sourceTests: matchedTests
  };
}

/**
 * Renders the Class Track Hub HTML in the Learn tab
 */
export function renderClassTrackHTML(containerId = 'class-track-container') {
  const container = document.getElementById(containerId);
  if (!container) return;

  const pkg = getActiveLessonPackage();
  const p = pkg.progress;
  const testBundle = buildClassCombinedTest(p);

  const readingLabel = p.readingStart === p.readingEnd 
    ? `第 ${p.readingStart} 課` 
    : `第 ${p.readingStart} ～ ${p.readingEnd} 課 (${p.readingEnd - p.readingStart + 1} Passages)`;

  container.innerHTML = `
    <div class="class-track-card">
      <div class="class-track-header">
        <div class="class-track-badge">
          <i class="fa-solid fa-graduation-cap"></i> 授業同期学習 · Synchronized Class Track
        </div>
        <p class="class-track-sub">
          週3回の授業ペースに完全同期。教科ごとの進度の違い（漢字1課＋読解2課など）も個別に自由調整できます。
        </p>
      </div>

      <!-- Individual Pillar Steppers Grid -->
      <div class="class-steppers-grid">
        <!-- 1. Vocabulary Stepper -->
        <div class="class-pillar-box">
          <div class="cpb-top">
            <span class="cpb-icon"><i class="fa-solid fa-book-bookmark"></i></span>
            <span class="cpb-name">語彙 Vocab</span>
          </div>
          <div class="cpb-stepper">
            <button class="cpb-btn" onclick="window.N3Class.step('vocab', -1)" title="Previous chapter"><i class="fa-solid fa-minus"></i></button>
            <span class="cpb-val">第 ${p.vocab} 課</span>
            <button class="cpb-btn" onclick="window.N3Class.step('vocab', 1)" title="Next chapter"><i class="fa-solid fa-plus"></i></button>
          </div>
          <div class="cpb-desc">${pkg.vocab.meta.topic_ja || `Chapter ${p.vocab}`}</div>
          <div class="cpb-actions">
            <button class="btn btn-sm btn-ghost" onclick="window.N3Class.openVocab(${p.vocab})">
              <i class="fa-solid fa-list"></i> ${pkg.vocab.words.length || 40} Words
            </button>
          </div>
        </div>

        <!-- 2. Kanji Stepper -->
        <div class="class-pillar-box">
          <div class="cpb-top">
            <span class="cpb-icon"><i class="fa-solid fa-shapes"></i></span>
            <span class="cpb-name">漢字 Kanji</span>
          </div>
          <div class="cpb-stepper">
            <button class="cpb-btn" onclick="window.N3Class.step('kanji', -1)" title="Previous lesson"><i class="fa-solid fa-minus"></i></button>
            <span class="cpb-val">第 ${p.kanji} 課</span>
            <button class="cpb-btn" onclick="window.N3Class.step('kanji', 1)" title="Next lesson"><i class="fa-solid fa-plus"></i></button>
          </div>
          <div class="cpb-desc">${pkg.kanji.lesson.title_ja || `Lesson ${p.kanji}`}</div>
          <div class="cpb-actions">
            <button class="btn btn-sm btn-ghost" onclick="window.drillKanjiLesson(${p.kanji})">
              <i class="fa-solid fa-play"></i> Drill Kanji (${(pkg.kanji.lesson.kanji || []).length || 18})
            </button>
          </div>
        </div>

        <!-- 3. Grammar Stepper -->
        <div class="class-pillar-box">
          <div class="cpb-top">
            <span class="cpb-icon"><i class="fa-solid fa-pen-nib"></i></span>
            <span class="cpb-name">文法 Grammar</span>
          </div>
          <div class="cpb-stepper">
            <button class="cpb-btn" onclick="window.N3Class.step('grammar', -1)" title="Previous section"><i class="fa-solid fa-minus"></i></button>
            <span class="cpb-val">第 ${p.grammar} 課</span>
            <button class="cpb-btn" onclick="window.N3Class.step('grammar', 1)" title="Next section"><i class="fa-solid fa-plus"></i></button>
          </div>
          <div class="cpb-desc">${pkg.grammar.section.title || `Section ${p.grammar}`}</div>
          <div class="cpb-actions">
            <button class="btn btn-sm btn-ghost" onclick="window.showView('grammar')">
              <i class="fa-solid fa-graduation-cap"></i> Patterns &amp; Drills
            </button>
          </div>
        </div>

        <!-- 4. Reading Stepper (with Span Range) -->
        <div class="class-pillar-box">
          <div class="cpb-top">
            <span class="cpb-icon"><i class="fa-solid fa-book-open"></i></span>
            <span class="cpb-name">読解 Reading</span>
          </div>
          <div class="cpb-stepper">
            <button class="cpb-btn" onclick="window.N3Class.step('reading', -1)" title="Previous passage"><i class="fa-solid fa-backward-step"></i></button>
            <span class="cpb-val">${readingLabel}</span>
            <button class="cpb-btn" onclick="window.N3Class.step('reading', 1)" title="Next passage"><i class="fa-solid fa-forward-step"></i></button>
          </div>
          <div class="cpb-span-ctrl">
            <button class="cpb-span-btn" onclick="window.N3Class.adjustReadingSpan(-1)" title="Reduce passage count" ${p.readingEnd <= p.readingStart ? 'disabled' : ''}>- 1課</button>
            <span class="cpb-span-label">${p.readingEnd - p.readingStart + 1}課 連続</span>
            <button class="cpb-span-btn" onclick="window.N3Class.adjustReadingSpan(1)" title="Add another passage">+ 1課</button>
          </div>
          <div class="cpb-actions">
            <button class="btn btn-sm btn-ghost" onclick="window.showView('reading')">
              <i class="fa-solid fa-book-reader"></i> Open Reader
            </button>
          </div>
        </div>
      </div>

      <!-- Quick Launch Action Bar -->
      <div class="class-track-footer">
        <div class="class-summary-pill">
          <i class="fa-solid fa-circle-check"></i>
          <span>同期テスト問題数: <strong>${testBundle.questionCount} 題</strong></span>
        </div>
        <button class="btn btn-primary class-launch-btn" onclick="window.N3Class.launchTest()">
          <i class="fa-solid fa-play"></i> 今日の授業分をまとめて総復習テスト (Start Sync Test)
        </button>
      </div>
    </div>
  `;
}

// Controller handlers exposed for DOM
export const N3Class = {
  get: loadClassProgress,
  save: saveClassProgress,
  step: (pillar, delta) => {
    stepPillarLesson(pillar, delta);
    renderClassTrackHTML();
    // Also re-render Today if present
    if (typeof window.renderToday === 'function') window.renderToday();
  },
  adjustReadingSpan: (delta) => {
    adjustReadingSpan(delta);
    renderClassTrackHTML();
    if (typeof window.renderToday === 'function') window.renderToday();
  },
  openVocab: (chapterNum) => {
    if (typeof window.showView === 'function') {
      window.showView('vocab');
      if (typeof window.selectChapter === 'function') {
        const chKey = chapterNum <= 21 
          ? `part1_${String(chapterNum).padStart(2, '0')}`
          : `part2_${String(chapterNum - 21).padStart(2, '0')}`;
        window.selectChapter(chKey);
      }
    }
  },
  launchTest: () => {
    const testBundle = buildClassCombinedTest();
    if (testBundle.questionCount === 0) {
      alert('No test questions available for the selected lesson targets yet.');
      return;
    }
    if (typeof window.startTestSession === 'function') {
      window.startTestSession(testBundle);
    }
  },
  render: renderClassTrackHTML
};

// Bind to window
if (typeof window !== 'undefined') {
  window.N3Class = N3Class;
}
