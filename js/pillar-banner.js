/* =======================================================
   NIHONGO INTERMEDIATE — pillar-banner.js
   SRS block per page (streak, due, progress, next lesson + action)
   and a four-pillar overview on the landing page.
   ======================================================= */

import { state } from './state.js';
import { getDueItemsCount, getItemStatus } from './srs.js';
import { getCurrentStreak, getDay } from './daylog.js';
import { istDateKey } from './time.js';
import { startDueReview, startLearnNew } from './study.js?v=4.4';
import { showView } from './navigation.js';

const PILLARS = {
  vocab:   { label: '語彙 Vocab',     color: 'var(--accent)', view: 'vocab' },
  kanji:   { label: '漢字 Kanji',     color: '#ec4899',       view: 'kanji' },
  grammar: { label: '文法 Grammar',   color: 'var(--amber)',  view: 'grammar' },
  reading: { label: '読解 Reading',   color: 'var(--cyan)',   view: 'reading' }
};

const seen = s => !!s && ((s.reps || 0) > 0 || (s.correct || 0) > 0 || (s.incorrect || 0) > 0);
const stripHtml = h => String(h || '').replace(/<rt>.*?<\/rt>/g, '').replace(/<[^>]+>/g, '').trim();

function statusCounts(keys) {
  let mastered = 0, learning = 0, hard = 0, unseen = 0;
  keys.forEach(ks => {
    const st = ks.map(k => getItemStatus(k));
    const any = ks.some(k => seen(state.stats && state.stats[k]));
    if (!any) { unseen++; return; }
    if (st.includes('hard')) hard++;
    else if (st.every(x => x === 'mastered')) mastered++;
    else learning++;
  });
  return { mastered, learning, hard, unseen, total: keys.length };
}

function vocabInfo() {
  const rank = k => (String(k).startsWith('review_') ? 1000 + parseInt(String(k).slice(7), 10) : parseInt(String(k).replace('part2_', ''), 10)) || 0;
  const units = Object.keys(state.vocabDB || {}).sort((a, b) => rank(a) - rank(b));
  const all = [];
  let next = null;
  units.forEach(u => {
    const words = state.vocabDB[u] || [];
    let fresh = 0;
    words.forEach(w => { all.push([`V:${w.id}`]); if (!seen(state.stats && state.stats[`V:${w.id}`])) fresh++; });
    if (!next && fresh > 0) next = { unit: u, fresh, total: words.length };
  });
  const c = statusCounts(all);
  return {
    counts: c,
    nextLabel: next ? `Unit ${next.unit} · ${next.fresh} new word${next.fresh === 1 ? '' : 's'}` : null,
    nextAction: next ? () => startLearnNew(next.unit, 10) : null,
    nextBtn: next ? 'Learn 10 new' : null
  };
}

function kanjiInfo() {
  const all = [];
  const byLesson = {};
  for (const ch in (state.kanjiDB || {})) {
    const k = state.kanjiDB[ch];
    const keys = [`K:${ch}`];
    (k.words || []).forEach(w => {
      const word = (w.term_ja || w.word || ch).trim();
      keys.push(`KWR:${word}`, `KWW:${word}`, `KWM:${word}`);
    });
    all.push(keys);
    const l = k.lesson_number || 1;
    const b = byLesson[l] || (byLesson[l] = { fresh: 0, total: 0 });
    b.total++;
    if (!keys.some(x => seen(state.stats && state.stats[x]))) b.fresh++;
  }
  const lessons = Object.keys(byLesson).map(Number).sort((a, b) => a - b);
  const nl = lessons.find(l => byLesson[l].fresh > 0);
  const title = nl && (state.kanjiLessons || []).find(x => x.lesson_number === nl);
  return {
    counts: statusCounts(all),
    nextLabel: nl ? `Lesson ${nl}${title && title.title_ja ? ' ' + stripHtml(title.title_ja) : ''} · ${byLesson[nl].fresh} new kanji` : null,
    nextAction: nl ? () => {
      state.kanjiSelectedLessons = new Set([nl]);
      state.kanjiLesson = nl;
      state.kanjiHardOnly = false;
      if (typeof window.drillKanjiSelected === 'function') window.drillKanjiSelected();
    } : null,
    nextBtn: nl ? `Drill Lesson ${nl}` : null
  };
}

