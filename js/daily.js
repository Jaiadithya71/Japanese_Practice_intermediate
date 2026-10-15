/* =======================================================
   NIHONGO INTERMEDIATE — daily.js
   Habit Engine, Daily Session Queue & Next Best Action (WP-6)
   Reference: n3_dev_handoff/01_UX_AND_SCREEN_SPEC.md §2, §3
              n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §6
   ======================================================= */

import { state as defaultState } from './state.js';
import { istNow, istDateKey } from './time.js';
import { getDay } from './daylog.js';
import { calculatePace, PACE_PROFILES } from './planner.js';
import {
  getAllDueItems,
  getDueItemsCount,
  getItemStats,
  getItemStatus,
  isCatchUpMode
} from './srs.js';
import { CHUNK_KANJI } from './kanji-runner.js';
import {
  BACKLOG_THRESHOLD,
  SEC_PER_REVIEW,
  SEC_PER_NEW,
  EXAM_DATE_ISO
} from './config.js';

export const DAILY_SESSION_STORAGE_KEY = 'nihongo_daily_session_progress_v1';

// Default grammar cluster definitions if not loaded in indexes
const DEFAULT_GRAMMAR_CLUSTERS = [
  { id: 'time', name_en: 'Time & Timing', name_ja: '時間・時期', patterns: ['P1-1', 'P1-2', 'P1-3', 'P1-4', 'P1-7', 'P1-9', 'P2-74', 'P2-75', 'P2-76'] },
  { id: 'cause', name_en: 'Cause & Reason', name_ja: '原因・理由', patterns: ['P1-19', 'P1-20', 'P1-21', 'P1-22', 'P1-23', 'P2-71', 'P2-72', 'P3-82', 'P3-83'] },
  { id: 'contrast', name_en: 'Contrast & Comparison', name_ja: '対比・逆接', patterns: ['P1-14', 'P1-15', 'P1-16', 'P1-17', 'P1-18', 'P1-38', 'P2-54', 'P2-55'] },
  { id: 'inability-compulsion', name_en: 'Obligation & Impossibility', name_ja: '義務・不可・禁止・部分否定', patterns: ['P1-34', 'P1-35', 'P1-36', 'P1-37', 'P1-42', 'P1-43', 'P1-44', 'P1-45', 'P2-59'] },
  { id: 'purpose-intent', name_en: 'Purpose, Volition & Desires', name_ja: '目的・意向・希望・働きかけ', patterns: ['P1-39', 'P1-40', 'P1-41', 'P1-46', 'P1-47', 'P1-48', 'P1-49', 'P2-60', 'P2-61'] },
  { id: 'condition', name_en: 'Condition & Hypothesis', name_ja: '条件・仮定・反実仮想', patterns: ['P1-5', 'P1-6', 'P1-8', 'P1-24', 'P1-25', 'P1-26', 'P1-27', 'P1-28', 'P2-56', 'P2-57', 'P2-62'] },
  { id: 'degree-limit', name_en: 'Degree & Limit', name_ja: '程度・限界・最高', patterns: ['P1-10', 'P1-11', 'P1-12', 'P1-13', 'P2-58'] },
  { id: 'viewpoint-attitude', name_en: 'Viewpoint, Attitude & Transmission', name_ja: '視点・伝聞・敬語', patterns: ['P1-29', 'P1-30', 'P1-31', 'P1-32', 'P1-33', 'P1-50', 'P1-51', 'P1-52', 'P1-53', 'P2-65', 'P2-77', 'P2-78', 'P2-79'] },
  { id: 'form-other', name_en: 'Sentence Forms & Cohesion', name_ja: '文型・構文・文の対応', patterns: ['P2-63', 'P2-64', 'P2-66', 'P2-67', 'P2-68', 'P2-69', 'P2-70', 'P2-73', 'P3-80', 'P3-81'] }
];

/**
 * Helper to check if an item has been previously seen in SRS
 */
