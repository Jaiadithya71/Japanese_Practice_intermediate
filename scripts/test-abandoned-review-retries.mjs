import assert from 'node:assert/strict';
import fs from 'node:fs';
import {
  collectAbandonedVocabRetries,
  getGradedOccurrences,
  isAbandonedVocabReview,
  persistAbandonedVocabRetries,
  resetStudySessionState
} from '../js/abandoned-review-retries.js';
import { createStudyHistory } from '../js/study-history.js';

const saved = {
  '01': { items: [{ key: 'V:kept', chapter: '01' }, { key: 'V:resolved', chapter: '01' }] },
  '02': { items: [{ key: 'V:untouched', chapter: '02' }] }
};
const active = [
  { key: 'V:resolved', chapter: '01', type: 'vocab' },
  { key: 'V:new-hard', chapter: '01', type: 'vocab' },
  { key: 'V:new-again', chapter: '02', type: 'vocab' },
  { key: 'K:糸', chapter: '01', type: 'kanji', book: 'kanji' },
  { key: 'V:no-chapter', type: 'vocab' }
];
const result = collectAbandonedVocabRetries(saved, active, [
  { key: 'V:resolved', grade: 3 },
  { key: 'V:new-hard', grade: 2 },
  { key: 'V:new-again', grade: 1 },
  { key: 'K:糸', grade: 1 }
]);
assert.deepEqual(Object.fromEntries(Object.entries(result).map(([chapter, items]) => [chapter, items.map(item => item.key)])), {
  '01': ['V:kept', 'V:new-hard'],
  '02': ['V:untouched', 'V:new-again']
});

// An Again grade counts even before its delayed re-queued occurrence appears.
assert.deepEqual(collectAbandonedVocabRetries({}, [{ key: 'V:again', chapter: '03', type: 'vocab' }], [
  { key: 'V:again', grade: 1 }
])['03'].map(item => item.key), ['V:again']);

// A later successful re-queue grade supersedes the original Again.
assert.deepEqual(collectAbandonedVocabRetries({}, [{ key: 'V:again', chapter: '03', type: 'vocab' }], [
  { key: 'V:again', grade: 1 }, { key: 'V:again', grade: 3 }
]), {});

const sessionItems = [{ key: 'V:a' }, { key: 'V:b' }];
const history = createStudyHistory();
history.set(sessionItems, sessionItems[0], { grade: 1 });
history.set(sessionItems, sessionItems[1], { grade: 2 });
assert.deepEqual(getGradedOccurrences(sessionItems, history, item => item.key), [
  { key: 'V:a', grade: 1 }, { key: 'V:b', grade: 2 }
]);
assert.equal(isAbandonedVocabReview({
  isDueReviewMode: true, dueReviewPillar: 'vocab', sessionIdx: 1, sessionItems: [{}, {}, {}]
}), true);
assert.equal(isAbandonedVocabReview({
  isDueReviewMode: true, dueReviewPillar: 'vocab', sessionIdx: 3, sessionItems: [{}, {}, {}]
}), false);
assert.equal(isAbandonedVocabReview({
  isDueReviewMode: true, dueReviewPillar: 'kanji', sessionIdx: 0, sessionItems: [{}]
}), false);

