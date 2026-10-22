import fs from 'node:fs';
import assert from 'node:assert/strict';
import {pickDistractors,shapeSimilarity} from '../js/distractors.js';
import {characterShapes} from '../data/kanji/character_shapes.js';
const words=[];
for(const f of fs.readdirSync('data/kanji').filter(f=>/^part\d_lessons/.test(f))){
 const d=JSON.parse(fs.readFileSync('data/kanji/'+f));
 for(const l of d.lessons)for(const k of l.kanji)for(const w of k.words||[])if(w.term_ja&&w.reading)words.push({...w,lesson:l.lesson_number});
}
let tested=0;
for(const t of words.filter(w=>[...w.term_ja].length===1)){
 const a=pickDistractors(t,'writing',words);
 assert.equal(a.length,3);
 assert(a.every(c=>[...c].length===1&&shapeSimilarity(t.term_ja,c)>0),t.term_ja+' '+a);
 const strong=Object.keys(characterShapes).filter(c=>shapeSimilarity(t.term_ja,c)>=12);
 if(strong.length>=6) assert(a.every(c=>shapeSimilarity(t.term_ja,c)>=12),'ignored available component/radical candidates: '+t.term_ja+' '+a);
 assert.deepEqual(a,pickDistractors(t,'writing',words.slice().reverse()));tested++;
}
assert.deepEqual(pickDistractors({term_ja:'組',reading:'くみ'},'writing',words),['紹','紺','細']);
const quiz=fs.readFileSync('js/kanji.js','utf8').split('function buildKanjiQuizOptions')[1].split('// Elementary-style test')[0];
assert(!quiz.includes('pickFrom')&&!quiz.includes('catch'));
const guided=fs.readFileSync('js/kanji-words.js','utf8');
assert(!guided.includes('generateDistractorsLegacy'));
console.log(`${tested} single-kanji questions: ranked shape candidates, full-book coverage, deterministic order; no random Quick Quiz/guided fallback.`);
