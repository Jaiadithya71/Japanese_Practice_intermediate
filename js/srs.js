/* =======================================================
   NIHONGO INTERMEDIATE — srs.js
   Unified Cross-Pillar SRS Engine & IST Routine Scheduler
   Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §4, §6, §8
   ======================================================= */

import {
  STORAGE_KEY,
  HARD_THRESHOLD,
  MASTERED_THRESHOLD,
  WEIGHT_RIGHT,
  WEIGHT_WRONG,
  WEIGHT_MIN,
  WEIGHT_MAX,
  DEFAULT_EASE_FACTOR,
  IST_SLOT_A_HOUR,
  IST_SLOT_A_MINUTE,
  IST_SLOT_B_HOUR,
  IST_SLOT_B_MINUTE,
  STEPS_DAYS,
  MIN_FIRST_GAP_MS,
  EASE_FLOOR,
  LAPSE_FACTOR,
  LEECH_LAPSES,
  CRITERION_CORRECT,
  EXAM_DATE_ISO,
  HIST_LEN,
  BACKLOG_THRESHOLD
} from './config.js';
import { state } from './state.js';
import { examCapDays } from './planner.js';
import { logActivity } from './daylog.js';

export { examCapDays };

export function loadStats() {
  try {
    state.stats = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
  } catch {
    state.stats = {};
  }
  return state.stats;
}

export function saveStats() {
  try {
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.stats));
    }
  } catch (err) {
    console.error('Failed to save stats to localStorage:', err);
  }
  if (typeof window !== 'undefined' && window.__n3ScheduleSync) {
    try { window.__n3ScheduleSync(); } catch {}
  }
}

/**
 * Align next due time to India Standard Time (IST UTC + 5.5 hours) study slots:
 * Slot A: 7:30 AM IST
 * Slot B: 5:45 PM IST
 */
export function snapToNextDueSlot(ms) {
  const istOffset = 5.5 * 60 * 60 * 1000;
  const istMs = ms + istOffset;
  const d = new Date(istMs);

  const year = d.getUTCFullYear();
  const month = d.getUTCMonth();
  const date = d.getUTCDate();

  const slotAMs = Date.UTC(year, month, date, IST_SLOT_A_HOUR, IST_SLOT_A_MINUTE, 0, 0) - istOffset;
  const slotBMs = Date.UTC(year, month, date, IST_SLOT_B_HOUR, IST_SLOT_B_MINUTE, 0, 0) - istOffset;

  if (ms <= slotAMs) {
    return slotAMs;
  } else if (ms <= slotBMs) {
    return slotBMs;
  } else {
    // Next day Slot A
    return Date.UTC(year, month, date + 1, IST_SLOT_A_HOUR, IST_SLOT_A_MINUTE, 0, 0) - istOffset;
  }
}

/**
 * Returns the pillar identifier for any item key:
 * 'vocab', 'kanji', 'grammar', 'reading', or 'other'.
 */
export function getPillarFromKey(key) {
  if (!key || typeof key !== 'string') return 'other';
  if (key.startsWith('V:') || key.startsWith('VC:')) return 'vocab';
  if (key.startsWith('K:') || key.startsWith('K_EX:') || key.startsWith('KWR:') || key.startsWith('KWW:') || key.startsWith('KWM:')) return 'kanji';
  if (key.startsWith('G:') || key.startsWith('GD:') || key.startsWith('GS:') || key.startsWith('GT:') || key.startsWith('GC:')) return 'grammar';
  if (key.startsWith('R_Q:') || key.startsWith('R_P:') || key.startsWith('RP:')) return 'reading';
  return 'other';
}

/**
 * Returns the facet prefix for any item key (e.g. 'KWR', 'KWW', 'V', 'GD', 'GS', 'GT', 'RP', 'K').
 */
export function getFacetFromKey(key) {
  if (!key || typeof key !== 'string') return '';
  const idx = key.indexOf(':');
  return idx > 0 ? key.slice(0, idx) : key;
}

