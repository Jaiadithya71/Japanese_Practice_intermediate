/* =======================================================
   NIHONGO INTERMEDIATE — reading-types.js
   Dokkai Passage Categorization, CPM & Speed Engine,
   Chunk Mode (区切り) Connectors, Question Taxonomy,
   and Second-Pass Re-read Scheduler.
   Reference: n3_dev_handoff/04_READING_COMPREHENSION_SPEC.md §4, §6, §7
   ======================================================= */

export const PASSAGE_GENRES = {
  SHORT: 'short',
  MEDIUM: 'medium',
  LONG: 'long',
  INFO: 'info',
  FOUNDATION: 'foundation',
  STRATEGY: 'strategy',
  OTHER: 'other'
};

export const GENRE_METADATA = {
  short: { id: 'short', label_ja: '短文', label_en: 'Short', icon: 'fa-file-lines' },
  medium: { id: 'medium', label_ja: '中文', label_en: 'Medium', icon: 'fa-book-open' },
  long: { id: 'long', label_ja: '長文', label_en: 'Long', icon: 'fa-scroll' },
  info: { id: 'info', label_ja: '情報検索', label_en: 'Info Retrieval', icon: 'fa-magnifying-glass' },
  foundation: { id: 'foundation', label_ja: '基礎編', label_en: 'Foundation', icon: 'fa-cube' },
  strategy: { id: 'strategy', label_ja: '対策編', label_en: 'Pattern Strategy', icon: 'fa-chess' },
  other: { id: 'other', label_ja: '読解', label_en: 'Reading', icon: 'fa-book' }
};

/**
 * Categorize a passage lesson by genre (short, medium, long, info retrieval, foundation, strategy).
 * @param {Object} lesson
 * @returns {string} One of PASSAGE_GENRES values
 */
export function categorizePassage(lesson) {
  if (!lesson) return PASSAGE_GENRES.OTHER;
  const cat = lesson.category || '';
  const genre = lesson.genre || '';
  const title = lesson.title_ja || lesson.title || '';

  if (cat === 'real_short' || genre.includes('短文') || title.includes('短文')) {
    return PASSAGE_GENRES.SHORT;
  }
  if (cat === 'real_medium' || genre.includes('中文') || title.includes('中文')) {
    return PASSAGE_GENRES.MEDIUM;
  }
  if (cat === 'real_long' || genre.includes('長文') || title.includes('長文')) {
    return PASSAGE_GENRES.LONG;
  }
  if (cat === 'info' || genre.includes('情報検索') || title.includes('情報検索')) {
    return PASSAGE_GENRES.INFO;
  }
  if (cat === 'foundation' || genre.includes('基礎') || title.includes('基礎')) {
    return PASSAGE_GENRES.FOUNDATION;
  }
  if (cat === 'strategy' || genre.includes('対策') || title.includes('対策')) {
    return PASSAGE_GENRES.STRATEGY;
  }

  // Fallback by problem numbers if present (Shin Kanzen Master standard numbering)
  if (lesson.problemNumber !== undefined && lesson.problemNumber !== null) {
    const pn = Number(lesson.problemNumber);
    if (pn >= 14 && pn <= 28) return PASSAGE_GENRES.SHORT;
    if (pn >= 29 && pn <= 48) return PASSAGE_GENRES.MEDIUM;
    if (pn >= 49 && pn <= 61) return PASSAGE_GENRES.LONG;
    if (pn >= 62 && pn <= 64) return PASSAGE_GENRES.INFO;
  }

  return PASSAGE_GENRES.OTHER;
}

/**
 * Count Japanese characters in a passage (excluding spaces and newline whitespace).
 * @param {Object|Array|string} passageOrSentences
 * @returns {number}
 */
export function countPassageChars(passageOrSentences) {
  if (!passageOrSentences) return 0;
  if (typeof passageOrSentences === 'string') {
    return passageOrSentences.replace(/\s+/g, '').length;
  }
  if (Array.isArray(passageOrSentences)) {
    return passageOrSentences.reduce((acc, s) => {
      const text = typeof s === 'string' ? s : (s.text_ja || '');
      return acc + text.replace(/\s+/g, '').length;
    }, 0);
  }
  if (typeof passageOrSentences === 'object') {
    if (Array.isArray(passageOrSentences.sentences)) {
      return countPassageChars(passageOrSentences.sentences);
    }
    if (typeof passageOrSentences.text_ja === 'string') {
      return countPassageChars(passageOrSentences.text_ja);
    }
  }
  return 0;
}

// Target Characters Per Minute for JLPT N3 reading pace
export const DEFAULT_READING_CPM = 330;

