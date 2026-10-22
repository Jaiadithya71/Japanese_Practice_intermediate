import assert from 'node:assert/strict';
// Two simulated devices sharing one fake Gist. Verifies stats + daylog merge without losing either side.
const gist = { files: {} };
const vals = new Map([['n3_github_pat', 'x'], ['n3_gist_id', 'g']]);
globalThis.localStorage = { getItem: k => vals.has(k) ? vals.get(k) : null, setItem: (k, v) => vals.set(k, String(v)), removeItem: k => vals.delete(k) };
const listeners = {};
globalThis.window = { addEventListener: (n, f) => { listeners[n] = f; } };
globalThis.document = { getElementById: () => null, addEventListener: (n, f) => { listeners['doc:' + n] = f; }, visibilityState: 'visible' };
Object.defineProperty(globalThis, 'navigator', { configurable: true, value: { onLine: true } });
globalThis.fetch = async (url, o = {}) => {
  if ((o.method || 'GET') === 'PATCH') {
    for (const [k, v] of Object.entries(JSON.parse(o.body).files)) gist.files[k] = { content: v.content };
    return { ok: true, status: 200, json: async () => ({}) };
  }
  return { ok: true, status: 200, json: async () => JSON.parse(JSON.stringify(gist)), text: async () => '{}' };
};
const sync = await import('../js/gist-sync.js');
const { state } = await import('../js/state.js');
const dl = await import('../js/daylog.js');
const enc = (await import('../js/stats-codec.js')).encodeStats;
// Remote (device B) already has progress + a day count of 40 and an item newer than local.
gist.files['nihongo-n3-stats.json'] = { content: enc({ 'V:b': { correct: 2, incorrect: 0, lastSeen: 200 } }) };
gist.files['nihongo-n3-daylog.json'] = { content: JSON.stringify({ '2026-10-21': { date: '2026-10-21', reviews: 40, newCards: 1, minutes: 9, pillars: { vocab: 40 } }, '2026-10-20': { date: '2026-10-20', reviews: 5 } }) };
// Local (device A): different item, lower count for 10-21, extra day 10-19.
state.stats = { 'V:a': { correct: 1, incorrect: 0, lastSeen: 100 } };
dl.saveDaylog({ '2026-10-21': { date: '2026-10-21', reviews: 12, newCards: 3, minutes: 2, pillars: { vocab: 12 } }, '2026-10-19': { date: '2026-10-19', reviews: 7 } });
sync.initSyncUI();
await new Promise(r => setTimeout(r, 50));
assert.ok(state.stats['V:a'] && state.stats['V:b'], 'both items present after pull');
const d = dl.loadDaylog();
assert.equal(d['2026-10-21'].reviews, 40, 'max reviews');
assert.equal(d['2026-10-21'].newCards, 3, 'max newCards');
assert.ok(d['2026-10-20'] && d['2026-10-19'], 'union of days');
assert.ok(vals.get('nihongo_intermediate_snapshot_presync_daylog'), 'backup snapshot taken before first merge');
// Push at review end, then check Gist holds the union.
sync.beginGistReviewSession(); sync.scheduleGistSave(); await sync.endGistReviewSession();
const g = JSON.parse(gist.files['nihongo-n3-daylog.json'].content);
assert.equal(g['2026-10-21'].reviews, 40); assert.ok(g['2026-10-19'] && g['2026-10-20']);
assert.ok(gist.files['nihongo-n3-stats.json'].content.includes('V:a') && gist.files['nihongo-n3-stats.json'].content.includes('V:b'), 'stats union uploaded');
// Visibility handler registered.
assert.equal(typeof listeners['doc:visibilitychange'], 'function');
console.log('two-device merge OK', Object.keys(d).sort());
