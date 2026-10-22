/* =======================================================
   NIHONGO INTERMEDIATE — daylog.js
   Activity Logging, Consecutive Streak & 30-Day Heatmap
   Storage key: nihongo_intermediate_daylog_v1
   ======================================================= */

import {
  istNow,
  istDateKey,
  istDayStart,
  daysBetween
} from './time.js';

export const DAYLOG_STORAGE_KEY = 'nihongo_intermediate_daylog_v1';

// In-memory fallback for environments without localStorage (e.g. Node tests without mock)
let memoryStore = {};

function getStorage() {
  if (typeof localStorage !== 'undefined') {
    return localStorage;
  }
  if (typeof window !== 'undefined' && window.localStorage) {
    return window.localStorage;
  }
  return null;
}

/**
 * Creates an empty daily record shape matching specification:
 * { date: 'YYYY-MM-DD', reviews: 0, newCards: 0, minutes: 0, pillars: { vocab: 0, kanji: 0, grammar: 0, reading: 0 } }
 */
export function createEmptyDayRecord(dateKey = istDateKey()) {
  return {
    date: dateKey,
    reviews: 0,
    newCards: 0,
    minutes: 0,
    pillars: {
      vocab: 0,
      kanji: 0,
      grammar: 0,
      reading: 0
    }
  };
}

/**
 * Normalises pillar strings to standard keys: 'vocab', 'kanji', 'grammar', 'reading'.
 */
function normalizePillar(pillar) {
  if (!pillar || typeof pillar !== 'string') return null;
  const p = pillar.trim().toLowerCase();
  if (p === 'vocab' || p === 'vocabulary' || p === 'words') return 'vocab';
  if (p === 'kanji') return 'kanji';
  if (p === 'grammar' || p === 'bunpou') return 'grammar';
  if (p === 'reading' || p === 'dokkai') return 'reading';
  return null;
}

/**
 * Loads entire daylog dictionary from localStorage or memory store.
 */
