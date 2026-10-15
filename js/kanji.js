/* =======================================================
   NIHONGO INTERMEDIATE — kanji.js
   Book 4: Shin Kanzen Master Kanji N3 Interactive Workspace
   - 443 Target Kanji Browser & Flashcard Launcher
   - Practice Exercises Drill Runner (Parts 1 to 5)
   - Bessatsu 300 Review Kanji (N4/N5) Explorer
   - Bessatsu Special Readings (21 irregular items)
   - Mock Exams 1 & 2 Runner (JLPT Q1 & Q2)
   - getKanjiBreakdown(text) Cross-Book Lookup Engine
   ======================================================= */

import { state } from './state.js';
import { beginGistReviewSession } from './gist-sync.js';
import { getKanjiStatus, toggleKanjiHard, updateItemStats, getItemStatus } from './srs.js';
import { startStudy, renderCard } from './study.js?v=3.4';
import { showView } from './navigation.js';
import { getKanjiBreakdownPills } from './kanji-words.js';

// =======================================================
// 1. MASTER VIEW RENDERER & TAB SWITCHING
// =======================================================

export function renderKanjiView() {
  const tab = state.kanjiActiveTab || 'target';
  
  // Highlight active tab
  document.querySelectorAll('.kanji-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-tab') === tab);
  });

  const targetPane = document.getElementById('kanji-pane-target');
  const exPane = document.getElementById('kanji-pane-exercises');
  const r300Pane = document.getElementById('kanji-pane-review300');
  const specialPane = document.getElementById('kanji-pane-special');
  const mockPane = document.getElementById('kanji-pane-mock');

  if (targetPane) targetPane.style.display = tab === 'target' ? 'block' : 'none';
  if (exPane) exPane.style.display = tab === 'exercises' ? 'block' : 'none';
  if (r300Pane) r300Pane.style.display = tab === 'review300' ? 'block' : 'none';
  if (specialPane) specialPane.style.display = tab === 'special' ? 'block' : 'none';
  if (mockPane) mockPane.style.display = tab === 'mock' ? 'block' : 'none';

  if (tab === 'target') {
    renderKanjiLessonChips();
    renderKanjiTargetGrid();
    updateKanjiActionButtonLabels();
  } else if (tab === 'exercises') {
    renderKanjiExercises();
  } else if (tab === 'review300') {
    renderKanjiReview300();
  } else if (tab === 'special') {
    renderKanjiSpecialReadings();
  } else if (tab === 'mock') {
    renderKanjiMockTests();
  }
}

export function setKanjiTab(tab) {
  state.kanjiActiveTab = tab;
  renderKanjiView();
}

// =======================================================
// 2. TARGET KANJI (443) BROWSER & MULTI-LESSON FILTERS
// =======================================================

export function setKanjiStudyDirection(dir) {
  state.kanjiStudyDirection = dir;
  ['ja-kana', 'kana-ja', 'ja-meaning', 'mixed'].forEach(d => {
    const btn = document.getElementById(`kdir-${d}`);
    if (btn) btn.classList.toggle('active', d === dir);
  });
  updateKanjiActionButtonLabels();
}

export function setKanjiPart(part) {
  state.kanjiPart = part === 'all' ? 'all' : parseInt(part, 10);
  populateLessonSelector();
  renderKanjiLessonChips();
  renderKanjiTargetGrid();
  updateKanjiActionButtonLabels();
}

export function setKanjiLesson(les) {
  if (les === 'all') {
    selectKanjiLesson('all');
  } else {
    selectKanjiLesson(parseInt(les, 10), 'replace');
  }
}

export function setKanjiFilter(status) {
  state.kanjiFilter = status;
  renderKanjiTargetGrid();
  updateKanjiActionButtonLabels();
}

export function onKanjiSearch(query) {
  state.kanjiSearchQuery = (query || '').trim().toLowerCase();
  renderKanjiTargetGrid();
  updateKanjiActionButtonLabels();
}

export function populateLessonSelector() {
  const sel = document.getElementById('kanji-lesson-select');
  if (!sel) return;
  
  sel.innerHTML = '<option value="all">All Lessons (1–25)</option>';
  const lessons = (state.kanjiLessons || []).filter(l => {
    return state.kanjiPart === 'all' || l.part === state.kanjiPart;
  });

  lessons.forEach(l => {
    const opt = document.createElement('option');
    opt.value = l.lesson_number;
    opt.textContent = `Lesson ${l.lesson_number}: ${l.title_ja}`;
    if (state.kanjiLesson === l.lesson_number) opt.selected = true;
    sel.appendChild(opt);
  });
}

export function renderKanjiLessonChips() {
  const container = document.getElementById('kanji-lesson-chips-row');
  if (!container) return;
  container.innerHTML = '';

  if (!(state.kanjiSelectedLessons instanceof Set)) {
    state.kanjiSelectedLessons = new Set();
  }

  const isAll = state.kanjiSelectedLessons.size === 0;

  // "All Lessons" chip
  const allChip = document.createElement('button');
  allChip.className = `kanji-lesson-chip ${isAll ? 'active' : ''}`;
  allChip.innerHTML = `${isAll ? '<i class="fa-solid fa-check"></i> ' : ''}All Lessons (1–25)`;
  allChip.onclick = () => selectKanjiLesson('all');
  container.appendChild(allChip);

  // Lessons 1 to 25
  for (let i = 1; i <= 25; i++) {
    const isSel = state.kanjiSelectedLessons.has(i);
    const chip = document.createElement('button');
    chip.className = `kanji-lesson-chip ${isSel ? 'active selected' : ''}`;

    let wordsCount = 0;
    for (const char in (state.kanjiDB || {})) {
      const k = state.kanjiDB[char];
      if (k && k.lesson_number === i) {
        wordsCount += (k.words || []).length;
      }
    }

    chip.innerHTML = `${isSel ? '<i class="fa-solid fa-check"></i> ' : ''}L${i} <span style="font-size: 0.72rem; opacity: 0.85;">(${wordsCount}w)</span>`;
    chip.onclick = () => selectKanjiLesson(i, 'toggle');
    container.appendChild(chip);
  }
}

