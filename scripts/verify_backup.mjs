/* =======================================================
   NIHONGO INTERMEDIATE — verify_backup.mjs
   Node.js Test Harness for backup.js
   Tests export/import roundtrip, JSON validation,
   merge rules, and snapshot create/restore.
   ======================================================= */

import assert from 'node:assert';

// 1. In-memory mock for localStorage
class MockLocalStorage {
  constructor() {
    this.store = new Map();
  }
  getItem(key) {
    return this.store.has(String(key)) ? this.store.get(String(key)) : null;
  }
  setItem(key, value) {
    this.store.set(String(key), String(value));
  }
  removeItem(key) {
    this.store.delete(String(key));
  }
  clear() {
    this.store.clear();
  }
  get length() {
    return this.store.size;
  }
  key(index) {
    const keys = Array.from(this.store.keys());
    return keys[index] || null;
  }
}

// Set up globals before importing module
globalThis.localStorage = new MockLocalStorage();
globalThis.window = globalThis;
globalThis.window.__n3ScheduleSync = () => {};
globalThis.window.updateSidebarStats = () => {};

// 2. Import backup module and state
const {
  exportBackup,
  importBackup,
  createSnapshot,
  restoreSnapshot,
  STORAGE_KEYS,
  SNAPSHOT_PREFIX,
  PREIMPORT_SNAPSHOT_KEY
} = await import('../js/backup.js');

const { state } = await import('../js/state.js');

console.log('--- Starting verify_backup.mjs suite ---');

// Test 1: Window bindings
console.log('Test 1: Verify window global bindings...');
assert.strictEqual(typeof window.exportBackup, 'function', 'window.exportBackup must be bound');
assert.strictEqual(typeof window.importBackup, 'function', 'window.importBackup must be bound');
assert.strictEqual(typeof window.createSnapshot, 'function', 'window.createSnapshot must be bound');
assert.strictEqual(typeof window.restoreSnapshot, 'function', 'window.restoreSnapshot must be bound');
console.log('✓ Test 1 passed: All window bindings registered.');

// Test 2: Validation of invalid JSON / schemas
console.log('Test 2: Validation of invalid inputs...');
{
  const r1 = importBackup('invalid json syntax {');
  assert.strictEqual(r1.success, false, 'Invalid JSON string should fail');
  assert.ok(r1.error.includes('Invalid JSON'), 'Error should mention Invalid JSON');

  const r2 = importBackup('{"schema": 1, "stats": {}}');
  assert.strictEqual(r2.success, false, 'Schema 1 should fail schema validation');
  assert.ok(r2.error.includes('schema'), 'Error should mention schema');

  const r3 = importBackup('{"schema": 2, "stats": "not-an-object"}');
  assert.strictEqual(r3.success, false, 'Non-object stats should fail');
  assert.ok(r3.error.includes('stats'), 'Error should mention stats');

  const r4 = importBackup('{"schema": 2, "stats": [1, 2, 3]}');
  assert.strictEqual(r4.success, false, 'Array stats should fail');

  const r5 = importBackup('');
  assert.strictEqual(r5.success, false, 'Empty backup input should fail');

  const r6 = importBackup('{"schema": 2}');
  assert.strictEqual(r6.success, false, 'Missing stats should fail');
}
console.log('✓ Test 2 passed: All invalid inputs rejected safely without exceptions.');

// Test 3: Export structure and content
console.log('Test 3: Export backup format...');
{
  localStorage.clear();
  state.stats = {
    'V:v01-001': { correct: 4, incorrect: 1, reps: 5, lastSeen: 1728800000000, interval: 3 },
    'K:日': { correct: 2, incorrect: 0, reps: 2, lastSeen: 1728810000000, interval: 1 }
  };
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(state.stats));
  localStorage.setItem(STORAGE_KEYS.SETTINGS, JSON.stringify({ examDate: '2026-12-13', studyDays: 6 }));
  localStorage.setItem(STORAGE_KEYS.DAYLOG, JSON.stringify({ '2026-10-14': { reviews: 42 } }));
  localStorage.setItem(STORAGE_KEYS.META, JSON.stringify({ schema: 2, migratedAt: 1728800000000 }));

  const rawExport = exportBackup();
  assert.strictEqual(typeof rawExport, 'string', 'exportBackup must return string');

  const parsed = JSON.parse(rawExport);
  assert.strictEqual(parsed.schema, 2, 'Exported schema must be 2');
  assert.ok(parsed.exportedAt, 'ExportedAt timestamp must exist');
  assert.strictEqual(typeof parsed.exportedAt, 'number', 'ExportedAt must be a numeric timestamp');
  assert.deepStrictEqual(parsed.stats, state.stats, 'Exported stats must match state.stats');
  assert.strictEqual(parsed.settings.studyDays, 6, 'Exported settings must match');
  assert.strictEqual(parsed.daylog['2026-10-14'].reviews, 42, 'Exported daylog must match');
  assert.strictEqual(parsed.meta.schema, 2, 'Exported meta must match');
}
console.log('✓ Test 3 passed: exportBackup output matches schema 2.');

