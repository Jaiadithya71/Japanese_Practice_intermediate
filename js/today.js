/* =======================================================
   NIHONGO INTERMEDIATE — today.js
   Habit Engine, Today Dashboard & Progress Heatmap (WP-6)
   Reference: n3_dev_handoff/01_UX_AND_SCREEN_SPEC.md §2, §3
              n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §6
   ======================================================= */

import { state as defaultState } from './state.js';
// Conditionally load browser-only pull-refresh in DOM environment
if (typeof window !== 'undefined') {
  import('./pull-refresh.js').catch(() => {});
}
import { istNow, istDateKey } from './time.js';
import { getHeatmap30, getCurrentStreak } from './daylog.js';
import { calculatePace, forecast } from './planner.js';
import {
  getDueItemsCount,
  getItemStatus,
  isCatchUpMode
} from './srs.js';
import {
  nextBestAction,
  getDailyPlanStatus,
  hasResumableDailySession,
  loadDailySessionProgress
} from './daily.js';
import {
  BACKLOG_THRESHOLD,
  EXAM_DATE_ISO
} from './config.js';

// Auto-inject css/today.css if not already linked
if (typeof document !== 'undefined' && !document.getElementById('today-stylesheet')) {
  const link = document.createElement('link');
  link.id = 'today-stylesheet';
  link.rel = 'stylesheet';
  link.href = 'css/today.css';
  document.head.appendChild(link);
}

/**
 * Calculates current mastery percentages across the 4 active pillars.
 */
export function getReadinessStats(st = defaultState) {
  const stats = st.stats || {};

  // 1. Vocabulary
  let vocabTotal = 0;
  let vocabMastered = 0;
  for (const chId in (st.vocabDB || {})) {
    for (const w of (st.vocabDB[chId] || [])) {
      vocabTotal++;
      const s = stats[`V:${w.id}`];
      if (s && ((s.reps >= 4 && (s.interval || 0) >= 21) || (s.correct || 0) >= 3) && (s.weight || 1.0) <= 0.8 && !s.isHard) {
        vocabMastered++;
      }
    }
  }

  // 2. Kanji
  const kanjiChars = Object.keys(st.kanjiDB || {});
  const kanjiTotal = kanjiChars.length > 0 ? kanjiChars.length : 443;
  let kanjiMastered = 0;
  for (const c of kanjiChars) {
    const s = stats[`K:${c}`];
    if (s && ((s.reps >= 4 && (s.interval || 0) >= 21) || (s.correct || 0) >= 3) && (s.weight || 1.0) <= 0.8 && !s.isHard) {
      kanjiMastered++;
    }
  }

  // 3. Grammar
  const grammarPatterns = st.grammarDB?.index || [];
  const grammarTotal = grammarPatterns.length > 0 ? grammarPatterns.length : 83;
  let grammarMastered = 0;
  for (const p of grammarPatterns) {
    const s = stats[`G:${p.id}`];
    if (s && ((s.reps >= 4 && (s.interval || 0) >= 21) || (s.correct || 0) >= 3) && (s.weight || 1.0) <= 0.8 && !s.isHard) {
      grammarMastered++;
    }
  }

  // 4. Reading
  const readingKeys = Object.keys(st.readingDB || {});
  const readingTotal = readingKeys.length > 0 ? readingKeys.length : 49;
  let readingMastered = 0;
  for (const lid of readingKeys) {
    const lesson = st.readingDB[lid] || {};
    const qs = lesson.comprehensionQuestions || lesson.questions || [];
    if (qs.length > 0) {
      const allPassed = qs.every(q => {
        const qid = q.id || `${lid}_q${q.questionNumber || 1}`;
        const s = stats[`R_Q:${qid}`];
        return Boolean(s && s.correct > 0 && (s.weight || 1.0) <= 1.0);
      });
      if (allPassed) readingMastered++;
    }
  }

  return {
    vocab: {
      mastered: vocabMastered,
      total: vocabTotal || 1251,
      pct: vocabTotal > 0 ? Math.round((vocabMastered / vocabTotal) * 100) : 0
    },
    kanji: {
      mastered: kanjiMastered,
      total: kanjiTotal,
      pct: kanjiTotal > 0 ? Math.round((kanjiMastered / kanjiTotal) * 100) : 0
    },
    grammar: {
      mastered: grammarMastered,
      total: grammarTotal,
      pct: grammarTotal > 0 ? Math.round((grammarMastered / grammarTotal) * 100) : 0
    },
    reading: {
      mastered: readingMastered,
      total: readingTotal,
      pct: readingTotal > 0 ? Math.round((readingMastered / readingTotal) * 100) : 0
    }
  };
}

