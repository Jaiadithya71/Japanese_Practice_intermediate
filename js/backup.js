/* =======================================================
   NIHONGO INTERMEDIATE — backup.js
   Full Data Export, Safe Import with Merging, and Snapshots
   ======================================================= */

import { state } from './state.js';

export const STORAGE_KEYS = {
  STATS: 'nihongo_intermediate_stats_v1',
  SETTINGS: 'nihongo_intermediate_settings_v1',
  DAYLOG: 'nihongo_intermediate_daylog_v1',
  META: 'nihongo_intermediate_meta_v1'
};

export const SNAPSHOT_PREFIX = 'nihongo_intermediate_snapshot_';
export const PREIMPORT_SNAPSHOT_TAG = 'preimport';
export const PREIMPORT_SNAPSHOT_KEY = 'nihongo_intermediate_snapshot_preimport';

function getStorageItem(key) {
  try {
    if (typeof localStorage !== 'undefined' && localStorage) {
      return localStorage.getItem(key);
    }
  } catch (err) {
    console.warn(`[backup] Error reading ${key} from localStorage:`, err);
  }
  return null;
}

function setStorageItem(key, value) {
  try {
    if (typeof localStorage !== 'undefined' && localStorage) {
      localStorage.setItem(key, value);
    }
  } catch (err) {
    console.error(`[backup] Error writing ${key} to localStorage:`, err);
  }
}

function parseJsonSafe(raw, fallback = {}) {
  if (!raw) return fallback;
  try {
    const val = JSON.parse(raw);
    return val !== null && typeof val === 'object' ? val : fallback;
  } catch (_) {
    return fallback;
  }
}

function gatherStats() {
  if (state && state.stats && typeof state.stats === 'object' && Object.keys(state.stats).length > 0) {
    return state.stats;
  }
  const raw = getStorageItem(STORAGE_KEYS.STATS);
  if (raw) {
    return parseJsonSafe(raw, {});
  }
  return (state && state.stats && typeof state.stats === 'object') ? state.stats : {};
}

function gatherSettings() {
  if (state && state.settings && typeof state.settings === 'object' && Object.keys(state.settings).length > 0) {
    return state.settings;
  }
  const raw = getStorageItem(STORAGE_KEYS.SETTINGS);
  if (raw) {
    return parseJsonSafe(raw, {});
  }
  return (state && state.settings && typeof state.settings === 'object') ? state.settings : {};
}

function gatherDaylog() {
  if (state && state.daylog && typeof state.daylog === 'object' && Object.keys(state.daylog).length > 0) {
    return state.daylog;
  }
  const raw = getStorageItem(STORAGE_KEYS.DAYLOG);
  if (raw) {
    return parseJsonSafe(raw, {});
  }
  return (state && state.daylog && typeof state.daylog === 'object') ? state.daylog : {};
}

function gatherMeta() {
  if (state && state.meta && typeof state.meta === 'object' && Object.keys(state.meta).length > 0) {
    return state.meta;
  }
  const raw = getStorageItem(STORAGE_KEYS.META);
  if (raw) {
    return parseJsonSafe(raw, { schema: 2 });
  }
  return (state && state.meta && typeof state.meta === 'object') ? state.meta : { schema: 2 };
}

/**
 * Gathers stats, settings, daylog, and meta from localStorage or state.
 * Returns a formatted JSON string with schema: 2.
 */
export function exportBackup() {
  const stats = gatherStats();
  const settings = gatherSettings();
  const daylog = gatherDaylog();
  const meta = gatherMeta();

  const backupData = {
    schema: 2,
    exportedAt: Date.now(),
    stats,
    settings,
    daylog,
    meta
  };

  return JSON.stringify(backupData, null, 2);
}

/**
 * Creates a safety snapshot of current state and stores it under
 * localStorage key `nihongo_intermediate_snapshot_<tag>`.
 */
export function createSnapshot(tag) {
  if (!tag) {
    tag = `manual_${Date.now()}`;
  }
  const key = `${SNAPSHOT_PREFIX}${tag}`;
  const stats = gatherStats();
  const settings = gatherSettings();
  const daylog = gatherDaylog();
  const meta = gatherMeta();

  const snapshot = {
    tag,
    createdAt: Date.now(),
    schema: 2,
    stats,
    settings,
    daylog,
    meta
  };

  setStorageItem(key, JSON.stringify(snapshot, null, 2));

  // Maintain snapshot history in meta if available
  try {
    const currentMeta = { ...meta };
    if (!Array.isArray(currentMeta.snapshots)) currentMeta.snapshots = [];
    if (!currentMeta.snapshots.includes(tag)) {
      currentMeta.snapshots = [tag, ...currentMeta.snapshots].slice(0, 5);
      setStorageItem(STORAGE_KEYS.META, JSON.stringify(currentMeta));
      if (typeof state !== 'undefined' && state) state.meta = currentMeta;
    }
  } catch (_) {}

  return { success: true, tag, key };
}