/**
 * Standardized key generator for any item across the 5 pillars (doc 02 §1.1, §9.4):
 * Vocab: V:v2-01-001 (or V:v2-01-001:rev), VC:v2-01-001:1
 * Kanji Word Reading: KWR:<term>
 * Kanji Word Writing: KWW:<term>
 * Kanji Word Meaning: KWM:<term>
 * Grammar Decision: GD:<part>:<sec>:<qid>
 * Grammar Star: GS:<part>:<sec>:<qid>
 * Grammar Text: GT:<passage_id>:<qid>
 * Grammar Contrast: GC:<patternId>:<n>
 * Reading Passage: RP:<passage_id>
 * Reading Question: R_Q:<qid>
 * Reading Point: R_P:<pid>
 * Kanji: K:<char>
 * Kanji Exercise: K_EX:<id>
 */
export function formatItemKey(item) {
  if (!item) return '';
  if (item.key) return item.key;

  if (item.type === 'vocab' || item.book === 'vocab') {
    const rev = state.studyDirection === 'en-ja' ? ':rev' : '';
    return `V:${item.id}${rev}`;
  }
  if (item.type === 'vocab_collocation' || item.type === 'vc') {
    return `VC:${item.id || item.vocabId}:${item.index || 1}`;
  }
  if (item.type === 'kanji_word_reading' || item.type === 'kwr') {
    return `KWR:${item.term || item.term_ja || item.id}`;
  }
  if (item.type === 'kanji_word_writing' || item.type === 'kww') {
    return `KWW:${item.term || item.term_ja || item.id}`;
  }
  if (item.type === 'kanji_word_meaning' || item.type === 'kwm') {
    return `KWM:${item.term || item.term_ja || item.id}`;
  }
  if (item.type === 'grammar_decision' || item.type === 'gd') {
    return `GD:${item.part || item.partId || 'p1'}:${item.sec || item.sectionId || '1'}:${item.qid || item.id}`;
  }
  if (item.type === 'grammar_star' || item.type === 'gs') {
    return `GS:${item.part || item.partId || 'p1'}:${item.sec || item.sectionId || '1'}:${item.qid || item.id}`;
  }
  if (item.type === 'grammar_text' || item.type === 'gt') {
    return `GT:${item.passage_id || item.passageId || 'p3'}:${item.qid || item.id}`;
  }
  if (item.type === 'grammar_contrast' || item.type === 'gc') {
    return `GC:${item.patternId || item.id}:${item.variantIndex || 1}`;
  }
  if (item.type === 'grammar' || item.book === 'grammar') {
    return `G:${item.id}`;
  }
  if (item.type === 'reading_passage' || item.type === 'reader_passage') {
    return `RP:${item.id || item.passage_id}`;
  }
  if (item.type === 'reading_question' || item.question_ja) {
    return `R_Q:${item.id || item.item_id || item.questionNumber}`;
  }
  if (item.type === 'reading_point') {
    return `R_P:${item.id}`;
  }
  if (item.type === 'kanji' || item.book === 'kanji') {
    return `K:${item.kanji || item.id}`;
  }
  if (item.type === 'kanji_exercise' || item.book === 'kanji_exercise') {
    return `K_EX:${item.id || item.item_id}`;
  }
  return `ITEM:${item.id}`;
}

export function getItemStats(itemKey) {
  if (!state.stats) state.stats = {};
  if (!state.stats[itemKey]) {
    state.stats[itemKey] = {
      correct: 0,
      incorrect: 0,
      weight: 1.0,
      reps: 0,
      interval: 0,
      easeFactor: DEFAULT_EASE_FACTOR,
      nextDue: 0,
      isHard: false,
      lapses: 0,
      streak: 0,
      learnState: 'learning',
      relearnBase: null,
      leech: false,
      firstSeen: 0,
      hist: [],
      note: '',
      cause: ''
    };
  }
  return state.stats[itemKey];
}

