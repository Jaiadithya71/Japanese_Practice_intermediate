/* =======================================================
   NIHONGO INTERMEDIATE — study.js
   Active Recall Flashcard Engine & Study Session Logic
   ======================================================= */

import { state } from './state.js';
import { updateWordStats, toggleWordHard, getWordStatus, updateSidebarStats, snapToNextDueSlot } from './srs.js';
import { showView } from './navigation.js';

export function startStudy(mode = 'flashcard', isDrillHard = false, origin = 'home') {
  state.studyMode = mode;
  state.studyIsDrillHard = isDrillHard;
  state.drillOrigin = origin;
  state.isDueReviewMode = false;

  const pool = [];
  const chaptersToUse = state.selectedChapters.size > 0 
    ? Array.from(state.selectedChapters) 
    : Object.keys(state.vocabDB);

  for (const chId of chaptersToUse) {
    for (const w of (state.vocabDB[chId] || [])) {
      if (isDrillHard) {
        if (getWordStatus(w.id, state.studyDirection) === 'hard') {
          pool.push(w);
        }
      } else {
        pool.push(w);
      }
    }
  }

  if (pool.length === 0) {
    alert(isDrillHard ? 'No hard words found in selected chapters!' : 'No words found in selected chapters!');
    return;
  }

  // Shuffle pool
  pool.sort(() => Math.random() - 0.5);

  const batchSize = isDrillHard ? pool.length : Math.min(25, pool.length);
  state.sessionWords = pool.slice(0, batchSize);
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = state.sessionWords.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

export function startDueReview() {
  const now = Date.now();
  const pool = [];

  for (const chId in state.vocabDB) {
    for (const w of state.vocabDB[chId]) {
      const s = state.stats[`W:${w.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`];
      if (s && s.nextDue && s.nextDue <= now) {
        pool.push(w);
      }
    }
  }

  if (pool.length === 0) {
    alert('No due words right now! Great job staying caught up.');
    return;
  }

  pool.sort(() => Math.random() - 0.5);
  const limit = state.dueBatchSize === 'all' ? pool.length : parseInt(state.dueBatchSize, 10);

  state.studyMode = 'flashcard';
  state.studyIsDrillHard = false;
  state.isDueReviewMode = true;
  state.drillOrigin = 'home';
  state.sessionWords = pool.slice(0, limit);
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = state.sessionWords.length;
  state.cardFlipped = false;

  showView('study');
  renderCard();
}

export function renderCard() {
  if (state.sessionIdx >= state.sessionTotal) {
    renderStudySummary();
    return;
  }

  const w = state.sessionWords[state.sessionIdx];
  const isHard = getWordStatus(w.id, state.studyDirection) === 'hard';

  // Update progress bar
  const fill = document.getElementById('study-progress-fill');
  const count = document.getElementById('study-progress-count');
  if (fill) fill.style.width = `${((state.sessionIdx) / state.sessionTotal) * 100}%`;
  if (count) count.textContent = `${state.sessionIdx + 1} / ${state.sessionTotal}`;

  const meta = state.chapterMetadata[w.chapter] || {};
  const lessonTag = document.getElementById('card-lesson-tag');
  if (lessonTag) lessonTag.textContent = `${meta.topic_ja || w.chapter} · ${w.section_title_ja || ''}`;

  const flameBtn = document.getElementById('card-hard-flame');
  if (flameBtn) {
    flameBtn.className = `btn-hard-flame${isHard ? ' is-hard' : ''}`;
  }

  const termEl = document.getElementById('card-term');
  const meaningEl = document.getElementById('card-meaning');
  const exBox = document.getElementById('card-example-box');
  const exJa = document.getElementById('card-ex-ja');
  const exEn = document.getElementById('card-ex-en');

  // Side A (Prompt) vs Side B (Answer)
  if (!state.cardFlipped) {
    if (state.studyDirection === 'ja-en') {
      termEl.innerHTML = state.showFurigana ? (w.ruby_html || w.term_ja) : w.term_ja;
      meaningEl.textContent = 'Tap card to reveal meaning';
      meaningEl.style.color = 'var(--text-dim)';
      if (exBox) exBox.style.display = 'none';
    } else {
      termEl.innerHTML = `<span style="font-size: 1.8rem;">${w.meaning_en}</span>`;
      meaningEl.textContent = 'Tap card to reveal Japanese';
      meaningEl.style.color = 'var(--text-dim)';
      if (exBox) exBox.style.display = 'none';
    }
    document.getElementById('card-controls-hint').style.display = 'block';
    document.getElementById('grade-controls').style.display = 'none';
  } else {
    // Flipped state
    if (state.studyDirection === 'ja-en') {
      termEl.innerHTML = w.ruby_html || w.term_ja;
      meaningEl.textContent = w.meaning_en;
      meaningEl.style.color = 'var(--text)';
    } else {
      termEl.innerHTML = w.ruby_html || w.term_ja;
      meaningEl.textContent = `${w.meaning_en} ${w.meaning_zh ? `(${w.meaning_zh})` : ''}`;
      meaningEl.style.color = 'var(--text)';
    }

    if (w.example_ja && exBox && exJa && exEn) {
      exBox.style.display = 'block';
      exJa.textContent = w.example_ja;
      exEn.textContent = w.example_en || '';
    } else if (exBox) {
      exBox.style.display = 'none';
    }

    document.getElementById('card-controls-hint').style.display = 'none';
    document.getElementById('grade-controls').style.display = 'grid';
  }
}

export function flipCard() {
  state.cardFlipped = !state.cardFlipped;
  renderCard();
}

export function gradeCard(grade) {
  if (state.sessionIdx >= state.sessionTotal) return;

  const w = state.sessionWords[state.sessionIdx];
  updateWordStats(w.id, grade, state.studyDirection);

  if (grade >= 3) {
    state.sessionRight++;
  }

  state.sessionIdx++;
  state.cardFlipped = false;
  renderCard();
}

export function toggleCurrentCardHard() {
  if (state.sessionIdx >= state.sessionTotal) return;
  const w = state.sessionWords[state.sessionIdx];
  const newHard = toggleWordHard(w.id, state.studyDirection);
  const flameBtn = document.getElementById('card-hard-flame');
  if (flameBtn) {
    flameBtn.className = `btn-hard-flame${newHard ? ' is-hard' : ''}`;
  }
}

export function playCurrentCardAudio() {
  if (state.sessionIdx >= state.sessionTotal) return;
  const w = state.sessionWords[state.sessionIdx];
  const text = w.reading || w.term_ja;
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

  const pct = Math.round((state.sessionRight / state.sessionTotal) * 100);

  container.innerHTML = `
    <div class="study-summary-card">
      <i class="fa-solid fa-trophy summary-trophy"></i>
      <h2>Session Complete!</h2>
      <p style="color: var(--text-muted);">You reviewed ${state.sessionTotal} intermediate vocabulary words.</p>

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
          <span class="summary-stat-val" style="color: var(--red);">${state.sessionTotal - state.sessionRight}</span>
          <span style="font-size: 0.8rem; color: var(--text-dim);">Struggling</span>
        </div>
      </div>

      <div style="display: flex; gap: 1rem; margin-top: 1rem;">
        <button class="btn btn-primary" onclick="startStudy('${state.studyMode}', ${state.studyIsDrillHard}, '${state.drillOrigin}')">
          <i class="fa-solid fa-rotate-right"></i> Study Again
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
  // Re-inject flashcard layout if next session starts
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
