/* =======================================================
   NIHONGO INTERMEDIATE — me-tab.js
   Me Tab Dashboard & Leech Fix-It Engine (WP-11 & WP-12)
   Reference:
   - n3_dev_handoff/01_UX_AND_SCREEN_SPEC.md §7
   - n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §8, §10
   ======================================================= */

import { state } from './state.js';
import {
  HARD_THRESHOLD,
  LEECH_LAPSES,
  EXAM_DATE_ISO
} from './config.js';
import {
  getItemStats,
  getItemStatus,
  toggleItemHard,
  getPillarFromKey,
  saveStats,
  updateSidebarStats
} from './srs.js';
import { getHeatmap30, getCurrentStreak } from './daylog.js';
import {
  downloadBackupFile,
  exportBackup,
  importBackup,
  createSnapshot
} from './backup.js';
import { showView } from './navigation.js';
import { renderCard } from './study.js?v=3.4';

// Storage Keys
export const SETTINGS_STORAGE_KEY = 'nihongo_intermediate_settings_v1';

// Default Application Settings
export const DEFAULT_SETTINGS = {
  examDate: EXAM_DATE_ISO || '2026-12-13',
  profile: 'standard', // 'light' | 'standard' | 'intensive'
  studyDays: 6,
  timeBudget: 40,
  furigana: true,
  readingFontScale: 1.0,
  targetReadingCpm: 330
};

// Pace Profile Quotas (doc 02 §6.3)
export const PACE_PROFILES = {
  light: {
    label: 'Light',
    vocab: 6,
    kanji: 6,
    grammar: 1,
    timeMin: 25,
    desc: 'Gentle routine · 6 vocab, 6 kanji, 1 grammar / day'
  },
  standard: {
    label: 'Standard',
    vocab: 10,
    kanji: 12,
    grammar: 2,
    timeMin: 40,
    desc: 'Target benchmark · 10 vocab, 12 kanji, 2 grammar / day'
  },
  intensive: {
    label: 'Intensive',
    vocab: 15,
    kanji: 18,
    grammar: 3,
    timeMin: 60,
    desc: 'Sprint exam prep · 15 vocab, 18 kanji, 3 grammar / day'
  }
};

// Safe localStorage accessor
function getStorage() {
  if (typeof localStorage !== 'undefined') return localStorage;
  if (typeof window !== 'undefined' && window.localStorage) return window.localStorage;
  return null;
}

// =======================================================
// 1. SETTINGS MANAGEMENT (Storage: nihongo_intermediate_settings_v1)
// =======================================================

/**
 * Loads user settings from localStorage into state.settings.
 * Falls back to DEFAULT_SETTINGS if key not present.
 * @returns {Object} Current settings
 */
export function loadSettings() {
  const storage = getStorage();
  let loaded = {};
  if (storage) {
    try {
      const raw = storage.getItem(SETTINGS_STORAGE_KEY);
      if (raw) {
        loaded = JSON.parse(raw);
      }
    } catch (e) {
      console.warn('[me-tab] Failed to parse settings from storage:', e);
    }
  }

  const merged = {
    ...DEFAULT_SETTINGS,
    ...(state.settings || {}),
    ...loaded
  };

  state.settings = merged;
  return merged;
}

/**
 * Saves partial or complete settings to localStorage and state.settings.
 * @param {Object} partialSettings
 * @returns {Object} Updated settings
 */
export function saveSettings(partialSettings = {}) {
  const current = state.settings || loadSettings();
  const updated = {
    ...current,
    ...partialSettings
  };

  state.settings = updated;
  const storage = getStorage();
  if (storage) {
    try {
      storage.setItem(SETTINGS_STORAGE_KEY, JSON.stringify(updated));
    } catch (e) {
      console.error('[me-tab] Failed to save settings to storage:', e);
    }
  }

  // Update dependent views if in browser
  if (typeof document !== 'undefined') {
    renderSettingsSegment();
  }

  return updated;
}

// =======================================================
// 2. WEAK POINTS QUERY & RESOLVER
// =======================================================

/**
 * Checks if a stats record meets weak point criteria:
 * isHard: true OR weight >= 1.8 OR leech: true OR lapses >= 5
 * @param {Object} s
 * @returns {boolean}
 */
export function isItemWeak(s) {
  if (!s || typeof s !== 'object') return false;
  return Boolean(
    s.isHard === true ||
    (typeof s.weight === 'number' && s.weight >= HARD_THRESHOLD) ||
    s.leech === true ||
    (typeof s.lapses === 'number' && s.lapses >= LEECH_LAPSES)
  );
}

/**
 * Checks if a stats record is a leech:
 * leech: true OR lapses >= 5
 * @param {Object} s
 * @returns {boolean}
 */
export function isItemLeech(s) {
  if (!s || typeof s !== 'object') return false;
  return Boolean(s.leech === true || (typeof s.lapses === 'number' && s.lapses >= LEECH_LAPSES));
}

/**
 * Resolves item metadata and content across all 4 pillars for card display & Fix-It.
 * @param {string} key - Item key (e.g. V:word_1, K:持, KWR:案内, GD:p1a:1:101, R_Q:q_1)
 * @param {Object} [stats] - Optional stats object
 * @returns {Object} Resolved weak item
 */
