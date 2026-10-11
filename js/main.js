/* =======================================================
   NIHONGO INTERMEDIATE — main.js
   Application Entry Point & Global Bindings
   ======================================================= */

import { state } from './state.js';
import { loadIntermediateVocabDB } from './data-loader.js';
import { loadStats, updateSidebarStats, toggleWordHard } from './srs.js';
import { showView } from './navigation.js';
import { startStudy, startDueReview, flipCard, gradeCard, exitStudy, playCurrentCardAudio, toggleCurrentCardHard } from './study.js';
import { setChapterGroup, selectChapter, setVocabFilter, onVocabSearch, toggleFurigana, playAudio, onToggleHard, drillAllHardWords, toggleRevealHardWords } from './vocab-browser.js';
import { setHomeGroup, toggleChapterSelection, selectAllChaptersInGroup, clearChapterSelection, renderHomeView } from './home.js';

// Expose controllers to window for HTML event handlers
window.state = state;
window.showView = showView;

// Study & Flashcards
window.startStudy = startStudy;
window.startDueReview = startDueReview;
window.flipCard = flipCard;
window.gradeCard = gradeCard;
window.exitStudy = exitStudy;
window.playCurrentCardAudio = playCurrentCardAudio;
window.toggleCurrentCardHard = toggleCurrentCardHard;

// Vocab Browser
window.setChapterGroup = setChapterGroup;
window.selectChapter = selectChapter;
window.setVocabFilter = setVocabFilter;
window.onVocabSearch = onVocabSearch;
window.toggleFurigana = toggleFurigana;
window.playAudio = playAudio;
window.onToggleHard = onToggleHard;
window.drillAllHardWords = drillAllHardWords;
window.toggleRevealHardWords = toggleRevealHardWords;

// Home Dashboard
window.setHomeGroup = setHomeGroup;
window.toggleChapterSelection = toggleChapterSelection;
window.selectAllChaptersInGroup = selectAllChaptersInGroup;
window.clearChapterSelection = clearChapterSelection;

// Global Keyboard Shortcuts
window.addEventListener('keydown', (e) => {
  if (state.currentView === 'study') {
    if (e.code === 'Space') {
      e.preventDefault();
      flipCard();
    } else if (state.cardFlipped && ['Digit1', 'Digit2', 'Digit3', 'Digit4'].includes(e.code)) {
      e.preventDefault();
      const grade = parseInt(e.code.replace('Digit', ''), 10);
      gradeCard(grade);
    } else if (e.code === 'Escape') {
      e.preventDefault();
      exitStudy();
    }
  }
});

// App Initialization
async function initApp() {
  console.log('Initializing Nihongo Intermediate...');
  loadStats();
  
  // Show loading indicator
  const loadEl = document.getElementById('dash-loading-status');
  if (loadEl) loadEl.textContent = 'Loading intermediate vocabulary database...';

  await loadIntermediateVocabDB();
  
  if (loadEl) loadEl.style.display = 'none';

  updateSidebarStats();
  showView('home');
  console.log('Nihongo Intermediate initialized successfully.');
}

window.addEventListener('DOMContentLoaded', initApp);
