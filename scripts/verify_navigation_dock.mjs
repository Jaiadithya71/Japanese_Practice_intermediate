/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_navigation_dock.mjs
   Verification Harness for Navigation Shell & Mobile Layout (WP-7)
   Tests:
   1. VIEW_TO_TAB mappings for all legacy and new routes.
   2. index.html structural audit (5-tab floating glass dock,
      desktop sidebar clean-up, tab containers, linked stylesheets).
   3. CSS verification (frosted glass, 48px touch targets, runner hide).
   4. DOM & State behavior (segment switching, runner hide/restore,
      window.* bindings).
   ======================================================= */

import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

console.log('--- Starting WP-7 Verification (Navigation Shell & Mobile Layout) ---');

// ==========================================
// 1. Static HTML Audit: index.html
// ==========================================
console.log('\n[1/4] Auditing index.html structure & markup...');

const indexHtmlPath = path.resolve('index.html');
assert.ok(fs.existsSync(indexHtmlPath), 'index.html must exist');
const html = fs.readFileSync(indexHtmlPath, 'utf8');

// Verify css/today.css is linked in <head>
assert.ok(
  html.includes('<link rel="stylesheet" href="css/today.css"') ||
  html.includes("<link rel='stylesheet' href='css/today.css'"),
  'css/today.css must be linked in index.html <head>'
);

// Verify Listening alert row is removed from desktop sidebar
assert.ok(
  !html.includes("alert('Book 5: Listening"),
  'Listening alert row must be removed from desktop sidebar'
);

// Verify 5-tab mobile dock exists with id="mobile-dock"
assert.ok(html.includes('id="mobile-dock"'), 'nav#mobile-dock must exist in index.html');
assert.ok(html.includes('class="mobile-dock'), 'nav#mobile-dock must have class "mobile-dock"');

// Verify the 5 dock items:
const expectedTabs = [
  { tab: 'today', icon: 'fa-calendar-day', label: '今日 Today' },
  { tab: 'learn', icon: 'fa-graduation-cap', label: '学習 Learn' },
  { tab: 'read', icon: 'fa-book-open', label: '読解 Read' },
  { tab: 'test', icon: 'fa-file-pen', label: '試験 Test' },
  { tab: 'me', icon: 'fa-user', label: '私 Me' }
];

for (const t of expectedTabs) {
  assert.ok(
    html.includes(`data-tab="${t.tab}"`),
    `Mobile dock must include data-tab="${t.tab}"`
  );
  assert.ok(
    html.includes(`showView('${t.tab}')`),
    `Mobile dock must invoke showView('${t.tab}')`
  );
  assert.ok(
    html.includes(t.icon),
    `Mobile dock tab ${t.tab} must contain icon ${t.icon}`
  );
  assert.ok(
    html.includes(t.label),
    `Mobile dock tab ${t.tab} must contain label ${t.label}`
  );
}

// Verify Container Views in index.html
assert.ok(html.includes('id="view-today"'), 'div#view-today container must exist');
assert.ok(html.includes('id="view-home"'), 'section#view-home must be preserved inside/alongside view-today');
assert.ok(html.includes('id="view-learn"'), 'div#view-learn container must exist');
assert.ok(html.includes('id="view-kanji"'), 'section#view-kanji must be preserved');
assert.ok(html.includes('id="view-vocab"'), 'section#view-vocab must be preserved');
assert.ok(html.includes('id="view-grammar"'), 'section#view-grammar must be preserved');
assert.ok(html.includes('id="view-read"'), 'div#view-read container must exist');
assert.ok(html.includes('id="view-reading"'), 'section#view-reading must be preserved');
assert.ok(html.includes('id="view-test"'), 'section#view-test must be preserved');
assert.ok(html.includes('id="view-me"'), 'div#view-me container must exist');
assert.ok(html.includes('id="view-hard-words"'), 'section#view-hard-words must be preserved in Me tab');
assert.ok(html.includes('id="view-study"'), 'section#view-study runner must be preserved');