function grammarInfo() {
  const idx = (state.grammarDB && state.grammarDB.index) || [];
  const all = idx.map(p => [`G:${p.id}`]);
  const sections = [];
  const map = {};
  idx.forEach(p => {
    const s = p.section_id || 'misc';
    if (!map[s]) { map[s] = { title: stripHtml(p.section_title) || s, fresh: 0 }; sections.push(s); }
    if (!seen(state.stats && state.stats[`G:${p.id}`])) map[s].fresh++;
  });
  const ns = sections.find(s => map[s].fresh > 0);
  return {
    counts: statusCounts(all),
    nextLabel: ns ? `${map[ns].title} · ${map[ns].fresh} new pattern${map[ns].fresh === 1 ? '' : 's'}` : null,
    nextAction: ns ? () => showView('grammar') : null,
    nextBtn: ns ? 'Open Grammar' : null
  };
}

function readingInfo() {
  const ids = Object.keys(state.readingDB || {});
  const all = [];
  let next = null;
  ids.forEach(lid => {
    const lesson = state.readingDB[lid] || {};
    const qs = lesson.comprehensionQuestions || lesson.questions || [];
    let fresh = 0;
    qs.forEach(q => {
      const k = `R_Q:${q.id || `${lid}_q${q.questionNumber || 1}`}`;
      all.push([k]);
      if (!seen(state.stats && state.stats[k])) fresh++;
    });
    if (!next && fresh > 0) next = { title: stripHtml(lesson.title_ja || lesson.title || lid), fresh };
  });
  return {
    counts: statusCounts(all),
    nextLabel: next ? `${next.title} · ${next.fresh} new question${next.fresh === 1 ? '' : 's'}` : null,
    nextAction: next ? () => showView('reading') : null,
    nextBtn: next ? 'Open Reading' : null
  };
}

const INFO = { vocab: vocabInfo, kanji: kanjiInfo, grammar: grammarInfo, reading: readingInfo };
const actions = {};

function pillarData(p) {
  const info = INFO[p]();
  actions[p] = info;
  return { ...info, due: getDueItemsCount(p) };
}

function streakChip(pillar = null) {
  let streak = 0, today = 0;
  try {
    streak = getCurrentStreak(undefined, pillar);
    const d = getDay(istDateKey(Date.now()));
    today = pillar ? (d.pillars?.[pillar] || 0) : (d.reviews || 0) + (d.newCards || 0);
  } catch (e) { /* ignore */ }
  const hot = today > 0;
  return `<span class="pb-streak ${hot ? 'hot' : ''}"><i class="fa-solid fa-fire"></i> ${streak} day streak${hot || pillar ? '' : streak > 0 ? ' · study today to keep it' : ''}</span>`;
}

function bannerHtml(p, d, compact) {
  const c = d.counts;
  const pct = c.total ? Math.round((c.mastered / c.total) * 100) : 0;
  const meta = PILLARS[p];
  const nextRow = d.nextLabel
    ? `<div class="pb-next"><div><span class="pb-k">Next lesson</span><span class="pb-v">${d.nextLabel}</span></div>${compact || p === 'kanji' ? '' : `<button class="pb-btn" onclick="window.__pbNext('${p}')">${d.nextBtn} <i class="fa-solid fa-arrow-right"></i></button>`}</div>`
    : `<div class="pb-next"><div><span class="pb-k">Next lesson</span><span class="pb-v">Everything started - keep reviewing</span></div></div>`;
  return `
    <div class="pb-top">
      ${compact ? `<span class="pb-title" style="color:${meta.color}">${meta.label}</span>` : streakChip(p === 'kanji' ? 'kanji' : null)}
      <span class="pb-due ${d.due > 0 ? 'has' : ''}">${d.due > 0 ? d.due + ' due' : 'Caught up'}</span>
    </div>
    <div class="pb-stats">
      <span><b class="g">${c.mastered}</b> mastered</span><span><b class="a">${c.learning}</b> learning</span><span><b class="r">${c.hard}</b> hard</span><span><b class="m">${c.unseen}</b> new</span>
    </div>
    ${p === 'kanji' ? `<div class="pb-bar pb-segments" role="img" aria-label="${c.mastered} mastered, ${c.learning} learning, ${c.hard} hard, ${c.unseen} new">${[['mastered',c.mastered],['learning',c.learning],['hard',c.hard],['new',c.unseen]].filter(([,n]) => n > 0).map(([status,n]) => `<span class="pb-segment-${status}" style="width:${c.total ? n/c.total*100 : 0}%"></span>`).join('')}</div>` : `<div class="pb-bar"><div style="width:${pct}%;background:${meta.color}"></div></div>`}
    ${nextRow}
    ${compact ? '' : `<div class="pb-actions">${p === 'kanji' && d.nextLabel ? `<button class="pb-btn" onclick="window.__pbNext('kanji')">${d.nextBtn} <i class="fa-solid fa-arrow-right"></i></button>` : ''}<button class="pb-btn ghost" ${d.due > 0 ? '' : 'disabled'} onclick="window.__pbDue('${p}')"><i class="fa-solid fa-bolt"></i> Review ${d.due} due</button></div>`}`;
}