export function getItemStatus(itemKey) {
  const s = getItemStats(itemKey);
  if (s.isHard || (s.weight || 1.0) >= HARD_THRESHOLD) {
    return 'hard';
  }
  if (((s.reps >= 4 && (s.interval || 0) >= 21) || (s.correct || 0) >= MASTERED_THRESHOLD) && (s.weight || 1.0) <= 0.8) {
    return 'mastered';
  }
  if ((s.correct || 0) > 0 || (s.incorrect || 0) > 0) {
    return 'learning';
  }
  return 'unseen';
}

// Backwards compatibility for wordId
export function getWordStats(wordId, direction = 'ja-en') {
  const rev = direction === 'en-ja' ? ':rev' : '';
  return getItemStats(`V:${wordId}${rev}`);
}

export function getWordStatus(wordId, direction = 'ja-en') {
  const rev = direction === 'en-ja' ? ':rev' : '';
  return getItemStatus(`V:${wordId}${rev}`);
}

/**
 * Extended SM-2 scheduling engine with 6 early steps, exam capping and leech detection (doc 02 §4.2).
 *
 * @param {string} itemKey
 * @param {number} grade - 1: Again, 2: Hard, 3: Good, 4: Easy
 * @param {Object} [opts={}] - { inSession, now, cause, elapsedMs }
 */
export function updateItemStats(itemKey, grade, opts = {}) {
  const s = getItemStats(itemKey);
  const now = opts.now || Date.now();
  const DAY = 24 * 60 * 60 * 1000;

  // Initialize tracking fields for legacy records without mutating unrelated disk records
  s.lastSeen = now;
  if (!s.firstSeen) s.firstSeen = now;

  s.hist = Array.isArray(s.hist) ? s.hist : [];
  s.hist.push([now, grade]);
  if (s.hist.length > HIST_LEN) {
    s.hist = s.hist.slice(-HIST_LEN);
  }

  // Clamp ease factor on read: heals old 1.3 values (doc 02 §4.2, ME-8)
  s.easeFactor = Math.max(EASE_FLOOR, Number(s.easeFactor) || DEFAULT_EASE_FACTOR);

  if (grade === 1) { // Again / Lapse
    const wasPassed = (s.reps || 0) > 0;
    s.incorrect = (s.incorrect || 0) + 1;
    s.lapses = (s.lapses || 0) + (wasPassed ? 1 : 0);
    s.weight = Math.min(WEIGHT_MAX, (s.weight || 1.0) * WEIGHT_WRONG);
    s.streak = 0;
    s.learnState = wasPassed ? 'relearning' : 'learning';
    s.relearnBase = wasPassed ? Math.max(2, Math.round((s.interval || 1) * LAPSE_FACTOR)) : null;
    s.reps = 0;
    s.interval = 1;
    s.easeFactor = Math.max(EASE_FLOOR, s.easeFactor - 0.2);
    s.nextDue = snapToNextDueSlot(now + 10 * 60 * 1000); // 10 min

    if ((s.lapses || 0) >= LEECH_LAPSES) {
      s.leech = true;
    }
    if (opts.cause) {
      s.cause = opts.cause;
    }
  } else { // Correct (grade >= 2)
    s.correct = (s.correct || 0) + 1;
    s.streak = (s.streak || 0) + 1;

    const currentLearnState = s.learnState || ((s.reps || 0) > 0 ? 'review' : 'learning');
    if ((currentLearnState === 'learning' || currentLearnState === 'relearning') &&
        s.streak < CRITERION_CORRECT &&
        opts.inSession) {
      // Still inside the learn-to-criterion loop: do NOT advance interval, just stay in loop
      saveStats();
      updateSidebarStats();
      return;
    }

    // Graduate to review
    s.learnState = 'review';
    s.reps = (s.reps || 0) + 1;

    const prevInterval = s.interval || 0;
    let interval;

    if (s.relearnBase && (s.reps - 1) === 0) {
      interval = s.relearnBase;
      s.relearnBase = null;
    } else {
      let idx = s.reps - 1;
      if (grade === 4) { // Easy skips a step
        idx += 1;
        s.reps += 1;
      }
      if (idx < STEPS_DAYS.length) {
        interval = STEPS_DAYS[idx];
      } else {
        interval = Math.round(Math.max(1, prevInterval) * (s.easeFactor || DEFAULT_EASE_FACTOR));
      }
    }

    // Grade adjustments
    if (grade === 2) { // Hard
      interval = Math.max(1, Math.max(prevInterval, Math.round((prevInterval || 1) * 1.2)));
      s.easeFactor = Math.max(EASE_FLOOR, (s.easeFactor || DEFAULT_EASE_FACTOR) - 0.15);
      s.weight = Math.max(WEIGHT_MIN, (s.weight || 1.0) * 0.9);
      s.reps = Math.max(1, s.reps - 1); // reps not advanced past current step
    } else if (grade === 3) { // Good
      s.weight = Math.max(WEIGHT_MIN, (s.weight || 1.0) * WEIGHT_RIGHT);
    } else if (grade === 4) { // Easy
      s.easeFactor = (s.easeFactor || DEFAULT_EASE_FACTOR) + 0.15;
      s.weight = Math.max(WEIGHT_MIN, (s.weight || 1.0) * 0.6);
    }

    // Apply exam cap (doc 02 §4.3, ME-7)
    const cap = examCapDays(now);
    if (interval > 0) {
      interval = Math.min(interval, cap);
    }
    s.interval = interval;

    // Snap nextDue
    if (interval === 0) {
      s.nextDue = snapToNextDueSlot(now + MIN_FIRST_GAP_MS);
    } else {
      s.nextDue = snapToNextDueSlot(now + (interval * DAY));
    }
  }

  saveStats();
  updateSidebarStats();

  try {
    const pillar = getPillarFromKey(itemKey);
    logActivity({
      pillar,
      type: 'review',
      count: 1,
      isNew: false,
      ms: opts.elapsedMs,
      wrong: grade === 1 ? 1 : 0
    });
  } catch {
    // Graceful fallback if daylog is unavailable
  }
}

