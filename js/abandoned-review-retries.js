export function collectAbandonedVocabRetries(savedByLesson, activeItems, gradedOccurrences) {
  const finalGrades = new Map();
  for (const occurrence of gradedOccurrences || []) {
    if (occurrence?.key && Number.isFinite(Number(occurrence.grade))) {
      finalGrades.set(occurrence.key, Number(occurrence.grade));
    }
  }

  const result = new Map();
  const seen = new Map();
  const add = (chapterId, item) => {
    const chapter = String(chapterId || item?.chapter || '');
    const key = item?.key || (item?.id ? `V:${item.id}` : '');
    if (!chapter || !key) return;
    if (!seen.has(chapter)) seen.set(chapter, new Set());
    if (seen.get(chapter).has(key)) return;
    seen.get(chapter).add(key);
    if (!result.has(chapter)) result.set(chapter, []);
    result.get(chapter).push({ ...item, key });
  };

  // Keep saved items not answered in this run, plus those still Hard/Again.
  for (const [chapter, entry] of Object.entries(savedByLesson || {})) {
    for (const item of Array.isArray(entry?.items) ? entry.items : []) {
      const key = item?.key || (item?.id ? `V:${item.id}` : '');
      const grade = finalGrades.get(key);
      if (grade === undefined || grade === 1 || grade === 2) add(chapter, item);
    }
  }

  // Add this run's distinct vocab cards whose final grade is Hard/Again.
  for (const item of Array.isArray(activeItems) ? activeItems : []) {
    const key = item?.key || (item?.id ? `V:${item.id}` : '');
    const isVocab = item?.type === 'vocab' || item?.book === 'vocab' || String(key).startsWith('V:');
    const grade = finalGrades.get(key);
    if (isVocab && (grade === 1 || grade === 2)) add(item?.chapter, item);
  }

  return Object.fromEntries([...result].map(([chapter, items]) => [chapter, items]));
}

export function getGradedOccurrences(sessionItems, studyHistory, formatItemKey) {
  const entries = [];
  for (const item of Array.isArray(sessionItems) ? sessionItems : []) {
    const grade = studyHistory?.get?.(sessionItems, item)?.grade;
    if (grade) entries.push({ key: formatItemKey(item), grade });
  }
  return entries;
}

export function isAbandonedVocabReview(state) {
  return Boolean(state?.isDueReviewMode &&
    state.sessionIdx < (state.sessionItems?.length || 0) &&
    (state.dueReviewPillar === 'vocab' || state.dueReviewPillar === 'all'));
}

export function persistAbandonedVocabRetries(state, studyHistory, formatItemKey, loadSaved, saveForLesson, clearForLesson) {
  if (!isAbandonedVocabReview(state)) return false;
  const activeItems = state.dueReviewActiveItems?.length
    ? state.dueReviewActiveItems
    : state.dueReviewOriginalItems;
  const grades = getGradedOccurrences(state.sessionItems, studyHistory, formatItemKey);
  const before = loadSaved();
  const merged = collectAbandonedVocabRetries(before, activeItems, grades);
  const keysEqual = (left, right) => {
    const a = (left || []).map(item => item?.key || (item?.id ? `V:${item.id}` : '')).filter(Boolean);
    const b = (right || []).map(item => item?.key || (item?.id ? `V:${item.id}` : '')).filter(Boolean);
    return a.length === b.length && a.every((key, i) => key === b[i]);
  };
  for (const chapter of Object.keys(before)) {
    if (!merged[chapter]?.length) clearForLesson(chapter);
  }
  for (const [chapter, items] of Object.entries(merged)) {
    if (!keysEqual(before[chapter]?.items, items)) saveForLesson(chapter, items);
  }
  return true;
}

export function resetStudySessionState(state) {
  state.sessionItems = [];
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = 0;
  state.sessionTotalInitial = 0;
  state.sessionTotalAnswered = 0;
  state.cardFlipped = false;
  state.dueReviewOriginalItems = [];
  state.dueReviewActiveItems = [];
  state.dueReviewRetryItems = [];
  state.dueReviewThresholdResult = null;
  state.dueReviewPillar = null;
  state.savedRetryLessonId = null;
  state.isDueReviewMode = false;
}
