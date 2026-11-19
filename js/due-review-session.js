// Keep a due-review round's initial queue separate from any Again copies
// inserted while grading. Repeats use a fresh copy of that original queue.
export function copyDueReviewItems(items) {
  return (Array.isArray(items) ? items : []).map(item => ({
    ...item,
    ...(item.stats ? { stats: { ...item.stats, ...(Array.isArray(item.stats.hist) ? { hist: [...item.stats.hist] } : {}) } } : {})
  }));
}

export function snapshotDueReviewItems(items) {
  return copyDueReviewItems(items);
}

export function repeatDueReviewItems(snapshot) {
  return copyDueReviewItems(snapshot);
}