function isItemSeen(statsRecord) {
  return Boolean(
    statsRecord &&
    (statsRecord.reps > 0 || statsRecord.correct > 0 || statsRecord.incorrect > 0 || statsRecord.lastSeen > 0)
  );
}

/**
 * Resolves Tier 1 vocab IDs from state indexes, state or fallback
 */
function getTier1VocabSet(db) {
  if (db?.idx?.vocabTiers?.tier1 && Array.isArray(db.idx.vocabTiers.tier1)) {
    return new Set(db.idx.vocabTiers.tier1);
  }
  if (db?.vocabTiers?.tier1 && Array.isArray(db.vocabTiers.tier1)) {
    return new Set(db.vocabTiers.tier1);
  }
  return null;
}

/**
 * Finds the next 3-kanji chunk for Step 3
 */
export function findNextKanjiChunk(db = defaultState, stats = db?.stats || {}) {
  const kanjiDB = db.kanjiDB || {};
  const lessons = db.kanjiLessons && db.kanjiLessons.length > 0
    ? db.kanjiLessons
    : Array.from({ length: 25 }, (_, i) => ({ lesson_number: i + 1 }));

  for (const l of lessons) {
    const lNum = Number(l.lesson_number || l.lesson) || 1;
    // Find all kanji in this lesson
    const lessonKanji = [];
    for (const char in kanjiDB) {
      const k = kanjiDB[char];
      if (k && Number(k.lesson_number) === lNum) {
        lessonKanji.push(k);
      }
    }
    lessonKanji.sort((a, b) => (a.order || 0) - (b.order || 0));
    if (lessonKanji.length === 0) continue;

    // Split into chunks of CHUNK_KANJI (3)
    const chunkSize = CHUNK_KANJI || 3;
    for (let cIdx = 0; cIdx < Math.ceil(lessonKanji.length / chunkSize); cIdx++) {
      const chunkKanjiList = lessonKanji.slice(cIdx * chunkSize, (cIdx + 1) * chunkSize);
      const chars = chunkKanjiList.map(k => k.kanji || k.char || k.id);

      // Check if this chunk is unfinished
      const hasUnseen = chars.some(char => {
        const s = stats[`K:${char}`];
        return !isItemSeen(s);
      });

      if (hasUnseen) {
        // Collect target words for this chunk
        const words = [];
        for (const k of chunkKanjiList) {
          const tw = k.target_words || k.words || [];
          for (const w of tw) {
            words.push({
              ...w,
              homeKanji: k.kanji || k.char,
              lesson: lNum
            });
          }
        }
        return {
          lessonNumber: lNum,
          chunkIndex: cIdx,
          totalChunks: Math.ceil(lessonKanji.length / chunkSize),
          kanji: chars,
          kanjiList: chunkKanjiList,
          words
        };
      }
    }
  }

  // Fallback: return lesson 1 chunk 0 if all done or empty
  return {
    lessonNumber: 1,
    chunkIndex: 0,
    totalChunks: 1,
    kanji: ['一', '二', '三'],
    kanjiList: [],
    words: []
  };
}

/**
 * Finds unseen Tier 1 vocabulary words for Step 4
 */
export function findNextVocabBatch(db = defaultState, stats = db?.stats || {}, quota = 10) {
  const vocabDB = db.vocabDB || {};
  const tier1Set = getTier1VocabSet(db);
  const result = [];

  const chKeys = Object.keys(vocabDB).sort((a, b) => {
    const parseNum = k => {
      const m = k.match(/\d+/);
      return m ? parseInt(m[0], 10) : 999;
    };
    return parseNum(a) - parseNum(b);
  });

  for (const chId of chKeys) {
    const words = vocabDB[chId] || [];
    for (const w of words) {
      if (tier1Set && !tier1Set.has(w.id)) {
        continue; // Only Tier 1 core words
      }
      const s = stats[`V:${w.id}`];
      if (!isItemSeen(s)) {
        result.push({
          ...w,
          chapterId: chId,
          key: `V:${w.id}`,
          type: 'vocab'
        });
        if (result.length >= quota) {
          return result;
        }
      }
    }
  }

  // If tier1 filtering yielded nothing, check general unseen vocab
  if (result.length === 0) {
    for (const chId of chKeys) {
      const words = vocabDB[chId] || [];
      for (const w of words) {
        const s = stats[`V:${w.id}`];
        if (!isItemSeen(s)) {
          result.push({
            ...w,
            chapterId: chId,
            key: `V:${w.id}`,
            type: 'vocab'
          });
          if (result.length >= quota) return result;
        }
      }
    }
  }

  return result;
}

