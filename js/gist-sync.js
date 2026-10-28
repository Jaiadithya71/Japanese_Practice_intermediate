/* =======================================================
   NIHONGO INTERMEDIATE - gist-sync.js
   Optional GitHub Gist sync for N3 progress (separate Gist
   from the N5/N4 app). Token stays in this browser only.
   ======================================================= */

import { STORAGE_KEY } from './config.js';
import { state } from './state.js';
import { updateSidebarStats } from './srs.js';
import { encodeStats, decodeStatsText } from './stats-codec.js';
import { getDay, loadDaylog, saveDaylog } from './daylog.js';

const GIST_FILENAME = 'nihongo-n3-stats.json';
const DAYLOG_FILENAME = 'nihongo-n3-daylog.json';
const PRESYNC_BACKUP_KEY = 'n3_presync_backup_done_v1';
const PAT_KEY = 'n3_github_pat';
const GIST_ID_KEY = 'n3_gist_id';
const DIRTY_KEY = 'n3_gist_dirty';
const READY_KEY = 'n3_gist_ready';
const ACTIVE_KEY = 'n3_gist_review_active';
const DAILY_SUMMARY_KEY = 'n3_day_summary_v1';
const SESSION_STARTED_KEY = 'n3_day_session_started';
const SESSION_ITEM_KEYS = 'n3_day_session_item_keys';
const SESSION_REVIEW_COUNT = 'n3_day_session_review_count';
const DAILY_SUMMARY_QUEUE_KEY = 'n3_day_summary_queue_v1';
const DAILY_SUMMARY_MAX_ATTEMPTS = 8;
const DAILY_SUMMARY_RETRY_DELAYS_MS = [60 * 1000, 5 * 60 * 1000, 15 * 60 * 1000, 60 * 60 * 1000];
const MAX_SYNC_BYTES = 1024 * 1024;

function markRemoteRepairRequired(message) {
  const error = new Error(message);
  error.remoteStatsRepair = true;
  return error;
}
const API = 'https://api.github.com';

let dirty = localStorage.getItem(DIRTY_KEY) === '1';
let reviewSessionActive = localStorage.getItem(ACTIVE_KEY) === '1';
let pushPromise = null;
let lastRemoteDaylog = null;
let changeRevision = 0;

function isReviewActive() {
  return reviewSessionActive || localStorage.getItem(ACTIVE_KEY) === '1';
}

function sanitizeCredential(key) {
  const stored = localStorage.getItem(key);
  if (stored == null) return null;
  // Header values must be Latin-1 and free of control characters. IDs/tokens
  // are ASCII; strip all whitespace/control/non-ASCII characters from pasted values.
  const cleaned = stored.replace(/[\s\x00-\x1F\x7F-\uFFFF]/g, '');
  if (cleaned !== stored) localStorage.setItem(key, cleaned);
  return cleaned;
}

function creds() {
  return { pat: sanitizeCredential(PAT_KEY), gistId: sanitizeCredential(GIST_ID_KEY) };
}

function headers(pat, json) {
  const h = { Authorization: `Bearer ${pat}`, Accept: 'application/vnd.github.v3+json' };
  if (json) h['Content-Type'] = 'application/json';
  return h;
}

function setStatus(kind, text) {
  if (typeof window !== 'undefined') window.__n3SyncStatus = { kind, text };
  const el = document.getElementById('n3sync-status');
  const label = document.getElementById('n3sync-label');
  if (el) {
    el.className = `n3s-pill n3s-${kind}`;
    el.title = text;
    el.setAttribute('aria-label', `Gist sync: ${text}`);
  }
  if (label) label.textContent = text;
  // The mobile Today header mirrors the desktop pill so connectivity is visible at a glance.
  const mobileIndicators = ['n3sync-mobile', 'n3sync-kanji'].map(id => document.getElementById(id)).filter(Boolean);
  for (const mobile of mobileIndicators) {
    mobile.classList.remove('n3s-idle', 'n3s-saving', 'n3s-ok', 'n3s-error', 'n3s-pending');
    mobile.classList.add(`n3s-${kind}`);
    mobile.title = text;
    mobile.setAttribute('aria-label', `Gist sync: ${text}`);
    const mobileLabel = mobile.querySelector('span');
    const mobileIcon = mobile.querySelector('i');
    if (mobileLabel) mobileLabel.textContent = ({ idle: 'Sync off', saving: 'Syncing…', ok: 'Synced', error: 'Sync error', pending: 'Pending' })[kind] || 'Sync';
    if (mobileIcon) {
      const mobileMap = { idle: 'fa-cloud', saving: 'fa-arrows-rotate fa-spin', ok: 'fa-circle-check', error: 'fa-triangle-exclamation', pending: 'fa-cloud-arrow-up' };
      mobileIcon.className = `fa-solid ${mobileMap[kind] || 'fa-cloud'}`;
    }
  }
  // Icon reflects state: cloud (idle), spinning arrows (working), check (synced), warning (error)
  const icon = el && el.querySelector('i');
  if (icon) {
    const map = { idle: 'fa-cloud', saving: 'fa-arrows-rotate fa-spin', ok: 'fa-circle-check', error: 'fa-triangle-exclamation', pending: 'fa-cloud-arrow-up' };
    icon.className = `fa-solid ${map[kind] || 'fa-cloud'}`;
  }
  const info = document.getElementById('n3s-info');
  if (info) info.textContent = text;
  const homeState = document.getElementById('home-sync-state');
  if (homeState) {
    homeState.className = `home-status-sync n3s-${kind}`;
    const labels = { idle: 'Sync off', saving: 'Syncing…', ok: 'Synced', error: 'Sync error', pending: 'Pending' };
    const icons = { idle: 'fa-cloud', saving: 'fa-arrows-rotate fa-spin', ok: 'fa-circle-check', error: 'fa-triangle-exclamation', pending: 'fa-cloud-arrow-up' };
    homeState.title = text;
    homeState.setAttribute('aria-label', `Gist sync: ${text}`);
    homeState.innerHTML = `<i class="fa-solid ${icons[kind] || icons.idle}"></i><span>${labels[kind] || 'Sync'}</span>`;
  }
}