// Backwards compatibility for wordId
export function updateWordStats(wordId, grade, direction = 'ja-en', opts = {}) {
  const rev = direction === 'en-ja' ? ':rev' : '';
  updateItemStats(`V:${wordId}${rev}`, grade, opts);
}

export function toggleWordHard(wordId, direction = 'ja-en') {
  const rev = direction === 'en-ja' ? ':rev' : '';
  return toggleItemHard(`V:${wordId}${rev}`);
}

export function toggleItemHard(itemKey) {
  const s = getItemStats(itemKey);
  s.isHard = !s.isHard;
  s.lastSeen = Date.now();
  if (s.isHard) {
    s.weight = Math.max(s.weight || 1.0, HARD_THRESHOLD);
  }
  saveStats();
  updateSidebarStats();
  return s.isHard;
}

export function getKanjiStatus(char) {
  return getItemStatus(`K:${char}`);
}

export function toggleKanjiHard(char) {
  return toggleItemHard(`K:${char}`);
}

/**
 * Checks whether catch-up mode is triggered (> 80 items due) (doc 02 §6.2, ME-10).
 */
export function isCatchUpMode() {
  return getDueItemsCount('all') > BACKLOG_THRESHOLD;
}

/**
 * Unlocking rules for item facets per doc 02 §1.1 & §2.1 (ME-4, ME-5)
 * - KWR: unlocked at learn time
 * - KWW: unlocked when KWR has reps >= 2
 * - KWM: unlocked at learn time ONLY if word is not in vocab DB (shared meaning with V:)
 */
export function isFacetUnlocked(key, stats = state.stats, vocabOverlapTerms = null) {
  if (!key || typeof key !== 'string') return false;
  if (key.startsWith('KWW:')) {
    const term = key.slice(4);
    const kwrKey = `KWR:${term}`;
    const kwrStats = stats?.[kwrKey];
    return Boolean(kwrStats && (kwrStats.reps || 0) >= 2);
  }
  if (key.startsWith('KWM:')) {
    const term = key.slice(4);
    if (vocabOverlapTerms && (vocabOverlapTerms.has?.(term) || vocabOverlapTerms[term])) {
      return false;
    }
    if (state.idx?.words?.[term]?.vocabId) {
      return false;
    }
    return true;
  }
  return true;
}