/**
 * Identifies weakest grammar cluster based on error rates and lapses
 */
export function findWeakestGrammarCluster(db = defaultState, stats = db?.stats || {}) {
  const clusters = db.idx?.grammar?.byCluster
    ? Object.values(db.idx.grammar.byCluster)
    : (db.clusters || DEFAULT_GRAMMAR_CLUSTERS);

  let weakest = clusters[0] || DEFAULT_GRAMMAR_CLUSTERS[0];
  let worstScore = Infinity;

  for (const c of clusters) {
    let lapses = 0;
    let errors = 0;
    let attempts = 0;

    for (const pid of (c.patterns || [])) {
      const gs = stats[`G:${pid}`];
      if (gs) {
        attempts += (gs.correct || 0) + (gs.incorrect || 0);
        errors += (gs.incorrect || 0);
        lapses += (gs.lapses || 0);
      }
    }

    // Lower score indicates weaker performance (high errors / lapses)
    const score = attempts > 0 ? ((attempts - errors - lapses * 2) / attempts) : 0.5;
    if (score < worstScore) {
      worstScore = score;
      weakest = c;
    }
  }

  return weakest;
}

/**
 * Finds next unseen grammar patterns for Step 5
 */
export function findNextGrammarPatterns(db = defaultState, stats = db?.stats || {}, quota = 2) {
  const grammarIndex = db.grammarDB?.index || [];
  const result = [];

  for (const p of grammarIndex) {
    const s = stats[`G:${p.id}`];
    if (!isItemSeen(s)) {
      result.push(p);
      if (result.length >= quota) break;
    }
  }

  return result;
}

/**
 * Finds next reading passage for Step 6 (unseen passage or due second pass)
 */
export function findNextReadingPassage(db = defaultState, stats = db?.stats || {}) {
  const readingDB = db.readingDB || {};
  const now = Date.now();

  // 1. Check for due RP second pass
  for (const key in stats) {
    if (key.startsWith('RP:')) {
      const s = stats[key];
      if (s && s.nextDue && s.nextDue <= now) {
        const passageId = key.slice(3);
        const lesson = readingDB[passageId];
        if (lesson) {
          return {
            id: passageId,
            isSecondPass: true,
            title_ja: lesson.title_ja || lesson.title || passageId,
            title_en: lesson.title_en || '',
            lesson
          };
        }
      }
    }
  }

  // 2. Next unseen lesson
  for (const lid of Object.keys(readingDB)) {
    const lesson = readingDB[lid];
    const qs = lesson.comprehensionQuestions || lesson.questions || [];
    const touched = qs.some(q => {
      const qid = q.id || `${lid}_q${q.questionNumber || 1}`;
      return isItemSeen(stats[`R_Q:${qid}`]);
    });
    if (!touched) {
      return {
        id: lid,
        isSecondPass: false,
        title_ja: lesson.title_ja || lesson.title || lid,
        title_en: lesson.title_en || '',
        lesson
      };
    }
  }

  // Fallback to first lesson
  const firstId = Object.keys(readingDB)[0];
  if (firstId) {
    return {
      id: firstId,
      isSecondPass: false,
      title_ja: readingDB[firstId].title_ja || readingDB[firstId].title || firstId,
      title_en: readingDB[firstId].title_en || '',
      lesson: readingDB[firstId]
    };
  }

  return null;
}

/**
 * Constructs 6–8 mini-check questions based on today's new items (Step 7)
 */