// Verify Learn segmented control
assert.ok(html.includes('data-segment="kanji"'), 'Learn segmented control must have kanji segment');
assert.ok(html.includes('data-segment="vocab"'), 'Learn segmented control must have vocab segment');
assert.ok(html.includes('data-segment="grammar"'), 'Learn segmented control must have grammar segment');

// Verify Me segmented control
assert.ok(html.includes('data-segment="weak"'), 'Me segmented control must have weak segment');
assert.ok(html.includes('data-segment="stats"'), 'Me segmented control must have stats segment');
assert.ok(html.includes('data-segment="settings"'), 'Me segmented control must have settings segment');

console.log('✓ index.html structure verified successfully');

// ==========================================
// 2. CSS Audit: navigation.css & mobile.css
// ==========================================
console.log('\n[2/4] Auditing CSS rules (Glassmorphism & Touch Targets)...');

const navCss = fs.readFileSync(path.resolve('css/navigation.css'), 'utf8');
const mobileCss = fs.readFileSync(path.resolve('css/mobile.css'), 'utf8');
const combinedCss = navCss + '\n' + mobileCss;

// Frosted glassmorphism parameters
assert.ok(combinedCss.includes('rgba(19, 22, 29, 0.85)') || combinedCss.includes('rgba(19,22,29,.85)'), 'Must include 0.85 opacity dark background');
assert.ok(combinedCss.includes('blur(16px)'), 'Must include blur(16px) backdrop-filter');
assert.ok(combinedCss.includes('border-radius: 20px') || combinedCss.includes('border-radius:20px'), 'Must include 20px border-radius');
assert.ok(combinedCss.includes('box-shadow: 0 8px 32px') || combinedCss.includes('box-shadow:0 8px 32px'), 'Must include 0 8px 32px box-shadow');
assert.ok(combinedCss.includes('height: 62px') || combinedCss.includes('height:62px'), 'Dock height must be 62px');

// Touch targets >= 48px
assert.ok(combinedCss.includes('min-height: 48px') || combinedCss.includes('min-height:48px'), 'Must define min-height >= 48px for touch targets');
assert.ok(combinedCss.includes('min-width: 48px') || combinedCss.includes('min-width:48px'), 'Must define min-width >= 48px for dock items');

// Runner mode dock hide
assert.ok(combinedCss.includes('body.in-runner') && combinedCss.includes('display: none'), 'Dock must be hidden in runner mode via body.in-runner');

// Desktop media query hiding mobile dock
assert.ok(combinedCss.includes('@media (min-width: 900px)') || combinedCss.includes('@media (min-width:900px)'), 'Mobile dock must be hidden on desktop (>=900px)');

// Safe padding on mobile
assert.ok(combinedCss.includes('84px'), 'Main container must provide at least 84px safe bottom padding on mobile');

console.log('✓ CSS specifications verified successfully');

// ==========================================
// 3. Setup DOM Environment & Test VIEW_TO_TAB
// ==========================================
console.log('\n[3/4] Testing VIEW_TO_TAB mappings...');

// Mock Element & Document for Node environment
class MockElement {
  constructor(id = '', tag = 'div', classes = []) {
    this.id = id;
    this.tagName = tag.toUpperCase();
    const set = new Set(classes);
    this.classList = {
      add: (...cls) => cls.forEach(c => set.add(c)),
      remove: (...cls) => cls.forEach(c => set.delete(c)),
      toggle: (c, force) => {
        if (force === undefined) {
          if (set.has(c)) { set.delete(c); return false; }
          set.add(c); return true;
        }
        if (force) set.add(c); else set.delete(c);
        return Boolean(force);
      },
      contains: (c) => set.has(c)
    };
    this.attributes = new Map();
    this.style = {};
    this.children = [];
    this.textContent = '';
  }

  getAttribute(name) {
    return this.attributes.get(name) || null;
  }

  setAttribute(name, val) {
    this.attributes.set(name, String(val));
  }
}

class MockDocument {
  constructor() {
    this.elements = new Map();
    this.head = new MockElement('head', 'head');
    this.head.appendChild = (el) => this.head.children.push(el);
    this.body = new MockElement('body', 'body');
    this.body.appendChild = (el) => this.body.children.push(el);
    this.addEventListener = () => {};
  }

