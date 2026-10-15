import re
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Patch index.html
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

if 'css/class-track.css' not in index_content:
    index_content = index_content.replace(
        '<link rel="stylesheet" href="css/me-tab.css" />',
        '<link rel="stylesheet" href="css/me-tab.css" />\n  <link rel="stylesheet" href="css/class-track.css" />'
    )

if 'seg-learn-class' not in index_content:
    old_grammar_btn = '''        <button class="seg-btn" id="seg-learn-grammar" data-segment="grammar" onclick="switchLearnSegment('grammar')" role="tab">
          <i class="fa-solid fa-graduation-cap"></i>
          <span>文法 Grammar</span>
        </button>'''
    new_btns = '''        <button class="seg-btn" id="seg-learn-grammar" data-segment="grammar" onclick="switchLearnSegment('grammar')" role="tab">
          <i class="fa-solid fa-graduation-cap"></i>
          <span>文法 Grammar</span>
        </button>
        <button class="seg-btn" id="seg-learn-class" data-segment="class" onclick="switchLearnSegment('class')" role="tab">
          <i class="fa-solid fa-graduation-cap"></i>
          <span>同期 Class Track</span>
        </button>'''
    # Normalize line endings for replacement
    index_content = index_content.replace(old_grammar_btn.replace('\n', '\r\n'), new_btns.replace('\n', '\r\n'))
    if 'seg-learn-class' not in index_content:
        index_content = index_content.replace(old_grammar_btn, new_btns)

if 'view-class-track' not in index_content:
    old_end = '''    </section>
      </div>
    </div>

    <!-- ==============================================
         TAB 3: READ'''
    new_end = '''    </section>

        <!-- CLASS TRACK: SYNCHRONIZED MULTI-SPEED CLASSROOM HUB -->
        <section id="view-class-track" class="view">
          <div id="class-track-container"></div>
        </section>
      </div>
    </div>

    <!-- ==============================================
         TAB 3: READ'''
    index_content = index_content.replace(old_end.replace('\n', '\r\n'), new_end.replace('\n', '\r\n'))
    if 'view-class-track' not in index_content:
        index_content = index_content.replace(old_end, new_end)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
print("index.html patched.")

# 2. Patch js/main.js
main_path = os.path.join(base_dir, 'js', 'main.js')
with open(main_path, 'r', encoding='utf-8') as f:
    main_content = f.read()

if 'class-curriculum.js' not in main_content:
    main_content = main_content.replace(
        "import './me-tab.js';",
        "import './me-tab.js';\nimport './class-curriculum.js';"
    )
    with open(main_path, 'w', encoding='utf-8') as f:
        f.write(main_content)
    print("main.js patched.")
else:
    print("main.js already contains class-curriculum.js.")

# 3. Patch js/navigation.js
nav_path = os.path.join(base_dir, 'js', 'navigation.js')
with open(nav_path, 'r', encoding='utf-8') as f:
    nav_content = f.read()

if "'class': 'learn'" not in nav_content and "class: 'learn'" not in nav_content:
    nav_content = nav_content.replace(
        "  grammar: 'learn',\n  read: 'read',",
        "  grammar: 'learn',\n  class: 'learn',\n  'class-track': 'learn',\n  read: 'read',"
    ).replace(
        "  grammar: 'learn',\r\n  read: 'read',",
        "  grammar: 'learn',\r\n  class: 'learn',\r\n  'class-track': 'learn',\r\n  read: 'read',"
    )

old_switch = """export function switchLearnSegment(segment) {
  if (!['kanji', 'vocab', 'grammar'].includes(segment)) {
    segment = 'kanji';
  }
  state.ui = state.ui || {};
  state.ui.learnSegment = segment;

  // Toggle segmented control buttons
  document.querySelectorAll('.learn-segmented-control .seg-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-segment') === segment);
  });

  // Toggle learn segment views
  const segments = ['kanji', 'vocab', 'grammar'];
  segments.forEach(s => {
    const el = document.getElementById(`view-${s}`);
    if (el) {
      el.classList.toggle('active', s === segment);
    }
  });

  // Highlight matching sidebar subnav item if present
  document.querySelectorAll('.nav-sub-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-view') === segment);
  });

  // Trigger segment-specific rendering
  if (segment === 'kanji') {
    renderKanjiView();
  } else if (segment === 'vocab') {
    renderChapterChips();
    renderVocabList();
  } else if (segment === 'grammar') {
    renderGrammarView();
  }
}"""

