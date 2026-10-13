/* =======================================================
   NIHONGO INTERMEDIATE — js/kanji-runner.js
   S0–S6 Lesson Runner Flow & Chunk State Manager (WP-5)
   Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §2.1, §2.2
   ======================================================= */

import { state as defaultState } from './state.js';
import { snapToNextDueSlot } from './time.js';
import {
  buildWordCard,
  generateDistractors,
  getFacetKey,
  FACET_READING,
  FACET_WRITING
} from './kanji-words.js';

// Configuration Constants per doc 02 §2.1 & §4.1
export const CHUNK_KANJI = 3;
export const CRITERION_CORRECT = 2; // correct answers needed in S4 to graduate
export const REQUEUE_OFFSET = 3;    // insert +3 cards later on wrong answer
export const MAX_REQUEUES = 2;       // max re-insertions per card per session
export const MIN_FIRST_GAP_MS = 4 * 60 * 60 * 1000; // 4 hours min gap for graduation nextDue

/**
 * Core Kanji Lesson Runner Engine.
 * Manages chunking, stage transitions (S0–S6), requeues, criterion loops, and graduation.
 */
export class KanjiLessonRunner {
  constructor(lessonNumber, options = {}) {
    this.lessonNumber = Number(lessonNumber) || 1;
    this.options = options;
    this.db = options.db || (typeof defaultState !== 'undefined' ? defaultState : {});
    this.stats = options.stats || (typeof defaultState !== 'undefined' && defaultState.stats ? defaultState.stats : {});
    this.onSaveStats = options.onSaveStats || null;
    this.onComplete = options.onComplete || null;

    // Lesson Data
    this.lessonKanji = [];
    this.allLessonWords = [];
    this.chunks = [];
    this.chunkIndex = 0;

    // Stage State
    this.currentStage = 'S0'; // 'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'COMPLETE'
    this.knownKanjiSet = new Set();
    this.firstTryCorrectS2 = new Set(); // words passed on first try in S2 (qualify for S5)

    // Current Active Stage Execution State
    this.queue = [];
    this.queueIdx = 0;
    this.criterionTracker = new Map(); // wordKey -> { correctCount: 0, requeues: 0 }
    this.stageResults = {
      S2: { total: 0, right: 0 },
      S3: { total: 0, right: 0 },
      S4: { total: 0, right: 0 },
      S5: { total: 0, right: 0 },
      S6: { total: 0, right: 0, missed: [] }
    };

    this.initLesson();
  }

  /**
   * Initializes lesson data and partitions kanji into chunks of 3.
   */
  initLesson() {
    const kanjiDB = this.db.kanjiDB || {};
    const wordsIndex = this.db.idx?.words || null;

    // Find all kanji belonging to this lesson
    this.lessonKanji = [];
    for (const char in kanjiDB) {
      const k = kanjiDB[char];
      if (k.lesson_number === this.lessonNumber) {
        this.lessonKanji.push(k);
      }
    }

    // Sort stably by character or original order
    this.lessonKanji.sort((a, b) => (a.order || 0) - (b.order || 0));

    // Extract all distinct target words for the lesson
    const seenWords = new Set();
    this.allLessonWords = [];

    for (const k of this.lessonKanji) {
      const words = k.words || [];
      for (const w of words) {
        const term = (w.term_ja || w.term || w.word || '').trim();
        const isTarget = Boolean(w.is_target ?? w.isTarget ?? true);
        if (term && isTarget && !seenWords.has(term)) {
          seenWords.add(term);
          // Enrich with index metadata if available
          const indexed = wordsIndex ? wordsIndex[term] : null;
          this.allLessonWords.push({
            ...w,
            term_ja: term,
            term,
            reading: w.reading || indexed?.reading || '',
            meaning_en: w.meaning_en || indexed?.meaning_en || '',
            meaning_zh: w.meaning_zh || indexed?.meaning_zh || '',
            ruby_html: w.ruby_html || indexed?.ruby_html || '',
            lesson: this.lessonNumber,
            part: k.part || 1,
            homeKanji: indexed?.homeKanji || k.kanji,
            context: indexed?.context || null
          });
        }
      }
    }

    // Partition kanji into chunks of CHUNK_KANJI (3 kanji per chunk, doc 02 §2.1)
    this.chunks = [];
    for (let i = 0; i < this.lessonKanji.length; i += CHUNK_KANJI) {
      const chunkKanjiList = this.lessonKanji.slice(i, i + CHUNK_KANJI);
      const chunkKanjiChars = new Set(chunkKanjiList.map(k => k.kanji));

      // Target words belonging to this chunk's kanji
      const chunkWords = this.allLessonWords.filter(w => {
        const kanjiInWord = (w.term_ja.match(/[\u4e00-\u9faf]/g) || []);
        return kanjiInWord.some(c => chunkKanjiChars.has(c));
      });

      this.chunks.push({
        chunkIndex: this.chunks.length,
        kanjiList: chunkKanjiList,
        targetWords: chunkWords
      });
    }

    this.chunkIndex = 0;
    this.currentStage = 'S0';
  }

