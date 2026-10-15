/* =======================================================
   NIHONGO INTERMEDIATE — book-platform.js
   Self-Contained Book Platform Controller (Option 1)
   Pillar Sub-Tabs, Pillar-Scoped SRS, Hard Panes, & Settings Drawer
   ======================================================= */

import { state } from './state.js';
import { getDueItemsCount, getItemStatus, getItemStats, toggleItemHard, getPillarFromKey, resolveItemForKey } from './srs.js';
import { startStudy, startOmniReview, startDueReview } from './study.js?v=3.4';
import { exportBackup, importBackup, restoreSnapshot } from './backup.js';
import { openSyncSetup } from './gist-sync.js';
import { renderKanjiView, setKanjiTab, drillKanjiSingle } from './kanji.js';
import { renderChapterChips, renderVocabList, toggleFurigana, playAudio } from './vocab-browser.js';
import { renderGrammarView, setGrammarTab } from './grammar.js';
import { renderReadingView, openReadingLesson } from './reader.js';

// Active sub-tabs per pillar
export const activeSubTabs = {
  vocab: 'units',
  kanji: 'target',
  grammar: 'patterns',
  reading: 'passages'
};

// Batch size per pillar
export const activeBatches = {
  vocab: '20',
  kanji: '20',
  grammar: '10',
  reading: 'all'
};

/**
 * Switch Sub-Tab inside Vocab Hub ('units' | 'srs' | 'hard' | 'tests')
 */
export function setVocabSubTab(tab) {
  activeSubTabs.vocab = tab;
  updateSubTabsUI('vocab', tab);

  const unitsPane = document.getElementById('vocab-pane-units');
  const srsPane = document.getElementById('vocab-pane-srs');
  const hardPane = document.getElementById('vocab-pane-hard');
  const testsPane = document.getElementById('vocab-pane-tests');

  if (unitsPane) unitsPane.style.display = tab === 'units' ? 'block' : 'none';
  if (srsPane) srsPane.style.display = tab === 'srs' ? 'block' : 'none';
  if (hardPane) hardPane.style.display = tab === 'hard' ? 'block' : 'none';
  if (testsPane) testsPane.style.display = tab === 'tests' ? 'block' : 'none';

  if (tab === 'units') {
    renderChapterChips();
    renderVocabList();
  } else if (tab === 'srs') {
    renderVocabSRSPane();
  } else if (tab === 'hard') {
    renderVocabHardPane();
  } else if (tab === 'tests') {
    renderVocabTestsPane();
  }
}

/**
 * Switch Sub-Tab inside Kanji Hub ('target' | 'srs' | 'hard' | 'exercises')
 */
export function setKanjiSubTab(tab) {
  activeSubTabs.kanji = tab;
  updateSubTabsUI('kanji', tab);

  const targetPane = document.getElementById('kanji-pane-target');
  const srsPane = document.getElementById('kanji-pane-srs');
  const hardPane = document.getElementById('kanji-pane-hard');
  const exercisesPane = document.getElementById('kanji-pane-exercises');

  // Hide all kanji tab panes first
  document.querySelectorAll('#view-kanji .kanji-view-container').forEach(el => {
    el.style.display = 'none';
  });

  if (tab === 'target') {
    if (targetPane) targetPane.style.display = 'block';
    setKanjiTab('target');
  } else if (tab === 'srs') {
    if (srsPane) srsPane.style.display = 'block';
    renderKanjiSRSPane();
  } else if (tab === 'hard') {
    if (hardPane) hardPane.style.display = 'block';
    renderKanjiHardPane();
  } else if (tab === 'exercises') {
    if (exercisesPane) exercisesPane.style.display = 'block';
    setKanjiTab('exercises');
  }
}

/**
 * Switch Sub-Tab inside Grammar Hub ('patterns' | 'srs' | 'hard' | 'drills')
 */
export function setGrammarSubTab(tab) {
  activeSubTabs.grammar = tab;
  updateSubTabsUI('grammar', tab);

  const patternsPane = document.getElementById('grammar-pane-patterns');
  const srsPane = document.getElementById('grammar-pane-srs');
  const hardPane = document.getElementById('grammar-pane-hard');
  const drillsPane = document.getElementById('grammar-pane-drills');

  // Hide all grammar panes first
  const allPanes = ['patterns', 'srs', 'hard', 'drills', 'star', 'text', 'mock', 'guide'];
  allPanes.forEach(p => {
    const el = document.getElementById(`grammar-pane-${p}`);
    if (el) el.style.display = 'none';
  });

  if (tab === 'patterns') {
    if (patternsPane) patternsPane.style.display = 'block';
    setGrammarTab('patterns');
  } else if (tab === 'srs') {
    if (srsPane) srsPane.style.display = 'block';
    renderGrammarSRSPane();
  } else if (tab === 'hard') {
    if (hardPane) hardPane.style.display = 'block';
    renderGrammarHardPane();
  } else if (tab === 'drills') {
    if (drillsPane) drillsPane.style.display = 'block';
    setGrammarTab('drills');
  }
}