export function resolveWeakItem(key, stats = null) {
  const s = stats || getItemStats(key);
  const pillar = getPillarFromKey(key);
  const isLeech = isItemLeech(s);

  const base = {
    key,
    id: key,
    stats: s,
    pillar,
    isLeech,
    lapses: s.lapses || 0,
    weight: typeof s.weight === 'number' ? s.weight : 1.0,
    isHard: Boolean(s.isHard),
    note: s.note || '',
    cause: s.cause || '',
    term: key,
    reading: '',
    meaning: '',
    ruby_html: '',
    exampleJa: '',
    exampleEn: '',
    partOfSpeech: '',
    lessonTitle: '',
    homeKanji: null,
    kanjiRefs: [],
    rivals: []
  };

  // 1. Vocabulary (V: / VC:)
  if (key.startsWith('V:') || key.startsWith('VC:')) {
    const rawId = key.replace(/^VC:/, '').replace(/^V:/, '').replace(/:rev$/, '');
    base.id = rawId;

    let found = null;
    for (const chId in (state.vocabDB || {})) {
      const list = state.vocabDB[chId] || [];
      const match = list.find(w => String(w.id) === String(rawId));
      if (match) {
        found = match;
        base.lessonTitle = `Ch. ${chId.replace('part', '').replace('_', ' ')}`;
        break;
      }
    }

    if (found) {
      base.term = found.term_ja || found.term || rawId;
      base.reading = found.reading || '';
      base.meaning = found.meaning_en || '';
      base.ruby_html = found.ruby_html || '';
      base.exampleJa = found.example_ja || '';
      base.exampleEn = found.example_en || '';
      base.partOfSpeech = found.part_of_speech || '';
    } else if (state.idx?.words?.[rawId]) {
      const w = state.idx.words[rawId];
      base.term = w.term || rawId;
      base.reading = w.reading || '';
      base.meaning = w.meaning_en || '';
      base.ruby_html = w.ruby_html || '';
    }
    return base;
  }

  // 2. Kanji Character (K:)
  if (key.startsWith('K:')) {
    const char = key.replace(/^K:/, '');
    base.id = char;
    base.term = char;
    base.homeKanji = char;
    base.kanjiRefs = [char];

    const k = state.kanjiDB?.[char];
    if (k) {
      base.meaning = Array.isArray(k.meanings) ? k.meanings.join(', ') : (k.meaning_en || '');
      const on = Array.isArray(k.on_readings) ? k.on_readings.join('、') : '';
      const kun = Array.isArray(k.kun_readings) ? k.kun_readings.join('、') : '';
      base.reading = [on && `On: ${on}`, kun && `Kun: ${kun}`].filter(Boolean).join(' · ');
      base.lessonTitle = k.lesson_number ? `Kanji Lesson ${k.lesson_number}` : 'Kanji Target';
      base.rivals = Array.isArray(k.similar) ? k.similar : [];
      if (Array.isArray(k.words) && k.words[0]) {
        base.exampleJa = k.words[0].term_ja || k.words[0].term || '';
        base.exampleEn = k.words[0].meaning_en || '';
      }
    }
    return base;
  }

  // 3. Kanji Compound Words (KWR / KWW / KWM)
  if (key.startsWith('KWR:') || key.startsWith('KWW:') || key.startsWith('KWM:')) {
    const facet = key.slice(0, 3);
    const term = key.slice(4);
    base.id = term;
    base.term = term;

    const w = state.idx?.words?.[term];
    if (w) {
      base.reading = w.reading || '';
      base.meaning = w.meaning_en || '';
      base.ruby_html = w.ruby_html || '';
      base.homeKanji = w.homeKanji || null;
      base.kanjiRefs = w.kanjiRefs || [];
      base.lessonTitle = w.lesson ? `Lesson ${w.lesson}` : 'Kanji Word';
      if (w.context) {
        base.exampleJa = w.context.ja || '';
        base.exampleEn = w.context.en || '';
      }
    } else if (state.idx?.wordContexts?.[term]) {
      const c = state.idx.wordContexts[term][0] || state.idx.wordContexts[term];
      base.exampleJa = c.sentence_ja || c.ja || '';
      base.exampleEn = c.meaning || c.en || '';
    }
    return base;
  }

  // 4. Grammar Items (G: / GD: / GS: / GT: / GC:)
  if (key.startsWith('G:') || key.startsWith('GD:') || key.startsWith('GS:') || key.startsWith('GT:') || key.startsWith('GC:')) {
    const composite = key.replace(/^(GD|GS|GT|GC|G):/, '');
    base.id = composite;

    // Check grammar cards in index
    const cardInfo = state.idx?.grammar?.cards?.get?.(composite);
    if (cardInfo) {
      base.rivals = cardInfo.rivals || [];
      base.lessonTitle = cardInfo.cluster ? `Cluster: ${cardInfo.cluster}` : (cardInfo.section || 'Grammar');
    }

    // Search patterns index
    const patterns = state.grammarDB?.index || [];
    const pat = patterns.find(p => p.id === composite || p.pattern === composite);
    if (pat) {
      base.term = pat.pattern || composite;
      base.meaning = pat.meaning_en || pat.meaning || '';
      base.reading = pat.connection || '';
      if (Array.isArray(pat.example_sentences) && pat.example_sentences[0]) {
        base.exampleJa = pat.example_sentences[0].ja || pat.example_sentences[0].sentence || '';
        base.exampleEn = pat.example_sentences[0].en || pat.example_sentences[0].meaning || '';
      }
    } else {
      base.term = `Grammar Drill [${composite}]`;
      base.meaning = cardInfo?.cluster ? `Grammar pattern (${cardInfo.cluster})` : 'Grammar revision item';
    }
    return base;
  }

  // 5. Reading Questions & Passages (R_Q: / RP:)
  if (key.startsWith('R_Q:') || key.startsWith('RP:') || key.startsWith('R_P:')) {
    const cleanId = key.replace(/^(R_Q|RP|R_P):/, '');
    base.id = cleanId;

    if (key.startsWith('RP:')) {
      const lesson = state.readingDB?.[cleanId];
      base.term = lesson?.title_ja || lesson?.title || `Passage ${cleanId}`;
      base.meaning = lesson?.genre ? `Genre: ${lesson.genre}` : 'Reading Passage';
      base.lessonTitle = 'Dokkai Passage';
    } else {
      // Question lookup
      for (const lid in (state.readingDB || {})) {
        const lesson = state.readingDB[lid] || {};
        const qList = lesson.comprehensionQuestions || lesson.questions || [];
        const q = qList.find(item => (item.id || `${lid}_q${item.questionNumber || 1}`) === cleanId);
        if (q) {
          base.term = q.question_ja || `Question ${q.questionNumber || cleanId}`;
          base.meaning = `Correct: Option ${q.correctAnswer} — ${q.explanation_ja || ''}`;
          base.lessonTitle = lesson.title_ja || lesson.title || lid;
          base.exampleJa = q.context_sentence || '';
          break;
        }
      }
    }
    return base;
  }

  return base;
}

/**
 * Queries all weak items from stats, filters by pillar,
 * and sorts with LEECHES FIRST, followed by weight/lapses.
 *
 * @param {string} [filter='all'] - 'all' | 'vocab' | 'kanji' | 'grammar' | 'reading'
 * @param {Object} [statsObj=state.stats] - Stats dictionary
 * @returns {Array<Object>} Sorted weak items
 */
export function getWeakPoints(filter = 'all', statsObj = null) {
  const stats = statsObj || state.stats || {};
  const weakItems = [];

  for (const key in stats) {
    const s = stats[key];
    if (!isItemWeak(s)) continue;

    const itemPillar = getPillarFromKey(key);
    if (filter !== 'all' && itemPillar !== filter) continue;

    const resolved = resolveWeakItem(key, s);
    weakItems.push(resolved);
  }

  // Sorting rule (doc 02 §8 & prompt):
  // 1. Leeches come first!
  // 2. Among leeches: lapses descending, then weight descending
  // 3. Among non-leeches: weight descending, then incorrect descending
  weakItems.sort((a, b) => {
    if (a.isLeech && !b.isLeech) return -1;
    if (!a.isLeech && b.isLeech) return 1;

    if (a.isLeech && b.isLeech) {
      if (b.lapses !== a.lapses) return b.lapses - a.lapses;
      return b.weight - a.weight;
    }

    if (Math.abs(b.weight - a.weight) > 1e-6) {
      return b.weight - a.weight;
    }
    const incA = a.stats?.incorrect || 0;
    const incB = b.stats?.incorrect || 0;
    return incB - incA;
  });

  return weakItems;
}

// =======================================================
// 3. SEGMENT SWITCHING & TAB ORCHESTRATION
// =======================================================

/**
 * Switches the active segment inside Me tab:
 * 'weak' | 'stats' | 'settings'
 * @param {string} segment
 */
