/* =======================================================
   NIHONGO INTERMEDIATE — vocab-browser.js
   Vocabulary Browser, Filtering & Hard Words Drill-Down
   ======================================================= */

import { state } from './state.js';
import { getWordStatus, toggleWordHard, updateSidebarStats } from './srs.js';
import { startStudy } from './study.js';

function groupKeys() {
  const isChar = state.activeChapterGroup !== 'topic';
  const rank = k => (k.startsWith('review_') ? 1000 + parseInt(k.slice(7), 10) : parseInt(k.replace('part2_', ''), 10));
  return Object.keys(state.vocabDB).filter(k => k.startsWith('part2_') === isChar).sort((a, b) => rank(a) - rank(b));
}

export function toggleVocabMultiSelectMode() {
  state.vocabMultiSelectMode = !state.vocabMultiSelectMode;
  renderChapterChips();
}

export function renderChapterChips() {
  const container = document.getElementById('chapter-chips');
  if (!container) return;
  container.innerHTML = '';

  if (!(state.selectedVocabChapters instanceof Set)) {
    state.selectedVocabChapters = new Set();
  }

  const isAll = state.selectedVocabChapters.size === 0 || state.vocabChapter === 'all';

  // All button
  const allBtn = document.createElement('button');
  allBtn.className = `chapter-chip${isAll ? ' active' : ''}`;
  allBtn.innerHTML = `${isAll ? '<i class="fa-solid fa-check"></i> ' : ''}All`;
  allBtn.onclick = () => selectChapter('all');
  container.appendChild(allBtn);

  const chapterKeys = groupKeys();

  chapterKeys.forEach(chId => {
    const meta = state.chapterMetadata[chId] || {};
    const words = state.vocabDB[chId] || [];
    let hardCount = 0;
    let masteredCount = 0;

    words.forEach(w => {
      const st = getWordStatus(w.id, state.studyDirection);
      if (st === 'hard') hardCount++;
      if (st === 'mastered') masteredCount++;
    });

    const isSelected = !isAll && state.selectedVocabChapters.has(chId);
    const chip = document.createElement('button');
    let cls = 'chapter-chip';
    if (isSelected) cls += ' active selected';
    else if (hardCount > 0) cls += ' has-hard';
    else if (masteredCount === words.length && words.length > 0) cls += ' all-done';

    let dot = '';
    if (!isSelected && hardCount > 0) {
      dot = '<span class="chip-dot red" style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#ef4444;margin-left:4px;"></span>';
    } else if (!isSelected && masteredCount === words.length && words.length > 0) {
      dot = '<span class="chip-dot green" style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#10b981;margin-left:4px;"></span>';
    }

    const shortLabel = chId.startsWith('part2_') ? 'C' + chId.slice(6) : chId.startsWith('review_') ? 'R' + chId.slice(7) : 'T' + chId;
    const checkIcon = isSelected ? '<i class="fa-solid fa-check"></i> ' : '';
    chip.className = cls;
    chip.title = `${shortLabel}: ${meta.topic_ja || chId} (${words.length} words)`;
    chip.innerHTML = `${checkIcon}${shortLabel}${dot}`;

    // Same as the kanji page: tap chips to add/remove units, All clears the selection
    chip.onclick = () => selectChapter(chId, 'toggle');
    container.appendChild(chip);
  });

  // Render Active Unit Banner
  const banner = document.getElementById('vocab-active-unit-banner');
  if (banner) {
    if (isAll) {
      const totalWords = chapterKeys.reduce((acc, k) => acc + (state.vocabDB[k] || []).length, 0);
      banner.innerHTML = `
        <div class="active-chapter-banner font-ja">
          <span class="badge badge-accent">All Units</span>
          <span><strong>${state.activeChapterGroup === 'topic' ? 'Part 1: Topics (21 Chapters)' : 'Part 2: Characteristics (8 Chapters)'}</strong> · ${totalWords} total words</span>
        </div>
      `;
    } else if (state.selectedVocabChapters.size === 1) {
      const chId = Array.from(state.selectedVocabChapters)[0];
      const meta = state.chapterMetadata[chId] || {};
      const words = state.vocabDB[chId] || [];
      const shortLabel = chId.startsWith('part2_') ? 'C' + chId.slice(6) : chId.startsWith('review_') ? 'R' + chId.slice(7) : 'T' + chId;
      banner.innerHTML = `
        <div class="active-chapter-banner font-ja">
          <span class="badge badge-accent">${shortLabel}</span>
          <span><strong>${meta.topic_ja || chId}</strong> ${meta.topic_en ? `(${meta.topic_en})` : ''} · ${words.length} words</span>
        </div>
      `;
    } else {
      let selWords = 0;
      for (const chId of state.selectedVocabChapters) {
        selWords += (state.vocabDB[chId] || []).length;
      }
      banner.innerHTML = `
        <div class="active-chapter-banner font-ja">
          <span class="badge badge-accent">${state.selectedVocabChapters.size} Units</span>
          <span><strong>Multi-Unit Selection</strong> · ${selWords} words selected</span>
        </div>
      `;
    }
  }

  updateVocabActionButtonLabels();
}