/**
 * Calculates target reading time in minutes (target = chars / 330 min).
 * @param {number} charCount
 * @param {number} [cpm=DEFAULT_READING_CPM]
 * @returns {number} Target time in minutes
 */
export function calculateTargetMinutes(charCount, cpm = DEFAULT_READING_CPM) {
  if (!charCount || charCount <= 0 || !cpm || cpm <= 0) return 0;
  return charCount / cpm;
}

/**
 * Calculates target reading time in seconds.
 * @param {number} charCount
 * @param {number} [cpm=DEFAULT_READING_CPM]
 * @returns {number} Target time in seconds
 */
export function calculateTargetSeconds(charCount, cpm = DEFAULT_READING_CPM) {
  if (!charCount || charCount <= 0 || !cpm || cpm <= 0) return 0;
  return Math.round((charCount / cpm) * 60);
}

/**
 * Calculates CPM (Characters Per Minute) given character count and elapsed seconds.
 * @param {number} charCount
 * @param {number} elapsedSeconds
 * @returns {number} CPM rounded to integer
 */
export function calculateCpm(charCount, elapsedSeconds) {
  if (!charCount || charCount <= 0 || !elapsedSeconds || elapsedSeconds <= 0) return 0;
  return Math.round((charCount / elapsedSeconds) * 60);
}

/**
 * Format seconds into mm:ss string.
 * @param {number} seconds
 * @returns {string}
 */
export function formatTime(seconds) {
  const s = Math.max(0, Math.round(seconds || 0));
  const mins = Math.floor(s / 60);
  const secs = s % 60;
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}

// =======================================================
// QUESTION KEYWORD MATCHER
// =======================================================

export const QUESTION_TYPES = {
  AUTHOR_OPINION: 'author_opinion',
  MEANING: 'meaning',
  REASON: 'reason',
  CONTENT_MATCH: 'content_match',
  TOPIC_DETAIL: 'topic_detail',
  UNKNOWN: 'unknown'
};

export const QUESTION_TYPE_RULES = [
  {
    type: QUESTION_TYPES.AUTHOR_OPINION,
    keyword: '筆者の考え',
    label_ja: '筆者の考え',
    label_en: "Author's Opinion",
    test: (text) => /筆者の考え|筆者が言いたいこと|筆者の主張/.test(text)
  },
  {
    type: QUESTION_TYPES.MEANING,
    keyword: 'どういう意味',
    label_ja: 'どういう意味',
    label_en: 'Meaning / Reference',
    test: (text) => /どういう意味|指示語|何を指して/.test(text)
  },
  {
    type: QUESTION_TYPES.REASON,
    keyword: 'なぜ',
    label_ja: 'なぜ',
    label_en: 'Reason / Cause',
    test: (text) => /なぜ|どうして|理由/.test(text)
  },
  {
    type: QUESTION_TYPES.CONTENT_MATCH,
    keyword: '内容と合っている',
    label_ja: '内容と合っている',
    label_en: 'Content Matching',
    test: (text) => /内容と合ってい|合っているもの|正しく述べている/.test(text)
  },
  {
    type: QUESTION_TYPES.TOPIC_DETAIL,
    keyword: '〜について',
    label_ja: '〜について',
    label_en: 'Topic / Detail',
    test: (text) => /について/.test(text)
  }
];

/**
 * Detect question taxonomy type using Japanese keyword matcher.
 * @param {string} questionTextJa
 * @returns {{ type: string, keyword: string, label_ja: string, label_en: string }}
 */
export function detectQuestionType(questionTextJa) {
  if (!questionTextJa || typeof questionTextJa !== 'string') {
    return {
      type: QUESTION_TYPES.UNKNOWN,
      keyword: '',
      label_ja: 'その他',
      label_en: 'Other / General'
    };
  }

  for (const rule of QUESTION_TYPE_RULES) {
    if (rule.test(questionTextJa)) {
      return {
        type: rule.type,
        keyword: rule.keyword,
        label_ja: rule.label_ja,
        label_en: rule.label_en
      };
    }
  }

  return {
    type: QUESTION_TYPES.UNKNOWN,
    keyword: '',
    label_ja: 'その他',
    label_en: 'Other / General'
  };
}

/**
 * Extract question type from question object or prompt string.
 * @param {Object|string} qOrText
 * @returns {{ type: string, keyword: string, label_ja: string, label_en: string }}
 */
export function getQuestionType(qOrText) {
  const text = typeof qOrText === 'string'
    ? qOrText
    : (qOrText?.question_ja || qOrText?.questionText_ja || qOrText?.prompt || '');
  return detectQuestionType(text);
}