export function selectKanjiLesson(lessonNum, mode = 'toggle') {
  if (!(state.kanjiSelectedLessons instanceof Set)) {
    state.kanjiSelectedLessons = new Set();
  }

  if (lessonNum === 'all') {
    state.kanjiSelectedLessons.clear();
    state.kanjiLesson = 'all';
  } else {
    const num = Number(lessonNum);
    if (mode === 'toggle') {
      if (state.kanjiSelectedLessons.has(num)) {
        state.kanjiSelectedLessons.delete(num);
      } else {
        state.kanjiSelectedLessons.add(num);
      }
    } else {
      state.kanjiSelectedLessons.clear();
      state.kanjiSelectedLessons.add(num);
    }
    state.kanjiLesson = state.kanjiSelectedLessons.size === 1 ? Array.from(state.kanjiSelectedLessons)[0] : 'all';
  }

  renderKanjiLessonChips();
  renderKanjiTargetGrid();
  updateKanjiActionButtonLabels();
  if (typeof window.renderPillarSRS === 'function' && state.kanjiSubTab === 'srs') {
    window.renderPillarSRS('kanji');
  }
}

export function renderKanjiTargetGrid() {
  const grid = document.getElementById('kanji-grid');
  const countEl = document.getElementById('kanji-count-badge');
  if (!grid) return;

  grid.innerHTML = '';
  const allChars = Object.keys(state.kanjiDB || {});
  const query = state.kanjiSearchQuery || '';
  const selLessons = state.kanjiSelectedLessons || new Set();

  const filtered = allChars.filter(char => {
    const k = state.kanjiDB[char];
    if (!k) return false;

    // Part filter
    if (state.kanjiPart !== 'all' && k.part !== state.kanjiPart) return false;

    // Multi-Lesson selection filter
    if (selLessons.size > 0 && !selLessons.has(k.lesson_number)) return false;

    // Status filter
    const status = getKanjiStatus(char);
    if (state.kanjiFilter !== 'all' && status !== state.kanjiFilter) return false;

    // Search query
    if (query) {
      const matchChar = char.includes(query);
      const matchOn = (k.onyomi || []).some(o => o.toLowerCase().includes(query));
      const matchKun = (k.kunyomi || []).some(ku => ku.toLowerCase().includes(query));
      const matchWords = (k.words || []).some(w => {
        return (w.term_ja && w.term_ja.includes(query)) ||
               (w.reading && w.reading.includes(query)) ||
               (w.meaning_en && w.meaning_en.toLowerCase().includes(query));
      });
      if (!matchChar && !matchOn && !matchKun && !matchWords) return false;
    }

    return true;
  });

  if (countEl) countEl.textContent = `${filtered.length} / 443 Kanji`;

  if (filtered.length === 0) {
    grid.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; color: var(--text-dim); padding: 3rem;">No Kanji matching the current filters.</div>';
    return;
  }

  filtered.forEach(char => {
    const k = state.kanjiDB[char];
    const status = getKanjiStatus(char);
    const card = document.createElement('div');
    card.className = 'kanji-card kanji-card-minimal';
    card.onclick = () => openKanjiModal(char);

    const primaryReading = (k.onyomi && k.onyomi[0]) || (k.kunyomi && k.kunyomi[0]) || '';
    const wordCount = (k.words || []).length;

    // Minimal card presentation on the grid (clean, prominent Kanji character)
    card.innerHTML = `
      <span class="kanji-card-lesson-tag">L${k.lesson_number}</span>
      <span class="kanji-card-status-dot ${status}" title="SRS Status: ${status}"></span>
      <div class="kanji-card-char">${char}</div>
      <div class="kanji-card-sub font-ja">${primaryReading || `${wordCount}w`}</div>
    `;
    grid.appendChild(card);
  });
}

// =======================================================
// 3. KANJI DETAIL MODAL & CROSS-BOOK LOOKUP
// =======================================================

export function openKanjiModal(char) {
  state.activeKanjiModal = char;
  const k = state.kanjiDB[char] || (state.kanjiReview300 || []).find(x => x.kanji === char);
  if (!k) return;

  const modal = document.getElementById('kanji-modal');
  if (!modal) return;

  const bigChar = document.getElementById('km-bigchar');
  const title = document.getElementById('km-title');
  const sub = document.getElementById('km-sub');
  const onEl = document.getElementById('km-onyomi');
  const kunEl = document.getElementById('km-kunyomi');
  const wordsBox = document.getElementById('km-words-list');
  const flameBtn = document.getElementById('km-hard-btn');

  if (bigChar) bigChar.textContent = char;
  if (title) title.textContent = `Lesson ${k.lesson_number || 'Review'}: ${k.lesson_title_ja || ''}`;
  if (sub) sub.textContent = `Part ${k.part || 'N4/N5'} · N3 Kanji Mastery`;

  const onStr = (k.onyomi || []).join('、 ') || '—';
  const kunStr = (k.kunyomi || []).join('、 ') || '—';
  if (onEl) onEl.textContent = onStr;
  if (kunEl) kunEl.textContent = kunStr;

  const isHard = getKanjiStatus(char) === 'hard';
  if (flameBtn) {
    flameBtn.innerHTML = `<i class="fa-solid fa-fire"></i> ${isHard ? 'Struggling (Hard)' : 'Mark as Weak Point'}`;
    flameBtn.className = `btn btn-sm ${isHard ? 'btn-danger' : 'btn-ghost'}`;
  }

  if (wordsBox) {
    wordsBox.innerHTML = '';
    const words = k.words || [];
    if (words.length === 0 && k.examples) {
      // Review 300 structure
      k.examples.forEach(ex => {
        const row = document.createElement('div');
        row.className = 'kanji-word-row';
        row.innerHTML = `
          <div class="kanji-word-term">${ex.example_ruby || ex.example}</div>
          <div class="kanji-word-en">${ex.example_reading}</div>
        `;
        wordsBox.appendChild(row);
      });
    } else {
      words.forEach(w => {
        const row = document.createElement('div');
        row.className = 'kanji-word-row';
        row.innerHTML = `
          <div class="kanji-word-term">${w.ruby_html || w.term_ja}</div>
          <div class="kanji-word-en">${w.meaning_en || ''} ${w.meaning_zh ? `(${w.meaning_zh})` : ''}</div>
        `;
        wordsBox.appendChild(row);
      });
    }
  }

  modal.classList.add('open');
}