function itemScore(s) {
  return (s.correct || 0) + (s.incorrect || 0);
}

// Merge remote stats into local: newer lastSeen wins; if tied, the entry with more reviews wins.
function mergeStats(remote) {
  let changed = false;
  Object.entries(remote || {}).forEach(([key, rs]) => {
    const ls = state.stats[key];
    if (!ls) { state.stats[key] = rs; changed = true; return; }
    const lt = ls.lastSeen || 0, rt = rs.lastSeen || 0;
    if (rt > lt || (rt === lt && itemScore(rs) > itemScore(ls))) {
      state.stats[key] = {
        ...rs,
        correct: Math.max(ls.correct || 0, rs.correct || 0),
        incorrect: Math.max(ls.incorrect || 0, rs.incorrect || 0)
      };
      changed = true;
    }
  });
  return changed;
}

// Per-day activity (heatmap, streak, daily review counts) lives in its own Gist file and merges by max,
// so a device never lowers a day's count and nothing is lost when two devices have diverged.
function mergeDaylogMax(remoteText) {
  if (!remoteText) return false;
  let remote;
  try { remote = JSON.parse(remoteText); } catch (_) { return false; }
  if (!remote || typeof remote !== 'object' || Array.isArray(remote)) return false;
  const local = loadDaylog();
  let changed = false;
  const mx = (a, b) => Math.max(Number(a) || 0, Number(b) || 0);
  for (const [date, r] of Object.entries(remote)) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !r || typeof r !== 'object') continue;
    const l = local[date];
    if (!l) { local[date] = r; changed = true; continue; }
    const merged = { ...l, date, reviews: mx(l.reviews, r.reviews), newCards: mx(l.newCards ?? l.new, r.newCards ?? r.new), minutes: mx(l.minutes, r.minutes),
      pillars: { vocab: mx(l.pillars?.vocab, r.pillars?.vocab), kanji: mx(l.pillars?.kanji, r.pillars?.kanji), grammar: mx(l.pillars?.grammar, r.pillars?.grammar), reading: mx(l.pillars?.reading, r.pillars?.reading) } };
    if (l.wrong !== undefined || r.wrong !== undefined) merged.wrong = mx(l.wrong, r.wrong);
    if (JSON.stringify(merged) !== JSON.stringify(l)) { local[date] = merged; changed = true; }
  }
  if (changed) saveDaylog(local);
  return changed;
}

async function backupBeforeFirstDaylogMerge() {
  if (localStorage.getItem(PRESYNC_BACKUP_KEY) === '1') return;
  try {
    const { createSnapshot } = await import('./backup.js');
    createSnapshot('presync_daylog');
    localStorage.setItem(PRESYNC_BACKUP_KEY, '1');
  } catch (e) { console.warn('[n3-sync] pre-sync backup failed:', e.message); }
}

function refreshViews() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.stats));
  updateSidebarStats();
  if (state.currentView && state.currentView !== 'study' && typeof window.showView === 'function') {
    window.showView(state.currentView);
  }
}

function serializeStats() {
  if (!state.stats || typeof state.stats !== 'object' || Array.isArray(state.stats)) {
    throw new Error('Local progress is not a valid stats object; nothing was written.');
  }
  // A versioned schema compacts repeated field names/defaults; codec round-trip validation is lossless.
  return encodeStats(state.stats);
}