export function buildMiniCheckQuestions(newKanjiWords = [], newVocab = [], newPatterns = []) {
  const questions = [];

  // Kanji reading items (MCQ)
  for (const kw of newKanjiWords.slice(0, 3)) {
    const term = kw.term_ja || kw.term || kw.word;
    const reading = kw.reading || kw.kana;
    if (term && reading) {
      questions.push({
        id: `mc_kw_${term}`,
        type: 'kanji_reading',
        prompt: term,
        question: `「${term}」の正しい読み方はどれですか？`,
        answer: reading,
        options: [reading, `${reading}っ`, `${reading}ん`, reading.slice(0, -1) || reading],
        banner: '問題 1 (漢字の読み)'
      });
    }
  }

  // Vocab meaning items (MCQ)
  for (const v of newVocab.slice(0, 3)) {
    const ja = v.japanese || v.word || v.term_ja;
    const en = v.english || v.meaning_en;
    if (ja && en) {
      questions.push({
        id: `mc_v_${v.id}`,
        type: 'vocab_meaning',
        prompt: ja,
        question: `「${ja}」の意味はどれですか？`,
        answer: en,
        options: [en, 'to prepare thoroughly', 'unexpected situation', 'important document'],
        banner: '問題 2 (言葉の意味)'
      });
    }
  }

  // Grammar decision items
  for (const g of newPatterns.slice(0, 2)) {
    const name = g.pattern_name_ja || g.title_ja || g.name || g.id;
    const meaning = g.meaning_en || g.explanation || 'Expresses core connection';
    questions.push({
      id: `mc_g_${g.id}`,
      type: 'grammar_decision',
      prompt: name,
      question: `文法「${name}」の用法として適切なものはどれですか？`,
      answer: meaning,
      options: [meaning, 'Expresses immediate contrast', 'Indicates gradual change', 'Denotes extreme limit'],
      banner: '問題 3 (文法判断)'
    });
  }

  return questions.slice(0, 8);
}

/**
 * Builds the structured 7-step Daily Session queue (doc 01 §3).
 *
 * @param {Object} [options={}]
 * @returns {Object} Structured daily session with steps 1–7
 */
