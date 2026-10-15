// Presentation state only. Choosing a phase must not change SRS or scores.
export function initialReviewPhase(item) {
  return item?.learnNew && !item.learned ? 'learn' : 'test';
}
export function canGradeReview(phase, revealed) {
  return phase === 'test' && revealed;
}
