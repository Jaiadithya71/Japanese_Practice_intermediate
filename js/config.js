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
