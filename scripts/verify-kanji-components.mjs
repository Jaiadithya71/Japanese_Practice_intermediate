import assert from 'node:assert/strict';
import { components, uncovered, metadata } from '../data/kanji/kanji_components.js';
import { entries } from '../data/kanji/vocab_character_meanings.js';

// Well-formed: every part is [single char, meaning string or null].
let partCount = 0;
for (const [kanji, entry] of Object.entries(components)) {
  assert.equal([...kanji].length, 1, kanji);
  assert.ok(Array.isArray(entry.parts), kanji);
  for (const part of entry.parts) {
    const [char, meaning] = part;
    assert.equal([...char].length, 1, `${kanji}: ${char}`);
    assert.notEqual(char, kanji, `${kanji}: self-reference`);
    assert.ok(meaning === null || (typeof meaning === 'string' && meaning.length), `${kanji}: ${char}`);
    partCount++;
  }
  assert.equal(typeof entry.hidden, 'boolean', kanji);
}

// Grounded samples straight from the KanjiVG component hierarchy.
const charsOf = k => components[k].parts.map(([c]) => c);
assert.deepEqual(charsOf('製'), ['制', '衣'], '製 = 制 + 衣');
assert.deepEqual(charsOf('知'), ['矢', '口'], '知 = 矢 + 口');
assert.deepEqual(charsOf('婦'), ['女', '帚'], '婦 = 女 + 帚');
assert.deepEqual(charsOf('造'), ['告', '⻌'], '造 = 告 + ⻌');
assert.deepEqual(charsOf('合'), ['人', '一', '口'], '合 = 人 + 一 + 口');
assert.deepEqual(charsOf('語'), ['言', '吾'], '語 = 言 + 吾');
assert.deepEqual(charsOf('人'), [], '人 is a building block');
assert.equal(components['人'].hidden, false);

// Meanings are KANJIDIC2 glosses (a variant element may take its original's).
assert.ok(components['製'].parts[0][1].includes('system'), '制 gloss');
assert.ok(components['衣'] && components['製'].parts[1][1].includes('garment'), '衣 gloss');
assert.ok(components['造'].parts[1][1].includes('walk'), '⻌ takes 辶 gloss');

// Coverage: every chip kanji either has a components entry (possibly empty
// parts for building blocks) or is a documented no-data character.
const missed = Object.keys(entries).filter(k => !components[k] && !uncovered.includes(k));
assert.deepEqual(missed, [], 'chip kanji with neither components nor uncovered entry');

assert.ok(metadata.license.includes('CC BY-SA 3.0'), 'KanjiVG licence');
assert.ok(metadata.source_url.includes('kanjivg'), 'KanjiVG attribution');
console.log(`${Object.keys(components).length} kanji with component data, ${partCount} parts, ${uncovered.length} documented no-data kanji.`);
