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
// Kanji book: every target kanji and compound character must have meanings.
let kanjiBookChars=new Set();
for (const file of fs.readdirSync('data/kanji').filter(f=>/^part\d+_lessons_.*\.json$/.test(f))) {
  const data=JSON.parse(fs.readFileSync(`data/kanji/${file}`));
  for(const lesson of data.lessons||[]) for(const k of lesson.kanji||[]) {
    if(/^[\u4e00-\u9fff]$/.test(k.kanji||'')) kanjiBookChars.add(k.kanji);
    for(const w of k.words||[]) for(const c of w.term_ja||'') if(/[\u4e00-\u9fff]/.test(c)) kanjiBookChars.add(c);
  }
}
for(const c of kanjiBookChars) assert.ok(entries[c]?.every(s=>typeof s==='string'&&s.length),c);
console.log(`${kanjiBookChars.size} kanji-book characters covered.`);
console.log(`${characters.size} kanji covered in ${words} kanji-bearing words; source ${metadata.database_date}, kana-only hidden, repeated characters deduplicated.`);
// Exercise the actual renderer, including its DOM branch and safe text handling.
const {renderVocabularyKanjiBreakdown}=await import('../js/vocab-kanji-breakdown.js');
class Element {
  constructor(tag) {this.tag=tag;this.children=[];}
  append(...children) {this.children.push(...children);}
  setAttribute() {}
  addEventListener() {}
  before(row) {this.inserted=row;}
}
const example=new Element('example');
globalThis.document={getElementById:id=>id==='card-example-box'?example:null,createElement:tag=>new Element(tag),createTextNode:text=>({text})};
renderVocabularyKanjiBreakdown({type:'vocab',term_ja:'夫婦'},true);
assert.equal(example.inserted.children[1].children.length,2);
assert.equal(example.inserted.children[1].children[0].children[0].textContent,'夫');
example.inserted=null;
renderVocabularyKanjiBreakdown({type:'vocab',term_ja:'夫婦'},false);
assert.equal(example.inserted,null);
renderVocabularyKanjiBreakdown({type:'vocab',term_ja:'いとこ'},true);
assert.equal(example.inserted,null);
console.log('Actual renderer: revealed chips, front hidden, kana-only hidden passed.');