/**
 * Switch Sub-Tab inside Reading Hub ('passages' | 'srs' | 'hard' | 'tests')
 */
export function setReadingSubTab(tab) {
  activeSubTabs.reading = tab;
  updateSubTabsUI('reading', tab);

  const passagesPane = document.getElementById('reading-pane-passages');
  const srsPane = document.getElementById('reading-pane-srs');
  const hardPane = document.getElementById('reading-pane-hard');
  const testsPane = document.getElementById('reading-pane-tests');

  if (passagesPane) passagesPane.style.display = tab === 'passages' ? 'block' : 'none';
  if (srsPane) srsPane.style.display = tab === 'srs' ? 'block' : 'none';
  if (hardPane) hardPane.style.display = tab === 'hard' ? 'block' : 'none';
  if (testsPane) testsPane.style.display = tab === 'tests' ? 'block' : 'none';

  if (tab === 'passages') {
    renderReadingView();
  } else if (tab === 'srs') {
    renderReadingSRSPane();
  } else if (tab === 'hard') {
    renderReadingHardPane();
  } else if (tab === 'tests') {
    renderReadingTestsPane();
  }
}

/**
 * Updates button active states in a pillar's sub-tab bar
 */
function updateSubTabsUI(pillar, activeTab) {
  const container = document.getElementById(`subtabs-${pillar}`);
  if (!container) return;
  container.querySelectorAll('.pst-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-sub') === activeTab);
  });
}

// =======================================================
// 1. VOCABULARY SUB-PANES
// =======================================================

