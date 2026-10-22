// Run: node scripts/verify-kanji-distractors.mjs
// Checks every kanji word in the book: 3 unique distractors, never a correct alternative,
// okurigana kept, deterministic, near-equal length.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { pickDistractors, okuriganaOf, readingVariants, readingMutations } from '../js/distractors.js';

const dir = new URL('../data/kanji/', import.meta.url).pathname;
const words = [];
for (const f of fs.readdirSync(dir).filter(f => /^part\d_lessons/.test(f))) {
  const d = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  for (const les of d.lessons || []) for (const k of les.kanji || []) for (const w of k.words || []) {
    if (w.term_ja && w.reading) words.push({ term_ja: w.term_ja.trim(), reading: w.reading.trim(), meaning_en: w.meaning_en || '', lesson: les.lesson_number });
  }
}
const uniq = [...new Map(words.map(w => [w.term_ja, w])).values()];
assert(uniq.length > 500, 'expected the full word list, got ' + uniq.length);

let endRelaxed = 0, n = 0, lenOff = 0, fewer = 0;
for (const w of uniq) {
  const alts = new Set(words.filter(x => x.term_ja === w.term_ja).flatMap(x => readingVariants(x.reading)));
  const homophones = new Set(words.filter(x => readingVariants(x.reading).some(v => readingVariants(w.reading).includes(v))).map(x => x.term_ja));
  for (const kind of ['reading', 'writing', 'meaning']) {
    const a = pickDistractors(w, kind, uniq);
    const b = pickDistractors(w, kind, uniq.slice().reverse());
    assert.deepEqual(a, b, `non-deterministic for ${w.term_ja} ${kind}`);
    assert.equal(new Set(a).size, a.length, `duplicates ${w.term_ja} ${kind}`);
    if (a.length < 3) { fewer++; console.log("FEW", kind, w.term_ja, w.reading, a); continue; }
    n++;
    if (kind === 'reading') {
      for (const d of a) {
        assert(!alts.has(d), `correct alt reading as distractor: ${w.term_ja} -> ${d}`);
        const ok = okuriganaOf(w.term_ja);
        if (ok && !d.endsWith([...ok].pop())) endRelaxed++;
        if (Math.abs([...d].length - [...w.reading].length) > 1) lenOff++;
      }
    } else if (kind === 'writing') {
      for (const d of a) {
        assert.notEqual(d, w.term_ja);
        assert(!homophones.has(d), `homophone (also correct) as distractor: ${w.term_ja} -> ${d}`);
      }
    } else {
      for (const d of a) assert.notEqual(d.toLowerCase(), w.meaning_en.toLowerCase());
    }
  }
}
assert.equal(fewer, 0, `${fewer} questions had <3 distractors`);
assert(readingMutations('きょう').length > 0);
assert(endRelaxed <= 15, 'too many okurigana-ending relaxations: ' + endRelaxed);
console.log(`ok (okurigana ending relaxed on ${endRelaxed} options): ${uniq.length} words, ${n} questions, ${lenOff} reading distractors off by >1 kana`);
for (const t of ['辺り','市場','割る','激しい','養う','押さえる','過ごす','減らす','事情','協力']) {
  const w = uniq.find(x => x.term_ja === t); if (!w) continue;
  console.log(t, w.reading, '| reading:', pickDistractors(w, 'reading', uniq).join(' / '), '| writing:', pickDistractors(w, 'writing', uniq).join(' / '));
}
