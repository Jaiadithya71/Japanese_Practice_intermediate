/* =======================================================
   NIHONGO INTERMEDIATE — reader.js
   Dokkai (Reading Comprehension) Reader & Engine
   Flow: Preview -> Read -> Answer -> Review -> Follow-up
   Reference: n3_dev_handoff/04_READING_COMPREHENSION_SPEC.md
   ======================================================= */

import { state } from './state.js';
import { beginGistReviewSession, endGistReviewSession } from './gist-sync.js';
import { updateItemStats, toggleItemHard, updateSidebarStats, snapToNextDueSlot, saveStats, peekItemStatus } from './srs.js';
import { renderCard } from './study.js?v=4.4';
import { showView } from './navigation.js';
import { getAllWords, getAllReadingLessons } from './data-loader.js';
import { vocabularyKanjiMeanings } from './vocab-kanji-breakdown.js';
import {
  PASSAGE_GENRES,
  GENRE_METADATA,
  categorizePassage,
  countPassageChars,
  DEFAULT_READING_CPM,
  calculateTargetMinutes,
  calculateTargetSeconds,
  calculateCpm,
  formatTime,
  detectQuestionType,
  getQuestionType,
  CHUNK_CONNECTORS,
  CHUNK_CONNECTOR_REGEX,
  insertChunkDividers,
  isSecondPassPassed,
  evaluateSecondPass,
  REREAD_INTERVALS_DAYS,
  REREAD_FAIL_REPEAT_DAYS,
  calculateRereadSchedule,
  shuffleQuestionOptions,
  evaluateQuestionAnswer
} from './reading-types.js';

// =======================================================
// PERSISTENT READER SETTINGS (RD-3)
// =======================================================

const SETTINGS_KEY = 'n3_reader_settings';

function loadReaderSettings() {
  try {
    const raw = localStorage.getItem(SETTINGS_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      return {
        fontScale: typeof parsed.fontScale === 'number' ? parsed.fontScale : 1.0,
        showFurigana: parsed.showFurigana !== false,
        showTranslations: Boolean(parsed.showTranslations),
        chunkMode: Boolean(parsed.chunkMode),
        showStrategyFurigana: Boolean(parsed.showStrategyFurigana)
      };
    }
  } catch {}
  return {
    fontScale: 1.0,
    showFurigana: true,
    showTranslations: false,
    chunkMode: false,
    showStrategyFurigana: false
  };
}

function saveReaderSettings(settings) {
  try {
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
  } catch {}
}

// Runtime Reader State
const readerRuntime = {
  phase: 'preview', // 'preview' | 'read' | 'answer' | 'review'
  lesson: null,
  isSecondPass: false,
  shuffledQuestions: [],
  selectedAnswers: {}, // { [qId]: selectedOptionNumber }
  submitted: false,
  timerInterval: null,
  readStartTime: null,
  elapsedSeconds: 0,
  targetSeconds: 0,
  charCount: 0,
  showOptionEn: false,
  showPassageInAnswer: false,
  activeGlossWord: null,
  expandedSentenceTrans: new Set(),
  settings: loadReaderSettings(),
  bookQueue: [],       // Book mode: ordered lesson ids being browsed
  bookIndex: -1,
  bookSectionIndex: 0, // Book mode: current section within the lesson
  practiceQueue: [],   // Practice chaining: ordered lesson ids from the picker
  practiceIndex: -1,
  lastDrillHardOnly: false
};

// Sync initial settings into state
state.showFurigana = readerRuntime.settings.showFurigana;
state.showSentenceTranslations = readerRuntime.settings.showTranslations;

// =======================================================
// READ TAB BROWSING & CATEGORIES
// =======================================================

export function renderReadingView() {
  ensureReaderStyles();
  renderCategoryTabs();
  renderReadingLessonChips();
  renderLessonList();
}

export function renderCategoryTabs() {
  const container = document.getElementById('reader-category-tabs');
  if (!container) return;
  container.innerHTML = '';

  const categories = [
    { id: 'all', label: 'All Passages', icon: 'fa-layer-group' },
    { id: 'real_short', label: 'Short (短文)', icon: 'fa-file-lines' },
    { id: 'real_medium', label: 'Medium (中文)', icon: 'fa-book-open' },
    { id: 'real_long', label: 'Long (長文)', icon: 'fa-scroll' },
    { id: 'info', label: 'Info (情報検索)', icon: 'fa-magnifying-glass' },
    { id: 'foundation', label: 'Foundation (基礎編)', icon: 'fa-cube' },
    { id: 'strategy', label: 'Strategy (対策編)', icon: 'fa-chess' }
  ];

  categories.forEach(c => {
    const btn = document.createElement('button');
    const isActive = state.readingCategory === c.id;
    btn.className = `reader-cat-tab${isActive ? ' active' : ''}`;
    btn.innerHTML = `<i class="fa-solid ${c.icon}"></i> ${c.label}`;
    btn.onclick = () => setReadingCategory(c.id);
    container.appendChild(btn);
  });
}

export function setReadingCategory(cat) {
  state.readingCategory = cat;
  renderCategoryTabs();
  renderReadingLessonChips();
  renderLessonList();
}