  /**
   * Returns list of kanji in lesson for Placement screen (S0).
   */
  getPlacementKanji() {
    return this.lessonKanji.map(k => ({
      kanji: k.kanji,
      onyomi: k.onyomi || [],
      kunyomi: k.kunyomi || [],
      meanings: k.meanings || [k.meaning_en || ''],
      isKnown: this.knownKanjiSet.has(k.kanji)
    }));
  }

  /**
   * S0 Placement Submission (doc 02 §2.2):
   * For each kanji marked known: creates KWR records with reps=2, interval=4d, nextDue=now+4d.
   */
  submitPlacement(knownKanjiChars = []) {
    const now = Date.now();
    this.knownKanjiSet = new Set(knownKanjiChars);

    for (const char of this.knownKanjiChars || knownKanjiChars) {
      const k = this.lessonKanji.find(x => x.kanji === char);
      if (!k) continue;

      const words = k.words || [];
      for (const w of words) {
        const term = w.term_ja || w.term;
        const isTarget = Boolean(w.is_target ?? w.isTarget ?? true);
        if (term && isTarget) {
          const key = `KWR:${term}`;
          const nextDue = snapToNextDueSlot(now + 4 * 24 * 60 * 60 * 1000);
          this.stats[key] = {
            correct: 2,
            incorrect: 0,
            reps: 2,
            interval: 4,
            weight: 1.0,
            easeFactor: 2.5,
            lastSeen: now,
            nextDue,
            isHard: false
          };
        }
      }
    }

    if (this.onSaveStats) this.onSaveStats();

    // Advance to Chunk 0, S1 (or skip S1 if all kanji in chunk are known)
    this.chunkIndex = 0;
    this.startCurrentChunk();
  }

  /**
   * Skips S0 placement and starts chunk 0.
   */
  skipPlacement() {
    this.submitPlacement([]);
  }

  /**
   * Starts the current chunk at S1 (Meet).
   */
  startCurrentChunk() {
    if (this.chunkIndex >= this.chunks.length) {
      this.currentStage = 'S6';
      this.initS6LessonTest();
      return;
    }

    const chunk = this.chunks[this.chunkIndex];
    // Check if all kanji in chunk are known from S0
    const allKnown = chunk.kanjiList.every(k => this.knownKanjiSet.has(k.kanji));
    if (allKnown) {
      // Known kanji skip S1–S3, jump straight to S4 criterion check
      this.startS4Criterion();
      return;
    }

    this.startS1Meet();
  }

  /**
   * S1: Meet the chunk preview data.
   */
  startS1Meet() {
    this.currentStage = 'S1';
  }

  /**
   * Completes S1 (Meet) and advances to S2 (Recognise).
   */
  advanceFromMeet() {
    this.startS2Recognise();
  }

  /**
   * S2: Recognise (Reading MCQ: kanji -> pick kana).
   */
  startS2Recognise() {
    this.currentStage = 'S2';
    const chunk = this.chunks[this.chunkIndex];
    const words = chunk.targetWords;

    this.queue = words.map(w => {
      const card = buildWordCard(w, FACET_READING, words, this.allLessonWords);
      return {
        ...card,
        stage: 'S2',
        firstTry: true,
        requeues: 0
      };
    });

    this.queueIdx = 0;
  }

  /**
   * S3: Recall (Flashcard: kanji -> think -> flip -> grade).
   */
  startS3Recall() {
    this.currentStage = 'S3';
    const chunk = this.chunks[this.chunkIndex];
    const words = chunk.targetWords;

    this.queue = words.map(w => {
      const card = buildWordCard(w, FACET_READING, words, this.allLessonWords);
      return {
        ...card,
        stage: 'S3',
        requeues: 0
      };
    });

    this.queueIdx = 0;
  }

