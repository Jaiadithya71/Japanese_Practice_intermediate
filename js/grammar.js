/* =======================================================
   NIHONGO INTERMEDIATE — grammar.js
   Book 3: Shin Kanzen Master JLPT N3 Grammar Interactive Workspace
   - 83+ Patterns Explorer & Nuance Comparator
   - Part 1 Drill Runner (Sections 1-12 Practice & Review)
   - Part 2 Sentence Composition / Star Problems (★ Blanks) Runner
   - Part 3 Text Grammar Passages & Context Clozes
   - Official JLPT N3 Mock Exam 1 & 2
   - Book Structure & Conjugation Symbols Guide
   ======================================================= */

import { state } from './state.js';

export function renderGrammarView() {
  const tab = state.grammarActiveTab || 'patterns';

  // Highlight active tab buttons
  document.querySelectorAll('.grammar-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-tab') === tab);
  });

  const patternsPane = document.getElementById('grammar-pane-patterns');
  const drillsPane = document.getElementById('grammar-pane-drills');
  const starPane = document.getElementById('grammar-pane-star');
  const textPane = document.getElementById('grammar-pane-text');
  const mockPane = document.getElementById('grammar-pane-mock');
  const guidePane = document.getElementById('grammar-pane-guide');

  if (patternsPane) patternsPane.style.display = tab === 'patterns' ? 'block' : 'none';
  if (drillsPane) drillsPane.style.display = tab === 'drills' ? 'block' : 'none';
  if (starPane) starPane.style.display = tab === 'star' ? 'block' : 'none';
  if (textPane) textPane.style.display = tab === 'text' ? 'block' : 'none';
  if (mockPane) mockPane.style.display = tab === 'mock' ? 'block' : 'none';
  if (guidePane) guidePane.style.display = tab === 'guide' ? 'block' : 'none';

  if (tab === 'patterns') {
    renderGrammarPatternsList();
  } else if (tab === 'drills') {
    renderGrammarDrills();
  } else if (tab === 'star') {
    renderGrammarStarProblems();
  } else if (tab === 'text') {
    renderGrammarTextPassages();
  } else if (tab === 'mock') {
    renderGrammarMockTests();
  } else if (tab === 'guide') {
    renderGrammarGuide();
  }
}

export function setGrammarTab(tab) {
  state.grammarActiveTab = tab;
  renderGrammarView();
}

// -------------------------------------------------------
// 1. GRAMMAR PATTERNS BROWSER
// -------------------------------------------------------
export function renderGrammarPatternsList() {
  const container = document.getElementById('grammar-patterns-grid');
  if (!container) return;

  const patterns = state.grammarDB.index || [];
  const partFilter = state.grammarFilterPart || 'all';
  const query = (state.grammarSearchQuery || '').toLowerCase().trim();

  const filtered = patterns.filter(p => {
    if (partFilter !== 'all' && !p.category.includes(partFilter)) return false;
    if (query) {
      const matchPat = (p.pattern || '').toLowerCase().includes(query);
      const matchEn = (p.meaning_en || '').toLowerCase().includes(query);
      const matchJa = (p.meaning_ja || '').toLowerCase().includes(query);
      const matchSec = (p.section_title || '').toLowerCase().includes(query);
      return matchPat || matchEn || matchJa || matchSec;
    }
    return true;
  });

  const countBadge = document.getElementById('grammar-count-badge');
  if (countBadge) {
    countBadge.textContent = `${filtered.length} / ${patterns.length} Patterns`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 3rem; text-align: center; color: var(--text-dim); background: var(--bg-card); border-radius: var(--radius); border: 1px solid var(--border);">
        <i class="fa-solid fa-magnifying-glass" style="font-size: 2rem; margin-bottom: 1rem; opacity: 0.5;"></i>
        <p>No grammar patterns match your filter.</p>
      </div>`;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <div class="grammar-card" style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; display: flex; flex-direction: column; gap: 0.75rem; transition: transform 0.15s, border-color 0.15s;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem;">
        <span class="badge badge-accent" style="font-size: 0.75rem;">${item.id}</span>
        <span class="badge badge-purple" style="font-size: 0.75rem;">${item.category}</span>
      </div>

      <div>
        <h4 style="font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 0.25rem;">
          ${item.pattern_ruby || item.pattern}
        </h4>
        <div style="font-size: 0.85rem; color: var(--text-muted);">${item.section_title || ''}</div>
      </div>

      <div style="background: var(--bg-surface); padding: 0.65rem 0.85rem; border-radius: 6px; font-size: 0.88rem; border-left: 3px solid var(--accent);">
        <div style="font-weight: 600; color: var(--text); margin-bottom: 0.2rem;">Meaning:</div>
        <div style="color: var(--text); line-height: 1.4;">${item.meaning_en}</div>
        ${item.meaning_ja ? `<div style="color: var(--text-dim); font-size: 0.8rem; margin-top: 0.25rem;">${item.meaning_ja}</div>` : ''}
      </div>

      ${item.connection ? `
        <div style="font-size: 0.82rem; color: var(--text-dim); background: rgba(255,255,255,0.03); padding: 0.5rem 0.75rem; border-radius: 6px;">
          <strong style="color: var(--accent);">接続:</strong> ${item.connection}
        </div>` : ''}
    </div>
  `).join('');
}