export function renderLessonList() {
  const container = document.getElementById('dokkai-grid-container');
  if (!container) return;
  container.innerHTML = '';

  let list = filterReadingByCategory(Object.values(state.readingDB || {}));

  const countBadge = document.getElementById('dokkai-count-badge');
  if (countBadge) countBadge.textContent = `${list.length} Lessons`;

  if (list.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-book-open-reader"></i>
        <h3>No lessons in this category</h3>
      </div>`;
    return;
  }

  // Recommended Sort: Re-reads due first, then unread, then others
  const now = Date.now();
  const sortedList = [...list].sort((a, b) => {
    const rpA = state.stats?.[`RP:${a.id}`];
    const rpB = state.stats?.[`RP:${b.id}`];

    const dueA = rpA?.nextDue && rpA.nextDue <= now;
    const dueB = rpB?.nextDue && rpB.nextDue <= now;
    if (dueA && !dueB) return -1;
    if (!dueA && dueB) return 1;

    const unreadA = !rpA || (rpA.reads || 0) === 0;
    const unreadB = !rpB || (rpB.reads || 0) === 0;
    if (unreadA && !unreadB) return -1;
    if (!unreadA && unreadB) return 1;

    return 0;
  });

  sortedList.forEach(l => {
    const qCount = (l.comprehensionQuestions || l.questions || l.drills || []).length;
    const charCount = countPassageChars(l.passage || l);
    const estMinutes = Math.max(2, Math.ceil(charCount / DEFAULT_READING_CPM) || Math.round(qCount * 2));
    const rpKey = `RP:${l.id}`;
    const rp = state.stats?.[rpKey];
    const isDue = rp?.nextDue && rp.nextDue <= now;

    const card = document.createElement('div');
    card.className = `dokkai-card${isDue ? ' re-read-due' : ''}`;
    card.onclick = () => openReadingLesson(l.id);

    const genre = categorizePassage(l);
    const genreMeta = GENRE_METADATA[genre] || GENRE_METADATA.other;
    const genreText = l.genre || genreMeta.label_ja;
    const pagesText = l.pages ? `pp. ${l.pages.join('–')}` : '';

    // Status ring / badge
    let statusBadge = '<span class="dokkai-status-badge unread">Unread</span>';
    if (rp?.mastered) {
      statusBadge = '<span class="dokkai-status-badge mastered"><i class="fa-solid fa-crown"></i> Mastered</span>';
    } else if (isDue) {
      statusBadge = '<span class="dokkai-status-badge due"><i class="fa-solid fa-bell"></i> Re-read Due</span>';
    } else if (rp?.reads > 0) {
      statusBadge = `<span class="dokkai-status-badge read">${rp.reads} read${rp.reads > 1 ? 's' : ''}</span>`;
    }

    // Best metrics
    let metricsHtml = '';
    if (rp && rp.bestAcc !== undefined) {
      metricsHtml = `
        <div class="dokkai-card-stats-pill">
          <span><i class="fa-solid fa-bullseye"></i> ${Math.round(rp.bestAcc * 100)}%</span>
          <span><i class="fa-solid fa-gauge-high"></i> ${rp.bestCpm || 0} CPM</span>
        </div>`;
    }

    card.innerHTML = `
      <div class="dokkai-card-top">
        <div style="display:flex; align-items:center; gap:0.4rem;">
          <span class="dokkai-genre-pill">${genreText}</span>
          ${isDue ? '<span class="dokkai-due-dot" title="Re-read pass due"></span>' : ''}
        </div>
        <div style="display:flex; align-items:center; gap:0.5rem;">
          <span style="font-size: 0.8rem; color: var(--text-dim);">${pagesText}</span>
          ${statusBadge}
        </div>
      </div>
      <div>
        <h4 class="dokkai-card-title font-ja">${l.title_ja || l.title}</h4>
        <p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.35rem;">${l.title_en || ''}</p>
      </div>
      ${metricsHtml}
      <div class="dokkai-card-meta">
        <span><i class="fa-solid fa-list-check"></i> ${qCount} Questions</span>
        ${charCount > 0 ? `<span><i class="fa-solid fa-font"></i> ~${charCount} chars</span>` : ''}
        <span><i class="fa-solid fa-clock"></i> ~${estMinutes} mins</span>
      </div>
    `;
    container.appendChild(card);
  });

  // RD-8: Problems 42-48 coming soon placeholder for Medium category
  if (state.readingCategory === 'all' || state.readingCategory === 'real_medium') {
    const placeholder = document.createElement('div');
    placeholder.className = 'dokkai-card dokkai-placeholder-card';
    placeholder.innerHTML = `
      <div class="dokkai-card-top">
        <span class="dokkai-genre-pill" style="background: var(--surface); color: var(--text-dim);">中文 (Medium)</span>
        <span style="font-size: 0.8rem; color: var(--text-dim);">pp. 82–95</span>
      </div>
      <div>
        <h4 class="dokkai-card-title font-ja" style="color: var(--text-muted);">問題 42–48 (準備中)</h4>
        <p style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.35rem;">Problems 42–48 coming in the next content update</p>
      </div>
      <div class="dokkai-card-meta">
        <span><i class="fa-solid fa-lock"></i> Pending release</span>
      </div>
    `;
    container.appendChild(placeholder);
  }
}

// =======================================================
// LESSON PICKER (mirrors the Vocabulary Home / Kanji tab)
// =======================================================

let _vocabTermIndex = null;
function getVocabTermIndex() {
  if (_vocabTermIndex && _vocabTermIndex._src === state.vocabDB) return _vocabTermIndex.map;
  const map = new Map();
  if (state.vocabDB) {
    for (const chId in state.vocabDB) {
      for (const w of (state.vocabDB[chId] || [])) {
        const t = (w.term_ja || w.term || '').trim();
        if (t && !map.has(t)) map.set(t, w.id);
      }
    }
  }
  _vocabTermIndex = { _src: state.vocabDB, map };
  return map;
}

// Resolve a reading-passage word to the same SRS key "Add to My Words" would use.
function readingWordKey(term) {
  const t = (term || '').trim();
  if (!t) return null;
  const vid = getVocabTermIndex().get(t);
  if (vid) return `V:${vid}`;
  if (state.idx?.words?.[t]) return `KWR:${t}`;
  return `RW:${t}`;
}

let _readingOrderCache = null;
function getOrderedReadingLessons() {
  if (_readingOrderCache && _readingOrderCache._src === state.readingDB) return _readingOrderCache.lessons;
  const db = state.readingDB || {};
  const cats = state.readingCategories || {};
  const catOrder = ['foundation', 'strategy', 'real_short', 'real_medium', 'real_long', 'info'];
  const seen = new Set();
  const lessons = [];
  for (const cat of catOrder) {
    for (const id of (cats[cat] || [])) {
      if (db[id] && !seen.has(id)) { seen.add(id); lessons.push(db[id]); }
    }
  }
  for (const id in db) {
    if (!seen.has(id)) { seen.add(id); lessons.push(db[id]); }
  }
  _readingOrderCache = { _src: state.readingDB, lessons };
  return lessons;
}

function filterReadingByCategory(list) {
  if (state.readingCategory === 'all') return list;
  return list.filter(l => {
    if (l.category === state.readingCategory) return true;
    const genre = categorizePassage(l);
    if (state.readingCategory === 'real_short' && genre === 'short') return true;
    if (state.readingCategory === 'real_medium' && genre === 'medium') return true;
    if (state.readingCategory === 'real_long' && genre === 'long') return true;
    if (state.readingCategory === 'info' && genre === 'info') return true;
    return false;
  });
}

function selectedReadingLessons() {
  const all = getOrderedReadingLessons();
  const isAll = !state.readingSelectionEmpty && state.readingSelectedLessons.size === 0;
  if (isAll) return all;
  if (state.readingSelectionEmpty || !(state.readingSelectedLessons instanceof Set)) return [];
  return all.filter(l => state.readingSelectedLessons.has(l.id));
}

// A lesson is gradable only when it has both a timed passage and at least one
// comprehension question. Strategy/drill-only pages (e.g. 長い文に慣れる) have
// neither; scoring or re-read scheduling them records false progress.
export function isGradableReadingLesson(lesson) {
  if (!lesson) return false;
  const chars = countPassageChars(lesson.passage || lesson);
  const qCount = (lesson.comprehensionQuestions || lesson.questions || []).length;
  return chars > 0 && qCount > 0;
}

export function renderReadingLessonChips() {
  const container = document.getElementById('reading-lesson-chips-row');
  if (!container) return;
  container.innerHTML = '';
  if (!(state.readingSelectedLessons instanceof Set)) state.readingSelectedLessons = new Set();
  if (state.readingSelectedLessons.size > 0) state.readingSelectionEmpty = false;

  const ordered = getOrderedReadingLessons();
  const numById = new Map(ordered.map((l, i) => [l.id, i + 1]));
  const list = filterReadingByCategory(ordered);
  const isAll = !state.readingSelectionEmpty && state.readingSelectedLessons.size === 0;

  list.forEach(l => {
    const vocab = l.vocabulary || [];
    let hasHard = false;
    vocab.forEach(v => {
      const k = readingWordKey(v.term);
      if (k && peekItemStatus(k) === 'hard') hasHard = true;
    });
    const rp = state.stats?.[`RP:${l.id}`];
    const allDone = Boolean(rp?.mastered);
    const selected = isAll || state.readingSelectedLessons.has(l.id);
    const qCount = (l.comprehensionQuestions || l.questions || l.drills || []).length;
    const num = numById.get(l.id);

    const tile = document.createElement('button');
    tile.type = 'button';
    tile.className = `home-lesson-tile${selected ? ' selected' : ''}${hasHard ? ' has-hard' : ''}${allDone ? ' all-done' : ''}`;
    tile.setAttribute('aria-pressed', String(selected));
    tile.setAttribute('aria-label', `Lesson ${num}, ${l.title_en || l.title_ja}, ${vocab.length} words, ${qCount} questions`);
    tile.title = `${l.title_ja || ''} · ${l.title_en || ''} · ${vocab.length} words · ${qCount} questions`;
    tile.innerHTML = `<span class="home-lesson-tile-num">${num}</span><span class="home-lesson-tile-count">${vocab.length}w</span><span class="home-lesson-tile-dot" aria-hidden="true"></span>`;
    tile.onclick = () => selectReadingLesson(l.id, 'toggle');
    container.appendChild(tile);
  });

  const selAllBtn = document.getElementById('reading-select-all');
  if (selAllBtn) selAllBtn.onclick = () => selectReadingLesson('all');
  const clearBtn = document.getElementById('reading-clear-selection');
  if (clearBtn) clearBtn.onclick = () => {
    state.readingSelectedLessons.clear();
    state.readingSelectionEmpty = true;
    renderReadingLessonChips();
  };

  const meta = document.getElementById('reading-picker-heading-meta');
  if (meta) meta.textContent = `${ordered.length} lessons`;

  updateReadingPickerSummary();
}

export function selectReadingLesson(id, mode = 'toggle') {
  if (!(state.readingSelectedLessons instanceof Set)) state.readingSelectedLessons = new Set();
  if (id === 'all') {
    state.readingSelectedLessons.clear();
    state.readingSelectionEmpty = false;
  } else {
    state.readingSelectionEmpty = false;
    if (state.readingSelectedLessons.has(id)) state.readingSelectedLessons.delete(id);
    else state.readingSelectedLessons.add(id);
  }
  renderReadingLessonChips();
}

function updateReadingPickerSummary() {
  const summaryEl = document.getElementById('reading-picker-summary');
  const hintEl = document.getElementById('reading-start-hint');
  const badge = document.getElementById('reading-hard-count-badge');
  const selected = selectedReadingLessons();
  const wordKeys = new Set();
  let qCount = 0;
  selected.forEach(l => {
    (l.vocabulary || []).forEach(v => { const k = readingWordKey(v.term); if (k) wordKeys.add(k); });
    qCount += (l.comprehensionQuestions || l.questions || l.drills || []).length;
  });
  let hardCount = 0;
  wordKeys.forEach(k => { if (peekItemStatus(k) === 'hard') hardCount++; });

  if (summaryEl) {
    summaryEl.textContent = selected.length === 0
      ? 'No lessons selected'
      : `${selected.length} lesson${selected.length === 1 ? '' : 's'} selected · ${wordKeys.size} words · ${qCount} questions`;
  }
  if (hintEl) {
    hintEl.textContent = selected.length === 0
      ? 'Tap lesson tiles above, then read them as a book, practise with the timer, or drill their words.'
      : '';
  }
  if (badge) {
    badge.style.display = hardCount > 0 ? '' : 'none';
    badge.textContent = hardCount;
  }
}

function flashReadingHint(msg) {
  const hintEl = document.getElementById('reading-start-hint');
  if (hintEl) hintEl.textContent = msg;
}

// =======================================================
// BOOK MODE: browse passages + informative sections freely
// =======================================================

export function startReadingBook() {
  const lessons = selectedReadingLessons();
  if (lessons.length === 0) {
    flashReadingHint('Select one or more lessons first - the book opens on the first and lets you skip between them.');
    return;
  }
  readerRuntime.bookQueue = lessons.map(l => l.id);
  readerRuntime.bookIndex = 0;
  openReadingLesson(lessons[0].id, { startPhase: 'book' });
}

export function bookNavReading(delta) {
  const q = readerRuntime.bookQueue || [];
  if (!q.length) return;
  const next = Math.min(q.length - 1, Math.max(0, (readerRuntime.bookIndex ?? 0) + delta));
  if (next === readerRuntime.bookIndex) return;
  readerRuntime.bookIndex = next;
  openReadingLesson(q[next], { startPhase: 'book' });
}

export function jumpReadingBookLesson(id) {
  const q = readerRuntime.bookQueue || [];
  const idx = q.indexOf(id);
  if (idx === -1) return;
  readerRuntime.bookIndex = idx;
  openReadingLesson(id, { startPhase: 'book' });
}

// =======================================================
// PRACTICE CHAINING: run selected lessons back to back
// =======================================================

export function startReadingPractice() {
  const lessons = selectedReadingLessons();
  if (lessons.length === 0) {
    flashReadingHint('Select one or more lessons first.');
    return;
  }
  // Timed practice needs a passage and questions to grade; strategy/drill-only
  // pages open in the book instead of faking a 0/0 pass.
  const gradable = lessons.filter(isGradableReadingLesson);
  const skipped = lessons.length - gradable.length;
  if (gradable.length === 0) {
    flashReadingHint(skipped > 0
      ? 'The selected lesson(s) are strategy pages with no timed passage or questions - open them with Read as book instead.'
      : 'Select one or more lessons first.');
    return;
  }
  if (skipped > 0) {
    flashReadingHint(`${skipped} strategy-only lesson${skipped === 1 ? '' : 's'} skipped (no passage/questions to grade) - read them with Read as book.`);
  }
  const ids = gradable.map(l => l.id);
  openReadingLesson(ids[0], { practiceQueue: ids, practiceIndex: 0 });
}

export function practiceNextReadingLesson() {
  const q = readerRuntime.practiceQueue || [];
  const next = (readerRuntime.practiceIndex ?? -1) + 1;
  if (next < 0 || next >= q.length) { closeReadingWorkspace(); return; }
  openReadingLesson(q[next], { practiceQueue: q, practiceIndex: next });
}

// =======================================================
// CHAPTER-WISE WORD DRILL (mirrors the Kanji hard drill)
// =======================================================

export function startReadingWordDrill(hardOnly = false) {
  const lessons = selectedReadingLessons();
  if (lessons.length === 0) {
    flashReadingHint('Select one or more lessons first - the drill pools their key vocabulary.');
    return;
  }
  readerRuntime.lastDrillHardOnly = Boolean(hardOnly);

  const seen = new Set();
  const pool = [];
  for (const l of lessons) {
    for (const v of (l.vocabulary || [])) {
      const term = (v.term || '').trim();
      if (!term) continue;
      const key = readingWordKey(term);
      if (!key || seen.has(key)) continue;
      seen.add(key);
      if (hardOnly && peekItemStatus(key) !== 'hard') continue;
      pool.push({
        id: key,
        key,
        type: 'vocab',
        book: 'reading',
        term_ja: term,
        ruby_html: v.reading && v.reading !== term ? `<ruby>${term}<rt>${v.reading}</rt></ruby>` : term,
        reading: v.reading || '',
        meaning_en: v.meaning || '',
        section_title_ja: l.title_ja || ''
      });
    }
  }

  if (pool.length === 0) {
    flashReadingHint(hardOnly
      ? 'No hard words in the selected lessons yet. Drill words first - struggling ones then appear here.'
      : 'The selected lessons have no key vocabulary.');
    return;
  }

  // Same session bootstrap as startStudy() so grades, re-queues and Gist sync match.
  state.homeRunQueue = [];
  state.homeRunBatchRun = false;
  state.kanjiRunQueue = [];
  state.kanjiRunBatchRun = false;
  state.studyMode = 'flashcard';
  state.studyIsDrillHard = Boolean(hardOnly);
  state.drillOrigin = 'reading';
  state.isDueReviewMode = false;
  state.learnUnit = null;

  beginGistReviewSession();
  pool.sort(() => Math.random() - 0.5);
  state.sessionItems = pool;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = pool.length;
  state.sessionTotal = pool.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

export function restartReadingWordDrill() {
  startReadingWordDrill(readerRuntime.lastDrillHardOnly);
}

// =======================================================
// READING WORKSPACE CONTROLLER
// =======================================================

export function openReadingLesson(lessonId, options = {}) {
  const lesson = state.readingDB?.[lessonId];
  if (!lesson) {
    console.warn(`Reading lesson ${lessonId} not found in readingDB.`);
    return;
  }

  // Switch to reading view if opened from elsewhere (Home/Daily/Study)
  if (typeof window !== 'undefined' && window.showView && state.currentView !== 'reading') {
    window.showView('reading');
  }

  stopTimer();

  // Strategy/drill-only pages have no passage or questions to time or grade.
  // Any non-book entry (Start practice, Home/Daily shortcuts) opens them in
  // the book instead, where their strategy and drill sections render.
  if (options.startPhase !== 'book' && !isGradableReadingLesson(lesson)) {
    options = { ...options, startPhase: 'book' };
  }

  const rpKey = `RP:${lessonId}`;
  const rp = state.stats?.[rpKey];
  // Book mode is relaxed browsing: never a locked second pass.
  const isSecondPass = options.startPhase === 'book'
    ? false
    : Boolean(options.isSecondPass || (rp && (rp.reads || 0) >= 1));

  // Book queue persists across book navigation; anything else clears it.
  if (options.startPhase !== 'book') {
    readerRuntime.bookQueue = [];
    readerRuntime.bookIndex = -1;
  }
  // Practice chaining comes only from an explicit queue handoff.
  readerRuntime.practiceQueue = options.practiceQueue || [];
  readerRuntime.practiceIndex = options.practiceIndex !== undefined
    ? options.practiceIndex
    : (options.practiceQueue ? 0 : -1);
  readerRuntime.bookSectionIndex = options.bookSectionIndex ?? 0;

  const questions = lesson.comprehensionQuestions || lesson.questions || [];

  readerRuntime.lesson = lesson;
  state.activeReadingLesson = lesson;
  readerRuntime.isSecondPass = isSecondPass;
  readerRuntime.selectedAnswers = {};
  state.readingAnswers = {};
  readerRuntime.submitted = false;
  state.readingQuizSubmitted = false;
  readerRuntime.elapsedSeconds = 0;
  readerRuntime.readStartTime = null;
  readerRuntime.expandedSentenceTrans.clear();
  readerRuntime.activeGlossWord = null;
  readerRuntime.showOptionEn = false;
  readerRuntime.showPassageInAnswer = false;

  readerRuntime.charCount = countPassageChars(lesson.passage || lesson);
  readerRuntime.targetSeconds = calculateTargetSeconds(readerRuntime.charCount);

  if (isSecondPass) {
    // Second pass rules: furigana and translation forced off, options shuffled
    readerRuntime.settings.showFurigana = false;
    readerRuntime.settings.showTranslations = false;
    state.showFurigana = false;
    state.showSentenceTranslations = false;
    readerRuntime.shuffledQuestions = questions.map(q => shuffleQuestionOptions(q));
  } else {
    readerRuntime.settings = loadReaderSettings();
    state.showFurigana = readerRuntime.settings.showFurigana;
    state.showSentenceTranslations = readerRuntime.settings.showTranslations;
    readerRuntime.shuffledQuestions = questions.map(q => ({ ...q }));
  }

  // Determine starting phase
  readerRuntime.phase = options.startPhase || 'preview';

  const listSection = document.getElementById('dokkai-list-section');
  const workspaceSection = document.getElementById('dokkai-workspace-section');
  if (listSection) listSection.style.display = 'none';
  if (workspaceSection) workspaceSection.style.display = 'block';

  // Focused reading: hide the hub chrome (hub title, stats banner, sub-tabs)
  // and the floating dock/sync pill while a lesson workspace is open.
  const readingView = document.getElementById('view-reading');
  if (readingView) readingView.classList.add('reading-focus');
  document.body.classList.add('reading-focus');

  renderWorkspace();
  if (readerRuntime.phase === 'book') scrollBookIntoView();
  else window.scrollTo({ top: 0, behavior: 'smooth' });
}

export function closeReadingWorkspace() {
  endGistReviewSession();
  stopTimer();
  readerRuntime.lesson = null;
  state.activeReadingLesson = null;
  readerRuntime.bookQueue = [];
  readerRuntime.bookIndex = -1;
  readerRuntime.practiceQueue = [];
  readerRuntime.practiceIndex = -1;

  const listSection = document.getElementById('dokkai-list-section');
  const workspaceSection = document.getElementById('dokkai-workspace-section');
  if (listSection) listSection.style.display = 'block';
  if (workspaceSection) workspaceSection.style.display = 'none';

  const readingView = document.getElementById('view-reading');
  if (readingView) readingView.classList.remove('reading-focus');
  document.body.classList.remove('reading-focus');

  renderReadingLessonChips();
  renderLessonList();
}

export function renderWorkspace() {
  const container = document.getElementById('dokkai-workspace-container');
  if (!container || !readerRuntime.lesson) return;

  ensureReaderStyles();

  switch (readerRuntime.phase) {
    case 'book':
      renderBookPhase(container);
      break;
    case 'preview':
      renderPreviewPhase(container);
      break;
    case 'read':
      renderReadPhase(container);
      break;
    case 'answer':
      renderAnswerPhase(container);
      break;
    case 'review':
      renderReviewPhase(container);
      break;
    default:
      renderPreviewPhase(container);
      break;
  }
}

// =======================================================
// BOOK PHASE: section-by-section reading, no timer
// One labelled section per page with Back/Next paging that
// flows across the selected lessons like a book.
// =======================================================

function getBookSections(lesson) {
  const sentences = lesson.passage ? (lesson.passage.sentences || []) : [];
  const drills = lesson.drills || [];
  const vocabulary = lesson.vocabulary || [];
  const commentary = lesson.commentary;
  const commentaryJa = commentary ? (commentary.text_ja || commentary.summary_ja || commentary.logicFlow || '') : '';
  const sections = [];
  if (lesson.readingStrategy) sections.push({ id: 'strategy', ja: '読解ストラテジー', en: 'Strategy', icon: 'fa-chess' });
  if (lesson.preReading) sections.push({ id: 'prereading', ja: '読む前に', en: 'Before Reading', icon: 'fa-lightbulb' });
  if (sentences.length > 0) sections.push({ id: 'passage', ja: '本文', en: 'Passage', icon: 'fa-book-open-reader' });
  if (drills.length > 0) sections.push({ id: 'drills', ja: '練習', en: `Drills (${drills.length})`, icon: 'fa-pen-to-square' });
  // Key Vocabulary section removed at his ask (2026-11-03): every lesson word
  // is drilled from the Reading home word drills, so the in-book list was
  // duplicate navigation. Vocabulary data itself is untouched.
  // Tough words only appears when it has content (his ask 2026-11-05): an empty
  // flagged-words page in the reading sequence is a dead tap. Word revision stays
  // available from the Reading home word drills either way.
  const toughWords = getLessonToughWords(lesson);
  if (toughWords.length > 0) sections.push({ id: 'tough', ja: '苦手な言葉', en: `Tough words (${toughWords.length})`, icon: 'fa-fire' });
  if (lesson.testAdvice) sections.push({ id: 'advice', ja: '試験のコツ', en: 'Test Advice', icon: 'fa-compass' });
  if (commentary && commentaryJa) sections.push({ id: 'commentary', ja: '本文の解説', en: 'Commentary', icon: 'fa-diagram-project' });
  if (sections.length === 0) sections.push({ id: 'overview', ja: '概要', en: 'Overview', icon: 'fa-circle-info' });
  return sections;
}

function scrollBookIntoView() {
  const ws = document.getElementById('dokkai-workspace-section');
  if (ws) ws.scrollIntoView({ block: 'start', behavior: 'smooth' });
  else window.scrollTo({ top: 0, behavior: 'smooth' });
}

export function bookNavSection(delta) {
  const lesson = readerRuntime.lesson;
  if (!lesson) return;
  const q = readerRuntime.bookQueue || [];
  const sections = getBookSections(lesson);
  const cur = readerRuntime.bookSectionIndex ?? 0;
  const next = cur + delta;
  if (next >= 0 && next < sections.length) {
    readerRuntime.bookSectionIndex = next;
    renderWorkspace();
    scrollBookIntoView();
    return;
  }
  // Spill over into the neighbouring lesson, book-style.
  const idx = readerRuntime.bookIndex ?? 0;
  if (delta > 0 && idx < q.length - 1) {
    readerRuntime.bookIndex = idx + 1;
    openReadingLesson(q[idx + 1], { startPhase: 'book', bookSectionIndex: 0 });
  } else if (delta < 0 && idx > 0) {
    const prevId = q[idx - 1];
    const prevLesson = state.readingDB?.[prevId];
    readerRuntime.bookIndex = idx - 1;
    openReadingLesson(prevId, { startPhase: 'book', bookSectionIndex: prevLesson ? getBookSections(prevLesson).length - 1 : 0 });
  }
}

export function jumpReadingBookSection(i) {
  const lesson = readerRuntime.lesson;
  if (!lesson) return;
  const sections = getBookSections(lesson);
  const n = Number(i);
  if (!Number.isInteger(n) || n < 0 || n >= sections.length) return;
  readerRuntime.bookSectionIndex = n;
  renderWorkspace();
  scrollBookIntoView();
}

function bookVocabChipHtml(v) {
  const term = (v.term || '').replace(/'/g, "\\'");
  const reading = (v.reading || '').replace(/'/g, "\\'");
  const meaning = (v.meaning || '').replace(/'/g, "\\'");
  return `
    <div class="vocab-preview-chip">
      <div class="vocab-preview-text">
        <span class="font-ja vocab-chip-term">${v.term}</span>
        <span class="vocab-chip-reading">${v.reading || ''}</span>
        <span class="vocab-chip-meaning">${v.meaning || ''}</span>
      </div>
      <button class="btn btn-xs btn-ghost btn-chip-add" onclick="event.stopPropagation(); addWordFromPreview('${term}', '${reading}', '${meaning}', this)">
        + Add
      </button>
    </div>`;
}

// Words of this lesson flagged tough: flame-marked or weight past the hard
// threshold. Non-mutating peek - browsing never creates SRS records.
function getLessonToughWords(lesson) {
  const out = [];
  const seen = new Set();
  for (const v of (lesson.vocabulary || [])) {
    const term = (v.term || '').trim();
    if (!term || seen.has(term)) continue;
    seen.add(term);
    const key = readingWordKey(term);
    if (key && peekItemStatus(key) === 'hard') out.push(v);
  }
  return out;
}



function renderBookDrillCard(d) {
  const titleJa = bookJaText(d.title_ja, d.title_ja_ruby);
  const instrJa = glossifyBookText(bookJaText(d.instruction_ja, d.instruction_ja_ruby));
  const sentenceJa = glossifyBookText(bookJaText(d.originalSentence_ja, d.originalSentence_ruby));
  return `
    <div class="book-drill-card">
      <div class="book-drill-title font-ja">${titleJa}</div>
      ${d.title_en ? `<div class="book-drill-sub">${d.title_en}</div>` : ''}
      ${d.instruction_ja ? `<p class="font-ja" style="margin: 0.4rem 0 0.2rem;">${instrJa}</p>` : ''}
      ${d.instruction_en ? `<p style="color: var(--text-dim); font-size: 0.82rem;">${d.instruction_en}</p>` : ''}
      ${sentenceJa ? `<p class="font-ja book-drill-sentence">${sentenceJa}</p>` : ''}
      ${d.originalSentence_en ? `<p style="color: var(--text-dim); font-size: 0.82rem;">${d.originalSentence_en}</p>` : ''}
      ${(d.items || []).length ? `
        <div class="book-drill-items">
          ${d.items.map(it => `
            <details class="book-drill-answer book-drill-item">
              <summary><span class="font-ja drill-item-term">${it.marker ? `${it.marker}. ` : ''}${it.term_ja || ''}${it.reading && it.reading !== it.term_ja ? `（${it.reading}）` : ''}</span></summary>
              ${it.hint_ja ? `<p class="font-ja" style="margin-top: 0.3rem;">${glossifyBookText(it.hint_ja)}</p>` : ''}
              ${it.hint_en ? `<p style="color: var(--text-dim); font-size: 0.82rem;">${it.hint_en}</p>` : ''}
              ${it.meaning_ja ? `<p class="font-ja" style="margin-top: 0.25rem; font-weight: 600;">${it.meaning_ja}</p>` : ''}
              ${it.meaning_en ? `<p style="color: var(--text-dim); font-size: 0.82rem; margin-top: 0.2rem;">${it.meaning_en}</p>` : ''}
            </details>`).join('')}
        </div>` : ''}
      ${(d.options || []).length ? `
        <div class="book-drill-items">
          ${d.options.map(o => `
            <div class="book-drill-option">
              <span class="drill-option-key">${o.key}</span>
              <span class="font-ja">${o.text_ja || ''}</span>
              ${o.text_en ? `<div style="color: var(--text-dim); font-size: 0.8rem; margin-left: 1.5rem;">${o.text_en}</div>` : ''}
            </div>`).join('')}
        </div>
        ${d.correctKey ? `
          <details class="book-drill-answer"><summary>Show answer</summary>
            <p style="margin-top: 0.35rem;">Answer: <strong>${d.correctKey}</strong></p>
            ${d.explanation_en ? `<p style="color: var(--text-dim); font-size: 0.82rem; margin-top: 0.3rem;">${d.explanation_en}</p>` : ''}
          </details>` : ''}` : ''}
      ${d.solution ? `
        <details class="book-drill-answer"><summary>Show answer</summary>
          <p class="font-ja" style="margin-top: 0.35rem;">${d.solution}</p>
          ${d.explanation_en ? `<p style="color: var(--text-dim); font-size: 0.82rem; margin-top: 0.3rem;">${d.explanation_en}</p>` : ''}
        </details>` : ''}
    </div>`;
}

function bookFuriganaToggleBtn() {
  const on = readerRuntime.settings.showFurigana;
  return `<button class="t-btn-toggle${on ? ' active' : ''}" style="margin-left: auto;"
                  onclick="togglePassageFurigana()"
                  title="${on ? 'Hide furigana' : 'Show furigana'}">ふりがな</button>`;
}

function renderBookPhase(container) {
  const lesson = readerRuntime.lesson;
  const q = readerRuntime.bookQueue || [];
  const idx = readerRuntime.bookIndex ?? 0;
  const ordered = getOrderedReadingLessons();
  const numById = new Map(ordered.map((l, i) => [l.id, i + 1]));
  const genre = categorizePassage(lesson);
  const genreMeta = GENRE_METADATA[genre] || GENRE_METADATA.other;
  const sentences = lesson.passage ? (lesson.passage.sentences || []) : [];
  const vocabMap = new Map((lesson.vocabulary || []).map(v => [v.term, v]));
  const footnotes = lesson.footnotes || [];
  const questions = lesson.comprehensionQuestions || lesson.questions || [];
  const drills = lesson.drills || [];
  const strategy = lesson.readingStrategy;
  const vocabulary = lesson.vocabulary || [];

  const sections = getBookSections(lesson);
  let sIdx = readerRuntime.bookSectionIndex ?? 0;
  if (sIdx < 0 || sIdx >= sections.length) sIdx = 0;
  readerRuntime.bookSectionIndex = sIdx;
  const section = sections[sIdx];
  const isLastSection = sIdx === sections.length - 1;

  const jumpOptions = q.map((id, i) => {
    const l = state.readingDB?.[id];
    const t = l ? (l.title_ja || l.title || id) : id;
    return `<option value="${id}"${i === idx ? ' selected' : ''}>${numById.get(id) || i + 1}. ${t}</option>`;
  }).join('');

  const sectionOptions = sections.map((s, i) =>
    `<option value="${i}"${i === sIdx ? ' selected' : ''}>${i + 1}/${sections.length} · ${s.ja} ${s.en}</option>`).join('');

  // ---------- per-section bodies ----------
  let bodyHtml = '';

  if (section.id === 'strategy' && strategy) {
    const showRuby = readerRuntime.settings.showStrategyFurigana;
    const ruleJa = showRuby ? (strategy.rule_ja_ruby || strategy.rule_ja || '') : (strategy.rule_ja || '');
    bodyHtml = `
      <div class="book-section">
        <div class="book-section-label" style="display: flex; align-items: center; gap: 0.5rem;">
          <span><i class="fa-solid fa-chess"></i> 読解ストラテジー Strategy</span>
          <button class="t-btn-toggle${showRuby ? ' active' : ''}" style="margin-left: auto;"
                  onclick="toggleStrategyFurigana()"
                  title="${showRuby ? 'Hide furigana' : 'Show furigana'}">ふりがな</button>
        </div>
        <div class="strategy-display-card">
          <p style="line-height: 1.8;" class="font-ja">${glossifyBookText(ruleJa)}</p>
          ${strategy.rule_en ? `<p style="color: var(--text-dim); font-size: 0.9rem; margin-top: 0.35rem;">${strategy.rule_en}</p>` : ''}
        </div>
        ${(strategy.keyPoints || []).length > 0 ? `
          <div class="book-keypoints">
            ${strategy.keyPoints.map(kp => `
              <div class="book-keypoint">
                <div class="font-ja" style="font-weight: 700;">${glossifyBookText(showRuby ? (kp.point_ja_ruby || kp.point_ja || '') : (kp.point_ja || ''))}</div>
                ${kp.point_en ? `<div style="color: var(--text-muted); font-size: 0.85rem;">${kp.point_en}</div>` : ''}
                ${kp.explanation_en ? `<div style="color: var(--text-dim); font-size: 0.82rem; margin-top: 0.2rem;">${kp.explanation_en}</div>` : ''}
              </div>`).join('')}
          </div>` : ''}
      </div>`;
  } else if (section.id === 'prereading' && lesson.preReading) {
    const preJa = bookJaText(lesson.preReading.question_ja || lesson.preReading.question || '', lesson.preReading.question_ja_ruby);
    bodyHtml = `
      <div class="book-section">
        <div class="book-section-label" style="display: flex; align-items: center; gap: 0.5rem;">
          <span><i class="fa-solid fa-lightbulb"></i> 読む前に Before Reading</span>
          ${bookFuriganaToggleBtn()}
        </div>
        <div class="pre-reading-box">
          <p class="font-ja pre-reading-text">${glossifyBookText(preJa)}</p>
          ${lesson.preReading.question_en ? `<p class="pre-reading-sub">${lesson.preReading.question_en}</p>` : ''}
        </div>
      </div>`;
  } else if (section.id === 'passage') {
    bodyHtml = `
      <div class="book-section">
        <div class="book-section-label"><i class="fa-solid fa-book-open-reader"></i> 本文 Passage</div>
        ${lesson.passageInstructions ? `
          <div class="reading-instructions-box font-ja" style="margin-bottom: 0.6rem;">
            <strong><i class="fa-solid fa-circle-info"></i> 指示:</strong> ${lesson.passageInstructions.instruction_ja || ''}
            <div style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.2rem;">${lesson.passageInstructions.instruction_en || ''}</div>
          </div>` : ''}
        <div class="passage-view-card">
          <div class="passage-scroll-pane font-ja" id="passage-content-area" style="font-size: ${1.2 * readerRuntime.settings.fontScale}rem; max-height: none;">
            ${sentences.map(sn => renderPassageSentenceHTML(sn, vocabMap, footnotes)).join('')}
          </div>
          ${renderFootnotesBlock(footnotes)}
        </div>
      </div>`;
  } else if (section.id === 'drills') {
    bodyHtml = `
      <div class="book-section">
        <div class="book-section-label" style="display: flex; align-items: center; gap: 0.5rem;">
          <span><i class="fa-solid fa-pen-to-square"></i> 練習 Drills (${drills.length})</span>
          ${bookFuriganaToggleBtn()}
        </div>
        ${drills.map(d => renderBookDrillCard(d)).join('')}
      </div>`;
  } else if (section.id === 'tough') {
    const tough = getLessonToughWords(lesson);
    bodyHtml = `
      <div class="book-section">
        <div class="book-section-label"><i class="fa-solid fa-fire"></i> 苦手な言葉 Tough Words (${tough.length})</div>
        ${tough.length > 0 ? `
          <p class="book-tough-hint">Words you flagged tough in drills. Tap + Add to put them into My Words for revision.</p>
          <div class="preview-vocab-chips">
            ${tough.map(v => bookVocabChipHtml(v)).join('')}
          </div>
          <div class="book-tough-actions">
            <button class="btn btn-sm btn-secondary" onclick="startReadingWordDrill(true)"><i class="fa-solid fa-fire"></i> Drill tough words</button>
          </div>` : `
          <div class="book-tough-empty">
            <p>No tough words in this lesson yet.</p>
            <p>Words you flame-mark or grade <strong>Hard</strong>/<strong>Again</strong> in word drills are flagged tough and listed here, ready to add for revision. Any word can also be added from the Key Vocabulary section.</p>
          </div>`}
      </div>`;
  } else if (section.id === 'advice' && lesson.testAdvice) {
    const advice = lesson.testAdvice;
    let adviceBody = '';
    if (advice.advice_ja || advice.traps) {
      adviceBody = `<p style="margin-top: 0.6rem; line-height: 1.8;">${glossifyBookText(bookJaText(advice.advice_ja || advice.traps || '', advice.advice_ja_ruby))}</p>
        ${advice.advice_en ? `<p style="font-size: 0.85rem; color: var(--text-dim); margin-top: 0.35rem;">${advice.advice_en}</p>` : ''}`;
    } else if (Array.isArray(advice.analysisSteps)) {
      adviceBody = `<ol class="book-advice-steps">
        ${advice.analysisSteps.map(st => `
          <li>
            <div class="font-ja" style="font-weight: 700;">${glossifyBookText(bookJaText(st.question_ja || '', st.question_ja_ruby))}</div>
            ${(st.analysis_ja || st.analysis_ja_ruby) ? `<div class="font-ja" style="font-size: 0.88rem; color: var(--text-muted);">${glossifyBookText(bookJaText(st.analysis_ja, st.analysis_ja_ruby))}</div>` : ''}
            ${st.analysis_en ? `<div style="font-size: 0.8rem; color: var(--text-dim);">${st.analysis_en}</div>` : ''}
          </li>`).join('')}
      </ol>`;
    }
    bodyHtml = `
      <div class="test-advice-card font-ja">
        <h3 style="display: flex; align-items: center; gap: 0.5rem;">
          <span><i class="fa-solid fa-compass" style="color: var(--amber);"></i> 試験のコツ (Test Advice)</span>
          ${bookFuriganaToggleBtn()}
        </h3>
        ${adviceBody}
      </div>`;
  } else if (section.id === 'commentary' && lesson.commentary) {
    const commentary = lesson.commentary;
    const commentaryJaPlain = commentary.text_ja || commentary.summary_ja || commentary.logicFlow || '';
    const commentaryJaRuby = commentary.text_ja_ruby || commentary.summary_ja_ruby || '';
    const commentaryEn = commentary.text_en || commentary.summary_en || '';
    bodyHtml = `
      <div class="commentary-card font-ja">
        <h3 style="display: flex; align-items: center; gap: 0.5rem;">
          <span><i class="fa-solid fa-diagram-project" style="color: var(--cyan);"></i> ${commentary.title_ja || '本文の解説 (Commentary)'}</span>
          ${bookFuriganaToggleBtn()}
        </h3>
        <p style="margin-top: 0.6rem; line-height: 1.8;">${glossifyBookText(bookJaText(commentaryJaPlain, commentaryJaRuby))}</p>
        ${commentaryEn ? `<p style="font-size: 0.85rem; color: var(--text-dim); margin-top: 0.35rem;">${commentaryEn}</p>` : ''}
      </div>`;
  } else {
    // overview fallback: lesson has no content sections beyond the title
    bodyHtml = lesson.passageInstructions ? `
      <div class="book-section">
        <div class="reading-instructions-box font-ja">
          <strong><i class="fa-solid fa-circle-info"></i> 指示:</strong> ${lesson.passageInstructions.instruction_ja || ''}
          <div style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.2rem;">${lesson.passageInstructions.instruction_en || ''}</div>
        </div>
      </div>` : '';
  }

  const atStart = sIdx <= 0 && idx <= 0;
  const atEnd = isLastSection && idx >= q.length - 1;

  container.innerHTML = `
    <div class="reading-workspace-shell">
      <div class="reading-nav-bar">
        <button class="btn btn-sm btn-ghost" onclick="closeReadingWorkspace()">
          <i class="fa-solid fa-arrow-left"></i> Lessons
        </button>
        <span class="dokkai-flow-badge"><i class="fa-solid fa-book-open"></i> Book ${q.length ? `${idx + 1}/${q.length}` : ''}</span>
      </div>

      ${q.length > 1 ? `
        <div class="book-lesson-jump">
          <select class="book-jump-select" onchange="jumpReadingBookLesson(this.value)" aria-label="Jump to lesson">${jumpOptions}</select>
        </div>` : ''}

      <div class="book-jump-row book-section-pager">
        <button class="btn btn-sm btn-secondary" onclick="bookNavSection(-1)" ${atStart ? 'disabled' : ''}><i class="fa-solid fa-chevron-left"></i> Back</button>
        <select class="book-jump-select book-section-select" onchange="jumpReadingBookSection(this.value)" aria-label="Jump to section">${sectionOptions}</select>
        <button class="btn btn-sm btn-secondary" onclick="bookNavSection(1)" ${atEnd ? 'disabled' : ''}>Next <i class="fa-solid fa-chevron-right"></i></button>
      </div>

      <div class="passage-view-card">
        <div class="dokkai-card-top" style="margin-bottom: 0.5rem;">
          <span class="dokkai-genre-pill"><i class="fa-solid ${genreMeta.icon}"></i> ${lesson.genre || genreMeta.label_ja}</span>
          <span style="font-size: 0.85rem; color: var(--text-dim);">${lesson.pages ? `pp. ${lesson.pages.join('–')}` : ''}</span>
        </div>
        <h1 class="reading-title-large font-ja">${lesson.title_ja || lesson.title}</h1>
        <p class="reading-subtitle">${lesson.title_en || ''}</p>
      </div>

      ${bodyHtml}

      ${isLastSection && (sentences.length > 0 || questions.length > 0) ? `
        <div class="book-footer-actions">
          ${(sentences.length > 0 || questions.length > 0) ? `
            <button class="btn btn-primary" onclick="startReadingPassage()">
              <i class="fa-solid fa-play"></i> Timed practice
            </button>` : ''}
          ${questions.length > 0 ? `
            <button class="btn btn-ghost" onclick="skipToQuestions()">
              Questions (${questions.length}) <i class="fa-solid fa-forward"></i>
            </button>` : ''}
        </div>` : ''}
    </div>

    ${section.id === 'passage' ? `
    <!-- Reading display toolbar (no timer in book mode) -->
    <div class="reading-sticky-toolbar">
      <div class="toolbar-pill-group">
        <div class="toolbar-btn-group">
          <button class="t-btn" title="Decrease font size" onclick="adjustFontScale(-0.1)">A−</button>
          <span class="t-label">${Math.round(readerRuntime.settings.fontScale * 100)}%</span>
          <button class="t-btn" title="Increase font size" onclick="adjustFontScale(0.1)">A+</button>
        </div>
        <button class="t-btn-toggle${readerRuntime.settings.showFurigana ? ' active' : ''}" onclick="togglePassageFurigana()" title="Toggle Furigana">ふりがな</button>
        <button class="t-btn-toggle${readerRuntime.settings.showTranslations ? ' active' : ''}" onclick="togglePassageTranslations()" title="Toggle Translations">訳</button>
        <button class="t-btn-toggle${readerRuntime.settings.chunkMode ? ' active' : ''}" onclick="togglePassageChunks()" title="区切り Chunk Mode">区切り</button>
      </div>
    </div>` : ''}

    <!-- Gloss Mini Sheet Container -->
    <div id="word-gloss-sheet-container"></div>
  `;
}


// =======================================================
// FLOW PHASE 1: PREVIEW (15-30 s, skippable)
// =======================================================

function renderPreviewPhase(container) {
  const lesson = readerRuntime.lesson;
  const questions = readerRuntime.shuffledQuestions;
  const genre = categorizePassage(lesson);
  const genreMeta = GENRE_METADATA[genre] || GENRE_METADATA.other;
  const estMins = Math.max(1, Math.ceil(readerRuntime.targetSeconds / 60));
  const vocabList = (lesson.vocabulary || []).slice(0, 8);

  container.innerHTML = `
    <div class="reading-workspace-shell">
      <div class="reading-nav-bar">
        <button class="btn btn-sm btn-ghost" onclick="closeReadingWorkspace()">
          <i class="fa-solid fa-arrow-left"></i> All Passages
        </button>
        <span class="dokkai-flow-badge"><i class="fa-solid fa-eye"></i> Step 1: Preview</span>
      </div>

      <div class="reading-preview-card">
        <div class="dokkai-card-top" style="margin-bottom: 0.5rem;">
          <span class="dokkai-genre-pill"><i class="fa-solid ${genreMeta.icon}"></i> ${lesson.genre || genreMeta.label_ja}</span>
          <span style="font-size: 0.85rem; color: var(--text-dim);">${lesson.pages ? `pp. ${lesson.pages.join('–')}` : ''}</span>
        </div>
        
        <h1 class="reading-title-large font-ja">${lesson.title_ja || lesson.title}</h1>
        <p class="reading-subtitle">${lesson.title_en || ''}</p>

        ${readerRuntime.isSecondPass ? `
          <div class="second-pass-alert">
            <i class="fa-solid fa-rotate"></i>
            <div>
              <strong>Second-Pass Re-read Mode</strong>
              <p>Furigana and translation are forced OFF. Question options are shuffled. Aim for &ge; 80% accuracy within 1.3&times; target time.</p>
            </div>
          </div>
        ` : ''}

        <div class="reading-stat-grid">
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-font"></i> Characters</span>
            <span class="stat-val font-ja">${readerRuntime.charCount || '—'}</span>
          </div>
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-clock"></i> Target Time</span>
            <span class="stat-val">~${estMins} min (${formatTime(readerRuntime.targetSeconds)})</span>
          </div>
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-circle-question"></i> Questions</span>
            <span class="stat-val">${questions.length}</span>
          </div>
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-gauge-high"></i> Target Pace</span>
            <span class="stat-val">${DEFAULT_READING_CPM} CPM</span>
          </div>
        </div>

        ${lesson.preReading ? `
          <div class="pre-reading-box">
            <div class="pre-reading-header"><i class="fa-solid fa-lightbulb"></i> Think First (Pre-Reading Prompt)</div>
            <p class="font-ja pre-reading-text">${glossifyBookText(bookJaText(lesson.preReading.question_ja || lesson.preReading.question || '', lesson.preReading.question_ja_ruby))}</p>
            ${lesson.preReading.question_en ? `<p class="pre-reading-sub">${lesson.preReading.question_en}</p>` : ''}
          </div>
        ` : ''}

        ${vocabList.length > 0 ? `
          <div class="preview-vocab-section">
            <div class="preview-vocab-header">
              <span><i class="fa-solid fa-book-bookmark"></i> Key Vocabulary (${vocabList.length})</span>
              <button class="btn btn-xs btn-ghost" onclick="addAllPassageWordsToMyWords()">
                <i class="fa-solid fa-plus"></i> Add all to my words
              </button>
            </div>
            <div class="preview-vocab-chips">
              ${vocabList.map(v => `
                <div class="vocab-preview-chip">
                  <div class="vocab-preview-text">
                    <span class="font-ja vocab-chip-term">${v.term}</span>
                    <span class="vocab-chip-reading">${v.reading || ''}</span>
                    <span class="vocab-chip-meaning">${v.meaning || ''}</span>
                  </div>
                  <button class="btn btn-xs btn-ghost btn-chip-add" onclick="event.stopPropagation(); addWordFromPreview('${v.term.replace(/'/g, "\\'")}', '${(v.reading||'').replace(/'/g, "\\'")}', '${(v.meaning||'').replace(/'/g, "\\'")}', this)">
                    + Add
                  </button>
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        <div class="preview-action-row">
          <button class="btn btn-primary btn-lg" onclick="startReadingPassage()">
            <i class="fa-solid fa-play"></i> Start Reading (⏱ Timer Starts)
          </button>
          <button class="btn btn-ghost" onclick="skipToQuestions()">
            Skip to Questions <i class="fa-solid fa-forward"></i>
          </button>
        </div>
      </div>
    </div>
  `;
}

// Optional furigana for book-mode strategy text. Off by default so the
// strategy can be attempted unaided first; the choice persists.
export function toggleStrategyFurigana() {
  readerRuntime.settings.showStrategyFurigana = !readerRuntime.settings.showStrategyFurigana;
  saveReaderSettings(readerRuntime.settings);
  renderWorkspace();
}

export function startReadingPassage() {
  beginGistReviewSession();
  readerRuntime.phase = 'read';
  readerRuntime.readStartTime = Date.now();
  startTimer();
  renderWorkspace();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

export function skipToQuestions() {
  beginGistReviewSession();
  stopTimer();
  readerRuntime.phase = 'answer';
  renderWorkspace();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// =======================================================
// FLOW PHASE 2: READ (Passage + Sticky Toolbar + Sentence Tap + Word Gloss)
// =======================================================

function renderReadPhase(container) {
  const lesson = readerRuntime.lesson;
  const sentences = lesson.passage ? (lesson.passage.sentences || []) : [];
  const vocabMap = new Map((lesson.vocabulary || []).map(v => [v.term, v]));
  const footnotes = lesson.footnotes || [];
  const isSecondPass = readerRuntime.isSecondPass;

  // Header and instructions
  container.innerHTML = `
    <div class="reading-workspace-shell">
      <div class="reading-nav-bar">
        <button class="btn btn-sm btn-ghost" onclick="closeReadingWorkspace()">
          <i class="fa-solid fa-arrow-left"></i> Exit Passage
        </button>
        <span class="dokkai-flow-badge"><i class="fa-solid fa-book-open"></i> Step 2: Read Passage</span>
      </div>

      <div class="passage-view-card">
        <div class="passage-view-header">
          <div>
            <h2 class="font-ja passage-view-title">${lesson.title_ja || lesson.title}</h2>
            <p style="color: var(--text-dim); font-size: 0.85rem;">${lesson.title_en || ''}</p>
          </div>
          <div class="passage-header-meta">
            <span><i class="fa-solid fa-font"></i> ${readerRuntime.charCount} chars</span>
            <span><i class="fa-solid fa-clock"></i> Target: ${formatTime(readerRuntime.targetSeconds)}</span>
          </div>
        </div>

        ${lesson.passageInstructions ? `
          <div class="reading-instructions-box font-ja">
            <strong><i class="fa-solid fa-circle-info"></i> 指示:</strong> ${lesson.passageInstructions.instruction_ja || ''}
            <div style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.2rem;">${lesson.passageInstructions.instruction_en || ''}</div>
          </div>` : ''}

        <!-- Passage Sentences -->
        <div class="passage-scroll-pane font-ja" id="passage-content-area" style="font-size: ${1.2 * readerRuntime.settings.fontScale}rem;">
          ${sentences.length > 0 ? sentences.map(s => renderPassageSentenceHTML(s, vocabMap, footnotes)).join('') : renderSkillsOrDrillFallback(lesson)}
        </div>
        ${renderFootnotesBlock(footnotes)}
      </div>

      <!-- Sticky Reading Toolbar -->
      <div class="reading-sticky-toolbar">
        <div class="toolbar-pill-group">
          <div class="toolbar-btn-group">
            <button class="t-btn" title="Decrease font size" onclick="adjustFontScale(-0.1)">A−</button>
            <span class="t-label">${Math.round(readerRuntime.settings.fontScale * 100)}%</span>
            <button class="t-btn" title="Increase font size" onclick="adjustFontScale(0.1)">A+</button>
          </div>

          <button class="t-btn-toggle${readerRuntime.settings.showFurigana ? ' active' : ''}${isSecondPass ? ' disabled' : ''}" 
                  onclick="togglePassageFurigana()" 
                  title="${isSecondPass ? 'Furigana locked OFF in 2nd pass' : 'Toggle Furigana'}">
            ふりがな
          </button>

          <button class="t-btn-toggle${readerRuntime.settings.showTranslations ? ' active' : ''}${isSecondPass ? ' disabled' : ''}" 
                  onclick="togglePassageTranslations()" 
                  title="${isSecondPass ? 'Translations locked OFF in 2nd pass' : 'Toggle Translations'}">
            訳
          </button>

          <button class="t-btn-toggle${readerRuntime.settings.chunkMode ? ' active' : ''}" 
                  onclick="togglePassageChunks()" 
                  title="区切り Chunk Mode (dividers after connectors)">
            区切り
          </button>
        </div>

        <div class="toolbar-timer-group">
          <div class="timer-pill" id="reader-live-timer">
            <i class="fa-solid fa-stopwatch"></i> ${formatTime(readerRuntime.elapsedSeconds)}
          </div>
          <button class="btn btn-primary btn-sm" onclick="goToQuestions()">
            Go to Questions <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>
      </div>

      <!-- Gloss Mini Sheet Container -->
      <div id="word-gloss-sheet-container"></div>
    </div>
  `;

  updateTimerPill();
}


// =======================================================
// GLOBAL PASSAGE GLOSSARY + FOOTNOTE MARKERS
// Lesson vocabulary is extended with the full dictionary so any
// word in a passage (or book-section text) is tappable for its
// reading and English meaning, with per-kanji meanings in the sheet.
// =======================================================

let glossCache = { lessonId: null, globalCount: -1, regex: null, map: new Map() };

function getGlossIndex(lesson) {
  const id = lesson ? lesson.id : null;
  // Rebuild when the global dictionary finishes loading after first render.
  let globalCount = -1;
  try { globalCount = getAllWords().length + getAllReadingLessons().length; } catch {}
  if (glossCache.lessonId === id && glossCache.globalCount === globalCount && glossCache.map.size > 0) return glossCache;
  const map = new Map();
  for (const v of ((lesson && lesson.vocabulary) || [])) {
    if (v.term && !map.has(v.term)) {
      map.set(v.term, { term: v.term, reading: v.reading || '', meaning: v.meaning || '', type: v.type || '' });
    }
  }
  try {
    for (const w of getAllWords()) {
      const term = (w.term_ja || '').trim();
      if (!term || map.has(term)) continue;
      map.set(term, { term, reading: w.reading || '', meaning: w.meaning_en || '', type: w.part_of_speech || '' });
    }
  } catch {}
  try {
    for (const other of getAllReadingLessons()) {
      for (const v of (other.vocabulary || [])) {
        const term = (v.term || '').trim();
        if (!term || map.has(term)) continue;
        map.set(term, { term, reading: v.reading || '', meaning: v.meaning || '', type: v.type || '' });
      }
    }
  } catch {}
  const terms = [...map.keys()]
    .filter(t => t.length >= 2)
    .sort((a, b) => b.length - a.length);
  const regex = terms.length ? new RegExp(terms.map(escapeRegExp).join('|'), 'g') : null;
  glossCache = { lessonId: id, globalCount, regex, map };
  return glossCache;
}

// Wrap dictionary terms found in html text nodes with tappable gloss spans.
// Skips content inside <rt> (furigana readings) and <sup> (footnote markers).
function wrapGlossTerms(html, gloss) {
  if (!html || !gloss || !gloss.regex) return html;
  const parts = html.split(/(<[^>]+>)/g);
  let skipDepth = 0;
  for (let i = 0; i < parts.length; i++) {
    const p = parts[i];
    if (!p) continue;
    if (p[0] === '<') {
      if (/^<(rt|sup)[\s>]/.test(p)) skipDepth++;
      else if (/^<\/(rt|sup)>/.test(p)) skipDepth = Math.max(0, skipDepth - 1);
      continue;
    }
    if (skipDepth > 0) continue;
    parts[i] = p.replace(gloss.regex, m =>
      `<span class="gloss-term" data-gloss="${m}" onclick="event.stopPropagation(); showWordGloss('${m.replace(/'/g, "\\'")}', this)">${m}</span>`);
  }
  return parts.join('');
}

