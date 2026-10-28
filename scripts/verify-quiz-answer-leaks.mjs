import fs from 'node:fs';import assert from 'node:assert/strict';import{pickDistractors,readingVariants}from '../js/distractors.js';
let words=[];for(const f of fs.readdirSync('data/kanji').filter(f=>/^part\d_lessons/.test(f)))for(const l of JSON.parse(fs.readFileSync('data/kanji/'+f)).lessons)for(const k of l.kanji)for(const w of k.words||[])if(w.term_ja&&w.reading)words.push({...w,lesson:l.lesson_number});
words=[...new Map(words.map(w=>[w.term_ja,w])).values()];const terms=new Set(words.map(w=>w.term_ja));let absent=0,allAbsent=0;
for(const w of words){const a=pickDistractors(w,'writing',words,{pool:words.filter(x=>x.lesson===w.lesson)});assert.equal(a.length,3);assert.equal(new Set(a).size,3);assert(!a.includes(w.term_ja));for(const v of a){const r=words.filter(x=>x.term_ja===v).flatMap(x=>readingVariants(x.reading));assert(!r.some(x=>readingVariants(w.reading).includes(x)));}const n=a.filter(x=>!terms.has(x)).length;absent+=n;if(n===3)allAbsent++;}
for(const [term,expected] of [['結ぶ',['喜ぶ','遊ぶ','転ぶ']],['場面',['方面','正面','表面']],['決める',['温める','冷める','覚める']]]){const w=words.find(x=>x.term_ja===term),a=pickDistractors(w,'writing',words,{pool:words.filter(x=>x.lesson===w.lesson)});assert.deepEqual(a,expected);assert(a.every(x=>terms.has(x)));}
assert(absent<300);assert(allAbsent<70);
const k=fs.readFileSync('js/kanji.js','utf8');assert(k.includes("lessonTag.textContent = item.answered"));assert(k.includes(": 'Quick Quiz';"));
console.log(JSON.stringify({words:words.length,options:words.length*3,absentFromBook:absent,allThreeAbsent:allAbsent}));
