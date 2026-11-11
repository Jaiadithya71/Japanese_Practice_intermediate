import assert from 'node:assert/strict';
import fs from 'node:fs';
import {state} from '../js/state.js';
import {resolveItemForKey, getAllDueItems, peekItemStatus} from '../js/srs.js';
const read = n => JSON.parse(fs.readFileSync(new URL('../data/grammar/'+n+'.json',import.meta.url)));
state.grammarDB = {index:read('grammar_index'),part1_1_6:read('part1_sec1_to_6'),part1_7_12:read('part1_sec7_to_12'),part2:read('part2_sentence_grammar2'),part3:read('part3_text_grammar')};
state.stats={};
for(const p of state.grammarDB.index){const r=resolveItemForKey('G:'+p.id,{});assert.equal(r.pattern,p.pattern);assert.equal(r.meaning_en,p.meaning_en);assert.equal(peekItemStatus('G:'+p.id),'unseen');}
let count=0;const keys=new Set();
for(const [prefix,dbKey] of [['p1a','part1_1_6'],['p1b','part1_7_12'],['p2','part2'],['p3','part3']])for(const sec of state.grammarDB[dbKey].sections)for(const q of sec.drills||[]){
 const k=`GD:${prefix}:${sec.section_number}:${q.question_id}`;
 assert(!keys.has(k));keys.add(k);
 const r=resolveItemForKey(k,{});assert(r.prompt.startsWith(q.prompt));assert.equal(r.type,'grammar_quiz');assert(r.answerText);assert(r.options===null || r.correctIndex>=1&&r.correctIndex<=r.options.length);
 state.stats[k]={nextDue:1,correct:1};count++;
}
assert.equal(count,495);assert.equal(keys.size,495);
assert.equal(getAllDueItems('grammar','all').length,495,'All must stay uncapped under catch-up');
assert.equal(getAllDueItems('grammar',10).length,10);
assert.equal(Object.keys(state.stats).length,495,'resolving must not create pattern grades');
const filtered = getAllDueItems('grammar','all',new Set(['p1-sec-1']));
assert.equal(filtered.length,9);assert(filtered.every(x=>x.section_id==='p1-sec-1'));
console.log('PASS: 83 pattern resolutions, 495 unique drill resolutions, no false pattern mastery, All uncapped, numeric batch respected');
