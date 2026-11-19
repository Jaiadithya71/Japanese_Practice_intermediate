import assert from 'node:assert/strict';
import { snapshotDueReviewItems, repeatDueReviewItems } from '../js/due-review-session.js';
import {
  DEFAULT_REVIEW_AGAIN_THRESHOLD,
  normalizeReviewAgainThreshold,
  selectReviewAgainKeys,
  selectReviewAgainItems
} from '../js/review-again-policy.js';

assert.equal(DEFAULT_REVIEW_AGAIN_THRESHOLD, 80);
assert.equal(normalizeReviewAgainThreshold('81'), 81);
assert.equal(normalizeReviewAgainThreshold(-4), 0);
assert.equal(normalizeReviewAgainThreshold(150), 100);
assert.equal(normalizeReviewAgainThreshold('bad'), 80);
const originalKeys = ['V:again', 'V:hard', 'V:good', 'V:again'];
const grades = new Map([['V:again', 1], ['V:hard', 2], ['V:good', 3]]);
assert.deepEqual(selectReviewAgainKeys(originalKeys, grades, 79, 80), ['V:again', 'V:hard']);
assert.deepEqual(selectReviewAgainKeys(originalKeys, grades, 80, 80), ['V:again', 'V:hard', 'V:good']);
assert.deepEqual(selectReviewAgainKeys(originalKeys, grades, 100, 80), ['V:again', 'V:hard', 'V:good']);
assert.deepEqual(selectReviewAgainKeys(originalKeys, grades, 50, 0), ['V:again', 'V:hard', 'V:good']);

const originalItems = [{ key: 'V:again' }, { key: 'V:hard' }, { key: 'V:good' }];
const outcome = selectReviewAgainItems(originalItems, [
  { key: 'V:again', grade: 1 },
  { key: 'V:again', grade: 3 }, // A successful Again re-queue clears that word from the retry set.
  { key: 'V:hard', grade: 2 },
  { key: 'V:good', grade: 3 }
], 79, 80);
assert.equal(outcome.belowThreshold, true);
assert.deepEqual(outcome.items, [{ key: 'V:hard' }]);
assert.deepEqual(selectReviewAgainItems(originalItems, [], 80, 80).items, []);
const queue = snapshotDueReviewItems(originalItems.map(item => ({ ...item, stats: { nextDue: 1, hist: [2] } })));
const retryQueue = repeatDueReviewItems(queue);
assert.deepEqual(retryQueue.map(item => item.key), originalItems.map(item => item.key));
assert.notEqual(retryQueue[0], queue[0]);
assert.notEqual(retryQueue[0].stats, queue[0].stats);
assert.notEqual(retryQueue[0].stats.hist, queue[0].stats.hist);
const sessionQueue = [...queue, { ...queue[0], _requeued: true }];
assert.equal(sessionQueue.length, 4);
assert.equal(repeatDueReviewItems(queue).length, 3, 'the repeat uses only the original captured scope');
console.log('Review Again policy and queue tests passed.');