  createElement(tag) {
    return new MockElement('', tag);
  }

  register(el) {
    if (el.id) this.elements.set(el.id, el);
    return el;
  }

  getElementById(id) {
    return this.elements.get(id) || null;
  }

  querySelectorAll(selector) {
    const results = [];
    if (selector === '.view') {
      for (const el of this.elements.values()) {
        if (el.classList.contains('view')) results.push(el);
      }
    } else if (selector === '.nav-btn') {
      for (const el of this.elements.values()) {
        if (el.classList.contains('nav-btn')) results.push(el);
      }
    } else if (selector === '.nav-sub-btn') {
      for (const el of this.elements.values()) {
        if (el.classList.contains('nav-sub-btn')) results.push(el);
      }
    } else if (selector.includes('.mobile-dock-item') || selector.includes('.mobile-nav-item')) {
      for (const el of this.elements.values()) {
        if (el.classList.contains('mobile-dock-item') || el.classList.contains('mobile-nav-item')) {
          results.push(el);
        }
      }
    } else if (selector.includes('.learn-segmented-control .seg-btn')) {
      for (const el of this.elements.values()) {
        if (el.classList.contains('seg-btn') && el.getAttribute('data-segment-group') === 'learn') {
          results.push(el);
        }
      }
    } else if (selector.includes('.me-segmented-control .seg-btn')) {
      for (const el of this.elements.values()) {
        if (el.classList.contains('seg-btn') && el.getAttribute('data-segment-group') === 'me') {
          results.push(el);
        }
      }
    }
    return results;
  }
}

const mockDoc = new MockDocument();

// Populate DOM with elements
const views = [
  'today', 'home', 'learn', 'kanji', 'vocab', 'grammar',
  'read', 'reading', 'test', 'me', 'hard-words', 'study'
];

views.forEach(v => {
  const el = new MockElement(`view-${v}`, 'section', ['view']);
  mockDoc.register(el);
});

// Register main
const mainEl = new MockElement('main', 'main');
mainEl.scrollTop = 100;
mockDoc.register(mainEl);

// Register dock items
const dockTabs = ['today', 'learn', 'read', 'test', 'me'];
dockTabs.forEach(t => {
  const el = new MockElement(`dock-${t}`, 'button', ['mobile-dock-item', 'mobile-nav-item']);
  el.setAttribute('data-tab', t);
  mockDoc.register(el);
});

// Register desktop sidebar buttons
const navBtns = [
  { view: 'home', tab: 'today' },
  { view: 'learn', tab: 'learn' },
  { view: 'reading', tab: 'read' },
  { view: 'test', tab: 'test' },
  { view: 'me', tab: 'me' }
];
navBtns.forEach(b => {
  const el = new MockElement(`nav-${b.view}`, 'button', ['nav-btn']);
  el.setAttribute('data-view', b.view);
  el.setAttribute('data-tab', b.tab);
  mockDoc.register(el);
});

// Register sidebar subnav buttons
['kanji', 'vocab', 'grammar'].forEach(s => {
  const el = new MockElement(`subnav-${s}`, 'button', ['nav-sub-btn']);
  el.setAttribute('data-view', s);
  mockDoc.register(el);
});

// Register Learn segmented buttons
['kanji', 'vocab', 'grammar'].forEach(s => {
  const el = new MockElement(`seg-learn-${s}`, 'button', ['seg-btn']);
  el.setAttribute('data-segment', s);
  el.setAttribute('data-segment-group', 'learn');
  mockDoc.register(el);
});

// Register Me segmented buttons and panels
['weak', 'stats', 'settings'].forEach(s => {
  const btn = new MockElement(`seg-me-${s}`, 'button', ['seg-btn']);
  btn.setAttribute('data-segment', s);
  btn.setAttribute('data-segment-group', 'me');
  mockDoc.register(btn);

  const panel = new MockElement(`me-panel-${s}`, 'div');
  mockDoc.register(panel);
});

