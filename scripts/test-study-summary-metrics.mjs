import assert from 'node:assert/strict';
import fs from 'node:fs';
import { selectReviewAgainItems } from '../js/review-again-policy.js';
import { summarizeStudyReviewCounts } from '../js/study-summary-metrics.js';

const metrics = summarizeStudyReviewCounts(83, 64);
assert.deepEqual(metrics, {
  totalReviews: 83,
  correctReviews: 64,
  againCount: 19,
  accuracyPercent: 77
});
assert.deepEqual(summarizeStudyReviewCounts(0, 0), {
  totalReviews: 0,
  correctReviews: 0,
  againCount: 0,
  accuracyPercent: 0
});
assert.deepEqual(summarizeStudyReviewCounts(10, 12), {
  totalReviews: 10,
  correctReviews: 10,
  againCount: 0,
  accuracyPercent: 100
});

// Same pattern as an 83-review session: 64 starting cards, 19 initial Again
// responses, then those 19 cards are retried and graded Hard. Correct reviews
// are 45 initial Hard + 19 retry Hard = 64. At 77%, the approved 80% policy
// keeps all final Hard cards in the retry pool, even though they count correct.
const originalItems = Array.from({ length: 64 }, (_, i) => ({ key: `V:${i}` }));
const initialGrades = originalItems.map((item, i) => ({ key: item.key, grade: i < 19 ? 1 : 2 }));
const retryGrades = originalItems.slice(0, 19).map(item => ({ key: item.key, grade: 2 }));
const gradedEntries = [...initialGrades, ...retryGrades];
const correctReviewCount = gradedEntries.filter(entry => entry.grade >= 2).length;
const wrongReviewCount = gradedEntries.filter(entry => entry.grade === 1).length;
assert.equal(gradedEntries.length, 83);
assert.equal(correctReviewCount, 64);
assert.equal(wrongReviewCount, 19);
assert.equal(summarizeStudyReviewCounts(gradedEntries.length, correctReviewCount).accuracyPercent, 77);
const retrySet = selectReviewAgainItems(originalItems, gradedEntries, 77, 80, item => item.key);
assert.equal(retrySet.belowThreshold, true);
assert.equal(retrySet.items.length, 64, 'Hard and Again final cards remain eligible for retry below threshold');

const source = fs.readFileSync(new URL('../js/study.js', import.meta.url), 'utf8');
assert.match(source, /const againReviewCount = reviewMetrics\.againCount/);
assert.match(source, /Correct/);
assert.match(source, /Again/);
assert.match(source, /Reviews/);
assert.match(source, /completed \$\{answered\} reviews, including retries/);
assert.match(source, /Hard\/Again card/);
console.log('Summary count clarity: 83 reviews = 64 correct + 19 Again; retry pool separately retains 64 Hard/Again cards.');