  /**
   * S4: Criterion (loop until every word has 2 correct, wrong -> +3 requeue).
   */
  startS4Criterion() {
    this.currentStage = 'S4';
    const chunk = this.chunks[this.chunkIndex];
    const words = chunk.targetWords;

    this.criterionTracker.clear();
    for (const w of words) {
      this.criterionTracker.set(w.term_ja, {
        correctCount: 0,
        requeues: 0,
        graduated: false,
        buried: false
      });
    }

    this.queue = words.map(w => {
      const card = buildWordCard(w, FACET_READING, words, this.allLessonWords);
      return {
        ...card,
        stage: 'S4'
      };
    });

    this.queueIdx = 0;
  }

  /**
   * S5: Writing (kana + meaning -> pick kanji for first-pass S2 words).
   */
  startS5Writing() {
    this.currentStage = 'S5';
    const chunk = this.chunks[this.chunkIndex];
    const qualifiedWords = chunk.targetWords.filter(w => this.firstTryCorrectS2.has(w.term_ja));

    if (qualifiedWords.length === 0) {
      // No words qualified for immediate writing; advance to next chunk
      this.advanceFromChunk();
      return;
    }

    this.queue = qualifiedWords.map(w => {
      const card = buildWordCard(w, FACET_WRITING, qualifiedWords, this.allLessonWords);
      return {
        ...card,
        stage: 'S5',
        requeues: 0
      };
    });

    this.queueIdx = 0;
  }

  /**
   * Advances from current chunk S5 to next chunk or S6.
   */
  advanceFromChunk() {
    this.chunkIndex++;
    if (this.chunkIndex < this.chunks.length) {
      this.startCurrentChunk();
    } else {
      this.startS6LessonTest();
    }
  }

  /**
   * S6: Lesson Test (all lesson words, mixed reading + writing, exam style).
   */
  startS6LessonTest() {
    this.currentStage = 'S6';
    this.initS6LessonTest();
  }

  initS6LessonTest() {
    // Combine Section 1 (Writing: 問題1) and Section 2 (Reading: 問題2)
    const testItems = [];

    // Section 1: Writing (kana -> kanji)
    for (const w of this.allLessonWords) {
      const card = buildWordCard(w, FACET_WRITING, this.allLessonWords, this.allLessonWords);
      testItems.push({
        ...card,
        stage: 'S6',
        section: 1,
        banner: '問題：１ (ひらがな → 正しい 漢字)'
      });
    }

    // Section 2: Reading (kanji -> kana)
    for (const w of this.allLessonWords) {
      const card = buildWordCard(w, FACET_READING, this.allLessonWords, this.allLessonWords);
      testItems.push({
        ...card,
        stage: 'S6',
        section: 2,
        banner: '問題：２ (漢字 → 正しい 読み方)'
      });
    }

    // Shuffle test items
    this.queue = testItems.sort(() => Math.random() - 0.5);
    this.queueIdx = 0;
    this.stageResults.S6 = {
      total: this.queue.length,
      right: 0,
      missed: []
    };
  }

  /**
   * Returns current active card in the current stage.
   */
  getCurrentCard() {
    if (this.queueIdx < this.queue.length) {
      return this.queue[this.queueIdx];
    }
    return null;
  }