/**
 * Renders the 30-day activity heatmap grid formatted into 7 columns (Mon-Sun).
 */
export function renderHeatmapGridHtml(heatmapData = []) {
  if (!heatmapData || heatmapData.length === 0) return '';
  const weekdays = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
  const headerCells = weekdays.map(w => `<span class="heatmap-col-head">${w}</span>`).join('');

  // Find day-of-week offset for first day (oldest)
  const d0 = heatmapData[0];
  const [y, m, d] = (d0.date || '').split('-').map(Number);
  const dateObj = new Date(Date.UTC(y, m - 1, d));
  const dow = (dateObj.getUTCDay() + 6) % 7; // Mon = 0, Sun = 6

  let padCells = '';
  for (let i = 0; i < dow; i++) {
    padCells += '<span class="heatmap-cell empty"></span>';
  }

  const todayKey = istDateKey();
  const dayCells = heatmapData.map(item => {
    const isToday = item.date === todayKey;
    const title = `${item.date}: ${item.count} items`;
    return `<span class="heatmap-cell level-${item.level}${isToday ? ' is-today' : ''}" data-date="${item.date}" data-count="${item.count}" title="${title}"></span>`;
  }).join('');

  return `
    <div class="heatmap-grid-inner">
      <div class="heatmap-weekdays">${headerCells}</div>
      <div class="heatmap-cells-grid">${padCells}${dayCells}</div>
    </div>
  `;
}

/**
 * Renders the 14-day projection bars sparkline from planner.forecast().
 */
export function renderForecastBarsHtml(forecastData = []) {
  if (!forecastData || forecastData.length === 0) return '';
  const maxMinutes = Math.max(45, ...forecastData.map(d => d.minutes || 0));

  const bars = forecastData.map(d => {
    const heightPct = Math.max(12, Math.round(((d.minutes || 0) / maxMinutes) * 100));
    const isOver = (d.minutes || 0) > 45;
    const title = `Day +${d.day}: ${d.reviews} reviews, ${d.newItems} new (~${d.minutes} min)`;
    return `
      <div class="forecast-bar-col" title="${title}">
        <div class="forecast-bar-track">
          <div class="forecast-bar-fill${isOver ? ' over-budget' : ''}" style="height: ${heightPct}%;"></div>
        </div>
        <span class="forecast-bar-label">d${d.day}</span>
      </div>
    `;
  }).join('');

  return `
    <div class="forecast-bars-container">
      ${bars}
    </div>
  `;
}

/**
 * Main dashboard render entry point.
 * Targets document.getElementById('view-today') or 'today-card' or 'view-home'.
 */
