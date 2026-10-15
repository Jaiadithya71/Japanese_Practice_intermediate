import assert from 'node:assert/strict';
import fs from 'node:fs';
const source=fs.readFileSync('js/study.js','utf8');
const recall=source.slice(source.indexOf("  if (!state.cardFlipped) {",source.indexOf('// CASE B: VOCABULARY TERM')));
assert.match(recall,/termEl\.textContent = item\.term_ja \|\| item\.reading \|\| '';/);
assert.doesNotMatch(recall.split('} else {')[0],/ruby_html|showFurigana/);
assert.match(recall,/termEl\.innerHTML = item\.ruby_html \|\| item\.term_ja;/);
let kanji=0,kana=0;
for(const file of fs.readdirSync('data/vocabulary').filter(f=>f.endsWith('.json'))){
 const data=JSON.parse(fs.readFileSync(`data/vocabulary/${file}`));
 for(const chapter of data.chapters||[])for(const section of chapter.sections||[])for(const word of section.words||[]){
  assert.ok(word.term_ja || word.reading,`${file}: no written word`);
  assert.doesNotMatch(word.term_ja||'',/<ruby|<rt/);
  if(/[一-龯々]/.test(word.term_ja||''))kanji++;else kana++;
 }
}
console.log(`Recall-front check passed: ${kanji} kanji-form words, ${kana} kana-only words. Back still uses ruby readings.`);