function formatBytes(bytes) {
  if (bytes >= 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(2)} MiB`;
  if (bytes >= 1024) return `${(bytes / 1024).toFixed(1)} KiB`;
  return `${bytes} B`;
}

function localStatsSizeDiagnostic(payload) {
  const encoder = new TextEncoder();
  const records = Object.entries(state.stats || {});
  const groups = new Map();
  const largest = [];
  const fieldBytes = new Map();

  for (const [key, value] of records) {
    const bytes = encoder.encode(JSON.stringify([key, value])).length;
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      for (const [field, fieldValue] of Object.entries(value)) {
        const fieldSize = encoder.encode(JSON.stringify([field, fieldValue])).length;
        fieldBytes.set(field, (fieldBytes.get(field) || 0) + fieldSize);
      }
    }
    const colon = key.indexOf(':');
    const prefix = colon > 0 ? key.slice(0, colon) : '(no prefix)';
    const group = groups.get(prefix) || { bytes: 0, count: 0 };
    group.bytes += bytes;
    group.count++;
    groups.set(prefix, group);
    largest.push({ prefix, bytes });
  }

  const totalBytes = encoder.encode(payload).length;
  const byPrefix = [...groups.entries()]
    .sort((a, b) => b[1].bytes - a[1].bytes)
    .map(([prefix, group]) => `${prefix} ${formatBytes(group.bytes)} (${totalBytes ? Math.round(group.bytes / totalBytes * 100) : 0}%, ${group.count})`)
    .join('; ');
  const byField = [...fieldBytes.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([field, bytes]) => `${field} ${formatBytes(bytes)} (${totalBytes ? Math.round(bytes / totalBytes * 100) : 0}%)`)
    .join('; ');
  const largestRecords = largest
    .sort((a, b) => b.bytes - a.bytes)
    .slice(0, 5)
    .map(record => `${record.prefix} ${formatBytes(record.bytes)}`)
    .join(', ');

  return `Payload ${formatBytes(totalBytes)}; ${records.length} records; key-prefix bytes (approx): ${byPrefix || 'none'}; largest records by prefix: ${largestRecords || 'none'}; largest record fields (approx): ${byField || 'none'}`;
}

function localStatsTooLargeMessage(payload) {
  return `Local progress is over GitHub Gist's 1 MiB sync limit; nothing was written. ${localStatsSizeDiagnostic(payload)}`;
}

async function getRemoteContent(pat, gistId) {
  const delays = [2000, 5000, 10000];
  let gist;
  for (let attempt = 0; attempt <= delays.length; attempt++) {
    try {
      const res = await fetch(`${API}/gists/${gistId}?t=${Date.now()}`, { headers: headers(pat) });
      if (!res.ok) {
        if (res.status >= 400 && res.status < 500) throw new Error(`HTTP ${res.status}`);
        throw new Error(`HTTP ${res.status}`);
      }
      gist = await res.json();
      break;
    } catch (e) {
      if (e.message && /^HTTP 4\d\d$/.test(e.message)) throw e;
      if (attempt === delays.length) throw e;
      const attemptsLeft = delays.length - attempt;
      setStatus('saving', `Retrying… (${attemptsLeft} left)`);
      console.warn(`Gist pull attempt ${attempt + 1} failed (${e.message}), retrying in ${delays[attempt] / 1000}s`);
      await new Promise(resolve => setTimeout(resolve, delays[attempt]));
    }
  }
  const dayFile = gist.files && gist.files[DAYLOG_FILENAME];
  lastRemoteDaylog = dayFile && typeof dayFile.content === 'string' && !dayFile.truncated ? dayFile.content : null;
  const file = gist.files && gist.files[GIST_FILENAME];
  if (!file) throw new Error('The progress file is missing from the Gist; nothing was written.');
  let content = file.content;
  if (file.truncated && file.raw_url) {
    // Public Gists can be fetched without a token. Avoid Authorization here: raw.githubusercontent.com
    // rejects that CORS preflight, even though a top-level navigation to the URL works.
    let rawContent;
    try {
      const raw = await fetch(file.raw_url);
      if (!raw.ok) throw new Error(`HTTP ${raw.status}`);
      rawContent = await raw.text();
    } catch (error) {
      throw markRemoteRepairRequired(`Remote progress is truncated and the full raw file could not be read (${error.message || 'network error'}); use Sync Now to replace it with this device's validated stats.`);
    }
    content = rawContent;
    await parseRemoteStats(rawContent);
    throw markRemoteRepairRequired("Remote progress is truncated; use Sync Now to replace it with this device's validated stats.");
  }
  if (typeof content !== 'string' || !content.length) {
    throw new Error('The remote progress file is empty or unavailable; nothing was written.');
  }
  return content;
}

async function parseRemoteStats(content) {
  let remote;
  try {
    remote = decodeStatsText(content); // accepts legacy verbose stats and the compact versioned envelope
  } catch (e) {
    if (e instanceof SyntaxError) {
      e.remoteStatsParse = true;
      throw e;
    }
    // Unknown versions or invalid codec payloads are not grounds to replace remote data.
    throw e;
  }
  return remote;
}

async function pull(pat, gistId) {
  return parseRemoteStats(await getRemoteContent(pat, gistId));
}

async function push(pat, gistId, allowCorruptRemote = false) {
  if (pushPromise) {
    await pushPromise;
    if (dirty && !isReviewActive() && localStorage.getItem(READY_KEY) === '1') return push(pat, gistId, allowCorruptRemote);
    return !dirty;
  }
  const revision = changeRevision;
  pushPromise = pushOnce(pat, gistId, allowCorruptRemote, revision);
  try { return await pushPromise; } finally { pushPromise = null; }
}

