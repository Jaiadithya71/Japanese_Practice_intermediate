/* SRS-first Hub card: due reviews across all pillars + one primary action.
   Replaces the vocab+reading-only Today card rendering on the Hub. */
import { state } from './state.js';
import { getDueItemsCount } from './srs.js';

const seenIt = s => !!s && (s.reps > 0 || s.correct > 0 || s.incorrect > 0);
const esc = t => String(t == null ? '' : t).replace(/</g, '&lt;');

function istDayStart() {
  const off = 330 * 60000;
  return Math.floor((Date.now() + off) / 86400000) * 86400000 - off;
}

function unitRank(k) {
  return k.startsWith('review_') ? 1000 + parseInt(k.slice(7), 10)
    : k.startsWith('part2_') ? 2000 + parseInt(k.slice(6), 10) : parseInt(k, 10);
}

function nextUnit() {
  const ids = Object.keys(state.vocabDB).sort((a, b) => unitRank(a) - unitRank(b));
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

function bar(label, seen, total) {
  const pct = total ? Math.round(seen / total * 100) : 0;
  return `<div class="today-prog"><div class="today-bar"><span style="width:${pct}%"></span></div><small>${label}: ${seen}/${total} (${pct}%)</small></div>`;
}

export function renderSrsHome() {
  const el = document.getElementById('today-card');
  if (!el) return;
  const start = istDayStart();
  let doneToday = 0;
  for (const k in state.stats) {
    const s = state.stats[k];
    if (s && s.lastSeen >= start) doneToday++;
  }

  let vocabTotal = 0, vocabSeen = 0;
  for (const ch in state.vocabDB) for (const w of state.vocabDB[ch]) {
    vocabTotal++;
    if (seenIt(state.stats[`V:${w.id}`])) vocabSeen++;
  }
  const kanjiChars = Object.keys(state.kanjiDB || {});
  const kanjiSeen = kanjiChars.filter(c => seenIt(state.stats[`K:${c}`])).length;

  const dueV = getDueItemsCount('vocab');
  const dueK = getDueItemsCount('kanji');
  const dueR = getDueItemsCount('reading');
  const due = dueV + dueK + dueR;
  const batch = parseInt(state.dueBatchSize, 10) || 20;
  const unit = nextUnit();
  const les = nextLesson();
  const grammarCount = (state.grammarDB.index || []).length;

  const chip = (n, label, pillar) =>
    `<button class="due-chip" ${n ? '' : 'disabled'} onclick="startDueReview('${pillar}')"><b>${n}</b> ${label}</button>`;

  let primary;
  if (due) {
    const shown = Math.min(due, batch);
    primary = `<button class="today-main btn btn-primary" onclick="startDueReview('all')"><i class="fa-solid fa-play"></i> Start review (${shown}${due > shown ? ` of ${due}` : ''} due)</button>`;
  } else if (unit) {
    primary = `<button class="today-main btn btn-primary" onclick="startLearnNew('${unit.id}')"><i class="fa-solid fa-seedling"></i> All caught up - learn ${Math.min(10, unit.fresh)} new words</button>`;
  } else {
    primary = `<button class="today-main btn btn-primary" disabled><i class="fa-solid fa-circle-check"></i> Nothing due right now</button>`;
  }

  el.innerHTML = `
    <div class="today-head">
      <div><div class="today-kicker">Today</div>
        <div class="today-sub">${doneToday} reviewed today &middot; ${due} due</div></div>
      <button class="today-sync" onclick="openSyncSetup()" aria-label="Sync settings"><i class="fa-solid fa-cloud-arrow-up"></i></button>
    </div>
    ${primary}
    <div class="due-chips">
      ${chip(dueV, 'vocab', 'vocab')}${chip(dueK, 'kanji', 'kanji')}${chip(dueR, 'reading', 'reading')}
    </div>
    <div class="today-steps">
      ${unit ? `<button class="today-step" onclick="startLearnNew('${unit.id}')"><span class="ts-n"><i class="fa-solid fa-seedling"></i></span><span class="ts-t">Learn new words<small>${unitLabel(unit.id)}: ${unit.fresh} of ${unit.total} unseen, ${Math.min(10, unit.fresh)} per session</small></span><i class="fa-solid fa-chevron-right"></i></button>` : ''}
      <button class="today-step" onclick="showView('kanji')"><span class="ts-n"><i class="fa-solid fa-shapes"></i></span><span class="ts-t">Kanji<small>${kanjiSeen} of ${kanjiChars.length} started${dueK ? `, ${dueK} due` : ''}</small></span><i class="fa-solid fa-chevron-right"></i></button>
      <button class="today-step" onclick="showView('grammar')"><span class="ts-n"><i class="fa-solid fa-diagram-project"></i></span><span class="ts-t">Grammar<small>${grammarCount} patterns &middot; browse and drills (not in the review queue yet)</small></span><i class="fa-solid fa-chevron-right"></i></button>
      ${les ? `<button class="today-step" onclick="openReadingLesson('${les.id}')"><span class="ts-n"><i class="fa-solid fa-book-open-reader"></i></span><span class="ts-t">Read one lesson<small>${esc(les.title)}</small></span><i class="fa-solid fa-chevron-right"></i></button>` : ''}
    </div>
    ${bar('Vocab started', vocabSeen, vocabTotal)}
    ${bar('Kanji started', kanjiSeen, kanjiChars.length)}`;
}
