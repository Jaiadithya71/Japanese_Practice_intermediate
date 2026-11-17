import fs from 'node:fs';
import assert from 'node:assert/strict';

// 1. Overlap data sanity: every entry has id/term/reading/meaning; no id
//    collides with a different word inside the same chapter's base list.
const overlaps = JSON.parse(fs.readFileSync('data/vocab_lesson_overlaps.json', 'utf8')).overlaps;
const vocabFiles = fs.readdirSync('data/vocabulary').filter(f => f.endsWith('.json'));
const chapterIds = new Set();
const wordById = new Map();
for (const f of vocabFiles) {
  const d = JSON.parse(fs.readFileSync('data/vocabulary/' + f, 'utf8'));
  for (const ch of (d.chapters || [])) {
    const cid = String(ch.metadata.chapter);
    chapterIds.add(cid);
    for (const s of (ch.sections || [])) for (const w of (s.words || [])) {
      if (w.id) wordById.set(`${cid}:${w.id}`, w);
    }
  }
}
let total = 0;
for (const [cid, words] of Object.entries(overlaps)) {
  assert.ok(chapterIds.has(cid), `overlap chapter ${cid} exists`);
  const baseIds = new Set();
  for (const f of vocabFiles) {
    const d = JSON.parse(fs.readFileSync('data/vocabulary/' + f, 'utf8'));
    for (const ch of (d.chapters || [])) {
      if (String(ch.metadata.chapter) !== cid) continue;
      for (const s of (ch.sections || [])) for (const w of (s.words || [])) baseIds.add(w.id);
    }
  }
  for (const w of words) {
    total++;
    assert.ok(w.id && w.term_ja && w.reading && w.meaning_en, `complete word ${w.id} in ${cid}`);
    assert.ok(!baseIds.has(w.id), `overlap ${w.id} not duplicating base chapter ${cid}`);
  }
}
assert.ok(total > 300, `expected 300+ overlap words, got ${total}`);

// 2. home.js wiring: checkbox handler exported, pool uses homeChapterWords, dedupe present.
const home = fs.readFileSync('js/home.js', 'utf8');
assert.match(home, /function homeIncludeOverlapsChecked\(\)/);
assert.match(home, /window\.toggleHomeIncludeOverlaps = toggleHomeIncludeOverlaps/);
assert.match(home, /for \(const word of homeChapterWords\(chapter\)\)/);
assert.match(home, /seenKeys\.has\(key\)/);
assert.match(home, /n3_home_include_overlaps/);

// 3. index.html checkbox next to Drill hard words only.
const html = fs.readFileSync('index.html', 'utf8');
assert.match(html, /id="home-include-overlaps"[^>]*onchange="window\.toggleHomeIncludeOverlaps\(\)"/);
assert.ok(html.indexOf('home-hard-only') < html.indexOf('home-include-overlaps'), 'sits next to drill-hard');

// 4. data-loader fetches the overlaps file.
const loader = fs.readFileSync('js/data-loader.js', 'utf8');
assert.match(loader, /vocab_lesson_overlaps\.json/);
assert.match(loader, /state\.vocabLessonOverlaps/);

// 5. Build markers bumped together (docs/DEPLOY.md).
assert.match(html, /js\/main\.js\?v=4\.21-ovl1/);
const main = fs.readFileSync('js/main.js', 'utf8');
const nav = fs.readFileSync('js/navigation.js', 'utf8');
const m1 = main.match(/home\.js\?v=([a-z0-9-]+)/gi), m2 = nav.match(/home\.js\?v=([a-z0-9-]+)/gi);
assert.deepEqual([...new Set([...m1, ...m2])], ["home.js?v=20261117-ovl1"], "home.js tag identical in every importer");

console.log(`Lesson overlaps verified: ${total} words across ${Object.keys(overlaps).length} lessons, wiring + markers OK.`);