export function closeKanjiModal() {
  const modal = document.getElementById('kanji-modal');
  if (modal) modal.classList.remove('open');
  state.activeKanjiModal = null;
}

export function toggleModalKanjiHard() {
  if (!state.activeKanjiModal) return;
  toggleKanjiHard(state.activeKanjiModal);
  openKanjiModal(state.activeKanjiModal);
  renderKanjiTargetGrid();
}

export function drillActiveModalKanji() {
  if (!state.activeKanjiModal) return;
  const char = state.activeKanjiModal;
  closeKanjiModal();
  drillKanjiSingle(char);
}

export function drillKanjiSingle(char) {
  const k = state.kanjiDB[char];
  if (!k) return;
  state.sessionItems = [{ ...k, type: 'kanji', book: 'kanji' }];
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = 1;
  state.cardFlipped = false;
  state.studyMode = 'flashcard';
  state.isDueReviewMode = false;
  state.drillOrigin = 'kanji';
  showView('study');
  renderCard();
}

export function buildKanjiStudyItems(kanjiList, direction = state.kanjiStudyDirection || 'ja-kana') {
  const studyItems = [];
  const seenWords = new Set();
  const MIXED_DIRS = ['ja-kana', 'kana-ja', 'ja-meaning'];

  kanjiList.forEach(k => {
    if (k.words && Array.isArray(k.words) && k.words.length > 0) {
      k.words.forEach(w => {
        const word = (w.term_ja || w.word || k.kanji).trim();
        const reading = (w.reading || (k.kunyomi && k.kunyomi[0]) || (k.onyomi && k.onyomi[0]) || '').trim();
        // 'mixed' picks a random direction per card, so each facet keeps its own SRS key
        const dir = direction === 'mixed' ? MIXED_DIRS[Math.floor(Math.random() * MIXED_DIRS.length)] : direction;
        const key = dir === 'kana-ja' ? `KWW:${word}` : (dir === 'ja-meaning' ? `KWM:${word}` : `KWR:${word}`);

        if (word && !seenWords.has(word)) {
          seenWords.add(word);
          studyItems.push({
            type: 'kanji_word',
            book: 'kanji',
            baseKanji: k.kanji,
            lesson_number: k.lesson_number || 1,
            word: word,
            reading: reading,
            ruby_html: w.ruby_html || word,
            meaning_en: w.meaning_en || '',
            meaning_zh: w.meaning_zh || '',
            onyomi: k.onyomi || [],
            kunyomi: k.kunyomi || [],
            direction: dir,
            key: key
          });
        }
      });
    } else {
      // Fallback for bare kanji without mapped words
      studyItems.push({
        type: 'kanji',
        book: 'kanji',
        baseKanji: k.kanji,
        kanji: k.kanji,
        lesson_number: k.lesson_number || 1,
        onyomi: k.onyomi || [],
        kunyomi: k.kunyomi || [],
        words: k.words || [],
        direction: direction,
        key: `K:${k.kanji}`
      });
    }
  });

  return studyItems;
}

// Hard-only items: every facet (reading / writing / meaning) that is flagged hard,
// plus the reading facet of any word whose base kanji is flagged hard (K: key).
export function buildHardKanjiItems(kanjiList) {
  const out = [];
  ['ja-kana', 'kana-ja', 'ja-meaning'].forEach(dir => {
    buildKanjiStudyItems(kanjiList, dir).forEach(it => {
      if (it.type === 'kanji') {
        if (dir === 'ja-kana' && getItemStatus(it.key) === 'hard') out.push(it);
      } else if (getItemStatus(it.key) === 'hard' ||
                 (dir === 'ja-kana' && getKanjiStatus(it.baseKanji) === 'hard')) {
        out.push(it);
      }
    });
  });
  return out;
}

function selectedKanjiPool() {
  const selLessons = state.kanjiSelectedLessons || new Set();
  const pool = [];
  for (const char in (state.kanjiDB || {})) {
    const k = state.kanjiDB[char];
    if (selLessons.size === 0 || selLessons.has(k.lesson_number)) pool.push(k);
  }
  return pool;
}

export function toggleKanjiHardOnly() {
  state.kanjiHardOnly = !state.kanjiHardOnly;
  updateKanjiActionButtonLabels();
}

export function drillKanjiHard() {
  state.kanjiHardOnly = true;
  drillKanjiSelected();
}

export function updateKanjiActionButtonLabels() {
  const runnerBtn = document.getElementById('btn-kanji-runner-action');
  const selectedLessons = state.kanjiSelectedLessons || new Set();
  if (runnerBtn) {
    runnerBtn.disabled = selectedLessons.size !== 1;
    runnerBtn.title = selectedLessons.size === 1
      ? 'Start the guided S0-S6 flow for the selected lesson'
      : 'Select exactly one lesson chip to start the guided lesson';
  }
  const hardBtn = document.getElementById('btn-kanji-hard-toggle');
  if (hardBtn) {
    const on = Boolean(state.kanjiHardOnly);
    hardBtn.innerHTML = `<i class="fa-solid fa-fire"></i> Hard only: ${on ? 'ON' : 'OFF'}`;
    hardBtn.style.background = on ? 'rgba(239,68,68,0.22)' : '';
  }
  const btn = document.getElementById('btn-kanji-drill-action');
  if (!btn) return;

  const selLessons = state.kanjiSelectedLessons || new Set();
  const pool = [];
  for (const char in (state.kanjiDB || {})) {
    const k = state.kanjiDB[char];
    if (selLessons.size === 0 || selLessons.has(k.lesson_number)) {
      pool.push(k);
    }
  }

  const items = state.kanjiHardOnly ? buildHardKanjiItems(pool) : buildKanjiStudyItems(pool);
  const wordsCount = items.length;

  let scope = 'All Lessons';
  if (selLessons.size === 1) {
    scope = `Lesson ${Array.from(selLessons)[0]}`;
  } else if (selLessons.size > 1 && selLessons.size <= 3) {
    scope = `L${Array.from(selLessons).sort((a,b)=>a-b).join('+')}`;
  } else if (selLessons.size > 3) {
    scope = `${selLessons.size} Lessons`;
  }

  btn.innerHTML = `<i class="fa-solid fa-play"></i> Drill ${state.kanjiHardOnly ? 'Hard · ' : ''}${scope} <span class="badge" style="margin-left: 0.35rem; font-size: 0.72rem; padding: 0.15rem 0.45rem; background: rgba(255, 255, 255, 0.2); color: #fff; border-radius: 999px;">${wordsCount}w</span>`;
}