export function buildDailySession(options = {}) {
  const db = options.state || defaultState;
  const stats = db.stats || {};
  const now = options.now ? new Date(options.now).getTime() : Date.now();
  const dateKey = istDateKey(now);

  let dueTotal = typeof options.dueCount === 'number' ? options.dueCount : null;
  if (dueTotal === null) {
    if (db && db !== defaultState && db.stats) {
      dueTotal = 0;
      for (const k in db.stats) {
        const s = db.stats[k];
        if (s && s.nextDue && s.nextDue <= now) dueTotal++;
      }
    } else {
      dueTotal = getDueItemsCount('all');
    }
  }
  const catchUp = dueTotal > BACKLOG_THRESHOLD || isCatchUpMode();
  const pace = calculatePace(
    {
      vocabTier1: Object.keys(db.vocabDB || {}).length * 10,
      kanjiWords: Object.keys(db.kanjiDB || {}).length,
      grammar: (db.grammarDB?.index || []).length
    },
    options.profile || db.settings?.profile || 'standard',
    options.examDate || EXAM_DATE_ISO,
    { now }
  );

  // Step 1: Review due (ordered, interleaved via srs.getAllDueItems())
  const reviewBatch = options.batchSize || db.dueBatchSize || 20;
  const dueItems = getAllDueItems('all', reviewBatch);
  const totalDue = getDueItemsCount('all');
  const step1EstMinutes = Math.max(1, Math.round(dueItems.length * (SEC_PER_REVIEW || 7) / 60));

  const step1 = {
    step: 1,
    id: 'review-due',
    title: 'Review Due',
    slot: 'morning',
    skippable: false,
    items: dueItems,
    count: dueItems.length,
    dueTotal: totalDue,
    estMinutes: step1EstMinutes,
    description: `Ordered, interleaved spaced repetition reviews (~${step1EstMinutes} min)`
  };

  // Step 2: Weak round: up to 5 weak/leech items
  const weakCandidates = [];
  for (const key in stats) {
    const s = stats[key];
    if (s && (s.isHard || (s.weight || 1.0) >= 1.8 || s.leech)) {
      weakCandidates.push({ key, stats: s });
    }
  }

  // Prioritize leeches first, then highest weight / lapses
  weakCandidates.sort((a, b) => {
    const leechDiff = (b.stats.leech ? 1 : 0) - (a.stats.leech ? 1 : 0);
    if (leechDiff !== 0) return leechDiff;
    const weightDiff = (b.stats.weight || 1.0) - (a.stats.weight || 1.0);
    if (Math.abs(weightDiff) > 1e-4) return weightDiff;
    return (b.stats.lapses || 0) - (a.stats.lapses || 0);
  });

  const weakItems = weakCandidates.slice(0, 5);
  const step2EstMinutes = Math.max(1, Math.ceil(weakItems.length * 15 / 60));

  const step2 = {
    step: 2,
    id: 'weak-round',
    title: 'Weak Round',
    slot: 'morning',
    skippable: true,
    items: weakItems,
    count: weakItems.length,
    estMinutes: step2EstMinutes,
    description: 'Up to 5 struggling items (leeches first)'
  };

  // Step 3: New kanji chunk (3 kanji via kanji-runner)
  const nextChunk = findNextKanjiChunk(db, stats);
  const step3 = {
    step: 3,
    id: 'new-kanji',
    title: 'New Kanji Chunk',
    slot: 'evening',
    skippable: true,
    paused: catchUp,
    lessonNumber: nextChunk.lessonNumber,
    chunkIndex: nextChunk.chunkIndex,
    totalChunks: nextChunk.totalChunks,
    kanji: nextChunk.kanji,
    words: nextChunk.words,
    count: nextChunk.kanji.length,
    estMinutes: 6,
    description: `Lesson ${nextChunk.lessonNumber} · chunk ${nextChunk.chunkIndex + 1} of ${nextChunk.totalChunks} (${nextChunk.kanji.join(' ')})`
  };

  // Step 4: New vocab (Tier 1 core words via vocab_tiers.json)
  const vocabQuota = pace.quotas.vocab || 10;
  const newVocab = findNextVocabBatch(db, stats, vocabQuota);
  const step4EstMinutes = Math.max(1, Math.round(newVocab.length * (SEC_PER_NEW || 30) / 60));

  const step4 = {
    step: 4,
    id: 'new-vocab',
    title: 'New Vocab (Tier 1)',
    slot: 'evening',
    skippable: true,
    paused: catchUp,
    items: newVocab,
    count: newVocab.length,
    quota: vocabQuota,
    estMinutes: step4EstMinutes,
    description: `${newVocab.length} Tier 1 core words`
  };

  // Step 5: New grammar patterns (per quota) + cluster round in weakest cluster
  const grammarQuota = pace.quotas.grammar || 2;
  const newPatterns = findNextGrammarPatterns(db, stats, grammarQuota);
  const weakestCluster = findWeakestGrammarCluster(db, stats);

  const step5 = {
    step: 5,
    id: 'new-grammar',
    title: 'Grammar & Cluster Round',
    slot: 'evening',
    skippable: true,
    paused: catchUp,
    patterns: newPatterns,
    weakestCluster,
    clusterDrillCount: 5,
    count: newPatterns.length + 5,
    quota: grammarQuota,
    estMinutes: 5,
    description: `${newPatterns.length} patterns + 5-card cluster round in ${weakestCluster.name_en || weakestCluster.id}`
  };

  // Step 6: Read one passage
  const nextPassage = findNextReadingPassage(db, stats);
  const step6 = {
    step: 6,
    id: 'reading-passage',
    title: 'Read One Passage',
    slot: 'evening',
    skippable: true,
    paused: catchUp,
    passage: nextPassage,
    count: 1,
    estMinutes: 8,
    description: nextPassage ? `Read passage: ${nextPassage.title_ja}` : 'Read 1 passage'
  };

  // Step 7: Mini-check (6-8 questions on today's new items)
  const miniQuestions = buildMiniCheckQuestions(nextChunk.words, newVocab, newPatterns);
  const step7 = {
    step: 7,
    id: 'mini-check',
    title: 'Mini-Check',
    slot: 'evening',
    skippable: true,
    paused: catchUp,
    questions: miniQuestions,
    count: miniQuestions.length,
    estMinutes: 3,
    description: `${miniQuestions.length} questions on today's new items`
  };

  const steps = [step1, step2, step3, step4, step5, step6, step7];
  const totalEstMinutes = steps.reduce((sum, s) => sum + s.estMinutes, 0);

  return {
    date: dateKey,
    isCatchUp: catchUp,
    totalEstMinutes,
    steps
  };
}