const savedState = { '01': { items: [{ key: 'V:old', chapter: '01' }] } };
const storeCalls = [];
const abandonState = {
  isDueReviewMode: true, dueReviewPillar: 'vocab', sessionIdx: 1,
  sessionItems: [{ key: 'V:old' }, { key: 'V:new', chapter: '01', type: 'vocab' }],
  dueReviewActiveItems: [
    { key: 'V:old', chapter: '01', type: 'vocab' },
    { key: 'V:new', chapter: '01', type: 'vocab' }
  ]
};
const abandonHistory = createStudyHistory();
for (const item of abandonState.sessionItems) abandonHistory.set(abandonState.sessionItems, item, { grade: item.key === 'V:old' ? 3 : 2 });
assert.equal(persistAbandonedVocabRetries(
  abandonState, abandonHistory, item => item.key,
  () => savedState,
  (chapter, items) => storeCalls.push(['save', chapter, items.map(item => item.key)]),
  chapter => storeCalls.push(['clear', chapter])
), true);
assert.deepEqual(storeCalls, [['save', '01', ['V:new']]], 'resolved saved Good is removed; new Hard card saved');
const unchangedCalls = [];
const preservedState = { isDueReviewMode: true, dueReviewPillar: 'vocab', sessionIdx: 0,
  sessionItems: [{}], dueReviewActiveItems: [{ key: 'V:unanswered', chapter: '01', type: 'vocab' }] };
assert.equal(persistAbandonedVocabRetries(preservedState, createStudyHistory(), item => item.key,
  () => ({ '01': { items: [{ key: 'V:kept', chapter: '01' }] } }),
  (...args) => unchangedCalls.push(['save', ...args]), chapter => unchangedCalls.push(['clear', chapter])), true);
assert.deepEqual(unchangedCalls, [], 'unchanged saved retries are not rewritten just because user exited');

const noGradeCalls = [];
const unfinishedUnseen = { isDueReviewMode: true, dueReviewPillar: 'vocab', sessionIdx: 0,
  sessionItems: [{}], dueReviewActiveItems: [{ key: 'V:unseen', chapter: '01', type: 'vocab' }] };
assert.equal(persistAbandonedVocabRetries(unfinishedUnseen, createStudyHistory(), item => item.key,
  () => ({}), (...args) => noGradeCalls.push(args), () => {}), true);
assert.deepEqual(noGradeCalls, [], 'no grade means no retry row is created');

const state = {
  sessionItems: [{ key: 'V:a' }], sessionIdx: 1, sessionRight: 1, sessionTotal: 2,
  sessionTotalInitial: 2, sessionTotalAnswered: 2, cardFlipped: true,
  dueReviewOriginalItems: [{}], dueReviewActiveItems: [{}], dueReviewRetryItems: [{}],
  dueReviewThresholdResult: {}, dueReviewPillar: 'vocab', savedRetryLessonId: '01', savedRetryPart: 'A', savedRetryAll: true, isDueReviewMode: true
};
resetStudySessionState(state);
assert.deepEqual(state, {
  sessionItems: [], sessionIdx: 0, sessionRight: 0, sessionTotal: 0,
  sessionTotalInitial: 0, sessionTotalAnswered: 0, cardFlipped: false,
  dueReviewOriginalItems: [], dueReviewActiveItems: [], dueReviewRetryItems: [],
  dueReviewThresholdResult: null, dueReviewPillar: null, savedRetryLessonId: null, savedRetryPart: null, savedRetryAll: null, isDueReviewMode: false
});
const studySource = fs.readFileSync(new URL('../js/study.js', import.meta.url), 'utf8');
assert.match(studySource, /function saveAbandonedReviewRetries\(\) \{[\s\S]*?persistAbandonedVocabRetries\(/);
assert.match(studySource, /export function exitStudy\(\) \{\s*const returnView = state\.drillOrigin \|\| 'home';\s*saveAbandonedReviewRetries\(\);\s*endGistReviewSession\(\);\s*resetStudySessionAfterExit\(\);/);
const homeSource = fs.readFileSync(new URL('../js/home.js', import.meta.url), 'utf8');
assert.match(homeSource, /tile\.className = 'home-lesson-tile hra-tile-part'/);
assert.match(homeSource, /startSavedReviewAgain\(chapter, \{ part \}\)/);
console.log('Exit integration: save pending lesson retries before ending sync, reset active queue, and show the lesson Resume boxes.');

console.log('Abandoned review: per-lesson Hard/Again persistence, resolved grades, retry occurrence handling, and session reset passed.');