async function pushOnce(pat, gistId, allowCorruptRemote = false, revision = changeRevision) {
  let payload;
  try {
    payload = serializeStats();
    const payloadBytes = new TextEncoder().encode(payload).length;
    if (payloadBytes >= MAX_SYNC_BYTES) {
      setStatus('error', localStatsTooLargeMessage(payload));
      console.info('[n3-sync] Local size diagnostic:', localStatsSizeDiagnostic(payload));
      return false;
    }
    const wrapped = JSON.stringify({ files: { [GIST_FILENAME]: { content: payload } } });
    JSON.parse(wrapped);
    const remoteContent = await getRemoteContent(pat, gistId);
    await backupBeforeFirstDaylogMerge();
    mergeDaylogMax(lastRemoteDaylog);
    try {
      await parseRemoteStats(remoteContent);
    } catch (e) {
      const isMalformed = e instanceof SyntaxError && e.remoteStatsParse === true;
      if (!(allowCorruptRemote && (isMalformed || e.remoteStatsRepair === true))) throw e;
    }
  } catch (e) {
    if (!(allowCorruptRemote && e.remoteStatsRepair === true)) {
      setStatus('error', 'Sync blocked: ' + e.message);
      return false;
    }
  }
  const delays = [2000, 5000, 10000];
  for (let i = 0; i <= delays.length; i++) {
    try {
      if (isReviewActive()) {
        setStatus('pending', 'Review active · syncs when it ends');
        return false;
      }
      const res = await fetch(`${API}/gists/${gistId}`, {
        method: 'PATCH',
        headers: headers(pat, true),
        body: JSON.stringify({ files: { [GIST_FILENAME]: { content: payload }, [DAYLOG_FILENAME]: { content: JSON.stringify(loadDaylog()) } } })
      });
      if (res.ok) {
        if (revision === changeRevision) {
          dirty = false;
          localStorage.removeItem(DIRTY_KEY);
          localStorage.removeItem(READY_KEY);
        } else {
          dirty = true;
          localStorage.setItem(DIRTY_KEY, '1');
        }
        state.lastSyncTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        setStatus(dirty ? 'pending' : 'ok', dirty ? 'New review changes still pending' : `Synced ${state.lastSyncTime}`);
        if (dirty && !isReviewActive() && localStorage.getItem(READY_KEY) === '1') {
          queueMicrotask(() => push(pat, gistId, allowCorruptRemote));
        }
        return true;
      }
      if (res.status >= 400 && res.status < 500) {
        setStatus('error', `Sync failed: HTTP ${res.status}`);
        return false;
      }
      throw new Error(`HTTP ${res.status}`);
    } catch (e) {
      if (i === delays.length) { setStatus('error', `Sync failed: ${e.message}`); return false; }
      setStatus('saving', 'Retrying…');
      await new Promise(r => setTimeout(r, delays[i]));
    }
  }
  return false;
}

// Local review progress is queued; only an explicit review end or Sync Now writes the Gist.
export function scheduleGistSave() {
  const { pat, gistId } = creds();
  if (!pat || !gistId) return;
  dirty = true;
  changeRevision++;
  localStorage.setItem(DIRTY_KEY, '1');
  if (!navigator.onLine) setStatus('pending', 'Offline · saved on this device');
  else if (isReviewActive()) setStatus('pending', 'Review active · syncs when it ends');
  else setStatus('pending', 'Sync pending · ends with a review');
}

function istDateKeyFor(timestamp = Date.now()) {
  const d = new Date(timestamp);
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit' }).format(d);
}

function daySessionTotals(date, elapsedMs) {
  const prior = (() => { try { return JSON.parse(localStorage.getItem(DAILY_SUMMARY_KEY) || '{}'); } catch (_) { return {}; } })();
  const row = prior[date] || { sessions: 0, elapsedMs: 0 };
  row.sessions = Math.min(1000, (row.sessions || 0) + 1);
  row.elapsedMs = Math.min(600 * 60 * 1000, (row.elapsedMs || 0) + Math.max(0, elapsedMs));
  prior[date] = row;
  try { localStorage.setItem(DAILY_SUMMARY_KEY, JSON.stringify(prior)); } catch (_) {}
  return row;
}

// Daily accountability summaries POST to /api/day, which is best-effort:
// the northstar dashboard stores the last POST it receives. Failed or offline
// summaries persist here and retry with backoff until delivered, permanently
// rejected (4xx), or attempts run out. Study records themselves live in the
// Gist daylog, which merges by max and is never affected by this queue.
function readDailySummaryQueue() {
  try {
    const queue = JSON.parse(localStorage.getItem(DAILY_SUMMARY_QUEUE_KEY) || '[]');
    return Array.isArray(queue) ? queue : [];
  } catch (_) { return []; }
}

function writeDailySummaryQueue(queue) {
  try {
    if (queue.length) localStorage.setItem(DAILY_SUMMARY_QUEUE_KEY, JSON.stringify(queue));
    else localStorage.removeItem(DAILY_SUMMARY_QUEUE_KEY);
  } catch (_) {}
}

