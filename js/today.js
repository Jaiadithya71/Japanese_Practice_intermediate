/* Today card: daily study flow for the Hub */
import { state } from './state.js';
import './pull-refresh.js';
import { getDueItemsCount } from './srs.js';

const seenIt = s => !!s && (s.reps > 0 || s.correct > 0 || s.incorrect > 0);

function istDayStart() {
  const off = 330 * 60000;
  return Math.floor((Date.now() + off) / 86400000) * 86400000 - off;
}

function nextUnit() {
  const rank = k => (k.startsWith('review_') ? 1000 + parseInt(k.slice(7), 10) : k.startsWith('part2_') ? 2000 + parseInt(k.slice(6), 10) : parseInt(k, 10));
  const ids = Object.keys(state.vocabDB).sort((a, b) => rank(a) - rank(b));
  for (const id of ids) {
    const words = state.vocabDB[id] || [];
    const fresh = words.filter(w => !seenIt(state.stats[`V:${w.id}`])).length;
    if (fresh > 0) return { id, fresh, total: words.length };
  }
  return null;
}

function nextLesson() {
  for (const lid of Object.keys(state.readingDB)) {
    const lesson = state.readingDB[lid];
    const qs = lesson.comprehensionQuestions || lesson.questions || [];
    const touched = qs.some(q => seenIt(state.stats[`R_Q:${q.id || `${lid}_q${q.questionNumber || 1}`}`]));
    if (!touched) return { id: lid, title: lesson.title_en || lesson.title_ja || lid };
  }
  return null;
}

function unitLabel(id) {
  const m = (state.chapterMetadata[id] || {}).topic_en;
  const n = id.startsWith('review_') ? 'Review ' + id.slice(7) : id.startsWith('part2_') ? 'Characteristics ' + id.slice(6) : 'Unit ' + id;
  return n + (m ? ' - ' + m : '');
}

export function renderToday() {
  const el = document.getElementById('today-card');
  if (!el) return;
  const start = istDayStart();
  let doneToday = 0, seen = 0, vocabTotal = 0, vocabSeen = 0;
  for (const k in state.stats) {
    const s = state.stats[k];
    if (s && s.lastSeen >= start) doneToday++;
  }
  for (const ch in state.vocabDB) for (const w of state.vocabDB[ch]) {
    vocabTotal++;
    if (seenIt(state.stats[`V:${w.id}`])) vocabSeen++;
  }
  const dueV = getDueItemsCount('vocab');
  const dueR = getDueItemsCount('reading');
  const due = dueV + dueR;
  const unit = nextUnit();
  const les = nextLesson();
  const pct = vocabTotal ? Math.round(vocabSeen / vocabTotal * 100) : 0;
  el.innerHTML = `
    <div class="today-head">
      <div><div class="today-kicker">Today</div>
        <div class="today-sub">${doneToday} reviewed today</div></div>
      <button class="today-sync" onclick="openSyncSetup()" aria-label="Sync settings"><i class="fa-solid fa-cloud-arrow-up"></i></button>
    </div>
    <button class="today-main btn btn-primary" onclick="startDueReview('all')" ${due ? '' : 'disabled'}>
      <i class="fa-solid fa-play"></i> ${due ? `Start review (${due} due)` : 'Nothing due right now'}
    </button>
    <div class="today-split">${dueV} vocab &middot; ${dueR} reading</div>
    <div class="today-steps">
      ${unit ? `<button class="today-step" onclick="state_pickUnit('${unit.id}')"><span class="ts-n">2</span><span class="ts-t">Learn new words<small>${unitLabel(unit.id)}: ${unit.fresh} of ${unit.total} unseen</small></span><i class="fa-solid fa-chevron-right"></i></button>` : ''}
      ${les ? `<button class="today-step" onclick="openReadingLesson('${les.id}')"><span class="ts-n">3</span><span class="ts-t">Read one lesson<small>${String(les.title).replace(/</g, '&lt;')}</small></span><i class="fa-solid fa-chevron-right"></i></button>` : ''}
    </div>
    <div class="today-prog"><div class="today-bar"><span style="width:${pct}%"></span></div><small>Vocab seen: ${vocabSeen}/${vocabTotal} (${pct}%)</small></div>`;
}

window.state_pickUnit = function (id) {
  state.selectedChapters = new Set([id]);
  window.startStudy('flashcard', false, 'home');
};

window.openMoreMenu = () => document.getElementById('more-sheet').classList.add('open');
window.closeMoreMenu = () => document.getElementById('more-sheet').classList.remove('open');