  /**
   * Submits an answer for the current card in MCQ or Flashcard mode.
   * Handles ME-1, ME-2, ME-3, and stage graduation rules.
   */
  submitAnswer(answerOrGrade) {
    const card = this.getCurrentCard();
    if (!card) return { complete: true };

    const stage = this.currentStage;
    let isCorrect = false;

    if (stage === 'S3') {
      // Flashcard self-grade (1: Again, 2: Hard, 3: Good, 4: Easy)
      const grade = Number(answerOrGrade) || 1;
      isCorrect = (grade >= 2);
    } else {
      // MCQ auto-grade
      if (typeof answerOrGrade === 'boolean') {
        isCorrect = answerOrGrade;
      } else if (typeof answerOrGrade === 'number') {
        isCorrect = (answerOrGrade === card.correctIndex);
      } else if (typeof answerOrGrade === 'string') {
        const correctText = (card.options && card.correctIndex != null)
          ? card.options[card.correctIndex]?.text
          : (card.facet === FACET_READING ? card.reading : card.term_ja);
        isCorrect = (answerOrGrade.trim() === correctText?.trim());
      }
    }

    // ----------------------------------------------------
    // STAGE SPECIFIC HANDLERS
    // ----------------------------------------------------

    if (stage === 'S2') {
      // First-try tracking
      if (card.firstTry && isCorrect) {
        this.firstTryCorrectS2.add(card.term_ja);
      }
      card.firstTry = false;

      this.stageResults.S2.total++;
      if (isCorrect) this.stageResults.S2.right++;

      if (!isCorrect && card.requeues < MAX_REQUEUES) {
        // ME-2: Re-insert card +3 positions later
        card.requeues++;
        const insertIdx = Math.min(this.queueIdx + REQUEUE_OFFSET, this.queue.length);
        this.queue.splice(insertIdx, 0, card);
      }

      this.queueIdx++;
      if (this.queueIdx >= this.queue.length) {
        this.startS3Recall();
        return { stageAdvanced: true, nextStage: 'S3' };
      }
    } else if (stage === 'S3') {
      this.stageResults.S3.total++;
      if (isCorrect) this.stageResults.S3.right++;

      if (!isCorrect && (card.requeues || 0) < MAX_REQUEUES) {
        card.requeues = (card.requeues || 0) + 1;
        const insertIdx = Math.min(this.queueIdx + REQUEUE_OFFSET, this.queue.length);
        this.queue.splice(insertIdx, 0, card);
      }

      this.queueIdx++;
      if (this.queueIdx >= this.queue.length) {
        this.startS4Criterion();
        return { stageAdvanced: true, nextStage: 'S4' };
      }
    } else if (stage === 'S4') {
      // CRITERION LOOP (ME-2, ME-3)
      this.stageResults.S4.total++;
      const tracker = this.criterionTracker.get(card.term_ja) || { correctCount: 0, requeues: 0 };

      if (isCorrect) {
        this.stageResults.S4.right++;
        tracker.correctCount++;

        // ME-3: 2 correct answers in session graduates word from loop
        if (tracker.correctCount >= CRITERION_CORRECT) {
          tracker.graduated = true;
        } else {
          // Needs 1 more correct answer: re-append to end of queue
          this.queue.push({ ...card });
        }
      } else {
        // ME-3: Answered wrong resets count
        tracker.correctCount = 0;

        // ME-2: Re-appears 3 cards later, at most twice; third failure buries the card
        if (tracker.requeues < MAX_REQUEUES) {
          tracker.requeues++;
          const insertIdx = Math.min(this.queueIdx + REQUEUE_OFFSET, this.queue.length);
          this.queue.splice(insertIdx, 0, { ...card });
        } else {
          tracker.buried = true;
        }
      }

      this.criterionTracker.set(card.term_ja, tracker);
      this.queueIdx++;

      // Check if all words have either graduated or been buried
      const allDone = Array.from(this.criterionTracker.values()).every(t => t.graduated || t.buried);

      if (this.queueIdx >= this.queue.length || allDone) {
        // ME-1: Graduation at end of chunk's S4
        this.graduateChunkWords(this.chunks[this.chunkIndex].targetWords);
        this.startS5Writing();
        return { stageAdvanced: true, nextStage: 'S5' };
      }
    } else if (stage === 'S5') {
      this.stageResults.S5.total++;
      if (isCorrect) this.stageResults.S5.right++;

      if (!isCorrect && (card.requeues || 0) < MAX_REQUEUES) {
        card.requeues = (card.requeues || 0) + 1;
        const insertIdx = Math.min(this.queueIdx + REQUEUE_OFFSET, this.queue.length);
        this.queue.splice(insertIdx, 0, card);
      }

      this.queueIdx++;
      if (this.queueIdx >= this.queue.length) {
        this.advanceFromChunk();
        return { stageAdvanced: true, nextStage: this.currentStage };
      }
    } else if (stage === 'S6') {
      this.stageResults.S6.total++;
      if (isCorrect) {
        this.stageResults.S6.right++;
      } else {
        // End of lesson test: word with error gets lapses += 1 and weight raised (doc 02 §2.1)
        this.stageResults.S6.missed.push(card.term_ja);
        const facetKey = getFacetKey(card.facet, card.term_ja);
        const s = this.stats[facetKey] || { reps: 1, correct: 1, incorrect: 0 };
        s.lapses = (s.lapses || 0) + 1;
        s.weight = Math.min(2.5, (s.weight || 1.0) * 1.5);
        s.incorrect = (s.incorrect || 0) + 1;
        this.stats[facetKey] = s;
      }

      this.queueIdx++;
      if (this.queueIdx >= this.queue.length) {
        this.currentStage = 'COMPLETE';
        if (this.onSaveStats) this.onSaveStats();
        if (this.onComplete) this.onComplete(this.getSummary());
        return { stageAdvanced: true, nextStage: 'COMPLETE', isComplete: true };
      }
    }

    return {
      isCorrect,
      stage: this.currentStage,
      queueIdx: this.queueIdx,
      queueTotal: this.queue.length
    };
  }

