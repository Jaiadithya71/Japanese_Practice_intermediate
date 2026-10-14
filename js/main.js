/* =======================================================
   NIHONGO INTERMEDIATE — main.js
   Application Entry Point & Global Bindings (5-Pillar Architecture)
   ======================================================= */

import { state } from './state.js';
import { loadAllActiveBooks } from './data-loader.js';
import { loadStats, updateSidebarStats, toggleWordHard } from './srs.js';
import { showView } from './navigation.js';
import { startStudy, startLearnNew, learnGotIt, skipCard, startDueReview, startOmniReview, flipCard, gradeCard, exitStudy, playCurrentCardAudio, toggleCurrentCardHard } from './study.js';
import { setChapterGroup, selectChapter, setVocabFilter, onVocabSearch, toggleFurigana, playAudio, onToggleHard, drillAllHardWords, toggleRevealHardWords, setWeakPointsFilter, drillVocabSelected, toggleVocabMultiSelectMode } from './vocab-browser.js?v=2.4';
import { setHomeGroup, toggleChapterSelection, selectAllChaptersInGroup, clearChapterSelection, renderHomeView, setHomeSessionSize, setHomeStudyDirection, startSelectedLessonRun, startNextHomeBatch, renderHomeActivity } from './home.js?v=2.6';
import { openReadingLesson, closeReadingWorkspace, setReadingCategory, selectQuizOption, submitQuizAnswers, addMissedQuestionsToSRS, toggleSentenceTranslations } from './reader.js';
import { scheduleGistSave, openSyncSetup, closeSyncSetup, connectGist, forceSyncNow, disconnectGist, initSyncUI } from './gist-sync.js';
import {
  renderKanjiView, setKanjiTab, setKanjiPart, setKanjiLesson, setKanjiFilter, onKanjiSearch,
  openKanjiModal, closeKanjiModal, toggleModalKanjiHard, drillActiveModalKanji,
  drillKanjiSingle, drillKanjiLesson, getKanjiBreakdown, setExerciseLesson,
  selectExerciseOption, checkExerciseInput, drillExerciseItem, checkMockOption,
  setKanjiStudyDirection, selectKanjiLesson, drillKanjiSelected,
  startKanjiQuickQuiz, renderKanjiQuizCard, answerKanjiQuizOption,
  nextKanjiQuizCard, toggleKanjiAutoNext
} from './kanji.js?v=2.5';
import { startKanjiRunner } from './kanji-runner.js';
import {
  initTestHub, startTestSession, submitQuestionAnswer, advanceTestQuestion,
  exitTestToHub, filterTestCategory, getAllAvailableTests
} from './test.js';

// New Foundation & Memory Engine Modules (WP-0 to WP-5)
import './backup.js';
import './time.js';
import './daylog.js';
import { buildIndexes } from './indexes.js';
import './session.js';
import './planner.js';
import './kanji-words.js';

// Releases R2, R3, R4 Modules (WP-6 to WP-12)
import './daily.js';
import './today.js';
import './reading-types.js';
import './grammar-srs.js';
import './me-tab.js';
import './class-curriculum.js';
import './book-platform.js';

// Expose controllers to window for HTML event handlers
window.state = state;
window.showView = showView;
window.initTestHub = initTestHub;
window.startTestSession = startTestSession;
window.submitQuestionAnswer = submitQuestionAnswer;
window.advanceTestQuestion = advanceTestQuestion;
window.exitTestToHub = exitTestToHub;
window.filterTestCategory = filterTestCategory;

// Optional Gist sync
window.__n3ScheduleSync = scheduleGistSave;
window.openSyncSetup = openSyncSetup;
window.closeSyncSetup = closeSyncSetup;
window.connectGist = connectGist;
window.forceSyncNow = forceSyncNow;
window.disconnectGist = disconnectGist;

// Study & Multi-Pillar Omni-Review
window.startStudy = startStudy;
window.startLearnNew = startLearnNew;
window.learnGotIt = learnGotIt;
window.skipCard = skipCard;
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
window.drillVocabSelected = drillVocabSelected;
window.toggleVocabMultiSelectMode = toggleVocabMultiSelectMode;

