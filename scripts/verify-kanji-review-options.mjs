import assert from 'node:assert/strict';
import fs from 'node:fs';
import {state} from '../js/state.js';
import {kanjiReviewPlan} from '../js/kanji-review-options.js';
state.stats={};state.kanjiDB={};state.kanjiSelectedLessons=new Set([99]);state.selectedDueKanjiLessons=new Set();
for(let l=1;l<=3;l++) for(let n=0;n<50;n++) {const word=`word-${l}-${n}`;state.kanjiDB[word]={lesson_number:l,words:[{term_ja:word,reading:'test'}]};for(const facet of ['KWW','KWR','K','KWM']) state.stats[`${facet}:${word}`]={nextDue:Date.now()-1000,reps:1,correct:1,interval:1};}
const original=JSON.stringify(state.stats);
for(const direction of ['reading','writing','both']) for(const single of [false,true]) for(const batch of [10,20,40,'all']) for(const lessons of [[],[1],[1,2]]){
state.kanjiDueDirection=direction;state.kanjiDueSingle=single;state.dueBatchSize=batch;state.selectedDueKanjiLessons=new Set(lessons);
const p=kanjiReviewPlan();assert(p.items.length<=40);assert.equal(p.items.length,batch==='all'?40:batch);
assert(p.items.every(i=>i.facet!=='KWM'));if(!single)assert(p.items.every(i=>i.facet!=='K'));
if(direction==='reading')assert(p.items.every(i=>i.facet==='KWR'||i.facet==='K'));
if(direction==='writing')assert(p.items.every(i=>i.facet==='KWW'||i.facet==='K'));
if(lessons.length)assert(p.items.every(i=>lessons.includes(i.lesson_number)));
assert.equal(p.round.writing+p.round.reading+p.round.single,p.items.length);
}
assert.equal(JSON.stringify(state.stats), original);
state.stats={};state.dueBatchSize='all';assert.equal(kanjiReviewPlan().items.length,0);
state.kanjiDB={a:{lesson_number:1,words:[{term_ja:'a'}]}};state.stats={'KWR:a':{nextDue:Date.now()-1000}};state.selectedDueKanjiLessons=new Set();state.kanjiDueDirection='reading';state.kanjiDueSingle=false;assert.equal(kanjiReviewPlan().items.length,1);assert.equal(kanjiReviewPlan().catchUp,false);
state.stats={};for(let n=0;n<50;n++)state.stats[`KWR:a${n}`]={nextDue:Date.now()-1000};assert.equal(kanjiReviewPlan().items.length,50);
const source=fs.readFileSync('js/study.js','utf8').split('export function startDueReview')[1].split('const seenIt')[0];assert(source.includes('kanjiReviewPlan(chapterFilter || state.selectedDueKanjiLessons).items'));assert(!source.includes('kanjiSelectedLessons'));
console.log('72 option combinations: facets, lessons, batches,40 cap, empty/non-catch-up and shared launch plan pass. No records written.');
