/* =======================================================
   NIHONGO INTERMEDIATE — navigation.js
   5-Pillar Navigation Shell & View Management (WP-7)
   ======================================================= */

import { state } from './state.js';
import { renderHomeView } from './home.js';
import './today.js';
import { renderSrsHome } from './home-srs.js';
import { renderChapterChips, renderVocabList, updateHardWordsView } from './vocab-browser.js';
import { renderReadingView } from './reader.js';
import { renderGrammarView } from './grammar.js';
import { renderKanjiView } from './kanji.js';
import { initTestHub } from './test.js';

// Safe UI state initialization
if (!state.ui) {
  state.ui = {
    learnSegment: 'kanji',
    meSegment: 'weak'
  };
} else {
  if (!state.ui.learnSegment) state.ui.learnSegment = 'kanji';
  if (!state.ui.meSegment) state.ui.meSegment = 'weak';
}

/**
 * VIEW_TO_TAB Mapping:
 * Maps all legacy and new routes to one of the 5 dock tabs:
 * 'today' | 'learn' | 'read' | 'test' | 'me'
 */
export const VIEW_TO_TAB = {
  today: 'today',
  home: 'today',
  vocab: 'vocab',
  kanji: 'kanji',
  grammar: 'grammar',
  reading: 'reading',
  read: 'reading',
  learn: 'kanji',
  class: 'today',
  'class-track': 'today',
  test: 'today',
  me: 'today',
  'hard-words': 'today'
};

/**
 * Switch segment inside Learn tab ('kanji' | 'vocab' | 'grammar')
 */
export function switchLearnSegment(segment) {
  if (!['kanji', 'vocab', 'grammar'].includes(segment)) {
    segment = 'kanji';
  }
  state.ui = state.ui || {};
  state.ui.learnSegment = segment;

  // Toggle segmented control buttons
  document.querySelectorAll('.learn-segmented-control .seg-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-segment') === segment);
  });

  // Toggle learn segment views
  const segments = ['kanji', 'vocab', 'grammar'];
  segments.forEach(s => {
    const el = document.getElementById(`view-${s}`);
    if (el) {
      el.classList.toggle('active', s === segment);
    }
  });

  // Highlight matching sidebar subnav item if present
  document.querySelectorAll('.nav-sub-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-view') === segment);
  });

  // Trigger segment-specific rendering
  if (segment === 'kanji') {
    renderKanjiView();
  } else if (segment === 'vocab') {
    renderChapterChips();
    renderVocabList();
  } else if (segment === 'grammar') {
    renderGrammarView();
  }
}

/**
 * Switch segment inside Me tab ('weak' | 'stats' | 'settings')
 */
export function switchMeSegment(segment) {
  if (!['weak', 'stats', 'settings'].includes(segment)) {
    segment = 'weak';
  }
  state.ui = state.ui || {};
  state.ui.meSegment = segment;

  // Toggle segmented control buttons
  document.querySelectorAll('.me-segmented-control .seg-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-segment') === segment);
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

  // Update view-hard-words active class
  const vHard = document.getElementById('view-hard-words');
  if (vHard) {
    vHard.classList.toggle('active', segment === 'weak');
  }

  // Lifecycle updates for Me segments
  if (segment === 'weak') {
    updateHardWordsView();
  } else if (segment === 'stats') {
    updateMeStats();
  }
}

/**
 * Sync Me stats with sidebar counters
 */
function updateMeStats() {
  const m = document.getElementById('sb-mastered');
  const l = document.getElementById('sb-learning');
  const s = document.getElementById('sb-struggling');
  const u = document.getElementById('sb-unseen');

  const mm = document.getElementById('me-stat-mastered');
  const ml = document.getElementById('me-stat-learning');
  const ms = document.getElementById('me-stat-struggling');
  const mu = document.getElementById('me-stat-unseen');

  if (mm && m) mm.textContent = m.textContent;
  if (ml && l) ml.textContent = l.textContent;
  if (ms && s) ms.textContent = s.textContent;
  if (mu && u) mu.textContent = u.textContent;
}

