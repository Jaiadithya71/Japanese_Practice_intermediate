import { state } from './state.js';

const STORE_NAME = 'n3-listening-audio-v1';
const STORE_VERSION = 1;
const MANIFEST_URL = 'https://n3-listening-audio.pages.dev/index.json';
const STORAGE_PREFIX = 'n3-listening-';
const SEPARATOR = '\u241f';

let selectedLessons = new Set();
let queue = [];
let currentIndex = -1;
let manifestByKey = new Map();
let dbPromise;
let downloadBusy = false;
let generatedLessons = [];

function pairKey(word) {
  return `${String(word.reading || '').trim()}${SEPARATOR}${String(word.meaning_en || '').trim()}`;
}

function orderedLessonKeys() {
  const keys = Object.keys(state.vocabDB || {}).filter(k => /^\d+$/.test(k) || k.startsWith('part2_'));
  const rank = key => {
    if (key.startsWith('part2_')) return 21 + Number(key.slice(6));
    const n = Number(key);
    return n <= 21 ? n : (n <= 30 ? 30 + (n - 21) : n + 9);
  };
  return keys.sort((a, b) => rank(a) - rank(b));
}

function lessonLabel(chapter) {
  if (chapter.startsWith('part2_')) return `C${Number(chapter.slice(6))}`;
  const n = Number(chapter);
  if (n > 30) return `K${n - 30}`;
  if (n > 21) return `R${n - 21}`;
  return String(n || chapter);
}

function wordsForLesson(chapter) {
  return [
    ...(state.vocabDB?.[chapter] || []),
    ...(state.vocabLessonOverlaps?.[chapter] || [])
  ];
}

function allLessons() {
  return orderedLessonKeys().map(chapter => ({
    chapter,
    label: lessonLabel(chapter),
    topic: state.chapterMetadata?.[chapter]?.topic_en || '',
    words: wordsForLesson(chapter)
  }));
}

function selectedOccurrences(lessonSelection = selectedLessons) {
  const occurrences = [];
  for (const lesson of allLessons()) {
    if (!lessonSelection.has(lesson.chapter)) continue;
    for (const word of lesson.words) {
      if (!word.reading || !word.meaning_en) continue;
      occurrences.push({
        key: pairKey(word),
        chapter: lesson.chapter,
        lessonLabel: lesson.label,
        reading: word.reading,
        term: word.term_ja || word.reading,
        meaning: word.meaning_en
      });
    }
  }
  return occurrences;
}

export function buildListeningQueue(lessonSelection = selectedLessons) {
  return selectedOccurrences(lessonSelection);
}

function selectedUniquePairs() {
  const pairs = new Map();
  for (const item of selectedOccurrences()) {
    if (!pairs.has(item.key)) pairs.set(item.key, item);
  }
  return pairs;
}

function openDb() {
  if (dbPromise) return dbPromise;
  dbPromise = new Promise((resolve, reject) => {
    if (!('indexedDB' in window)) return reject(new Error('Offline storage is unavailable in this browser.'));
    const request = indexedDB.open(STORE_NAME, STORE_VERSION);
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains('clips')) db.createObjectStore('clips', { keyPath: 'key' });
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error || new Error('Could not open offline audio storage.'));
  });
  return dbPromise;
}

async function readClip(key) {
  const db = await openDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction('clips', 'readonly');
    const request = tx.objectStore('clips').get(key);
    request.onsuccess = () => resolve(request.result?.blob || null);
    request.onerror = () => reject(request.error);
  });
}

async function writeClip(key, blob) {
  const db = await openDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction('clips', 'readwrite');
    tx.objectStore('clips').put({ key, blob, savedAt: Date.now() });
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error || new Error('Could not save an audio clip.'));
    tx.onabort = () => reject(tx.error || new Error('Audio save was interrupted.'));
  });
}

async function savedKeys(keys) {
  const present = new Set();
  try {
    const db = await openDb();
    await new Promise((resolve, reject) => {
      const tx = db.transaction('clips', 'readonly');
      const store = tx.objectStore('clips');
      const request = store.openCursor();
      request.onsuccess = () => {
        const cursor = request.result;
        if (!cursor) return resolve();
        if (keys.has(cursor.key)) present.add(cursor.key);
        cursor.continue();
      };
      request.onerror = () => reject(request.error);
    });
  } catch (_) { /* status will explain unsupported storage on download */ }
  return present;
}

