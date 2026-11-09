// Regression test: every vocab card sentence must ship with an English line.
// Checks source files, the aggregated vocabulary.json and derived word contexts.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = (p) => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const problems = [];
let checked = 0;

function walk(o, file) {
  if (Array.isArray(o)) return o.forEach((v) => walk(v, file));
  if (o && typeof o === 'object') {
    if (typeof o.example_ja === 'string' && o.example_ja.trim()) {
      checked++;
      if (!(o.example_en || '').trim()) problems.push(`${file}: ${o.id || o.term_ja} has example_ja but no example_en`);
    }
    Object.values(o).forEach((v) => walk(v, file));
  }
}

const vocabDir = 'data/vocabulary';
for (const f of fs.readdirSync(path.join(root, vocabDir)).filter((n) => n.startsWith('part') && n.endsWith('.json'))) {
  walk(read(`${vocabDir}/${f}`), `${vocabDir}/${f}`);
}
walk(read('data/vocabulary.json'), 'data/vocabulary.json');

for (const f of ['data/word_contexts.json', 'data/kanji/word_contexts.json']) {
  for (const [term, list] of Object.entries(read(f))) {
    for (const c of list) {
      checked++;
      if (!(c.en || c.meaning || '').trim()) problems.push(`${f}: context for ${term} (${c.src}) has no English`);
    }
  }
}

if (problems.length) {
  console.error(problems.slice(0, 30).join('\n'));
  console.error(`FAIL: ${problems.length} problem(s) in ${checked} checked sentences`);
  process.exit(1);
}
console.log(`PASS: ${checked} sentences checked, all have English`);