function enqueueDailySummary(summary) {
  const queue = readDailySummaryQueue().filter(entry => entry && entry.summary && entry.summary.date !== summary.date);
  queue.push({ summary, attempts: 0, nextRetryAt: Date.now() + DAILY_SUMMARY_RETRY_DELAYS_MS[0] });
  writeDailySummaryQueue(queue);
}

async function postDailySummary(summary) {
  const response = await fetch('/api/day', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(summary)
  });
  if (!response.ok) {
    const error = new Error(`HTTP ${response.status}`);
    error.status = response.status;
    throw error;
  }
  const result = await response.json().catch(() => ({}));
  if (result.error) {
    const error = new Error(result.error);
    error.status = response.status;
    throw error;
  }
}

export async function flushDailySummaryQueue() {
  const queue = readDailySummaryQueue();
  if (!queue.length || !navigator.onLine) return false;
  const remaining = [];
  let delivered = 0;
  for (const entry of queue) {
    if (!entry || !entry.summary) continue;
    if (Date.now() < (entry.nextRetryAt || 0)) { remaining.push(entry); continue; }
    try {
      await postDailySummary(entry.summary);
      delivered++;
    } catch (error) {
      const status = Number(error.status) || 0;
      const attempts = (entry.attempts || 0) + 1;
      // 4xx means the proxy will never accept this summary (e.g. the date is
      // too old); retrying cannot help, and the Gist daylog still holds the day.
      if ((status >= 400 && status < 500) || attempts >= DAILY_SUMMARY_MAX_ATTEMPTS) {
        console.warn(`[n3-sync] Daily summary for ${entry.summary.date} not deliverable (${error.message}); dropped from retry queue.`);
        continue;
      }
      const delay = DAILY_SUMMARY_RETRY_DELAYS_MS[Math.min(attempts - 1, DAILY_SUMMARY_RETRY_DELAYS_MS.length - 1)];
      remaining.push({ ...entry, attempts, nextRetryAt: Date.now() + delay });
    }
  }
  writeDailySummaryQueue(remaining);
  return delivered > 0 || remaining.length === 0;
}

// Read only the shared daylog file from the Gist. Best-effort: any failure
// returns null and the summary falls back to this device's local totals.
async function pullRemoteDaylog(pat, gistId) {
  try {
    const res = await fetch(`${API}/gists/${gistId}?t=${Date.now()}`, { headers: headers(pat) });
    if (!res.ok) return null;
    const gist = await res.json();
    const dayFile = gist.files && gist.files[DAYLOG_FILENAME];
    if (!dayFile) return null;
    if (dayFile.truncated && dayFile.raw_url) {
      try {
        const raw = await fetch(dayFile.raw_url);
        if (raw.ok) return await raw.text();
      } catch (_) {}
      return null;
    }
    return typeof dayFile.content === 'string' ? dayFile.content : null;
  } catch (_) { return null; }
}

function buildDailySummary(date) {
  const touched = new Set();
  const chapters = new Set();
  const units = new Set();
  const wordChapter = new Map();
  for (const [chapterId, words] of Object.entries(state.vocabDB || {})) {
    for (const word of words || []) wordChapter.set(word.id, chapterId);
  }
  for (const [key, stats] of Object.entries(state.stats || {})) {
    if (!stats || istDateKeyFor(Number(stats.lastSeen || 0)) !== date) continue;
    // SRS history distinguishes reviewed items from test-mistake lastSeen updates.
    const reviewedToday = Array.isArray(stats.hist) && stats.hist.some(entry => Array.isArray(entry) && istDateKeyFor(Number(entry[0] || 0)) === date);
    if (!reviewedToday) continue;
    touched.add(key);
    if (!key.startsWith('V:')) continue;
    const wordId = key.slice(2).replace(/:rev$/, '');
    const chapterId = wordChapter.get(wordId);
    if (!chapterId) continue;
    const meta = state.chapterMetadata?.[chapterId] || {};
    const part = chapterId.startsWith('part2_') ? 'Part 2: Characteristics' : 'Part 1: Topics';
    chapters.add(part);
    const chapterNum = chapterId.startsWith('part2_') ? `C${chapterId.slice(6)}` : `T${chapterId}`;
    units.add(`${chapterNum}: ${meta.topic_en || meta.topic_ja || chapterNum}`);
  }
  const allDaily = (() => { try { return JSON.parse(localStorage.getItem(DAILY_SUMMARY_KEY) || '{}'); } catch (_) { return {}; } })();
  const local = allDaily[date] || {};
  const reviewsDone = date === istDateKeyFor() ? Math.max(Number(getDay(date).reviews) || 0, Number(local.reviewedFallback) || 0) : Number(getDay(date).reviews) || 0;
  const dailyItems = new Set(Array.isArray(local.itemKeys) ? local.itemKeys : [...touched]);
  for (const key of touched) dailyItems.add(key);
  const dailyUnits = new Set(units);
  const dailyChapters = new Set(chapters);
  for (const key of dailyItems) {
    if (typeof key !== 'string' || !key.startsWith('V:')) continue;
    const wordId = key.slice(2).replace(/:rev$/, '');
    const chapterId = wordChapter.get(wordId);
    if (!chapterId) continue;
    const meta = state.chapterMetadata?.[chapterId] || {};
    dailyChapters.add(chapterId.startsWith('part2_') ? 'Part 2: Characteristics' : 'Part 1: Topics');
    const chapterNum = chapterId.startsWith('part2_') ? `C${chapterId.slice(6)}` : `T${chapterId}`;
    dailyUnits.add(`${chapterNum}: ${meta.topic_en || meta.topic_ja || chapterNum}`);
  }
  return {
    date,
    reviewsDone: Math.min(10000, reviewsDone),
    uniqueItems: Math.min(10000, dailyItems.size),
    sessions: Math.min(1000, Number(local.sessions) || 0),
    // Minutes come from this device's session timer and the shared daylog
    // (merged by max), so a lower local value never reports over a higher one.
    minutes: Math.min(600, Math.max(Math.round((Number(local.elapsedMs) || 0) / 60000), Number(getDay(date).minutes) || 0)),
    chapters: [...dailyChapters].sort(), units: [...dailyUnits].sort()
  };
}

