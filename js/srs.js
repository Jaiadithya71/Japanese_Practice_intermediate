/* =======================================================
   NIHONGO INTERMEDIATE — srs.js
   Spaced Repetition System (SRS) & IST Routine Scheduler
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

export function getWordKey(wordId, direction = 'ja-en') {
  const rev = direction === 'en-ja' ? ':rev' : '';
  return `W:${wordId}${rev}`;
}

export function getWordStats(wordId, direction = 'ja-en') {
  const key = getWordKey(wordId, direction);
  if (!state.stats[key]) {
    state.stats[key] = {
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
  return state.stats[key];
}

export function getWordStatus(wordId, direction = 'ja-en') {
  const s = getWordStats(wordId, direction);
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

/**
 * Grade 1 (Again), 2 (Hard), 3 (Good), 4 (Easy)
 */
export function updateWordStats(wordId, grade, direction = 'ja-en') {
  const s = getWordStats(wordId, direction);
  const now = Date.now();

  if (grade === 1) { // Again / Wrong
    s.incorrect = (s.incorrect || 0) + 1;
    s.weight = Math.min(WEIGHT_MAX, (s.weight || 1.0) * WEIGHT_WRONG);
    s.reps = 0;
    s.interval = 1; // 1 day
    s.easeFactor = Math.max(1.3, (s.easeFactor || DEFAULT_EASE_FACTOR) - 0.2);
    s.nextDue = snapToNextDueSlot(now + 10 * 60 * 1000); // 10 mins or next slot
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

export function toggleWordHard(wordId, direction = 'ja-en') {
  const s = getWordStats(wordId, direction);
  s.isHard = !s.isHard;
  if (s.isHard) {
    s.weight = Math.max(s.weight || 1.0, HARD_THRESHOLD);
  }
  saveStats();
  updateSidebarStats();
  return s.isHard;
}

export function getDueWordsCount() {
  const now = Date.now();
  let count = 0;
  for (const chId in state.vocabDB) {
    for (const w of state.vocabDB[chId]) {
      const s = getWordStats(w.id, state.studyDirection);
      if (s.nextDue && s.nextDue <= now) {
        count++;
      }
    }
  }
  return count;
}

export function updateSidebarStats() {
  let mastered = 0, learning = 0, hard = 0, unseen = 0;

  for (const chId in state.vocabDB) {
    for (const w of state.vocabDB[chId]) {
      const st = getWordStatus(w.id, state.studyDirection);
      if (st === 'mastered') mastered++;
      else if (st === 'hard') hard++;
      else if (st === 'learning') learning++;
      else unseen++;
    }
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
    dueEl.textContent = getDueWordsCount();
  }
}
