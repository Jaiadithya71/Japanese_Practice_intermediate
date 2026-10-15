// Presentation state only. Choosing a phase must not change SRS or scores.
export function initialReviewPhase(item, selected = 'test') {
  return item?.learnNew && !item.learned ? 'learn' : selected;
}
export function canGradeReview(phase, revealed) {
  return phase === 'test' && revealed;
}

export function getReviewPhase() {
  try { return localStorage.getItem('n3_review_phase') === 'learn' ? 'learn' : 'test'; }
  catch (_) { return 'test'; }
}
export function setReviewPhasePreference(phase) {
  if (!['learn', 'test'].includes(phase)) return;
  try { localStorage.setItem('n3_review_phase', phase); } catch (_) {}
}
