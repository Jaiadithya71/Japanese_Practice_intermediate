import assert from 'node:assert/strict';
import fs from 'node:fs';
const s=fs.readFileSync('js/study.js','utf8');
const flip=s.slice(s.indexOf('export function flipCard()'),s.indexOf('export function gradeCard'));
assert.doesNotMatch(flip,/animate|await|setTimeout/);
assert.match(flip,/state.cardFlipped = !state.cardFlipped/);
assert.match(flip,/renderCard\(\)/);
console.log('Instant reveal restored, no animation or delay.');