// Dokkai Reading (Book 2)
window.openReadingLesson = openReadingLesson;
window.closeReadingWorkspace = closeReadingWorkspace;
window.setReadingCategory = setReadingCategory;
window.selectQuizOption = selectQuizOption;
window.submitQuizAnswers = submitQuizAnswers;
window.addMissedQuestionsToSRS = addMissedQuestionsToSRS;
window.toggleSentenceTranslations = toggleSentenceTranslations;

// Kanji (Book 4)
window.renderKanjiView = renderKanjiView;
window.setKanjiTab = setKanjiTab;
window.setKanjiPart = setKanjiPart;
window.setKanjiLesson = setKanjiLesson;
window.setKanjiFilter = setKanjiFilter;
window.onKanjiSearch = onKanjiSearch;
window.openKanjiModal = openKanjiModal;
window.closeKanjiModal = closeKanjiModal;
window.toggleModalKanjiHard = toggleModalKanjiHard;
window.drillActiveModalKanji = drillActiveModalKanji;
window.drillKanjiSingle = drillKanjiSingle;
window.drillKanjiLesson = drillKanjiLesson;
window.getKanjiBreakdown = getKanjiBreakdown;
window.setExerciseLesson = setExerciseLesson;
window.selectExerciseOption = selectExerciseOption;
window.checkExerciseInput = checkExerciseInput;
window.drillExerciseItem = drillExerciseItem;
window.checkMockOption = checkMockOption;
window.setKanjiStudyDirection = setKanjiStudyDirection;
window.selectKanjiLesson = selectKanjiLesson;
window.drillKanjiSelected = drillKanjiSelected;
window.startKanjiQuickQuiz = startKanjiQuickQuiz;
window.renderKanjiQuizCard = renderKanjiQuizCard;
window.answerKanjiQuizOption = answerKanjiQuizOption;
window.nextKanjiQuizCard = nextKanjiQuizCard;
window.toggleKanjiAutoNext = toggleKanjiAutoNext;
window.startKanjiRunner = startKanjiRunner;
window.startKanjiLessonRunner = () => {
  const selected = Array.from(state.kanjiSelectedLessons || []);
  if (selected.length !== 1) {
    alert('Select exactly one lesson chip to start the guided lesson.');
    return;
  }
  startKanjiRunner(Number(selected[0]));
};

// Home Dashboard
window.setHomeGroup = setHomeGroup;
window.toggleChapterSelection = toggleChapterSelection;
window.selectAllChaptersInGroup = selectAllChaptersInGroup;
window.clearChapterSelection = clearChapterSelection;
window.setHomeSessionSize = setHomeSessionSize;
window.setHomeStudyDirection = setHomeStudyDirection;
window.startSelectedLessonRun = startSelectedLessonRun;
window.startNextHomeBatch = startNextHomeBatch;
window.renderHomeActivity = renderHomeActivity;

// Global Keyboard Shortcuts
window.addEventListener('keydown', (e) => {
  if (state.currentView === 'study') {
    if (e.code === 'Space') {
      e.preventDefault();
      flipCard();
    } else if (state.studyMode === 'kanji_quiz' && ['Digit1', 'Digit2', 'Digit3', 'Digit4'].includes(e.code)) {
      e.preventDefault();
      const idx = parseInt(e.code.replace('Digit', ''), 10) - 1;
      answerKanjiQuizOption(idx);
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
  window.N3Indexes = buildIndexes(state.db);
  
  if (loadEl) {
    loadEl.textContent = '';
    loadEl.style.display = 'none';
  }

  const testNavBadge = document.getElementById('nav-test-count');
  if (testNavBadge) {
    const totalQ = getAllAvailableTests().reduce((acc, t) => acc + t.questionCount, 0);
    testNavBadge.textContent = `${totalQ} Qs`;
  }

  updateSidebarStats();
  showView('home');
  initSyncUI();
  console.log('Nihongo Intermediate initialized successfully.');
}

import './pillar-banner.js?v=1';

window.addEventListener('DOMContentLoaded', initApp);
