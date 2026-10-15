import assert from 'node:assert/strict';
import fs from 'node:fs';
import { vocabularyKanjiMeanings } from '../js/vocab-kanji-breakdown.js';
import { entries, metadata } from '../data/kanji/vocab_character_meanings.js';
let characters=new Set(),words=0;
for (const file of fs.readdirSync('data/vocabulary').filter(f=>f.endsWith('.json'))) {
  const data=JSON.parse(fs.readFileSync(`data/vocabulary/${file}`));
  for(const chapter of data.chapters||[]) for(const section of chapter.sections||[]) for(const word of section.words||[]) {
    const chars=[...new Set([...word.term_ja].filter(c=>/[\u4e00-\u9fff]/.test(c)))];
    if(chars.length) words++;
    assert.equal(vocabularyKanjiMeanings(word.term_ja).length,chars.length,word.term_ja);
    for(const c of chars) { characters.add(c); assert.ok(entries[c]?.every(s=>typeof s==='string'&&s.length)); }
  }
}
assert.deepEqual(vocabularyKanjiMeanings('思いやり')[0].meanings,['think']);
assert.equal(vocabularyKanjiMeanings('いろいろ').length,0);
assert.equal(vocabularyKanjiMeanings('時々').length,1);
assert.equal(vocabularyKanjiMeanings('人人').length,1);
assert.equal(metadata.license,'CC BY-SA 4.0');
console.log(`${characters.size} kanji covered in ${words} kanji-bearing words; source ${metadata.database_date}, kana-only hidden, repeated characters deduplicated.`);
