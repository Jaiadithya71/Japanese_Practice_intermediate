import assert from 'node:assert/strict';

globalThis.window = {};
const { state } = await import('../js/state.js');
const { buildListeningQueue } = await import('../js/listening.js');

const repeatedWord = { id: 'v07-038', term_ja: '命', reading: 'いのち', meaning_en: 'life' };
state.vocabDB = {
  '07': [repeatedWord],
  '31': []
};
state.vocabLessonOverlaps = {
  '31': [{ ...repeatedWord, chapter: '31' }]
};

const queue = buildListeningQueue(new Set(['07', '31']));
assert.equal(queue.length, 2, 'the same word appears once for each selected lesson');
assert.deepEqual(queue.map(item => item.chapter), ['07', '31']);
assert.equal(new Set(queue.map(item => item.key)).size, 1, 'both lesson plays reuse one unique audio key');
assert.equal(queue[0].reading, 'いのち');
assert.equal(queue[0].meaning, 'life');

const oneLessonQueue = buildListeningQueue(new Set(['07']));
assert.equal(oneLessonQueue.length, 1, 'one selected lesson produces one occurrence');
assert.equal(buildListeningQueue(new Set()).length, 0, 'no selection creates no queue');

console.log('Listening queue tests passed: repeats once per selected lesson, one unique audio key reused.');