  /**
   * ME-1: Chunk Graduation:
   * When S4 completes, each target word's KWR record is created with reps=1
   * and nextDue at the next legal slot at least 4 hours away.
   */
  graduateChunkWords(words) {
    const now = Date.now();
    for (const w of words) {
      const term = w.term_ja || w.term;
      const key = `KWR:${term}`;
      const existing = this.stats[key] || {};

      this.stats[key] = {
        correct: (existing.correct || 0) + 1,
        incorrect: existing.incorrect || 0,
        reps: 1,
        interval: 0,
        weight: existing.weight || 1.0,
        easeFactor: existing.easeFactor || 2.5,
        lastSeen: now,
        nextDue: snapToNextDueSlot(now + MIN_FIRST_GAP_MS),
        isHard: Boolean(existing.isHard)
      };
    }

    if (this.onSaveStats) this.onSaveStats();
  }

  /**
   * Returns comprehensive runner results summary.
   */
  getSummary() {
    const s6 = this.stageResults.S6;
    const accuracy = s6.total > 0 ? Math.round((s6.right / s6.total) * 100) : 100;

    return {
      lessonNumber: this.lessonNumber,
      totalChunks: this.chunks.length,
      knownKanjiCount: this.knownKanjiSet.size,
      totalWordsLearned: this.allLessonWords.length,
      stageResults: this.stageResults,
      accuracyPct: accuracy,
      missedWords: Array.from(new Set(s6.missed)),
      isComplete: this.currentStage === 'COMPLETE'
    };
  }
}

/**
 * Factory to create a KanjiLessonRunner.
 */
export function createLessonRunner(lessonNumber, options = {}) {
  return new KanjiLessonRunner(lessonNumber, options);
}

// =======================================================
// BROWSER UI INTEGRATION & INTERACTIVE RUNNER
// =======================================================

let activeRunner = null;

/**
 * Launches the interactive S0–S6 Lesson Runner in the browser.
 */
export function startKanjiRunner(lessonNumber, containerId = 'view-study') {
  activeRunner = createLessonRunner(lessonNumber, {
    db: defaultState,
    stats: defaultState.stats,
    onSaveStats: () => {
      if (typeof window !== 'undefined' && window.saveStats) window.saveStats();
    },
    onComplete: (summary) => {
      renderRunnerResults(summary);
    }
  });

  renderRunnerStage();
}

/**
 * Master UI renderer based on runner's currentStage.
 */
export function renderRunnerStage() {
  if (!activeRunner) return;

  const stage = activeRunner.currentStage;
  if (stage === 'S0') {
    renderS0PlacementUI();
  } else if (stage === 'S1') {
    renderS1MeetUI();
  } else if (stage === 'S2' || stage === 'S4' || stage === 'S5' || stage === 'S6') {
    renderMCQStageUI();
  } else if (stage === 'S3') {
    renderS3RecallUI();
  } else if (stage === 'COMPLETE') {
    renderRunnerResults(activeRunner.getSummary());
  }
}

function getRunnerContainer() {
  let el = document.getElementById('kanji-runner-container');
  if (!el) {
    const parent = document.getElementById('view-study') || document.body;
    el = document.createElement('div');
    el.id = 'kanji-runner-container';
    el.className = 'kanji-runner-workspace';
    parent.innerHTML = '';
    parent.appendChild(el);
  }
  return el;
}