// Test 4: Preimport safety snapshot
console.log('Test 4: Preimport safety snapshot creation...');
{
  localStorage.clear();
  state.stats = {
    'INITIAL:KEY': { correct: 10, reps: 10, lastSeen: 500 }
  };
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(state.stats));

  const incomingPayload = JSON.stringify({
    schema: 2,
    stats: {
      'NEW:KEY': { correct: 1, reps: 1, lastSeen: 600 }
    }
  });

  const res = importBackup(incomingPayload, { merge: false });
  assert.strictEqual(res.success, true, 'Import should succeed');

  const preimportRaw = localStorage.getItem(PREIMPORT_SNAPSHOT_KEY);
  assert.ok(preimportRaw, 'Preimport snapshot key must exist in localStorage');

  const preimport = JSON.parse(preimportRaw);
  assert.ok(preimport.stats['INITIAL:KEY'], 'Preimport snapshot must preserve data before mutation');
  assert.strictEqual(preimport.stats['INITIAL:KEY'].reps, 10);
}
console.log('✓ Test 4 passed: Preimport snapshot taken before writing.');

// Test 5: Snapshot create and restore
console.log('Test 5: Snapshot create and restore...');
{
  localStorage.clear();
  state.stats = {
    'SNAP:ITEM1': { correct: 7, reps: 7, lastSeen: 1234 }
  };
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(state.stats));

  const snapRes = createSnapshot('checkpoint_1');
  assert.strictEqual(snapRes.success, true, 'createSnapshot should succeed');
  assert.ok(localStorage.getItem(`${SNAPSHOT_PREFIX}checkpoint_1`), 'Snapshot item must be stored');

  // Corrupt state & storage
  state.stats = { 'CORRUPTED': { reps: 0 } };
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(state.stats));

  // Restore snapshot
  const restoreRes = restoreSnapshot('checkpoint_1');
  assert.strictEqual(restoreRes.success, true, 'restoreSnapshot should succeed');
  assert.strictEqual(restoreRes.count, 1, 'Restored count should be 1');
  assert.ok(state.stats['SNAP:ITEM1'], 'Restored state must match snapshotted stats');
  assert.strictEqual(state.stats['SNAP:ITEM1'].reps, 7);

  // Restore non-existent snapshot
  const missingRes = restoreSnapshot('does_not_exist');
  assert.strictEqual(missingRes.success, false, 'Restoring missing snapshot should fail');
  assert.ok(missingRes.error.includes('not found'), 'Error should state snapshot not found');
}
console.log('✓ Test 5 passed: Snapshot create and restore functional.');

// Test 6: Import with merge = true (keeping newer lastSeen or higher reps)
console.log('Test 6: Import with merge = true...');
{
  localStorage.clear();
  state.stats = {
    'ITEM:NEWER_LOCAL': { correct: 5, incorrect: 1, reps: 6, lastSeen: 2000, interval: 4 },
    'ITEM:NEWER_INCOMING': { correct: 2, incorrect: 0, reps: 2, lastSeen: 1000, interval: 1 },
    'ITEM:TIED_LASTSEEN': { correct: 1, incorrect: 0, reps: 2, lastSeen: 1500, interval: 1 },
    'ITEM:LOCAL_ONLY': { correct: 8, reps: 8, lastSeen: 1200 }
  };
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(state.stats));

  const incomingStats = {
    'ITEM:NEWER_LOCAL': { correct: 3, incorrect: 0, reps: 3, lastSeen: 1800, interval: 2 }, // older incoming -> local wins
    'ITEM:NEWER_INCOMING': { correct: 4, incorrect: 1, reps: 5, lastSeen: 3000, interval: 5 }, // newer incoming -> incoming wins
    'ITEM:TIED_LASTSEEN': { correct: 3, incorrect: 2, reps: 6, lastSeen: 1500, interval: 3 }, // tied lastSeen, higher reps -> incoming wins
    'ITEM:INCOMING_ONLY': { correct: 2, reps: 2, lastSeen: 2500 } // new item -> added
  };

  const incomingPayload = JSON.stringify({
    schema: 2,
    stats: incomingStats
  });

  const res = importBackup(incomingPayload, { merge: true });
  assert.strictEqual(res.success, true);
  assert.strictEqual(res.count, 5, 'Should have 5 total merged items');

  // Verify ITEM:NEWER_LOCAL kept local interval & lastSeen, but took max correct
  const newerLocal = state.stats['ITEM:NEWER_LOCAL'];
  assert.strictEqual(newerLocal.lastSeen, 2000, 'Local lastSeen should win');
  assert.strictEqual(newerLocal.interval, 4, 'Local interval should win');
  assert.strictEqual(newerLocal.correct, 5, 'Max correct preserved');

  // Verify ITEM:NEWER_INCOMING incoming won
  const newerIncoming = state.stats['ITEM:NEWER_INCOMING'];
  assert.strictEqual(newerIncoming.lastSeen, 3000, 'Incoming lastSeen should win');
  assert.strictEqual(newerIncoming.interval, 5, 'Incoming interval should win');
  assert.strictEqual(newerIncoming.reps, 5, 'Incoming reps should win');

  // Verify ITEM:TIED_LASTSEEN higher reps won
  const tied = state.stats['ITEM:TIED_LASTSEEN'];
  assert.strictEqual(tied.reps, 6, 'Higher incoming reps should win on tie');
  assert.strictEqual(tied.interval, 3, 'Incoming winner properties retained');
  assert.strictEqual(tied.correct, 3, 'Max correct preserved');

  // Verify items unique to local and incoming both exist
  assert.ok(state.stats['ITEM:LOCAL_ONLY'], 'Local-only item must be preserved');
  assert.ok(state.stats['ITEM:INCOMING_ONLY'], 'Incoming-only item must be added');
}
console.log('✓ Test 6 passed: Stats merge logic verified.');