// Make (注N) footnote markers tappable in both ruby (<sup>) and plain text.
function wrapFootnoteMarkers(html) {
  if (!html || html.indexOf('注') === -1) return html;
  html = html.replace(/<sup>\s*\(?（?注(\d+)\)?）?\s*<\/sup>/g,
    (m, n) => `<sup class="footnote-marker" onclick="event.stopPropagation(); scrollToFootnote(${n})">(注${n})</sup>`);
  html = html.replace(/(?<!>)（注(\d+)）|(?<!>)\(注(\d+)\)/g,
    (m, a, b) => `<sup class="footnote-marker" onclick="event.stopPropagation(); scrollToFootnote(${a || b})">(注${a || b})</sup>`);
  return html;
}

function glossifyBookText(html, lesson) {
  return wrapGlossTerms(html, getGlossIndex(lesson || readerRuntime.lesson));
}

function bookJaText(plain, ruby) {
  const showRuby = readerRuntime.settings.showFurigana;
  return showRuby ? (ruby || plain || '') : (plain || '');
}

function normalizeFootnote(fn, i) {
  const rawNum = fn.index !== undefined ? fn.index : (fn.number !== undefined ? fn.number : (fn.label !== undefined ? fn.label : i + 1));
  const num = String(rawNum).replace(/[^0-9]/g, '') || String(i + 1);
  return {
    num,
    term: fn.term_ja || fn.term || '',
    reading: fn.reading || '',
    defJa: fn.definition_ja || fn.meaning_ja || '',
    defEn: fn.definition_en || fn.meaning_en || ''
  };
}

