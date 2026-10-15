/* =======================================================
   NIHONGO INTERMEDIATE — planner.js
   Pace Planner, Exam-Aware Interval Capping & Load Forecaster
   Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §4.3, §6.3, §6.4
   ======================================================= */

import {
  EXAM_DATE_ISO,
  EXAM_MIN_REVIEWS,
  STEPS_DAYS,
  EASE_FLOOR,
  DEFAULT_EASE_FACTOR,
  SEC_PER_REVIEW,
  SEC_PER_NEW
} from './config.js';

export const PACE_PROFILES = {
  light: {
    vocab: 6,
    kanjiWords: 6,
    grammar: 1,
    targetMinutes: 25
  },
  standard: {
    vocab: 10,
    kanjiWords: 12,
    grammar: 2,
    targetMinutes: 40
  },
  intensive: {
    vocab: 15,
    kanjiWords: 18,
    grammar: 3,
    targetMinutes: 60
  }
};

/**
 * Calculates exam-aware interval cap in days (doc 02 §4.3).
 * daysLeft = floor((examDate - now) / DAY).
 * If daysLeft <= 0 return 1; clamp(floor(daysLeft / (EXAM_MIN_REVIEWS + 1)), 2, 30).
 *
 * @param {number|Date} [now=Date.now()]
 * @param {string|number|Date} [examDate=EXAM_DATE_ISO]
 * @returns {number} Cap in days (1 to 30)
 */
export function examCapDays(now = Date.now(), examDate = EXAM_DATE_ISO) {
  const DAY_MS = 24 * 60 * 60 * 1000;
  const nowMs = typeof now === 'number' ? now : (now instanceof Date ? now.getTime() : Date.now());
  const examMs = typeof examDate === 'string'
    ? new Date(examDate).getTime()
    : (examDate instanceof Date ? examDate.getTime() : Number(examDate));

  const daysLeft = Math.floor((examMs - nowMs) / DAY_MS);
  if (daysLeft <= 0) return 1;

  const rawCap = Math.floor(daysLeft / (EXAM_MIN_REVIEWS + 1));
  return Math.min(30, Math.max(2, rawCap));
}

/**
 * Calculates daily new item quotas based on days remaining to the exam (doc 02 §6.3).
 *
 * @param {Object} unseenCounts - { vocab / vocabTier1, kanjiWords / kanji, grammar }
 * @param {string} [profile='standard'] - 'light' | 'standard' | 'intensive'
 * @param {string|number|Date} [examDate=EXAM_DATE_ISO]
 * @param {Object} [options] - { now, reserveDays, studyDays }
 * @returns {Object} Pace planning breakdown with quotas, feasible flags, and user-facing warnings
 */
export function calculatePace(unseenCounts = {}, profile = 'standard', examDate = EXAM_DATE_ISO, options = {}) {
  const DAY_MS = 24 * 60 * 60 * 1000;
  const nowMs = options.now
    ? (typeof options.now === 'number' ? options.now : new Date(options.now).getTime())
    : Date.now();
  const examMs = typeof examDate === 'string'
    ? new Date(examDate).getTime()
    : (examDate instanceof Date ? examDate.getTime() : Number(examDate));

  const daysToExam = Math.floor((examMs - nowMs) / DAY_MS);
  const reserveDays = options.reserveDays !== undefined ? options.reserveDays : 10;
  const studyDaysPerWeek = options.studyDays !== undefined ? options.studyDays : 6;
  const learningDays = Math.max(1, Math.floor(((daysToExam - reserveDays) * studyDaysPerWeek) / 7));

  const profileKey = String(profile || 'standard').toLowerCase();
  const profileCaps = PACE_PROFILES[profileKey] || PACE_PROFILES.standard;

  const counts = {
    vocab: unseenCounts.vocabTier1 !== undefined ? unseenCounts.vocabTier1 : (unseenCounts.vocab || 0),
    kanjiWords: unseenCounts.kanjiWords !== undefined ? unseenCounts.kanjiWords : (unseenCounts.kanji || 0),
    grammar: unseenCounts.grammar !== undefined ? unseenCounts.grammar : 0
  };

  const quotas = {};
  const rawQuotas = {};
  const feasible = {};
  const shortfall = {};
  const warnings = [];

  const pillars = ['vocab', 'kanjiWords', 'grammar'];
  for (const p of pillars) {
    const remaining = counts[p] || 0;
    const raw = Math.ceil(remaining / learningDays);
    const cap = profileCaps[p] || 0;
    const quota = Math.max(0, Math.min(raw, cap));
    const isFeasible = raw <= cap;
    const covered = quota * learningDays;
    const diff = Math.max(0, remaining - covered);

    quotas[p] = quota;
    rawQuotas[p] = raw;
    feasible[p] = isFeasible;
    shortfall[p] = diff;

    if (!isFeasible && diff > 0) {
      const pLabel = p === 'kanjiWords' ? 'kanji-words' : p;
      warnings.push(`At this pace, ${diff} ${pLabel} will not be learned before the exam. Raise the pace or accept lower coverage.`);
    }
  }

  const allFeasible = Boolean(feasible.vocab && feasible.kanjiWords && feasible.grammar);

  return {
    daysToExam,
    learningDays,
    reserveDays,
    studyDaysPerWeek,
    profile: profileKey,
    quotas,
    rawQuotas,
    feasible,
    shortfall,
    allFeasible,
    warnings,
    summary: warnings.join(' ')
  };
}

