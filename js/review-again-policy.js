// Threshold policy is pure so the boundary and retry set stay testable.
export const DEFAULT_REVIEW_AGAIN_THRESHOLD = 80;

export function normalizeReviewAgainThreshold(value) {
  const n = Number(value);
  return Number.isFinite(n) ? Math.max(0, Math.min(100, Math.round(n))) : DEFAULT_REVIEW_AGAIN_THRESHOLD;
}

export function collectFinalGrades(gradedEntries) {
  const finalGrades = new Map();
  for (const entry of gradedEntries || []) {
    if (entry && entry.key && Number.isFinite(entry.grade)) finalGrades.set(entry.key, entry.grade);
  }
  return finalGrades;
}

export function selectReviewAgainKeys(originalKeys, finalGrades, accuracyPercent, threshold) {
  const limit = normalizeReviewAgainThreshold(threshold);
  const keys = [...new Set(originalKeys || [])];
  if (!(Number(accuracyPercent) < limit)) return keys;
  return keys.filter(key => {
    const grade = finalGrades instanceof Map ? finalGrades.get(key) : finalGrades?.[key];
    return grade === 1 || grade === 2;
  });
}

export function selectReviewAgainItems(originalItems, gradedEntries, accuracyPercent, threshold, keyOf) {
  const finalGrades = collectFinalGrades(gradedEntries);
  const key = typeof keyOf === 'function' ? keyOf : item => item?.key || '';
  const originalKeys = (originalItems || []).map(key);
  const belowThreshold = Number(accuracyPercent) < normalizeReviewAgainThreshold(threshold);
  if (!belowThreshold) return { belowThreshold: false, items: [] };
  const selected = new Set(selectReviewAgainKeys(originalKeys, finalGrades, accuracyPercent, threshold));
  return { belowThreshold: true, items: (originalItems || []).filter(item => selected.has(key(item))) };
}