export function switchMeTabSegment(segment) {
  if (!['weak', 'stats', 'settings'].includes(segment)) {
    segment = 'weak';
  }

  state.ui = state.ui || {};
  state.ui.meSegment = segment;

  if (typeof document === 'undefined') return;

  // Toggle segmented control buttons
  document.querySelectorAll('.me-segmented-control .seg-btn').forEach(btn => {
    const btnSeg = btn.getAttribute('data-segment');
    btn.classList.toggle('active', btnSeg === segment);
  });

  // Toggle me segment panels
  const segments = ['weak', 'stats', 'settings'];
  segments.forEach(s => {
    const panel = document.getElementById(`me-panel-${s}`);
    if (panel) {
      panel.style.display = (s === segment) ? 'block' : 'none';
      panel.classList.toggle('active', s === segment);
    }
  });

  // Render the selected segment
  if (segment === 'weak') {
    renderWeakPointsSegment();
  } else if (segment === 'stats') {
    renderStatsSegment();
  } else if (segment === 'settings') {
    renderSettingsSegment();
  }
}

/**
 * Renders the full Me tab based on current UI state.
 * @param {string} [targetSegment]
 */
export function renderMeTab(targetSegment) {
  state.ui = state.ui || {};
  const segment = targetSegment || state.ui.meSegment || 'weak';
  switchMeTabSegment(segment);
}

// =======================================================
// 4. WEAK POINTS SEGMENT RENDERING
// =======================================================

/**
 * Filter chip handler for Weak Points
 * @param {string} filter - 'all' | 'vocab' | 'kanji' | 'grammar' | 'reading'
 */
export function setMeWeakFilter(filter) {
  state.weakPointsFilter = filter;
  renderWeakPointsSegment();
}

/**
 * Renders the Weak Points list with prominent leech badges,
 * filter chips, and primary CTAs.
 */
export function renderWeakPointsSegment() {
  if (typeof document === 'undefined') return;

  const panel = document.getElementById('me-panel-weak');
  if (!panel) return;

  const currentFilter = state.weakPointsFilter || 'all';
  const weakItems = getWeakPoints(currentFilter);
  const allWeakItems = getWeakPoints('all');

  // Count leeches
  const leechCount = allWeakItems.filter(i => i.isLeech).length;
  const totalCount = allWeakItems.length;

  // Pillar counts for filter chips
  const vocabCount = allWeakItems.filter(i => i.pillar === 'vocab').length;
  const kanjiCount = allWeakItems.filter(i => i.pillar === 'kanji').length;
  const grammarCount = allWeakItems.filter(i => i.pillar === 'grammar').length;
  const readingCount = allWeakItems.filter(i => i.pillar === 'reading').length;

  panel.innerHTML = `
    <div class="weak-points-header">
      <div class="wp-title-group">
        <div class="wp-title-row">
          <i class="fa-solid fa-fire-flame-curved wp-header-flame"></i>
          <div>
            <h2 class="wp-header-title">Exam Weak Points Revision Desk</h2>
            <p class="wp-header-sub" id="me-weak-count-sub">
              <strong>${totalCount}</strong> Weak Items · 
              <span class="leech-count-highlight"><i class="fa-solid fa-triangle-exclamation"></i> ${leechCount} Leech${leechCount === 1 ? '' : 'es'}</span>
            </p>
          </div>
        </div>
      </div>

      <!-- Primary CTAs in Thumb Zone -->
      <div class="wp-cta-group">
        <button class="btn btn-primary wp-cta-btn" onclick="drillAllWeak()" title="Drill all filtered weak points in active recall">
          <i class="fa-solid fa-fire"></i> Drill All Weak (${weakItems.length})
        </button>
        <button class="btn btn-quick wp-cta-btn" onclick="quick5Weak()" title="Fast 5-card burst focusing on top leeches">
          <i class="fa-solid fa-bolt"></i> Quick 5 Weak
        </button>
      </div>
    </div>

    <!-- Filter Chips -->
    <div class="wp-filter-chips" role="tablist" aria-label="Weak points filter">
      <button class="wp-chip ${currentFilter === 'all' ? 'active' : ''}" onclick="window.setMeWeakFilter('all')">
        All <span class="chip-count">${totalCount}</span>
      </button>
      <button class="wp-chip ${currentFilter === 'vocab' ? 'active' : ''}" onclick="window.setMeWeakFilter('vocab')">
        Vocab <span class="chip-count">${vocabCount}</span>
      </button>
      <button class="wp-chip ${currentFilter === 'kanji' ? 'active' : ''}" onclick="window.setMeWeakFilter('kanji')">
        Kanji <span class="chip-count">${kanjiCount}</span>
      </button>
      <button class="wp-chip ${currentFilter === 'grammar' ? 'active' : ''}" onclick="window.setMeWeakFilter('grammar')">
        Grammar <span class="chip-count">${grammarCount}</span>
      </button>
      <button class="wp-chip ${currentFilter === 'reading' ? 'active' : ''}" onclick="window.setMeWeakFilter('reading')">
        Reading <span class="chip-count">${readingCount}</span>
      </button>
    </div>

    <!-- Weak Items Container -->
    <div class="wp-card-list" id="me-weak-items-list">
      ${weakItems.length === 0 ? renderEmptyWeakState(currentFilter) : weakItems.map(renderWeakItemCard).join('')}
    </div>
  `;
}

function renderEmptyWeakState(filter) {
  return `
    <div class="wp-empty-state">
      <div class="empty-icon-wrap">
        <i class="fa-solid fa-circle-check"></i>
      </div>
      <h3>No Weak Points Found</h3>
      <p>All items in ${filter === 'all' ? 'all pillars' : filter} are currently stable in SRS with no high lapse counts.</p>
      <button class="btn btn-ghost btn-sm" onclick="showView('today')">
        <i class="fa-solid fa-calendar-day"></i> Return to Today Dashboard
      </button>
    </div>
  `;
}

function renderWeakItemCard(item) {
  const isLeech = item.isLeech;
  const lapses = item.lapses;
  const weight = Number(item.weight).toFixed(2);
  const noteSnippet = item.note ? `<div class="wp-card-note"><i class="fa-solid fa-note-sticky"></i> ${escapeHtml(item.note)}</div>` : '';

  return `
    <div class="wp-card ${isLeech ? 'wp-card-leech' : ''}" id="wp-card-${escapeAttr(item.key)}">
      <div class="wp-card-header">
        <div class="wp-card-badges">
          ${isLeech ? `<span class="leech-badge"><i class="fa-solid fa-fire"></i> LEECH</span>` : ''}
          <span class="lapse-pill ${lapses >= 5 ? 'lapse-critical' : ''}">Lapses: ${lapses}</span>
          <span class="weight-pill">W: ${weight}</span>
          <span class="pillar-tag pillar-${item.pillar}">${item.pillar}</span>
        </div>
        <div class="wp-card-actions-top">
          ${isLeech ? `
            <button class="btn btn-fixit" onclick="openLeechFixItSheet('${escapeAttr(item.key)}')" title="Open 3-step Leech Fix-It Desk">
              <i class="fa-solid fa-wrench"></i> Fix-It
            </button>
          ` : ''}
          <button class="btn-hard-flame ${item.isHard ? 'is-hard' : ''}" onclick="toggleWeakItemHard('${escapeAttr(item.key)}')" title="Toggle weak/hard flag">
            <i class="fa-solid fa-fire"></i>
          </button>
        </div>
      </div>

      <div class="wp-card-body">
        <div class="wp-term-row font-ja">
          ${item.ruby_html ? item.ruby_html : escapeHtml(item.term)}
          ${item.reading && !item.ruby_html ? `<span class="wp-reading">（${escapeHtml(item.reading)}）</span>` : ''}
        </div>
        <div class="wp-meaning-row">
          ${escapeHtml(item.meaning || item.lessonTitle || 'Revision item')}
        </div>
        ${item.exampleJa ? `
          <div class="wp-example-box font-ja">
            <div class="wp-example-ja">${escapeHtml(item.exampleJa)}</div>
            ${item.exampleEn ? `<div class="wp-example-en">${escapeHtml(item.exampleEn)}</div>` : ''}
          </div>
        ` : ''}
        ${noteSnippet}
      </div>
    </div>
  `;
}