/**
 * Returns checklist status of today's items matching daylog against pace quotas (doc 01 §2).
 *
 * @param {Object} [options={}]
 * @returns {Object} Daily plan status with checklist items and completion flags
 */
export function getDailyPlanStatus(options = {}) {
  const db = options.state || defaultState;
  const dateKey = options.date ? istDateKey(options.date) : istDateKey();
  const dayRecord = options.dayRecord || getDay(dateKey);

  const pace = calculatePace(
    {
      vocabTier1: Object.keys(db.vocabDB || {}).length * 10,
      kanjiWords: Object.keys(db.kanjiDB || {}).length,
      grammar: (db.grammarDB?.index || []).length
    },
    options.profile || db.settings?.profile || 'standard',
    options.examDate || EXAM_DATE_ISO,
    { now: options.now }
  );

  const dueCount = typeof options.dueCount === 'number'
    ? options.dueCount
    : getDueItemsCount('all');

  const quotaKanji = pace.quotas.kanjiWords || 12;
  const quotaVocab = pace.quotas.vocab || 10;
  const quotaGrammar = pace.quotas.grammar || 2;
  const quotaReading = 1;

  const reviewsDoneToday = Number(dayRecord.reviews) || 0;
  const kanjiDoneToday = Number(dayRecord.pillars?.kanji) || 0;
  const vocabDoneToday = Number(dayRecord.pillars?.vocab) || 0;
  const grammarDoneToday = Number(dayRecord.pillars?.grammar) || 0;
  const readingDoneToday = Number(dayRecord.pillars?.reading) || 0;

  // Review status
  const isReviewDone = (dueCount === 0 && reviewsDoneToday > 0) || dueCount === 0;

  // Intake status
  const isKanjiDone = kanjiDoneToday >= quotaKanji || (dayRecord.newCards > 0 && kanjiDoneToday > 0);
  const isVocabDone = vocabDoneToday >= quotaVocab;
  const isGrammarDone = grammarDoneToday >= quotaGrammar;
  const isReadingDone = readingDoneToday >= quotaReading;

  const nextChunk = findNextKanjiChunk(db, db.stats);
  const kanjiDetail = `Lesson ${nextChunk.lessonNumber} · chunk ${nextChunk.chunkIndex + 1} of ${nextChunk.totalChunks}`;

  const nextPassage = findNextReadingPassage(db, db.stats);
  const readingDetail = nextPassage ? nextPassage.title_ja : '1 passage';

  const items = [
    {
      id: 'review',
      title: 'Review due',
      completed: isReviewDone,
      current: reviewsDoneToday,
      target: reviewsDoneToday + dueCount,
      label: dueCount === 0 ? `${reviewsDoneToday}/${reviewsDoneToday}` : `${reviewsDoneToday}/${reviewsDoneToday + dueCount} (${dueCount} due)`,
      handler: 'startDueReview("all")'
    },
    {
      id: 'kanji',
      title: 'New kanji',
      completed: isKanjiDone,
      current: kanjiDoneToday,
      target: quotaKanji,
      detail: kanjiDetail,
      label: `${kanjiDetail} · ${kanjiDoneToday}/${quotaKanji}`,
      handler: `startKanjiRunner(${nextChunk.lessonNumber})`
    },
    {
      id: 'vocab',
      title: 'New vocab',
      completed: isVocabDone,
      current: vocabDoneToday,
      target: quotaVocab,
      detail: `Tier 1 core words`,
      label: `${vocabDoneToday}/${quotaVocab} (Tier 1 core)`,
      handler: 'startLearnNew()'
    },
    {
      id: 'grammar',
      title: 'Grammar',
      completed: isGrammarDone,
      current: grammarDoneToday,
      target: quotaGrammar,
      detail: `${quotaGrammar} patterns`,
      label: `${grammarDoneToday}/${quotaGrammar} patterns`,
      handler: 'showView("grammar")'
    },
    {
      id: 'reading',
      title: 'Read 1 passage',
      completed: isReadingDone,
      current: readingDoneToday,
      target: quotaReading,
      detail: readingDetail,
      label: `${readingDoneToday}/${quotaReading} (${readingDetail})`,
      handler: nextPassage ? `openReadingLesson("${nextPassage.id}")` : 'showView("reading")'
    }
  ];

  const completedCount = items.filter(it => it.completed).length;
  const hasUnfinishedNew = (!isKanjiDone || !isVocabDone || !isGrammarDone || !isReadingDone);
  const allDone = (isReviewDone && isKanjiDone && isVocabDone && isGrammarDone && isReadingDone);

  return {
    date: dateKey,
    items,
    completedCount,
    totalCount: items.length,
    hasUnfinishedNew,
    allDone,
    quotas: {
      kanji: quotaKanji,
      vocab: quotaVocab,
      grammar: quotaGrammar,
      reading: quotaReading
    }
  };
}

