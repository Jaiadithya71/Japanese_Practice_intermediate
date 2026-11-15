import assert from 'node:assert/strict';
import { state } from '../js/state.js';
import { getVocabDueSummary, getDueItemsCount, getAllDueItems, resolveItemForKey } from '../js/srs.js';
state.vocabDB = { '01': [{id:'one', chapter:'01'}], part2_1:[{id:'two',chapter:'part2_1'}] };
state.stats = {};
for (const id of ['one','two','missing']) for(const tail of ['',':kana',':rev']) state.stats[`V:${id}${tail}`]={nextDue:1,correct:1};
Object.assign(state.stats, {'VC:extra:1':{nextDue:1},'V:future':{nextDue:Date.now()+60000},'K:字':{nextDue:1},'G:grammar':{nextDue:1}});
const before=JSON.stringify(state.stats);
for(const part of ['A','B','both']){
 const options=part==='both'?{}:{part};
 const summary=getVocabDueSummary(options);
 assert.equal(summary.total,getDueItemsCount('vocab',null,options));
 for(const ids of [[],['01'],['part2_1'],['01','part2_1'],['absent']]){
  const filter=new Set(ids);
  const count=filter.size?summary.unassigned+ids.reduce((n,id)=>n+(summary.byChapter.get(id)||0),0):summary.total;
  assert.equal(count,getDueItemsCount('vocab',filter,options));
  assert.equal(count,getAllDueItems('vocab','all',filter,{...options,uncapped:true}).length);
 }
}
assert.equal(JSON.stringify(state.stats),before,'display counts must not mutate study records');
state.stats['V:one'].nextDue=Date.now()+60000;
assert.equal(getVocabDueSummary({part:'A'}).byChapter.has('01'),false,'updates/merged sync stats are read live');
assert.equal(resolveItemForKey('V:one',{}).chapter,'01');
state.vocabDB={'02':[{id:'one',chapter:'02'}]};
assert.equal(resolveItemForKey('V:one',{}).chapter,'02','replaced data rebuilds lookup');
console.log('PASS: all parts/lesson filters match count and launch queue; live stats, replaced data and zero display writes.');