function renderFootnotesBlock(footnotes) {
  if (!footnotes || !footnotes.length) return '';
  const items = footnotes.map(normalizeFootnote).sort((a, b) => Number(a.num) - Number(b.num));
  return `
    <div class="passage-footnotes">
      <div class="passage-footnotes-title"><i class="fa-solid fa-note-sticky"></i> 注 Notes</div>
      ${items.map(f => `
        <div class="passage-footnote" id="footnote-${f.num}">
          <span class="footnote-num">(注${f.num})</span>
          <span class="font-ja footnote-term">${f.term}${f.reading && f.reading !== f.term ? `【${f.reading}】` : ''}</span>
          ${f.defJa ? `<span class="font-ja footnote-def-ja">${f.defJa}</span>` : ''}
          ${f.defEn ? `<span class="footnote-def-en">${f.defEn}</span>` : ''}
        </div>`).join('')}
    </div>`;
}

export function scrollToFootnote(n) {
  const el = document.getElementById(`footnote-${n}`);
  if (!el) return;
  el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  el.classList.add('footnote-flash');
  setTimeout(() => el.classList.remove('footnote-flash'), 1600);
}

function renderPassageSentenceHTML(sentence, vocabMap, footnotes) {
  const isSecondPass = readerRuntime.isSecondPass;
  const showFurigana = !isSecondPass && readerRuntime.settings.showFurigana;
  const showAllTrans = !isSecondPass && readerRuntime.settings.showTranslations;
  const isIndividuallyExpanded = readerRuntime.expandedSentenceTrans.has(sentence.id);
  const showThisTrans = showAllTrans || isIndividuallyExpanded;

  let textJa = showFurigana && sentence.ruby_html ? sentence.ruby_html : sentence.text_ja;

  // 区切り Chunk Mode
  if (readerRuntime.settings.chunkMode) {
    textJa = insertChunkDividers(textJa);
  }

  // Footnote markers, then glossary terms (lesson vocab + full dictionary)
  textJa = wrapFootnoteMarkers(textJa);
  textJa = wrapGlossTerms(textJa, getGlossIndex(readerRuntime.lesson));

  return `
    <div class="passage-sentence-row${showThisTrans ? ' trans-active' : ''}" onclick="toggleSingleSentenceTrans('${sentence.id}')">
      <div class="sentence-ja-text">${textJa}</div>
      ${sentence.text_en ? `
        <div class="sentence-en-trans" style="display: ${showThisTrans ? 'block' : 'none'};">
          ${sentence.text_en}
        </div>
      ` : ''}
    </div>
  `;
}