export function selectChapter(chId, mode = 'single') {
  if (!(state.selectedVocabChapters instanceof Set)) {
    state.selectedVocabChapters = new Set();
  }

  if (chId === 'all') {
    state.selectedVocabChapters.clear();
    state.vocabChapter = 'all';
  } else {
    if (mode === 'toggle') {
      if (state.selectedVocabChapters.has(chId)) {
        state.selectedVocabChapters.delete(chId);
      } else {
        state.selectedVocabChapters.add(chId);
      }
    } else {
      state.selectedVocabChapters.clear();
      state.selectedVocabChapters.add(chId);
    }
    state.vocabChapter = state.selectedVocabChapters.size === 1 ? Array.from(state.selectedVocabChapters)[0] : (state.selectedVocabChapters.size === 0 ? 'all' : 'multi');
  }

  renderChapterChips();
  renderVocabList();
  updateVocabActionButtonLabels();
}

export function updateVocabActionButtonLabels() {
  const btn = document.getElementById('btn-vocab-study-action');
  if (!btn) return;

  const selChapters = state.selectedVocabChapters || new Set();
  let wordsCount = 0;

  if (selChapters.size === 0) {
    for (const chId in (state.vocabDB || {})) {
      wordsCount += (state.vocabDB[chId] || []).length;
    }
    btn.innerHTML = `<i class="fa-solid fa-play"></i> Drill All Words <span class="badge" style="margin-left: 0.35rem; font-size: 0.72rem; padding: 0.15rem 0.45rem; background: rgba(255, 255, 255, 0.2); color: #fff; border-radius: 999px;">${wordsCount}w</span>`;
  } else {
    for (const chId of selChapters) {
      wordsCount += (state.vocabDB[chId] || []).length;
    }
    const label = selChapters.size === 1 ? `Unit ${Array.from(selChapters)[0]}` : `${selChapters.size} Units`;
    btn.innerHTML = `<i class="fa-solid fa-play"></i> Drill ${label} <span class="badge" style="margin-left: 0.35rem; font-size: 0.72rem; padding: 0.15rem 0.45rem; background: rgba(255, 255, 255, 0.2); color: #fff; border-radius: 999px;">${wordsCount}w</span>`;
  }
}

export function drillVocabSelected() {
  const selChapters = state.selectedVocabChapters || new Set();
  state.selectedChapters = new Set(selChapters);
  startStudy('flashcard', false, 'vocab');
}

export function setChapterGroup(group) {
  state.activeChapterGroup = group;
  state.vocabChapter = 'all';
  if (state.selectedVocabChapters instanceof Set) {
    state.selectedVocabChapters.clear();
  }

  const tabT = document.getElementById('vgroup-topic');
  const tabC = document.getElementById('vgroup-char');
  if (tabT) tabT.classList.toggle('active', group === 'topic');
  if (tabC) tabC.classList.toggle('active', group === 'characteristics');

  renderChapterChips();
  renderVocabList();
  updateVocabActionButtonLabels();
}

export function setVocabFilter(filter) {
  state.vocabFilter = filter;
  document.querySelectorAll('.vf-tab').forEach(t => t.classList.remove('active'));
  const activeTab = document.getElementById(`vf-${filter}`);
  if (activeTab) activeTab.classList.add('active');
  renderVocabList();
}

export function onVocabSearch(query) {
  state.vocabSearchQuery = query.trim().toLowerCase();
  renderVocabList();
}

