/* =======================================================
   NIHONGO INTERMEDIATE — state.js
   Central Application State Management (5-Pillar Architecture)
   ======================================================= */

export const state = {
  // 5 PILLARS DATA REPOSITORIES
  vocabDB: {},           // Book 1: Vocabulary (29 units, 1,251 words)
  chapterMetadata: {},

  readingDB: {},         // Book 2: Reading Comprehension (54 lessons, 90+ questions)
  readingCategories: {}, // Categorized lesson IDs

  grammarDB: {},         // Book 3: Grammar (Staged)
  kanjiDB: {},           // Book 4: Kanji (Staged)
  listeningDB: {},       // Book 5: Listening (Staged)

  // User Stats (Unified SRS for Vocab, Reading Questions, Grammar, etc.)
  stats: {},

  // Navigation & View State
  currentView: 'home',
  activePillar: 'vocab',
  selectedChapters: new Set(),
  activeChapterGroup: 'topic', // 'topic' (Ch 1-21) | 'characteristics' (Ch 1-8)

  // Vocab Browser State
  vocabChapter: 'all',
  vocabFilter: 'all', // 'all' | 'learning' | 'hard' | 'mastered'
  vocabSearchQuery: '',
  showFurigana: true,
  selectedHardChapters: new Set(),
  hardWordsDirection: 'ja-en',

  // Dokkai Reading State (Book 2)
  readingCategory: 'all', // 'all' | 'foundation' | 'strategy' | 'real_short' | 'real_medium' | 'real_long' | 'info'
  activeReadingLesson: null,
  showSentenceTranslations: false,
  readingAnswers: {},    // { [questionId]: selectedOption }
  readingQuizSubmitted: false,

  // Universal Weak Points State
  weakPointsFilter: 'all', // 'all' | 'vocab' | 'reading' | 'grammar' | 'kanji'

  // Study Session State (Active Recall & Omni-Review)
  studyMode: 'flashcard',
  sessionItems: [],      // Can contain Vocab words OR Dokkai questions OR Grammar rules
  sessionIdx: 0,
  sessionRight: 0,
  sessionTotal: 0,
  cardFlipped: false,
  studyDirection: 'ja-en',
  isDueReviewMode: false,
  studyIsDrillHard: false,
  drillOrigin: 'home',
  omniDueFilter: 'all',  // 'all' | 'vocab' | 'reading'

  // Due Review Settings
  dueBatchSize: '20'
};