function renderSkillsOrDrillFallback(lesson) {
  if (lesson.readingStrategy) {
    return `
      <div class="strategy-display-card">
        <h3><i class="fa-solid fa-chess"></i> ${lesson.readingStrategy.point_ja || '読解ストラテジー'}</h3>
        <p style="margin-top: 0.5rem; line-height: 1.8;">${lesson.readingStrategy.rule_ja || ''}</p>
        <p style="color: var(--text-dim); font-size: 0.9rem; margin-top: 0.35rem;">${lesson.readingStrategy.rule_en || ''}</p>
      </div>
    `;
  }
  return `<div class="empty-passage-state">No passage sentences found.</div>`;
}

export function goToQuestions() {
  stopTimer();
  readerRuntime.phase = 'answer';
  renderWorkspace();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// =======================================================
// FLOW PHASE 3: ANSWER (Bottom Sheet / Large 52px Options)
// =======================================================

function renderAnswerPhase(container) {
  const lesson = readerRuntime.lesson;
  const questions = readerRuntime.shuffledQuestions;
  const isSingle = questions.length === 1;

  container.innerHTML = `
    <div class="reading-workspace-shell">
      <div class="reading-nav-bar">
        <button class="btn btn-sm btn-ghost" onclick="returnToPassageReading()">
          <i class="fa-solid fa-book-open"></i> Read Passage Again
        </button>
        <span class="dokkai-flow-badge"><i class="fa-solid fa-pen"></i> Step 3: Answer</span>
      </div>

      <!-- Passage Peek Pane -->
      <div class="peek-passage-toggle-row">
        <button class="btn btn-sm btn-ghost" onclick="togglePassagePeek()">
          <i class="fa-solid fa-book"></i> ${readerRuntime.showPassageInAnswer ? 'Hide Passage' : 'Peek Passage'}
        </button>
        <button class="btn btn-sm btn-ghost" onclick="toggleOptionEnglish()">
          <i class="fa-solid fa-language"></i> EN Translations: ${readerRuntime.showOptionEn ? 'ON' : 'OFF'}
        </button>
      </div>

      <div id="answer-peek-pane" style="display: ${readerRuntime.showPassageInAnswer ? 'block' : 'none'}; margin-bottom: 1.5rem;" class="passage-view-card">
        <div class="font-ja" style="line-height: 1.85; max-height: 240px; overflow-y: auto; padding: 0.75rem;">
          ${(lesson.passage?.sentences || []).map(s => `<div>${s.text_ja}</div>`).join('')}
        </div>
      </div>

      <!-- Question Cards -->
      <div class="reading-questions-sheet">
        <div class="questions-sheet-header">
          <h3><i class="fa-solid fa-clipboard-question" style="color: var(--accent);"></i> Comprehension Questions (${questions.length})</h3>
          <span style="font-size: 0.85rem; color: var(--text-dim);">Reading Time: ${formatTime(readerRuntime.elapsedSeconds)}</span>
        </div>

        <div class="questions-list">
          ${questions.map((q, idx) => renderQuestionCardHTML(q, idx, isSingle)).join('')}
        </div>

        ${!isSingle ? `
          <div class="questions-sheet-actions">
            <button class="btn btn-primary btn-lg" id="btn-check-all-answers" onclick="submitQuizAnswers()">
              <i class="fa-solid fa-check"></i> Check Answers
            </button>
          </div>
        ` : ''}
      </div>
    </div>
  `;
}

function renderQuestionCardHTML(q, idx, isSingle) {
  const qId = q.id || `q_${idx + 1}`;
  const options = q.options || [];
  const optionsEn = q.options_en || [];
  const optionsRuby = q.options_ruby || [];
  const qType = getQuestionType(q);
  const selectedOpt = readerRuntime.selectedAnswers[qId];

  return `
    <div class="question-interactive-card" id="qcard-${qId}">
      <div class="question-meta-bar">
        <span class="q-number">Question ${idx + 1}</span>
        <span class="dokkai-genre-pill">${qType.label_ja} (${qType.label_en})</span>
      </div>

      <div class="question-prompt-text font-ja">
        ${glossifyBookText(bookJaText(q.question_ja || q.instruction_ja || '', q.questionText_ja_ruby || q.question_ja_ruby))}
      </div>
      ${readerRuntime.showOptionEn && q.question_en ? `
        <div class="question-prompt-sub">${q.question_en}</div>
      ` : ''}

      <div class="options-button-list">
        ${options.map((opt, optIdx) => {
          const optVal = optIdx + 1;
          const isSelected = selectedOpt === optVal;
          const optEn = optionsEn[optIdx] || '';

          return `
            <button type="button" 
                    class="dokkai-option-btn font-ja${isSelected ? ' selected' : ''}" 
                    id="opt-${qId}-${optVal}"
                    onclick="selectQuizOption('${qId}', ${optVal})">
              <span class="opt-num-badge">${optVal}</span>
              <div class="opt-text-wrap">
                <span class="opt-text-ja">${bookJaText(opt, optionsRuby[optIdx])}</span>
                ${readerRuntime.showOptionEn && optEn ? `<span class="opt-text-en">${optEn}</span>` : ''}
              </div>
            </button>
          `;
        }).join('')}
      </div>
    </div>
  `;
}

export function selectQuizOption(qId, optVal) {
  if (readerRuntime.submitted) return;
  readerRuntime.selectedAnswers[qId] = optVal;
  state.readingAnswers[qId] = optVal;

  const card = document.getElementById(`qcard-${qId}`);
  if (card) {
    card.querySelectorAll('.dokkai-option-btn').forEach(btn => btn.classList.remove('selected'));
    const target = document.getElementById(`opt-${qId}-${optVal}`);
    if (target) target.classList.add('selected');
  }

  // Single question locks immediately (doc 04 §4.3)
  if (readerRuntime.shuffledQuestions.length === 1) {
    submitQuizAnswers();
  }
}

// =======================================================
// FLOW PHASE 4: REVIEW & FOLLOW-UP (SRS & Layer A Re-read)
// =======================================================

export function submitQuizAnswers() {
  if (!readerRuntime.lesson || readerRuntime.submitted) return;
  readerRuntime.submitted = true;
  state.readingQuizSubmitted = true;

  const lesson = readerRuntime.lesson;
  const questions = readerRuntime.shuffledQuestions;

  // Safety net: a session with no passage or no questions is ungradable.
  // Never score it, never schedule a re-read, never claim a pass or mastery.
  if (questions.length === 0 || readerRuntime.charCount === 0) {
    readerRuntime.phase = 'review';
    readerRuntime.lastResults = {
      ungraded: true,
      correctCount: 0,
      totalQuestions: 0,
      accuracy: 0,
      cpm: 0,
      results: []
    };
    endGistReviewSession();
    renderWorkspace();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    return;
  }

  let correctCount = 0;
  const results = [];

  questions.forEach((q, idx) => {
    const qId = q.id || `q_${idx + 1}`;
    const userChoice = readerRuntime.selectedAnswers[qId];
    const evaluation = evaluateQuestionAnswer(q, userChoice);

    const srsKey = `R_Q:${qId}`;
    if (evaluation.isCorrect) {
      correctCount++;
      updateItemStats(srsKey, 3); // Good
    } else {
      updateItemStats(srsKey, 1); // Missed lapse
      toggleItemHard(srsKey);     // Flag for Weak Points
    }

    results.push({
      question: q,
      evaluation,
      userChoice,
      correctAnswer: evaluation.correctAnswer
    });
  });

  const accuracy = questions.length > 0 ? (correctCount / questions.length) : 0; // unreachable for empty sessions (guarded above); never pass vacuously
  const cpm = calculateCpm(readerRuntime.charCount, readerRuntime.elapsedSeconds);

  // Layer A Re-read Loop: RP:<lessonId> in state.stats
  updateLayerARereadPassage(lesson.id, {
    accuracy,
    cpm,
    elapsedSeconds: readerRuntime.elapsedSeconds,
    targetSeconds: readerRuntime.targetSeconds
  });

  readerRuntime.phase = 'review';
  readerRuntime.lastResults = {
    correctCount,
    totalQuestions: questions.length,
    accuracy,
    cpm,
    results
  };

  endGistReviewSession();
  renderWorkspace();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function updateLayerARereadPassage(lessonId, { accuracy, cpm, elapsedSeconds, targetSeconds }) {
  const rpKey = `RP:${lessonId}`;
  const existing = state.stats?.[rpKey];
  const now = Date.now();

  const isPass = isSecondPassPassed(accuracy, elapsedSeconds, targetSeconds);
  const currentStep = existing?.step !== undefined ? existing.step : 0;
  const reads = (existing?.reads || 0);

  const schedule = calculateRereadSchedule({
    reads,
    currentStep,
    passed: isPass,
    now,
    snapFn: snapToNextDueSlot
  });

  const bestAcc = Math.max(existing?.bestAcc || 0, accuracy);
  const bestCpm = Math.max(existing?.bestCpm || 0, cpm);

  state.stats[rpKey] = {
    ...existing,
    reads: reads + 1,
    bestAcc,
    lastAcc: accuracy,
    bestCpm,
    lastCpm: cpm,
    nextDue: schedule.nextDue,
    interval: schedule.intervalDays,
    lastSeen: now,
    weight: existing?.weight || 1.0,
    step: schedule.nextStep,
    mastered: schedule.mastered || Boolean(existing?.mastered)
  };

  saveStats();
  updateSidebarStats();
}

function renderReviewPhase(container) {
  const lesson = readerRuntime.lesson;
  const resultsData = readerRuntime.lastResults;
  if (!resultsData) return;

  if (resultsData.ungraded) {
    const missing = readerRuntime.charCount === 0 ? 'timed passage' : 'comprehension questions';
    container.innerHTML = `
    <div class="reading-workspace-shell">
      <div class="reading-nav-bar">
        <button class="btn btn-sm btn-ghost" onclick="closeReadingWorkspace()">
          <i class="fa-solid fa-arrow-left"></i> Return to All Passages
        </button>
        <span class="dokkai-flow-badge"><i class="fa-solid fa-flag-checkered"></i> Step 4: Review</span>
      </div>
      <div class="reading-result-summary-card">
        <h2 style="margin-bottom: 0.5rem;">Nothing to grade here</h2>
        <p style="color: var(--text-dim); line-height: 1.6;">
          <span class="font-ja">${lesson.title_ja || lesson.title || 'This lesson'}</span> has no ${missing},
          so no score, pass or re-read step was recorded.
        </p>
        <div class="review-bottom-actions">
          <button class="btn btn-primary" onclick="openReadingLesson('${lesson.id}', { startPhase: 'book' })">
            <i class="fa-solid fa-book-open"></i> Open in the Book
          </button>
          <button class="btn btn-ghost" onclick="closeReadingWorkspace()">
            <i class="fa-solid fa-list-check"></i> Back to Passages List
          </button>
        </div>
      </div>
    </div>`;
    return;
  }

  const { correctCount, totalQuestions, accuracy, cpm, results } = resultsData;
  const targetCpm = DEFAULT_READING_CPM;
  const isSecondPass = readerRuntime.isSecondPass;
  const passedCriteria = isSecondPassPassed(accuracy, readerRuntime.elapsedSeconds, readerRuntime.targetSeconds);
  const rpKey = `RP:${lesson.id}`;
  const rp = state.stats?.[rpKey];

  container.innerHTML = `
    <div class="reading-workspace-shell">
      <div class="reading-nav-bar">
        <button class="btn btn-sm btn-ghost" onclick="closeReadingWorkspace()">
          <i class="fa-solid fa-arrow-left"></i> Return to All Passages
        </button>
        <span class="dokkai-flow-badge"><i class="fa-solid fa-flag-checkered"></i> Step 4: Review</span>
      </div>

      <!-- Result Summary Card -->
      <div class="reading-result-summary-card">
        <div class="result-score-banner">
          <div class="score-circle ${accuracy >= 0.8 ? 'pass' : 'fail'}">
            <span class="score-num">${correctCount}/${totalQuestions}</span>
            <span class="score-percent">${Math.round(accuracy * 100)}%</span>
          </div>
          <div>
            <h2>${accuracy >= 0.8 ? '🎉 Great Job!' : '📚 Keep Practicing!'}</h2>
            <p style="color: var(--text-dim); margin-top: 0.25rem;">
              Read ${readerRuntime.charCount} characters in ${formatTime(readerRuntime.elapsedSeconds)} 
              (Target: ${formatTime(readerRuntime.targetSeconds)}).
            </p>
          </div>
        </div>

        <div class="reading-stat-grid" style="margin-top: 1.5rem;">
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-gauge-high"></i> Reading Pace</span>
            <span class="stat-val ${cpm >= targetCpm ? 'cpm-good' : ''}">${cpm} CPM</span>
            <small style="color: var(--text-dim);">Target: ${targetCpm} CPM</small>
          </div>
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-stopwatch"></i> Elapsed Time</span>
            <span class="stat-val">${formatTime(readerRuntime.elapsedSeconds)}</span>
            <small style="color: var(--text-dim);">${readerRuntime.elapsedSeconds <= readerRuntime.targetSeconds ? 'Under target' : 'Over target'}</small>
          </div>
          <div class="reading-stat-box">
            <span class="stat-label"><i class="fa-solid fa-rotate"></i> Layer A Re-read</span>
            <span class="stat-val">${rp?.mastered ? '👑 Mastered' : `+${rp?.interval || 3}d Due`}</span>
            <small style="color: var(--text-dim);">Pass ${rp?.reads || 1}</small>
          </div>
        </div>

        ${isSecondPass ? `
          <div class="second-pass-review-badge ${passedCriteria ? 'passed' : 'failed'}">
            <i class="fa-solid ${passedCriteria ? 'fa-circle-check' : 'fa-circle-xmark'}"></i>
            <div>
              <strong>Second Pass Result: ${passedCriteria ? 'PASSED' : 'NEEDS PRACTICE'}</strong>
              <p>Criteria: &ge; 80% accuracy (${Math.round(accuracy * 100)}%) and &le; 1.3&times; target time (${formatTime(readerRuntime.elapsedSeconds)} / max ${formatTime(readerRuntime.targetSeconds * 1.3)}).</p>
            </div>
          </div>
        ` : ''}

        <div class="srs-status-banner font-ja" id="reading-srs-status-line">
          <i class="fa-solid fa-database"></i> 
          ${results.filter(r => !r.evaluation.isCorrect).length > 0 
            ? `${results.filter(r => !r.evaluation.isCorrect).length} missed question(s) saved to Weak Points review.` 
            : 'All comprehension questions answered correctly!'}
        </div>
      </div>

      <!-- Question Feedback Cards -->
      <div class="review-questions-list">
        ${results.map((r, idx) => renderReviewQuestionHTML(r, idx)).join('')}
      </div>

      <!-- Commentary & Test Advice Cards -->
      ${lesson.commentary ? `
        <div class="commentary-card font-ja">
          <h3><i class="fa-solid fa-diagram-project" style="color: var(--cyan);"></i> 本文の解説 (Commentary)</h3>
          <p style="margin-top: 0.6rem; line-height: 1.8;">${lesson.commentary.summary_ja || lesson.commentary.logicFlow || ''}</p>
          ${lesson.commentary.summary_en ? `<p style="font-size: 0.85rem; color: var(--text-dim); margin-top: 0.35rem;">${lesson.commentary.summary_en}</p>` : ''}
        </div>
      ` : ''}

      ${lesson.testAdvice ? `
        <div class="test-advice-card font-ja">
          <h3><i class="fa-solid fa-compass" style="color: var(--amber);"></i> 試験のコツ (Test Advice)</h3>
          <p style="margin-top: 0.6rem; line-height: 1.8;">${lesson.testAdvice.advice_ja || lesson.testAdvice.traps || ''}</p>
          ${lesson.testAdvice.advice_en ? `<p style="font-size: 0.85rem; color: var(--text-dim); margin-top: 0.35rem;">${lesson.testAdvice.advice_en}</p>` : ''}
        </div>
      ` : ''}

      <div class="review-bottom-actions">
        ${(readerRuntime.practiceIndex ?? -1) >= 0 && readerRuntime.practiceIndex < (readerRuntime.practiceQueue || []).length - 1 ? `
        <button class="btn btn-primary" onclick="practiceNextReadingLesson()">
          <i class="fa-solid fa-forward-step"></i> Next Lesson (${readerRuntime.practiceIndex + 2}/${readerRuntime.practiceQueue.length})
        </button>` : ''}
        <button class="btn btn-primary" onclick="closeReadingWorkspace()">
          <i class="fa-solid fa-list-check"></i> Back to Passages List
        </button>
        <button class="btn btn-ghost" onclick="resetReadingLesson()">
          <i class="fa-solid fa-rotate-left"></i> Re-read Passage Now
        </button>
      </div>
    </div>
  `;
}

function renderReviewQuestionHTML(res, idx) {
  const { question: q, evaluation, userChoice, correctAnswer } = res;
  const isCorrect = evaluation.isCorrect;
  const qType = getQuestionType(q);
  const options = q.options || [];
  const optionsRuby = q.options_ruby || [];

  return `
    <div class="review-question-card ${isCorrect ? 'card-correct' : 'card-incorrect'}">
      <div class="review-q-header">
        <span class="q-verdict ${isCorrect ? 'verdict-correct' : 'verdict-incorrect'}">
          <i class="fa-solid ${isCorrect ? 'fa-check' : 'fa-xmark'}"></i> ${isCorrect ? 'Correct' : 'Incorrect'}
        </span>
        <span class="dokkai-genre-pill">${qType.label_ja}</span>
      </div>

      <div class="question-prompt-text font-ja" style="margin-top: 0.5rem;">
        ${idx + 1}. ${q.question_ja || ''}
      </div>
      ${q.question_en ? `<div class="question-prompt-sub">${q.question_en}</div>` : ''}

      <div class="review-options-display">
        ${options.map((opt, optIdx) => {
          const optVal = optIdx + 1;
          const isThisCorrect = optVal === correctAnswer;
          const isUserPick = optVal === userChoice;
          let optClass = 'opt-neutral';

          if (isThisCorrect) optClass = 'opt-is-correct';
          else if (isUserPick) optClass = 'opt-is-wrong';

          return `
            <div class="review-option-row ${optClass} font-ja">
              <span class="badge">${optVal}</span>
              <span>${glossifyBookText(bookJaText(opt, optionsRuby[optIdx]))}</span>
              ${isThisCorrect ? '<span class="status-tag correct"><i class="fa-solid fa-check"></i> Answer</span>' : ''}
              ${isUserPick && !isThisCorrect ? '<span class="status-tag incorrect"><i class="fa-solid fa-xmark"></i> Your pick</span>' : ''}
            </div>
          `;
        }).join('')}
      </div>

      <div class="quiz-explanation-box">
        <strong style="color: var(--green);"><i class="fa-solid fa-circle-check"></i> 正解: Option ${correctAnswer}</strong>
        <p class="font-ja" style="margin-top: 0.4rem; line-height: 1.7;">${glossifyBookText(bookJaText(q.explanation_ja || '', q.explanation_ja_ruby))}</p>
        ${q.explanation_en ? `
          <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.35rem;">${q.explanation_en}</p>
        ` : ''}
      </div>
    </div>
  `;
}

export function resetReadingLesson() {
  if (readerRuntime.lesson) {
    openReadingLesson(readerRuntime.lesson.id);
  }
}

// =======================================================
// TOOLBAR & INTERACTIVE CONTROLLERS
// =======================================================

export function adjustFontScale(delta) {
  const current = readerRuntime.settings.fontScale;
  const next = Math.max(0.8, Math.min(1.5, Math.round((current + delta) * 10) / 10));
  readerRuntime.settings.fontScale = next;
  saveReaderSettings(readerRuntime.settings);

  const pane = document.getElementById('passage-content-area');
  if (pane) pane.style.fontSize = `${1.2 * next}rem`;

  const label = document.querySelector('.toolbar-btn-group .t-label');
  if (label) label.textContent = `${Math.round(next * 100)}%`;
}

export function togglePassageFurigana() {
  if (readerRuntime.isSecondPass) return;
  readerRuntime.settings.showFurigana = !readerRuntime.settings.showFurigana;
  state.showFurigana = readerRuntime.settings.showFurigana;
  saveReaderSettings(readerRuntime.settings);
  renderWorkspace();
}

export function togglePassageTranslations() {
  if (readerRuntime.isSecondPass) return;
  readerRuntime.settings.showTranslations = !readerRuntime.settings.showTranslations;
  state.showSentenceTranslations = readerRuntime.settings.showTranslations;
  saveReaderSettings(readerRuntime.settings);
  renderWorkspace();
}

export function toggleSentenceTranslations() {
  togglePassageTranslations();
}

export function togglePassageChunks() {
  readerRuntime.settings.chunkMode = !readerRuntime.settings.chunkMode;
  saveReaderSettings(readerRuntime.settings);
  renderWorkspace();
}

export function toggleSingleSentenceTrans(sId) {
  if (readerRuntime.expandedSentenceTrans.has(sId)) {
    readerRuntime.expandedSentenceTrans.delete(sId);
  } else {
    readerRuntime.expandedSentenceTrans.add(sId);
  }
  renderWorkspace();
}

export function togglePassagePeek() {
  readerRuntime.showPassageInAnswer = !readerRuntime.showPassageInAnswer;
  const pane = document.getElementById('answer-peek-pane');
  if (pane) {
    pane.style.display = readerRuntime.showPassageInAnswer ? 'block' : 'none';
  }
}

export function toggleOptionEnglish() {
  readerRuntime.showOptionEn = !readerRuntime.showOptionEn;
  renderWorkspace();
}

export function returnToPassageReading() {
  readerRuntime.phase = 'read';
  renderWorkspace();
}

// =======================================================
// WORD GLOSS MINI-SHEET & VOCABULARY ENGINE INTEGRATION (§8)
// =======================================================

export function showWordGloss(term, anchorEl) {
  const lesson = readerRuntime.lesson;
  if (!lesson) return;

  let vocab = (lesson.vocabulary || []).find(v => v.term === term);
  if (!vocab) vocab = getGlossIndex(lesson).map.get(term);
  if (!vocab) return;

  readerRuntime.activeGlossWord = vocab;
  const container = document.getElementById('word-gloss-sheet-container');
  if (!container) return;

  const kanjiParts = vocabularyKanjiMeanings(vocab.term);

  container.innerHTML = `
    <div class="word-gloss-popup" role="dialog" aria-label="Word meaning">
      <div class="gloss-sheet-header">
        <div>
          <span class="font-ja gloss-term-title">${vocab.term}</span>
          ${vocab.reading ? `<span class="gloss-reading">【${vocab.reading}】</span>` : ''}
          ${vocab.type ? `<span class="badge" style="background:var(--surface);">${vocab.type}</span>` : ''}
        </div>
        <button class="btn btn-xs btn-ghost" onclick="closeWordGloss()"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="gloss-meaning-text">${vocab.meaning || ''}</div>
      ${kanjiParts.length ? `
        <div class="vocab-kanji-breakdown gloss-kanji-breakdown">
          <div class="vocab-kanji-heading">Kanji meanings</div>
          <div class="vocab-kanji-chips">
            ${kanjiParts.map(({ kanji, meanings }) => `
              <span class="vocab-kanji-chip" title="${kanji}: ${meanings.join(', ')}"><b class="font-ja">${kanji}</b> ${meanings.slice(0, 2).join(' / ')}</span>`).join('')}
          </div>
        </div>` : ''}
      <div class="gloss-actions">
        <button class="btn btn-sm btn-primary" onclick="addActiveWordToMyWords()">
          <i class="fa-solid fa-plus"></i> Add to My Words
        </button>
      </div>
    </div>
  `;

  // Anchor the popup beside the tapped word without moving the page.
  // Mounted on <body>: an ancestor with transform/filter would otherwise trap
  // position:fixed and pin the sheet to the document bottom.
  const popup = container.querySelector('.word-gloss-popup');
  if (popup) document.body.appendChild(popup);
  if (popup && anchorEl && anchorEl.getBoundingClientRect) {
    const rect = anchorEl.getBoundingClientRect();
    popup.style.visibility = 'hidden';
    popup.style.left = '0px';
    popup.style.top = '0px';
    const pw = popup.offsetWidth;
    const ph = popup.offsetHeight;
    const margin = 8;
    let left = Math.min(Math.max(rect.left, margin), Math.max(margin, window.innerWidth - pw - margin));
    let top = rect.bottom + 6;
    if (top + ph > window.innerHeight - margin) {
      top = rect.top - ph - 6;
      if (top < margin) top = Math.max(margin, Math.min(window.innerHeight - ph - margin, rect.bottom + 6));
    }
    popup.style.left = `${Math.round(left)}px`;
    popup.style.top = `${Math.round(top)}px`;
    popup.style.visibility = 'visible';
  }

  // Dismiss on outside tap, scroll, or Escape; keep the reading position.
  const dismiss = (ev) => {
    if (popup && ev && ev.target && popup.contains(ev.target)) return;
    closeWordGloss();
  };
  readerRuntime.glossDismissHandlers = {
    pointerdown: (ev) => dismiss(ev),
    scroll: () => closeWordGloss(),
    keydown: (ev) => { if (ev.key === 'Escape') closeWordGloss(); }
  };
  setTimeout(() => {
    if (!readerRuntime.glossDismissHandlers) return;
    document.addEventListener('pointerdown', readerRuntime.glossDismissHandlers.pointerdown, true);
    window.addEventListener('scroll', readerRuntime.glossDismissHandlers.scroll, true);
    document.addEventListener('keydown', readerRuntime.glossDismissHandlers.keydown, true);
  }, 0);
}

export function closeWordGloss() {
  readerRuntime.activeGlossWord = null;
  if (readerRuntime.glossDismissHandlers) {
    document.removeEventListener('pointerdown', readerRuntime.glossDismissHandlers.pointerdown, true);
    window.removeEventListener('scroll', readerRuntime.glossDismissHandlers.scroll, true);
    document.removeEventListener('keydown', readerRuntime.glossDismissHandlers.keydown, true);
    readerRuntime.glossDismissHandlers = null;
  }
  document.querySelectorAll('body > .word-gloss-popup').forEach(el => el.remove());
  const container = document.getElementById('word-gloss-sheet-container');
  if (container) container.innerHTML = '';
}

export function addWordFromPreview(term, reading, meaning, btnEl) {
  const res = addWordToMyWords({ term, reading, meaning });
  if (btnEl) {
    if (res.success) {
      btnEl.textContent = 'Added ✓';
      btnEl.disabled = true;
      btnEl.style.color = 'var(--green)';
    } else if (res.capped) {
      btnEl.textContent = 'Capped';
      btnEl.disabled = true;
    }
  }
}

export function addActiveWordToMyWords() {
  if (readerRuntime.activeGlossWord) {
    const res = addWordToMyWords(readerRuntime.activeGlossWord);
    closeWordGloss();
  }
}

export function addAllPassageWordsToMyWords() {
  const lesson = readerRuntime.lesson;
  if (!lesson || !lesson.vocabulary) return;

  let added = 0;
  for (const v of lesson.vocabulary) {
    const res = addWordToMyWords(v);
    if (res.success) added++;
    if (res.capped) break;
  }
  renderWorkspace();
}

/**
 * Adds a passage word into the vocabulary / SRS engine (doc 04 §8, RD-10).
 * Respects daily cap of 8 words.
 * @param {Object} wordObj
 * @returns {Object} { success, capped, key, message }
 */
export function addWordToMyWords(wordObj) {
  if (!wordObj || !wordObj.term) return { success: false };

  const term = wordObj.term.trim();
  const today = new Date().toISOString().slice(0, 10);
  const capKey = 'n3_reading_words_added_today';

  let addedToday = { date: today, count: 0, terms: [] };
  try {
    const raw = localStorage.getItem(capKey);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed.date === today) {
        addedToday = parsed;
      }
    }
  } catch {}

  const DAILY_CAP = 8;
  if (addedToday.count >= DAILY_CAP) {
    savePendingWord(wordObj);
    return {
      success: false,
      capped: true,
      message: `Daily limit of ${DAILY_CAP} words reached. "${term}" saved for tomorrow.`
    };
  }

  // 1. Matches vocabDB -> V:<id>
  // 2. In state.idx.words -> KWR:<term> and KWM:<term>
  // 3. Custom card -> RW:<term>
  let targetKey = null;
  let targetType = 'custom';

  let matchedVocab = null;
  if (state.vocabDB) {
    for (const chId in state.vocabDB) {
      const words = state.vocabDB[chId] || [];
      const found = words.find(w => w.term_ja === term || w.term === term);
      if (found) {
        matchedVocab = found;
        break;
      }
    }
  }

  if (matchedVocab) {
    targetKey = `V:${matchedVocab.id}`;
    targetType = 'vocab';
    if (!state.stats[targetKey]) {
      state.stats[targetKey] = {
        reps: 0,
        interval: 0,
        easeFactor: 2.5,
        learnState: 'learning',
        nextDue: snapToNextDueSlot(Date.now()),
        lastSeen: Date.now()
      };
    }
  } else if (state.idx?.words?.[term]) {
    targetKey = `KWR:${term}`;
    targetType = 'kanji_word';
    if (!state.stats[targetKey]) {
      state.stats[targetKey] = {
        reps: 0,
        interval: 0,
        easeFactor: 2.5,
        learnState: 'learning',
        nextDue: snapToNextDueSlot(Date.now()),
        lastSeen: Date.now()
      };
    }
    const kwmKey = `KWM:${term}`;
    if (!state.stats[kwmKey]) {
      state.stats[kwmKey] = {
        reps: 0,
        interval: 0,
        easeFactor: 2.5,
        learnState: 'learning',
        nextDue: snapToNextDueSlot(Date.now()),
        lastSeen: Date.now()
      };
    }
  } else {
    targetKey = `RW:${term}`;
    targetType = 'reading_word';
    if (!state.stats[targetKey]) {
      state.stats[targetKey] = {
        reps: 0,
        interval: 0,
        easeFactor: 2.5,
        learnState: 'learning',
        nextDue: snapToNextDueSlot(Date.now()),
        lastSeen: Date.now(),
        reading: wordObj.reading || '',
        meaning: wordObj.meaning || '',
        term: term
      };
    }
  }

  addedToday.count += 1;
  addedToday.terms.push(term);
  try {
    localStorage.setItem(capKey, JSON.stringify(addedToday));
  } catch {}

  saveStats();
  updateSidebarStats();

  return {
    success: true,
    capped: false,
    key: targetKey,
    type: targetType,
    message: `"${term}" added to your study cards!`
  };
}