/**
 * Restores a snapshot from localStorage key `nihongo_intermediate_snapshot_<tag>`.
 * Updates localStorage and state.stats.
 */
export function restoreSnapshot(tag) {
  if (!tag) {
    return { success: false, error: 'Snapshot tag is required' };
  }
  const key = `${SNAPSHOT_PREFIX}${tag}`;
  const raw = getStorageItem(key);
  if (!raw) {
    return { success: false, error: `Snapshot not found: ${tag}` };
  }

  let snapshot;
  try {
    snapshot = JSON.parse(raw);
  } catch (err) {
    return { success: false, error: `Failed to parse snapshot: ${err.message}` };
  }

  if (!snapshot || typeof snapshot !== 'object') {
    return { success: false, error: 'Invalid snapshot format' };
  }

  // Support both full snapshot structure and raw stats mapping
  const stats = (snapshot.stats && typeof snapshot.stats === 'object' && !Array.isArray(snapshot.stats))
    ? snapshot.stats
    : snapshot;

  setStorageItem(STORAGE_KEYS.STATS, JSON.stringify(stats));
  if (typeof state !== 'undefined' && state) {
    state.stats = stats;
  }

  if (snapshot.settings && typeof snapshot.settings === 'object' && !Array.isArray(snapshot.settings)) {
    setStorageItem(STORAGE_KEYS.SETTINGS, JSON.stringify(snapshot.settings));
    if (typeof state !== 'undefined' && state) state.settings = snapshot.settings;
  }

  if (snapshot.daylog && typeof snapshot.daylog === 'object' && !Array.isArray(snapshot.daylog)) {
    setStorageItem(STORAGE_KEYS.DAYLOG, JSON.stringify(snapshot.daylog));
    if (typeof state !== 'undefined' && state) state.daylog = snapshot.daylog;
  }

  if (snapshot.meta && typeof snapshot.meta === 'object' && !Array.isArray(snapshot.meta)) {
    setStorageItem(STORAGE_KEYS.META, JSON.stringify(snapshot.meta));
    if (typeof state !== 'undefined' && state) state.meta = snapshot.meta;
  }

  if (typeof window !== 'undefined') {
    if (typeof window.__n3ScheduleSync === 'function') window.__n3ScheduleSync();
    if (typeof window.updateSidebarStats === 'function') window.updateSidebarStats();
  }

  return { success: true, count: Object.keys(stats).length };
}

/**
 * Imports a backup JSON string with schema validation and safety snapshots.
 * If merge is true, keeps newer lastSeen or higher reps on tie; if false, overwrites.
 * Takes a safety snapshot to `nihongo_intermediate_snapshot_preimport` before writing.
 */