function injectStyle() {
  if (document.getElementById('pb-style')) return;
  const s = document.createElement('style');
  s.id = 'pb-style';
  s.textContent = `
.pb-card{background:var(--bg-card,#141821);border:1px solid var(--border,#2a2f3a);border-radius:16px;padding:.9rem 1rem;margin:0 0 1rem;display:flex;flex-direction:column;gap:.6rem}
.pb-top{display:flex;justify-content:space-between;align-items:center;gap:.5rem}
.pb-title{font-weight:800;font-size:.95rem}
.pb-streak{font-size:.8rem;font-weight:700;color:var(--text-muted,#9aa3b2)}.pb-streak.hot{color:#fb923c}
.pb-due{font-size:.75rem;font-weight:700;padding:.2rem .6rem;border-radius:999px;background:rgba(52,211,153,.12);color:#34d399}.pb-due.has{background:rgba(129,140,248,.18);color:#a5b4fc}
.pb-stats{display:flex;gap:.9rem;flex-wrap:wrap;font-size:.75rem;color:var(--text-muted,#9aa3b2)}
.pb-stats b{font-size:.95rem;margin-right:.2rem}.pb-stats .g{color:#34d399}.pb-stats .a{color:#fbbf24}.pb-stats .r{color:#f87171}.pb-stats .m{color:#9aa3b2}
.pb-bar{height:6px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}.pb-bar>div{height:100%;border-radius:99px;transition:width .4s}
.pb-next{display:flex;justify-content:space-between;align-items:center;gap:.6rem;border-top:1px solid rgba(255,255,255,.06);padding-top:.6rem}
.pb-k{display:block;font-size:.65rem;text-transform:uppercase;letter-spacing:.04em;color:var(--text-dim,#6b7280);font-weight:700}
.pb-v{display:block;font-size:.85rem;color:#fff;font-weight:600}
.pb-actions{display:flex;gap:.5rem}
.pb-btn{border:none;cursor:pointer;border-radius:10px;padding:.5rem .8rem;font-size:.8rem;font-weight:700;color:#fff;background:linear-gradient(135deg,#6366f1,#8b5cf6);white-space:nowrap}
.pb-btn.ghost{background:rgba(255,255,255,.07);border:1px solid var(--border,#2a2f3a)}.pb-btn:disabled{opacity:.4;cursor:default}
.pb-overview{display:grid;grid-template-columns:repeat(2,1fr);gap:.75rem;margin:0 0 1.25rem}
.pb-overview .pb-card{margin:0;cursor:pointer}
.pb-overview-head{grid-column:1/-1;display:flex;justify-content:space-between;align-items:center}
#pb-kanji{gap:.65rem;padding:1rem;border-color:rgba(212,175,106,.2);background:linear-gradient(135deg,rgba(212,175,106,.045),transparent 65%),var(--bg-card,#141821)}
#pb-kanji .pb-streak.hot{color:var(--accent,#d4af6a)}
#pb-kanji .pb-due.has{background:var(--accent-light);color:var(--accent)}
#pb-kanji .pb-stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.35rem}
#pb-kanji .pb-stats span{display:flex;flex-direction:column;gap:.12rem;font-size:.68rem}
#pb-kanji .pb-stats b{font-size:1.05rem;line-height:1.2;margin:0;font-variant-numeric:tabular-nums}
#pb-kanji .pb-stats .a{color:var(--accent)}
#pb-kanji .pb-segments{display:flex;height:5px;gap:2px;background:transparent;margin:0 0 .1rem}
#pb-kanji .pb-segments span{height:100%;flex-shrink:1}
.pb-segment-mastered{background:#34d399}.pb-segment-learning{background:var(--accent,#d4af6a)}.pb-segment-hard{background:#f87171}.pb-segment-new{background:#424d61}
#pb-kanji .pb-next{display:block;padding-top:.65rem}
#pb-kanji .pb-v{font-size:.8rem;line-height:1.5;margin:.2rem 0 .6rem;color:var(--text)}
#pb-kanji .pb-btn{min-height:42px;background:linear-gradient(135deg,#e6cb91,#c49c52);color:#171d2b;width:100%}
#pb-kanji .pb-btn.ghost{background:transparent;border-color:rgba(212,175,106,.28);color:var(--accent)}
#pb-kanji .pb-actions{margin-top:-.2rem}#pb-kanji .pb-actions .pb-btn{flex:1;min-width:0;width:auto;padding:.5rem .45rem;font-size:.74rem}
@media(min-width:900px){.pb-overview{grid-template-columns:repeat(4,1fr)}}
`;
  document.head.appendChild(s);
}

