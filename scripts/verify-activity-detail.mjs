import assert from 'node:assert/strict';
import fs from 'node:fs';
import { renderActivityDayHtml } from '../js/activity-detail.js';
for (const count of [0,1,126]) {
 const html=renderActivityDayHtml({date:'2026-10-15',reviews:count,newCards:9,minutes:18,pillars:{vocab:100},wrong:7});

 assert.ok(html.includes(`>${count}</span> ${count === 1 ? 'review' : 'reviews'}`));
 assert.doesNotMatch(html,/New cards|Minutes|Vocabulary|Wrong attempts|accuracy/);
}
const source=fs.readFileSync('js/home.js','utf8');
const detail=source.slice(source.indexOf('const detail ='),source.indexOf('const streak ='));
assert.match(detail,/createElement\('button'\)/);
assert.match(detail,/getDay\(button.dataset.date\)/);
assert.doesNotMatch(detail,/logActivity|saveDaylog|localStorage.setItem/);
console.log('Day click: inline reviews only, pluralisation, keyboard-native buttons and read-only rendering passed.');