/**
 * Determines whether a term's meaning card is credited to V: or KWM: (doc 02 §1.1, ME-5).
 */
export function getMeaningFacetKey(term) {
  if (state.idx?.words?.[term]?.vocabId) {
    return `V:${state.idx.words[term].vocabId}`;
  }
  return `KWM:${term}`;
}

// =======================================================
// OMNI-REVIEW & MULTI-BOOK DUE ITEMS
// =======================================================

export function getDueItemsCount(pillar = 'all') {
  const now = Date.now();
  let count = 0;
  if (!state.stats) return 0;

  for (const key in state.stats) {
    const s = state.stats[key];
    if (!s || !s.nextDue || s.nextDue > now) continue;

    const itemPillar = getPillarFromKey(key);
    if (pillar === 'all' || pillar === itemPillar) {
      count++;
    }
  }

  return count;
}

/**
 * Sorts due candidates according to doc 02 §6.1:
 * 1. learnState in (learning, relearning)
 * 2. overdueRatio = (now - nextDue) / max(1, interval * DAY)
 * 3. weight (higher = weaker)
 */
function compareDueCandidates(a, b, now, catchUp = false) {
  const sa = a.stats;
  const sb = b.stats;
  const DAY = 24 * 60 * 60 * 1000;

  const intA = Math.max(1, (sa.interval || 0) * DAY);
  const intB = Math.max(1, (sb.interval || 0) * DAY);
  const overdueRatioA = (now - (sa.nextDue || now)) / intA;
  const overdueRatioB = (now - (sb.nextDue || now)) / intB;

  if (catchUp) {
    // Catch-up mode: strict overdueRatio ordering
    if (Math.abs(overdueRatioA - overdueRatioB) > 1e-6) {
      return overdueRatioB - overdueRatioA;
    }
  }

  // 1. Fresh/short-interval first
  const isLearningA = (sa.learnState === 'learning' || sa.learnState === 'relearning' || (!sa.learnState && (sa.reps || 0) === 0)) ? 1 : 0;
  const isLearningB = (sb.learnState === 'learning' || sb.learnState === 'relearning' || (!sb.learnState && (sb.reps || 0) === 0)) ? 1 : 0;
  if (isLearningA !== isLearningB) {
    return isLearningB - isLearningA;
  }

  // 2. overdueRatio descending
  if (Math.abs(overdueRatioA - overdueRatioB) > 1e-6) {
    return overdueRatioB - overdueRatioA;
  }

  // 3. weight descending
  const weightA = sa.weight !== undefined ? sa.weight : 1.0;
  const weightB = sb.weight !== undefined ? sb.weight : 1.0;
  if (Math.abs(weightA - weightB) > 1e-6) {
    return weightB - weightA;
  }

  return 0;
}

/**
 * Interleaves candidates so no more than maxConsecutive items share the same facet while alternatives exist (doc 02 §6.1, ME-9).
 */
export function interleaveQueue(candidates, maxConsecutive = 3) {
  const result = [];
  const remaining = [...candidates];

  while (remaining.length > 0) {
    const len = result.length;
    let forbiddenFacet = null;

    if (len >= maxConsecutive) {
      const lastFacet = result[len - 1].facet;
      let allSame = true;
      for (let i = 1; i < maxConsecutive; i++) {
        if (result[len - 1 - i].facet !== lastFacet) {
          allSame = false;
          break;
        }
      }
      if (allSame) {
        forbiddenFacet = lastFacet;
      }
    }

    let pickIndex = -1;
    if (forbiddenFacet !== null) {
      for (let i = 0; i < remaining.length; i++) {
        if (remaining[i].facet !== forbiddenFacet) {
          pickIndex = i;
          break;
        }
      }
    }

    if (pickIndex === -1) {
      pickIndex = 0;
    }

    result.push(remaining.splice(pickIndex, 1)[0]);
  }

  return result;
}

