export function summarizeStudyReviewCounts(answeredCount, correctCount) {
  const asCount = value => {
    const n = Number(value);
    return Number.isFinite(n) ? Math.max(0, Math.trunc(n)) : 0;
  };
  const totalReviews = asCount(answeredCount);
  const correctReviews = Math.min(totalReviews, asCount(correctCount));
  return {
    totalReviews,
    correctReviews,
    againCount: totalReviews - correctReviews,
    accuracyPercent: totalReviews ? Math.round((correctReviews / totalReviews) * 100) : 0
  };
}
