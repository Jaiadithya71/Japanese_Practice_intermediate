import assert from 'node:assert/strict';

const values = new Map([
  ['n3_github_pat', 'fake-token'],
  ['n3_gist_id', 'fake-gist']
]);
globalThis.localStorage = {
  getItem: key => values.has(key) ? values.get(key) : null,
  setItem: (key, value) => values.set(key, String(value)),
  removeItem: key => values.delete(key)
};
const listeners = new Map();
globalThis.window = { addEventListener: (name, fn) => listeners.set(name, fn) };
globalThis.document = { getElementById: () => null };
Object.defineProperty(globalThis, 'navigator', { configurable: true, value: { onLine: true } });
const patches = [];
globalThis.fetch = async (url, options = {}) => {
  if ((options.method || 'GET') === 'PATCH') {
    patches.push(JSON.parse(options.body).files['nihongo-n3-stats.json'].content);
    return { ok: true, status: 200, json: async () => ({}) };
  }
  return {
    ok: true,
    status: 200,
    json: async () => ({ files: { 'nihongo-n3-stats.json': { content: '{}' } } }),
    text: async () => '{}'
  };
};
const sync = await import('../js/gist-sync.js');
const { state } = await import('../js/state.js');
state.stats = { 'V:test': { correct: 1, lastSeen: 100 } };
sync.initSyncUI();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(patches.length, 0, 'initial pull may read but does not write');
sync.scheduleGistSave();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(patches.length, 0, 'local stats save does not upload');
sync.beginGistReviewSession();
sync.scheduleGistSave();
await sync.forceSyncNow();
assert.equal(patches.length, 0, 'Sync Now during a review cannot upload');
await sync.endGistReviewSession();
assert.equal(patches.length, 1, 'completed review uploads exactly once');
assert.ok(JSON.parse(patches[0]).$, 'upload uses compact stats codec');
sync.beginGistReviewSession();
sync.scheduleGistSave();
Object.defineProperty(navigator, 'onLine', { configurable: true, value: false });
await sync.endGistReviewSession();
assert.equal(patches.length, 1, 'offline completion queues without upload');
assert.equal(values.get('n3_gist_ready'), '1', 'offline completion persists queued state');
Object.defineProperty(navigator, 'onLine', { configurable: true, value: true });
listeners.get('online')();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(patches.length, 2, 'queued completed review uploads after reconnection');
assert.equal(values.has('n3_gist_dirty'), false, 'successful upload clears pending state');
// An interrupted review survives reload as pending local data, not a false completion.
sync.beginGistReviewSession();
sync.scheduleGistSave();
await import(`../js/gist-sync.js?restart=${Date.now()}`);
// The second module shares persistent storage but has independent in-memory activity state.
assert.equal(values.has('n3_gist_ready'), false, 'unfinished review does not become upload-ready on reload');
console.log('Gist sync policy checks passed: local saves defer writes; Sync Now cannot bypass active review; completion writes once; offline completion writes on reconnect.');
