/* =======================================================
   NIHONGO INTERMEDIATE - reading-times.js
   Timed reading attempts: self-timer "Stop & Save" captures
   and graded timed-practice results, one record per attempt.

   Kept out of the SRS stats object on purpose: these are
   measurements, not review counts. They live in their own
   localStorage key and their own Gist file
   (nihongo-n3-reading-times.json), merged across devices by
   union on attempt id, so no device's history can clobber
   another's.
   ======================================================= */

export const READING_TIMES_STORAGE_KEY = 'n3_reading_attempts_v1';
export const MAX_READING_ATTEMPTS = 600;
export const MIN_ATTEMPT_SECONDS = 10; // below this a "reading" is an accidental tap, not a measurement

function getStorage() {
  if (typeof localStorage !== 'undefined') return localStorage;
  if (typeof window !== 'undefined' && window.localStorage) return window.localStorage;
  return null;
}

function isValidAttempt(a) {
  return a && typeof a === 'object'
    && typeof a.id === 'string' && a.id.length > 0
    && typeof a.lesson === 'string' && a.lesson.length > 0
    && Number.isFinite(a.s) && a.s > 0
    && Number.isFinite(a.ts) && a.ts > 0;
}

export function loadAttempts() {
  const storage = getStorage();
  if (!storage) return [];
  try {
    const raw = storage.getItem(READING_TIMES_STORAGE_KEY);
    const list = raw ? JSON.parse(raw) : [];
    if (!Array.isArray(list)) return [];
    return list.filter(isValidAttempt).sort((a, b) => a.ts - b.ts);
  } catch (e) {
    console.warn('[reading-times] Failed to parse attempts:', e);
    return [];
  }
}

function saveAttempts(list) {
  const storage = getStorage();
  if (!storage) return;
  const trimmed = list.slice(-MAX_READING_ATTEMPTS);
  try {
    storage.setItem(READING_TIMES_STORAGE_KEY, JSON.stringify(trimmed));
  } catch (e) {
    console.warn('[reading-times] Failed to save attempts:', e);
  }
}

// The latest attempt for a lesson strictly before a given timestamp.
export function previousAttemptFor(lessonId, beforeTs = Infinity) {
  let prev = null;
  for (const a of loadAttempts()) {
    if (a.lesson !== lessonId || a.ts >= beforeTs) continue;
    if (!prev || a.ts > prev.ts) prev = a;
  }
  return prev;
}

// Records one measured attempt. `seconds` must be active reading time only
// (the caller's timer already excludes paused time). Returns the saved
// attempt plus the previous attempt for the SAME passage, so the UI can
// show an honest like-for-like comparison. Never mixes passages.
export function addAttempt({ lessonId, seconds, chars, source, accuracy }) {
  if (!lessonId || !Number.isFinite(seconds) || seconds < MIN_ATTEMPT_SECONDS) return null;
  const safeChars = Number.isFinite(chars) && chars > 0 ? Math.round(chars) : 0;
  const attempt = {
    id: `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 6)}`,
    lesson: lessonId,
    s: Math.round(seconds),
    c: safeChars,
    cpm: safeChars > 0 ? Math.round(safeChars / (seconds / 60)) : 0,
    ts: Date.now(),
    src: source === 'practice' ? 'practice' : 'self'
  };
  if (Number.isFinite(accuracy) && accuracy >= 0 && accuracy <= 1) {
    attempt.acc = Math.round(accuracy * 100) / 100;
  }
  const previous = previousAttemptFor(lessonId);
  const list = loadAttempts();
  list.push(attempt);
  saveAttempts(list);
  return { attempt, previous };
}

// Attaches a later test score to an existing saved attempt on the same
// passage, so a read saved with Stop & Save and a test completed right
// after appear as one measured read with its comprehension score.
export function attachAccuracy(lessonId, attemptId, accuracy) {
  if (!lessonId || !attemptId || !Number.isFinite(accuracy) || accuracy < 0 || accuracy > 1) return false;
  const list = loadAttempts();
  const target = list.find(a => a.id === attemptId && a.lesson === lessonId);
  if (!target) return false;
  target.acc = Math.round(accuracy * 100) / 100;
  saveAttempts(list);
  return true;
}

// Union-merge remote attempts by id; neither side loses history.
export function mergeAttempts(remote) {
  if (!Array.isArray(remote)) return false;
  const local = loadAttempts();
  const seen = new Set(local.map(a => a.id));
  let changed = false;
  for (const a of remote) {
    if (!isValidAttempt(a) || seen.has(a.id)) continue;
    local.push(a);
    seen.add(a.id);
    changed = true;
  }
  if (changed) saveAttempts(local);
  return changed;
}

export function parseAttemptsText(text) {
  if (typeof text !== 'string' || !text.length) return [];
  try {
    const parsed = JSON.parse(text);
    return Array.isArray(parsed) ? parsed.filter(isValidAttempt) : [];
  } catch (_) {
    return [];
  }
}
