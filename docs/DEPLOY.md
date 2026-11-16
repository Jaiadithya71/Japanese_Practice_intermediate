# Deploy checklist (every push to main)

Vercel auto-deploys every push to `main`. Phones run this app as a resumed
PWA session for days, so a deploy that changes any js/css file MUST bump the
build marker in `index.html`:

    <script type="module" src="js/main.js?v=4.19-hrd1"></script>

The in-app update check (js/update-check.js) compares this tag to detect new
builds and show the "Update available - tap to refresh" pill. If the tag is
not bumped, resumed sessions never learn about the deploy and keep running
the old build (2026-11-16: 0537e01 changed js/home.js without a bump; the
phone kept the stale session, buttons froze until a full restart).

Rules:
1. Any push touching js/ or css/ bumps the main.js ?v= tag in index.html.
2. When js/home.js changes, bump its ?v= tag in BOTH importers
   (js/main.js and js/navigation.js) to the same new value. The two imports
   must always carry an identical query, or the browser loads home.js twice
   as two separate module instances with separate state.