/**
 * Resolves or constructs a rich item object for a due item key.
 */
function resolveItemForKey(key, stats) {
  const facet = getFacetFromKey(key);
  const pillar = getPillarFromKey(key);

  if (facet === 'V') {
    const id = key.replace(/^V:/, '').replace(/:rev$/, '');
    for (const chId in (state.vocabDB || {})) {
      const w = (state.vocabDB[chId] || []).find(item => item.id === id);
      if (w) return { ...w, type: 'vocab', key, book: 'vocab', stats, facet, pillar };
    }
    return { id, key, type: 'vocab', book: 'vocab', stats, facet, pillar };
  }

  if (facet === 'VC') {
    return { id: key, key, type: 'vocab_collocation', book: 'vocab', stats, facet, pillar };
  }

  if (facet === 'K') {
    const char = key.replace(/^K:/, '');
    const k = state.kanjiDB?.[char];
    if (k) return { ...k, id: char, kanji: char, type: 'kanji', key, book: 'kanji', stats, facet, pillar };
    return { id: char, kanji: char, type: 'kanji', key, book: 'kanji', stats, facet, pillar };
  }

  if (facet === 'K_EX') {
    const exId = key.replace(/^K_EX:/, '');
    for (const lNum in (state.kanjiExercisesDB || {})) {
      for (const ex of (state.kanjiExercisesDB[lNum] || [])) {
        const it = (ex.items || []).find(item => item.id === exId);
        if (it) return { ...it, exercise_title: ex.title_ja, type: 'kanji_exercise', key, book: 'kanji_exercise', stats, facet, pillar };
      }
    }
    return { id: exId, type: 'kanji_exercise', key, book: 'kanji_exercise', stats, facet, pillar };
  }

  if (facet === 'KWR' || facet === 'KWW' || facet === 'KWM') {
    const term = key.slice(facet.length + 1);
    const wordData = state.idx?.words?.[term] || {};
    const typeMap = {
      KWR: 'kanji_word_reading',
      KWW: 'kanji_word_writing',
      KWM: 'kanji_word_meaning'
    };
    return {
      term,
      term_ja: term,
      id: term,
      ...wordData,
      type: typeMap[facet],
      key,
      book: 'kanji',
      stats,
      facet,
      pillar
    };
  }

  if (facet === 'R_Q') {
    const qId = key.replace(/^R_Q:/, '');
    for (const lid in (state.readingDB || {})) {
      const lesson = state.readingDB[lid] || {};
      const questions = lesson.comprehensionQuestions || lesson.questions || [];
      const q = questions.find(item => (item.id || `${lid}_q${item.questionNumber || 1}`) === qId);
      if (q) {
        return {
          ...q,
          id: qId,
          lessonId: lid,
          lessonTitle: lesson.title_ja || lesson.title,
          type: 'reading_question',
          key,
          book: 'reading',
          stats,
          facet,
          pillar
        };
      }
    }
    return { id: qId, type: 'reading_question', key, book: 'reading', stats, facet, pillar };
  }

  if (facet === 'RP') {
    const pId = key.replace(/^RP:/, '');
    const lesson = state.readingDB?.[pId] || {};
    return {
      id: pId,
      passage_id: pId,
      lessonTitle: lesson.title_ja || lesson.title,
      type: 'reading_passage',
      key,
      book: 'reading',
      stats,
      facet,
      pillar
    };
  }

  if (facet === 'R_P') {
    return { id: key.replace(/^R_P:/, ''), type: 'reading_point', key, book: 'reading', stats, facet, pillar };
  }

  if (facet === 'GD') {
    return { id: key, type: 'grammar_decision', key, book: 'grammar', stats, facet, pillar };
  }

  if (facet === 'GS') {
    return { id: key, type: 'grammar_star', key, book: 'grammar', stats, facet, pillar };
  }

  if (facet === 'GT') {
    return { id: key, type: 'grammar_text', key, book: 'grammar', stats, facet, pillar };
  }

  if (facet === 'GC') {
    return { id: key, type: 'grammar_contrast', key, book: 'grammar', stats, facet, pillar };
  }

  if (facet === 'G') {
    return { id: key.replace(/^G:/, ''), type: 'grammar', key, book: 'grammar', stats, facet, pillar };
  }

  return { id: key, key, type: 'item', stats, facet, pillar };
}

