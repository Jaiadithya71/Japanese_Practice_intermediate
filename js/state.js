/* =======================================================
   NIHONGO INTERMEDIATE — state.js
   Central Application State Management
   ======================================================= */

export const state = {
  // Vocabulary Database (keyed by chapter id, e.g. "part1_01", "part2_05")
  vocabDB: {},
  chapterMetadata: {},

  // User Stats (SRS intervals, review history, weights)
  stats: {},

  // Navigation & Selection
  currentView: 'home',
  selectedChapters: new Set(),
  activeChapterGroup: 'topic', // 'topic' (Ch 1-21) | 'characteristics' (Ch 1-8)

  // Vocab Browser State
  vocabChapter: 'all',
  vocabFilter: 'all', // 'all' | 'learning' | 'hard' | 'mastered'
  vocabSearchQuery: '',
  showFurigana: true,
  selectedHardChapters: new Set(),
  hardWordsDirection: 'ja-en',

  // Study Session State
  studyMode: 'flashcard',
  sessionWords: [],
  sessionIdx: 0,
  sessionRight: 0,
  sessionTotal: 0,
  cardFlipped: false,
  studyDirection: 'ja-en',
  isDueReviewMode: false,
  studyIsDrillHard: false,
  drillOrigin: 'home',

  // Due Review Settings
  dueBatchSize: '20'
};
