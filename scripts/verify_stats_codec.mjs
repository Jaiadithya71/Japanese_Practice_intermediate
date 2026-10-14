import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const codecPath = new URL('../js/stats-codec.js', import.meta.url);
const { encodeStats, decodeStatsText, decodeStatsPayload } = await import(codecPath);
const fixture = {
  'V:v2-01-001': {
    correct: 0, incorrect: 0, weight: 1, reps: 0, interval: 0, easeFactor: 2.5,
    nextDue: 0, isHard: false, lapses: 0, streak: 0, learnState: 'learning',
    relearnBase: null, leech: false, firstSeen: 0, hist: [], note: '', cause: '', lastSeen: 0,
    customMeta: { source: 'fixture', flags: [true, 2] }
  },
  'KWR:水': {
    correct: 7, incorrect: 2, weight: 1.2, reps: 4, interval: 8, easeFactor: 2.35,
    nextDue: 1792000000000, isHard: true, lapses: 1, streak: 3, learnState: 'review',
    relearnBase: 5, leech: false, firstSeen: 1791000000000,
    hist: [[1791000000000, 3], [1791100000000, 1]], note: '例', cause: 'test-mistake',
    lastSeen: 1791200000000, reads: 4, bestAcc: .92, lastAcc: .9, bestCpm: 330,
    lastCpm: 320, step: 2, mastered: false
  },
  'R_Q:q1': {
    correct: 1, interval: 3,
    answerState: { selected: '二', flags: ['a', 'b'] },
    c: 'unknown alias collision', '~meta': 'escape reserved extension key'
  },
  'RW:reading-word': { reading: 'よみ', meaning: 'meaning', term: '読む', lastSeen: 1791200000000 }
};

const encoded = encodeStats(fixture);
assert.deepEqual(decodeStatsText(encoded), fixture, 'compact encode/decode must preserve every value and key');
assert.deepEqual(decodeStatsPayload(JSON.parse(JSON.stringify(fixture))), fixture, 'legacy verbose stats remain readable');
assert.ok(new TextEncoder().encode(encoded).length < new TextEncoder().encode(JSON.stringify(fixture)).length);
assert.throws(() => decodeStatsPayload({ $: 'n3s', v: 99, s: {} }), /unsupported/);
assert.throws(() => decodeStatsPayload({ $: 'n3s', v: 1, s: { bad: 'not a record' } }), /invalid shape/);
assert.throws(() => decodeStatsPayload({ $: 'other', v: 1, s: {} }), /unknown format/);

const defaultRecord = fixture['V:v2-01-001'];
const largeFixture = Object.fromEntries(Array.from({ length: 4469 }, (_, i) => [`V:${i}`, defaultRecord]));
const legacyBytes = new TextEncoder().encode(JSON.stringify(largeFixture)).length;
const compactBytes = new TextEncoder().encode(encodeStats(largeFixture)).length;
console.log(`stats-codec checks passed; fixture keys=${Object.keys(fixture).length}; legacy bytes=${new TextEncoder().encode(JSON.stringify(fixture)).length}; compact bytes=${new TextEncoder().encode(encoded).length}; 4469-record all-default projection=${legacyBytes} -> ${compactBytes} bytes (${(100*(1-compactBytes/legacyBytes)).toFixed(1)}% smaller)`);