export function importBackup(jsonString, options = { merge: true }) {
  const { merge = true } = options || {};

  if (!jsonString) {
    return { success: false, error: 'Empty backup data provided' };
  }

  let data;
  try {
    data = typeof jsonString === 'string' ? JSON.parse(jsonString) : jsonString;
  } catch (err) {
    return { success: false, error: `Invalid JSON: ${err.message}` };
  }

  if (!data || typeof data !== 'object' || Array.isArray(data)) {
    return { success: false, error: 'Backup root must be an object' };
  }

  if (Number(data.schema) !== 2) {
    return { success: false, error: `Unsupported backup schema: ${data.schema}. Expected schema 2.` };
  }

  if (!data.stats || typeof data.stats !== 'object' || Array.isArray(data.stats)) {
    return { success: false, error: 'Backup stats must be an object' };
  }

  // Pre-import safety snapshot before any mutation
  createSnapshot(PREIMPORT_SNAPSHOT_TAG);

  let finalStats;
  if (!merge) {
    finalStats = { ...data.stats };
  } else {
    // Current local stats
    const localStats = gatherStats();
    finalStats = { ...localStats };

    for (const [key, incomingItem] of Object.entries(data.stats)) {
      if (!incomingItem || typeof incomingItem !== 'object') continue;
      const existingItem = finalStats[key];
      if (!existingItem) {
        finalStats[key] = { ...incomingItem };
        continue;
      }

      const existLastSeen = existingItem.lastSeen || 0;
      const incomLastSeen = incomingItem.lastSeen || 0;
      const existReps = existingItem.reps || 0;
      const incomReps = incomingItem.reps || 0;

      let incomingWins = false;
      if (incomLastSeen > existLastSeen) {
        incomingWins = true;
      } else if (incomLastSeen < existLastSeen) {
        incomingWins = false;
      } else {
        // Tied lastSeen: higher reps wins
        incomingWins = incomReps > existReps;
      }

      const winner = incomingWins ? incomingItem : existingItem;

      finalStats[key] = {
        ...winner,
        correct: Math.max(existingItem.correct || 0, incomingItem.correct || 0),
        incorrect: Math.max(existingItem.incorrect || 0, incomingItem.incorrect || 0),
        reps: Math.max(existingItem.reps || 0, incomingItem.reps || 0)
      };

      if (existingItem.lapses !== undefined || incomingItem.lapses !== undefined) {
        finalStats[key].lapses = Math.max(existingItem.lapses || 0, incomingItem.lapses || 0);
      }
      if (existingItem.leech || incomingItem.leech) {
        finalStats[key].leech = true;
      }
    }
  }

  // Update storage & state
  setStorageItem(STORAGE_KEYS.STATS, JSON.stringify(finalStats));
  if (typeof state !== 'undefined' && state) {
    state.stats = finalStats;
  }

  // Optional settings sync
  if (data.settings && typeof data.settings === 'object' && !Array.isArray(data.settings)) {
    let finalSettings = data.settings;
    if (merge) {
      const curSettings = gatherSettings();
      finalSettings = { ...curSettings, ...data.settings };
    }
    setStorageItem(STORAGE_KEYS.SETTINGS, JSON.stringify(finalSettings));
    if (typeof state !== 'undefined' && state) {
      state.settings = finalSettings;
    }
  }

  // Optional daylog sync
  if (data.daylog && typeof data.daylog === 'object' && !Array.isArray(data.daylog)) {
    let finalDaylog = data.daylog;
    if (merge) {
      const curDaylog = gatherDaylog();
      finalDaylog = { ...curDaylog };
      for (const [dateKey, dayData] of Object.entries(data.daylog)) {
        if (!finalDaylog[dateKey]) {
          finalDaylog[dateKey] = dayData;
        } else if (typeof dayData === 'object' && dayData !== null) {
          const cur = finalDaylog[dateKey];
          finalDaylog[dateKey] = {
            ...cur,
            ...dayData,
            reviews: Math.max(cur.reviews || 0, dayData.reviews || 0),
            new: Math.max(cur.new || 0, dayData.new || 0),
            ms: Math.max(cur.ms || 0, dayData.ms || 0),
            sessions: Math.max(cur.sessions || 0, dayData.sessions || 0),
            wrong: Math.max(cur.wrong || 0, dayData.wrong || 0)
          };
        }
      }
    }
    setStorageItem(STORAGE_KEYS.DAYLOG, JSON.stringify(finalDaylog));
    if (typeof state !== 'undefined' && state) {
      state.daylog = finalDaylog;
    }
  }

  // Optional meta sync
  if (data.meta && typeof data.meta === 'object' && !Array.isArray(data.meta)) {
    let finalMeta = data.meta;
    if (merge) {
      const curMeta = gatherMeta();
      finalMeta = { ...curMeta, ...data.meta };
    }
    setStorageItem(STORAGE_KEYS.META, JSON.stringify(finalMeta));
    if (typeof state !== 'undefined' && state) {
      state.meta = finalMeta;
    }
  }

  if (typeof window !== 'undefined') {
    if (typeof window.__n3ScheduleSync === 'function') window.__n3ScheduleSync();
    if (typeof window.updateSidebarStats === 'function') window.updateSidebarStats();
  }

  return { success: true, count: Object.keys(finalStats).length };
}

/**
 * Browser helper to trigger JSON file download.
 */
export function downloadBackupFile() {
  if (typeof document === 'undefined' || typeof Blob === 'undefined') return;
  const jsonStr = exportBackup();
  const dateStr = new Date().toISOString().slice(0, 10);
  const blob = new Blob([jsonStr], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `nihongo-intermediate-backup-${dateStr}.json`;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    URL.revokeObjectURL(a.href);
    a.remove();
  }, 500);
}

// Bind to window if in browser environment
if (typeof window !== 'undefined') {
  window.exportBackup = exportBackup;
  window.importBackup = importBackup;
  window.createSnapshot = createSnapshot;
  window.restoreSnapshot = restoreSnapshot;
  window.downloadBackupFile = downloadBackupFile;
}
