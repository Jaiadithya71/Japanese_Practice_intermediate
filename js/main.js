/* =======================================================
   NIHONGO INTERMEDIATE — main.js
   Application Entry Point & Global Bindings (5-Pillar Architecture)
   ======================================================= */

import { state } from './state.js';
import { loadAllActiveBooks } from './data-loader.js';
import { loadStats, updateSidebarStats, toggleWordHard } from './srs.js';
import { showView } from './navigation.js';
import { startStudy, startDueReview, startOmniReview, flipCard, gradeCard, exitStudy, playCurrentCardAudio, toggleCurrentCardHard } from './study.js';
import { setChapterGroup, selectChapter, setVocabFilter, onVocabSearch, toggleFurigana, playAudio, onToggleHard, drillAllHardWords, toggleRevealHardWords, setWeakPointsFilter } from './vocab-browser.js';
import { setHomeGroup, toggleChapterSelection, selectAllChaptersInGroup, clearChapterSelection, renderHomeView } from './home.js';
import { openReadingLesson, closeReadingWorkspace, setReadingCategory, selectQuizOption, submitQuizAnswers, addMissedQuestionsToSRS, toggleSentenceTranslations } from './reader.js';
import { scheduleGistSave, openSyncSetup, closeSyncSetup, connectGist, forceSyncNow, disconnectGist, initSyncUI } from './gist-sync.js';

// Expose controllers to window for HTML event handlers
window.state = state;
window.showView = showView;

// Optional Gist sync
window.__n3ScheduleSync = scheduleGistSave;
window.openSyncSetup = openSyncSetup;
window.closeSyncSetup = closeSyncSetup;
window.connectGist = connectGist;
window.forceSyncNow = forceSyncNow;
window.disconnectGist = disconnectGist;

// Study & Multi-Pillar Omni-Review
window.startStudy = startStudy;
window.startDueReview = startDueReview;
window.startOmniReview = startOmniReview;
window.flipCard = flipCard;
window.gradeCard = gradeCard;
window.exitStudy = exitStudy;
window.playCurrentCardAudio = playCurrentCardAudio;
window.toggleCurrentCardHard = toggleCurrentCardHard;

// Vocab Browser & Universal Weak Points
window.setChapterGroup = setChapterGroup;
window.selectChapter = selectChapter;
window.setVocabFilter = setVocabFilter;
window.onVocabSearch = onVocabSearch;
window.toggleFurigana = toggleFurigana;
window.playAudio = playAudio;
window.onToggleHard = onToggleHard;
window.drillAllHardWords = drillAllHardWords;
window.toggleRevealHardWords = toggleRevealHardWords;
window.setWeakPointsFilter = setWeakPointsFilter;

// Dokkai Reading (Book 2)
window.openReadingLesson = openReadingLesson;
window.closeReadingWorkspace = closeReadingWorkspace;
window.setReadingCategory = setReadingCategory;
window.selectQuizOption = selectQuizOption;
window.submitQuizAnswers = submitQuizAnswers;
window.addMissedQuestionsToSRS = addMissedQuestionsToSRS;
window.toggleSentenceTranslations = toggleSentenceTranslations;

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
  console.log('Initializing Nihongo Intermediate 5-Pillar Suite...');
  loadStats();
  
  const loadEl = document.getElementById('dash-loading-status');
  if (loadEl) loadEl.textContent = 'Loading intermediate datasets (Vocabulary & Dokkai Reading)...';

  await loadAllActiveBooks();
  
  if (loadEl) loadEl.style.display = 'none';

  updateSidebarStats();
  initSyncUI();
  showView('home');
  console.log('Nihongo Intermediate initialized successfully.');
}

window.addEventListener('DOMContentLoaded', initApp);
