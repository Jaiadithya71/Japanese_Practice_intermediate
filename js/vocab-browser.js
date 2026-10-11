/* =======================================================
   NIHONGO INTERMEDIATE — vocab-browser.js
   Vocabulary Browser, Filtering & Hard Words Drill-Down
   ======================================================= */

import { state } from './state.js';
import { getWordStatus, toggleWordHard, updateSidebarStats } from './srs.js';
import { startStudy } from './study.js';

export function renderChapterChips() {
  const container = document.getElementById('chapter-chips');
  if (!container) return;
  container.innerHTML = '';

  // All button
  const allBtn = document.createElement('button');
  allBtn.className = `chapter-chip${state.vocabChapter === 'all' ? ' active' : ''}`;
  allBtn.textContent = 'All Units';
  allBtn.onclick = () => selectChapter('all');
  container.appendChild(allBtn);

  const prefix = state.activeChapterGroup === 'topic' ? 'part1_' : 'part2_';
  const chapterKeys = Object.keys(state.vocabDB)
    .filter(k => k.startsWith(prefix))
    .sort();

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

    const chip = document.createElement('button');
    const isActive = state.vocabChapter === chId;
    let cls = 'chapter-chip';
    if (isActive) cls += ' active';
    else if (hardCount > 0) cls += ' has-hard';

    let dot = '';
    if (!isActive && hardCount > 0) {
      dot = '<span class="chip-dot red"></span>';
    } else if (!isActive && masteredCount === words.length && words.length > 0) {
      dot = '<span class="chip-dot green"></span>';
    }

    const shortLabel = chId.replace('part1_', 'T').replace('part2_', 'C');
    chip.className = cls;
    chip.innerHTML = `${shortLabel}: ${meta.topic_ja || chId}${dot}`;
    chip.onclick = () => selectChapter(chId);
    container.appendChild(chip);
  });
}

export function selectChapter(chId) {
  state.vocabChapter = chId;
  renderChapterChips();
  renderVocabList();
}

export function setChapterGroup(group) {
  state.activeChapterGroup = group;
  state.vocabChapter = 'all';

  const tabT = document.getElementById('vgroup-topic');
  const tabC = document.getElementById('vgroup-char');
  if (tabT) tabT.classList.toggle('active', group === 'topic');
  if (tabC) tabC.classList.toggle('active', group === 'characteristics');

  renderChapterChips();
  renderVocabList();
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

  let list = [];
  const prefix = state.activeChapterGroup === 'topic' ? 'part1_' : 'part2_';
  
  if (state.vocabChapter === 'all') {
    for (const chId in state.vocabDB) {
      if (chId.startsWith(prefix)) {
        list.push(...state.vocabDB[chId]);
      }
    }
  } else {
    list = [...(state.vocabDB[state.vocabChapter] || [])];
  }

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

  list.forEach(w => {
    const isHard = getWordStatus(w.id, state.studyDirection) === 'hard';
    const card = document.createElement('div');
    card.className = 'vocab-card';
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
      <div class="vocab-actions">
        <button class="btn-sm btn-ghost" onclick="playAudio('${w.reading || w.term_ja}')" title="Play pronunciation">
          <i class="fa-solid fa-volume-high"></i>
        </button>
        <button class="btn-hard-flame${isHard ? ' is-hard' : ''}" id="flame-${w.id}" onclick="onToggleHard('${w.id}')" title="Mark as Hard Word">
          <i class="fa-solid fa-fire"></i>
        </button>
      </div>
    `;
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
  startStudy('flashcard', true, 'hard-words');
}

export function toggleRevealHardWords() {
  const defs = document.querySelectorAll('.hard-word-def');
  defs.forEach(d => {
    d.classList.toggle('hide');
  });
}
