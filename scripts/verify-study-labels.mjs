import assert from 'node:assert/strict';
import fs from 'node:fs';
import { vocabularyLessonLabel as label } from '../js/study-labels.js';
assert.equal(label('人間関係1: 家族と友達、性格','性格'),'人間関係1: 家族と友達、性格');
assert.equal(label('病院','入院'),'病院 · 入院');
assert.equal(label('Topic',''), 'Topic');
assert.equal(label('', 'Section'), 'Section');
let total=0, duplicates=0;
for(const file of fs.readdirSync('data/vocabulary').filter(f=>f.endsWith('.json'))) {
 const data=JSON.parse(fs.readFileSync(`data/vocabulary/${file}`));
 for(const chapter of data.chapters || []) {
  for(const section of chapter.sections || []) {
   if(!section.words?.length) continue;
   total++;
   const topic=chapter.metadata?.topic_ja || '', part=section.title_ja || '';
   if(part && topic.includes(part)) {duplicates++; assert.equal(label(topic,part),topic);}
   else assert.equal(label(topic,part),[topic,part].filter(Boolean).join(' · '));
  }
 }
}
console.log(`Checked ${total} vocabulary topic/section pairs; ${duplicates} redundant joins prevented. Vocabulary data unchanged.`);