async function syncDailySummary(date) {
  const { pat, gistId } = creds();
  if (!navigator.onLine) {
    enqueueDailySummary(buildDailySummary(date));
    setStatus('pending', 'Offline · daily summary queued');
    return false;
  }
  // Merge the shared Gist daylog before building the summary. The dashboard
  // keeps the last POST it receives, so posting this device's local totals
  // before merging could overwrite a higher total another device recorded.
  if (pat && gistId) {
    mergeDaylogMax(await pullRemoteDaylog(pat, gistId));
  }
  const summary = buildDailySummary(date);
  try {
    await postDailySummary(summary);
    flushDailySummaryQueue();
    return true;
  } catch (error) {
    const status = Number(error.status) || 0;
    if (status >= 400 && status < 500) {
      console.warn(`[n3-sync] Daily accountability summary rejected (${error.message}); not queued for retry.`);
      return false;
    }
    console.warn('[n3-sync] Daily accountability summary not delivered:', error.message);
    enqueueDailySummary(summary);
    setStatus('pending', 'Daily summary queued · will retry');
    return false;
  }
}

export function beginGistReviewSession() {
  if (reviewSessionActive) return;
  reviewSessionActive = true;
  try { localStorage.setItem(SESSION_STARTED_KEY, JSON.stringify({ date: istDateKeyFor(), startedAt: Date.now() })); localStorage.setItem(SESSION_ITEM_KEYS, '[]'); localStorage.setItem(SESSION_REVIEW_COUNT, '0'); } catch (_) {}
  if (typeof window !== 'undefined') window.__n3ReviewSessionActive = true;
  localStorage.setItem(ACTIVE_KEY, '1');
  localStorage.removeItem(READY_KEY);
  const { pat, gistId } = creds();
  if (pat && gistId) setStatus('pending', navigator.onLine ? 'Review active · syncs when it ends' : 'Offline · review changes saved locally');
}

export async function endGistReviewSession() {
  if (!reviewSessionActive) return false;
  reviewSessionActive = false;
  if (typeof window !== 'undefined') window.__n3ReviewSessionActive = false;
  localStorage.removeItem(ACTIVE_KEY);
  let session = null;
  try { session = JSON.parse(localStorage.getItem(SESSION_STARTED_KEY) || 'null'); localStorage.removeItem(SESSION_STARTED_KEY); } catch (_) {}
  if (session && session.date && Number.isFinite(session.startedAt)) {
    const elapsed = Math.max(0, Date.now() - session.startedAt);
    const totals = daySessionTotals(session.date, elapsed);
    const sessionReviews = (() => { try { return Number(localStorage.getItem(SESSION_REVIEW_COUNT)) || 0; } catch (_) { return 0; } })();
    try { localStorage.removeItem(SESSION_REVIEW_COUNT); } catch (_) {}
    if (session.date === istDateKeyFor()) totals.reviewedFallback = Math.max(0, Number(totals.reviewedFallback) || 0) + sessionReviews;
    const sessionKeys = (() => { try { return JSON.parse(localStorage.getItem(SESSION_ITEM_KEYS) || '[]'); } catch (_) { return []; } })();
    totals.itemKeys = [...new Set([...(totals.itemKeys || []), ...sessionKeys])];
    try { const all = JSON.parse(localStorage.getItem(DAILY_SUMMARY_KEY) || '{}'); all[session.date] = totals; localStorage.setItem(DAILY_SUMMARY_KEY, JSON.stringify(all)); localStorage.removeItem(SESSION_ITEM_KEYS); } catch (_) {}
    await syncDailySummary(session.date);
  }
  const { pat, gistId } = creds();
  if (!dirty) {
    if (pat && gistId) setStatus(navigator.onLine ? 'ok' : 'pending', navigator.onLine ? 'Connected · up to date' : 'Offline · last sync may be out of date');
    return false;
  }
  if (!pat || !gistId) return false;
  localStorage.setItem(READY_KEY, '1');
  if (!navigator.onLine) {
    setStatus('pending', 'Offline · sync queued');
    return false;
  }
  setStatus('saving', 'Review ended · syncing…');
  return gistLoadStats({ forcePush: true });
}

