/* =======================================================
   NIHONGO INTERMEDIATE — study.js
   Active Recall & Omni-Review Flashcard Engine (Multi-Pillar)
   ======================================================= */

import { state } from './state.js';
import { updateItemStats, toggleItemHard, getItemStatus, getAllDueItems, formatItemKey } from './srs.js';
import { showView } from './navigation.js';

export function startStudy(mode = 'flashcard', isDrillHard = false, origin = 'home') {
  state.studyMode = mode;
  state.studyIsDrillHard = isDrillHard;
  state.drillOrigin = origin;
  state.isDueReviewMode = false;
  state.learnUnit = null;
  state.sessionSkipped = 0;

  const pool = [];
  const chaptersToUse = state.selectedChapters.size > 0 
    ? Array.from(state.selectedChapters) 
    : Object.keys(state.vocabDB);

  for (const chId of chaptersToUse) {
    for (const w of (state.vocabDB[chId] || [])) {
      const itemKey = `V:${w.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
      if (isDrillHard) {
        if (getItemStatus(itemKey) === 'hard') {
          pool.push({ ...w, type: 'vocab', key: itemKey, book: 'vocab' });
        }
      } else {
        pool.push({ ...w, type: 'vocab', key: itemKey, book: 'vocab' });
      }
    }
  }

  if (pool.length === 0) {
    alert(isDrillHard ? 'No hard items found in selected chapters!' : 'No items found in selected chapters!');
    return;
  }

  // Shuffle pool
  pool.sort(() => Math.random() - 0.5);

  const batchSize = pool.length; // run every word in the selection
  state.sessionItems = pool.slice(0, batchSize);
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = state.sessionItems.length;
  state.sessionTotal = state.sessionItems.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

export function startDueReview(pillarFilter = 'all', chapterFilter = null) {
  state.omniDueFilter = pillarFilter;

  // Use explicit chapterFilter or active selection from state
  if (!chapterFilter) {
    if (pillarFilter === 'vocab') {
      if (state.selectedDueVocabChapters && state.selectedDueVocabChapters.size > 0) {
        chapterFilter = state.selectedDueVocabChapters;
      } else if (state.selectedVocabChapters && state.selectedVocabChapters.size > 0 && state.vocabChapter !== 'all') {
        chapterFilter = state.selectedVocabChapters;
      }
    } else if (pillarFilter === 'kanji') {
      if (state.selectedDueKanjiLessons && state.selectedDueKanjiLessons.size > 0) {
        chapterFilter = state.selectedDueKanjiLessons;
      } else if (state.kanjiSelectedLessons && state.kanjiSelectedLessons.size > 0) {
        chapterFilter = state.kanjiSelectedLessons;
      }
    }
  }

  const pool = getAllDueItems(pillarFilter, state.dueBatchSize, chapterFilter);

  if (pool.length === 0) {
    alert('No due items right now for this filter! Great job staying caught up.');
    return;
  }

  state.studyMode = 'flashcard';
  state.studyIsDrillHard = false;
  state.learnUnit = null;
  state.sessionSkipped = 0;
  state.isDueReviewMode = true;
  state.drillOrigin = 'home';
  state.sessionItems = pool;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = pool.length;
  state.sessionTotal = pool.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

const seenIt = st => !!st && (st.reps > 0 || st.correct > 0 || st.incorrect > 0);

// Learn new words: teach (meaning first), then quiz. Skipped words stay unseen.
export function startLearnNew(unitId, count = 10) {
  const words = (state.vocabDB[unitId] || []).filter(w => !seenIt(state.stats[`V:${w.id}`]));
  if (words.length === 0) {
    alert('No new words left in this unit.');
    return;
  }
  const pool = words.slice(0, count).map(w => ({
    ...w, type: 'vocab', book: 'vocab', key: `V:${w.id}`, learnNew: true, learned: false
  }));
  state.studyMode = 'flashcard';
  state.studyIsDrillHard = false;
  state.isDueReviewMode = false;
  state.drillOrigin = 'home';
  state.learnUnit = unitId;
  state.sessionSkipped = 0;
  state.sessionItems = pool;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = pool.length;
  state.cardFlipped = false;
  showView('study');
  renderCard();
}

export function learnGotIt() {
  const item = state.sessionItems[state.sessionIdx];
  if (!item || !item.learnNew || item.learned) return;
  item.learned = true;
  state.cardFlipped = false;
  renderCard();
}

export function skipCard() {
  if (state.sessionIdx >= state.sessionTotal) return;
  state.sessionSkipped = (state.sessionSkipped || 0) + 1;
  state.sessionIdx++;
  state.cardFlipped = false;
  renderCard();
}

function isLearnStage(item) {
  return !!item && item.learnNew && !item.learned;
}

export function startOmniReview() {
  startDueReview('all');
}

export function renderCard() {
  if (state.sessionIdx >= state.sessionItems.length) {
    renderStudySummary();
    return;
  }

  // After a summary screen the flashcard DOM is gone - rebuild it before rendering
  if (!document.getElementById('card-term')) {
    resetStudyViewHTML();
  }

  const item = state.sessionItems[state.sessionIdx];
  const itemKey = formatItemKey(item);
  const isHard = getItemStatus(itemKey) === 'hard';
  const skipRow = document.getElementById('study-skip-row');
  if (skipRow) skipRow.style.display = 'flex';

  // Progress Bar & Live Counters
  const fill = document.getElementById('study-progress-fill');
  const count = document.getElementById('study-progress-count');
  const correctEl = document.getElementById('session-correct');
  const totalEl = document.getElementById('session-total');

  const curIdx = state.sessionIdx + 1;
  const totalCards = state.sessionItems.length;
  const pct = Math.min(100, Math.round(((state.sessionIdx) / totalCards) * 100));

  if (fill) fill.style.width = `${pct}%`;
  if (count) count.textContent = `${Math.min(curIdx, totalCards)} / ${totalCards}`;
  if (correctEl) correctEl.textContent = state.sessionRight || 0;
  if (totalEl) totalEl.textContent = state.sessionTotalAnswered || 0;

  const flameBtn = document.getElementById('card-hard-flame');
  if (flameBtn) {
    flameBtn.className = `btn-hard-flame${isHard ? ' is-hard' : ''}`;
  }

  const lessonTag = document.getElementById('card-lesson-tag');
  const termEl = document.getElementById('card-term');
  const meaningEl = document.getElementById('card-meaning');
  const exBox = document.getElementById('card-example-box');
  const exJa = document.getElementById('card-ex-ja');
  const exEn = document.getElementById('card-ex-en');

  // ==========================================
  // CASE 0: KANJI QUICK QUIZ (MCQ fast drill)
  // Renderer lives in kanji.js; dispatched via window to avoid an import cycle
  // ==========================================
  if (state.studyMode === 'kanji_quiz') {
    if (typeof window !== 'undefined' && typeof window.renderKanjiQuizCard === 'function') {
      window.renderKanjiQuizCard(item);
    }
    return;
  }

  // ==========================================
  // CASE A: READING COMPREHENSION QUESTION
  // ==========================================
  if (item.type === 'reading_question') {
    if (lessonTag) lessonTag.textContent = `読解 · ${item.lessonTitle || 'Passage Question'}`;

    if (!state.cardFlipped) {
      termEl.innerHTML = `<div style="font-size: 1.15rem; text-align: left; line-height: 1.6;">${item.question_ja || ''}</div>`;
      meaningEl.innerHTML = `
        <div style="font-size: 0.95rem; text-align: left; margin-top: 1rem; display: flex; flex-direction: column; gap: 0.4rem;">
          ${(item.options || []).map((opt, i) => `<div style="color: var(--text-muted);"><strong style="color: var(--accent);">${i + 1}.</strong> ${opt}</div>`).join('')}
        </div>
      `;
      if (exBox) exBox.style.display = 'none';
      document.getElementById('grade-controls').style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'none';
    } else {
      termEl.innerHTML = `
        <div style="font-size: 1.15rem; text-align: left; line-height: 1.6;">
          ${item.question_ja || ''}
          <div style="color: var(--green); font-size: 1.05rem; margin-top: 0.5rem; font-weight: 700;">
            <i class="fa-solid fa-circle-check"></i> Correct: Option ${item.correctAnswer} (${(item.options || [])[item.correctAnswer - 1] || ''})
          </div>
        </div>
      `;
      meaningEl.innerHTML = '';
      if (exBox && exJa && exEn) {
        exBox.style.display = 'block';
        exJa.textContent = item.explanation_ja || '';
        exEn.textContent = item.explanation_en || '';
      }
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'grid';
    }
    return;
  }

  // ==========================================
  // CASE C: KANJI TARGET CHARACTER
  // ==========================================
  if (item.type === 'kanji') {
    if (lessonTag) lessonTag.textContent = `漢字 · 第${item.lesson_number}課 ${item.lesson_title_ja || ''}`;

    if (!state.cardFlipped) {
      if (state.studyDirection === 'ja-en') {
        termEl.innerHTML = `<span style="font-size: 4rem; font-family: var(--font-jp); font-weight: 800; color: #fff;">${item.kanji}</span>`;
        meaningEl.innerHTML = `<span style="color: var(--text-dim); font-size: 1rem;">Tap card to reveal readings &amp; vocabulary</span>`;
      } else {
        const onStr = (item.onyomi || []).join('、 ');
        const kunStr = (item.kunyomi || []).join('、 ');
        termEl.innerHTML = `
          <div style="font-size: 1.1rem; line-height: 1.6;">
            ${(item.words || []).map(w => w.meaning_en).filter(Boolean).slice(0, 3).join(', ') || 'Recall Kanji'}
            <div style="font-size: 0.9rem; color: #f472b6; margin-top: 0.35rem;">音: ${onStr || '—'} · 訓: ${kunStr || '—'}</div>
          </div>
        `;
        meaningEl.innerHTML = `<span style="color: var(--text-dim); font-size: 1rem;">Tap card to reveal Kanji</span>`;
      }
      if (exBox) exBox.style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'none';
    } else {
      const onStr = (item.onyomi || []).join('、 ');
      const kunStr = (item.kunyomi || []).join('、 ');
      const wordsHtml = (item.words || []).map(w => `
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.35rem 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
          <span style="font-family: var(--font-jp); font-weight: 600;">${w.ruby_html || w.term_ja}</span>
          <span style="color: var(--text-muted); font-size: 0.85rem;">${w.meaning_en || ''}</span>
        </div>
      `).join('');

      termEl.innerHTML = `
        <div>
          <span style="font-size: 3.8rem; font-family: var(--font-jp); font-weight: 800; color: #fff;">${item.kanji}</span>
          <div style="font-size: 0.95rem; margin-top: 0.5rem; display: flex; justify-content: center; gap: 1rem;">
            <span style="color: #f472b6; font-weight: 600;">音: ${onStr || '—'}</span>
            <span style="color: var(--text-muted); font-weight: 600;">訓: ${kunStr || '—'}</span>
          </div>
        </div>
      `;
      meaningEl.innerHTML = wordsHtml ? `<div style="text-align: left; margin-top: 0.75rem; max-width: 380px; margin-left: auto; margin-right: auto;">${wordsHtml}</div>` : '';
      if (exBox) exBox.style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'grid';
    }
    return;
  }

  // ==========================================
  // CASE D: KANJI PRACTICE EXERCISE
  // ==========================================
  if (item.type === 'kanji_exercise') {
    if (lessonTag) lessonTag.textContent = `漢字練習 · ${item.exercise_title || 'Drill'}`;

    const qText = item.question_ja || item.sentence || item.target_word || '';
    if (!state.cardFlipped) {
      termEl.innerHTML = `<div style="font-size: 1.2rem; font-family: var(--font-jp); text-align: left; line-height: 1.6;">${qText}</div>`;
      if (item.options && item.options.length > 0) {
        meaningEl.innerHTML = `
          <div style="font-size: 0.95rem; text-align: left; margin-top: 1rem; display: flex; flex-direction: column; gap: 0.4rem;">
            ${item.options.map((opt, i) => `<div style="color: var(--text-muted);"><strong style="color: #ec4899;">${i + 1}.</strong> ${opt}</div>`).join('')}
          </div>
        `;
      } else {
        meaningEl.innerHTML = `<span style="color: var(--text-dim); font-size: 1rem;">Tap card to reveal correct reading &amp; answer</span>`;
      }
      if (exBox) exBox.style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'none';
    } else {
      const ans = item.answer || item.reading || (item.answers ? item.answers.join(', ') : '');
      termEl.innerHTML = `
        <div style="font-size: 1.2rem; font-family: var(--font-jp); text-align: left; line-height: 1.6;">
          ${qText}
          <div style="color: var(--green); font-size: 1.1rem; margin-top: 0.75rem; font-weight: 700;">
            <i class="fa-solid fa-circle-check"></i> 正解: ${ans}
          </div>
        </div>
      `;
      meaningEl.innerHTML = '';
      if (item.explanation && exBox && exJa && exEn) {
        exBox.style.display = 'block';
        exJa.textContent = item.explanation;
        exEn.textContent = '';
      } else if (exBox) {
        exBox.style.display = 'none';
      }
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'grid';
    }
    return;
  }

  // ==========================================
  // CASE E: KANJI TARGET COMPOUND WORD (JLPT MONDAI 1 & 2 DRILL)
  // ==========================================
  if (item.type === 'kanji_word') {
    const dir = item.direction || state.kanjiStudyDirection || 'ja-kana';
    if (lessonTag) lessonTag.textContent = `漢字第${item.lesson_number}課 · 親漢字「${item.baseKanji || '漢字'}」`;

    if (!state.cardFlipped) {
      if (dir === 'ja-kana') {
        // JLPT Mondai 1: Given Kanji, recall Kana reading
        termEl.innerHTML = `
          <div>
            <div style="font-size: 3.4rem; font-family: var(--font-jp); font-weight: 800; color: #fff; letter-spacing: 0.05em;">
              ${item.word}
            </div>
            <div style="margin-top: 0.75rem; display: flex; justify-content: center; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
              <span class="badge" style="background: rgba(236,72,153,0.18); border: 1px solid #ec4899; color: #f472b6; font-size: 0.78rem; font-weight: 700;">
                <i class="fa-solid fa-shapes"></i> 親漢字: ${item.baseKanji || '—'}
              </span>
              <span class="badge badge-purple" style="font-size: 0.78rem;">漢字読み (Kanji → Kana)</span>
            </div>
          </div>
        `;
        meaningEl.innerHTML = `<span style="color: var(--text-dim); font-size: 0.95rem;">Tap to reveal</span>`;
      } else if (dir === 'kana-ja') {
        // JLPT Mondai 2: Given Kana, recall Kanji spelling
        termEl.innerHTML = `
          <div>
            <div style="font-size: 3rem; font-family: var(--font-jp); font-weight: 800; color: #38bdf8; letter-spacing: 0.05em;">
              ${item.reading}
            </div>
            <div style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">
              ${item.meaning_en || ''}
            </div>
            <div style="margin-top: 0.75rem;">
              <span class="badge badge-cyan" style="font-size: 0.78rem;">表記 (Kana → Kanji)</span>
            </div>
          </div>
        `;
        meaningEl.innerHTML = `<span style="color: var(--text-dim); font-size: 0.95rem;">Tap to reveal</span>`;
      } else {
        // Meaning mode: Given Kanji, recall English
        termEl.innerHTML = `
          <div>
            <div style="font-size: 3.4rem; font-family: var(--font-jp); font-weight: 800; color: #fff;">
              ${item.word}
            </div>
            <div style="color: #f472b6; font-size: 1.15rem; font-family: var(--font-jp); margin-top: 0.4rem;">
              （${item.reading}）
            </div>
          </div>
        `;
        meaningEl.innerHTML = `<span style="color: var(--text-dim); font-size: 0.95rem;">Tap to reveal</span>`;
      }

      if (exBox) exBox.style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'none';
    } else {
      // Detailed Back / Revealed view (Full breakdown)
      const onStr = (item.onyomi || []).join('、 ');
      const kunStr = (item.kunyomi || []).join('、 ');
      termEl.innerHTML = `
        <div>
          <div style="font-size: 3.2rem; font-family: var(--font-jp); font-weight: 800; color: #fff;">
            ${item.ruby_html || item.word}
          </div>
          <div style="font-size: 1.6rem; color: #ec4899; font-weight: 700; margin-top: 0.35rem; font-family: var(--font-jp);">
            ${item.reading}
          </div>
        </div>
      `;
      meaningEl.innerHTML = `
        <div style="margin-top: 0.75rem; text-align: center;">
          <div style="font-size: 1.15rem; color: #fff; font-weight: 600;">
            ${item.meaning_en || ''} ${item.meaning_zh ? `<span style="color: var(--text-dim); font-size: 0.88rem;">(${item.meaning_zh})</span>` : ''}
          </div>
          <div style="margin-top: 0.85rem; padding: 0.65rem 0.85rem; background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: var(--radius-sm); display: inline-flex; gap: 1rem; align-items: center; font-size: 0.82rem; text-align: left; flex-wrap: wrap; justify-content: center;">
            <div><strong style="color: #fff;">親漢字:</strong> <span style="font-size: 1.15rem; color: #f472b6; font-weight: 800; font-family: var(--font-jp);">${item.baseKanji || '—'}</span></div>
            <div><strong style="color: #ec4899;">音:</strong> ${onStr || '—'}</div>
            <div><strong style="color: var(--text-muted);">訓:</strong> ${kunStr || '—'}</div>
          </div>
        </div>
      `;

      if (exBox) exBox.style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'none';
      document.getElementById('grade-controls').style.display = 'grid';
    }
    return;
  }

  // ==========================================
  // CASE B: VOCABULARY TERM
  // ==========================================
  const meta = state.chapterMetadata[item.chapter] || {};
  if (lessonTag) lessonTag.textContent = `${meta.topic_ja || item.chapter} · ${item.section_title_ja || ''}`;

  // New word, teach stage: meaning first, then "Got it, quiz me"
  if (isLearnStage(item)) {
    termEl.innerHTML = item.ruby_html || item.term_ja;
    meaningEl.innerHTML = `<span class="learn-badge">NEW WORD</span><div>${item.meaning_en || ''}</div>`;
    meaningEl.style.color = 'var(--text)';
    if (item.example_ja && exBox && exJa && exEn) {
      exBox.style.display = 'block';
      exJa.textContent = item.example_ja;
      exEn.textContent = item.example_en || '';
    } else if (exBox) {
      exBox.style.display = 'none';
    }
    const hint = document.getElementById('card-controls-hint');
    hint.innerHTML = '<button class="btn btn-primary learn-gotit" onclick="event.stopPropagation(); learnGotIt()"><i class="fa-solid fa-check"></i> Got it, quiz me</button>';
    hint.style.display = 'block';
    document.getElementById('grade-controls').style.display = 'none';
    return;
  }

  if (!state.cardFlipped) {
    if (state.studyDirection === 'ja-en') {
      termEl.innerHTML = state.showFurigana ? (item.ruby_html || item.term_ja) : item.term_ja;
      meaningEl.textContent = 'Tap card to reveal meaning';
      meaningEl.style.color = 'var(--text-dim)';
      if (exBox) exBox.style.display = 'none';
    } else {
      termEl.innerHTML = `<span style="font-size: 1.8rem;">${item.meaning_en}</span>`;
      meaningEl.textContent = 'Tap card to reveal Japanese';
      meaningEl.style.color = 'var(--text-dim)';
      if (exBox) exBox.style.display = 'none';
    }
    document.getElementById('card-controls-hint').style.display = 'none';
    document.getElementById('grade-controls').style.display = 'none';
  } else {
    if (state.studyDirection === 'ja-en') {
      termEl.innerHTML = item.ruby_html || item.term_ja;
      meaningEl.textContent = item.meaning_en;
      meaningEl.style.color = 'var(--text)';
    } else {
      termEl.innerHTML = item.ruby_html || item.term_ja;
      meaningEl.textContent = `${item.meaning_en} ${item.meaning_zh ? `(${item.meaning_zh})` : ''}`;
      meaningEl.style.color = 'var(--text)';
    }

    if (item.example_ja && exBox && exJa && exEn) {
      exBox.style.display = 'block';
      exJa.textContent = item.example_ja;
      exEn.textContent = item.example_en || '';
    } else if (exBox) {
      exBox.style.display = 'none';
    }

    document.getElementById('card-controls-hint').style.display = 'none';
    document.getElementById('grade-controls').style.display = 'grid';
  }
}

export function flipCard() {
  if (state.studyMode === 'kanji_quiz') return;
  if (isLearnStage(state.sessionItems[state.sessionIdx])) { learnGotIt(); return; }
  state.cardFlipped = !state.cardFlipped;
  renderCard();
}

export function gradeCard(grade) {
  if (state.sessionIdx >= state.sessionItems.length) return;

  const item = state.sessionItems[state.sessionIdx];
  const itemKey = formatItemKey(item);
  updateItemStats(itemKey, grade);

  state.sessionTotalAnswered = (state.sessionTotalAnswered || 0) + 1;

  if (grade >= 2) {
    state.sessionRight = (state.sessionRight || 0) + 1;
  }

  // Anki / Elementary app model: Re-queue failed cards (grade 1 Again) +3 positions down the deck
  const isAgain = grade === 1;
  if (isAgain) {
    const insertAt = Math.min(state.sessionIdx + 3, state.sessionItems.length);
    state.sessionItems.splice(insertAt, 0, { ...item, _requeued: true });
  }

  state.sessionIdx++;
  state.cardFlipped = false;
  renderCard();
}

export function toggleCurrentCardHard() {
  if (state.sessionIdx >= state.sessionItems.length) return;
  const item = state.sessionItems[state.sessionIdx];
  const itemKey = formatItemKey(item);
  const newHard = toggleItemHard(itemKey);
  const flameBtn = document.getElementById('card-hard-flame');
  if (flameBtn) {
    flameBtn.className = `btn-hard-flame${newHard ? ' is-hard' : ''}`;
  }
}

export function playCurrentCardAudio() {
  if (state.sessionIdx >= state.sessionItems.length) return;
  const item = state.sessionItems[state.sessionIdx];
  const text = item.reading || item.term_ja || item.word || item.question_ja;
  if ('speechSynthesis' in window && text) {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ja-JP';
    u.rate = 0.9;
    window.speechSynthesis.speak(u);
  }
}

function renderStudySummary() {
  const container = document.getElementById('study-card-container');
  if (!container) return;

  const skipped = state.sessionSkipped || 0;
  const answered = state.sessionTotalAnswered || Math.max(state.sessionTotal - skipped, 0);
  const correct = state.sessionRight || 0;
  const pct = answered ? Math.round((correct / answered) * 100) : 0;
  const initialTotal = state.sessionTotalInitial || state.sessionTotal || state.sessionItems.length;

  const skipRow = document.getElementById('study-skip-row');
  if (skipRow) skipRow.style.display = 'none';
  const again = state.studyMode === 'kanji_quiz'
    ? 'startKanjiQuickQuiz()'
    : state.learnUnit
      ? `startLearnNew('${state.learnUnit}')`
      : (state.drillOrigin === 'kanji'
        ? 'drillKanjiSelected()'
        : `startStudy('${state.studyMode}', ${state.studyIsDrillHard}, '${state.drillOrigin}')`);
  const againLabel = state.studyMode === 'kanji_quiz'
    ? 'Quiz Again'
    : state.learnUnit
      ? 'Learn more words'
      : (state.drillOrigin === 'kanji' ? 'Drill Again' : 'Review Again');

  container.innerHTML = `
    <div class="study-summary-card">
      <i class="fa-solid fa-trophy summary-trophy"></i>
      <h2>Session Complete!</h2>
      <p style="color: var(--text-muted);">You completed all ${initialTotal} items (${answered} reviews total${skipped ? `, ${skipped} skipped` : ''}).</p>

      <div class="summary-stats-row">
        <div class="summary-stat-box">
          <span class="summary-stat-val" style="color: var(--green);">${correct}</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Correct</span>
        </div>
        <div class="summary-stat-box">
          <span class="summary-stat-val" style="color: var(--accent);">${pct}%</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Accuracy</span>
        </div>
        <div class="summary-stat-box">
          <span class="summary-stat-val" style="color: var(--red);">${Math.max(0, answered - correct)}</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Again Re-queues</span>
        </div>
      </div>

      <div style="display: flex; gap: 1rem; margin-top: 1rem;">
        <button class="btn btn-primary" onclick="${again}">
          <i class="fa-solid fa-rotate-right"></i> ${againLabel}
        </button>
        <button class="btn btn-ghost" onclick="exitStudy()">
          <i class="fa-solid fa-arrow-left"></i> Return
        </button>
      </div>
    </div>
  `;
  // card-controls-hint lives inside the container we just replaced - guard both
  const gradeControlsEl = document.getElementById('grade-controls');
  if (gradeControlsEl) gradeControlsEl.style.display = 'none';
  const controlsHintEl = document.getElementById('card-controls-hint');
  if (controlsHintEl) controlsHintEl.style.display = 'none';
}

export function exitStudy() {
  showView(state.drillOrigin || 'home');
  resetStudyViewHTML();
}

export function resetStudyViewHTML() {
  const container = document.getElementById('study-card-container');
  if (!container) return;
  container.innerHTML = `
    <div class="flashcard-stage" onclick="flipCard()">
      <div class="flashcard" id="flashcard">
        <div class="flashcard-top">
          <span class="card-lesson-tag" id="card-lesson-tag">Unit</span>
          <div style="display: flex; gap: 0.5rem; align-items: center;" onclick="event.stopPropagation()">
            <button class="btn-sm btn-ghost" onclick="playCurrentCardAudio()" title="Listen to pronunciation">
              <i class="fa-solid fa-volume-high"></i>
            </button>
            <button class="btn-hard-flame" id="card-hard-flame" onclick="toggleCurrentCardHard()" title="Toggle Hard Word">
              <i class="fa-solid fa-fire"></i>
            </button>
          </div>
        </div>

        <div class="flashcard-body">
          <div class="card-term-large font-ja" id="card-term">Loading...</div>
          <div class="card-meaning-large" id="card-meaning">Tap to reveal</div>
          <div class="card-example-box" id="card-example-box" style="display: none;">
            <div class="card-example-ja font-ja" id="card-ex-ja"></div>
            <div class="card-example-en" id="card-ex-en"></div>
          </div>
        </div>

        <div class="flashcard-bottom" id="card-controls-hint" style="display: none;"></div>
      </div>
    </div>
  `;
}
