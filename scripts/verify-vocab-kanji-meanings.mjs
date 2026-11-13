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

// App-wide coverage: every kanji in the app's Japanese text must have
// meanings, except documented Chinese-gloss-only characters (exported as
// `uncovered` by the refresh script).
import { uncovered } from '../data/kanji/vocab_character_meanings.js';
import path from 'node:path';
const KANJI = /[\u4e00-\u9fff]/g, KANA = /[ぁ-んァ-ヶー]/;
const appChars = new Set();
function collect(obj, key = '') {
  if (typeof obj === 'string') {
    if (!(key.endsWith('_zh') || key === 'meaning_zh')) for (const m of obj.matchAll(KANJI)) appChars.add(m[0]);
  } else if (Array.isArray(obj)) obj.forEach(v => collect(v, key));
  else if (obj && typeof obj === 'object') for (const [k, v] of Object.entries(obj)) collect(v, k);
}
function* jsonFiles(dir) {
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) yield* jsonFiles(p);
    else if (name.name.endsWith('.json')) yield p;
  }
}
for (const p of jsonFiles('data')) collect(JSON.parse(fs.readFileSync(p, 'utf8')));
const lookupSrc = fs.readFileSync('data/reading-lookup.js', 'utf8');
for (const m of lookupSrc.matchAll(/\["((?:[^"\\]|\\.)*)","((?:[^"\\]|\\.)*)"/g)) {
  if (KANA.test(m[2])) for (const c of m[1].matchAll(KANJI)) appChars.add(c[0]);
}
for (const p of fs.readdirSync('js').filter(f => f.endsWith('.js')).map(f => `js/${f}`).concat(['index.html'])) {
  for (const c of fs.readFileSync(p, 'utf8').matchAll(KANJI)) appChars.add(c[0]);
}
const uncoveredSet = new Set(uncovered);
const gaps = [...appChars].filter(c => !(entries[c]?.every(s => typeof s === 'string' && s.length)) && !uncoveredSet.has(c));
assert.deepEqual(gaps, [], 'app-text kanji without meanings');
for (const c of appChars) if (!entries[c]) assert.ok(uncoveredSet.has(c), c);
console.log(`${appChars.size} app-text kanji: all covered by meanings or documented Chinese-gloss exclusions (${uncoveredSet.size}).`);
