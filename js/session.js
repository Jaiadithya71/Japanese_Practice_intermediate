/* =======================================================
   NIHONGO INTERMEDIATE — session.js
   Session Engine, Re-queue Management & Criterion Grading
   Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §5
   ======================================================= */

import {
  SLOW_MS,
  REQUEUE_OFFSET,
  MAX_REQUEUES,
  CRITERION_CORRECT
} from './config.js';
import { state } from './state.js';
import {
  updateItemStats,
  getItemStats,
  formatItemKey
} from './srs.js';

/**
 * Creates and initializes a session state object (doc 02 §5.1).
 * Mirrors legacy state fields for full backward compatibility with study.js.
 *
 * @param {string} mode - 'learn-kanji' | 'review' | 'drill-hard' | 'lesson-test' | 'quick5'
 * @param {Array<Object>} [cards=[]] - Initial card queue
 * @param {string} [origin='today'] - Origin route/view to return on exit
 * @returns {Object} Initialized session
 */
export function createSession(mode, cards = [], origin = 'today') {
  const session = {
    id: `sess_${Date.now()}_${Math.random().toString(36).substr(2, 6)}`,
    mode,
    queue: Array.isArray(cards) ? [...cards] : [],
    cursor: 0,
    retries: new Map(),
    correctCount: new Map(),
    stats: {
      right: 0,
      total: 0,
      startedAt: Date.now(),
      ms: []
    },
    origin
  };

  state.session = session;

  // Mirror to legacy state fields for study.js compatibility
  state.sessionItems = session.queue;
  state.sessionIdx = session.cursor;
  state.sessionRight = session.stats.right;
  state.sessionTotal = session.stats.total;
  state.studyMode = session.mode;
  state.drillOrigin = session.origin;

  return session;
}

/**
 * Returns the card currently at the session cursor or null if finished.
 *
 * @param {Object} [session=state.session]
 * @returns {Object|null}
 */
export function getCurrentCard(session = state.session) {
  if (!session || !session.queue || session.cursor >= session.queue.length) {
    return null;
  }
  return session.queue[session.cursor];
}

/**
 * Auto-grades MCQ responses (doc 02 §5.2, ME-6).
 * - Wrong -> 1 (Again)
 * - Correct and (elapsedMs > SLOW_MS or usedHint) -> 2 (Hard)
 * - Correct -> 3 (Good)
 * "Easy" (4) is NEVER auto-assigned for MCQ.
 *
 * @param {boolean} isCorrect
 * @param {number} [elapsedMs=0]
 * @param {boolean} [usedHint=false]
 * @returns {number} Grade 1, 2, or 3
 */
export function deriveGradeFromMCQ(isCorrect, elapsedMs = 0, usedHint = false) {
  if (!isCorrect) {
    return 1;
  }
  if (usedHint || (typeof elapsedMs === 'number' && elapsedMs > SLOW_MS)) {
    return 2;
  }
  return 3;
}

/**
 * Records card grading result, handles +3 re-queue on error, criterion tracking,
 * and updates stats (doc 02 §5.3, §5.4, ME-2, ME-3).
 *
 * @param {Object} session
 * @param {Object} card
 * @param {number} grade - 1: Again, 2: Hard, 3: Good, 4: Easy
 * @param {Object} [opts={}] - { elapsedMs, usedHint, cause }
 * @returns {Object} Result summary
 */
export function recordCardResult(session = state.session, card, grade, opts = {}) {
  if (!session || !card) return null;

  const key = card.key || formatItemKey(card);
  const isRequeued = Boolean(card._requeued);

  // Update session stats (re-queued cards do not count twice in total, doc 02 §5.3)
  if (!isRequeued) {
    session.stats.total++;
    if (grade >= 2) {
      session.stats.right++;
    }
  }

  if (opts.elapsedMs !== undefined && typeof opts.elapsedMs === 'number') {
    session.stats.ms.push(opts.elapsedMs);
  }

  if (grade === 1) { // Wrong / Again
    const curRetries = session.retries.get(key) || 0;
    session.correctCount.set(key, 0); // resets criterion count on failure

    // Re-insert card +3 positions later if under retry limit (doc 02 §5.3, ME-2)
    if (curRetries < MAX_REQUEUES) {
      session.retries.set(key, curRetries + 1);
      const insertIdx = Math.min(session.cursor + REQUEUE_OFFSET, session.queue.length);
      const requeuedCopy = { ...card, _requeued: true };
      session.queue.splice(insertIdx, 0, requeuedCopy);
    } else {
      session.retries.set(key, curRetries + 1);
    }

    updateItemStats(key, 1, opts);
  } else { // Correct (grade >= 2)
    const count = (session.correctCount.get(key) || 0) + 1;
    session.correctCount.set(key, count);

    const s = getItemStats(key);
    const isLearning = (s.learnState === 'learning' || s.learnState === 'relearning' || (!s.learnState && (s.reps || 0) === 0));

    if (isLearning && count < CRITERION_CORRECT) {
      // Still inside the learn-to-criterion loop: stay in session (doc 02 §5.4, ME-3)
      const hasUpcoming = session.queue.slice(session.cursor + 1).some(c => (c.key || formatItemKey(c)) === key);
      if (!hasUpcoming) {
        const insertIdx = Math.min(session.cursor + REQUEUE_OFFSET, session.queue.length);
        const requeuedCopy = { ...card, _requeued: true };
        session.queue.splice(insertIdx, 0, requeuedCopy);
      }
      updateItemStats(key, grade, { ...opts, inSession: true });
    } else {
      // Criterion reached (or standard review): graduate card
      updateItemStats(key, grade, { ...opts, inSession: false });
    }
  }

  session.cursor++;

  // Keep legacy state mirrored
  state.sessionItems = session.queue;
  state.sessionIdx = session.cursor;
  state.sessionRight = session.stats.right;
  state.sessionTotal = session.stats.total;

  return {
    card,
    grade,
    cursor: session.cursor,
    isFinished: isSessionFinished(session)
  };
}

/**
 * Returns true if the session has reached the end of the queue.
 *
 * @param {Object} [session=state.session]
 * @returns {boolean}
 */
export function isSessionFinished(session = state.session) {
  if (!session || !session.queue) return true;
  return session.cursor >= session.queue.length;
}

/**
 * Computes summary results for the completed session.
 *
 * @param {Object} [session=state.session]
 * @returns {Object|null}
 */
export function getSessionResults(session = state.session) {
  if (!session) return null;
  const total = session.stats.total || 0;
  const right = session.stats.right || 0;
  const pct = total > 0 ? Math.round((right / total) * 100) : 0;
  const durationMs = Date.now() - (session.stats.startedAt || Date.now());
  const avgMs = session.stats.ms.length > 0
    ? Math.round(session.stats.ms.reduce((a, b) => a + b, 0) / session.stats.ms.length)
    : 0;

  return {
    total,
    right,
    wrong: Math.max(0, total - right),
    percentage: pct,
    durationMs,
    avgMs,
    stats: { ...session.stats }
  };
}

if (typeof window !== 'undefined') {
  window.N3Session = {
    createSession,
    getCurrentCard,
    deriveGradeFromMCQ,
    recordCardResult,
    isSessionFinished,
    getSessionResults
  };
}