function renderS0PlacementUI() {
  const container = getRunnerContainer();
  const kanjiList = activeRunner.getPlacementKanji();

  let html = `
    <div class="kr-card kr-placement-card">
      <div class="kr-top-bar">
        <button class="btn btn-sm btn-ghost" onclick="exitKanjiRunner()"><i class="fa-solid fa-arrow-left"></i> Exit</button>
        <span class="badge badge-purple">S0 · Placement (Lesson ${activeRunner.lessonNumber})</span>
        <button class="btn btn-sm btn-secondary" onclick="skipPlacement()">Skip</button>
      </div>

      <div class="kr-hero-text">
        <h2 style="font-size: 1.35rem; color: #fff;">Tap the kanji you already know</h2>
        <p style="color: var(--text-dim); font-size: 0.9rem;">Known kanji skip introductory drills and enter SRS with early verification.</p>
      </div>

      <div class="kr-placement-grid">
        ${kanjiList.map(k => `
          <button class="kr-placement-tile ${k.isKnown ? 'active' : ''}" id="tile-k-${k.kanji}" onclick="togglePlacementKanji('${k.kanji}')">
            <span class="kr-tile-char font-ja">${k.kanji}</span>
            <span class="kr-tile-sub">${k.meanings[0] || ''}</span>
          </button>
        `).join('')}
      </div>

      <div class="kr-footer-actions">
        <button class="btn btn-primary btn-block" onclick="confirmPlacement()">Confirm &amp; Start Lesson (${activeRunner.knownKanjiSet.size} known)</button>
      </div>
    </div>
  `;

  container.innerHTML = html;
}

export function togglePlacementKanji(char) {
  if (!activeRunner) return;
  if (activeRunner.knownKanjiSet.has(char)) {
    activeRunner.knownKanjiSet.delete(char);
  } else {
    activeRunner.knownKanjiSet.add(char);
  }
  const tile = document.getElementById(`tile-k-${char}`);
  if (tile) tile.classList.toggle('active', activeRunner.knownKanjiSet.has(char));
}

export function confirmPlacement() {
  if (!activeRunner) return;
  activeRunner.submitPlacement(Array.from(activeRunner.knownKanjiSet));
  renderRunnerStage();
}

export function skipPlacement() {
  if (!activeRunner) return;
  activeRunner.skipPlacement();
  renderRunnerStage();
}

function renderS1MeetUI() {
  const container = getRunnerContainer();
  const chunk = activeRunner.chunks[activeRunner.chunkIndex];

  let html = `
    <div class="kr-card kr-meet-card">
      <div class="kr-top-bar">
        <button class="btn btn-sm btn-ghost" onclick="exitKanjiRunner()"><i class="fa-solid fa-arrow-left"></i> Hub</button>
        <span class="badge badge-cyan">S1 · Meet Chunk ${activeRunner.chunkIndex + 1} of ${activeRunner.chunks.length}</span>
        <span style="font-size: 0.85rem; color: var(--text-dim);">${chunk.targetWords.length} Words</span>
      </div>

      <div class="kr-chunk-kanji-strip">
        ${chunk.kanjiList.map(k => `
          <div class="kr-chunk-kanji-pill">
            <span class="kr-ck-char font-ja">${k.kanji}</span>
            <span class="kr-ck-mean">${k.meanings ? k.meanings[0] : (k.meaning_en || '')}</span>
          </div>
        `).join('')}
      </div>

      <div class="kr-words-preview-list">
        ${chunk.targetWords.map(w => `
          <div class="kr-word-row">
            <div class="kr-word-header">
              <span class="font-ja kr-ruby">${w.ruby_html || w.term_ja}</span>
              <span class="kr-meaning">${w.meaning_en}</span>
            </div>
            ${w.context?.ja ? `
              <div class="kr-context-ja font-ja">${w.context.ja}</div>
              <div class="kr-context-en">${w.context.en || ''}</div>
            ` : ''}
          </div>
        `).join('')}
      </div>

      <div class="kr-footer-actions">
        <button class="btn btn-primary btn-block" onclick="advanceFromMeetUI()">Got it, quiz me! <i class="fa-solid fa-arrow-right"></i></button>
      </div>
    </div>
  `;

  container.innerHTML = html;
}

export function advanceFromMeetUI() {
  if (!activeRunner) return;
  activeRunner.advanceFromMeet();
  renderRunnerStage();
}