async function fetchManifest() {
  try {
    const response = await fetch(MANIFEST_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error(`Audio pack manifest returned ${response.status}.`);
    const data = await response.json();
    manifestByKey = new Map((data.pairs || []).map(item => [item.key, { ...item, url: new URL(item.url, data.baseUrl || response.url).href }]));
    return data;
  } catch (error) {
    manifestByKey = new Map();
    return { available: false, error };
  }
}

function setStatus(message, kind = 'info') {
  const el = document.getElementById('listen-status');
  if (!el) return;
  el.textContent = message;
  el.className = `listen-status is-${kind}`;
}

function renderLessonTiles() {
  const root = document.getElementById('listen-lesson-grid');
  if (!root) return;
  const lessons = allLessons();
  root.innerHTML = lessons.map(lesson => {
    const selected = selectedLessons.has(lesson.chapter);
    const uniqueWords = new Map();
    for (const word of lesson.words) if (word.reading && word.meaning_en) uniqueWords.set(pairKey(word), word);
    const uniqueKeys = [...uniqueWords.keys()];
    const complete = uniqueKeys.length > 0 && uniqueKeys.every(key => Number(manifestByKey.get(key)?.durationSeconds) > 0);
    const totalSeconds = complete ? Math.round(uniqueKeys.reduce((sum, key) => sum + Number(manifestByKey.get(key).durationSeconds), 0)) : 0;
    const duration = `${Math.floor(totalSeconds / 60)}:${String(totalSeconds % 60).padStart(2, '0')}`;
    const wordText = `${uniqueKeys.length} words`;
    const timeText = complete ? `<br>${duration}` : '';
    const aria = complete ? `Lesson ${lesson.label}, ${wordText}, ${duration}` : `Lesson ${lesson.label}, ${wordText}, audio time not ready`;
    return `<button type="button" class="listen-lesson-tile${selected ? ' selected' : ''}" data-lesson="${escapeAttr(lesson.chapter)}" aria-label="${escapeAttr(aria)}" aria-pressed="${selected}" onclick="window.N3Listening.toggleLesson('${escapeAttr(lesson.chapter)}')">
      <span class="listen-tile-badge">${escapeHtml(lesson.label)}</span>
      <span class="listen-tile-details">${escapeHtml(wordText)}${timeText}</span>
      <i class="fa-solid ${selected ? 'fa-circle-check' : 'fa-circle'}" aria-hidden="true"></i>
    </button>`;
  }).join('');
  const countEl = document.getElementById('listen-selected-count');
  const occurrences = selectedOccurrences();
  const unique = selectedUniquePairs().size;
  if (countEl) countEl.textContent = `${selectedLessons.size} lessons · ${occurrences.length} plays · ${unique} clips`;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch]));
}
function escapeAttr(value) { return escapeHtml(value).replace(/`/g, '&#96;'); }

function renderPlayer() {
  const item = queue[currentIndex];
  const term = document.getElementById('listen-current-term');
  const meaning = document.getElementById('listen-current-meaning');
  const lesson = document.getElementById('listen-current-lesson');
  const previous = document.getElementById('listen-previous');
  const next = document.getElementById('listen-next');
  const toggle = document.getElementById('listen-toggle');
  const player = document.getElementById('listen-audio-player');
  if (term) term.textContent = item ? item.term : 'Ready to listen';
  if (meaning) meaning.textContent = item ? item.meaning : '';
  if (lesson) lesson.textContent = item ? `Lesson ${item.lessonLabel} · ${currentIndex + 1} of ${queue.length}` : 'No lesson selected';
  if (previous) previous.disabled = currentIndex <= 0;
  if (next) next.disabled = !queue.length || currentIndex >= queue.length - 1;
  if (toggle) {
    toggle.disabled = !queue.length;
    toggle.innerHTML = player && !player.paused ? '<i class="fa-solid fa-pause"></i><span>Pause</span>' : '<i class="fa-solid fa-play"></i><span>Play</span>';
  }
  if ('mediaSession' in navigator) {
    try { navigator.mediaSession.playbackState = player && !player.paused ? 'playing' : 'paused'; } catch (_) {}
  }
}

async function loadQueueItem(index, autoPlay = false) {
  if (index < 0 || index >= queue.length) return;
  const player = document.getElementById('listen-audio-player');
  if (!player) return;
  const item = queue[index];
  const blob = await readClip(item.key).catch(() => null);
  if (!blob) {
    currentIndex = index;
    renderPlayer();
    setStatus('This clip is not saved on this device yet. Download the selected lessons audio pack first.', 'warning');
    return;
  }
  if (player.dataset.objectUrl) URL.revokeObjectURL(player.dataset.objectUrl);
  const url = URL.createObjectURL(blob);
  player.dataset.objectUrl = url;
  player.src = url;
  player.playbackRate = Number(document.getElementById('listen-speed')?.value || 1);
  currentIndex = index;
  renderPlayer();
  updateMediaSession(item);
  if (autoPlay) {
    try { await player.play(); setStatus('Playing Japanese, then English.', 'success'); }
    catch (_) { setStatus('Tap Play to start audio. Your browser may require a direct tap.', 'warning'); }
  }
}

function updateMediaSession(item) {
  if (!('mediaSession' in navigator)) return;
  try {
    navigator.mediaSession.metadata = new MediaMetadata({
      title: `${item.term} · ${item.meaning}`,
      artist: `N3 Listening · Lesson ${item.lessonLabel}`,
      album: 'Nihongo Intermediate'
    });
    navigator.mediaSession.setActionHandler('play', () => document.getElementById('listen-audio-player')?.play());
    navigator.mediaSession.setActionHandler('pause', () => document.getElementById('listen-audio-player')?.pause());
    navigator.mediaSession.setActionHandler('previoustrack', () => previous());
    navigator.mediaSession.setActionHandler('nexttrack', () => next());
  } catch (_) { /* Media Session support varies by browser */ }
}

function previous() { if (currentIndex > 0) loadQueueItem(currentIndex - 1, true); }
function next() { if (currentIndex + 1 < queue.length) loadQueueItem(currentIndex + 1, true); }

export function toggleLesson(chapter) {
  chapter = String(chapter);
  if (selectedLessons.has(chapter)) selectedLessons.delete(chapter);
  else selectedLessons.add(chapter);
  persistSelection();
  renderLessonTiles();
}

function persistSelection() {
  try { localStorage.setItem(`${STORAGE_PREFIX}selected_lessons`, JSON.stringify([...selectedLessons])); } catch (_) {}
}

export function selectAll() {
  selectedLessons = new Set(orderedLessonKeys());
  persistSelection();
  renderLessonTiles();
}

export function clearSelection() {
  selectedLessons.clear();
  persistSelection();
  queue = [];
  currentIndex = -1;
  document.getElementById('listen-audio-player')?.pause();
  renderLessonTiles();
  renderPlayer();
}

export async function downloadSelectedAudio() {
  if (downloadBusy) return;
  const uniquePairs = selectedUniquePairs();
  if (!uniquePairs.size) {
    setStatus('Select at least one lesson first.', 'warning');
    return;
  }
  const cache = await savedKeys(new Set(uniquePairs.keys()));
  const missing = [...uniquePairs.keys()].filter(key => !cache.has(key) && !manifestByKey.has(key));
  if (missing.length) {
    setStatus(`The audio pack is not installed for ${missing.length} unique clips. The audio files must be supplied separately from the public app code.`, 'warning');
    return;
  }
  downloadBusy = true;
  const button = document.getElementById('listen-download');
  if (button) button.disabled = true;
  let saved = 0;
  try {
    const entries = [...uniquePairs].filter(([key]) => !cache.has(key));
    for (const [key, item] of entries) {
      const source = manifestByKey.get(key)?.url;
      if (!source) throw new Error(`Missing audio URL for ${item.reading}.`);
      const response = await fetch(source);
      if (!response.ok) throw new Error(`Audio fetch returned ${response.status} for ${item.reading}.`);
      const blob = await response.blob();
      if (!blob.size) throw new Error(`Empty audio file for ${item.reading}.`);
      await writeClip(key, blob);
      saved += 1;
      setStatus(`Saving audio: ${saved} of ${entries.length} clips. Keep this tab open until it finishes.`, 'info');
    }
    setStatus(`Saved ${uniquePairs.size} unique clips for ${selectedOccurrences().length} lesson plays on this device.`, 'success');
  } catch (error) {
    setStatus(`Audio save stopped: ${error.message}`, 'error');
  } finally {
    downloadBusy = false;
    if (button) button.disabled = false;
    renderStorageStatus();
  }
}

export async function startPlayback() {
  const occurrences = selectedOccurrences();
  if (!occurrences.length) {
    setStatus('Select one or more lessons to build the listening queue.', 'warning');
    return;
  }
  queue = occurrences;
  const keys = new Set(queue.map(item => item.key));
  const present = await savedKeys(keys);
  const absent = [...keys].filter(key => !present.has(key)).length;
  if (absent) {
    renderPlayer();
    setStatus(`${absent} unique clips are not saved yet. Download audio before starting playback.`, 'warning');
    return;
  }
  currentIndex = 0;
  await loadQueueItem(0, true);
  renderPlayer();
}

export function setSpeed(value) {
  const player = document.getElementById('listen-audio-player');
  const speed = Number(value) || 1;
  if (player) player.playbackRate = speed;
  const label = document.getElementById('listen-speed-label');
  if (label) label.textContent = `${speed.toFixed(2).replace(/0$/, '')}×`;
}

function formatTime(seconds) {
  if (!Number.isFinite(seconds) || seconds < 0) return '0:00';
  const whole = Math.floor(seconds);
  return `${Math.floor(whole / 60)}:${String(whole % 60).padStart(2, '0')}`;
}

export function seek(percent) {
  const player = document.getElementById('listen-audio-player');
  const p = Math.max(0, Math.min(100, Number(percent) || 0));
  if (player && Number.isFinite(player.duration) && player.duration > 0) {
    player.currentTime = player.duration * p / 100;
  }
}

function updateProgress() {
  const player = document.getElementById('listen-audio-player');
  if (!player) return;
  const progress = document.getElementById('listen-progress');
  const current = document.getElementById('listen-time-current');
  const total = document.getElementById('listen-time-total');
  if (progress) progress.value = Number.isFinite(player.duration) && player.duration > 0 ? String(player.currentTime / player.duration * 100) : '0';
  if (current) current.textContent = formatTime(player.currentTime);
  if (total) total.textContent = formatTime(player.duration);
}

export async function togglePlayback() {
  const player = document.getElementById('listen-audio-player');
  if (!player) return;
  if (!queue.length || currentIndex < 0) return startPlayback();
  if (player.paused) {
    try { await player.play(); setStatus('Playing Japanese, then English.', 'success'); }
    catch (_) { setStatus('Tap Play again to start audio.', 'warning'); }
  } else player.pause();
  renderPlayer();
}

async function renderStorageStatus() {
  const countEl = document.getElementById('listen-storage-count');
  if (!countEl) return;
  try {
    const db = await openDb();
    const count = await new Promise((resolve, reject) => {
      const tx = db.transaction('clips', 'readonly');
      const request = tx.objectStore('clips').count();
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
    countEl.textContent = `${count.toLocaleString()} clips saved on this device`;
  } catch (_) {
    countEl.textContent = 'Offline audio storage is not available in this browser';
  }
}

export async function initListening() {
  try {
    const saved = JSON.parse(localStorage.getItem(`${STORAGE_PREFIX}selected_lessons`) || '[]');
    selectedLessons = new Set(saved.map(String));
  } catch (_) { selectedLessons = new Set(); }
  const data = await fetchManifest();
  setStatus(data.available ? `${data.pairs?.length || 0} audio clips available.` : 'Audio pack unavailable.', data.available ? 'info' : 'warning');
  renderLessonTiles();
  renderPlayer();
  renderStorageStatus();
  const player = document.getElementById('listen-audio-player');
  if (player && !player.dataset.bound) {
    player.dataset.bound = '1';
    player.addEventListener('play', renderPlayer);
    player.addEventListener('pause', renderPlayer);
    player.addEventListener('timeupdate', updateProgress);
    player.addEventListener('loadedmetadata', updateProgress);
    player.addEventListener('ended', () => {
      if (currentIndex + 1 < queue.length) loadQueueItem(currentIndex + 1, true);
      else { renderPlayer(); setStatus('Listening queue finished.', 'success'); }
    });
    player.addEventListener('error', () => setStatus('This saved audio file could not be played.', 'error'));
  }
}

export function renderListening() {
  if (!generatedLessons.length) generatedLessons = allLessons();
  renderLessonTiles();
  renderPlayer();
}

if (typeof window !== 'undefined') {
  window.N3Listening = { toggleLesson, selectAll, clearSelection, downloadSelectedAudio, startPlayback, togglePlayback, seek, setSpeed, previous, next, initListening };
}
