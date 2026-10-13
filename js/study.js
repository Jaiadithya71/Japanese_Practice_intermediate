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

  const batchSize = isDrillHard ? pool.length : Math.min(25, pool.length);
  state.sessionItems = pool.slice(0, batchSize);
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = state.sessionItems.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

export function startDueReview(pillarFilter = 'all') {
  state.omniDueFilter = pillarFilter;
  const pool = getAllDueItems(pillarFilter, state.dueBatchSize);

  if (pool.length === 0) {
    alert('No due items right now for this pillar! Great job staying caught up.');
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
  if (state.sessionIdx >= state.sessionTotal) {
    renderStudySummary();
    return;
  }

  const item = state.sessionItems[state.sessionIdx];
  const itemKey = formatItemKey(item);
  const isHard = getItemStatus(itemKey) === 'hard';
  const skipRow = document.getElementById('study-skip-row');
  if (skipRow) skipRow.style.display = 'flex';

  // Progress Bar
  const fill = document.getElementById('study-progress-fill');
  const count = document.getElementById('study-progress-count');
  if (fill) fill.style.width = `${((state.sessionIdx) / state.sessionTotal) * 100}%`;
  if (count) count.textContent = `${state.sessionIdx + 1} / ${state.sessionTotal}`;

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
      document.getElementById('card-controls-hint').innerHTML = '<i class="fa-solid fa-hand-pointer"></i> Tap card or press Space to reveal correct answer & rationale';
      document.getElementById('grade-controls').style.display = 'none';
      document.getElementById('card-controls-hint').style.display = 'block';
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
      document.getElementById('card-controls-hint').innerHTML = '<i class="fa-solid fa-hand-pointer"></i> Tap card or press Space to reveal';
      document.getElementById('card-controls-hint').style.display = 'block';
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
      document.getElementById('card-controls-hint').innerHTML = '<i class="fa-solid fa-hand-pointer"></i> Tap card or press Space to reveal answer';
      document.getElementById('card-controls-hint').style.display = 'block';
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
    document.getElementById('card-controls-hint').innerHTML = '<i class="fa-solid fa-hand-pointer"></i> Tap card or press Space to reveal';
    document.getElementById('card-controls-hint').style.display = 'block';
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
  if (isLearnStage(state.sessionItems[state.sessionIdx])) { learnGotIt(); return; }
  state.cardFlipped = !state.cardFlipped;
  renderCard();
}

export function gradeCard(grade) {
  if (state.sessionIdx >= state.sessionTotal) return;

  const item = state.sessionItems[state.sessionIdx];
  const itemKey = formatItemKey(item);
  updateItemStats(itemKey, grade);

  if (grade >= 3) {
    state.sessionRight++;
  }

  state.sessionIdx++;
  state.cardFlipped = false;
  renderCard();
}

export function toggleCurrentCardHard() {
  if (state.sessionIdx >= state.sessionTotal) return;
  const item = state.sessionItems[state.sessionIdx];
  const itemKey = formatItemKey(item);
  const newHard = toggleItemHard(itemKey);
  const flameBtn = document.getElementById('card-hard-flame');
  if (flameBtn) {
    flameBtn.className = `btn-hard-flame${newHard ? ' is-hard' : ''}`;
  }
}

export function playCurrentCardAudio() {
  if (state.sessionIdx >= state.sessionTotal) return;
  const item = state.sessionItems[state.sessionIdx];
  const text = item.reading || item.term_ja || item.question_ja;
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
  const answered = Math.max(state.sessionTotal - skipped, 0);
  const pct = answered ? Math.round((state.sessionRight / answered) * 100) : 0;
  const skipRow = document.getElementById('study-skip-row');
  if (skipRow) skipRow.style.display = 'none';
  const again = state.learnUnit
    ? `startLearnNew('${state.learnUnit}')`
    : `startStudy('${state.studyMode}', ${state.studyIsDrillHard}, '${state.drillOrigin}')`;
  const againLabel = state.learnUnit ? 'Learn more words' : 'Review Again';

  container.innerHTML = `
    <div class="study-summary-card">
      <i class="fa-solid fa-trophy summary-trophy"></i>
      <h2>Session Complete!</h2>
      <p style="color: var(--text-muted);">You went through ${state.sessionTotal} items${skipped ? ` (${skipped} skipped, not scored)` : ''}.</p>

      <div class="summary-stats-row">
        <div class="summary-stat-box">
          <span class="summary-stat-val" style="color: var(--green);">${state.sessionRight}</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Correct</span>
        </div>
        <div class="summary-stat-box">
          <span class="summary-stat-val" style="color: var(--accent);">${pct}%</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Accuracy</span>
        </div>
        <div class="summary-stat-box">
          <span class="summary-stat-val" style="color: var(--red);">${answered - state.sessionRight}</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Struggling</span>
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
  document.getElementById('grade-controls').style.display = 'none';
  document.getElementById('card-controls-hint').style.display = 'none';
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

        <div class="flashcard-bottom" id="card-controls-hint">
          <i class="fa-solid fa-hand-pointer"></i> Tap card or press Space to reveal
        </div>
      </div>
    </div>
  `;
}