export function drillKanjiSelected() {
  const selLessons = state.kanjiSelectedLessons || new Set();
  const pool = [];

  for (const char in (state.kanjiDB || {})) {
    const k = state.kanjiDB[char];
    if (selLessons.size === 0 || selLessons.has(k.lesson_number)) {
      pool.push(k);
    }
  }

  if (pool.length === 0) {
    alert('No kanji found for the selected lessons!');
    return;
  }

  const studyItems = state.kanjiHardOnly ? buildHardKanjiItems(pool) : buildKanjiStudyItems(pool);
  if (studyItems.length === 0) {
    alert(state.kanjiHardOnly ? 'No hard kanji in the selected lessons!' : 'No kanji found for the selected lessons!');
    return;
  }
  studyItems.sort(() => Math.random() - 0.5);

  state.sessionItems = studyItems;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = studyItems.length;
  state.sessionTotal = studyItems.length;
  state.cardFlipped = false;
  state.studyMode = 'flashcard';
  state.isDueReviewMode = false;
  state.drillOrigin = 'kanji';

  showView('study');
  renderCard();
}

export function drillKanjiLesson(lessonNum) {
  if (lessonNum !== undefined && lessonNum !== 'all') {
    selectKanjiLesson(lessonNum, 'replace');
  }
  drillKanjiSelected();
}

/**
 * Universal Cross-Book Kanji Breakdown Lookup:
 * Extracts all kanji characters in a word/sentence and returns their info
 */
export function getKanjiBreakdown(text) {
  if (!text) return [];
  const chars = text.match(/[\u4e00-\u9faf]/g) || [];
  const unique = Array.from(new Set(chars));
  const results = [];

  for (const c of unique) {
    if (state.kanjiDB[c]) {
      results.push({
        char: c,
        isTargetN3: true,
        onyomi: state.kanjiDB[c].onyomi || [],
        kunyomi: state.kanjiDB[c].kunyomi || [],
        lesson: state.kanjiDB[c].lesson_number,
        words: state.kanjiDB[c].words || []
      });
    } else {
      const r = (state.kanjiReview300 || []).find(x => x.kanji === c);
      if (r) {
        results.push({
          char: c,
          isTargetN3: false,
          isReviewN4N5: true,
          examples: r.examples || []
        });
      }
    }
  }
  return results;
}

// =======================================================
// 4. PRACTICE EXERCISES DRILL RUNNER
// =======================================================

export function setExerciseLesson(les) {
  const num = Number(les);
  state.kanjiExerciseLesson = (!isNaN(num) && String(num) === String(les)) ? num : les;
  renderKanjiExercises();
}

export function renderKanjiExercises() {
  const container = document.getElementById('kanji-exercises-container');
  if (!container) return;

  const lNum = state.kanjiExerciseLesson || 1;
  const exercises = state.kanjiExercisesDB[lNum] || [];
  const lessonKeys = Object.keys(state.kanjiExercisesDB || {});
  const activeTitle = (exercises[0] && exercises[0].lesson_title_ja) ? exercises[0].lesson_title_ja : `Lesson ${lNum}`;

  const optionsHtml = lessonKeys.map(k => {
    const exList = state.kanjiExercisesDB[k] || [];
    const label = (exList[0] && exList[0].lesson_title_ja) ? exList[0].lesson_title_ja : `Lesson ${k}`;
    const isSel = String(k) === String(lNum);
    return `<option value="${k}" ${isSel ? 'selected' : ''}>${label}</option>`;
  }).join('');

  let html = `
    <div class="exercise-header-box">
      <div>
        <h3 style="font-size: 1.25rem; color: #fff;">${activeTitle} — Practice Drills</h3>
        <p style="color: var(--text-muted); font-size: 0.85rem;">Shin Kanzen Master Kanji N3 textbook questions transcribed directly.</p>
      </div>
      <div style="display: flex; gap: 0.5rem; align-items: center;">
        <label style="font-size: 0.85rem; color: var(--text-dim);">Section:</label>
        <select class="kanji-select" onchange="setExerciseLesson(this.value)">
          ${optionsHtml}
        </select>
      </div>
    </div>
  `;

  if (exercises.length === 0) {
    html += `<div style="text-align: center; color: var(--text-dim); padding: 3rem;">No exercises loaded yet for Lesson ${lNum}.</div>`;
    container.innerHTML = html;
    return;
  }

  exercises.forEach(ex => {
    html += `
      <div style="margin-top: 1.25rem;">
        <h4 style="color: #f472b6; font-size: 1rem; margin-bottom: 0.75rem;">${ex.title_ja}</h4>
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
    `;

    (ex.items || []).forEach(it => {
      const qText = it.question_ja || it.sentence || it.target_word || '';
      const hasOpts = Array.isArray(it.options) && it.options.length > 0;
      const key = `K_EX:${it.id}`;
      const savedAns = state.kanjiExerciseAnswers[it.id];

      html += `
        <div class="exercise-item-card" id="card-${it.id}">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <span class="exercise-q-num">Q${it.item_id || it.id}</span>
            <button class="btn-ghost btn-sm" onclick="drillExerciseItem('${it.id}')" title="Drill in Flashcards" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;">
              <i class="fa-solid fa-play"></i> SRS
            </button>
          </div>
          <div class="exercise-q-text">${qText}</div>
      `;

      if (hasOpts) {
        html += `<div class="exercise-options-grid">`;
        it.options.forEach((opt, idx) => {
          const isSelected = savedAns === opt;
          html += `
            <button class="exercise-opt-btn ${isSelected ? 'selected' : ''}" 
                    id="btn-${it.id}-${idx}"
                    onclick="selectExerciseOption('${it.id}', '${escapeAttr(opt)}')">
              ${opt}
            </button>
          `;
        });
        html += `</div>`;
      } else {
        html += `
          <div class="exercise-input-row">
            <input type="text" class="exercise-input" id="input-${it.id}" 
                   placeholder="Enter reading or answer..." 
                   value="${savedAns || ''}"
                   onkeydown="if(event.key==='Enter')checkExerciseInput('${it.id}')" />
            <button class="btn btn-primary btn-sm" onclick="checkExerciseInput('${it.id}')">Check</button>
          </div>
        `;
      }

      html += `
          <div id="fb-${it.id}" style="display: none;" class="exercise-feedback-box"></div>
        </div>
      `;
    });

    html += `</div></div>`;
  });

  container.innerHTML = html;
}