// Set globals for navigation module
globalThis.window = globalThis;
globalThis.document = mockDoc;
globalThis.localStorage = {
  getItem: () => null,
  setItem: () => {},
  removeItem: () => {},
  clear: () => {}
};

// Import navigation module
const {
  VIEW_TO_TAB,
  showView,
  switchLearnSegment,
  switchMeSegment
} = await import('../js/navigation.js');
const { state } = await import('../js/state.js');

// Test VIEW_TO_TAB table mapping
const expectedMappings = {
  today: 'today',
  home: 'today',
  learn: 'learn',
  kanji: 'learn',
  vocab: 'learn',
  grammar: 'learn',
  read: 'read',
  reading: 'read',
  test: 'test',
  me: 'me',
  'hard-words': 'me'
};

for (const [route, expectedTab] of Object.entries(expectedMappings)) {
  assert.equal(
    VIEW_TO_TAB[route],
    expectedTab,
    `VIEW_TO_TAB['${route}'] must map to '${expectedTab}'`
  );
}

console.log('✓ VIEW_TO_TAB mappings validated for all 11 routes');

// ==========================================
// 4. Functional DOM & State Testing
// ==========================================
console.log('\n[4/4] Testing navigation transitions, segments & runner mode...');

// Test 4.1: showView('today') & showView('home')
showView('today');
assert.equal(state.currentView, 'today', 'state.currentView should be today');
assert.ok(mockDoc.getElementById('view-today').classList.contains('active'), 'view-today must be active');
assert.ok(mockDoc.getElementById('view-home').classList.contains('active'), 'view-home must be active');
assert.ok(mockDoc.getElementById('dock-today').classList.contains('active'), 'dock today must be highlighted');
assert.ok(!mockDoc.getElementById('dock-learn').classList.contains('active'), 'dock learn must not be active');

showView('home');
assert.equal(state.currentView, 'home', 'state.currentView should be home');
assert.ok(mockDoc.getElementById('view-today').classList.contains('active'), 'view-today must be active for home route');
assert.ok(mockDoc.getElementById('dock-today').classList.contains('active'), 'dock today must be highlighted for home route');

// Test 4.2: showView('learn') and segment switching
showView('learn');
assert.equal(state.currentView, 'learn', 'state.currentView should be learn');
assert.ok(mockDoc.getElementById('view-learn').classList.contains('active'), 'view-learn must be active');
assert.ok(mockDoc.getElementById('dock-learn').classList.contains('active'), 'dock learn must be active');
assert.ok(!mockDoc.getElementById('dock-today').classList.contains('active'), 'dock today must be deactivated');

// Test direct pillar routes inside Learn
showView('kanji');
assert.equal(state.currentView, 'kanji');
assert.equal(state.ui.learnSegment, 'kanji');
assert.ok(mockDoc.getElementById('view-kanji').classList.contains('active'), 'view-kanji must be active');
assert.ok(!mockDoc.getElementById('view-vocab').classList.contains('active'), 'view-vocab must be inactive');
assert.ok(mockDoc.getElementById('dock-learn').classList.contains('active'), 'dock learn must remain highlighted');

showView('vocab');
assert.equal(state.currentView, 'vocab');
assert.equal(state.ui.learnSegment, 'vocab');
assert.ok(mockDoc.getElementById('view-vocab').classList.contains('active'), 'view-vocab must be active');
assert.ok(!mockDoc.getElementById('view-kanji').classList.contains('active'), 'view-kanji must be inactive');
assert.ok(mockDoc.getElementById('dock-learn').classList.contains('active'), 'dock learn must remain highlighted');

showView('grammar');
assert.equal(state.currentView, 'grammar');
assert.equal(state.ui.learnSegment, 'grammar');
assert.ok(mockDoc.getElementById('view-grammar').classList.contains('active'), 'view-grammar must be active');
assert.ok(!mockDoc.getElementById('view-vocab').classList.contains('active'), 'view-vocab must be inactive');

