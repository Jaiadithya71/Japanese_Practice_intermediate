import assert from 'node:assert/strict';
import fs from 'node:fs';
import { textLookupTokens, lookupEntry, lookupHash, wrapReadingGloss } from '../js/reading-lookup.js';
import data from '../data/reading-lookup.js';

const target = 'この文章で一番言いたいことは何か。';
const tokens = textLookupTokens(target);
assert(tokens.some(t => t.term === '一番'));
const verb = tokens.find(t => t.term === '言いたい');
assert(verb);
assert.deepEqual(lookupEntry(verb.id).slice(0, 4), ['言いたい', '言う', 'いいたい', 'want to']);
assert(lookupEntry(verb.id)[5].includes('to say'));
assert(!tokens.some(t => t.term === '一番言'));
const ichiban = lookupEntry(tokens.find(t => t.term === '一番').id);
assert.equal(ichiban[4], 'いちばん');
assert(ichiban[5].includes('most'));
assert(!textLookupTokens(target, new Set(['言いたい'])).some(t => t.term === '言いたい'));
assert(!textLookupTokens(target, new Set(['言い'])).some(t => t.term === '言いたい'));
assert.deepEqual(textLookupTokens('未収録造語XYZ'), []);

let forms = 0;
for (const [hash, [length, list]] of Object.entries(data.chunks)) {
  let last = 0;
  for (const [start, end, id] of list) {
    assert(start >= last && end > start && end <= length, `invalid range in ${hash}`);
    assert(lookupEntry(id)); last = end; forms++;
  }
}
// Cross-check every Japanese string in all checked-in Reading source files,
// plain and ruby variants, including prompts/options/answers/drills/notes.
let strings = 0, covered = 0, examples = [];
function visit(v) {
  if (typeof v === 'string' && /[一-龯ぁ-んァ-ヶ]/.test(v)) {
    const wrapped = wrapReadingGloss(v, {map:new Map(), protected:new Set()});
    assert.equal(wrapped.replace(/<span class="gloss-term"[^>]*>([\s\S]*?)<\/span>/g, '$1'), v, 'markup/furigana bytes changed');
    assert(!/<rt>[^<]*<span/.test(wrapped), 'furigana must never be a tap target');
    const plain = v.replace(/<(rt|rp|sup)\b[^>]*>.*?<\/\1>/gs, '').replace(/<[^>]*>/g, '');
    // Entities are decoded in the actual browser integration test.
    if (plain.includes('&')) return;
    assert.equal((wrapped.match(/data-gloss-start=""/g) || []).length,
      textLookupTokens(plain).length, 'one hint marker per word, including across ruby boundaries');
    assert.equal(wrapReadingGloss(wrapped, {map:new Map(), protected:new Set()}), wrapped,
      'rewrapping must not add markers or duplicate tap spans');
    strings++;
    for (const chunk of plain.match(/[^。！？!?\n]+[。！？!?]?|[。！？!?]/g) || []) {
      if (!/[一-龯々ぁ-んァ-ヶ]/.test(chunk)) continue;
      assert(data.chunks[lookupHash(chunk)], `missing analysis: ${chunk}`);
      for (const t of textLookupTokens(chunk)) {
        assert.equal(chunk.slice(t.start, t.end), t.term);
        assert(!/[。！？]/.test(t.term));
        covered++;
        if (examples.length < 20 && lookupEntry(t.id)[3] && !examples.some(e => e[0] === t.term)) examples.push(lookupEntry(t.id));
      }
    }
  } else if (Array.isArray(v)) v.forEach(visit);
  else if (v && typeof v === 'object') Object.values(v).forEach(visit);
}
for (const name of fs.readdirSync(new URL('../data/reading/', import.meta.url))) if (name.endsWith('.json')) {
  visit(JSON.parse(fs.readFileSync(new URL('../data/reading/' + name, import.meta.url))));
}
console.log(JSON.stringify({chunks:Object.keys(data.chunks).length, forms:data.entries.length, checkedRanges:forms, sourceStrings:strings, sourceWordOccurrences:covered, examples}, null, 2));