export function selectExerciseOption(itemId, optText) {
  state.kanjiExerciseAnswers[itemId] = optText;
  const lNum = state.kanjiExerciseLesson || 1;
  const exercises = state.kanjiExercisesDB[lNum] || [];
  let targetItem = null;

  for (const ex of exercises) {
    for (const it of ex.items) {
      if (it.id === itemId) { targetItem = it; break; }
    }
    if (targetItem) break;
  }
  if (!targetItem) return;

  const correctAns = targetItem.answer || targetItem.reading;
  const isRight = (optText === correctAns) || 
                  (targetItem.answers && targetItem.answers.includes(optText));

  const card = document.getElementById(`card-${itemId}`);
  const fb = document.getElementById(`fb-${itemId}`);

  if (card) {
    card.classList.toggle('is-correct', isRight);
    card.classList.toggle('is-incorrect', !isRight);
  }

  if (fb) {
    fb.style.display = 'block';
    fb.className = `exercise-feedback-box ${isRight ? 'correct' : 'incorrect'}`;
    fb.innerHTML = isRight 
      ? `<strong><i class="fa-solid fa-circle-check"></i> 正解！</strong> ${targetItem.explanation || ''}`
      : `<strong><i class="fa-solid fa-circle-xmark"></i> 不正解</strong> <div style="margin-top:.35rem;"><b>Correct answer:</b> ${correctAns}</div>${targetItem.explanation ? `<div style="margin-top:.35rem;">${targetItem.explanation}</div>` : ''}`;
  }

  // Update SRS
  updateItemStats(`K_EX:${itemId}`, isRight ? 3 : 1);
}

export function checkExerciseInput(itemId) {
  const inp = document.getElementById(`input-${itemId}`);
  if (!inp) return;
  const userVal = inp.value.trim();
  if (!userVal) return;

  state.kanjiExerciseAnswers[itemId] = userVal;
  const lNum = state.kanjiExerciseLesson || 1;
  const exercises = state.kanjiExercisesDB[lNum] || [];
  let targetItem = null;

  for (const ex of exercises) {
    for (const it of ex.items) {
      if (it.id === itemId) { targetItem = it; break; }
    }
    if (targetItem) break;
  }
  if (!targetItem) return;

  const correctAns = targetItem.answer || targetItem.reading;
  const isRight = (userVal === correctAns) || 
                  (targetItem.answers && targetItem.answers.includes(userVal));

  const card = document.getElementById(`card-${itemId}`);
  const fb = document.getElementById(`fb-${itemId}`);

  if (card) {
    card.classList.toggle('is-correct', isRight);
    card.classList.toggle('is-incorrect', !isRight);
  }

  if (fb) {
    fb.style.display = 'block';
    fb.className = `exercise-feedback-box ${isRight ? 'correct' : 'incorrect'}`;
    fb.innerHTML = isRight 
      ? `<strong><i class="fa-solid fa-circle-check"></i> 正解！</strong> ${targetItem.explanation || ''}`
      : `<strong><i class="fa-solid fa-circle-xmark"></i> 不正解</strong> <div style="margin-top:.35rem;"><b>Correct answer:</b> ${correctAns}</div>${targetItem.explanation ? `<div style="margin-top:.35rem;">${targetItem.explanation}</div>` : ''}`;
  }

  updateItemStats(`K_EX:${itemId}`, isRight ? 3 : 1);
}

export function drillExerciseItem(itemId) {
  const lNum = state.kanjiExerciseLesson || 1;
  const exercises = state.kanjiExercisesDB[lNum] || [];
  let targetItem = null;
  let targetEx = null;

  for (const ex of exercises) {
    for (const it of ex.items) {
      if (it.id === itemId) {
        targetItem = it;
        targetEx = ex;
        break;
      }
    }
    if (targetItem) break;
  }
  if (!targetItem) return;

  beginGistReviewSession();
  state.sessionItems = [{
    ...targetItem,
    exercise_title: targetEx ? targetEx.title_ja : '',
    type: 'kanji_exercise',
    book: 'kanji_exercise'
  }];
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotal = 1;
  state.cardFlipped = false;
  state.studyMode = 'flashcard';
  state.isDueReviewMode = false;
  state.drillOrigin = 'kanji';
  showView('study');
  renderCard();
}

// =======================================================
// 5. REVIEW 300 (N4/N5) EXPLORER
// =======================================================