function savePendingWord(wordObj) {
  try {
    const raw = localStorage.getItem('n3_reading_pending_words') || '[]';
    const list = JSON.parse(raw);
    if (!list.some(w => w.term === wordObj.term)) {
      list.push(wordObj);
      localStorage.setItem('n3_reading_pending_words', JSON.stringify(list));
    }
  } catch {}
}

export function addMissedQuestionsToSRS() {
  // RD-5: alert() is eliminated
  const btn = document.getElementById('btn-add-missed-srs');
  if (btn) {
    btn.innerHTML = '<i class="fa-solid fa-check"></i> Added to Review Desk';
    btn.disabled = true;
  }
}

// =======================================================
// TIMER ENGINE
// =======================================================

function startTimer() {
  stopTimer();
  readerRuntime.readStartTime = Date.now() - (readerRuntime.elapsedSeconds * 1000);
  readerRuntime.timerInterval = setInterval(() => {
    if (readerRuntime.phase !== 'read') {
      stopTimer();
      return;
    }
    readerRuntime.elapsedSeconds = Math.max(1, Math.round((Date.now() - readerRuntime.readStartTime) / 1000));
    updateTimerPill();
  }, 1000);
}

function stopTimer() {
  if (readerRuntime.timerInterval) {
    clearInterval(readerRuntime.timerInterval);
    readerRuntime.timerInterval = null;
  }
}

