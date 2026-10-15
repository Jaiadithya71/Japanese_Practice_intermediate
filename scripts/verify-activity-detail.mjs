import assert from 'node:assert/strict';
import fs from 'node:fs';
import { renderActivityDayHtml } from '../js/activity-detail.js';
for (const count of [0,1,126]) {
 const html=renderActivityDayHtml({date:'2026-10-15',reviews:count,newCards:9,minutes:18,pillars:{vocab:100},wrong:7});

 assert.match(html,/Oct 15 - /);
 assert.ok(html.includes(`>${count}</span> ${count === 1 ? 'review' : 'reviews'}`));
 assert.doesNotMatch(html,/New cards|Minutes|Vocabulary|Wrong attempts|accuracy/);
}
const source=fs.readFileSync('js/home.js','utf8');
const detail=source.slice(source.indexOf('const detail ='),source.indexOf('const streak ='));
assert.match(detail,/createElement\('button'\)/);
assert.match(detail,/getDay\(button.dataset.date\)/);
assert.doesNotMatch(detail,/logActivity|saveDaylog|localStorage.setItem/);
console.log('Day click: inline date and reviews, pluralisation, keyboard-native buttons and read-only rendering passed.');

assert.match(renderActivityDayHtml({date:'2026-01-01',reviews:2}), /Jan 1 - /);
assert.match(renderActivityDayHtml({date:'2026-12-31',reviews:3}), /Dec 31 - /);