// Test 7: Import with merge = false (overwrite)
console.log('Test 7: Import with merge = false (overwrite)...');
{
  localStorage.clear();
  state.stats = {
    'OLD_ITEM_1': { reps: 5 },
    'OLD_ITEM_2': { reps: 8 }
  };
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(state.stats));

  const overwritePayload = JSON.stringify({
    schema: 2,
    stats: {
      'NEW_ONLY': { reps: 1, lastSeen: 500 }
    }
  });

  const res = importBackup(overwritePayload, { merge: false });
  assert.strictEqual(res.success, true);
  assert.strictEqual(res.count, 1);
  assert.strictEqual(state.stats['OLD_ITEM_1'], undefined, 'Old item 1 should be gone on overwrite');
  assert.strictEqual(state.stats['OLD_ITEM_2'], undefined, 'Old item 2 should be gone on overwrite');
  assert.ok(state.stats['NEW_ONLY'], 'New item should be present');
}
console.log('✓ Test 7 passed: Overwrite import replaces all stats.');

// Test 8: Export -> Import roundtrip on fresh state
console.log('Test 8: Export -> Import full roundtrip...');
{
  localStorage.clear();
  const sampleStats = {
    'V:v05-012': { correct: 12, incorrect: 2, reps: 14, lastSeen: 1729000000000, lapses: 1, leech: false },
    'R_Q:passage1_q1': { correct: 3, incorrect: 1, reps: 4, lastSeen: 1729005000000 }
  };
  const sampleSettings = { examDate: '2026-12-13', studyDays: 6, timeBudgetMin: 45 };
  const sampleDaylog = { '2026-10-14': { reviews: 84, new: 22, ms: 1260000 } };
  const sampleMeta = { schema: 2, migratedAt: 1728000000000 };

  state.stats = sampleStats;
  localStorage.setItem(STORAGE_KEYS.STATS, JSON.stringify(sampleStats));
  localStorage.setItem(STORAGE_KEYS.SETTINGS, JSON.stringify(sampleSettings));
  localStorage.setItem(STORAGE_KEYS.DAYLOG, JSON.stringify(sampleDaylog));
  localStorage.setItem(STORAGE_KEYS.META, JSON.stringify(sampleMeta));

  // Export 1
  const exportedJson1 = exportBackup();

  // Wipe clean
  localStorage.clear();
  state.stats = {};

  // Import into fresh state
  const importRes = importBackup(exportedJson1, { merge: false });
  assert.strictEqual(importRes.success, true);
  assert.deepStrictEqual(state.stats, sampleStats, 'Imported stats must equal sample stats');

  // Export 2
  const exportedJson2 = exportBackup();
  const parsed1 = JSON.parse(exportedJson1);
  const parsed2 = JSON.parse(exportedJson2);

  assert.deepStrictEqual(parsed2.stats, parsed1.stats, 'Stats must roundtrip identically');
  assert.deepStrictEqual(parsed2.settings, parsed1.settings, 'Settings must roundtrip identically');
  assert.deepStrictEqual(parsed2.daylog, parsed1.daylog, 'Daylog must roundtrip identically');
  assert.strictEqual(parsed2.schema, 2);
}
console.log('✓ Test 8 passed: Full export -> import roundtrip complete.');

console.log('\n========================================');
console.log('ALL VERIFY_BACKUP TESTS PASSED SUCCESSFULLY!');
console.log('========================================\n');