new_switch = """export function switchLearnSegment(segment) {
  if (!['kanji', 'vocab', 'grammar', 'class'].includes(segment)) {
    segment = 'kanji';
  }
  state.ui = state.ui || {};
  state.ui.learnSegment = segment;

  // Toggle segmented control buttons
  document.querySelectorAll('.learn-segmented-control .seg-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-segment') === segment);
  });

  // Toggle learn segment views
  const segments = ['kanji', 'vocab', 'grammar', 'class-track'];
  segments.forEach(s => {
    const el = document.getElementById(s === 'class-track' ? 'view-class-track' : `view-${s}`);
    if (el) {
      el.classList.toggle('active', (s === segment || (s === 'class-track' && segment === 'class')));
    }
  });

  // Highlight matching sidebar subnav item if present
  document.querySelectorAll('.nav-sub-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-view') === segment);
  });

  // Trigger segment-specific rendering
  if (segment === 'kanji') {
    renderKanjiView();
  } else if (segment === 'vocab') {
    renderChapterChips();
    renderVocabList();
  } else if (segment === 'grammar') {
    renderGrammarView();
  } else if (segment === 'class') {
    if (window.N3Class && typeof window.N3Class.render === 'function') {
      window.N3Class.render();
    }
  }
}"""

nav_content = nav_content.replace(old_switch.replace('\n', '\r\n'), new_switch.replace('\n', '\r\n'))
if 'class-track' not in nav_content:
    nav_content = nav_content.replace(old_switch, new_switch)

old_show = "  } else if (viewId === 'kanji' || viewId === 'vocab' || viewId === 'grammar') {\n    const vLearn = document.getElementById('view-learn');\n    if (vLearn) vLearn.classList.add('active');\n    switchLearnSegment(viewId);"
new_show = "  } else if (viewId === 'kanji' || viewId === 'vocab' || viewId === 'grammar' || viewId === 'class' || viewId === 'class-track') {\n    const vLearn = document.getElementById('view-learn');\n    if (vLearn) vLearn.classList.add('active');\n    switchLearnSegment(viewId === 'class-track' ? 'class' : viewId);"

nav_content = nav_content.replace(old_show.replace('\n', '\r\n'), new_show.replace('\n', '\r\n'))
if 'class-track' not in nav_content:
    nav_content = nav_content.replace(old_show, new_show)

with open(nav_path, 'w', encoding='utf-8') as f:
    f.write(nav_content)
print("navigation.js patched.")

# 4. Patch js/today.js
today_path = os.path.join(base_dir, 'js', 'today.js')
with open(today_path, 'r', encoding='utf-8') as f:
    today_content = f.read()

class_card_code = """
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
"""

if 'today-class-card' not in today_content:
    # Insert classCardHtml calculation before container.innerHTML
    today_content = today_content.replace(
        "  // Render Full Dashboard Layout\n  container.innerHTML = `",
        class_card_code + "\n  // Render Full Dashboard Layout\n  container.innerHTML = `"
    ).replace(
        "  // Render Full Dashboard Layout\r\n  container.innerHTML = `",
        class_card_code.replace('\n', '\r\n') + "\r\n  // Render Full Dashboard Layout\r\n  container.innerHTML = `"
    )

    # Insert ${classCardHtml} into container.innerHTML after today-due-card
    today_content = today_content.replace(
        '      <!-- 4. Today\'s Plan Checklist -->',
        '      <!-- 3.5 Class Track Widget -->\n      ${classCardHtml}\n\n      <!-- 4. Today\'s Plan Checklist -->'
    ).replace(
        '      <!-- 4. Today\'s Plan Checklist -->',
        '      <!-- 3.5 Class Track Widget -->\r\n      ${classCardHtml}\r\n\r\n      <!-- 4. Today\'s Plan Checklist -->'
    )

    with open(today_path, 'w', encoding='utf-8') as f:
        f.write(today_content)
    print("today.js patched.")
else:
    print("today.js already contains today-class-card.")