// =======================================================
// CHUNKY PUNCTUATION CONNECTORS (区切り MODE)
// Connectors: が、ので、から、と、ば、たら、なら、ても、のに、plus 、
// =======================================================

export const CHUNK_CONNECTORS = ['ので', 'から', 'たら', 'なら', 'ても', 'のに', 'が', 'と', 'ば', '、'];

// Single match regex (ordered with multi-char tokens first)
export const CHUNK_CONNECTOR_REGEX = /(?:ので|から|たら|なら|ても|のに|が|と|ば|、)/;

// Global regex for matching all connectors
export const CHUNK_CONNECTOR_GLOBAL_REGEX = /(?:ので|から|たら|なら|ても|のに|が|と|ば|、)/g;

// Splitting regex: splits AFTER connectors/commas without splitting between a connector and its trailing comma
export const CHUNK_SPLIT_REGEX = /(?<=(?:ので|から|たら|なら|ても|のに|が|と|ば)、|(?<!(?:ので|から|たら|なら|ても|のに|が|と|ば))、|(?:ので|から|たら|なら|ても|のに|が|と|ば)(?!、))/;

/**
 * Inserts division slashes `／` after connectors and commas for 区切り reading mode.
 * Preserves connector + comma combinations cleanly (e.g. が、／ instead of が／、／).
 * @param {string} textJa
 * @param {string} [divider='／']
 * @returns {string}
 */
export function insertChunkDividers(textJa, divider = '／') {
  if (!textJa || typeof textJa !== 'string') return '';
  return textJa.replace(/(?:(?:ので|から|たら|なら|ても|のに|が|と|ば)、?|、)/g, (match) => `${match}${divider}`);
}

/**
 * Splits Japanese text into chunk array at connector and comma boundaries.
 * @param {string} textJa
 * @returns {string[]}
 */
export function splitIntoChunks(textJa) {
  if (!textJa || typeof textJa !== 'string') return [];
  return textJa.split(CHUNK_SPLIT_REGEX).filter(s => s.length > 0);
}

// =======================================================
// SECOND-PASS CRITERIA & RE-READ SCHEDULER
// Criteria: accuracy >= 0.8 and elapsed <= 1.3 * target
// =======================================================

/**
 * Check whether a second-pass attempt meets the pass criteria.
 * Criteria: accuracy >= 0.8 AND elapsed <= 1.3 * targetSeconds.
 * @param {number|Object} accuracy
 * @param {number} [elapsedSeconds]
 * @param {number} [targetSeconds]
 * @returns {boolean}
 */
export function isSecondPassPassed(accuracy, elapsedSeconds, targetSeconds) {
  if (typeof accuracy === 'object' && accuracy !== null) {
    const opts = accuracy;
    accuracy = opts.accuracy ?? 0;
    elapsedSeconds = opts.elapsedSeconds ?? opts.elapsed ?? 0;
    targetSeconds = opts.targetSeconds ?? opts.targetTime ?? opts.target ?? 0;
  }

  const accNum = Number(accuracy) || 0;
  const elapsedNum = Number(elapsedSeconds) || 0;
  const targetNum = Number(targetSeconds) || 0;

  const meetsAccuracy = accNum >= 0.8;
  const meetsTime = targetNum <= 0 ? true : elapsedNum <= (1.3 * targetNum);

  return meetsAccuracy && meetsTime;
}

/**
 * Evaluate second-pass attempt with comprehensive breakdown.
 * @param {Object} params
 * @returns {Object}
 */
export function evaluateSecondPass({ accuracy = 0, elapsedSeconds = 0, targetSeconds = 0 }) {
  const acc = Number(accuracy) || 0;
  const elapsed = Number(elapsedSeconds) || 0;
  const target = Number(targetSeconds) || 0;
  const maxAllowedSeconds = target > 0 ? 1.3 * target : Infinity;

  const meetsAccuracy = acc >= 0.8;
  const meetsTime = target <= 0 ? true : elapsed <= maxAllowedSeconds;
  const passed = meetsAccuracy && meetsTime;

  return {
    passed,
    meetsAccuracy,
    meetsTime,
    accuracy: acc,
    elapsedSeconds: elapsed,
    targetSeconds: target,
    maxAllowedSeconds: Math.round(maxAllowedSeconds)
  };
}

export const REREAD_INTERVALS_DAYS = [3, 10, 25];
export const REREAD_FAIL_REPEAT_DAYS = 2;