function updateTimerPill() {
  const pill = document.getElementById('reader-live-timer');
  if (!pill) return;

  const elapsed = readerRuntime.elapsedSeconds;
  const target = readerRuntime.targetSeconds;
  pill.innerHTML = `<i class="fa-solid fa-stopwatch"></i> ${formatTime(elapsed)}${target > 0 ? ` / ~${formatTime(target)}` : ''}`;

  if (target > 0 && elapsed > (1.3 * target)) {
    pill.classList.add('timer-amber');
  } else {
    pill.classList.remove('timer-amber');
  }
}

function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// =======================================================
// COMPONENT STYLES INJECTION
// =======================================================

function ensureReaderStyles() {
  if (document.getElementById('dokkai-reader-injected-styles')) return;
  const style = document.createElement('style');
  style.id = 'dokkai-reader-injected-styles';
  style.textContent = `
    /* Focused reading: hub chrome and global dock/sync pill stay hidden
       while a lesson workspace is open; restored on close. */
    #view-reading.reading-focus > .view-header,
    #view-reading.reading-focus > #pb-reading,
    #view-reading.reading-focus > .pillar-sub-tabs {
      display: none !important;
    }
    body.reading-focus #mobile-dock,
    body.reading-focus #n3sync-mobile {
      display: none !important;
    }
    .reading-workspace-shell {
      max-width: 900px;
      margin: 0 auto;
      padding-bottom: 5rem;
    }
    .reading-nav-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.25rem;
    }
    .dokkai-flow-badge {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--accent);
      background: var(--surface);
      padding: 0.3rem 0.75rem;
      border-radius: 999px;
      border: 1px solid var(--border);
    }
    .reading-preview-card, .passage-view-card, .reading-result-summary-card {
      background: var(--bg2);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 1.5rem;
    }
    .reading-title-large {
      font-size: 1.6rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.35;
    }
    .reading-subtitle {
      color: var(--text-dim);
      font-size: 0.95rem;
      margin-top: 0.25rem;
    }
    .second-pass-alert {
      display: flex;
      gap: 1rem;
      align-items: center;
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.35);
      border-radius: 12px;
      padding: 1rem;
      margin: 1.25rem 0;
      color: #c4b5fd;
    }
    .reading-stat-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 0.75rem;
      margin: 1.5rem 0;
    }
    .reading-stat-box {
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }
    .reading-stat-box .stat-label {
      font-size: 0.75rem;
      color: var(--text-dim);
    }
    .reading-stat-box .stat-val {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
    }
    .pre-reading-box {
      background: var(--bg3);
      border-left: 3px solid var(--amber);
      border-radius: 0 10px 10px 0;
      padding: 1rem 1.25rem;
      margin: 1.5rem 0;
    }
    .pre-reading-header {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--amber);
      margin-bottom: 0.4rem;
    }
    .pre-reading-text {
      font-size: 1.05rem;
      line-height: 1.6;
      color: #fff;
    }
    .pre-reading-sub {
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-top: 0.25rem;
    }
    .preview-vocab-section {
      margin: 1.5rem 0;
    }
    .preview-vocab-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text);
    }
    .preview-vocab-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .vocab-preview-chip {
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.45rem 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.85rem;
    }
    .vocab-chip-term {
      font-weight: 700;
      color: #fff;
    }
    .vocab-chip-reading {
      color: var(--text-dim);
      font-size: 0.75rem;
    }
    .vocab-chip-meaning {
      color: var(--text-muted);
      font-size: 0.8rem;
    }
    .preview-action-row {
      display: flex;
      gap: 1rem;
      margin-top: 2rem;
      flex-wrap: wrap;
    }
    .passage-scroll-pane {
      line-height: 1.9;
      margin-top: 1rem;
    }
    .passage-sentence-row {
      padding: 0.6rem 0.85rem;
      border-radius: 8px;
      transition: background 0.12s;
      cursor: pointer;
      border-left: 2px solid transparent;
    }
    .passage-sentence-row:hover {
      background: var(--surface);
      border-left-color: var(--accent);
    }
    .sentence-en-trans {
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-top: 0.35rem;
      line-height: 1.45;
    }
    .footnote-marker {
      color: var(--cyan);
      cursor: pointer;
    }
    .passage-footnotes {
      margin-top: 0.9rem;
      border-top: 1px dashed var(--border);
      padding: 0.6rem 0.75rem 0.25rem;
    }
    .passage-footnotes-title {
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-bottom: 0.4rem;
    }
    .passage-footnote {
      font-size: 0.85rem;
      line-height: 1.65;
      padding: 0.15rem 0.35rem;
      border-radius: 6px;
      margin-bottom: 0.15rem;
      transition: background 0.3s ease;
    }
    .passage-footnote .footnote-num {
      color: var(--cyan);
      font-weight: 700;
      margin-right: 0.3rem;
    }
    .passage-footnote .footnote-term {
      font-weight: 600;
      margin-right: 0.35rem;
    }
    .passage-footnote .footnote-def-ja {
      color: var(--text-muted);
      margin-right: 0.35rem;
    }
    .passage-footnote .footnote-def-en {
      color: var(--text-dim);
    }
    .passage-footnote.footnote-flash {
      background: var(--surface);
      outline: 1px solid var(--cyan);
    }
    .book-drill-items {
      margin-top: 0.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }
    .book-drill-item summary {
      cursor: pointer;
    }
    .book-drill-item .drill-item-term {
      font-weight: 600;
    }
    .book-drill-option {
      display: flex;
      gap: 0.5rem;
      align-items: baseline;
      font-size: 0.9rem;
    }
    .book-drill-option .drill-option-key {
      font-weight: 700;
      color: var(--cyan);
      min-width: 1rem;
    }
    .gloss-kanji-breakdown {
      margin-top: 0.6rem;
    }
    .gloss-term {
      border-bottom: 1px dashed var(--accent);
      color: #fff;
      cursor: pointer;
    }
    .gloss-term:hover {
      color: var(--accent);
    }
    .reading-sticky-toolbar {
      position: sticky;
      bottom: 1rem;
      background: rgba(18, 21, 30, 0.95);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-strong);
      border-radius: 16px;
      padding: 0.75rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
      z-index: 100;
      margin-top: 2rem;
      flex-wrap: wrap;
      gap: 0.75rem;
    }
    .toolbar-pill-group {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      flex-wrap: wrap;
    }
    .toolbar-btn-group {
      display: flex;
      align-items: center;
      background: var(--bg3);
      border-radius: 8px;
      padding: 0.15rem;
    }
    .t-btn {
      background: transparent;
      border: none;
      color: var(--text);
      font-size: 0.85rem;
      padding: 0.25rem 0.5rem;
      cursor: pointer;
      font-weight: 700;
    }
    .t-label {
      font-size: 0.75rem;
      color: var(--text-dim);
      padding: 0 0.25rem;
    }
    .t-btn-toggle {
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.65rem;
      cursor: pointer;
      transition: all 0.15s;
    }
    .t-btn-toggle.active {
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }
    .t-btn-toggle.disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }
    .toolbar-timer-group {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .timer-pill {
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.8rem;
      border-radius: 8px;
      background: var(--bg3);
      border: 1px solid var(--border);
      color: var(--text);
    }
    .timer-pill.timer-amber {
      background: rgba(245, 158, 11, 0.2);
      border-color: #f59e0b;
      color: #fbbf24;
    }
    .dokkai-option-btn {
      width: 100%;
      min-height: 52px;
      display: flex;
      align-items: center;
      gap: 0.85rem;
      padding: 0.85rem 1.25rem;
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 12px;
      color: var(--text);
      cursor: pointer;
      text-align: left;
      font-size: 1.02rem;
      line-height: 1.45;
      transition: all 0.15s ease;
      margin-bottom: 0.6rem;
    }
    .dokkai-option-btn:hover {
      border-color: var(--accent);
      background: var(--surface);
    }
    .dokkai-option-btn.selected {
      border-color: var(--accent);
      background: rgba(99, 102, 241, 0.18);
      color: #fff;
    }
    .opt-num-badge {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--surface);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
    }
    .opt-text-wrap {
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
    }
    .opt-text-en {
      font-size: 0.8rem;
      color: var(--text-dim);
    }
    .question-interactive-card, .review-question-card {
      background: var(--bg2);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }
    .question-prompt-text {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.55;
      margin: 0.6rem 0;
    }
    .question-prompt-sub {
      font-size: 0.88rem;
      color: var(--text-dim);
      margin-bottom: 1rem;
    }
    .dokkai-status-badge {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
    }
    .dokkai-status-badge.unread { background: var(--surface); color: var(--text-dim); }
    .dokkai-status-badge.read { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }
    .dokkai-status-badge.due { background: rgba(239, 68, 68, 0.15); color: #f87171; }
    .dokkai-status-badge.mastered { background: rgba(16, 185, 129, 0.15); color: #34d399; }
    .dokkai-due-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #ef4444;
      display: inline-block;
    }
    .dokkai-card-stats-pill {
      display: flex;
      gap: 0.75rem;
      font-size: 0.78rem;
      color: var(--text-muted);
      background: var(--bg3);
      padding: 0.35rem 0.6rem;
      border-radius: 6px;
      width: fit-content;
    }
    .word-gloss-popup {
      position: fixed;
      z-index: 9999;
      width: max-content;
      max-width: min(340px, calc(100vw - 1rem));
      background: #181d29;
      border: 1px solid var(--accent);
      border-radius: 12px;
      padding: 0.8rem 0.9rem;
      box-shadow: 0 12px 40px rgba(0,0,0,0.6);
      font-size: 0.9rem;
    }
    .word-gloss-popup .gloss-sheet-header {
      gap: 0.75rem;
    }
    .word-gloss-popup .gloss-actions {
      margin-top: 0.6rem;
    }
    .word-gloss-modal-sheet {
      position: fixed;
      bottom: 1rem;
      left: 50%;
      transform: translateX(-50%);
      width: min(520px, calc(100vw - 2rem));
      background: #181d29;
      border: 1px solid var(--accent);
      border-radius: 14px;
      padding: 1.25rem;
      box-shadow: 0 12px 40px rgba(0,0,0,0.6);
      z-index: 200;
    }
    .gloss-sheet-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.5rem;
    }
    .gloss-term-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: #fff;
    }
    .gloss-reading {
      font-size: 0.95rem;
      color: var(--accent);
      margin-left: 0.4rem;
    }
    .gloss-meaning-text {
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.45;
      margin-bottom: 1rem;
    }
    .second-pass-review-badge {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      padding: 0.85rem 1.1rem;
      border-radius: 10px;
      margin: 1.25rem 0;
    }
    .second-pass-review-badge.passed {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      color: #34d399;
    }
    .second-pass-review-badge.failed {
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid #ef4444;
      color: #f87171;
    }
    .srs-status-banner {
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-size: 0.88rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-top: 1rem;
    }
    .score-circle {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      flex-shrink: 0;
    }
    .score-circle.pass {
      background: rgba(16, 185, 129, 0.2);
      border: 2px solid #10b981;
      color: #34d399;
    }
    .score-circle.fail {
      background: rgba(239, 68, 68, 0.2);
      border: 2px solid #ef4444;
      color: #f87171;
    }
    .score-num { font-size: 1.2rem; }
    .score-percent { font-size: 0.75rem; opacity: 0.85; }
    .result-score-banner {
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }
    .review-option-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.4rem;
      font-size: 0.95rem;
    }
    .review-option-row.opt-neutral { background: var(--bg3); color: var(--text); }
    .review-option-row.opt-is-correct { background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #fff; }
    .review-option-row.opt-is-wrong { background: rgba(239, 68, 68, 0.15); border: 1px solid #ef4444; color: #fff; }
    .status-tag {
      margin-left: auto;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }
    .status-tag.correct { background: var(--green); color: #fff; }
    .status-tag.incorrect { background: var(--red); color: #fff; }
    .commentary-card, .test-advice-card {
      background: var(--bg2);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      margin-top: 1.25rem;
    }
    .review-bottom-actions {
      display: flex;
      gap: 1rem;
      margin-top: 2rem;
      flex-wrap: wrap;
    }
  `;
  document.head.appendChild(style);
}