let lastSig = '';

export function renderPillarBanners() {
  if (typeof document === 'undefined' || !state.stats) return;
  injectStyle();
  const dataByP = {};
  Object.keys(PILLARS).forEach(p => { try { dataByP[p] = pillarData(p); } catch (e) { /* skip */ } });

  // Per-page banners
  Object.keys(PILLARS).forEach(p => {
    const view = document.getElementById(`view-${p}`);
    if (!view || !dataByP[p]) return;
    let el = document.getElementById(`pb-${p}`);
    if (!el) {
      el = document.createElement('div');
      el.id = `pb-${p}`;
      el.className = 'pb-card';
      const header = view.querySelector('.view-header');
      if (header && header.nextSibling) header.parentNode.insertBefore(el, header.nextSibling);
      else view.prepend(el);
    }
    el.innerHTML = bannerHtml(p, dataByP[p], false);
    if (p === 'kanji') {
      const picker = view.querySelector('.home-lessons-card');
      if (picker && picker.nextElementSibling !== el) picker.after(el);
    }
  });

  // Landing overview
  const home = document.getElementById('view-home');
  if (home) {
    let ov = document.getElementById('pb-overview');
    if (!ov) {
      ov = document.createElement('div');
      ov.id = 'pb-overview';
      ov.className = 'pb-overview';
      const anchor = document.getElementById('today-card');
      if (anchor && anchor.nextSibling) anchor.parentNode.insertBefore(ov, anchor.nextSibling);
      else home.prepend(ov);
    }
    const totalDue = Object.values(dataByP).reduce((a, d) => a + d.due, 0);
    ov.innerHTML = `<div class="pb-overview-head">${streakChip()}<span class="pb-due ${totalDue > 0 ? 'has' : ''}">${totalDue > 0 ? totalDue + ' due today' : 'All caught up'}</span></div>` +
      Object.keys(PILLARS).filter(p => dataByP[p]).map(p => `<div class="pb-card" onclick="showView('${PILLARS[p].view}')">${bannerHtml(p, dataByP[p], true)}</div>`).join('');
  }
}

function signature() {
  const n = state.stats ? Object.keys(state.stats).length : 0;
  let sum = 0;
  if (state.stats) for (const k in state.stats) { const s = state.stats[k]; sum += (s.reps || 0) + (s.correct || 0) + (s.incorrect || 0); }
  return `${state.currentView}|${n}|${sum}|${Object.keys(state.vocabDB || {}).length}|${Object.keys(state.kanjiDB || {}).length}`;
}

if (typeof window !== 'undefined') {
  window.__pbNext = p => { const a = actions[p]; if (a && a.nextAction) a.nextAction(); };
  window.__pbDue = p => startDueReview(p);
  window.renderPillarBanners = renderPillarBanners;
  setInterval(() => {
    if (state.currentView === 'study') return;
    const sig = signature();
    if (sig !== lastSig) { lastSig = sig; try { renderPillarBanners(); } catch (e) { /* ignore */ } }
  }, 1200);
}