export function renderToday() {
  if (typeof document === 'undefined') return;

  const container = document.getElementById('view-today')
    || document.getElementById('today-card')
    || document.getElementById('view-home');
  if (!container) return;

  const st = defaultState;
  const now = Date.now();
  const examDate = st.settings?.examDate || EXAM_DATE_ISO;

  // 1. Exam Countdown & Phase Header (time.js & planner.js)
  const pace = calculatePace(
    {
      vocabTier1: Object.keys(st.vocabDB || {}).length * 10,
      kanjiWords: Object.keys(st.kanjiDB || {}).length,
      grammar: (st.grammarDB?.index || []).length
    },
    st.settings?.profile || 'standard',
    examDate,
    { now }
  );

  const daysToExam = pace.daysToExam > 0 ? pace.daysToExam : 0;
  let phase = 'Phase 1 Foundation';
  if (daysToExam <= 14) {
    phase = 'Phase 3 Final Sprint';
  } else if (daysToExam <= 35) {
    phase = 'Phase 2 Consolidation';
  }
  const headerTitle = `N3 · ${daysToExam} days to exam · ${phase}`;

  // 2. Due Reviews & Pillars Breakdown
  const dueV = getDueItemsCount('vocab');
  const dueK = getDueItemsCount('kanji');
  const dueG = getDueItemsCount('grammar');
  const dueR = getDueItemsCount('reading');
  const totalDue = dueV + dueK + dueG + dueR;
  const catchUp = totalDue > BACKLOG_THRESHOLD;

  // Batch selector state
  const currentBatch = String(st.dueBatchSize || '20').toLowerCase();

  // 3. Primary Hero CTA Recommendation from nextBestAction()
  const planStatus = getDailyPlanStatus({ state: st, dueCount: totalDue });
  const action = nextBestAction({ state: st, dueCount: totalDue, planStatus });

  // 4. Backlog Catch-up Banner (shown if totalDue > BACKLOG_THRESHOLD)
  let catchUpBannerHtml = '';
  if (catchUp) {
    catchUpBannerHtml = `
      <div class="today-banner catch-up-banner">
        <div class="banner-icon"><i class="fa-solid fa-clock-rotate-left"></i></div>
        <div class="banner-body">
          <div class="banner-title">Catching up: ${totalDue} due. New items resume under ${BACKLOG_THRESHOLD}.</div>
          <div class="banner-sub">Per-session cap is 40 items. Ordered by overdue ratio.</div>
        </div>
        <button class="btn btn-sm btn-catchup" onclick="setDueBatch('40'); startDueReview('all');">Catch Up (40)</button>
      </div>
    `;
  }

  // 5. Pace Shortfall Warning (amber banner if kanji/vocab shortfall)
  let paceWarningHtml = '';
  if (!pace.allFeasible && pace.warnings && pace.warnings.length > 0) {
    paceWarningHtml = `
      <div class="today-banner pace-warning-banner">
        <div class="banner-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
        <div class="banner-body">
          <div class="banner-title">Pace Shortfall</div>
          <div class="banner-sub">${pace.warnings[0]}</div>
        </div>
        <button class="btn btn-sm btn-outline-amber" onclick="showView('hard-words')">Adjust</button>
      </div>
    `;
  }

  // 6. Resume Session Banner (if mid-session left)
  let resumeBannerHtml = '';
  if (hasResumableDailySession()) {
    const prog = loadDailySessionProgress();
    resumeBannerHtml = `
      <div class="today-banner resume-banner">
        <div class="banner-icon"><i class="fa-solid fa-play-pause"></i></div>
        <div class="banner-body">
          <div class="banner-title">Resume Session</div>
          <div class="banner-sub">You were on step ${(prog?.currentStepIndex || 0) + 1}. Continue where you left off.</div>
        </div>
        <button class="btn btn-sm btn-primary" onclick="resumeDailySession()">Continue</button>
      </div>
    `;
  }

  // 7. Sunday Weekly Check Card
  let weeklyCheckHtml = '';
  const istDate = istNow();
  if (istDate.getDay() === 0) { // Sunday
    weeklyCheckHtml = `
      <div class="today-card-weekly">
        <div class="weekly-header">
          <span class="badge badge-amber"><i class="fa-solid fa-calendar-check"></i> Sunday Weekly Check</span>
          <span class="weekly-title">7-Day Cumulative Test</span>
        </div>
        <button class="btn btn-primary btn-sm" onclick="startTestSession('weekly')">Start Weekly Check (20 Qs)</button>
      </div>
    `;
  }

  // 8. Today's Plan Checklist Rows
  const planRowsHtml = planStatus.items.map(it => {
    return `
      <div class="plan-row ${it.completed ? 'completed' : 'pending'}" onclick="${it.handler}">
        <span class="plan-check ${it.completed ? 'checked' : 'pending'}">
          <i class="${it.completed ? 'fa-solid fa-circle-check' : 'fa-regular fa-circle'}"></i>
        </span>
        <div class="plan-info">
          <div class="plan-title">${it.title}</div>
          <div class="plan-detail">${it.label}</div>
        </div>
        <i class="fa-solid fa-chevron-right plan-arrow"></i>
      </div>
    `;
  }).join('');

  // 9. 30-Day Activity Heatmap & Streak
  const heatmapData = getHeatmap30();
  const streak = getCurrentStreak();
  const heatmapGridHtml = renderHeatmapGridHtml(heatmapData);

  // 10. Readiness Mastery Bars
  const readiness = getReadinessStats(st);
  const readinessPillars = [
    { key: 'vocab', name: 'Vocab', data: readiness.vocab, color: 'bar-accent' },
    { key: 'kanji', name: 'Kanji', data: readiness.kanji, color: 'bar-cyan' },
    { key: 'grammar', name: 'Grammar', data: readiness.grammar, color: 'bar-amber' },
    { key: 'reading', name: 'Reading', data: readiness.reading, color: 'bar-green' }
  ];
  const readinessBarsHtml = readinessPillars.map(p => {
    return `
      <div class="readiness-item">
        <div class="readiness-label-row">
          <span class="readiness-name">${p.name}</span>
          <span class="readiness-pct">${p.data.pct}%</span>
        </div>
        <div class="readiness-track">
          <div class="readiness-fill ${p.color}" style="width: ${p.data.pct}%;"></div>
        </div>
        <div class="readiness-counts">${p.data.mastered} / ${p.data.total} mastered</div>
      </div>
    `;
  }).join('');

  // 11. 14-Day Load Forecast Sparkline
  const forecast14 = forecast(st.settings, st.stats, 14);
  const forecastBarsHtml = renderForecastBarsHtml(forecast14);
  const forecastWarningHtml = forecast14.warning
    ? `<div class="forecast-warning-note"><i class="fa-solid fa-triangle-exclamation"></i> ${forecast14.warning}</div>`
    : '';


  // Class Track Widget Data
  let classProgress = { vocab: 1, kanji: 1, grammar: 1, readingStart: 1, readingEnd: 1 };
  if (typeof window !== 'undefined' && window.N3Class && typeof window.N3Class.get === 'function') {
    classProgress = window.N3Class.get();
  } else {
    try {
      const raw = (typeof localStorage !== 'undefined') ? localStorage.getItem('nihongo_intermediate_class_progress_v1') : null;
      if (raw) classProgress = { ...classProgress, ...JSON.parse(raw) };
    } catch (e) {}
  }
  const readingSpanText = classProgress.readingStart === classProgress.readingEnd 
    ? `第 ${classProgress.readingStart} 課` 
    : `第 ${classProgress.readingStart}～${classProgress.readingEnd} 課`;

  const classCardHtml = `
    <div class="today-card today-class-card">
      <div class="tcc-header">
        <span class="tcc-tag"><i class="fa-solid fa-graduation-cap"></i> 授業同期 Class Sync</span>
        <button class="tcc-view-btn" onclick="showView('class')">
          <span>詳細 Hub</span> <i class="fa-solid fa-chevron-right"></i>
        </button>
      </div>
      <div class="tcc-grid">
        <div class="tcc-item">
          <span class="tcc-label">語彙 Vocab</span>
          <div class="tcc-stepper">
            <button onclick="window.N3Class ? window.N3Class.step('vocab', -1) : null" title="Prev Chapter">-</button>
            <span class="tcc-val">第 ${classProgress.vocab} 課</span>
            <button onclick="window.N3Class ? window.N3Class.step('vocab', 1) : null" title="Next Chapter">+</button>
          </div>
        </div>
        <div class="tcc-item">
          <span class="tcc-label">漢字 Kanji</span>
          <div class="tcc-stepper">
            <button onclick="window.N3Class ? window.N3Class.step('kanji', -1) : null" title="Prev Lesson">-</button>
            <span class="tcc-val">第 ${classProgress.kanji} 課</span>
            <button onclick="window.N3Class ? window.N3Class.step('kanji', 1) : null" title="Next Lesson">+</button>
          </div>
        </div>
        <div class="tcc-item">
          <span class="tcc-label">文法 Grammar</span>
          <div class="tcc-stepper">
            <button onclick="window.N3Class ? window.N3Class.step('grammar', -1) : null" title="Prev Section">-</button>
            <span class="tcc-val">第 ${classProgress.grammar} 課</span>
            <button onclick="window.N3Class ? window.N3Class.step('grammar', 1) : null" title="Next Section">+</button>
          </div>
        </div>
        <div class="tcc-item">
          <span class="tcc-label">読解 Reading</span>
          <div class="tcc-stepper">
            <button onclick="window.N3Class ? window.N3Class.step('reading', -1) : null" title="Prev Passage">-</button>
            <span class="tcc-val">${readingSpanText}</span>
            <button onclick="window.N3Class ? window.N3Class.step('reading', 1) : null" title="Next Passage">+</button>
          </div>
        </div>
      </div>
      <div style="margin-top: 0.85rem; display: flex; gap: 0.5rem;">
        <button class="btn btn-sm btn-primary" style="flex: 1;" onclick="window.N3Class ? window.N3Class.launchTest() : showView('class')">
          <i class="fa-solid fa-play"></i> 今日の授業分をまとめて総復習テスト (Sync Test)
        </button>
      </div>
    </div>
  `;

  // Render Full Dashboard Layout
  container.innerHTML = `
    <div class="today-container">
      <!-- 1. Header Bar -->
      <div class="today-header-row">
        <div class="today-exam-kicker">
          <span class="badge badge-purple">JLPT N3</span>
          <span class="today-countdown">${headerTitle}</span>
        </div>
        <div class="today-header-actions">
          <button class="btn-sync-pill" onclick="openSyncSetup()" aria-label="Sync settings">
            <i class="fa-solid fa-cloud-arrow-up"></i>
            <span>Sync</span>
          </button>
          <button class="btn-icon" onclick="window.openSettingsDrawer ? window.openSettingsDrawer() : openMoreMenu()" aria-label="Settings and Backup" title="Settings">
            <i class="fa-solid fa-gear"></i>
          </button>
        </div>
      </div>

      <!-- Notifications & Banners -->
      ${resumeBannerHtml}
      ${catchUpBannerHtml}
      ${paceWarningHtml}

      <!-- 2. Primary Hero Card (nextBestAction) -->
      <div class="today-hero-card">
        <div class="today-hero-header">
          <span class="today-hero-tag"><i class="fa-solid fa-bolt"></i> Next Best Action</span>
          <span class="today-hero-time"><i class="fa-regular fa-clock"></i> ~${action.estMinutes} min</span>
        </div>
        <div class="today-hero-body">
          <h2 class="today-hero-title">${action.title}</h2>
          <p class="today-hero-sub">${action.subtitle}</p>
        </div>
        <button class="btn btn-primary today-hero-cta" onclick="${action.handler}">
          <i class="fa-solid fa-play"></i> ${action.label}
        </button>
      </div>

      <!-- 3. Due Breakdown & Batch Selector -->
      <div class="today-card today-due-card">
        <div class="today-card-header">
          <span class="today-card-title">Due Reviews</span>
          <span class="today-card-sub">${totalDue} total due</span>
        </div>
        <div class="today-due-pills">
          <button class="due-pill vocab-pill" ${dueV ? '' : 'disabled'} onclick="setDuePillarAndStart('vocab')">
            <span class="due-pill-label">Vocab</span>
            <span class="due-pill-count">${dueV}</span>
          </button>
          <button class="due-pill kanji-pill" ${dueK ? '' : 'disabled'} onclick="setDuePillarAndStart('kanji')">
            <span class="due-pill-label">Kanji</span>
            <span class="due-pill-count">${dueK}</span>
          </button>
          <button class="due-pill grammar-pill" ${dueG ? '' : 'disabled'} onclick="setDuePillarAndStart('grammar')">
            <span class="due-pill-label">Grammar</span>
            <span class="due-pill-count">${dueG}</span>
          </button>
          <button class="due-pill reading-pill" ${dueR ? '' : 'disabled'} onclick="setDuePillarAndStart('reading')">
            <span class="due-pill-label">Reading</span>
            <span class="due-pill-count">${dueR}</span>
          </button>
        </div>
        <div class="today-batch-selector">
          <span class="batch-label">Batch:</span>
          <button class="batch-chip ${currentBatch === '10' ? 'active' : ''}" onclick="setDueBatch('10')">10</button>
          <button class="batch-chip ${currentBatch === '20' ? 'active' : ''}" onclick="setDueBatch('20')">20</button>
          <button class="batch-chip ${currentBatch === '40' ? 'active' : ''}" onclick="setDueBatch('40')">40</button>
          <button class="batch-chip ${currentBatch === 'all' ? 'active' : ''}" onclick="setDueBatch('all')">All</button>
        </div>
      </div>

      <!-- 3.5 Class Track Widget -->
      ${classCardHtml}

      <!-- 4. Today's Plan Checklist -->
      <div class="today-card today-plan-card">
        <div class="today-card-header">
          <span class="today-card-title">Today's Plan</span>
          <span class="today-card-sub">${planStatus.completedCount}/${planStatus.totalCount} completed</span>
        </div>
        <div class="today-plan-list">
          ${planRowsHtml}
        </div>
      </div>

      <!-- 5. Sunday Weekly Check Card -->
      ${weeklyCheckHtml}

      <!-- 6. 30-Day Activity Heatmap & Streak -->
      <div class="today-card today-heatmap-card">
        <div class="today-card-header">
          <div class="streak-badge">
            <i class="fa-solid fa-fire"></i>
            <span>${streak}-day streak</span>
          </div>
          <span class="today-card-sub">Past 30 Days</span>
        </div>
        <div class="heatmap-calendar-wrap">
          ${heatmapGridHtml}
          <div class="heatmap-legend">
            <span class="legend-text">Less</span>
            <span class="legend-cell level-0"></span>
            <span class="legend-cell level-1"></span>
            <span class="legend-cell level-2"></span>
            <span class="legend-cell level-3"></span>
            <span class="legend-cell level-4"></span>
            <span class="legend-text">More</span>
          </div>
        </div>
      </div>

      <!-- 7. Readiness Progress Bars -->
      <div class="today-card today-readiness-card">
        <div class="today-card-header">
          <span class="today-card-title">Readiness</span>
          <span class="today-card-sub">Mastery by Pillar</span>
        </div>
        <div class="readiness-bars-grid">
          ${readinessBarsHtml}
        </div>
      </div>

      <!-- 8. Load Forecast Sparkline (14-day) -->
      <div class="today-card today-forecast-card">
        <div class="today-card-header">
          <span class="today-card-title">Load Forecast</span>
          <span class="today-card-sub">Next 14 Days</span>
        </div>
        <div class="forecast-sparkline-wrap">
          ${forecastBarsHtml}
          ${forecastWarningHtml}
        </div>
      </div>
    </div>
  `;
}

