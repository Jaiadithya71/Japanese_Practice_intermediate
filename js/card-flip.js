// Match the elementary card's 650ms 3D horizontal turn.
export const FLIP_DURATION = 650;
const easing = 'cubic-bezier(0.4, 0, 0.2, 1)';
export async function animateCardFlip(card, reveal, reducedMotion = false) {
  if (!card?.animate || reducedMotion) { reveal(); return; }
  const out = card.animate([
    {transform:'rotateY(0deg)'}, {transform:'rotateY(90deg)'}
  ], {duration:FLIP_DURATION / 2, easing, fill:'forwards'});
  try { await out.finished; }
  catch (_) { out.cancel(); return; }
  reveal();
  const incoming = card.animate([
    {transform:'rotateY(-90deg)'}, {transform:'rotateY(0deg)'}
  ], {duration:FLIP_DURATION / 2, easing, fill:'forwards'});
  out.cancel();
  try { await incoming.finished; } catch (_) {}
  incoming.cancel();
}