export function renderKanjiReview300() {
  const container = document.getElementById('kanji-review300-grid');
  if (!container) return;

  container.innerHTML = '';
  const items = state.kanjiReview300 || [];
  const query = state.kanjiSearchQuery || '';

  const filtered = items.filter(it => {
    if (!query) return true;
    const matchChar = it.kanji.includes(query);
    const matchEx = (it.examples || []).some(ex => {
      return (ex.example && ex.example.includes(query)) ||
             (ex.reading && ex.reading.includes(query)) ||
             (ex.example_reading && ex.example_reading.includes(query));
    });
    return matchChar || matchEx;
  });

  if (filtered.length === 0) {
    container.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; color: var(--text-dim); padding: 3rem;">No review kanji matching filter.</div>';
    return;
  }

  filtered.forEach(it => {
    const card = document.createElement('div');
    card.className = 'kanji-card';
    card.onclick = () => openKanjiModal(it.kanji);

    const firstEx = (it.examples || [])[0] || {};
    card.innerHTML = `
      <span class="kanji-card-lesson-tag">#${it.number}</span>
      <div class="kanji-card-char">${it.kanji}</div>
      <div class="kanji-card-onyomi">${firstEx.reading || '—'}</div>
      <div class="kanji-card-meaning">${firstEx.example || ''}</div>
    `;
    container.appendChild(card);
  });
}

// =======================================================
// 6. SPECIAL READINGS (熟字訓) EXPLORER
// =======================================================