/**
 * Updates batch size preference and re-renders Today view
 */
export function setDueBatch(size) {
  defaultState.dueBatchSize = String(size);
  renderToday();
}

/**
 * Launches due review with specified pillar filter
 */
export function setDuePillarAndStart(pillar) {
  if (typeof window.startDueReview === 'function') {
    window.startDueReview(pillar);
  }
}

/**
 * Quick 5 cards action for staying sharp when all caught up
 */
export function startQuick5() {
  defaultState.dueBatchSize = '5';
  if (typeof window.startDueReview === 'function') {
    window.startDueReview('all');
  }
}

/**
 * Resumes previously unfinished daily session
 */
export function resumeDailySession() {
  if (typeof window.startDueReview === 'function') {
    window.startDueReview('all');
  }
}

// Backward Compatibility Window Bindings
if (typeof window !== 'undefined') {
  window.renderToday = renderToday;
  window.setDueBatch = setDueBatch;
  window.setDuePillarAndStart = setDuePillarAndStart;
  window.startQuick5 = startQuick5;
  window.resumeDailySession = resumeDailySession;

  window.state_pickUnit = function (id) {
    defaultState.selectedChapters = new Set([id]);
    if (typeof window.startStudy === 'function') {
      window.startStudy('flashcard', false, 'home');
    }
  };

  window.openMoreMenu = () => {
    const el = document.getElementById('more-sheet');
    if (el) el.classList.add('open');
  };

  window.closeMoreMenu = () => {
    const el = document.getElementById('more-sheet');
    if (el) el.classList.remove('open');
  };
}

export default {
  renderToday,
  getReadinessStats,
  renderHeatmapGridHtml,
  renderForecastBarsHtml,
  setDueBatch,
  setDuePillarAndStart,
  startQuick5
};
