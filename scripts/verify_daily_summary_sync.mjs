// Verifies the daily accountability summary (/api/day) reliability fixes:
//  1. The summary is built after max-merging the shared Gist daylog, so a
//     device with lower local totals never overwrites a higher merged day.
//  2. Failed/offline POSTs persist in a retry queue and are delivered later.
//  3. Permanent rejections (4xx) are not retried forever.
//  4. The proxy accepts yesterday in IST (sessions crossing midnight) and
//     forwards that date, but still rejects older dates.
import assert from 'node:assert/strict';

const DAYLOG_KEY = 'nihongo_intermediate_daylog_v1';
const QUEUE_KEY = 'n3_day_summary_queue_v1';
const istKey = (offsetDays = 0) => new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date(Date.now() - offsetDays * 86400000));
const today = istKey(0);
const yesterday = istKey(1);

const values = new Map([
  ['n3_github_pat', 'fake-token'],
  ['n3_gist_id', 'fake-gist'],
  [DAYLOG_KEY, JSON.stringify({ [today]: { date: today, reviews: 19, newCards: 0, minutes: 5, pillars: { vocab: 19, kanji: 0, grammar: 0, reading: 0 } } })]
]);
globalThis.localStorage = {
  getItem: key => values.has(key) ? values.get(key) : null,
  setItem: (key, value) => values.set(key, String(value)),
  removeItem: key => values.delete(key)
};
const listeners = new Map();
globalThis.window = { addEventListener: (name, fn) => listeners.set(name, fn) };
globalThis.document = { getElementById: () => null, addEventListener: () => {} };
Object.defineProperty(globalThis, 'navigator', { configurable: true, value: { onLine: true } });

const remoteDaylog = { [today]: { date: today, reviews: 102, newCards: 4, minutes: 24, pillars: { vocab: 0, kanji: 102, grammar: 0, reading: 0 } } };
const calls = [];
let postBehavior = { mode: 'ok' };
globalThis.fetch = async (url, options = {}) => {
  const method = options.method || 'GET';
  calls.push(`${method} ${url}`);
  if (url === '/api/day') {
    if (postBehavior.mode === 'fail') { const e = new Error('network down'); e.status = 0; throw e; }
    if (postBehavior.mode === 'reject') return { ok: false, status: 400, json: async () => ({ error: 'date must be today or yesterday in IST' }) };
    postBehavior.bodies = postBehavior.bodies || [];
    postBehavior.bodies.push(JSON.parse(options.body));
    return { ok: true, status: 200, json: async () => ({}) };
  }
  if (method === 'PATCH') return { ok: true, status: 200, json: async () => ({}) };
  return {
    ok: true, status: 200,
    json: async () => ({ files: {
      'nihongo-n3-stats.json': { content: '{}' },
      'nihongo-n3-daylog.json': { content: JSON.stringify(remoteDaylog) }
    } }),
    text: async () => '{}'
  };
};

const sync = await import('../js/gist-sync.js');

// 1. Session end: Gist daylog (102) is merged before the summary POST, so the
//    POST reports 102, not this device's local 19.
sync.beginGistReviewSession();
await sync.endGistReviewSession();
const postIndex = calls.findIndex(c => c.startsWith('POST /api/day'));
const gistGetIndex = calls.findIndex(c => c.startsWith('GET https://api.github.com/gists/'));
assert.ok(postIndex > -1, 'session end posts the daily summary');
assert.ok(gistGetIndex > -1 && gistGetIndex < postIndex, 'Gist daylog is pulled before the summary POST');
const firstPost = postBehavior.bodies[0];
assert.equal(firstPost.date, today);
assert.equal(firstPost.reviewsDone, 102, 'summary reports the merged day total, not the lower local one');
assert.equal(firstPost.minutes, 24, 'minutes take the merged daylog max over the local session timer');
assert.equal(values.has(QUEUE_KEY), false, 'successful POST leaves no queue');
console.log('1 passed: summary POST carries the max-merged day total (102, not local 19)');

// 2. Failed POST queues; flush delivers after recovery.
postBehavior.mode = 'fail';
sync.beginGistReviewSession();
await sync.endGistReviewSession();
let queue = JSON.parse(values.get(QUEUE_KEY) || '[]');
assert.equal(queue.length, 1, 'failed POST is queued');
assert.ok(queue[0].nextRetryAt > Date.now(), 'queued entry waits for its backoff window');
await sync.flushDailySummaryQueue();
assert.equal((postBehavior.bodies || []).length, 1, 'flush respects the backoff window');
queue = JSON.parse(values.get(QUEUE_KEY));
queue[0].nextRetryAt = 0;
values.set(QUEUE_KEY, JSON.stringify(queue));
postBehavior.mode = 'ok';
await sync.flushDailySummaryQueue();
assert.equal(postBehavior.bodies.length, 2, 'queued summary is delivered after recovery');
assert.equal(postBehavior.bodies[1].reviewsDone, 102, 'queued summary keeps the merged total');
assert.equal(values.has(QUEUE_KEY), false, 'queue clears after delivery');
console.log('2 passed: offline/failed summaries persist, back off, and deliver later');

// 3. A 4xx rejection is permanent; it is not queued or retried.
postBehavior.mode = 'reject';
sync.beginGistReviewSession();
await sync.endGistReviewSession();
assert.equal(values.has(QUEUE_KEY), false, '4xx rejection is not queued for retry');
postBehavior.mode = 'ok';
console.log('3 passed: permanent rejections are dropped, not retried');

// 4. Proxy accepts today and yesterday IST and forwards the posted date;
//    older dates are rejected.
const dayHandler = (await import('../api/day.js')).default;
const northstarCalls = [];
globalThis.fetch = async (url, options = {}) => {
  northstarCalls.push({ url, body: options.body && JSON.parse(options.body) });
  return { status: 200, text: async () => '{"ok":true}' };
};
const runProxy = async body => {
  const req = { method: 'POST', headers: { origin: 'https://nihongo-n3-study.vercel.app' }, body };
  let statusCode = 0; let payload = null;
  const res = { status(c) { statusCode = c; return this; }, setHeader() { return this; }, send(b) { payload = b; return this; } };
  await dayHandler(req, res);
  return { statusCode, payload: typeof payload === 'string' ? JSON.parse(payload) : payload };
};
const valid = extra => ({ date: today, reviewsDone: 5, uniqueItems: 4, sessions: 1, minutes: 3, chapters: ['Part 1: Topics'], units: ['T1: Greetings'], ...extra });

let r = await runProxy(valid());
assert.equal(r.statusCode, 200, 'today is accepted');
assert.equal(northstarCalls.at(-1).body.date, today);
r = await runProxy(valid({ date: yesterday }));
assert.equal(r.statusCode, 200, 'yesterday is accepted (session crossing midnight)');
assert.equal(northstarCalls.at(-1).body.date, yesterday, 'the posted date is forwarded, not rewritten to today');
assert.equal(northstarCalls.at(-1).body.changes[0].entryDate, yesterday);
r = await runProxy(valid({ date: istKey(2) }));
assert.equal(r.statusCode, 400, 'older dates are still rejected');
r = await runProxy(valid({ date: 'not-a-date' }));
assert.equal(r.statusCode, 400, 'malformed dates are rejected');
console.log('4 passed: proxy accepts today/yesterday IST, forwards the date, rejects older');

console.log('All daily-summary reliability checks passed.');