/**
 * Main navigation router
 * Accepts every legacy viewId: home, vocab, kanji, grammar, reading, test, hard-words, study
 * and new viewIds: today, learn, read, me
 */
export function showView(viewId) {
  state.currentView = viewId;

  // Full-screen study runner mode: toggle .in-runner class on body
  if (viewId === 'study') {
    document.body.classList.add('in-runner');
  } else {
    document.body.classList.remove('in-runner');
  }

  // Deactivate all views first
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));

  const activeTab = VIEW_TO_TAB[viewId] || null;

  // Activate matching container and view
  if (viewId === 'today' || viewId === 'home') {
    const vToday = document.getElementById('view-today');
    const vHome = document.getElementById('view-home');
    if (vToday) vToday.classList.add('active');
    if (vHome) vHome.classList.add('active');
  } else if (viewId === 'learn') {
    const vLearn = document.getElementById('view-learn');
    if (vLearn) vLearn.classList.add('active');
    const seg = (state.ui && state.ui.learnSegment) || 'kanji';
    switchLearnSegment(seg);
  } else if (viewId === 'kanji' || viewId === 'vocab' || viewId === 'grammar') {
    const vLearn = document.getElementById('view-learn');
    if (vLearn) vLearn.classList.add('active');
    switchLearnSegment(viewId);
  } else if (viewId === 'read' || viewId === 'reading') {
    const vRead = document.getElementById('view-read');
    const vReading = document.getElementById('view-reading');
    if (vRead) vRead.classList.add('active');
    if (vReading) vReading.classList.add('active');
  } else if (viewId === 'test') {
    const vTest = document.getElementById('view-test');
    if (vTest) vTest.classList.add('active');
  } else if (viewId === 'me') {
    const vMe = document.getElementById('view-me');
    if (vMe) vMe.classList.add('active');
    const seg = (state.ui && state.ui.meSegment) || 'weak';
    switchMeSegment(seg);
  } else if (viewId === 'hard-words') {
    const vMe = document.getElementById('view-me');
    if (vMe) vMe.classList.add('active');
    switchMeSegment('weak');
  } else if (viewId === 'study') {
    const vStudy = document.getElementById('view-study');
    if (vStudy) vStudy.classList.add('active');
  } else {
    // Fallback for any unknown / custom viewId
    const target = document.getElementById(`view-${viewId}`);
    if (target) target.classList.add('active');
  }

  // Update navigation button active state (Sidebar)
  document.querySelectorAll('.nav-btn').forEach(btn => {
    const btnView = btn.getAttribute('data-view');
    const btnTab = btn.getAttribute('data-tab');
    const isActive = btnView === viewId || (activeTab && btnTab === activeTab) || (btnView === 'home' && activeTab === 'today');
    btn.classList.toggle('active', Boolean(isActive));
  });

  // Update sidebar subnav buttons
  document.querySelectorAll('.nav-sub-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-view') === viewId);
  });

  // Update mobile floating dock and legacy mobile nav
  document.querySelectorAll('#mobile-dock .mobile-dock-item, .mobile-nav-bar .mobile-nav-item').forEach(btn => {
    const itemTab = btn.getAttribute('data-tab') || VIEW_TO_TAB[btn.getAttribute('data-view')];
    btn.classList.toggle('active', Boolean(activeTab && itemTab === activeTab));
  });

  // Scroll to top of main container
  const main = document.getElementById('main');
  if (main) main.scrollTop = 0;

  // Lifecycle updates for target view
  if (viewId === 'today' || viewId === 'home') {
    renderHomeView();
    renderSrsHome();
  } else if (viewId === 'read' || viewId === 'reading') {
    renderReadingView();
  } else if (viewId === 'test') {
    initTestHub();
  }
}

// Bind to window for HTML onclick handlers
if (typeof window !== 'undefined') {
  window.showView = showView;
  window.switchLearnSegment = switchLearnSegment;
  window.switchMeSegment = switchMeSegment;
  window.VIEW_TO_TAB = VIEW_TO_TAB;
}