function renderMCQStageUI() {
  const container = getRunnerContainer();
  const card = activeRunner.getCurrentCard();
  if (!card) return;

  const stage = activeRunner.currentStage;
  const isReading = card.facet === FACET_READING;

  let html = `
    <div class="kr-card kr-mcq-card">
      <div class="kr-top-bar">
        <button class="btn btn-sm btn-ghost" onclick="exitKanjiRunner()"><i class="fa-solid fa-arrow-left"></i></button>
        <span class="badge badge-purple">${stage} · ${stage === 'S6' ? 'Lesson Exam' : `Chunk ${activeRunner.chunkIndex + 1}`}</span>
        <span style="font-size: 0.85rem; color: var(--text-dim);">${activeRunner.queueIdx + 1} / ${activeRunner.queue.length}</span>
      </div>

      <div class="kr-banner-strip">${card.banner || ''}</div>

      <div class="kr-prompt-area">
        ${isReading ? `
          <div class="kr-prompt-word font-ja">${card.term_ja}</div>
        ` : `
          <div class="kr-prompt-word font-ja" style="font-size: 2.2rem;">${card.reading}</div>
          <div class="kr-sub-prompt">[ ${card.meaning_en} ]</div>
        `}
      </div>

      <div class="kr-mcq-grid" id="kr-options-grid">
        ${(card.options || []).map((opt, idx) => `
          <button class="kr-opt-btn" onclick="selectMCQAnswer(${idx})">
            <span class="kr-opt-letter">${idx + 1}.</span>
            <span class="font-ja kr-opt-text">${opt.text}</span>
          </button>
        `).join('')}
      </div>

      <div id="kr-feedback-box" class="kr-feedback-box hide"></div>
    </div>
  `;

  container.innerHTML = html;
}

export function selectMCQAnswer(selectedIdx) {
  if (!activeRunner) return;
  const card = activeRunner.getCurrentCard();
  if (!card) return;

  const isCorrect = (selectedIdx === card.correctIndex);
  const btns = document.querySelectorAll('.kr-opt-btn');
  btns.forEach((btn, idx) => {
    btn.disabled = true;
    if (idx === card.correctIndex) {
      btn.classList.add('correct');
    } else if (idx === selectedIdx && !isCorrect) {
      btn.classList.add('incorrect');
    }
  });

  const fb = document.getElementById('kr-feedback-box');
  if (fb) {
    fb.classList.remove('hide');
    fb.className = `kr-feedback-box ${isCorrect ? 'correct' : 'incorrect'}`;
    fb.innerHTML = isCorrect
      ? `<div><strong><i class="fa-solid fa-circle-check"></i> 正解！</strong> ${card.ruby_html} · ${card.meaning_en}</div>`
      : `<div><strong><i class="fa-solid fa-circle-xmark"></i> 不正解</strong> 正解: <span class="font-ja">${card.options[card.correctIndex]?.text}</span> (${card.meaning_en})</div>`;
  }

  setTimeout(() => {
    activeRunner.submitAnswer(selectedIdx);
    renderRunnerStage();
  }, isCorrect ? 500 : 1200);
}

function renderS3RecallUI() {
  const container = getRunnerContainer();
  const card = activeRunner.getCurrentCard();
  if (!card) return;

  let html = `
    <div class="kr-card kr-recall-card" id="kr-recall-card" onclick="flipRecallCard()">
      <div class="kr-top-bar">
        <button class="btn btn-sm btn-ghost" onclick="exitKanjiRunner()"><i class="fa-solid fa-arrow-left"></i></button>
        <span class="badge badge-amber">S3 · Recall Flashcard</span>
        <span style="font-size: 0.85rem; color: var(--text-dim);">${activeRunner.queueIdx + 1} / ${activeRunner.queue.length}</span>
      </div>

      <div class="kr-prompt-area">
        <div class="kr-prompt-word font-ja">${card.term_ja}</div>
        <div class="kr-sub-prompt" id="kr-fc-hint"><i class="fa-solid fa-hand-pointer"></i> Tap to flip</div>
      </div>

      <div id="kr-fc-back" class="kr-fc-back hide">
        <div class="kr-reading-ans font-ja">${card.reading}</div>
        <div class="kr-meaning-ans">${card.meaning_en}</div>

        ${card.breakdown && card.breakdown.length > 0 ? `
          <div class="kr-breakdown-strip">
            ${card.breakdown.map(b => `
              <div class="kr-pill">
                <span class="font-ja">${b.kanji}</span>
                <span>${b.meaning}</span>
              </div>
            `).join('<span class="kr-plus">+</span>')}
          </div>
        ` : ''}

        ${card.context?.ja ? `
          <div class="kr-context-box">
            <div class="font-ja">${card.context.ja}</div>
            <div>${card.context.en || ''}</div>
          </div>
        ` : ''}
      </div>

      <div id="kr-grade-strip" class="kr-grade-strip hide" onclick="event.stopPropagation()">
        <button class="btn btn-grade btn-again" onclick="gradeRecallCard(1)">Again (1)</button>
        <button class="btn btn-grade btn-hard" onclick="gradeRecallCard(2)">Hard (2)</button>
        <button class="btn btn-grade btn-good" onclick="gradeRecallCard(3)">Good (3)</button>
        <button class="btn btn-grade btn-easy" onclick="gradeRecallCard(4)">Easy (4)</button>
      </div>
    </div>
  `;

  container.innerHTML = html;
}