export function renderKanjiSpecialReadings() {
  const container = document.getElementById('kanji-special-list');
  if (!container) return;

  container.innerHTML = '';
  const items = state.kanjiSpecialReadings || [];

  if (items.length === 0) {
    container.innerHTML = '<div style="text-align: center; color: var(--text-dim); padding: 3rem;">No special readings loaded.</div>';
    return;
  }

  items.forEach(it => {
    const card = document.createElement('div');
    card.className = 'exercise-item-card';
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="exercise-q-num">SR #${it.number}</span>
        <span style="color: var(--text-muted); font-size: 0.85rem;">${it.meaning_en || ''}</span>
      </div>
      <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 0.25rem;">
        <div style="font-family: var(--font-jp); font-size: 1.5rem; font-weight: 700; color: #fff;">
          ${it.ruby || it.word}
        </div>
        <div style="color: #f472b6; font-size: 1.1rem; font-weight: 600;">
          ${it.reading}
        </div>
      </div>
    `;
    container.appendChild(card);
  });
}

// =======================================================
// 7. MOCK TESTS RUNNER (実力テスト 1 & 2)
// =======================================================

export function renderKanjiMockTests() {
  const container = document.getElementById('kanji-mock-container');
  if (!container) return;

  const chapters = state.kanjiMockTests || [];
  if (chapters.length === 0) {
    container.innerHTML = '<div style="text-align: center; color: var(--text-dim); padding: 3rem;">No mock tests loaded.</div>';
    return;
  }

  let html = '';
  chapters.forEach(chap => {
    const meta = chap.metadata || {};
    html += `
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.25rem; margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; margin-bottom: 1rem;">
          <div>
            <h3 style="color: #fff; font-size: 1.2rem;">${meta.topic_ja || '実力テスト'}</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem;">${meta.topic_en || ''} (Pages ${meta.pages ? meta.pages.join('–') : ''})</p>
          </div>
        </div>
    `;

    (chap.exercises || []).forEach(ex => {
      html += `
        <div style="margin-bottom: 1.25rem;">
          <h4 style="color: #f472b6; font-size: 0.95rem; margin-bottom: 0.75rem;">${ex.title_ja}</h4>
          <div style="display: flex; flex-direction: column; gap: 0.85rem;">
      `;

      (ex.items || []).forEach(it => {
        const itemId = `${ex.exercise_id}_${it.item_id}`;
        html += `
          <div class="exercise-item-card" id="mock-${itemId}">
            <div class="exercise-q-text">${it.item_id}. ${it.question_ja}</div>
            <div class="exercise-options-grid">
              ${(it.options || []).map((opt, i) => `
                <button class="exercise-opt-btn" onclick="checkMockOption('${itemId}', '${i + 1}', '${it.answer}', '${escapeAttr(it.explanation)}')">
                  ${opt}
                </button>
              `).join('')}
            </div>
            <div id="mock-fb-${itemId}" style="display: none;" class="exercise-feedback-box"></div>
          </div>
        `;
      });

      html += `</div></div>`;
    });

    html += `</div>`;
  });

  container.innerHTML = html;
}

export function checkMockOption(itemId, selectedIdx, correctAns, explanation) {
  const isRight = selectedIdx === correctAns;
  const card = document.getElementById(`mock-${itemId}`);
  const fb = document.getElementById(`mock-fb-${itemId}`);

  if (card) {
    card.classList.toggle('is-correct', isRight);
    card.classList.toggle('is-incorrect', !isRight);
  }

  if (fb) {
    fb.style.display = 'block';
    fb.className = `exercise-feedback-box ${isRight ? 'correct' : 'incorrect'}`;
    fb.innerHTML = isRight 
      ? `<strong><i class="fa-solid fa-circle-check"></i> 正解！</strong> ${explanation}`
      : `<strong><i class="fa-solid fa-circle-xmark"></i> 不正解</strong> (正解: ${correctAns}) ${explanation}`;
  }

  updateItemStats(`K_MOCK:${itemId}`, isRight ? 3 : 1);
}

// =======================================================
// 8. QUICK QUIZ (MCQ FAST-REVISION DRILL)
// Elementary-app speed pattern: tap-to-answer options,
// auto-next on correct, mixed direction, same-lesson distractors.
// SRS writes go to the same facet keys (KWR/KWW/KWM) as flashcards.
// =======================================================


export function toggleKanjiAutoNext(checked) {
  state.kanjiAutoNext = Boolean(checked);
  try { localStorage.setItem('n3_kanji_auto_next', checked ? 'true' : 'false'); } catch (e) {}
}

function isKanjiAutoNextOn() {
  if (typeof state.kanjiAutoNext === 'boolean') return state.kanjiAutoNext;
  try { state.kanjiAutoNext = localStorage.getItem('n3_kanji_auto_next') === 'true'; } catch (e) { state.kanjiAutoNext = false; }
  return state.kanjiAutoNext;
}

function quizValueOf(it, dir) {
  if (dir === 'kana-ja') return it.word;
  if (dir === 'ja-meaning') return it.meaning_en;
  return it.reading;
}

function buildKanjiQuizOptions(item, allItems) {
  const dir = item.direction;
  const correct = quizValueOf(item, dir);
  const seen = new Set([correct]);
  const distractors = [];
  const pickFrom = (list) => {
    const cands = list.slice().sort(() => Math.random() - 0.5);
    for (const c of cands) {
      if (distractors.length >= 3) break;
      const v = quizValueOf(c, dir);
      if (v && !seen.has(v)) {
        seen.add(v);
        distractors.push(v);
      }
    }
  };
  // Same-lesson distractors first (harder, more plausible), then the wider pool
  pickFrom(allItems.filter(x => x !== item && x.lesson_number === item.lesson_number));
  pickFrom(allItems.filter(x => x !== item && x.lesson_number !== item.lesson_number));
  const values = [correct, ...distractors].sort(() => Math.random() - 0.5);
  return { values, correctValue: correct };
}

export function startKanjiQuickQuiz() {
  const selLessons = state.kanjiSelectedLessons || new Set();
  const pool = [];
  for (const char in (state.kanjiDB || {})) {
    const k = state.kanjiDB[char];
    if (selLessons.size === 0 || selLessons.has(k.lesson_number)) {
      pool.push(k);
    }
  }

  if (pool.length === 0) {
    alert('No kanji found for the selected lessons!');
    return;
  }

  // Distractors come from the full selected pool; the round covers EVERY word (or every hard word)
  const allItems = buildKanjiStudyItems(pool).filter(it => it.type === 'kanji_word' && it.word && it.reading && it.meaning_en);
  const roundSource = state.kanjiHardOnly
    ? buildHardKanjiItems(pool).filter(it => it.type === 'kanji_word' && it.word && it.reading && it.meaning_en)
    : allItems;
  if (state.kanjiHardOnly && roundSource.length === 0) {
    alert('No hard kanji words in the selected lessons!');
    return;
  }
  const items = roundSource.slice().sort(() => Math.random() - 0.5);

  if (items.length < (state.kanjiHardOnly ? 1 : 2)) {
    alert('Not enough compound words in this selection to quiz!');
    return;
  }

  beginGistReviewSession();
  items.forEach(it => {
    it.options = buildKanjiQuizOptions(it, allItems);
    it.answered = false;
  });

  state.sessionItems = items;
  state.sessionIdx = 0;
  state.sessionRight = 0;
  state.sessionTotalAnswered = 0;
  state.sessionTotalInitial = items.length;
  state.sessionTotal = items.length;
  state.sessionSkipped = 0;
  state.cardFlipped = false;
  state.studyMode = 'kanji_quiz';
  state.studyIsDrillHard = false;
  state.isDueReviewMode = false;
  state.drillOrigin = 'kanji';
  state.learnUnit = null;

  showView('study');
  renderCard();
}

export function renderKanjiQuizCard(item) {
  if (state._kanjiQuizTimer) {
    clearTimeout(state._kanjiQuizTimer);
    state._kanjiQuizTimer = null;
  }

  const lessonTag = document.getElementById('card-lesson-tag');
  const termEl = document.getElementById('card-term');
  const meaningEl = document.getElementById('card-meaning');
  const exBox = document.getElementById('card-example-box');
  const hint = document.getElementById('card-controls-hint');
  const gradeControls = document.getElementById('grade-controls');

  if (termEl) termEl.classList.toggle('kanji-quiz-term', true);
  if (meaningEl) meaningEl.classList.toggle('kanji-quiz-options', true);
  if (exBox) exBox.style.display = 'none';
  if (gradeControls) gradeControls.style.display = 'none';

  const dir = item.direction || 'ja-kana';
  const dirBadge = dir === 'kana-ja'
    ? '<span class="badge badge-cyan" style="font-size: 0.78rem;">表記 (Kana → Kanji)</span>'
    : (dir === 'ja-meaning'
      ? '<span class="badge" style="background: rgba(236,72,153,0.18); border: 1px solid #ec4899; color: #f472b6; font-size: 0.78rem; font-weight: 700;">意味 (Kanji → English)</span>'
      : '<span class="badge badge-purple" style="font-size: 0.78rem;">漢字読み (Kanji → Kana)</span>');

  if (lessonTag) lessonTag.textContent = `Quick Quiz · 漢字第${item.lesson_number}課 · 親漢字「${item.baseKanji || '漢字'}」`;

  if (dir === 'ja-kana') {
    termEl.innerHTML = `
      <div>
        <div class="kanji-quiz-prompt" style="font-size:clamp(3.8rem,14vw,5.4rem);font-family:var(--font-jp);font-weight:800;color:#fff;letter-spacing:.04em;line-height:1.18;">${item.word}</div>
        <div style="margin-top: 0.75rem;">${dirBadge}</div>
      </div>`;
  } else if (dir === 'kana-ja') {
    termEl.innerHTML = `
      <div>
        <div style="font-size: 3rem; font-family: var(--font-jp); font-weight: 800; color: #38bdf8; letter-spacing: 0.05em;">${item.reading}</div>
        <div style="color: var(--text-muted); font-size: 1.05rem; margin-top: 0.5rem;">${item.meaning_en || ''}</div>
        <div style="margin-top: 0.75rem;">${dirBadge}</div>
      </div>`;
  } else {
    termEl.innerHTML = `
      <div>
        <div style="font-size: 3.2rem; font-family: var(--font-jp); font-weight: 800; color: #fff;">${item.word}</div>
        <div style="color: #f472b6; font-size: 1.15rem; font-family: var(--font-jp); margin-top: 0.4rem;">（${item.reading}）</div>
        <div style="margin-top: 0.75rem;">${dirBadge}</div>
      </div>`;
  }

  const optsHtml = item.options.values.map((v, i) => `
    <button class="kanji-quiz-opt" data-idx="${i}" onclick="event.stopPropagation(); answerKanjiQuizOption(${i})"
      style="padding: 0.7rem 1rem; border-radius: 10px; border: 1px solid var(--border); background: rgba(255,255,255,0.05); color: #fff; font-size: 1.05rem; cursor: pointer; text-align: left; width: 100%; ${dir === 'ja-meaning' ? '' : 'font-family: var(--font-jp);'}">
      <strong style="color: var(--text-dim); margin-right: 0.5rem;">${i + 1}.</strong>${v}
    </button>
  `).join('');

  meaningEl.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem; width: 100%; max-width: 420px; margin-left: auto; margin-right: auto;">
      ${optsHtml}
    </div>`;
  meaningEl.style.color = 'var(--text)';

  if (hint) {
    hint.style.display = 'block';
    hint.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; width: 100%; padding: 0 0.25rem;" onclick="event.stopPropagation()">
        <label style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.78rem; color: var(--text-dim); cursor: pointer; user-select: none;">
          <input type="checkbox" id="kq-toggle-auto-next" ${isKanjiAutoNextOn() ? 'checked' : ''} onchange="toggleKanjiAutoNext(this.checked)" style="cursor: pointer;">
          <span><i class="fa-solid fa-bolt"></i> Auto-next on correct</span>
        </label>
        <button class="btn btn-primary btn-sm" id="kq-btn-next" onclick="event.stopPropagation(); nextKanjiQuizCard()" style="visibility: hidden;">
          Next <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>`;
  }
}

export function answerKanjiQuizOption(idx) {
  if (state.studyMode !== 'kanji_quiz') return;
  const item = state.sessionItems[state.sessionIdx];
  if (!item || item.answered || !item.options) return;
  item.answered = true;

  const chosen = item.options.values[idx];
  const isCorrect = chosen === item.options.correctValue;

  // Facet-split SRS: write to the same key the flashcard drill uses
  updateItemStats(item.key, isCorrect ? 3 : 1);

  state.sessionTotalAnswered = (state.sessionTotalAnswered || 0) + 1;
  if (isCorrect) {
    state.sessionRight = (state.sessionRight || 0) + 1;
  }

  document.querySelectorAll('.kanji-quiz-opt').forEach(btn => {
    const btnIdx = Number(btn.getAttribute('data-idx'));
    const v = item.options.values[btnIdx];
    if (v === item.options.correctValue) {
      btn.style.borderColor = 'var(--green)';
      btn.style.background = 'rgba(34, 197, 94, 0.18)';
    } else if (btnIdx === idx) {
      btn.style.borderColor = 'var(--red)';
      btn.style.background = 'rgba(239, 68, 68, 0.18)';
    }
    btn.disabled = true;
    btn.style.cursor = 'default';
  });

  if (!isCorrect) {
    const review = document.createElement('div');
    review.className = 'kanji-quiz-wrong-review';
    review.style.cssText = 'margin-top:0.85rem;padding:0.85rem 1rem;border:1px solid rgba(239,68,68,.35);border-radius:12px;background:rgba(239,68,68,.08);text-align:left;';
    review.innerHTML = '<strong style="color:#fca5a5;display:block;margin-bottom:.35rem;">Review this answer</strong>' +
      '<div class="font-ja" style="font-size:1.35rem;font-weight:800;color:#fff;">' + item.word + '</div>' +
      '<div style="color:#f472b6;font-weight:700;">' + (item.reading || '') + '</div>' +
      '<div style="color:var(--text-muted);">' + (item.meaning_en || '') + (item.meaning_zh ? ' · ' + item.meaning_zh : '') + '</div>' +
      '<div style="font-size:.78rem;color:var(--text-dim);margin-top:.25rem;">Correct choice: ' + item.options.correctValue + '</div>';
    const breakdown = getKanjiBreakdownPills(item.word, state.kanjiDB);
    if (breakdown.length) {
      const pills = document.createElement('div');
      pills.style.cssText = 'display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.5rem;';
      pills.innerHTML = breakdown.map(x => '<span style="padding:.2rem .45rem;border-radius:8px;background:rgba(255,255,255,.06);font-size:.78rem;"><b class="font-ja">' + x.kanji + '</b> ' + (x.meaning || '') + '</span>').join('');
      review.appendChild(pills);
    }
    const meaningEl = document.getElementById('card-meaning');
    if (meaningEl) meaningEl.appendChild(review);
  }

  const correctEl = document.getElementById('session-correct');
  const totalEl = document.getElementById('session-total');
  if (correctEl) correctEl.textContent = state.sessionRight;
  if (totalEl) totalEl.textContent = state.sessionTotalAnswered;

  if (!isCorrect) {
    // Missed cards re-queue +3 down the deck, mirroring gradeCard's Again handling
    const insertAt = Math.min(state.sessionIdx + 3, state.sessionItems.length);
    state.sessionItems.splice(insertAt, 0, { ...item, answered: false });
  }

  if (isCorrect && isKanjiAutoNextOn()) {
    if (state._kanjiQuizTimer) clearTimeout(state._kanjiQuizTimer);
    state._kanjiQuizTimer = setTimeout(() => nextKanjiQuizCard(), 750);
  } else {
    const nextBtn = document.getElementById('kq-btn-next');
    if (nextBtn) nextBtn.style.visibility = 'visible';
  }
}

export function nextKanjiQuizCard() {
  if (state.studyMode !== 'kanji_quiz') return;
  if (state._kanjiQuizTimer) {
    clearTimeout(state._kanjiQuizTimer);
    state._kanjiQuizTimer = null;
  }
  state.sessionIdx++;
  state.cardFlipped = false;
  renderCard();
}

function escapeAttr(str) {
  if (!str) return '';
  return str.replace(/'/g, "\\'").replace(/"/g, '&quot;');
}

if (typeof window !== 'undefined') {
  window.toggleKanjiHardOnly = toggleKanjiHardOnly;
  window.drillKanjiHard = drillKanjiHard;
}