export async function gistLoadStats(options = {}) {
  const { pat, gistId } = creds();
  if (!pat || !gistId) {
    setStatus('idle', 'Sync off · saved on this device');
    if (localStorage.getItem(PAT_KEY) === '' || localStorage.getItem(GIST_ID_KEY) === '') {
      setStatus('error', 'Sync settings need attention: re-enter your GitHub token and Gist ID.');
    }
    return;
  }
  try {
    setStatus('saving', 'Syncing…');
    const remote = await pull(pat, gistId);
    await backupBeforeFirstDaylogMerge();
    const dayChanged = mergeDaylogMax(lastRemoteDaylog);
    if (mergeStats(remote) || dayChanged) {
      refreshViews();
      dirty = true;
      changeRevision++;
      localStorage.setItem(DIRTY_KEY, '1');
    }
    if (options.forcePush || (!isReviewActive() && dirty && localStorage.getItem(READY_KEY) === '1')) {
      await push(pat, gistId, Boolean(options.allowRepair));
    } else if (dirty) {
      setStatus('pending', isReviewActive() ? 'Review active · syncs when it ends' : 'Saved locally · waiting for review end');
    } else {
      setStatus('ok', 'Connected · up to date');
    }
  } catch (e) {
    const isMalformed = e instanceof SyntaxError && e.remoteStatsParse === true;
    const needsRepair = e.remoteStatsRepair === true;
    if (options.allowRepair && (isMalformed || needsRepair)) {
      setStatus('saving', 'Remote progress is damaged or truncated; validating this device progress…');
      const ok = await push(pat, gistId, true);
      if (ok) setStatus('ok', 'Synced valid progress from this device');
      return;
    }
    const probeResult = async (url, headers = {}) => {
      try {
        const probe = await fetch(url, { headers });
        return `HTTP ${probe.status}`;
      } catch (probeError) {
        return `fetch failed (${probeError.name || 'Error'}: ${probeError.message || 'unknown'})`;
      }
    };
    const unauthenticatedApi = await probeResult(`${API}/rate_limit`, { Accept: 'application/vnd.github.v3+json' });
    const authorizedApi = await probeResult(`${API}/rate_limit`, {
      Authorization: `Bearer ${pat}`,
      Accept: 'application/vnd.github.v3+json'
    });
    let unauthenticatedGist = 'unavailable';
    let publicGistFile = 'unavailable';
    try {
      const publicResponse = await fetch(`${API}/gists/${gistId}`, {
        headers: { Accept: 'application/vnd.github.v3+json' }
      });
      unauthenticatedGist = `HTTP ${publicResponse.status}`;
      try {
        const metadata = await publicResponse.json();
        const file = metadata.files && metadata.files[GIST_FILENAME];
        publicGistFile = file
          ? `size ${file.size} bytes; truncated ${Boolean(file.truncated)}`
          : 'stats file missing';
      } catch (metadataError) {
        publicGistFile = `metadata body read failed: ${metadataError.message || metadataError.name || 'unknown'}`;
      }
    } catch (publicError) {
      unauthenticatedGist = `fetch failed (${publicError.name || 'Error'}: ${publicError.message || 'unknown'})`;
      publicGistFile = 'unavailable';
    }
    let authorizedGist = 'unavailable';
    try {
      const response = await fetch(`${API}/gists/${gistId}?t=${Date.now()}`, { headers: headers(pat) });
      authorizedGist = `status read ok (HTTP ${response.status})`;
      try {
        const body = await response.text();
        authorizedGist += `; body read ok (${new TextEncoder().encode(body).length} bytes)`;
      } catch (bodyError) {
        authorizedGist += `; body read failed: ${bodyError.message || bodyError.name || 'unknown'}`;
      }
    } catch (requestError) {
      authorizedGist = `request failed: ${requestError.message || requestError.name || 'unknown'}`;
    }
    const diag = ` [${e.name || 'Error'}: ${e.message || 'unknown'}; Gist ID set; token set; online ${navigator.onLine ? 'yes' : 'no'}; GitHub API no auth ${unauthenticatedApi}; GitHub API auth ${authorizedApi}; Gist no auth ${unauthenticatedGist}; stats file ${publicGistFile}; Gist auth ${authorizedGist}]`;
    setStatus('error', `Sync error: ${e.message}${diag}`);
  }
}

export function openSyncSetup() {
  const { pat, gistId } = creds();
  const err = document.getElementById('n3s-error');
  if (err) err.classList.add('n3s-hide');
  document.getElementById('n3s-step1').classList.toggle('n3s-hide', !!(pat && gistId));
  document.getElementById('n3s-connected').classList.toggle('n3s-hide', !(pat && gistId));
  if (pat && gistId) {
    const info = document.getElementById('n3s-info');
    if (info) info.textContent = `Connected to your private N3 Gist (${gistId.slice(0, 8)}…).`;
  }
  document.getElementById('n3s-overlay').classList.remove('n3s-hide');
}

export function closeSyncSetup() {
  document.getElementById('n3s-overlay').classList.add('n3s-hide');
}

