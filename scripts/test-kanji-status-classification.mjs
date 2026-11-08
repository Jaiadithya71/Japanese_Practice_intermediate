// Isolated, in-memory verification of the Kanji status box classification.
// Imports the REAL srs.js / state.js from the repo; crafts fake stats in
// memory only. Nothing touches localStorage, the Gist, or any real record.
import { state } from '../js/state.js';
import { peekItemStatus, getItemStatus } from '../js/srs.js';

let failures = 0;
const eq = (name, got, want) => {
  const ok = got === want;
  if (!ok) failures++;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${name}: got=${got} want=${want}`);
};

// --- fixture stats (fabricated, in-memory only) ---
state.stats = {
  // mastered via reps>=4 && interval>=21 && weight<=0.8
  'KWR:食べる': { reps: 5, interval: 30, weight: 0.6, correct: 2, incorrect: 1, isHard: false },
  // mastered via correct>=MASTERED_THRESHOLD(3) && weight<=0.8
  'KWR:飲む':   { reps: 2, interval: 3, weight: 0.5, correct: 3, incorrect: 0, isHard: false },
  // learning: some activity, no mastery, weight mid
  'KWR:走る':   { reps: 1, interval: 1, weight: 1.2, correct: 1, incorrect: 0, isHard: false },
  // hard by weight >= HARD_THRESHOLD(1.8)
  'KWR:読む':   { reps: 3, interval: 2, weight: 2.1, correct: 1, incorrect: 2, isHard: false },
  // hard by isHard flag even with mastered-looking numbers (flag wins)
  'KWR:書く':   { reps: 10, interval: 60, weight: 0.5, correct: 9, incorrect: 0, isHard: true },
  // weight exactly 0.8 boundary still mastered
  'KWK:食べる': { reps: 4, interval: 21, weight: 0.8, correct: 1, incorrect: 0, isHard: false },
  // weight 0.81 with mastery reps -> NOT mastered -> learning
  'KWK:飲む':   { reps: 6, interval: 40, weight: 0.81, correct: 4, incorrect: 0, isHard: false },
  // hard on the kana facet only
  'KWK:読む':   { reps: 2, interval: 1, weight: 3.0, correct: 0, incorrect: 4, isHard: false },
  // learning on kana facet
  'KWK:走る':   { reps: 1, interval: 1, weight: 1.0, correct: 0, incorrect: 1, isHard: false },
  // KWK:書く and KWR:話す intentionally absent -> unseen
};

// --- direct classification checks ---
eq('KWR mastered (reps+interval)', peekItemStatus('KWR:食べる'), 'mastered');
eq('KWR mastered (correct>=3)', peekItemStatus('KWR:飲む'), 'mastered');
eq('KWR learning', peekItemStatus('KWR:走る'), 'learning');
eq('KWR hard (weight)', peekItemStatus('KWR:読む'), 'hard');
eq('KWR hard (isHard flag beats mastered)', peekItemStatus('KWR:書く'), 'hard');
eq('KWK mastered (weight 0.8 boundary)', peekItemStatus('KWK:食べる'), 'mastered');
eq('KWK learning (weight 0.81 not mastered)', peekItemStatus('KWK:飲む'), 'learning');
eq('KWK hard', peekItemStatus('KWK:読む'), 'hard');
eq('KWK learning2', peekItemStatus('KWK:走る'), 'learning');
eq('absent key -> unseen', peekItemStatus('KWR:話す'), 'unseen');

// --- peek must match getItemStatus on existing records, and stay non-mutating ---
let mismatch = 0;
for (const k of Object.keys(state.stats)) {
  if (peekItemStatus(k) !== getItemStatus(k)) { mismatch++; console.log('MISMATCH', k); }
}
eq('peek==getItemStatus on all existing records', mismatch, 0);
const before = Object.keys(state.stats).length;
peekItemStatus('KWR:話す'); peekItemStatus('KWK:書く'); peekItemStatus('KWR:見る');
eq('peek created no records', Object.keys(state.stats).length, before);

// --- replicate renderKanjiStatus's counting loop over a fake kanjiDB ---
// (same loop as js/kanji.js renderKanjiStatus; verifies bucketing + dedup)
state.kanjiDB = {
  '食': { words: [{ term_ja: '食べる' }, { term_ja: '飲む' }] },
  '飲': { words: [{ term_ja: '飲む' }, { term_ja: '走る' }] },   // 飲む duplicated across kanji
  '読': { words: [{ term_ja: '読む' }, { word: '書く' }] },       // word fallback key
  '話': { words: [{ term_ja: '話す' }] },                          // unseen both facets
};
const words = new Set();
for (const char in state.kanjiDB) {
  for (const w of state.kanjiDB[char].words || []) {
    const t = (w.term_ja || w.word || '').trim();
    if (t) words.add(t);
  }
}
eq('unique words pooled', words.size, 6);
const counts = facet => {
  const c = { mastered: 0, learning: 0, hard: 0, unseen: 0 };
  words.forEach(w => {
    const st = peekItemStatus(`${facet}:${w}`);
    c[st === 'mastered' || st === 'hard' || st === 'learning' ? st : 'unseen']++;
  });
  return c;
};
const a = counts('KWR'), b = counts('KWK');
console.log('Part A (KWR):', JSON.stringify(a));
console.log('Part B (KWK):', JSON.stringify(b));
eq('A mastered', a.mastered, 2);            // 食べる, 飲む
eq('A learning', a.learning, 1);            // 走る
eq('A hard', a.hard, 2);                    // 読む, 書く(flag)
eq('A unseen', a.unseen, 1);                // 話す
eq('A total preserved', a.mastered + a.learning + a.hard + a.unseen, 6);
eq('B mastered', b.mastered, 1);            // 食べる
eq('B learning', b.learning, 2);            // 飲む(0.81), 走る
eq('B hard', b.hard, 1);                    // 読む
eq('B unseen', b.unseen, 2);                // 書く, 話す
eq('B total preserved', b.mastered + b.learning + b.hard + b.unseen, 6);

console.log(failures === 0 ? 'ALL TESTS PASSED' : `${failures} FAILURES`);
process.exit(failures === 0 ? 0 : 1);