/**
 * Returns prioritized and interleaved due review items (doc 02 §6.1, ME-9, ME-10).
 */
export function getAllDueItems(pillar = 'all', limit = 20) {
  const now = Date.now();
  const pool = [];
  if (!state.stats) return [];

  for (const key in state.stats) {
    const s = state.stats[key];
    if (!s || !s.nextDue || s.nextDue > now) continue;

    const itemPillar = getPillarFromKey(key);
    if (pillar !== 'all' && pillar !== itemPillar) continue;

    const resolved = resolveItemForKey(key, s);
    pool.push(resolved);
  }

  const catchUp = isCatchUpMode();

  // 1. Priority sort
  pool.sort((a, b) => compareDueCandidates(a, b, now, catchUp));

  // 2. Interleave facets (never more than 3 consecutive)
  const interleaved = interleaveQueue(pool, 3);

  // 3. Batch sizing & Catch-up mode per-session cap (40 cards)
  if (limit === 'all') {
    return catchUp ? interleaved.slice(0, 40) : interleaved;
  }

  const requestedLimit = parseInt(limit, 10) || 20;
  const effectiveLimit = catchUp ? Math.min(requestedLimit, 40) : requestedLimit;
  return interleaved.slice(0, effectiveLimit);
}

export function updateSidebarStats() {
  if (typeof document === 'undefined') return;

  let mastered = 0, learning = 0, hard = 0, unseen = 0;

  // Track Vocabulary
  for (const chId in (state.vocabDB || {})) {
    for (const w of (state.vocabDB[chId] || [])) {
      const st = getWordStatus(w.id, state.studyDirection);
      if (st === 'mastered') mastered++;
      else if (st === 'hard') hard++;
      else if (st === 'learning') learning++;
      else unseen++;
    }
  }

  // Track Reading Questions
  for (const lid in (state.readingDB || {})) {
    const lesson = state.readingDB[lid] || {};
    const questions = lesson.comprehensionQuestions || lesson.questions || [];
    for (const q of questions) {
      const qId = q.id || `${lid}_q${q.questionNumber || 1}`;
      const st = getItemStatus(`R_Q:${qId}`);
      if (st === 'mastered') mastered++;
      else if (st === 'hard') hard++;
      else if (st === 'learning') learning++;
      else unseen++;
    }
  }

  // Track Kanji Target Characters
  for (const char in (state.kanjiDB || {})) {
    const st = getItemStatus(`K:${char}`);
    if (st === 'mastered') mastered++;
    else if (st === 'hard') hard++;
    else if (st === 'learning') learning++;
    else unseen++;
  }

  const elM = document.getElementById('sb-mastered');
  const elL = document.getElementById('sb-learning');
  const elH = document.getElementById('sb-struggling');
  const elU = document.getElementById('sb-unseen');
  const elBadgeH = document.getElementById('hard-count-badge');

  if (elM) elM.textContent = mastered;
  if (elL) elL.textContent = learning;
  if (elH) elH.textContent = hard;
  if (elU) elU.textContent = unseen;

  if (elBadgeH) {
    elBadgeH.textContent = hard;
    elBadgeH.classList.toggle('hide', hard === 0);
  }

  const dueEl = document.getElementById('due-count-num');
  if (dueEl) {
    dueEl.textContent = getDueItemsCount('all');
  }

  const dueVocab = getDueItemsCount('vocab');
  const dueReading = getDueItemsCount('reading');
  const dueKanji = getDueItemsCount('kanji');
  const dueGrammar = getDueItemsCount('grammar');

  const subText = document.getElementById('due-breakdown-sub');
  if (subText) {
    subText.textContent = `${dueVocab} Vocab · ${dueReading} Reading · ${dueKanji} Kanji · ${dueGrammar} Grammar`;
  }
}