export function setGrammarPartFilter(part) {
  state.grammarFilterPart = part;
  renderGrammarPatternsList();
}

export function onGrammarSearch(query) {
  state.grammarSearchQuery = query;
  renderGrammarPatternsList();
}

// -------------------------------------------------------
// 2. PART 1 DRILLS RUNNER
// -------------------------------------------------------
export function renderGrammarDrills() {
  const container = document.getElementById('grammar-drills-container');
  if (!container) return;

  const sec1to6 = state.grammarDB.part1_1_6?.sections || [];
  const sec7to12 = state.grammarDB.part1_7_12?.sections || [];
  const allSections = [...sec1to6, ...sec7to12];

  if (allSections.length === 0) {
    container.innerHTML = `<div style="padding: 2rem; text-align: center; color: var(--text-muted);">No drill sections loaded.</div>`;
    return;
  }

  const activeSecId = state.grammarCurrentSection === 'all' 
    ? allSections[0].id 
    : state.grammarCurrentSection;
  
  const currentSec = allSections.find(s => s.id === activeSecId) || allSections[0];
  const drills = currentSec.drills || [];

  container.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 1.5rem;">
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
        ${allSections.map(s => `
          <button class="btn btn-sm ${s.id === currentSec.id ? 'btn-accent' : 'btn-ghost'}"
                  onclick="selectGrammarSection('${s.id}')">
            ${s.title} (${(s.drills || []).length} Qs)
          </button>
        `).join('')}
      </div>

      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem;">
        <h3 style="font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">${currentSec.title} 練習問題</h3>
        <p style="color: var(--text-dim); font-size: 0.85rem; margin-bottom: 1.25rem;">Select the most appropriate option to complete each sentence.</p>

        <div style="display: flex; flex-direction: column; gap: 1.25rem;">
          ${drills.map((drill, idx) => {
            const userChoice = state.grammarSelectedAnswers[drill.id];
            const isCorrect = userChoice === drill.correct_answer;
            return `
              <div class="drill-item" style="background: var(--bg-surface); border: 1px solid var(--border); border-radius: 8px; padding: 1rem;">
                <div style="font-size: 0.95rem; font-weight: 600; color: #fff; margin-bottom: 0.75rem;">
                  <span style="color: var(--accent); margin-right: 0.5rem;">Q${idx + 1}.</span> ${drill.prompt}
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.5rem; margin-bottom: 0.75rem;">
                  ${(drill.options || []).map((opt, oIdx) => {
                    const optNum = oIdx + 1;
                    const isSelected = userChoice === optNum;
                    const showKey = userChoice !== undefined;
                    let bg = 'background: rgba(255,255,255,0.03);';
                    let border = 'border: 1px solid var(--border);';
                    if (showKey) {
                      if (optNum === drill.correct_answer) {
                        bg = 'background: rgba(34, 197, 94, 0.15);';
                        border = 'border: 1px solid #22c55e;';
                      } else if (isSelected) {
                        bg = 'background: rgba(239, 68, 68, 0.15);';
                        border = 'border: 1px solid #ef4444;';
                      }
                    }
                    return `
                      <button onclick="answerGrammarDrill('${drill.id}', ${optNum})"
                              style="${bg} ${border} text-align: left; padding: 0.6rem 0.85rem; border-radius: 6px; color: var(--text); cursor: pointer;">
                        <span style="font-weight: 700; margin-right: 0.4rem;">(${optNum})</span> ${opt}
                      </button>
                    `;
                  }).join('')}
                </div>

                ${userChoice !== undefined ? `
                  <div style="font-size: 0.85rem; padding: 0.65rem 0.85rem; border-radius: 6px; background: rgba(255,255,255,0.02); border-left: 3px solid ${isCorrect ? '#22c55e' : '#ef4444'};">
                    <span style="font-weight: 600; color: ${isCorrect ? '#22c55e' : '#ef4444'};">
                      ${isCorrect ? '✓ 正解 (Correct!)' : `✗ 不正解 (Correct answer is (${drill.correct_answer}))`}
                    </span>
                    <div style="color: var(--text-dim); margin-top: 0.25rem;">${drill.explanation_en || drill.explanation_ja || ''}</div>
                  </div>` : ''}
              </div>
            `;
          }).join('')}
        </div>
      </div>
    </div>
  `;
}

export function selectGrammarSection(secId) {
  state.grammarCurrentSection = secId;
  renderGrammarDrills();
}

export function answerGrammarDrill(drillId, choice) {
  state.grammarSelectedAnswers[drillId] = choice;
  renderGrammarDrills();
}

// -------------------------------------------------------
// 3. PART 2 STAR PROBLEMS (★ Blanks) RUNNER
// -------------------------------------------------------
export function renderGrammarStarProblems() {
  const container = document.getElementById('grammar-star-container');
  if (!container) return;

  const sections = state.grammarDB.part2?.sections || [];
  if (sections.length === 0) {
    container.innerHTML = `<div style="padding: 2rem; text-align: center; color: var(--text-muted);">No Part 2 sentence composition exercises loaded.</div>`;
    return;
  }

  container.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 1.5rem;">
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem;">
        <h3 style="font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">第2部 文の組み立て (★に入るものはどれか)</h3>
        <p style="color: var(--text-dim); font-size: 0.85rem; margin-bottom: 1.25rem;">Scrambled sentence composition: choose the item that correctly fills the star position (★).</p>

        <div style="display: flex; flex-direction: column; gap: 1.25rem;">
          ${sections.flatMap(s => (s.drills || [])).slice(0, 30).map((drill, idx) => {
            const userChoice = state.grammarSelectedAnswers[drill.id];
            const isCorrect = userChoice === drill.correct_answer;
            return `
              <div style="background: var(--bg-surface); border: 1px solid var(--border); border-radius: 8px; padding: 1rem;">
                <div style="font-size: 1rem; font-weight: 600; color: #fff; margin-bottom: 0.75rem;">
                  <span style="color: var(--accent); margin-right: 0.5rem;">★${idx + 1}.</span> ${drill.prompt}
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.5rem; margin-bottom: 0.75rem;">
                  ${(drill.options || []).map((opt, oIdx) => {
                    const optNum = oIdx + 1;
                    const isSelected = userChoice === optNum;
                    const showKey = userChoice !== undefined;
                    let bg = 'background: rgba(255,255,255,0.03);';
                    let border = 'border: 1px solid var(--border);';
                    if (showKey) {
                      if (optNum === drill.correct_answer) {
                        bg = 'background: rgba(34, 197, 94, 0.15);';
                        border = 'border: 1px solid #22c55e;';
                      } else if (isSelected) {
                        bg = 'background: rgba(239, 68, 68, 0.15);';
                        border = 'border: 1px solid #ef4444;';
                      }
                    }
                    return `
                      <button onclick="answerGrammarStar('${drill.id}', ${optNum})"
                              style="${bg} ${border} text-align: left; padding: 0.6rem 0.85rem; border-radius: 6px; color: var(--text); cursor: pointer;">
                        <span style="font-weight: 700; margin-right: 0.4rem;">(${optNum})</span> ${opt}
                      </button>
                    `;
                  }).join('')}
                </div>

                ${userChoice !== undefined ? `
                  <div style="font-size: 0.85rem; padding: 0.65rem 0.85rem; border-radius: 6px; background: rgba(255,255,255,0.02); border-left: 3px solid ${isCorrect ? '#22c55e' : '#ef4444'};">
                    <span style="font-weight: 600; color: ${isCorrect ? '#22c55e' : '#ef4444'};">
                      ${isCorrect ? '✓ 正解 (Correct!)' : `✗ 不正解 (Star position is (${drill.correct_answer}))`}
                    </span>
                    ${drill.full_sentence ? `<div style="color: #fff; margin-top: 0.4rem; font-weight: 500;">Complete Sentence: ${drill.full_sentence}</div>` : ''}
                    <div style="color: var(--text-dim); margin-top: 0.25rem;">${drill.explanation_en || drill.explanation_ja || ''}</div>
                  </div>` : ''}
              </div>
            `;
          }).join('')}
        </div>
      </div>
    </div>
  `;
}