export function toggleFurigana() {
  state.showFurigana = !state.showFurigana;
  document.body.classList.toggle('hide-furigana', !state.showFurigana);
  const btn = document.getElementById('btn-toggle-furigana');
  if (btn) {
    btn.innerHTML = `<i class="fa-solid fa-font"></i> Furigana: ${state.showFurigana ? 'ON' : 'OFF'}`;
  }
}

export function renderVocabList() {
  const container = document.getElementById('vocab-list-container');
  if (!container) return;
  container.innerHTML = '';

  let baseList = [];
  const selChapters = state.selectedVocabChapters || new Set();

  if (selChapters.size === 0 || state.vocabChapter === 'all') {
    for (const chId of groupKeys()) {
      baseList.push(...(state.vocabDB[chId] || []));
    }
  } else {
    for (const chId of selChapters) {
      if (state.vocabDB[chId]) {
        baseList.push(...state.vocabDB[chId]);
      }
    }
  }

  // Calculate stats for current chapter selection before filtering
  let totalShowing = baseList.length;
  let totalHard = 0, totalLearning = 0, totalMastered = 0, totalUnseen = 0;
  baseList.forEach(w => {
    const st = getWordStatus(w.id, state.studyDirection);
    if (st === 'hard') totalHard++;
    else if (st === 'learning') totalLearning++;
    else if (st === 'mastered') totalMastered++;
    else if (st === 'unseen') totalUnseen++;
  });

  const vsShowing = document.getElementById('vs-showing');
  const vsHard = document.getElementById('vs-hard');
  const vsLearning = document.getElementById('vs-learning');
  const vsMastered = document.getElementById('vs-mastered');
  const vsUnseen = document.getElementById('vs-unseen');

  if (vsShowing) vsShowing.textContent = `${totalShowing} words`;
  if (vsHard) vsHard.textContent = `${totalHard} hard`;
  if (vsLearning) vsLearning.textContent = `${totalLearning} learning`;
  if (vsMastered) vsMastered.textContent = `${totalMastered} mastered`;
  if (vsUnseen) vsUnseen.textContent = `${totalUnseen} unseen`;

  let list = [...baseList];

  // Filter by status tab
  if (state.vocabFilter !== 'all') {
    list = list.filter(w => getWordStatus(w.id, state.studyDirection) === state.vocabFilter);
  }

  // Filter by search query
  if (state.vocabSearchQuery) {
    const q = state.vocabSearchQuery;
    list = list.filter(w => 
      (w.term_ja || '').toLowerCase().includes(q) ||
      (w.reading || '').toLowerCase().includes(q) ||
      (w.meaning_en || '').toLowerCase().includes(q) ||
      (w.meaning_zh || '').toLowerCase().includes(q)
    );
  }

  const countBadge = document.getElementById('vocab-count-badge');
  if (countBadge) countBadge.textContent = `${list.length} words`;

  if (list.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-magnifying-glass"></i>
        <h3>No vocabulary found</h3>
        <p>Try adjusting your search query or filter tab.</p>
      </div>`;
    return;
  }

  const isStudyMode = document.getElementById('vocab-study-mode')?.checked || false;

  list.forEach(w => {
    const st = getWordStatus(w.id, state.studyDirection);
    const isHard = st === 'hard';
    const card = document.createElement('div');
    card.className = 'vocab-card';

    const statusPillHtml = `
      <span class="badge ${st === 'hard' ? 'badge-red' : st === 'mastered' ? 'badge-green' : st === 'learning' ? 'badge-amber' : 'badge-ghost'}" style="font-size: 0.68rem; padding: 0.12rem 0.4rem;">
        ${st === 'hard' ? 'Hard' : st === 'mastered' ? 'Mastered' : st === 'learning' ? 'Learning' : 'New'}
      </span>
    `;

    if (isStudyMode) {
      card.innerHTML = `
        <div class="vocab-main">
          <div class="vocab-term-row">
            <span class="vocab-term font-ja">${w.ruby_html || w.term_ja}</span>
            ${w.part_of_speech ? `<span class="vocab-pos">${w.part_of_speech}</span>` : ''}
          </div>
          <div class="vw-study-cell" onclick="event.stopPropagation(); this.classList.toggle('show')" title="Tap to toggle English meaning">
            <div class="study-cell-hint"><i class="fa-solid fa-comment-dots"></i> Tap to Show Meaning</div>
            <div class="study-cell-content">
              <div class="vocab-meaning">${w.meaning_en} ${w.meaning_zh ? `<span style="color: var(--text-dim);">· ${w.meaning_zh}</span>` : ''}</div>
              ${w.example_ja ? `
                <div class="vocab-example font-ja" style="margin-top: 0.35rem;">
                  <div>${w.example_ja}</div>
                  <div style="font-size: 0.78rem; color: var(--text-dim); margin-top: 0.15rem;">${w.example_en || ''}</div>
                </div>` : ''}
            </div>
          </div>
        </div>
        <div class="vocab-actions" style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.4rem;">
          <div style="display: flex; align-items: center; gap: 0.4rem;">
            <button class="btn-sm btn-ghost" onclick="playAudio('${w.reading || w.term_ja}')" title="Play pronunciation">
              <i class="fa-solid fa-volume-high"></i>
            </button>
            <button class="btn-hard-flame${isHard ? ' is-hard' : ''}" id="flame-${w.id}" onclick="onToggleHard('${w.id}')" title="Mark as Hard Word">
              <i class="fa-solid fa-fire"></i>
            </button>
          </div>
          ${statusPillHtml}
        </div>
      `;
    } else {
      card.innerHTML = `
        <div class="vocab-main">
          <div class="vocab-term-row">
            <span class="vocab-term font-ja">${w.ruby_html || w.term_ja}</span>
            ${w.part_of_speech ? `<span class="vocab-pos">${w.part_of_speech}</span>` : ''}
          </div>
          <div class="vocab-meaning">${w.meaning_en} ${w.meaning_zh ? `<span style="color: var(--text-dim);">· ${w.meaning_zh}</span>` : ''}</div>
          ${w.example_ja ? `
            <div class="vocab-example font-ja">
              <div>${w.example_ja}</div>
              <div style="font-size: 0.78rem; color: var(--text-dim); margin-top: 0.15rem;">${w.example_en || ''}</div>
            </div>` : ''}
        </div>
        <div class="vocab-actions" style="display: flex; flex-direction: column; align-items: flex-end; gap: 0.4rem;">
          <div style="display: flex; align-items: center; gap: 0.4rem;">
            <button class="btn-sm btn-ghost" onclick="playAudio('${w.reading || w.term_ja}')" title="Play pronunciation">
              <i class="fa-solid fa-volume-high"></i>
            </button>
            <button class="btn-hard-flame${isHard ? ' is-hard' : ''}" id="flame-${w.id}" onclick="onToggleHard('${w.id}')" title="Mark as Hard Word">
              <i class="fa-solid fa-fire"></i>
            </button>
          </div>
          ${statusPillHtml}
        </div>
      `;
    }
    container.appendChild(card);
  });
}

export function onToggleHard(wordId) {
  const isHard = toggleWordHard(wordId, state.studyDirection);
  const btn = document.getElementById(`flame-${wordId}`);
  if (btn) btn.className = `btn-hard-flame${isHard ? ' is-hard' : ''}`;
  renderChapterChips();
  updateHardWordsView();
}

export function playAudio(text) {
  if ('speechSynthesis' in window && text) {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ja-JP';
    u.rate = 0.9;
    window.speechSynthesis.speak(u);
  }
}

// =======================================================
// UNIVERSAL EXAM WEAK POINTS DESK
// =======================================================

export function setWeakPointsFilter(filter) {
  state.weakPointsFilter = filter;
  document.querySelectorAll('.wp-tab').forEach(t => t.classList.remove('active'));
  const activeTab = document.getElementById(`wpt-${filter}`);
  if (activeTab) activeTab.classList.add('active');
  updateHardWordsView();
}

export function updateHardWordsView() {
  const container = document.getElementById('hard-words-list');
  if (!container) return;
  container.innerHTML = '';

  const weakItems = [];

  // 1. Vocabulary Hard Words
  if (state.weakPointsFilter === 'all' || state.weakPointsFilter === 'vocab') {
    for (const chId in state.vocabDB) {
      for (const w of state.vocabDB[chId]) {
        const itemKey = `V:${w.id}${state.studyDirection === 'en-ja' ? ':rev' : ''}`;
        if (getWordStatus(w.id, state.studyDirection) === 'hard') {
          weakItems.push({ ...w, type: 'vocab', key: itemKey, book: 'vocab' });
        }
      }
    }
  }

  // 2. Reading Missed Questions
  if (state.weakPointsFilter === 'all' || state.weakPointsFilter === 'reading') {
    for (const lid in state.readingDB) {
      const lesson = state.readingDB[lid];
      const questions = lesson.comprehensionQuestions || lesson.questions || [];
      for (const q of questions) {
        const qId = q.id || `${lid}_q${q.questionNumber || 1}`;
        const itemKey = `R_Q:${qId}`;
        const s = state.stats[itemKey];
        if (s && (s.isHard || (s.weight || 1.0) >= 1.8 || s.incorrect > 0)) {
          weakItems.push({
            ...q,
            id: qId,
            lessonId: lid,
            lessonTitle: lesson.title_ja || lesson.title,
            type: 'reading_question',
            key: itemKey,
            book: 'reading'
          });
        }
      }
    }
  }

  const hardHeaderCount = document.getElementById('hard-words-header-count');
  if (hardHeaderCount) {
    hardHeaderCount.textContent = `${weakItems.length} Exam Weak Points Need Revision`;
  }

  if (weakItems.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-fire" style="color: var(--text-dim);"></i>
        <h3>No Exam Weak Points Flagged</h3>
        <p>Words you struggle with or Dokkai questions you miss will appear here for targeted revision.</p>
      </div>`;
    return;
  }

  weakItems.forEach(item => {
    const card = document.createElement('div');
    card.className = 'vocab-card';

    if (item.type === 'reading_question') {
      card.innerHTML = `
        <div class="vocab-main">
          <div class="vocab-term-row">
            <span class="vocab-pos" style="background: var(--accent-light); color: var(--accent);">読解 Question</span>
            <span style="font-size: 0.85rem; color: var(--text-muted);">${item.lessonTitle || ''}</span>
          </div>
          <div style="font-size: 1.05rem; font-weight: 700; color: #fff; margin-top: 0.25rem;" class="font-ja">${item.question_ja || ''}</div>
          <div class="vocab-meaning hard-word-def" style="margin-top: 0.4rem; color: var(--green);">
            <strong>Correct: Option ${item.correctAnswer}</strong> — ${item.explanation_ja || ''}
          </div>
        </div>
        <div class="vocab-actions">
          <button class="btn-hard-flame is-hard" onclick="onToggleHard('${item.id}')" title="Unmark Weak Point">
            <i class="fa-solid fa-fire"></i>
          </button>
        </div>
      `;
    } else {
      card.innerHTML = `
        <div class="vocab-main">
          <div class="vocab-term-row">
            <span class="vocab-term font-ja">${item.ruby_html || item.term_ja}</span>
            ${item.part_of_speech ? `<span class="vocab-pos">${item.part_of_speech}</span>` : ''}
          </div>
          <div class="vocab-meaning hard-word-def">${item.meaning_en}</div>
          ${item.example_ja ? `<div class="vocab-example font-ja">${item.example_ja}</div>` : ''}
        </div>
        <div class="vocab-actions">
          <button class="btn-sm btn-ghost" onclick="playAudio('${item.reading || item.term_ja}')">
            <i class="fa-solid fa-volume-high"></i>
          </button>
          <button class="btn-hard-flame is-hard" onclick="onToggleHard('${item.id}')" title="Unmark Hard">
            <i class="fa-solid fa-fire"></i>
          </button>
        </div>
      `;
    }
    container.appendChild(card);
  });
}

export function drillAllHardWords() {
  state.selectedChapters = new Set(); // hard tab = hard words across every unit
  startStudy('flashcard', true, 'hard-words');
}

// Hard words only, limited to the units currently selected on the browser (all units if none)
export function drillVocabHard() {
  state.selectedChapters = new Set(state.selectedVocabChapters || []);
  startStudy('flashcard', true, 'vocab');
}
if (typeof window !== 'undefined') window.drillVocabHard = drillVocabHard;

export function toggleRevealHardWords() {
  const defs = document.querySelectorAll('.hard-word-def');
  defs.forEach(d => {
    d.classList.toggle('hide');
  });
}