// =======================================================
// GLOBAL WINDOW BINDINGS (Preserve All Existing + New)
// =======================================================

if (typeof window !== 'undefined') {
  window.openReadingLesson = openReadingLesson;
  window.closeReadingWorkspace = closeReadingWorkspace;
  window.setReadingCategory = setReadingCategory;
  window.selectQuizOption = selectQuizOption;
  window.submitQuizAnswers = submitQuizAnswers;
  window.addMissedQuestionsToSRS = addMissedQuestionsToSRS;
  window.toggleSentenceTranslations = toggleSentenceTranslations;
  window.renderReadingView = renderReadingView;

  // New interactive handlers
  window.startReadingPassage = startReadingPassage;
  window.goToQuestions = goToQuestions;
  window.skipToQuestions = skipToQuestions;
  window.togglePassageFurigana = togglePassageFurigana;
  window.togglePassageTranslations = togglePassageTranslations;
  window.togglePassageChunks = togglePassageChunks;
  window.toggleStrategyFurigana = toggleStrategyFurigana;
  window.adjustFontScale = adjustFontScale;
  window.toggleSingleSentenceTrans = toggleSingleSentenceTrans;
  window.showWordGloss = showWordGloss;
  window.scrollToFootnote = scrollToFootnote;
  window.closeWordGloss = closeWordGloss;
  window.addActiveWordToMyWords = addActiveWordToMyWords;
  window.addWordFromPreview = addWordFromPreview;
  window.addAllPassageWordsToMyWords = addAllPassageWordsToMyWords;
  window.togglePassagePeek = togglePassagePeek;
  window.toggleOptionEnglish = toggleOptionEnglish;
  window.returnToPassageReading = returnToPassageReading;
  window.resetReadingLesson = resetReadingLesson;

  // Lesson picker, book mode, practice chaining, word drill
  window.renderReadingLessonChips = renderReadingLessonChips;
  window.selectReadingLesson = selectReadingLesson;
  window.startReadingBook = startReadingBook;
  window.bookNavReading = bookNavReading;
  window.jumpReadingBookLesson = jumpReadingBookLesson;
  window.bookNavSection = bookNavSection;
  window.jumpReadingBookSection = jumpReadingBookSection;
  window.startReadingPractice = startReadingPractice;
  window.practiceNextReadingLesson = practiceNextReadingLesson;
  window.startReadingWordDrill = startReadingWordDrill;
  window.restartReadingWordDrill = restartReadingWordDrill;
}
