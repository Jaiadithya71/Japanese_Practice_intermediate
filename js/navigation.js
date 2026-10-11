/* =======================================================
   NIHONGO INTERMEDIATE — navigation.js
   View Management & Tab Navigation
   ======================================================= */

import { state } from './state.js';
import { renderHomeView } from './home.js';
import { renderChapterChips, renderVocabList, updateHardWordsView } from './vocab-browser.js';

import { renderReadingView } from './reader.js';

export function showView(viewId) {
  state.currentView = viewId;

  // Toggle active class on views
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  const target = document.getElementById(`view-${viewId}`);
  if (target) {
    target.classList.add('active');
  }

  // Update navigation button active state
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-view') === viewId);
  });
  document.querySelectorAll('.mobile-nav-item').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-view') === viewId);
  });

  // Scroll to top of main container
  const main = document.getElementById('main');
  if (main) main.scrollTop = 0;

  // Lifecycle updates for target view
  if (viewId === 'home') {
    renderHomeView();
  } else if (viewId === 'vocab') {
    renderChapterChips();
    renderVocabList();
  } else if (viewId === 'reading') {
    renderReadingView();
  } else if (viewId === 'hard-words') {
    updateHardWordsView();
  }
}
