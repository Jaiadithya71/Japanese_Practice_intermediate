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
const API = 'https://api.github.com';

let saveTimer = null;
let dirty = false;

function creds() {
  return { pat: localStorage.getItem(PAT_KEY), gistId: localStorage.getItem(GIST_ID_KEY) };
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
  const res = await fetch(`${API}/gists/${gistId}?t=${Date.now()}`, { headers: headers(pat) });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const gist = await res.json();
  const file = gist.files && gist.files[GIST_FILENAME];
  if (!file) throw new Error('The progress file is missing from the Gist; nothing was written.');
  let content = file.content;
  if (file.truncated && file.raw_url) {
    const raw = await fetch(file.raw_url, { headers: headers(pat) });
    if (!raw.ok) throw new Error(`Could not read full remote progress (HTTP ${raw.status}); nothing was written.`);
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
const API = 'https://api.github.com';

let saveTimer = null;
let dirty = false;

function creds() {
  return { pat: localStorage.getItem(PAT_KEY), gistId: localStorage.getItem(GIST_ID_KEY) };
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
  const res = await fetch(`${API}/gists/${gistId}?t=${Date.now()}`, { headers: headers(pat) });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const gist = await res.json();
  const file = gist.files && gist.files[GIST_FILENAME];
  if (!file) throw new Error('The progress file is missing from the Gist; nothing was written.');
  let content = file.content;
  if (file.truncated && file.raw_url) {
    const raw = await fetch(file.raw_url, { headers: headers(pat) });
    if (!raw.ok) throw new Error(`Could not read full remote progress (HTTP ${raw.status}); nothing was written.`);
    content = await raw.text();
  }
  if (typeof content !== 'string' || !content.length) {
    throw new Error('The remote progress file is empty or unavailable; nothing was written.');
  }
  return content;
}

async function pull(pat, gistId) {
  const remote = JSON.parse(await getRemoteContent(pat, gistId));
  if (!remote || typeof remote !== 'object' || Array.isArray(remote)) {
    throw new Error('Remote progress is not a valid stats object.');
  }
  return remote;
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
      if (!remote || typeof remote !== 'object' || Array.isArray(remote)) throw new Error('Remote progress is not a stats object.');
    } catch (e) {
      if (!(allowCorruptRemote && e instanceof SyntaxError)) throw e;
    }
  } catch (e) {
    setStatus('error', `Sync blocked: ${e.message}`);
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

export async function gistLoadStats({ allowRepair = false } = {}) {
  const { pat, gistId } = creds();
  if (!pat || !gistId) return;
  try {
    setStatus('saving', 'Syncing…');
    const remote = await pull(pat, gistId);
    if (mergeStats(remote)) refreshViews();
    await push(pat, gistId);
  } catch (e) {
    if (allowRepair && e instanceof SyntaxError) {
      setStatus('saving', 'Remote JSON is damaged; validating this device’s progress…');
      const ok = await push(pat, gistId, true);
      if (ok) setStatus('ok', 'Synced valid progress from this device');
      return;
    }
    setStatus('error', `Sync error: ${e.message}`);
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
          files: { [GIST_FILENAME]: { content: serializeStats() } }
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
  try { await gistLoadStats({ allowRepair: true }); } finally { if (btn) btn.disabled = false; }
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
  // beforeunload cannot safely validate remote state, so it never PATCHes.
  if (pat && gistId) gistLoadStats();
}
