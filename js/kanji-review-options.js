// One queue plan for compact review preview and launch. No study records are changed.
import { state } from './state.js';
import { getAllDueItems, isCatchUpMode } from './srs.js';
export function kanjiReviewPlan(lessons = state.selectedDueKanjiLessons) {
  const direction = state.kanjiDueDirection || 'both';
  const facets = new Set(direction === 'reading' ? ['KWR'] : direction === 'writing' ? ['KWW'] : ['KWR', 'KWW']);
  if (state.kanjiDueSingle !== false) facets.add('K');
  const available = getAllDueItems('kanji', 'all', null, { uncapped: true });
  const pool = getAllDueItems('kanji', 'all', lessons, { facets, uncapped: true });
  const catchUp = isCatchUpMode();
  const requested = state.dueBatchSize === 'all' ? Infinity : (parseInt(state.dueBatchSize, 10) || 20);
  const cap = catchUp ? Math.min(requested, 40) : requested;
  const items = pool.slice(0, cap);
  const count = rows => ({ writing: rows.filter(i => i.facet === 'KWW').length, reading: rows.filter(i => i.facet === 'KWR').length, single: rows.filter(i => i.facet === 'K').length });
  const byLesson = {};
  available.filter(i => facets.has(i.facet)).forEach(i => { if (i.lesson_number) byLesson[i.lesson_number] = (byLesson[i.lesson_number] || 0) + 1; });
  return { items, pool, available, byLesson, catchUp, counts: count(pool), round: count(items), scoped: !!lessons?.size };
}
