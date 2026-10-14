/* =======================================================
   NIHONGO INTERMEDIATE - gist-sync.js
   Optional GitHub Gist sync for N3 progress (separate Gist
   from the N5/N4 app). Token stays in this browser only.
   ======================================================= */

import { STORAGE_KEY } from './config.js';
import { state } from './state.js';
import { updateSidebarStats } from './srs.js';

const GIST_FILENAME = 'nihongo-n3-stats.json';
const PAT_KEY = 'n3_github_pat';
const GIST_ID_KEY = 'n3_gist_id';
const MAX_SYNC_BYTES = 1024 * 1024;

function markRemoteRepairRequired(message) {
  const error = new Error(message);
  error.remoteStatsRepair = true;
  return error;
}
const API = 'https://api.github.com';

let saveTimer = null;
let dirty = false;

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
  const el = document.getElementById('n3sync-status');
  const label = document.getElementById('n3sync-label');
  if (el) el.className = `n3s-pill n3s-${kind}`;
  if (label) label.textContent = text;
  // Icon reflects state: cloud (idle), spinning arrows (working), check (synced), warning (error)
  const icon = el && el.querySelector('i');
  if (icon) {
    const map = { idle: 'fa-cloud', saving: 'fa-arrows-rotate fa-spin', ok: 'fa-circle-check', error: 'fa-triangle-exclamation' };
    icon.className = `fa-solid ${map[kind] || 'fa-cloud'}`;
  }
  const info = document.getElementById('n3s-info');
  if (info) info.textContent = text;
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
  const content = JSON.stringify(state.stats, null, 2);
  const parsed = JSON.parse(content);
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
    throw new Error('Local progress did not serialize to a valid stats object; nothing was written.');
  }
  return content;
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
    remote = JSON.parse(content);
  } catch (e) {
    e.remoteStatsParse = true;
    throw e;
  }
  if (!remote || typeof remote !== 'object' || Array.isArray(remote)) {
    throw markRemoteRepairRequired('Remote progress is malformed; use Sync Now to replace it with this device\'s validated stats.');
  }
  return remote;
}

async function pull(pat, gistId) {
  return parseRemoteStats(await getRemoteContent(pat, gistId));
}

async function push(pat, gistId, allowCorruptRemote = false) {
  let payload;
  try {
    payload = serializeStats();
    const wrapped = JSON.stringify({ files: { [GIST_FILENAME]: { content: payload } } });
    JSON.parse(wrapped);
    const remoteContent = await getRemoteContent(pat, gistId);
    try {
      const remote = JSON.parse(remoteContent);
      if (!remote || typeof remote !== 'object' || Array.isArray(remote)) throw markRemoteRepairRequired('Remote progress is malformed; use Sync Now to replace it with this device\'s validated stats.');
    } catch (e) {
      const isMalformed = e instanceof SyntaxError;
      if (isMalformed) e.remoteStatsParse = true;
      if (!(allowCorruptRemote && (isMalformed || e.remoteStatsRepair === true))) throw e;
    }
  } catch (e) {
    if (!(allowCorruptRemote && e.remoteStatsRepair === true)) {
      setStatus('error', 'Sync blocked: ' + e.message);
      return false;
    }
  }
  if (new TextEncoder().encode(payload).length >= MAX_SYNC_BYTES) {
    setStatus('error', "Local progress is still over GitHub Gist's 1 MB sync limit; nothing was written.");
    return false;
  }
  const delays = [2000, 5000, 10000];
  for (let i = 0; i <= delays.length; i++) {
    try {
      const res = await fetch(`${API}/gists/${gistId}`, {
        method: 'PATCH',
        headers: headers(pat, true),
        body: JSON.stringify({ files: { [GIST_FILENAME]: { content: payload } } })
      });
      if (res.ok) {
        dirty = false;
        state.lastSyncTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        setStatus('ok', `Synced ${state.lastSyncTime}`);
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

// Called by saveStats() after every local save. Debounced upload.
export function scheduleGistSave() {
  const { pat, gistId } = creds();
  if (!pat || !gistId) return;
  dirty = true;
  clearTimeout(saveTimer);
  setStatus('saving', 'Saving…');
  saveTimer = setTimeout(() => push(pat, gistId), 15000);
}

export async function gistLoadStats(options = {}) {
  const { pat, gistId } = creds();
  if (!pat || !gistId) {
    if (localStorage.getItem(PAT_KEY) === '' || localStorage.getItem(GIST_ID_KEY) === '') {
      setStatus('error', 'Sync settings need attention: re-enter your GitHub token and Gist ID.');
    }
    return;
  }
  try {
    setStatus('saving', 'Syncing…');
    const remote = await pull(pat, gistId);
    if (mergeStats(remote)) refreshViews();
    await push(pat, gistId);
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
      const createRes = await fetch(`${API}/gists`, {
        method: 'POST',
        headers: headers(pat, true),
        body: JSON.stringify({
          description: 'Nihongo N3 - SRS study progress (auto-managed)',
          public: false,
          files: { [GIST_FILENAME]: { content: JSON.stringify(state.stats, null, 2) } }
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
  await gistLoadStats({ allowRepair: true });
  if (btn) btn.disabled = false;
}

export function disconnectGist() {
  if (!confirm('Disconnect sync? Progress on this device stays; nothing is deleted.')) return;
  localStorage.removeItem(PAT_KEY);
  localStorage.removeItem(GIST_ID_KEY);
  clearTimeout(saveTimer);
  setStatus('idle', 'Saved on this device');
  closeSyncSetup();
}

export function initSyncUI() {
  const { pat, gistId } = creds();
  setStatus('idle', pat && gistId ? 'Tap to sync' : 'Saved on this device');
  window.addEventListener('online', () => { if (dirty) gistLoadStats(); });
  window.addEventListener('beforeunload', () => {
    const c = creds();
    if (dirty && c.pat && c.gistId) {
      try {
        fetch(`${API}/gists/${c.gistId}`, {
          method: 'PATCH', keepalive: true, headers: headers(c.pat, true),
          body: JSON.stringify({ files: { [GIST_FILENAME]: { content: JSON.stringify(state.stats) } } })
        });
      } catch (_) {}
    }
  });
  if (pat && gistId) gistLoadStats();
}