export function loadDaylog() {
  const storage = getStorage();
  if (storage) {
    try {
      const raw = storage.getItem(DAYLOG_STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      console.warn('Failed to parse daylog from storage:', e);
      return {};
    }
  }
  return { ...memoryStore };
}

/**
 * Saves daylog dictionary to localStorage or memory store.
 */
export function saveDaylog(data) {
  const storage = getStorage();
  if (storage) {
    try {
      storage.setItem(DAYLOG_STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
      console.warn('Failed to save daylog to storage:', e);
    }
  } else {
    memoryStore = { ...data };
  }
}

/**
 * Clears the daylog from storage and memory (useful for tests and resets).
 */
export function clearDaylog() {
  memoryStore = {};
  const storage = getStorage();
  if (storage) {
    try {
      storage.removeItem(DAYLOG_STORAGE_KEY);
    } catch (e) {
      // ignore
    }
  }
}

/**
 * Returns the daylog entry for dateKey (or today in IST if omitted).
 * Returns complete record shape even if uninitialized.
 */
export function getDay(dateKey) {
  const key = dateKey ? istDateKey(dateKey) : istDateKey();
  const daylog = loadDaylog();
  const raw = daylog[key];
  if (!raw) {
    return createEmptyDayRecord(key);
  }
  return {
    date: key,
    reviews: Number(raw.reviews) || 0,
    newCards: Number(raw.newCards || raw.new) || 0,
    minutes: Number(raw.minutes) || 0,
    pillars: {
      vocab: Number(raw.pillars?.vocab) || 0,
      kanji: Number(raw.pillars?.kanji) || 0,
      grammar: Number(raw.pillars?.grammar) || 0,
      reading: Number(raw.pillars?.reading) || 0
    },
    ...(raw.wrong !== undefined ? { wrong: Number(raw.wrong) || 0 } : {})
  };
}

/**
 * Increments today's activity log safely.
 *
 * @param {Object} options
 * @param {string} [options.pillar] - 'vocab' | 'kanji' | 'grammar' | 'reading'
 * @param {string} [options.type] - 'review' | 'reviews' | 'new' | 'newCards'
 * @param {number} [options.count=1] - Number of items completed
 * @param {number} [options.minutes=0] - Study time in minutes
 * @param {boolean} [options.isNew=false] - If true, increments newCards instead of reviews
 * @param {number} [options.ms] - Card duration in ms (capped at 60s per card, added to minutes)
 * @param {number} [options.wrong] - Number of wrong attempts (optional)
 * @param {string|number|Date} [options.date] - Optional date override (defaults to today IST)
 * @returns {Object} The updated day record
 */
export function logActivity(options = {}) {
  const {
    pillar,
    type = 'review',
    count = 1,
    minutes = 0,
    isNew = false,
    date,
    ms,
    wrong
  } = options;

  const dateKey = date ? istDateKey(date) : istDateKey();
  const daylog = loadDaylog();

  if (!daylog[dateKey]) {
    daylog[dateKey] = createEmptyDayRecord(dateKey);
  }

  const record = daylog[dateKey];
  record.date = dateKey;
  record.reviews = Number(record.reviews) || 0;
  record.newCards = Number(record.newCards || record.new) || 0;
  record.minutes = Number(record.minutes) || 0;
  if (!record.pillars || typeof record.pillars !== 'object') {
    record.pillars = { vocab: 0, kanji: 0, grammar: 0, reading: 0 };
  } else {
    record.pillars.vocab = Number(record.pillars.vocab) || 0;
    record.pillars.kanji = Number(record.pillars.kanji) || 0;
    record.pillars.grammar = Number(record.pillars.grammar) || 0;
    record.pillars.reading = Number(record.pillars.reading) || 0;
  }

  const addCount = Number(count) >= 0 ? Number(count) : 1;
  const isNewCard = Boolean(isNew || type === 'new' || type === 'newCards');

  if (isNewCard) {
    record.newCards += addCount;
  } else {
    record.reviews += addCount;
  }

  if (pillar) {
    const p = normalizePillar(pillar);
    if (p && record.pillars[p] !== undefined) {
      record.pillars[p] += addCount;
    }
  }

  if (typeof minutes === 'number' && minutes > 0) {
    record.minutes += minutes;
  } else if (typeof ms === 'number' && ms > 0) {
    // Cap per-card duration at 60s (doc 03 §6)
    const cappedMs = Math.min(ms, 60000);
    record.minutes += Math.round((cappedMs / 60000) * 100) / 100;
  }

  if (typeof wrong === 'number' && wrong > 0) {
    record.wrong = (Number(record.wrong) || 0) + wrong;
  }

  // Keep at most 400 days in log (doc 03 §6)
  const keys = Object.keys(daylog);
  if (keys.length > 400) {
    keys.sort();
    const removeCount = keys.length - 400;
    for (let i = 0; i < removeCount; i++) {
      delete daylog[keys[i]];
    }
  }

  saveDaylog(daylog);
  return { ...record, pillars: { ...record.pillars } };
}

/**
 * Counts consecutive active days (days with reviews > 0 or newCards > 0) ending today or yesterday.
 *
 * @param {string|number|Date} [referenceDate] - Optional reference date (defaults to today IST)
 * @param {string|null} [pillar] - Optional subject filter; uses the same IST day boundaries.
 * @returns {number} Consecutive active streak count
 */
export function getCurrentStreak(referenceDate, pillar = null) {
  const active = day => pillar ? (day.pillars?.[pillar] || 0) > 0 : (day.reviews > 0 || day.newCards > 0);
  const refStart = istDayStart(referenceDate || Date.now());
  const todayKey = istDateKey(refStart);
  const yesterdayKey = istDateKey(refStart - 86400000);

  const todayLog = getDay(todayKey);
  const yesterdayLog = getDay(yesterdayKey);

  const isTodayActive = active(todayLog);
  const isYesterdayActive = active(yesterdayLog);

  let startMs;
  if (isTodayActive) {
    startMs = refStart;
  } else if (isYesterdayActive) {
    startMs = refStart - 86400000;
  } else {
    return 0;
  }

  let streak = 0;
  let currMs = startMs;
  for (let i = 0; i < 400; i++) {
    const key = istDateKey(currMs);
    const day = getDay(key);
    if (active(day)) {
      streak++;
      currMs -= 86400000;
    } else {
      break;
    }
  }

  return streak;
}

/**
 * Maps daily activity count to heatmap intensity level (0..4).
 */
export function countToHeatmapLevel(count) {
  if (!count || count <= 0) return 0;
  if (count < 10) return 1;
  if (count < 25) return 2;
  if (count < 50) return 3;
  return 4;
}

/**
 * Returns an array of 30 days up to today (inclusive) in IST.
 * Each entry has { date: 'YYYY-MM-DD', count: number, level: 0..4 }.
 * Ordered chronologically (oldest at index 0, today at index 29).
 *
 * @param {string|number|Date} [referenceDate] - Optional reference date (defaults to today IST)
 * @returns {Array<{ date: string, count: number, level: number }>}
 */
export function getHeatmap30(referenceDate) {
  const baseStart = istDayStart(referenceDate || Date.now());
  const result = [];

  for (let i = 29; i >= 0; i--) {
    const dayMs = baseStart - (i * 86400000);
    const key = istDateKey(dayMs);
    const day = getDay(key);
    const count = (day.reviews || 0) + (day.newCards || 0);
    result.push({
      date: key,
      count,
      level: countToHeatmapLevel(count)
    });
  }

  return result;
}

/**
 * Merges local and remote daylog data idempotently by taking max of numeric counters (doc 03 §7).
 */
export function mergeDaylogs(local = {}, remote = {}) {
  const merged = { ...local };
  for (const [date, rDay] of Object.entries(remote)) {
    if (!merged[date]) {
      merged[date] = { ...rDay, pillars: { ...(rDay.pillars || {}) } };
    } else {
      const lDay = merged[date];
      merged[date] = {
        date,
        reviews: Math.max(lDay.reviews || 0, rDay.reviews || 0),
        newCards: Math.max(lDay.newCards || lDay.new || 0, rDay.newCards || rDay.new || 0),
        minutes: Math.max(lDay.minutes || 0, rDay.minutes || 0),
        pillars: {
          vocab: Math.max(lDay.pillars?.vocab || 0, rDay.pillars?.vocab || 0),
          kanji: Math.max(lDay.pillars?.kanji || 0, rDay.pillars?.kanji || 0),
          grammar: Math.max(lDay.pillars?.grammar || 0, rDay.pillars?.grammar || 0),
          reading: Math.max(lDay.pillars?.reading || 0, rDay.pillars?.reading || 0)
        }
      };
      if (lDay.wrong !== undefined || rDay.wrong !== undefined) {
        merged[date].wrong = Math.max(lDay.wrong || 0, rDay.wrong || 0);
      }
    }
  }
  return merged;
}

export const N3Daylog = {
  DAYLOG_STORAGE_KEY,
  createEmptyDayRecord,
  loadDaylog,
  saveDaylog,
  clearDaylog,
  getDay,
  logActivity,
  getCurrentStreak,
  countToHeatmapLevel,
  getHeatmap30,
  mergeDaylogs
};

if (typeof window !== 'undefined') {
  window.N3Daylog = N3Daylog;
}

export default N3Daylog;
