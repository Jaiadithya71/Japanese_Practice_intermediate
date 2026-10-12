/* =======================================================
   NIHONGO INTERMEDIATE — srs.js
   Unified Cross-Pillar SRS Engine & IST Routine Scheduler
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
  IST_SLOT_B_MINUTE
} from './config.js';
import { state } from './state.js';

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
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state.stats));
  } catch (err) {
    console.error('Failed to save stats to localStorage:', err);
  }
  if (typeof window !== 'undefined' && window.__n3ScheduleSync) window.__n3ScheduleSync();
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
 * Standardized key generator for any item across the 5 pillars:
 * Vocab: V:v2-01-001 (or V:v2-01-001:rev)
 * Reading Question: R_Q:dokkai-n3-p4-49_q1
 * Reading Rule: R_P:dokkai-n3-p1-01
 * Grammar: G:bunpou-n3-01
 * Kanji: K:kanji-n3-01
 */
export function formatItemKey(item) {
  if (item.key) return item.key;
  if (item.type === 'vocab' || item.book === 'vocab') {
    const rev = state.studyDirection === 'en-ja' ? ':rev' : '';
    return `V:${item.id}${rev}`;
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
  if (!state.stats[itemKey]) {
    state.stats[itemKey] = {
      correct: 0,
      incorrect: 0,
      weight: 1.0,
      reps: 0,
      interval: 0,
      easeFactor: DEFAULT_EASE_FACTOR,
      nextDue: 0,
      isHard: false
    };
  }
  return state.stats[itemKey];
}

export function getItemStatus(itemKey) {
  const s = getItemStats(itemKey);
  if (s.isHard || (s.weight || 1.0) >= HARD_THRESHOLD) {
    return 'hard';
  }
  if ((s.correct || 0) >= MASTERED_THRESHOLD && (s.weight || 1.0) <= 0.8) {
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

export function updateItemStats(itemKey, grade) {
  const s = getItemStats(itemKey);
  const now = Date.now();
  s.lastSeen = now;

  if (grade === 1) { // Again / Missed
    s.incorrect = (s.incorrect || 0) + 1;
    s.weight = Math.min(WEIGHT_MAX, (s.weight || 1.0) * WEIGHT_WRONG);
    s.reps = 0;
    s.interval = 1;
    s.easeFactor = Math.max(1.3, (s.easeFactor || DEFAULT_EASE_FACTOR) - 0.2);
    s.nextDue = snapToNextDueSlot(now + 10 * 60 * 1000);
  } else { // Correct
    s.correct = (s.correct || 0) + 1;
    s.reps = (s.reps || 0) + 1;

    if (grade === 2) { // Hard
      s.weight = Math.max(WEIGHT_MIN, (s.weight || 1.0) * 0.9);
      s.interval = Math.max(1, Math.round((s.interval || 1) * 1.2));
      s.easeFactor = Math.max(1.3, (s.easeFactor || DEFAULT_EASE_FACTOR) - 0.15);
    } else if (grade === 3) { // Good
      s.weight = Math.max(WEIGHT_MIN, (s.weight || 1.0) * WEIGHT_RIGHT);
      if (s.reps === 1) {
        s.interval = 1;
      } else if (s.reps === 2) {
        s.interval = 6;
      } else {
        s.interval = Math.round((s.interval || 6) * (s.easeFactor || DEFAULT_EASE_FACTOR));
      }
    } else if (grade === 4) { // Easy
      s.weight = Math.max(WEIGHT_MIN, (s.weight || 1.0) * 0.6);
      s.easeFactor = (s.easeFactor || DEFAULT_EASE_FACTOR) + 0.15;
      s.interval = Math.max(4, Math.round(((s.interval || 1) + 2) * (s.easeFactor || DEFAULT_EASE_FACTOR)));
    }

    const nextDueRaw = now + (s.interval * 24 * 60 * 60 * 1000);
    s.nextDue = snapToNextDueSlot(nextDueRaw);
  }

  saveStats();
  updateSidebarStats();
}

// Backwards compatibility for wordId
export function updateWordStats(wordId, grade, direction = 'ja-en') {
  const rev = direction === 'en-ja' ? ':rev' : '';
  updateItemStats(`V:${wordId}${rev}`, grade);
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

// =======================================================
// OMNI-REVIEW & MULTI-BOOK DUE ITEMS
// =======================================================

export function getDueItemsCount(pillar = 'all') {
  const now = Date.now();
  let count = 0;

  // Book 1: Vocabulary
  if (pillar === 'all' || pillar === 'vocab') {
    for (const chId in state.vocabDB) {
      for (const w of state.vocabDB[chId]) {
        const key = `V:${w.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
        const s = state.stats[key];
        if (s && s.nextDue && s.nextDue <= now) count++;
      }
    }
  }

  // Book 2: Reading Questions & Points
  if (pillar === 'all' || pillar === 'reading') {
    for (const lid in state.readingDB) {
      const lesson = state.readingDB[lid];
      const questions = lesson.comprehensionQuestions || lesson.questions || [];
      for (const q of questions) {
        const qId = q.id || `${lid}_q${q.questionNumber || 1}`;
        const key = `R_Q:${qId}`;
        const s = state.stats[key];
        if (s && s.nextDue && s.nextDue <= now) count++;
      }
    }
  }

  // Book 4: Kanji Target & Exercises
  if (pillar === 'all' || pillar === 'kanji') {
    for (const char in state.kanjiDB) {
      const key = `K:${char}`;
      const s = state.stats[key];
      if (s && s.nextDue && s.nextDue <= now) count++;
    }
    for (const lNum in state.kanjiExercisesDB) {
      for (const ex of state.kanjiExercisesDB[lNum]) {
        for (const it of (ex.items || [])) {
          const key = `K_EX:${it.id}`;
          const s = state.stats[key];
          if (s && s.nextDue && s.nextDue <= now) count++;
        }
      }
    }
  }

  return count;
}

export function getAllDueItems(pillar = 'all', limit = 20) {
  const now = Date.now();
  const pool = [];

  // Book 1: Vocabulary
  if (pillar === 'all' || pillar === 'vocab') {
    for (const chId in state.vocabDB) {
      for (const w of state.vocabDB[chId]) {
        const key = `V:${w.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
        const s = state.stats[key];
        if (s && s.nextDue && s.nextDue <= now) {
          pool.push({ ...w, type: 'vocab', key, book: 'vocab' });
        }
      }
    }
  }

  // Book 2: Reading Questions
  if (pillar === 'all' || pillar === 'reading') {
    for (const lid in state.readingDB) {
      const lesson = state.readingDB[lid];
      const questions = lesson.comprehensionQuestions || lesson.questions || [];
      for (const q of questions) {
        const qId = q.id || `${lid}_q${q.questionNumber || 1}`;
        const key = `R_Q:${qId}`;
        const s = state.stats[key];
        if (s && s.nextDue && s.nextDue <= now) {
          pool.push({
            ...q,
            id: qId,
            lessonId: lid,
            lessonTitle: lesson.title_ja || lesson.title,
            type: 'reading_question',
            key,
            book: 'reading'
          });
        }
      }
    }
  }

  // Book 4: Kanji Target & Exercises
  if (pillar === 'all' || pillar === 'kanji') {
    for (const char in state.kanjiDB) {
      const k = state.kanjiDB[char];
      const key = `K:${char}`;
      const s = state.stats[key];
      if (s && s.nextDue && s.nextDue <= now) {
        pool.push({
          ...k,
          id: char,
          kanji: char,
          type: 'kanji',
          key,
          book: 'kanji'
        });
      }
    }
    for (const lNum in state.kanjiExercisesDB) {
      for (const ex of state.kanjiExercisesDB[lNum]) {
        for (const it of (ex.items || [])) {
          const key = `K_EX:${it.id}`;
          const s = state.stats[key];
          if (s && s.nextDue && s.nextDue <= now) {
            pool.push({
              ...it,
              exercise_title: ex.title_ja,
              type: 'kanji_exercise',
              key,
              book: 'kanji_exercise'
            });
          }
        }
      }
    }
  }

  pool.sort(() => Math.random() - 0.5);
  return limit === 'all' ? pool : pool.slice(0, parseInt(limit, 10));
}

export function updateSidebarStats() {
  let mastered = 0, learning = 0, hard = 0, unseen = 0;

  // Track Vocabulary
  for (const chId in state.vocabDB) {
    for (const w of state.vocabDB[chId]) {
      const st = getWordStatus(w.id, state.studyDirection);
      if (st === 'mastered') mastered++;
      else if (st === 'hard') hard++;
      else if (st === 'learning') learning++;
      else unseen++;
    }
  }

  // Track Reading Questions
  for (const lid in state.readingDB) {
    const lesson = state.readingDB[lid];
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
  for (const char in state.kanjiDB) {
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
  const subText = document.getElementById('due-breakdown-sub');
  if (subText) {
    subText.textContent = `${dueVocab} Vocab · ${dueReading} Reading · ${dueKanji} Kanji`;
  }
}