export function flipRecallCard() {
  const back = document.getElementById('kr-fc-back');
  const grades = document.getElementById('kr-grade-strip');
  const hint = document.getElementById('kr-fc-hint');

  if (back && grades) {
    const isFlipped = back.classList.contains('hide');
    back.classList.toggle('hide', !isFlipped);
    grades.classList.toggle('hide', !isFlipped);
    if (hint) hint.style.display = isFlipped ? 'none' : 'block';
  }
}

export function gradeRecallCard(grade) {
  if (!activeRunner) return;
  activeRunner.submitAnswer(grade);
  renderRunnerStage();
}

function renderRunnerResults(summary) {
  const container = getRunnerContainer();

  let html = `
    <div class="kr-card kr-results-card">
      <div class="kr-results-hero">
        <i class="fa-solid fa-trophy" style="font-size: 3rem; color: #fbbf24; margin-bottom: 0.75rem;"></i>
        <h2 style="font-size: 1.6rem; color: #fff;">Lesson ${summary.lessonNumber} Complete!</h2>
        <div style="font-size: 2.2rem; font-weight: 800; color: var(--green); margin: 0.5rem 0;">
          ${summary.accuracyPct}%
        </div>
        <p style="color: var(--text-dim); font-size: 0.95rem;">
          ${summary.totalWordsLearned} words graduated to active SRS scheduling.
        </p>
      </div>

      ${summary.missedWords && summary.missedWords.length > 0 ? `
        <div class="kr-missed-box">
          <h4 style="color: #f87171; font-size: 0.95rem; margin-bottom: 0.5rem;">
            <i class="fa-solid fa-triangle-exclamation"></i> Words needing reinforcement (${summary.missedWords.length})
          </h4>
          <div class="kr-missed-tags">
            ${summary.missedWords.map(w => `<span class="badge badge-red font-ja">${w}</span>`).join(' ')}
          </div>
        </div>
      ` : ''}

      <div class="kr-footer-actions" style="margin-top: 1.5rem;">
        <button class="btn btn-primary btn-block" onclick="exitKanjiRunner()">
          Return to Kanji Hub <i class="fa-solid fa-shapes"></i>
        </button>
      </div>
    </div>
  `;

  container.innerHTML = html;
}

export function exitKanjiRunner() {
  activeRunner = null;
  const container = document.getElementById('kanji-runner-container');
  if (container) container.remove();

  if (typeof window !== 'undefined') {
    if (window.renderKanjiView) window.renderKanjiView();
    if (window.showView) window.showView('kanji');
  }
}

export const N3KanjiRunner = {
  CHUNK_KANJI,
  CRITERION_CORRECT,
  REQUEUE_OFFSET,
  MAX_REQUEUES,
  MIN_FIRST_GAP_MS,
  KanjiLessonRunner,
  createLessonRunner,
  startKanjiRunner,
  renderRunnerStage,
  togglePlacementKanji,
  confirmPlacement,
  skipPlacement,
  advanceFromMeetUI,
  selectMCQAnswer,
  flipRecallCard,
  gradeRecallCard,
  exitKanjiRunner
};

if (typeof window !== 'undefined') {
  window.N3KanjiRunner = N3KanjiRunner;
}

export default N3KanjiRunner;
