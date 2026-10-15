// Each queue occurrence is graded once. Again copies are new occurrences.
export function createStudyHistory() {
  let queue = null;
  let outcomes = new WeakMap();
  const sync = items => {
    if (queue !== items) { queue = items; outcomes = new WeakMap(); }
  };
  return {
    get(items, item) { sync(items); return item ? outcomes.get(item) : undefined; },
    set(items, item, outcome) { sync(items); if (item) outcomes.set(item, outcome); }
  };
}