export function renderVocabSRSPane() {
  const container = document.getElementById('vocab-srs-container');
  if (!container) return;

  if (!(state.selectedDueVocabChapters instanceof Set)) {
    state.selectedDueVocabChapters = new Set();
  }

  const now = Date.now();
  const dueChaptersCount = {};
  for (const key in (state.stats || {})) {
    const s = state.stats[key];
    if (!s || !s.nextDue || s.nextDue > now) continue;
    if (getPillarFromKey(key) === 'vocab') {
      const resolved = resolveItemForKey(key, s);
      const ch = resolved.chapter;
      if (ch) {
        dueChaptersCount[ch] = (dueChaptersCount[ch] || 0) + 1;
      }
    }
  }

  const formatChLabel = (chId) => {
    const s = String(chId);
    if (s.startsWith('part2_')) return 'C' + s.slice(6);
    if (s.startsWith('review_')) return 'R' + s.slice(7);
    return 'T' + s.padStart(2, '0');
  };

  const sortChapters = (a, b) => {
    const sa = String(a);
    const sb = String(b);
    const getScore = (s) => {
      if (s.startsWith('part2_')) return 2000 + (parseInt(s.slice(6), 10) || 0);
      if (s.startsWith('review_')) return 1000 + (parseInt(s.slice(7), 10) || 0);
      return parseInt(s, 10) || 0;
    };
    return getScore(sa) - getScore(sb);
  };

  const dueChaptersList = Object.keys(dueChaptersCount).sort(sortChapters);
  const totalDeckDue = getDueItemsCount('vocab');
  const hasFilter = state.selectedDueVocabChapters.size > 0;
  const isAllSelected = !hasFilter;
  const dueCount = hasFilter ? getDueItemsCount('vocab', state.selectedDueVocabChapters) : totalDeckDue;
  const currentBatch = activeBatches.vocab;
  const effectiveBatchCount = currentBatch === 'all' ? dueCount : Math.min(dueCount, parseInt(currentBatch, 10));

  const filterList = hasFilter ? Array.from(state.selectedDueVocabChapters).sort(sortChapters).map(formatChLabel).join(', ') : '';
  const filterBadgeHtml = hasFilter
    ? `<span class="badge badge-accent" style="margin-left: 0.5rem;"><i class="fa-solid fa-filter"></i> ${filterList}</span>`
    : '';

  const subLabel = hasFilter 
    ? `words due in selected chapters (${totalDeckDue} due overall in deck)`
    : `words due for review right now`;

  let filterGridHtml = '';
  if (dueChaptersList.length > 0) {
    const allChipHtml = `
      <button class="due-chip ${isAllSelected ? 'selected' : ''}" onclick="window.N3BookPlatform.toggleAllVocabDueChapters()">
        All
        <span class="due-chip-count">${totalDeckDue}</span>
      </button>
    `;
    const chapterChipsHtml = dueChaptersList.map(chId => {
      const isSel = state.selectedDueVocabChapters.has(chId) || state.selectedDueVocabChapters.has(String(chId));
      const lbl = formatChLabel(chId);
      const meta = state.chapterMetadata?.[chId] || {};
      const tooltip = `${lbl}: ${meta.topic_ja || chId} (${dueChaptersCount[chId]} due)`;
      return `
        <button class="due-chip ${isSel ? 'selected' : ''}" title="${tooltip}" onclick="window.N3BookPlatform.toggleVocabDueChapter('${chId}')">
          ${lbl}
          <span class="due-chip-count">${dueChaptersCount[chId]}</span>
        </button>
      `;
    }).join('');

    filterGridHtml = `
      <div class="due-chapter-filter-section">
        <div class="due-filter-header">
          <span class="due-filter-title"><i class="fa-solid fa-filter"></i> Filter by Chapter:</span>
          <span style="font-size: 0.72rem; color: var(--text-dim);">${hasFilter ? `${state.selectedDueVocabChapters.size} selected` : 'All due chapters'}</span>
        </div>
        <div class="due-chapter-grid">
          ${allChipHtml}
          ${chapterChipsHtml}
        </div>
      </div>
    `;
  }

  container.innerHTML = `
    <div class="pillar-srs-card">
      <div class="psc-header">
        <div class="psc-title"><i class="fa-solid fa-bolt" style="color: var(--accent);"></i> 語彙 SRS復習 (Vocabulary Reviews) ${filterBadgeHtml}</div>
        <span class="badge ${dueCount > 0 ? 'badge-accent' : 'badge-green'}">${dueCount > 0 ? `${dueCount} Due` : 'Caught Up'}</span>
      </div>
      <div class="psc-count-box">
        <span class="psc-count">${dueCount}</span>
        <span class="psc-count-label">${subLabel}</span>
      </div>
      ${filterGridHtml}
      <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5; margin-top: 0.75rem;">
        Spaced repetition flashcards with bidirectional recall, audio pronunciation, and automatic interval progression.
      </p>
      <div class="today-batch-selector" style="margin-top: 1rem;">
        <span class="batch-label">Batch Size:</span>
        <button class="batch-chip ${currentBatch === '10' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('vocab', '10')">10</button>
        <button class="batch-chip ${currentBatch === '20' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('vocab', '20')">20</button>
        <button class="batch-chip ${currentBatch === '40' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('vocab', '40')">40</button>
        <button class="batch-chip ${currentBatch === 'all' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('vocab', 'all')">All</button>
      </div>
      <div class="psc-actions">
        <button class="btn btn-primary psc-btn-launch" ${dueCount === 0 ? 'disabled' : ''} onclick="window.N3BookPlatform.startPillarSRS('vocab')">
          <i class="fa-solid fa-play"></i> Start Vocab Flashcards (${dueCount} words · ~${Math.ceil(effectiveBatchCount * 0.5)} min)
        </button>
      </div>
    </div>
  `;
}