export function answerGrammarStar(drillId, choice) {
  state.grammarSelectedAnswers[drillId] = choice;
  renderGrammarStarProblems();
}

// -------------------------------------------------------
// 4. PART 3 TEXT GRAMMAR PASSAGES
// -------------------------------------------------------
export function renderGrammarTextPassages() {
  const container = document.getElementById('grammar-text-container');
  if (!container) return;

  const sections = state.grammarDB.part3?.sections || [];
  if (sections.length === 0) {
    container.innerHTML = `<div style="padding: 2rem; text-align: center; color: var(--text-muted);">No Part 3 text passages loaded.</div>`;
    return;
  }

  container.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 1.5rem;">
      ${sections.map((sec, sIdx) => `
        <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem;">
          <h3 style="font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">
            ${sec.title || `第${sIdx + 1}課 文章の文法`}
          </h3>
          <p style="color: var(--text-dim); font-size: 0.85rem; margin-bottom: 1rem;">${sec.theme_en || ''}</p>

          ${(sec.points || []).map(pt => `
            <div style="background: var(--bg-surface); padding: 0.85rem 1rem; border-radius: 6px; margin-bottom: 0.75rem;">
              <h5 style="color: var(--accent); font-size: 0.95rem; margin-bottom: 0.35rem;">${pt.title}</h5>
              <div style="font-size: 0.85rem; color: var(--text-dim);">${pt.title_en || ''}</div>
            </div>
          `).join('')}

          ${(sec.drills || []).map(d => `
            <div style="border-top: 1px solid var(--border); padding-top: 0.75rem; margin-top: 0.75rem;">
              <div style="font-weight: 600; color: #fff; margin-bottom: 0.5rem;">${d.prompt}</div>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.5rem;">
                ${(d.options || []).map((o, idx) => `
                  <div style="background: rgba(255,255,255,0.03); padding: 0.5rem 0.75rem; border-radius: 6px; font-size: 0.85rem;">
                    (${idx + 1}) ${o}
                  </div>
                `).join('')}
              </div>
            </div>
          `).join('')}
        </div>
      `).join('')}
    </div>
  `;
}

// -------------------------------------------------------
// 5. MOCK TESTS RUNNER
// -------------------------------------------------------
export function renderGrammarMockTests() {
  const container = document.getElementById('grammar-mock-container');
  if (!container) return;

  const mockData = state.grammarDB.mock;
  const tests = mockData?.mock_tests || [];

  if (tests.length === 0) {
    container.innerHTML = `<div style="padding: 2rem; text-align: center; color: var(--text-muted);">No mock tests loaded.</div>`;
    return;
  }

  container.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 1.5rem;">
      ${tests.map((test, tIdx) => `
        <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h3 style="font-size: 1.25rem; color: #fff;">${test.title} (${test.total_questions} Questions)</h3>
            <span class="badge badge-accent">JLPT N3 Grammar Exam</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 1rem;">
            ${(test.questions || []).map((q, qIdx) => `
              <div style="background: var(--bg-surface); padding: 0.85rem 1rem; border-radius: 6px; border: 1px solid var(--border);">
                <div style="font-weight: 600; color: #fff; margin-bottom: 0.5rem;">
                  Q${qIdx + 1}. ${q.prompt}
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.5rem;">
                  ${(q.options || []).map((opt, oIdx) => `
                    <div style="background: rgba(255,255,255,0.03); padding: 0.5rem 0.75rem; border-radius: 6px; font-size: 0.85rem;">
                      (${oIdx + 1}) ${opt}
                    </div>
                  `).join('')}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      `).join('')}
    </div>
  `;
}

// -------------------------------------------------------
// 6. BOOK GUIDE & CONNECTION SYMBOLS
// -------------------------------------------------------
export function renderGrammarGuide() {
  const container = document.getElementById('grammar-guide-container');
  if (!container) return;

  const guide = state.grammarDB.intro || {};
  const symbols = guide.connection_symbols || [];

  container.innerHTML = `
    <div style="display: flex; flex-direction: column; gap: 1.5rem;">
      <div style="background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem;">
        <h3 style="font-size: 1.25rem; color: #fff; margin-bottom: 0.5rem;">新完全マスター文法 N3: 本書の構成と使い方</h3>
        <p style="color: var(--text-dim); font-size: 0.9rem; line-height: 1.5; margin-bottom: 1.25rem;">
          ${guide.book_structure?.structure_overview_en || ''}
        </p>

        <h4 style="font-size: 1.05rem; color: var(--accent); margin-bottom: 0.75rem;">接続の表記について (Connection Notation & Symbols)</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0.75rem;">
          ${symbols.map(s => `
            <div style="background: var(--bg-surface); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border);">
              <div style="font-weight: 700; color: #fff; font-size: 0.95rem;">${s.symbol}</div>
              <div style="color: var(--text); font-size: 0.85rem; margin-top: 0.2rem;">${s.meaning_ja}</div>
              <div style="color: var(--text-dim); font-size: 0.8rem; margin-top: 0.15rem;">${s.meaning_en}</div>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
  `;
}

// Window bindings for inline onclicks
window.setGrammarTab = setGrammarTab;
window.setGrammarPartFilter = setGrammarPartFilter;
window.onGrammarSearch = onGrammarSearch;
window.selectGrammarSection = selectGrammarSection;
window.answerGrammarDrill = answerGrammarDrill;
window.answerGrammarStar = answerGrammarStar;