// Test switchLearnSegment directly
switchLearnSegment('kanji');
assert.equal(state.ui.learnSegment, 'kanji');
assert.ok(mockDoc.getElementById('view-kanji').classList.contains('active'));
assert.ok(mockDoc.getElementById('seg-learn-kanji').classList.contains('active'));
assert.ok(!mockDoc.getElementById('seg-learn-vocab').classList.contains('active'));

// Test 4.3: showView('read') & showView('reading')
showView('read');
assert.equal(state.currentView, 'read');
assert.ok(mockDoc.getElementById('view-reading').classList.contains('active'), 'view-reading must be active');
assert.ok(mockDoc.getElementById('dock-read').classList.contains('active'), 'dock read must be highlighted');

showView('reading');
assert.equal(state.currentView, 'reading');
assert.ok(mockDoc.getElementById('view-reading').classList.contains('active'), 'view-reading must be active');
assert.ok(mockDoc.getElementById('dock-read').classList.contains('active'), 'dock read must be highlighted');

// Test 4.4: showView('test')
showView('test');
assert.equal(state.currentView, 'test');
assert.ok(mockDoc.getElementById('view-test').classList.contains('active'), 'view-test must be active');
assert.ok(mockDoc.getElementById('dock-test').classList.contains('active'), 'dock test must be highlighted');

// Test 4.5: showView('me') & showView('hard-words')
showView('me');
assert.equal(state.currentView, 'me');
assert.ok(mockDoc.getElementById('view-me').classList.contains('active'), 'view-me must be active');
assert.ok(mockDoc.getElementById('dock-me').classList.contains('active'), 'dock me must be highlighted');

showView('hard-words');
assert.equal(state.currentView, 'hard-words');
assert.equal(state.ui.meSegment, 'weak');
assert.ok(mockDoc.getElementById('view-hard-words').classList.contains('active'), 'view-hard-words must be active');
assert.ok(mockDoc.getElementById('dock-me').classList.contains('active'), 'dock me must be highlighted');

// Test switchMeSegment
switchMeSegment('stats');
assert.equal(state.ui.meSegment, 'stats');
assert.equal(mockDoc.getElementById('me-panel-stats').style.display, 'block');
assert.equal(mockDoc.getElementById('me-panel-weak').style.display, 'none');
assert.ok(mockDoc.getElementById('seg-me-stats').classList.contains('active'));

switchMeSegment('settings');
assert.equal(state.ui.meSegment, 'settings');
assert.equal(mockDoc.getElementById('me-panel-settings').style.display, 'block');
assert.equal(mockDoc.getElementById('me-panel-stats').style.display, 'none');
assert.ok(mockDoc.getElementById('seg-me-settings').classList.contains('active'));

// Test 4.6: Runner Mode (study) Dock Hide & Restore
showView('study');
assert.equal(state.currentView, 'study');
assert.ok(mockDoc.body.classList.contains('in-runner'), 'body must have in-runner class when in study');
assert.ok(!mockDoc.getElementById('dock-today').classList.contains('active'));
assert.ok(!mockDoc.getElementById('dock-learn').classList.contains('active'));
assert.ok(!mockDoc.getElementById('dock-read').classList.contains('active'));
assert.ok(!mockDoc.getElementById('dock-test').classList.contains('active'));
assert.ok(!mockDoc.getElementById('dock-me').classList.contains('active'));

// Exiting runner mode restores dock
showView('today');
assert.ok(!mockDoc.body.classList.contains('in-runner'), 'body must remove in-runner class after exiting study');
assert.ok(mockDoc.getElementById('dock-today').classList.contains('active'), 'dock today must be restored');

// Test 4.7: Window controller bindings
assert.equal(typeof window.showView, 'function', 'window.showView must be bound');
assert.equal(typeof window.switchLearnSegment, 'function', 'window.switchLearnSegment must be bound');
assert.equal(typeof window.switchMeSegment, 'function', 'window.switchMeSegment must be bound');
assert.ok(window.VIEW_TO_TAB, 'window.VIEW_TO_TAB must be bound');

console.log('✓ All navigation transitions, segments and runner dock actions verified');
console.log('\n=======================================================');
console.log('WP-7 VERIFICATION PASSED: All tests succeeded!');
console.log('=======================================================');