export function renderVocabHardPane() {
  const container = document.getElementById('vocab-hard-container');
  if (!container) return;

  const hardWords = [];
  for (const chId in (state.vocabDB || {})) {
    for (const w of (state.vocabDB[chId] || [])) {
      const s = getItemStats(`V:${w.id}`);
      if (s.isHard || (s.weight || 1.0) >= 1.2 || s.lapses >= 3) {
        hardWords.push({ ...w, stats: s });
      }
    }
  }

  // Update badge
  const badge = document.getElementById('subtab-vocab-hard-badge');
  if (badge) badge.textContent = hardWords.length;

  if (hardWords.length === 0) {
    container.innerHTML = `
      <div class="empty-state" style="padding: 3rem 1rem; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🎉</div>
        <h3 style="color: #fff; margin-bottom: 0.5rem;">No Struggling Words!</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem;">
          Any vocabulary marked with the flame <i class="fa-solid fa-fire" style="color: #ef4444;"></i> or repeatedly missed in flashcards will appear here for focused drill.
        </p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="pillar-hard-header">
      <div class="phh-info">
        <div class="phh-title"><i class="fa-solid fa-fire" style="color: #ef4444;"></i> 苦手単語 (Hard Vocabulary)</div>
        <div class="phh-sub">${hardWords.length} words flagged for active recall practice</div>
      </div>
      <button class="btn btn-primary phh-drill-btn" onclick="window.drillAllHardWords()">
        <i class="fa-solid fa-rotate"></i> Drill All Hard (${hardWords.length})
      </button>
    </div>
    <div class="vocab-list">
      ${hardWords.map(w => `
        <div class="vocab-card hard-card">
          <div class="vc-top">
            <div class="vc-ja-group">
              <span class="vc-kanji">${w.word_ja}</span>
              <span class="vc-reading">${w.reading_hiragana}</span>
            </div>
            <div class="vc-actions">
              <button class="btn-icon" onclick="window.playAudio ? window.playAudio('${w.id}') : null" title="Listen">
                <i class="fa-solid fa-volume-high"></i>
              </button>
              <button class="btn-hard-flame active" onclick="window.onToggleHard('${w.id}'); window.N3BookPlatform.renderHard('vocab');" title="Remove from Hard">
                <i class="fa-solid fa-fire"></i>
              </button>
            </div>
          </div>
          <div class="vc-en">${w.meaning_en}</div>
        </div>
      `).join('')}
    </div>
  `;
}

export function renderVocabTestsPane() {
  const container = document.getElementById('vocab-tests-container');
  if (!container) return;
  const tests = (typeof window.getAllAvailableTests === 'function' ? window.getAllAvailableTests() : []).filter(t => t.pillar === 'vocab');

  container.innerHTML = `
    <div class="view-header" style="margin-bottom: 1rem;">
      <div class="view-title-group">
        <h3>語彙 総合問題 (Vocab Chapter Tests)</h3>
      </div>
    </div>
    <div class="tests-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
      ${tests.map(t => `
        <div class="stat-card" style="cursor: pointer; border-left: 3px solid var(--accent);" onclick="window.startTestSession('${t.id}')">
          <div style="font-weight: 700; color: #fff; margin-bottom: 0.35rem;">${t.title}</div>
          <div style="color: var(--text-muted); font-size: 0.82rem; margin-bottom: 0.75rem;">${t.subTitle || `${t.questionCount} Questions`}</div>
          <button class="btn btn-sm btn-outline-accent"><i class="fa-solid fa-play"></i> Start Test (${t.questionCount} Qs)</button>
        </div>
      `).join('')}
    </div>
  `;
}

// =======================================================
// 2. KANJI SUB-PANES
// =======================================================

export function renderKanjiSRSPane() {
  const container = document.getElementById('kanji-srs-container');
  if (!container) return;

  if (!(state.selectedDueKanjiLessons instanceof Set)) {
    state.selectedDueKanjiLessons = new Set();
  }

  const now = Date.now();
  const dueLessonsCount = {};
  for (const key in (state.stats || {})) {
    const s = state.stats[key];
    if (!s || !s.nextDue || s.nextDue > now) continue;
    if (getPillarFromKey(key) === 'kanji') {
      const resolved = resolveItemForKey(key, s);
      const lNum = resolved.lesson_number;
      if (lNum) {
        dueLessonsCount[lNum] = (dueLessonsCount[lNum] || 0) + 1;
      }
    }
  }

  const dueLessonsList = Object.keys(dueLessonsCount).map(Number).sort((a, b) => a - b);
  const totalDeckDue = getDueItemsCount('kanji');
  const hasFilter = state.selectedDueKanjiLessons.size > 0;
  const isAllSelected = !hasFilter;
  const dueCount = hasFilter ? getDueItemsCount('kanji', state.selectedDueKanjiLessons) : totalDeckDue;
  const currentBatch = activeBatches.kanji;
  const effectiveBatchCount = currentBatch === 'all' ? dueCount : Math.min(dueCount, parseInt(currentBatch, 10));

  const filterList = hasFilter ? Array.from(state.selectedDueKanjiLessons).sort((a, b) => a - b).map(l => `L${String(l).padStart(2, '0')}`).join(', ') : '';
  const filterBadgeHtml = hasFilter
    ? `<span class="badge badge-cyan" style="margin-left: 0.5rem;"><i class="fa-solid fa-filter"></i> ${filterList}</span>`
    : '';

  const subLabel = hasFilter 
    ? `kanji items due in selected lessons (${totalDeckDue} due overall in deck)`
    : `kanji readings &amp; characters due right now`;

  let filterGridHtml = '';
  if (dueLessonsList.length > 0) {
    const allChipHtml = `
      <button class="due-chip cyan ${isAllSelected ? 'selected' : ''}" onclick="window.N3BookPlatform.toggleAllKanjiDueLessons()">
        All
        <span class="due-chip-count">${totalDeckDue}</span>
      </button>
    `;
    const lessonChipsHtml = dueLessonsList.map(lNum => {
      const isSel = state.selectedDueKanjiLessons.has(lNum) || state.selectedDueKanjiLessons.has(String(lNum));
      const lbl = `L${String(lNum).padStart(2, '0')}`;
      return `
        <button class="due-chip cyan ${isSel ? 'selected' : ''}" title="Lesson ${lNum} (${dueLessonsCount[lNum]} due)" onclick="window.N3BookPlatform.toggleKanjiDueLesson(${lNum})">
          ${lbl}
          <span class="due-chip-count">${dueLessonsCount[lNum]}</span>
        </button>
      `;
    }).join('');

    filterGridHtml = `
      <div class="due-chapter-filter-section">
        <div class="due-filter-header">
          <span class="due-filter-title" style="color: var(--cyan);"><i class="fa-solid fa-filter"></i> Filter by Lesson:</span>
          <span style="font-size: 0.72rem; color: var(--text-dim);">${hasFilter ? `${state.selectedDueKanjiLessons.size} selected` : 'All due lessons'}</span>
        </div>
        <div class="due-chapter-grid">
          ${allChipHtml}
          ${lessonChipsHtml}
        </div>
      </div>
    `;
  }

  container.innerHTML = `
    <div class="pillar-srs-card">
      <div class="psc-header">
        <div class="psc-title"><i class="fa-solid fa-bolt" style="color: var(--cyan);"></i> 漢字 SRS復習 (Kanji Reviews) ${filterBadgeHtml}</div>
        <span class="badge ${dueCount > 0 ? 'badge-cyan' : 'badge-green'}">${dueCount > 0 ? `${dueCount} Due` : 'Caught Up'}</span>
      </div>
      <div class="psc-count-box">
        <span class="psc-count" style="color: var(--cyan);">${dueCount}</span>
        <span class="psc-count-label">${subLabel}</span>
      </div>
      ${filterGridHtml}
      <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5; margin-top: 0.75rem;">
        Multi-facet SRS: character recognition (K:), reading identification (KWR:), and writing recall (KWW:).
      </p>
      <div class="today-batch-selector" style="margin-top: 1rem;">
        <span class="batch-label">Batch Size:</span>
        <button class="batch-chip ${currentBatch === '10' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('kanji', '10')">10</button>
        <button class="batch-chip ${currentBatch === '20' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('kanji', '20')">20</button>
        <button class="batch-chip ${currentBatch === '40' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('kanji', '40')">40</button>
        <button class="batch-chip ${currentBatch === 'all' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('kanji', 'all')">All</button>
      </div>
      <div class="psc-actions">
        <button class="btn btn-primary psc-btn-launch" ${dueCount === 0 ? 'disabled' : ''} onclick="window.N3BookPlatform.startPillarSRS('kanji')">
          <i class="fa-solid fa-play"></i> Launch Kanji Runner (${dueCount} items · ~${Math.ceil(effectiveBatchCount * 0.5)} min)
        </button>
      </div>
    </div>
  `;
}

export function renderKanjiHardPane() {
  const container = document.getElementById('kanji-hard-container');
  if (!container) return;

  const hardChars = [];
  for (const char in (state.kanjiDB || {})) {
    const s = getItemStats(`K:${char}`);
    if (s.isHard || (s.weight || 1.0) >= 1.2 || s.lapses >= 3) {
      hardChars.push({ char, ...state.kanjiDB[char], stats: s });
    }
  }

  // Update badge
  const badge = document.getElementById('subtab-kanji-hard-badge');
  if (badge) badge.textContent = hardChars.length;

  if (hardChars.length === 0) {
    container.innerHTML = `
      <div class="empty-state" style="padding: 3rem 1rem; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🎉</div>
        <h3 style="color: #fff; margin-bottom: 0.5rem;">No Struggling Kanji!</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem;">
          Any kanji marked with the flame <i class="fa-solid fa-fire" style="color: #ef4444;"></i> or repeatedly failed will appear here for targeted drill.
        </p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="pillar-hard-header">
      <div class="phh-info">
        <div class="phh-title"><i class="fa-solid fa-fire" style="color: #ef4444;"></i> 苦手漢字 (Hard Kanji &amp; Leeches)</div>
        <div class="phh-sub">${hardChars.length} characters flagged for mastery drill</div>
      </div>
      <button class="btn btn-primary phh-drill-btn" onclick="window.N3BookPlatform.drillHardKanji()">
        <i class="fa-solid fa-rotate"></i> Drill Hard Kanji (${hardChars.length})
      </button>
    </div>
    <div class="kanji-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 0.75rem;">
      ${hardChars.map(k => `
        <div class="kanji-card hard-kanji-card" onclick="window.drillKanjiSingle('${k.char}')" style="cursor: pointer; background: var(--bg2); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 0.85rem; text-align: center;">
          <div style="font-size: 2.2rem; font-weight: 800; color: #fff; margin-bottom: 0.25rem;">${k.char}</div>
          <div style="font-size: 0.75rem; color: #f472b6; font-weight: 600;">${(k.onyomi || []).slice(0, 2).join('・')}</div>
          <div style="font-size: 0.75rem; color: var(--text-muted);">${(k.meanings || []).slice(0, 2).join(', ')}</div>
        </div>
      `).join('')}
    </div>
  `;
}

// =======================================================
// 3. GRAMMAR SUB-PANES
// =======================================================

export function renderGrammarSRSPane() {
  const container = document.getElementById('grammar-srs-container');
  if (!container) return;
  const dueCount = getDueItemsCount('grammar');
  const currentBatch = activeBatches.grammar;

  container.innerHTML = `
    <div class="pillar-srs-card">
      <div class="psc-header">
        <div class="psc-title"><i class="fa-solid fa-bolt" style="color: var(--amber);"></i> 文法 SRS復習 (Grammar Reviews)</div>
        <span class="badge ${dueCount > 0 ? 'badge-amber' : 'badge-green'}">${dueCount > 0 ? `${dueCount} Due` : 'Caught Up'}</span>
      </div>
      <div class="psc-count-box">
        <span class="psc-count" style="color: var(--amber);">${dueCount}</span>
        <span class="psc-count-label">star blanks (★) &amp; decision questions due</span>
      </div>
      <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5;">
        Grammar sentence ordering and meaning discrimination drills calibrated with interleaved cluster reviews.
      </p>
      <div class="today-batch-selector" style="margin-top: 1rem;">
        <span class="batch-label">Batch Size:</span>
        <button class="batch-chip ${currentBatch === '10' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('grammar', '10')">10</button>
        <button class="batch-chip ${currentBatch === '20' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('grammar', '20')">20</button>
        <button class="batch-chip ${currentBatch === 'all' ? 'active' : ''}" onclick="window.N3BookPlatform.setBatch('grammar', 'all')">All</button>
      </div>
      <div class="psc-actions">
        <button class="btn btn-primary psc-btn-launch" ${dueCount === 0 ? 'disabled' : ''} onclick="window.N3BookPlatform.startPillarSRS('grammar')">
          <i class="fa-solid fa-play"></i> Start Grammar Star SRS (~${Math.ceil((currentBatch === 'all' ? dueCount : parseInt(currentBatch, 10)) * 0.7)} min)
        </button>
      </div>
    </div>
  `;
}

export function renderGrammarHardPane() {
  const container = document.getElementById('grammar-hard-container');
  if (!container) return;

  const patterns = state.grammarDB?.index || [];
  const hardPatterns = patterns.filter(p => {
    const s = getItemStats(`G:${p.id}`);
    return s.isHard || (s.weight || 1.0) >= 1.2 || s.lapses >= 2;
  });

  // Update badge
  const badge = document.getElementById('subtab-grammar-hard-badge');
  if (badge) badge.textContent = hardPatterns.length;

  container.innerHTML = `
    <div class="pillar-hard-header">
      <div class="phh-info">
        <div class="phh-title"><i class="fa-solid fa-fire" style="color: #ef4444;"></i> 苦手文法 &amp; 混同しやすい文型 (Confusion Clusters)</div>
        <div class="phh-sub">Patterns with similar forms or meanings that cause exam errors</div>
      </div>
    </div>
    <div id="grammar-clusters-box" style="margin-top: 1rem;">
      <!-- Populated with cluster cards -->
    </div>
  `;

  // Render clusters if available
  if (typeof window.N3GrammarSRS?.renderClustersToContainer === 'function') {
    window.N3GrammarSRS.renderClustersToContainer('grammar-clusters-box');
  }
}

// =======================================================
// 4. READING SUB-PANES
// =======================================================

export function renderReadingSRSPane() {
  const container = document.getElementById('reading-srs-container');
  if (!container) return;
  const dueCount = getDueItemsCount('reading');

  container.innerHTML = `
    <div class="pillar-srs-card">
      <div class="psc-header">
        <div class="psc-title"><i class="fa-solid fa-bolt" style="color: var(--green);"></i> 読解 再読SRS (Re-Read Loops)</div>
        <span class="badge ${dueCount > 0 ? 'badge-green' : 'badge-green'}">${dueCount > 0 ? `${dueCount} Due` : 'Caught Up'}</span>
      </div>
      <div class="psc-count-box">
        <span class="psc-count" style="color: var(--green);">${dueCount}</span>
        <span class="psc-count-label">passages due for second-pass speed reading</span>
      </div>
      <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.5;">
        Layer A 3-step re-read schedule (+3d, +10d, +25d) with real-time 330 CPM pacing timer and comprehension verification.
      </p>
      <div class="psc-actions">
        <button class="btn btn-primary psc-btn-launch" ${dueCount === 0 ? 'disabled' : ''} onclick="window.N3BookPlatform.startPillarSRS('reading')">
          <i class="fa-solid fa-book-reader"></i> Begin Second-Pass Re-Read Loop
        </button>
      </div>
    </div>
  `;
}

export function renderReadingHardPane() {
  const container = document.getElementById('reading-hard-container');
  if (!container) return;

  const missedQs = [];
  for (const lid in (state.readingDB || {})) {
    const lesson = state.readingDB[lid] || {};
    const questions = lesson.comprehensionQuestions || lesson.questions || [];
    for (const q of questions) {
      const qId = q.id || `${lid}_q${q.questionNumber || 1}`;
      const s = getItemStats(`R_Q:${qId}`);
      if (s.isHard || (s.weight || 1.0) >= 1.2 || s.incorrect > 0) {
        missedQs.push({ ...q, id: qId, lessonId: lid, lessonTitle: lesson.title_ja || lesson.title, stats: s });
      }
    }
  }

  // Update badge
  const badge = document.getElementById('subtab-reading-hard-badge');
  if (badge) badge.textContent = missedQs.length;

  if (missedQs.length === 0) {
    container.innerHTML = `
      <div class="empty-state" style="padding: 3rem 1rem; text-align: center;">
        <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🎉</div>
        <h3 style="color: #fff; margin-bottom: 0.5rem;">No Missed Reading Questions!</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem;">
          Comprehension questions missed during timed drills will appear here for targeted review.
        </p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div class="pillar-hard-header">
      <div class="phh-info">
        <div class="phh-title"><i class="fa-solid fa-fire" style="color: #ef4444;"></i> 読解 誤答問題 (Missed Questions)</div>
        <div class="phh-sub">${missedQs.length} reading questions missed in past quizzes</div>
      </div>
    </div>
    <div class="reading-missed-list" style="display: flex; flex-direction: column; gap: 0.75rem;">
      ${missedQs.map(q => `
        <div class="stat-card" style="border-left: 3px solid #ef4444; padding: 1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span class="badge badge-cyan">${q.lessonTitle}</span>
            <button class="btn btn-sm btn-outline" onclick="window.openReadingLesson('${q.lessonId}')">Open Passage</button>
          </div>
          <div style="color: #fff; font-size: 0.95rem; font-weight: 600; line-height: 1.4;">${q.question_ja || q.question}</div>
        </div>
      `).join('')}
    </div>
  `;
}

export function renderReadingTestsPane() {
  const container = document.getElementById('reading-tests-container');
  if (!container) return;
  const tests = (typeof window.getAllAvailableTests === 'function' ? window.getAllAvailableTests() : []).filter(t => t.pillar === 'reading');

  container.innerHTML = `
    <div class="view-header" style="margin-bottom: 1rem;">
      <div class="view-title-group">
        <h3>読解 実戦テスト (Reading Comprehension Tests)</h3>
      </div>
    </div>
    <div class="tests-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
      ${tests.map(t => `
        <div class="stat-card" style="cursor: pointer; border-left: 3px solid var(--cyan);" onclick="window.startTestSession('${t.id}')">
          <div style="font-weight: 700; color: #fff; margin-bottom: 0.35rem;">${t.title}</div>
          <div style="color: var(--text-muted); font-size: 0.82rem; margin-bottom: 0.75rem;">${t.subTitle || `${t.questionCount} Questions`}</div>
          <button class="btn btn-sm btn-outline-cyan"><i class="fa-solid fa-play"></i> Start Test (${t.questionCount} Qs)</button>
        </div>
      `).join('')}
    </div>
  `;
}

// =======================================================
// SETTINGS & BACKUP DRAWER CONTROLLER
// =======================================================

export function openSettingsDrawer() {
  const drawer = document.getElementById('settings-drawer-overlay');
  if (drawer) drawer.classList.add('active');
}

export function closeSettingsDrawer() {
  const drawer = document.getElementById('settings-drawer-overlay');
  if (drawer) drawer.classList.remove('active');
}

// Controller Object exposed on window
export const N3BookPlatform = {
  setVocabSubTab,
  setKanjiSubTab,
  setGrammarSubTab,
  setReadingSubTab,
  openSettings: openSettingsDrawer,
  closeSettings: closeSettingsDrawer,
  setBatch: (pillar, batch) => {
    activeBatches[pillar] = batch;
    if (pillar === 'vocab') renderVocabSRSPane();
    if (pillar === 'kanji') renderKanjiSRSPane();
    if (pillar === 'grammar') renderGrammarSRSPane();
  },
  toggleVocabDueChapter: (chId) => {
    if (!(state.selectedDueVocabChapters instanceof Set)) {
      state.selectedDueVocabChapters = new Set();
    }
    if (state.selectedDueVocabChapters.has(chId) || state.selectedDueVocabChapters.has(String(chId))) {
      state.selectedDueVocabChapters.delete(chId);
      state.selectedDueVocabChapters.delete(String(chId));
    } else {
      state.selectedDueVocabChapters.add(chId);
    }
    renderVocabSRSPane();
  },
  toggleAllVocabDueChapters: () => {
    if (!(state.selectedDueVocabChapters instanceof Set)) {
      state.selectedDueVocabChapters = new Set();
    }
    state.selectedDueVocabChapters.clear();
    renderVocabSRSPane();
  },
  toggleKanjiDueLesson: (lNum) => {
    if (!(state.selectedDueKanjiLessons instanceof Set)) {
      state.selectedDueKanjiLessons = new Set();
    }
    const num = Number(lNum);
    if (state.selectedDueKanjiLessons.has(num) || state.selectedDueKanjiLessons.has(String(num))) {
      state.selectedDueKanjiLessons.delete(num);
      state.selectedDueKanjiLessons.delete(String(num));
    } else {
      state.selectedDueKanjiLessons.add(num);
    }
    renderKanjiSRSPane();
  },
  toggleAllKanjiDueLessons: () => {
    if (!(state.selectedDueKanjiLessons instanceof Set)) {
      state.selectedDueKanjiLessons = new Set();
    }
    state.selectedDueKanjiLessons.clear();
    renderKanjiSRSPane();
  },
  startPillarSRS: (pillar) => {
    const limit = activeBatches[pillar] === 'all' ? 100 : parseInt(activeBatches[pillar], 10);
    state.dueBatchSize = limit;
    let filter = null;
    if (pillar === 'vocab') {
      if (state.selectedDueVocabChapters && state.selectedDueVocabChapters.size > 0) {
        filter = state.selectedDueVocabChapters;
      }
    } else if (pillar === 'kanji') {
      if (state.selectedDueKanjiLessons && state.selectedDueKanjiLessons.size > 0) {
        filter = state.selectedDueKanjiLessons;
      }
    }
    if (typeof window.startDueReview === 'function') {
      window.startDueReview(pillar, filter);
    }
  },
  drillHardKanji: () => {
    if (typeof window.drillKanjiHard === 'function') {
      window.drillKanjiHard();
    } else if (typeof window.startDueReview === 'function') {
      window.startDueReview('kanji');
    }
  },
  renderHard: (pillar) => {
    if (pillar === 'vocab') renderVocabHardPane();
    if (pillar === 'kanji') renderKanjiHardPane();
    if (pillar === 'grammar') renderGrammarHardPane();
    if (pillar === 'reading') renderReadingHardPane();
  }
};

if (typeof window !== 'undefined') {
  window.N3BookPlatform = N3BookPlatform;
  window.setVocabSubTab = setVocabSubTab;
  window.setKanjiSubTab = setKanjiSubTab;
  window.setGrammarSubTab = setGrammarSubTab;
  window.setReadingSubTab = setReadingSubTab;
  window.openSettingsDrawer = openSettingsDrawer;
  window.closeSettingsDrawer = closeSettingsDrawer;
}
