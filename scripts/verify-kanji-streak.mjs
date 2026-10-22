import assert from 'node:assert/strict';
import {saveDaylog, getCurrentStreak} from '../js/daylog.js';
// No localStorage in Node: these tests use the in-memory log only.
saveDaylog({
  '2026-10-20': {reviews:10, pillars:{vocab:10}},
  '2026-10-21': {reviews:20, pillars:{vocab:20}},
  '2026-10-22': {reviews:43, pillars:{kanji:43}}
});
assert.equal(getCurrentStreak('2026-10-22'),3);
assert.equal(getCurrentStreak('2026-10-22','kanji'),1);
assert.equal(getCurrentStreak('2026-10-23','kanji'),1);
assert.equal(getCurrentStreak('2026-10-24','kanji'),0);
assert.equal(getCurrentStreak('2026-10-22T18:29:59Z','kanji'),1);
assert.equal(getCurrentStreak('2026-10-22T18:30:00Z','kanji'),1);
saveDaylog({});
console.log('Kanji-only streak, global streak, yesterday grace, gaps and IST midnight passed.');
