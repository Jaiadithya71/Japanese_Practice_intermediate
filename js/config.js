/* =======================================================
   NIHONGO INTERMEDIATE — config.js
   Constants, SRS weights, and study thresholds
   ======================================================= */

export const STORAGE_KEY = 'nihongo_intermediate_stats_v1';

// SRS Parameters
export const HARD_THRESHOLD = 1.8;
export const MASTERED_THRESHOLD = 3;

// Dynamic Weight Multipliers
export const WEIGHT_RIGHT = 0.75;
export const WEIGHT_WRONG = 2.2;
export const WEIGHT_MIN = 0.1;
export const WEIGHT_MAX = 5.0;

// SM-2 Defaults
export const DEFAULT_EASE_FACTOR = 2.5;

// IST Daily Schedule Windows (UTC + 5.5 hours)
export const IST_SLOT_A_HOUR = 7;
export const IST_SLOT_A_MINUTE = 30; // 7:30 AM IST

export const IST_SLOT_B_HOUR = 17;
export const IST_SLOT_B_MINUTE = 45; // 5:45 PM IST

// Chapter Identifiers
export const TOPIC_CHAPTERS = Array.from({ length: 21 }, (_, i) => `part1_${String(i + 1).padStart(2, '0')}`);
export const CHARACTERISTIC_CHAPTERS = Array.from({ length: 8 }, (_, i) => `part2_${String(i + 1).padStart(2, '0')}`);

// Memory Engine & Scheduling Constants (doc 02 §4)
export const STEPS_DAYS        = [0, 1, 3, 7, 14, 30];  // 0 = next slot (≥4h)
export const MIN_FIRST_GAP_MS  = 4 * 60 * 60 * 1000;    // first review gap
export const EASE_FLOOR        = 1.8;                   // replaces old 1.3
export const LAPSE_FACTOR      = 0.4;                   // relearn base after lapse = max(2, round(prev * 0.4))
export const LEECH_LAPSES      = 5;                     // threshold to mark as leech
export const REQUEUE_OFFSET    = 3;                     // cards later in session
export const MAX_REQUEUES      = 2;                     // per card per session
export const CRITERION_CORRECT = 2;                     // correct answers to leave learning loop
export const EXAM_DATE_ISO     = '2026-12-13';          // NAT-TEST 3Q exam date
export const EXAM_MIN_REVIEWS  = 3;                     // minimum reviews guaranteed before exam
export const HIST_LEN          = 5;                     // stored grade history length
export const SLOW_MS           = 12000;                 // MCQ speed threshold for auto-grade
export const BACKLOG_THRESHOLD = 80;                    // triggers catch-up mode
export const SEC_PER_REVIEW    = 7;                     // forecaster seconds per review
export const SEC_PER_NEW       = 30;                    // forecaster seconds per new item

