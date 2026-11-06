/* =======================================================
   UPDATE CHECK — detect a newer deployed build and offer a
   one-tap refresh, so fixes actually reach resumed sessions.

   Why: the app's HTML/JS is served with must-revalidate, but a
   long-resumed phone session (PWA / background tab) can keep
   running an old build for days without ever re-fetching. The
   single version marker is the ?v= query on js/main.js in
   index.html; bump it on every deploy and this check notices.
   ======================================================= */

const UPDATE_CHECK_TAG = () => {
  const el = document.querySelector('script[type="module"][src*="main.js"]');
  if (!el) return null;
  const m = el.src.match(/[?&]v=([^&]+)/);
  return m ? m[1] : null;
};

function extractBuildTag(html) {
  const m = html.match(/main\.js\?v=([^"']+)/);
  return m ? m[1] : null;
}

function ensureUpdateCheckStyle() {
  if (document.getElementById('n3-update-check-style')) return;
  const style = document.createElement('style');
  style.id = 'n3-update-check-style';
  style.textContent = `
    #n3-update-pill {
      position: fixed;
      left: 50%;
      bottom: calc(env(safe-area-inset-bottom, 0px) + 14px);
      transform: translateX(-50%);
      z-index: 4000;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--bg3, #171c2b);
      color: var(--accent, #d4af6a);
      border: 1px solid var(--accent, #d4af6a);
      border-radius: 999px;
      padding: 0.45rem 0.9rem;
      font-size: 0.82rem;
      font-family: inherit;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.45);
      cursor: pointer;
      white-space: nowrap;
    }
    #n3-update-pill .n3-update-dismiss {
      color: var(--text-dim, #505570);
      border: none;
      background: none;
      padding: 0 0 0 0.25rem;
      font-size: 0.9rem;
      cursor: pointer;
    }
  `;
  document.head.appendChild(style);
}

function showUpdatePill(latestTag) {
  if (document.getElementById('n3-update-pill')) return;
  try {
    if (sessionStorage.getItem('n3_update_dismissed') === latestTag) return;
  } catch (e) { /* sessionStorage unavailable: show the pill anyway */ }
  ensureUpdateCheckStyle();
  const pill = document.createElement('button');
  pill.id = 'n3-update-pill';
  pill.type = 'button';
  pill.innerHTML = '<i class="fa-solid fa-rotate"></i><span>Update available - tap to refresh</span><span class="n3-update-dismiss" role="button" aria-label="Dismiss">&times;</span>';
  pill.addEventListener('click', () => location.reload());
  pill.querySelector('.n3-update-dismiss').addEventListener('click', (ev) => {
    ev.stopPropagation();
    try { sessionStorage.setItem('n3_update_dismissed', latestTag); } catch (e) {}
    pill.remove();
  });
  document.body.appendChild(pill);
}

// Compares the running build tag with the latest deployed one and shows the
// refresh pill on mismatch. Pass a string to skip the fetch (used by tests).
export async function checkForUpdate(latestOverride) {
  const current = UPDATE_CHECK_TAG();
  if (!current) return false;
  let latest = typeof latestOverride === 'string' ? latestOverride : null;
  if (!latest) {
    try {
      const res = await fetch(`${location.pathname || '/'}?update-check=${Date.now()}`, { cache: 'no-store' });
      if (!res.ok) return false;
      latest = extractBuildTag(await res.text());
    } catch (e) {
      return false; // offline or blocked: stay quiet
    }
  }
  if (latest && latest !== current) {
    showUpdatePill(latest);
    return true;
  }
  return false;
}

export function initUpdateCheck() {
  // Check once after startup, and again whenever a long-hidden session
  // resumes - the exact situation that strands an old build.
  checkForUpdate();
  let hiddenAt = 0;
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      hiddenAt = Date.now();
    } else if (hiddenAt && Date.now() - hiddenAt > 2 * 60 * 1000) {
      checkForUpdate();
    }
  });
}

window.checkN3Update = checkForUpdate;
