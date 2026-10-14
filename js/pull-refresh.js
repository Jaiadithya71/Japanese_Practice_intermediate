/* Pull-down-to-refresh for the mobile app (main scroller #main) */
import { state } from './state.js';

const THRESH = 70, MAX = 110;
let startY = 0, pulling = false, dist = 0, busy = false;
const el = document.createElement('div');
el.id = 'ptr';
el.innerHTML = '<i class="fa-solid fa-arrow-down"></i><span>Pull to refresh</span>';
document.addEventListener('DOMContentLoaded', () => document.body.appendChild(el));
if (document.body) document.body.appendChild(el);

function ok() {
  const main = document.getElementById('main');
  if (!main || busy || window.innerWidth > 900) return false;
  if (state.currentView === 'study') return false;
  const ov = document.getElementById('n3s-overlay');
  if (ov && !ov.classList.contains('n3s-hide')) return false;
  const ms = document.getElementById('more-sheet');
  if (ms && ms.classList.contains('open')) return false;
  return main.scrollTop <= 0;
}

document.addEventListener('touchstart', e => {
  if (e.touches.length !== 1 || !ok()) return;
  startY = e.touches[0].clientY; pulling = true; dist = 0;
}, { passive: true });

document.addEventListener('touchmove', e => {
  if (!pulling) return;
  const dy = e.touches[0].clientY - startY;
  if (dy <= 0) { dist = 0; el.style.transform = ''; el.classList.remove('show'); return; }
  const main = document.getElementById('main');
  if (main && main.scrollTop > 0) { pulling = false; return; }
  dist = Math.min(MAX, dy * 0.5);
  el.classList.add('show');
  el.style.transform = `translate(-50%, ${dist - 50}px)`;
  const ready = dist >= THRESH * 0.8;
  el.classList.toggle('ready', ready);
  el.querySelector('span').textContent = ready ? 'Release to refresh' : 'Pull to refresh';
}, { passive: true });

async function end() {
  if (!pulling) return;
  pulling = false;
  if (dist >= THRESH * 0.8) {
    busy = true;
    el.classList.add('loading');
    el.classList.remove('ready');
    el.querySelector('i').className = 'ptr-ring';
    el.querySelector('span').textContent = 'Refreshing...';
    el.style.transform = 'translate(-50%, 24px)';
    let synced = false;
    try {
      if (window.forceSyncNow && localStorage.getItem('n3_github_pat') && localStorage.getItem('n3_gist_id')) {
        await Promise.race([window.forceSyncNow(), new Promise(r => setTimeout(r, 4000))]);
        const pill = document.getElementById('n3sync-status');
        synced = !!pill && pill.classList.contains('n3s-ok');
      }
    } catch (e) { /* ignore, reload anyway */ }
    if (synced) {
      el.classList.remove('loading');
      el.classList.add('done');
      el.querySelector('i').className = 'fa-solid fa-circle-check';
      el.querySelector('span').textContent = 'Synced';
      await new Promise(r => setTimeout(r, 650));
    }
    location.reload();
  } else {
    el.classList.remove('show', 'ready');
    el.style.transform = '';
  }
}
document.addEventListener('touchend', end, { passive: true });
document.addEventListener('touchcancel', end, { passive: true });
