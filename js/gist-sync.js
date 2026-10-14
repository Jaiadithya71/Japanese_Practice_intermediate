/* =======================================================
   NIHONGO INTERMEDIATE - gist-sync.js
   Optional GitHub Gist sync for N3 progress (separate Gist
   from the N5/N4 app). Token stays in this browser only.
   ======================================================= */

import { STORAGE_KEY } from './config.js';
import { state } from './state.js';
import { updateSidebarStats } from './srs.js';
import { encodeStats, decodeStatsText } from './stats-codec.js';

const GIST_FILENAME = 'nihongo-n3-stats.json';
const PAT_KEY = 'n3_github_pat';
const GIST_ID_KEY = 'n3_gist_id';
const DIRTY_KEY = 'n3_gist_dirty';
const READY_KEY = 'n3_gist_ready';
const ACTIVE_KEY = 'n3_gist_review_active';
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
  const mobileIndicators = ['n3sync-mobile'].map(id => document.getElementById(id)).filter(Boolean);
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
        body: JSON.stringify({ files: { [GIST_FILENAME]: { content: payload } } })
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

export function beginGistReviewSession() {
  reviewSessionActive = true;
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
    if (mergeStats(remote)) {
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
  const { pat, gistId } = creds();
  setStatus(pat && gistId ? 'saving' : 'idle', pat && gistId ? 'Checking Gist…' : 'Sync off · saved on this device');
  window.addEventListener('offline', () => {
    if (creds().pat && creds().gistId) setStatus('pending', dirty ? 'Offline · sync queued' : 'Offline · last sync may be out of date');
  });
  window.addEventListener('online', () => {
    const c = creds();
    if (!c.pat || !c.gistId) return;
    if (isReviewActive()) { setStatus('pending', 'Review active · syncs when it ends'); return; }
    if (dirty && localStorage.getItem(READY_KEY) === '1') gistLoadStats({ forcePush: true });
    else gistLoadStats();
  });
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