export async function connectGist() {
  const patInput = document.getElementById('n3s-pat');
  const err = document.getElementById('n3s-error');
  if (isReviewActive()) {
    err.textContent = 'Finish the current review before connecting sync.';
    err.classList.remove('n3s-hide');
    return;
  }
  const pat = patInput.value.trim();
  err.classList.add('n3s-hide');
  if (!pat) {
    err.textContent = 'Paste your token first.';
    err.classList.remove('n3s-hide');
    return;
  }
  setStatus('saving', 'Connecting…');
  try {
    let gistId = null;
    const listRes = await fetch(`${API}/gists?per_page=100&t=${Date.now()}`, { headers: headers(pat) });
    if (!listRes.ok) {
      if (listRes.status === 403 || listRes.status === 429) throw new Error('GitHub rate limit. Wait a few minutes and try again.');
      throw new Error('Token rejected. It needs the "gist" permission.');
    }
    const gists = await listRes.json();
    for (const g of gists) {
      if (g.files && g.files[GIST_FILENAME]) { gistId = g.id; break; }
    }
    if (!gistId) {
      const initialPayload = serializeStats();
      if (new TextEncoder().encode(initialPayload).length >= MAX_SYNC_BYTES) {
        throw new Error(localStatsTooLargeMessage(initialPayload));
      }
      const createRes = await fetch(`${API}/gists`, {
        method: 'POST',
        headers: headers(pat, true),
        body: JSON.stringify({
          description: 'Nihongo N3 - SRS study progress (auto-managed)',
          public: false,
          files: { [GIST_FILENAME]: { content: initialPayload } }
        })
      });
      if (!createRes.ok) throw new Error('Could not create the Gist. Check the token has the "gist" permission.');
      gistId = (await createRes.json()).id;
    }
    localStorage.setItem(PAT_KEY, pat);
    localStorage.setItem(GIST_ID_KEY, gistId);
    patInput.value = '';
    await gistLoadStats();
    openSyncSetup();
  } catch (e) {
    setStatus('error', 'Not connected');
    err.textContent = e.message;
    err.classList.remove('n3s-hide');
  }
}

export async function forceSyncNow() {
  const btn = document.getElementById('n3s-sync-now');
  if (btn) btn.disabled = true;
  const inReview = isReviewActive();
  if (inReview) {
    setStatus('pending', 'Review active · syncs when it ends');
  } else {
    await gistLoadStats({ allowRepair: true, forcePush: true });
  }
  if (btn) btn.disabled = false;
}

export function disconnectGist() {
  if (!confirm('Disconnect sync? Progress on this device stays; nothing is deleted.')) return;
  localStorage.removeItem(PAT_KEY);
  localStorage.removeItem(GIST_ID_KEY);
  dirty = false;
  reviewSessionActive = false;
  if (typeof window !== 'undefined') window.__n3ReviewSessionActive = false;
  localStorage.removeItem(ACTIVE_KEY);
  localStorage.removeItem(DIRTY_KEY);
  localStorage.removeItem(READY_KEY);
  setStatus('idle', 'Sync off · saved on this device');
  closeSyncSetup();
}

export function initSyncUI() {
  flushDailySummaryQueue();
  if (typeof window !== 'undefined' && !window.__n3DailySummaryTimer) {
    const timer = setInterval(() => { flushDailySummaryQueue(); }, 5 * 60 * 1000);
    if (timer && typeof timer.unref === 'function') timer.unref();
    window.__n3DailySummaryTimer = timer;
  }
  const { pat, gistId } = creds();
  setStatus(pat && gistId ? 'saving' : 'idle', pat && gistId ? 'Checking Gist…' : 'Sync off · saved on this device');
  window.addEventListener('offline', () => {
    if (creds().pat && creds().gistId) setStatus('pending', dirty ? 'Offline · sync queued' : 'Offline · last sync may be out of date');
  });
  window.addEventListener('online', () => {
    flushDailySummaryQueue();
    const c = creds();
    if (!c.pat || !c.gistId) return;
    if (isReviewActive()) { setStatus('pending', 'Review active · syncs when it ends'); return; }
    if (dirty && localStorage.getItem(READY_KEY) === '1') gistLoadStats({ forcePush: true });
    else gistLoadStats();
  });
  if (typeof document !== 'undefined' && document.addEventListener) {
    // Installed app or tab left open in the background: sync again whenever it comes back to the screen.
    let lastVisibleSync = Date.now();
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState !== 'visible') return;
      const c = creds();
      if (!c.pat || !c.gistId || isReviewActive()) return;
      if (Date.now() - lastVisibleSync < 20000) return;
      lastVisibleSync = Date.now();
      gistLoadStats();
    });
  }
  if (pat && gistId && reviewSessionActive) {
    // A persisted active marker means the prior page ended mid-review; do not mistake that for completion.
    reviewSessionActive = false;
    if (typeof window !== 'undefined') window.__n3ReviewSessionActive = false;
    localStorage.removeItem(ACTIVE_KEY);
    localStorage.removeItem(READY_KEY);
    if (dirty) setStatus('pending', 'Review interrupted · saved locally');
  }
  if (pat && gistId) gistLoadStats();
}
