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

  grammarDB: {
    index: [],
    intro: {},
    part1_1_6: {},
    part1_7_12: {},
    part2: {},
    part3: {},
    mock: {}
  },
  grammarActiveTab: 'patterns', // 'patterns' | 'drills' | 'star' | 'text' | 'mock' | 'guide'
  grammarFilterPart: 'all',
  grammarSearchQuery: '',
  grammarCurrentSection: 'all',
  grammarSelectedAnswers: {},
  grammarShowNuances: true,
  kanjiDB: {},           // Book 4: Kanji Target DB (443 Kanji)
  kanjiLessons: [],      // Book 4: Lessons List (Lessons 01-25)
  kanjiExercisesDB: {},  // Book 4: Practice Exercises
  kanjiReview300: [],    // Book 4: Bessatsu 300 N4/N5 Kanji
  kanjiSpecialReadings: [], // Book 4: Bessatsu Special Readings (21 items)
  kanjiMockTests: [],    // Book 4: Mock Tests 1 & 2
  listeningDB: {},       // Book 5: Listening (Staged)

  // Book 4: Kanji Browser & Workspace State
  kanjiActiveTab: 'target', // 'target' | 'exercises' | 'review300' | 'special' | 'mock'
  kanjiPart: 'all',         // 'all' | 1 | 2 | 3 | 4 | 5
  kanjiLesson: 'all',       // 'all' | 1 .. 25
  kanjiFilter: 'all',       // 'all' | 'learning' | 'hard' | 'mastered' | 'unseen'
  kanjiSearchQuery: '',
  kanjiExerciseLesson: 1,   // Active exercise lesson
  kanjiExerciseAnswers: {}, // { [itemId]: answer }
  activeKanjiModal: null,

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
  sessionSkipped: 0,
  learnUnit: null,
  studyDirection: 'ja-en',
  isDueReviewMode: false,
  studyIsDrillHard: false,
  drillOrigin: 'home',
  omniDueFilter: 'all',  // 'all' | 'vocab' | 'reading'

  // Due Review Settings
  dueBatchSize: '20'
};