/**
 * Dynamic recommendation function for primary hero CTA (doc 01 §2).
 *
 * Decision Tree:
 * 1. If now < 12:00 IST and reviews due -> Morning Review (estimated minutes)
 * 2. Else if plan has unfinished new items -> Evening Intake (next plan item)
 * 3. Else if reviews due -> Review Due
 * 4. Else -> "All caught up! Quick 5?"
 *
 * @param {Object} [options={}]
 * @returns {Object} Primary action recommendation
 */
export function nextBestAction(options = {}) {
  const db = options.state || defaultState;
  const now = options.now ? new Date(options.now) : istNow();
  const istHour = now.getHours(); // proxied to IST hours by time.js istNow()

  const dueCount = typeof options.dueCount === 'number'
    ? options.dueCount
    : getDueItemsCount('all');

  const planStatus = options.planStatus || getDailyPlanStatus({
    state: db,
    now: options.now,
    dueCount
  });

  const estReviewMinutes = Math.max(1, Math.round(dueCount * (SEC_PER_REVIEW || 7) / 60));
  const isMorning = istHour < 12;

  // 1. Morning Review
  if (isMorning && dueCount > 0) {
    return {
      type: 'morning-review',
      title: "Start today's session",
      label: `Review ${dueCount} due · ~${estReviewMinutes} min`,
      subtitle: `Morning review · ${dueCount} due (~${estReviewMinutes} min)`,
      action: 'review',
      target: 'all',
      dueCount,
      estMinutes: estReviewMinutes,
      handler: 'startDueReview("all")'
    };
  }

  // 2. Evening Intake (next plan item)
  if (planStatus.hasUnfinishedNew) {
    // Find first unfinished new item
    const kanjiItem = planStatus.items.find(i => i.id === 'kanji');
    const vocabItem = planStatus.items.find(i => i.id === 'vocab');
    const grammarItem = planStatus.items.find(i => i.id === 'grammar');
    const readingItem = planStatus.items.find(i => i.id === 'reading');

    if (kanjiItem && !kanjiItem.completed) {
      return {
        type: 'evening-intake',
        title: 'Evening: new + drills',
        label: `New kanji chunk (${kanjiItem.target || 3} words)`,
        subtitle: `Evening intake · ${kanjiItem.detail || 'Kanji chunk'}`,
        action: 'kanji',
        target: kanjiItem.id,
        dueCount,
        estMinutes: 6,
        handler: kanjiItem.handler
      };
    }

    if (vocabItem && !vocabItem.completed) {
      return {
        type: 'evening-intake',
        title: 'Evening: new + drills',
        label: `Learn ${vocabItem.target || 10} new words`,
        subtitle: `Evening intake · Tier 1 vocab`,
        action: 'vocab',
        target: vocabItem.id,
        dueCount,
        estMinutes: 5,
        handler: vocabItem.handler
      };
    }

    if (grammarItem && !grammarItem.completed) {
      return {
        type: 'evening-intake',
        title: 'Evening: new + drills',
        label: `New grammar (${grammarItem.target || 2} patterns)`,
        subtitle: `Evening intake · Grammar drills`,
        action: 'grammar',
        target: grammarItem.id,
        dueCount,
        estMinutes: 5,
        handler: grammarItem.handler
      };
    }

    if (readingItem && !readingItem.completed) {
      return {
        type: 'evening-intake',
        title: 'Evening: new + drills',
        label: `Read 1 passage`,
        subtitle: `Evening intake · ${readingItem.detail || 'Passage'}`,
        action: 'reading',
        target: readingItem.id,
        dueCount,
        estMinutes: 8,
        handler: readingItem.handler
      };
    }
  }

  // 3. Review Due (after intake or during afternoon/evening)
  if (dueCount > 0) {
    return {
      type: 'review-due',
      title: 'Review Due',
      label: `Review ${dueCount} due · ~${estReviewMinutes} min`,
      subtitle: `${dueCount} reviews waiting (~${estReviewMinutes} min)`,
      action: 'review',
      target: 'all',
      dueCount,
      estMinutes: estReviewMinutes,
      handler: 'startDueReview("all")'
    };
  }

  // 4. All caught up -> Quick 5
  return {
    type: 'caught-up',
    title: 'All caught up',
    label: 'All caught up! Quick 5?',
    subtitle: 'Stay sharp with 5 quick reviews',
    action: 'quick5',
    target: 'quick5',
    dueCount: 0,
    estMinutes: 2,
    handler: 'startQuick5()'
  };
}