/**
 * Toggles hard state for a weak item and re-renders view.
 * @param {string} key
 */
export function toggleWeakItemHard(key) {
  toggleItemHard(key);
  renderWeakPointsSegment();
}

/**
 * Primary CTA: Drills all filtered weak items in study runner
 */
export function drillAllWeak() {
  const currentFilter = state.weakPointsFilter || 'all';
  const pool = getWeakPoints(currentFilter);
  if (pool.length === 0) {
    if (typeof alert !== 'undefined') alert('No weak points to drill in this category!');
    return;
  }

  startWeakDrillSession(pool);
}

/**
 * Primary CTA: Drills top 5 weak items (prioritizing leeches)
 */
export function quick5Weak() {
  const currentFilter = state.weakPointsFilter || 'all';
  const pool = getWeakPoints(currentFilter);
  if (pool.length === 0) {
    if (typeof alert !== 'undefined') alert('No weak points to drill right now! Great job.');
    return;
  }

  const top5 = pool.slice(0, 5);
  startWeakDrillSession(top5);
}

function startWeakDrillSession(items) {
  state.studyMode = 'flashcard';
  state.studyIsDrillHard = true;
  state.drillOrigin = 'me';
  state.isDueReviewMode = false;
  state.learnUnit = null;
  state.sessionSkipped = 0;

  state.sessionItems = items.map(item => ({
    ...item,
    type: item.pillar === 'kanji' ? 'kanji' : 'vocab',
    book: item.pillar,
    key: item.key,
    term_ja: item.term,
    meaning_en: item.meaning,
    reading: item.reading,
    ruby_html: item.ruby_html,
    example_ja: item.exampleJa,
    example_en: item.exampleEn
  }));

  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = state.sessionItems.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

// =======================================================
// 5. STATS SEGMENT RENDERING
// =======================================================

/**
 * Renders the Stats segment:
 * 1. 4-Pillar summary cards (Vocab, Kanji, Grammar, Reading)
 * 2. 30-Day Activity Heatmap
 * 3. Consecutive Streak badge
 * 4. Reading CPM speed chart / average speed
 */
export function renderStatsSegment() {
  if (typeof document === 'undefined') return;

  const panel = document.getElementById('me-panel-stats');
  if (!panel) return;

  // 1. Gather stats per pillar
  const pillarStats = computePillarMasteryCounts();

  // 2. Heatmap & Streak
  const heatmap = getHeatmap30();
  const streak = getCurrentStreak();
  const totalHeatmapCards = heatmap.reduce((acc, d) => acc + (d.count || 0), 0);
  const activeDaysCount = heatmap.filter(d => (d.count || 0) > 0).length;

  // 3. Reading CPM stats
  const cpmData = computeReadingCpmStats();

  panel.innerHTML = `
    <div class="stats-segment-wrap">
      <!-- Section Header -->
      <div class="stats-header-group">
        <div>
          <h2 class="stats-main-title">Pillar Mastery &amp; Study Stats</h2>
        </div>
        <!-- Streak Badge -->
        <div class="streak-badge-card" title="Consecutive active study days">
          <div class="streak-icon-wrap">
            <i class="fa-solid fa-fire"></i>
          </div>
          <div>
            <div class="streak-val">${streak}</div>
            <div class="streak-lbl">Days Streak</div>
          </div>
        </div>
      </div>

      <!-- 4-Pillar Summary Cards Grid -->
      <div class="pillars-stats-grid">
        ${renderPillarCard('vocab', 'Vocabulary', 'fa-book', '#8b5cf6', pillarStats.vocab)}
        ${renderPillarCard('kanji', 'Kanji Characters', 'fa-shapes', '#22d3a4', pillarStats.kanji)}
        ${renderPillarCard('grammar', 'Sentence Grammar', 'fa-diagram-project', '#38bdf8', pillarStats.grammar)}
        ${renderPillarCard('reading', 'Dokkai Reading', 'fa-book-open', '#f59e0b', pillarStats.reading)}
      </div>

      <!-- 30-Day Activity Heatmap Section -->
      <div class="stat-card heatmap-card-wrap">
        <div class="heatmap-card-header">
          <div class="heatmap-title-row">
            <i class="fa-solid fa-calendar-check" style="color: #22d3a4;"></i>
            <h3>30-Day Study Activity Heatmap</h3>
          </div>
          <div class="heatmap-summary-pill">
            ${totalHeatmapCards} Reviews · ${activeDaysCount}/30 Active Days
          </div>
        </div>

        <div class="me-heatmap-grid" role="grid" aria-label="30-day activity calendar">
          ${heatmap.map(d => `
            <div class="me-heatmap-cell level-${d.level}" 
                 data-date="${d.date}" 
                 data-count="${d.count}"
                 title="${d.date}: ${d.count} cards reviewed">
            </div>
          `).join('')}
        </div>

        <div class="heatmap-footer-legend">
          <span>Less</span>
          <span class="legend-cell level-0"></span>
          <span class="legend-cell level-1"></span>
          <span class="legend-cell level-2"></span>
          <span class="legend-cell level-3"></span>
          <span class="legend-cell level-4"></span>
          <span>More</span>
        </div>
      </div>

      <!-- Reading CPM Speed Chart Section -->
      <div class="stat-card reading-cpm-card-wrap">
        <div class="cpm-header-row">
          <div class="cpm-title-group">
            <i class="fa-solid fa-gauge-high" style="color: #38bdf8;"></i>
            <h3>Reading CPM Speed Benchmarks</h3>
          </div>
          <div class="cpm-target-tag">
            Target: ${cpmData.targetCpm} Chars/Min (JLPT N3)
          </div>
        </div>

        <div class="cpm-metrics-summary">
          <div class="cpm-metric">
            <span class="metric-num">${cpmData.avgCpm || '—'}</span>
            <span class="metric-lbl">Average CPM</span>
          </div>
          <div class="cpm-metric">
            <span class="metric-num">${cpmData.bestCpm || '—'}</span>
            <span class="metric-lbl">Peak CPM</span>
          </div>
          <div class="cpm-metric">
            <span class="metric-num">${cpmData.passagesRead}</span>
            <span class="metric-lbl">Passages Read</span>
          </div>
        </div>

        <!-- CPM Speed Progress Bar vs Target -->
        <div class="cpm-chart-container">
          ${renderCpmChart(cpmData)}
        </div>
      </div>
    </div>
  `;
}

function renderPillarCard(id, label, icon, accentColor, data) {
  const total = (data.mastered || 0) + (data.learning || 0) + (data.struggling || 0);
  const masteredPct = total > 0 ? Math.round((data.mastered / total) * 100) : 0;
  const learningPct = total > 0 ? Math.round((data.learning / total) * 100) : 0;
  const strugglingPct = total > 0 ? Math.round((data.struggling / total) * 100) : 0;

  return `
    <div class="stat-card pillar-card">
      <div class="pillar-card-top">
        <div class="pillar-icon-name">
          <i class="fa-solid ${icon}" style="color: ${accentColor};"></i>
          <h4>${label}</h4>
        </div>
        <span class="pillar-total-tag">${total} Active</span>
      </div>

      <div class="pillar-counts-row">
        <div class="count-col">
          <span class="count-val green">${data.mastered || 0}</span>
          <span class="count-lbl">Mastered</span>
        </div>
        <div class="count-col">
          <span class="count-val amber">${data.learning || 0}</span>
          <span class="count-lbl">Learning</span>
        </div>
        <div class="count-col">
          <span class="count-val red">${data.struggling || 0}</span>
          <span class="count-lbl">Struggling</span>
        </div>
      </div>

      <div class="pillar-progress-track">
        <div class="pillar-prog-fill fill-green" style="width: ${masteredPct}%;" title="Mastered: ${masteredPct}%"></div>
        <div class="pillar-prog-fill fill-amber" style="width: ${learningPct}%;" title="Learning: ${learningPct}%"></div>
        <div class="pillar-prog-fill fill-red" style="width: ${strugglingPct}%;" title="Struggling: ${strugglingPct}%"></div>
      </div>
    </div>
  `;
}

function renderCpmChart(cpmData) {
  if (cpmData.passagesRead === 0) {
    return `
      <div class="cpm-empty-note">
        <i class="fa-solid fa-book-reader"></i>
        <p>No Dokkai passages recorded yet. Read passages in the <strong>Read tab</strong> to automatically track characters-per-minute speed against the 330 CPM benchmark.</p>
      </div>
    `;
  }

  const target = cpmData.targetCpm || 330;
  const pct = Math.min(100, Math.round((cpmData.avgCpm / target) * 100));

  return `
    <div class="cpm-progress-wrap">
      <div class="cpm-bar-header">
        <span>Average Pace vs 330 CPM Standard</span>
        <span class="cpm-pct-label ${pct >= 100 ? 'cpm-good' : ''}">${pct}% Target</span>
      </div>
      <div class="cpm-progress-track">
        <div class="cpm-progress-fill ${pct >= 100 ? 'cpm-good' : ''}" style="width: ${pct}%;"></div>
        <div class="cpm-target-pin" title="330 CPM Standard"></div>
      </div>
    </div>
    ${cpmData.recentPassages.length > 0 ? `
      <div class="cpm-recent-list">
        <div class="cpm-recent-title">Recent Passages Read:</div>
        ${cpmData.recentPassages.map(p => `
          <div class="cpm-recent-row">
            <span class="p-title">${escapeHtml(p.title)}</span>
            <span class="p-cpm ${p.cpm >= target ? 'cpm-good' : ''}">${p.cpm} CPM</span>
          </div>
        `).join('')}
      </div>
    ` : ''}
  `;
}

function computePillarMasteryCounts() {
  const result = {
    vocab: { mastered: 0, learning: 0, struggling: 0 },
    kanji: { mastered: 0, learning: 0, struggling: 0 },
    grammar: { mastered: 0, learning: 0, struggling: 0 },
    reading: { mastered: 0, learning: 0, struggling: 0 }
  };

  const stats = state.stats || {};
  for (const key in stats) {
    const s = stats[key];
    const pillar = getPillarFromKey(key);
    if (!result[pillar]) continue;

    const st = getItemStatus(key);
    if (st === 'mastered') result[pillar].mastered++;
    else if (st === 'hard') result[pillar].struggling++;
    else if (st === 'learning') result[pillar].learning++;
  }

  return result;
}

function computeReadingCpmStats() {
  const stats = state.stats || {};
  const cpms = [];
  const recent = [];

  for (const key in stats) {
    if (!key.startsWith('RP:')) continue;
    const s = stats[key];
    const cpm = s.lastCpm || s.bestCpm;
    if (typeof cpm === 'number' && cpm > 0) {
      cpms.push(cpm);
      const cleanId = key.replace(/^RP:/, '');
      const lesson = state.readingDB?.[cleanId];
      recent.push({
        id: cleanId,
        title: lesson?.title_ja || lesson?.title || cleanId,
        cpm
      });
    }
  }

  const passagesRead = cpms.length;
  const avgCpm = passagesRead > 0 ? Math.round(cpms.reduce((a, b) => a + b, 0) / passagesRead) : 0;
  const bestCpm = passagesRead > 0 ? Math.max(...cpms) : 0;

  return {
    targetCpm: 330,
    avgCpm,
    bestCpm,
    passagesRead,
    recentPassages: recent.slice(0, 5)
  };
}

// =======================================================
// 6. SETTINGS SEGMENT RENDERING & ACTIONS
// =======================================================

/**
 * Renders the Settings segment:
 * 1. NAT-TEST / JLPT Exam Date Picker
 * 2. Pace Profile Selector (Light, Standard, Intensive)
 * 3. Study days per week selector
 * 4. Data Management actions (Export, Import, Snapshot & Reset)
 */
export function renderSettingsSegment() {
  if (typeof document === 'undefined') return;

  const panel = document.getElementById('me-panel-settings');
  if (!panel) return;

  const settings = state.settings || loadSettings();
  const examDate = settings.examDate || EXAM_DATE_ISO || '2026-12-13';
  const profileKey = (settings.profile || 'standard').toLowerCase();
  const studyDays = settings.studyDays !== undefined ? settings.studyDays : 6;

  // Compute countdown
  const now = Date.now();
  const examMs = new Date(examDate).getTime();
  const daysLeft = Math.max(0, Math.ceil((examMs - now) / 86400000));

  panel.innerHTML = `
    <div class="settings-segment-wrap">
      <!-- Section Header -->
      <div class="settings-header-group">
        <h2 class="settings-main-title">Settings &amp; Data Management</h2>
      </div>

      <!-- 1. Exam Target Date Picker -->
      <div class="stat-card setting-section-card">
        <div class="setting-title-row">
          <i class="fa-solid fa-calendar-star" style="color: #ec4899;"></i>
          <div>
            <h3>NAT-TEST / JLPT Exam Date</h3>
            <p>Calculates safe SRS interval caps so cards are scheduled before the exam.</p>
          </div>
        </div>

        <div class="exam-date-control-group">
          <input type="date" 
                 id="me-setting-exam-date" 
                 class="me-date-input" 
                 value="${escapeAttr(examDate)}" 
                 onchange="window.onExamDateChange(this.value)">
          <div class="exam-countdown-badge">
            <i class="fa-solid fa-hourglass-half"></i>
            <span><strong>${daysLeft}</strong> days until Exam</span>
          </div>
        </div>
      </div>

      <!-- 2. Pace Profile Selector -->
      <div class="stat-card setting-section-card">
        <div class="setting-title-row">
          <i class="fa-solid fa-sliders" style="color: #8b5cf6;"></i>
          <div>
            <h3>Pace Profile Selector</h3>
            <p>Determines daily new items quota across Vocab, Kanji, and Grammar.</p>
          </div>
        </div>

        <div class="pace-profiles-grid">
          ${renderPaceProfileCard('light', PACE_PROFILES.light, profileKey === 'light')}
          ${renderPaceProfileCard('standard', PACE_PROFILES.standard, profileKey === 'standard')}
          ${renderPaceProfileCard('intensive', PACE_PROFILES.intensive, profileKey === 'intensive')}
        </div>
      </div>

      <!-- 3. Study Days Per Week -->
      <div class="stat-card setting-section-card">
        <div class="setting-title-row">
          <i class="fa-solid fa-calendar-week" style="color: #22d3a4;"></i>
          <div>
            <h3>Study Days Per Week</h3>
            <p>Reserve days allow buffer for catch-up and revision routines.</p>
          </div>
        </div>

        <div class="study-days-selector-row">
          ${[4, 5, 6, 7].map(d => `
            <button class="day-chip-btn ${studyDays === d ? 'active' : ''}" 
                    onclick="window.onStudyDaysChange(${d})">
              ${d} Days / Week
            </button>
          `).join('')}
        </div>
      </div>

      <!-- 4. Data Management Actions -->
      <div class="stat-card setting-section-card">
        <div class="setting-title-row">
          <i class="fa-solid fa-database" style="color: #38bdf8;"></i>
          <div>
            <h3>Data Management &amp; Recovery</h3>
            <p>Full JSON backups, safety snapshots, and device-to-device migration.</p>
          </div>
        </div>

        <div class="data-actions-flex">
          <button class="btn btn-outline data-btn" onclick="window.downloadBackupFile ? window.downloadBackupFile() : window.exportBackupJson()" title="Download JSON file of stats and settings">
            <i class="fa-solid fa-download"></i> Export Backup JSON
          </button>
          <button class="btn btn-outline data-btn" onclick="window.triggerImportBackup()" title="Restore from local JSON file">
            <i class="fa-solid fa-upload"></i> Import Backup JSON
          </button>
          <button class="btn btn-danger-outline data-btn" onclick="window.snapshotAndReset()" title="Snapshot state and reset stats">
            <i class="fa-solid fa-rotate-left"></i> Snapshot &amp; Reset
          </button>
        </div>
        <input type="file" id="me-backup-file-picker" accept=".json" style="display: none;" onchange="window.handleBackupFileSelected(this)">
      </div>
    </div>
  `;
}

function renderPaceProfileCard(id, data, isActive) {
  return `
    <div class="pace-card ${isActive ? 'active' : ''}" onclick="window.onPaceProfileChange('${id}')">
      <div class="pace-card-head">
        <span class="pace-badge">${data.label}</span>
        ${isActive ? '<i class="fa-solid fa-circle-check pace-check"></i>' : ''}
      </div>
      <div class="pace-quotas">
        <span><strong>${data.vocab}</strong> vocab</span> · 
        <span><strong>${data.kanji}</strong> kanji</span> · 
        <span><strong>${data.grammar}</strong> gram</span>
      </div>
      <div class="pace-time">~${data.timeMin} min / day</div>
    </div>
  `;
}

export function onExamDateChange(newDate) {
  if (!newDate) return;
  saveSettings({ examDate: newDate });
}

export function onPaceProfileChange(profileKey) {
  saveSettings({ profile: profileKey });
}

export function onStudyDaysChange(days) {
  saveSettings({ studyDays: parseInt(days, 10) || 6 });
}

export function exportBackupJson() {
  if (typeof downloadBackupFile === 'function') {
    downloadBackupFile();
  } else {
    const jsonStr = exportBackup();
    if (typeof document !== 'undefined' && typeof Blob !== 'undefined') {
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `nihongo-backup-${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      setTimeout(() => {
        URL.revokeObjectURL(a.href);
        a.remove();
      }, 500);
    }
  }
}

export function triggerImportBackup() {
  const picker = document.getElementById('me-backup-file-picker');
  if (picker) {
    picker.value = '';
    picker.click();
  }
}

export function handleBackupFileSelected(input) {
  if (!input || !input.files || !input.files[0]) return;
  const file = input.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    try {
      const content = e.target.result;
      const res = importBackup(content, { merge: true });
      if (res.success) {
        if (typeof alert !== 'undefined') {
          alert(`Backup restored successfully! ${res.count || 0} items updated.`);
        }
        renderMeTab();
      } else {
        if (typeof alert !== 'undefined') alert(`Import failed: ${res.error}`);
      }
    } catch (err) {
      if (typeof alert !== 'undefined') alert(`Error reading backup file: ${err.message}`);
    }
  };

  reader.readAsText(file);
}

export function snapshotAndReset() {
  const confirmed = typeof confirm !== 'undefined'
    ? confirm('This will create an automatic recovery snapshot and reset all study records. Continue?')
    : true;

  if (!confirmed) return;

  const tag = `reset_${Date.now()}`;
  createSnapshot(tag);

  state.stats = {};
  saveStats();
  if (typeof updateSidebarStats === 'function') updateSidebarStats();

  if (typeof alert !== 'undefined') {
    alert(`Reset complete. Safety snapshot created: ${tag}. You can restore it anytime via Restore Snapshot.`);
  }

  renderMeTab();
}

// =======================================================
// 7. LEECH FIX-IT SHEET (doc 02 §8 3-Step Bottom Modal)
// =======================================================

let activeFixItKey = null;
let activeFixItStep = 1;

/**
 * Opens the 3-step Leech Fix-It bottom modal for a specific card key.
 * Step 1: Contrast
 * Step 2: Context
 * Step 3: Hook
 *
 * @param {string} itemKey
 */
export function openLeechFixItSheet(itemKey) {
  if (!itemKey) return;
  activeFixItKey = itemKey;
  activeFixItStep = 1;

  if (typeof document === 'undefined') return;

  let modalOverlay = document.getElementById('leech-fixit-modal-overlay');
  if (!modalOverlay) {
    modalOverlay = document.createElement('div');
    modalOverlay.id = 'leech-fixit-modal-overlay';
    modalOverlay.className = 'fixit-modal-overlay';
    document.body.appendChild(modalOverlay);
  }

  renderFixItModalContent();
  modalOverlay.classList.add('is-open');
}

/**
 * Closes the Leech Fix-It bottom modal.
 */
export function closeLeechFixItSheet() {
  activeFixItKey = null;
  if (typeof document === 'undefined') return;

  const modalOverlay = document.getElementById('leech-fixit-modal-overlay');
  if (modalOverlay) {
    modalOverlay.classList.remove('is-open');
  }
}

/**
 * Saves personal hook/mnemonic to s.note for an item key.
 * @param {string} itemKey
 * @param {string} mnemonic
 */
export function saveLeechMnemonic(itemKey, mnemonic) {
  if (!itemKey) return;
  const s = getItemStats(itemKey);
  s.note = String(mnemonic || '').trim();
  saveStats();
}

/**
 * Action button: "Done, Schedule in 1 Day"
 * Sets nextDue = now + 1 day, interval = 1, reps = 0, relearning state.
 * @param {string} itemKey
 */
export function scheduleLeechInOneDay(itemKey) {
  if (!itemKey) return;
  const s = getItemStats(itemKey);
  const now = Date.now();
  const DAY_MS = 24 * 60 * 60 * 1000;

  s.nextDue = now + DAY_MS;
  s.interval = 1;
  s.reps = 0;
  s.learnState = 'relearning';
  s.streak = 0;

  saveStats();
  if (typeof updateSidebarStats === 'function') {
    updateSidebarStats();
  }
}

/**
 * Switches step inside Fix-It modal (1: Contrast, 2: Context, 3: Hook)
 * @param {number} step
 */
export function setFixItStep(step) {
  activeFixItStep = Math.max(1, Math.min(3, step));
  renderFixItModalContent();
}

/**
 * Completes Fix-It flow, saves mnemonic, schedules in 1 day, and closes modal.
 */
export function finishLeechFixIt() {
  if (!activeFixItKey) return;

  // Grab latest mnemonic text from textarea
  if (typeof document !== 'undefined') {
    const input = document.getElementById('fixit-mnemonic-input');
    if (input) {
      saveLeechMnemonic(activeFixItKey, input.value);
    }
  }

  scheduleLeechInOneDay(activeFixItKey);
  closeLeechFixItSheet();

  // Re-render weak points list
  if (typeof document !== 'undefined') {
    renderWeakPointsSegment();
  }
}

function renderFixItModalContent() {
  if (typeof document === 'undefined' || !activeFixItKey) return;
  const overlay = document.getElementById('leech-fixit-modal-overlay');
  if (!overlay) return;

  const item = resolveWeakItem(activeFixItKey);
  const contrastData = getLeechContrastData(item);
  const contextSentence = getLeechContextSentence(item);
  const breakdownStrip = getKanjiBreakdownStrip(item);

  overlay.innerHTML = `
    <div class="fixit-backdrop" onclick="closeLeechFixItSheet()"></div>
    <div class="fixit-sheet" role="dialog" aria-modal="true" aria-labelledby="fixit-sheet-title">
      <!-- Sheet Header -->
      <div class="fixit-sheet-header">
        <div class="fixit-header-left">
          <span class="leech-badge"><i class="fa-solid fa-fire"></i> LEECH FIX-IT</span>
          <h3 id="fixit-sheet-title" class="fixit-term-title font-ja">${escapeHtml(item.term)}</h3>
        </div>
        <button class="fixit-close-btn" onclick="closeLeechFixItSheet()" aria-label="Close Fix-It Sheet">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Step Indicator Chips -->
      <div class="fixit-step-nav" role="tablist">
        <button class="fixit-step-chip ${activeFixItStep === 1 ? 'active' : ''}" onclick="window.setFixItStep(1)">
          <span class="step-num">1</span> Contrast
        </button>
        <button class="fixit-step-chip ${activeFixItStep === 2 ? 'active' : ''}" onclick="window.setFixItStep(2)">
          <span class="step-num">2</span> Context
        </button>
        <button class="fixit-step-chip ${activeFixItStep === 3 ? 'active' : ''}" onclick="window.setFixItStep(3)">
          <span class="step-num">3</span> Hook
        </button>
      </div>

      <!-- Step Body -->
      <div class="fixit-sheet-body">
        ${activeFixItStep === 1 ? renderFixItStep1Contrast(item, contrastData) : ''}
        ${activeFixItStep === 2 ? renderFixItStep2Context(item, contextSentence) : ''}
        ${activeFixItStep === 3 ? renderFixItStep3Hook(item, breakdownStrip) : ''}
      </div>

      <!-- Sticky Thumb-Zone Footer CTA -->
      <div class="fixit-sheet-footer">
        <div class="fixit-footer-nav-btns">
          ${activeFixItStep > 1 ? `
            <button class="btn btn-ghost fixit-nav-btn" onclick="window.setFixItStep(${activeFixItStep - 1})">
              <i class="fa-solid fa-arrow-left"></i> Back
            </button>
          ` : '<div style="flex: 1;"></div>'}
          ${activeFixItStep < 3 ? `
            <button class="btn btn-outline fixit-nav-btn" onclick="window.setFixItStep(${activeFixItStep + 1})">
              Next Step <i class="fa-solid fa-arrow-right"></i>
            </button>
          ` : ''}
        </div>

        <button class="btn btn-primary fixit-done-btn" onclick="finishLeechFixIt()">
          <i class="fa-solid fa-check"></i> Done, Schedule in 1 Day
        </button>
      </div>
    </div>
  `;
}

function renderFixItStep1Contrast(item, contrast) {
  return `
    <div class="fixit-step-content fixit-step-contrast">
      <div class="step-instructions">
        <i class="fa-solid fa-scale-unbalanced" style="color: #38bdf8;"></i>
        <span>Step 1: Tell rivals apart. Pinpoint what makes this word distinct.</span>
      </div>

      <div class="contrast-cards-duo">
        <!-- Target Card -->
        <div class="contrast-box target-box">
          <div class="contrast-box-label">Target Item</div>
          <div class="contrast-term font-ja">${escapeHtml(item.term)}</div>
          <div class="contrast-reading">${escapeHtml(item.reading || '')}</div>
          <div class="contrast-meaning">${escapeHtml(item.meaning || '')}</div>
        </div>

        <!-- Confusable Rival Card -->
        <div class="contrast-box rival-box">
          <div class="contrast-box-label">Nearest Confusable Rival</div>
          <div class="contrast-term font-ja">${escapeHtml(contrast.rivalTerm || 'Rival pattern')}</div>
          <div class="contrast-reading">${escapeHtml(contrast.rivalReading || '')}</div>
          <div class="contrast-meaning">${escapeHtml(contrast.rivalMeaning || 'Similar form / reading trap')}</div>
        </div>
      </div>

      <div class="contrast-cue-note">
        <i class="fa-solid fa-lightbulb"></i>
        <span><strong>Key Distinction:</strong> ${escapeHtml(contrast.cue)}</span>
      </div>
    </div>
  `;
}

function renderFixItStep2Context(item, context) {
  const highlightedSentence = highlightTermInSentence(context.ja, item.term);

  return `
    <div class="fixit-step-content fixit-step-context">
      <div class="step-instructions">
        <i class="fa-solid fa-quote-left" style="color: #22d3a4;"></i>
        <span>Step 2: Experience in context. Read the target in an authentic sentence.</span>
      </div>

      <div class="context-sentence-card">
        <div class="context-ja font-ja">
          ${highlightedSentence || escapeHtml(item.exampleJa || 'No sentence available.')}
        </div>
        <div class="context-en">
          ${escapeHtml(context.en || item.exampleEn || 'Read the context carefully to cement target usage.')}
        </div>
      </div>

      <div class="context-source-badge">
        <i class="fa-solid fa-bookmark"></i>
        <span>${escapeHtml(context.src || item.lessonTitle || 'JLPT N3 Context Bank')}</span>
      </div>
    </div>
  `;
}

function renderFixItStep3Hook(item, breakdownStrip) {
  const currentNote = item.note || '';

  return `
    <div class="fixit-step-content fixit-step-hook">
      <div class="step-instructions">
        <i class="fa-solid fa-anchor" style="color: #ec4899;"></i>
        <span>Step 3: Anchor a memory hook. Personal mnemonics break lapse loops permanently.</span>
      </div>

      ${breakdownStrip ? `
        <div class="kanji-breakdown-section">
          <div class="breakdown-title">Kanji Component Breakdown:</div>
          <div class="breakdown-chips-row">${breakdownStrip}</div>
        </div>
      ` : ''}

      <div class="hook-input-group">
        <label for="fixit-mnemonic-input" class="hook-label">
          <i class="fa-solid fa-pen-nib"></i> My Personal Mnemonic / Hook (saves to s.note):
        </label>
        <textarea id="fixit-mnemonic-input" 
                  class="hook-textarea" 
                  placeholder="e.g. 案 (plan) + 内 (inside) -> The person inside plans your path = 案内 (guide)..."
                  oninput="window.saveLeechMnemonic('${escapeAttr(item.key)}', this.value)">${escapeHtml(currentNote)}</textarea>
      </div>
    </div>
  `;
}

// =======================================================
// 8. RESOLVER HELPERS (Contrast, Context & Breakdown)
// =======================================================

function getLeechContrastData(item) {
  // 1. Kanji Word Confusable Lookup
  if (item.homeKanji && state.idx?.kanjiWords?.[item.homeKanji]) {
    const siblings = state.idx.kanjiWords[item.homeKanji].filter(t => t !== item.term);
    if (siblings.length > 0) {
      const rivalTerm = siblings[0];
      const rivalData = state.idx?.words?.[rivalTerm] || {};
      return {
        rivalTerm,
        rivalReading: rivalData.reading || '',
        rivalMeaning: rivalData.meaning_en || 'Different reading of the same kanji',
        cue: `Both words contain kanji ${item.homeKanji}, but have distinct readings and roles.`
      };
    }
  }

  // 2. Grammar rivals
  if (item.rivals && item.rivals.length > 0) {
    const rId = item.rivals[0];
    const patterns = state.grammarDB?.index || [];
    const rPat = patterns.find(p => p.id === rId);
    return {
      rivalTerm: rPat?.pattern || rId,
      rivalReading: rPat?.connection || '',
      rivalMeaning: rPat?.meaning_en || 'Cluster rival pattern',
      cue: `Notice nuance differences in connection rules and emotional stance.`
    };
  }

  // 3. Kanji character similar
  if (item.pillar === 'kanji' && state.kanjiDB?.[item.term]?.similar) {
    const sim = state.kanjiDB[item.term].similar[0];
    if (sim) {
      const simK = state.kanjiDB[sim] || {};
      return {
        rivalTerm: sim,
        rivalReading: Array.isArray(simK.on_readings) ? simK.on_readings[0] : '',
        rivalMeaning: Array.isArray(simK.meanings) ? simK.meanings.join(', ') : '',
        cue: `Visually similar kanji with different radical components.`
      };
    }
  }

  // 4. Default fallback
  return {
    rivalTerm: 'Confusable / Opposite',
    rivalReading: '—',
    rivalMeaning: 'Common pitfall pairing',
    cue: 'Pay close attention to okurigana and phonetic reading markers.'
  };
}

function getLeechContextSentence(item) {
  if (item.exampleJa) {
    return {
      ja: item.exampleJa,
      en: item.exampleEn,
      src: item.lessonTitle
    };
  }

  // Check wordContexts
  const rawCtx = state.idx?.wordContexts?.[item.term];
  if (rawCtx) {
    const c = Array.isArray(rawCtx) ? rawCtx[0] : rawCtx;
    if (c) {
      return {
        ja: c.ja || c.sentence_ja || '',
        en: c.en || c.meaning || '',
        src: c.src || c.source || 'Sentence Bank'
      };
    }
  }

  return {
    ja: `彼は${item.term}について詳しく説明した。`,
    en: 'He explained in detail regarding this item.',
    src: 'Practice Sentence'
  };
}

function getKanjiBreakdownStrip(item) {
  const chars = item.kanjiRefs && item.kanjiRefs.length > 0
    ? item.kanjiRefs
    : (item.term.match(/[\u4e00-\u9faf]/g) || []);

  if (!chars || chars.length === 0) return '';

  return chars.map(ch => {
    const k = state.kanjiDB?.[ch] || {};
    const meaning = Array.isArray(k.meanings) ? k.meanings[0] : (k.meaning_en || '');
    const on = Array.isArray(k.on_readings) ? k.on_readings[0] : '';
    return `
      <div class="k-chip font-ja">
        <span class="k-char">${escapeHtml(ch)}</span>
        <span class="k-sub">${escapeHtml(meaning || on || '')}</span>
      </div>
    `;
  }).join('');
}

function highlightTermInSentence(sentence, term) {
  if (!sentence || !term) return sentence || '';
  const escapedTerm = escapeHtml(term);
  const escapedSentence = escapeHtml(sentence);

  // Wrap target occurrences in highlight marker
  return escapedSentence.split(escapedTerm).join(`<mark class="fixit-highlight">${escapedTerm}</mark>`);
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function escapeAttr(str) {
  if (!str) return '';
  return String(str).replace(/"/g, '&quot;').replace(/'/g, '&#039;');
}

// =======================================================
// 9. WINDOW BINDINGS (Seamless Event Integration)
// =======================================================

if (typeof window !== 'undefined') {
  window.renderMeTab = renderMeTab;
  window.switchMeTabSegment = switchMeTabSegment;
  window.switchMeSegment = switchMeTabSegment; // Backwards compatibility for HTML buttons
  window.setMeWeakFilter = setMeWeakFilter;
  window.openLeechFixItSheet = openLeechFixItSheet;
  window.closeLeechFixItSheet = closeLeechFixItSheet;
  window.saveLeechMnemonic = saveLeechMnemonic;
  window.scheduleLeechInOneDay = scheduleLeechInOneDay;
  window.setFixItStep = setFixItStep;
  window.finishLeechFixIt = finishLeechFixIt;
  window.drillAllWeak = drillAllWeak;
  window.quick5Weak = quick5Weak;
  window.toggleWeakItemHard = toggleWeakItemHard;
  window.onExamDateChange = onExamDateChange;
  window.onPaceProfileChange = onPaceProfileChange;
  window.onStudyDaysChange = onStudyDaysChange;
  window.exportBackupJson = exportBackupJson;
  window.triggerImportBackup = triggerImportBackup;
  window.handleBackupFileSelected = handleBackupFileSelected;
  window.snapshotAndReset = snapshotAndReset;
}
