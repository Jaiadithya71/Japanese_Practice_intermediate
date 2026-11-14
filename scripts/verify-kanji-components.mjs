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

// Grounded samples straight from KRADFILE.
const charsOf = k => components[k].parts.map(([c]) => c);
assert.ok(charsOf('製').includes('衣') && charsOf('製').includes('巾'), '製');
assert.ok(charsOf('語').includes('言') && charsOf('語').includes('五'), '語');
assert.ok(charsOf('勉').includes('力') && charsOf('勉').includes('免'), '勉');
assert.deepEqual(charsOf('人'), [], '人 is a building block');
assert.equal(components['人'].hidden, false);

// Coverage: every chip kanji either has a components entry (possibly empty
// parts for building blocks) or is a documented no-data character.
const missed = Object.keys(entries).filter(k => !components[k] && !uncovered.includes(k));
assert.deepEqual(missed, [], 'chip kanji with neither components nor uncovered entry');

assert.ok(metadata.license.includes('CC BY-SA 4.0'));
console.log(`${Object.keys(components).length} kanji with component data, ${partCount} parts, ${uncovered.length} documented no-data kanji.`);