/**
 * Storage helpers for persisting daily session step progress
 */
export function loadDailySessionProgress() {
  if (typeof localStorage === 'undefined') return null;
  try {
    const raw = localStorage.getItem(DAILY_SESSION_STORAGE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch (_) {
    return null;
  }
}

export function saveDailySessionProgress(progress) {
  if (typeof localStorage === 'undefined') return;
  try {
    localStorage.setItem(DAILY_SESSION_STORAGE_KEY, JSON.stringify(progress));
  } catch (_) {}
}

export function clearDailySessionProgress() {
  if (typeof localStorage === 'undefined') return;
  try {
    localStorage.removeItem(DAILY_SESSION_STORAGE_KEY);
  } catch (_) {}
}

export function hasResumableDailySession() {
  const p = loadDailySessionProgress();
  if (!p) return false;
  const today = istDateKey();
  if (p.date !== today) return false;
  return Boolean(p.currentStepIndex > 0 && !p.completed);
}

export const N3Daily = {
  buildDailySession,
  nextBestAction,
  getDailyPlanStatus,
  findNextKanjiChunk,
  findNextVocabBatch,
  findWeakestGrammarCluster,
  findNextReadingPassage,
  buildMiniCheckQuestions,
  loadDailySessionProgress,
  saveDailySessionProgress,
  clearDailySessionProgress,
  hasResumableDailySession
};

if (typeof window !== 'undefined') {
  window.N3Daily = N3Daily;
  window.buildDailySession = buildDailySession;
  window.nextBestAction = nextBestAction;
  window.getDailyPlanStatus = getDailyPlanStatus;
}

export default N3Daily;