/**
 * Pure load forecasting simulation function (doc 02 §6.4).
 * Returns [{ day, newItems, reviews, minutes }] for future days.
 *
 * @param {Object} [settings={}] - Configuration overrides (profile, timeBudgetMin, secPerReview, etc.)
 * @param {Object} [stats={}] - Current state.stats for initializing existing item schedules
 * @param {number} [days=60] - Number of future days to simulate
 * @returns {Array<{ day: number, newItems: number, reviews: number, minutes: number }>}
 */
export function forecast(settings = {}, stats = {}, days = 60) {
  const profileKey = String(settings.profile || 'standard').toLowerCase();
  const profileCaps = PACE_PROFILES[profileKey] || PACE_PROFILES.standard;

  const defaultNewPerDay = profileCaps.vocab + profileCaps.kanjiWords + profileCaps.grammar;
  const newPerDay = settings.newPerDay !== undefined ? Number(settings.newPerDay) : defaultNewPerDay;
  const timeBudgetMin = Number(settings.timeBudgetMin || 45);
  const secPerReview = Number(settings.secPerReview || SEC_PER_REVIEW || 7);
  const secPerNew = Number(settings.secPerNew || SEC_PER_NEW || 30);
  const passRate = settings.passRate !== undefined ? Number(settings.passRate) : 0.9;
  const examDate = settings.examDate || EXAM_DATE_ISO;
  const DAY_MS = 24 * 60 * 60 * 1000;
  const nowMs = settings.now
    ? (typeof settings.now === 'number' ? settings.now : new Date(settings.now).getTime())
    : Date.now();

  // Learning days before exam reserve window
  const pace = calculatePace({}, profileKey, examDate, { now: nowMs, studyDays: settings.studyDays || 6 });
  const learningDaysLimit = settings.learningDays !== undefined ? Number(settings.learningDays) : pace.learningDays;

  // Active items in simulation: Array<{ dueDay, rep, interval, easeFactor }>
  const activeItems = [];

  // Seed existing items from stats
  if (stats && typeof stats === 'object') {
    for (const key of Object.keys(stats)) {
      const s = stats[key];
      if (!s || !s.nextDue) continue;
      const daysUntilDue = Math.max(1, Math.round((s.nextDue - nowMs) / DAY_MS));
      if (daysUntilDue <= days) {
        activeItems.push({
          dueDay: daysUntilDue,
          rep: Math.max(1, Number(s.reps) || 1),
          interval: Math.max(1, Number(s.interval) || 1),
          easeFactor: Math.max(EASE_FLOOR, Number(s.easeFactor) || DEFAULT_EASE_FACTOR)
        });
      }
    }
  }

  const results = [];
  let budgetWarningCount = 0;

  for (let d = 1; d <= days; d++) {
    const currentSimMs = nowMs + (d * DAY_MS);
    const dayExamCap = examCapDays(currentSimMs, examDate);

    // 1. Determine new items introduced today
    const newCount = d <= learningDaysLimit ? newPerDay : 0;
    for (let n = 0; n < newCount; n++) {
      // Step 0 is completed on introduction day; first real SRS review is Step 1 (interval = 1 day)
      activeItems.push({
        dueDay: d + 1,
        rep: 1,
        interval: 1,
        easeFactor: DEFAULT_EASE_FACTOR
      });
    }

    // 2. Count and progress reviews due today
    let reviewsToday = 0;
    const len = activeItems.length;
    for (let i = 0; i < len; i++) {
      const item = activeItems[i];
      if (item.dueDay === d) {
        reviewsToday++;

        // Deterministic progression matching passRate (e.g. 90% pass, 10% lapse)
        const isPass = ((i + d) % 10) < Math.round(passRate * 10);
        if (isPass) {
          item.rep++;
          const idx = item.rep - 1;
          let nextInt;
          if (idx < STEPS_DAYS.length) {
            nextInt = STEPS_DAYS[idx] || 1;
          } else {
            nextInt = Math.round(Math.max(1, item.interval) * item.easeFactor);
          }
          item.interval = Math.min(nextInt, dayExamCap);
          item.dueDay = d + Math.max(1, item.interval);
        } else {
          // Lapse
          item.rep = 0;
          item.interval = 1;
          item.easeFactor = Math.max(EASE_FLOOR, item.easeFactor - 0.2);
          item.dueDay = d + 1;
        }
      }
    }

    // 3. Compute study minutes
    const totalSec = (reviewsToday * secPerReview) + (newCount * secPerNew);
    const minutes = Math.round(totalSec / 60);

    // Track 14-day budget warning threshold (20% over budget)
    if (d <= 14 && minutes > (timeBudgetMin * 1.2)) {
      budgetWarningCount++;
    }

    results.push({
      day: d,
      newItems: newCount,
      reviews: reviewsToday,
      minutes
    });
  }

  // Attach metadata to results array
  results.budgetWarningCount = budgetWarningCount;
  results.warning = budgetWarningCount > 0
    ? `Study time exceeds budget on ${budgetWarningCount} day(s) in next 2 weeks. Consider lowering daily quota or switching to Light profile.`
    : null;

  return results;
}

if (typeof window !== 'undefined') {
  window.N3Planner = {
    examCapDays,
    calculatePace,
    forecast,
    PACE_PROFILES
  };
}