/**
 * Calculate the next re-read schedule for Layer A passage tracking.
 * - Initial read: schedules second pass at +3 days (step 0 -> 1).
 * - Second pass 1: pass -> +10 days (step 1 -> 2).
 * - Second pass 2: pass -> +25 days (step 2 -> 3; mastered).
 * - Failure: repeats same step in 2 days (+2d).
 * @param {Object} options
 * @param {number} [options.reads=0]
 * @param {number} [options.currentStep=0]
 * @param {boolean} [options.passed=false]
 * @param {number} [options.now=Date.now()]
 * @param {Function} [options.snapFn]
 * @returns {Object}
 */
export function calculateRereadSchedule({
  reads = 0,
  currentStep = 0,
  passed = false,
  now = Date.now(),
  snapFn = null
} = {}) {
  let nextStep = currentStep;
  let intervalDays = 3;
  let advanced = false;
  let mastered = false;

  if (reads === 0) {
    // First read: always schedules second pass at +3 days
    intervalDays = REREAD_INTERVALS_DAYS[0]; // 3 days
    nextStep = 0;
    advanced = true;
  } else {
    // Subsequent read (second pass or later)
    if (passed) {
      advanced = true;
      if (currentStep === 0) {
        nextStep = 1;
        intervalDays = REREAD_INTERVALS_DAYS[1]; // 10 days
      } else if (currentStep === 1) {
        nextStep = 2;
        intervalDays = REREAD_INTERVALS_DAYS[2]; // 25 days
        mastered = true; // 2 successful passes
      } else {
        nextStep = 3;
        intervalDays = REREAD_INTERVALS_DAYS[2]; // 25 days cap
        mastered = true;
      }
    } else {
      // Failed: repeat the same step in 2 days
      intervalDays = REREAD_FAIL_REPEAT_DAYS; // 2 days
      nextStep = currentStep;
      advanced = false;
      mastered = false;
    }
  }

  const rawMs = now + intervalDays * 86400000;
  const nextDue = typeof snapFn === 'function' ? snapFn(rawMs) : rawMs;

  return {
    intervalDays,
    nextStep,
    nextDue,
    advanced,
    mastered
  };
}

// =======================================================
// QUESTION SHUFFLING & EVALUATION
// =======================================================

/**
 * Shuffles question options (and parallel options_en) for second pass re-reads.
 * Updates correctAnswer to match the new 1-based index of the original answer.
 * @param {Object} question
 * @param {Function} [rng=Math.random]
 * @returns {Object} A new question object with shuffled options and updated correctAnswer
 */
export function shuffleQuestionOptions(question, rng = Math.random) {
  if (!question || !Array.isArray(question.options) || question.options.length <= 1) {
    return { ...question };
  }

  const originalOptions = question.options;
  const originalOptionsEn = question.options_en || [];
  const originalCorrect = parseInt(question.correctAnswer, 10);

  // Array of 0-based indices [0, 1, 2, ...]
  const indices = originalOptions.map((_, i) => i);

  // Fisher-Yates shuffle
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    const temp = indices[i];
    indices[i] = indices[j];
    indices[j] = temp;
  }

  const shuffledOptions = indices.map(i => originalOptions[i]);
  const shuffledOptionsEn = originalOptionsEn.length === originalOptions.length
    ? indices.map(i => originalOptionsEn[i])
    : [];

  const originalCorrectIdx = originalCorrect - 1;
  const newCorrectIdx = indices.indexOf(originalCorrectIdx);
  const newCorrectAnswer = newCorrectIdx !== -1 ? newCorrectIdx + 1 : originalCorrect;

  return {
    ...question,
    options: shuffledOptions,
    options_en: shuffledOptionsEn,
    correctAnswer: newCorrectAnswer,
    _originalOptions: originalOptions,
    _originalCorrectAnswer: originalCorrect,
    _shuffledIndices: indices
  };
}

/**
 * Evaluates a selected option number against the question's correct answer.
 * @param {Object} question
 * @param {number|string} selectedOption 1-based option number
 * @returns {{ isCorrect: boolean, selectedOption: number, correctAnswer: number }}
 */
export function evaluateQuestionAnswer(question, selectedOption) {
  const selected = parseInt(selectedOption, 10);
  const correct = parseInt(question?.correctAnswer, 10);
  const isCorrect = !isNaN(selected) && !isNaN(correct) && selected === correct;

  return {
    isCorrect,
    selectedOption: selected,
    correctAnswer: correct
  };
}

// Bind to window for universal browser availability
const N3ReadingTypes = {
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
};

if (typeof window !== 'undefined') {
  window.N3ReadingTypes = N3ReadingTypes;
}

export default N3ReadingTypes;
