/* =======================================================
   NIHONGO INTERMEDIATE — scripts/verify_time_daylog.mjs
   Verification suite for WP-2 (Time Module & Daylog)
   ======================================================= */

import assert from 'node:assert/strict';
import {
  IST_OFFSET_MS,
  IST_SLOT_A_HOUR,
  IST_SLOT_A_MINUTE,
  IST_SLOT_B_HOUR,
  IST_SLOT_B_MINUTE,
  istNow,
  istDateKey,
  istDayStart,
  daysBetween,
  snapToNextDueSlot,
  N3Time
} from '../js/time.js';

import {
  DAYLOG_STORAGE_KEY,
  createEmptyDayRecord,
  loadDaylog,
  saveDaylog,
  clearDaylog,
  getDay,
  logActivity,
  getCurrentStreak,
  countToHeatmapLevel,
  getHeatmap30,
  mergeDaylogs,
  N3Daylog
} from '../js/daylog.js';

console.log('--- Starting WP-2 Verification (Time Module & Daylog) ---');

// ==========================================
// 1. Time Module: IST Constants & Conversions
// ==========================================
console.log('\n[1/5] Testing IST Date/Time Calculations...');

assert.equal(IST_OFFSET_MS, 19800000, 'IST offset should be 5.5 hours in ms (19,800,000)');

const nowIST = istNow();
assert.ok(nowIST instanceof Date, 'istNow() should return a Date instance');
assert.ok(nowIST.__isIST, 'istNow() should be marked as an IST Date');
assert.equal(typeof nowIST.getHours(), 'number', 'nowIST.getHours() should return a number');
assert.equal(nowIST.getHours(), nowIST.getUTCHours(), 'Proxied local getHours should match UTC hours on adjusted Date');

// Test IST Date Key format
const todayKey = istDateKey();
assert.match(todayKey, /^\d{4}-\d{2}-\d{2}$/, 'istDateKey() should return YYYY-MM-DD');

// Test IST date transition across midnight (UTC 18:30 is IST 00:00 next day)
// 2026-10-13 18:29:59.000 UTC = 2026-10-13 23:59:59.000 IST
const beforeMidnightUTC = Date.UTC(2026, 9, 13, 18, 29, 59);
assert.equal(istDateKey(beforeMidnightUTC), '2026-10-13', '18:29:59 UTC should be 2026-10-13 in IST');

// 2026-10-13 18:30:00.000 UTC = 2026-10-14 00:00:00.000 IST
const atMidnightUTC = Date.UTC(2026, 9, 13, 18, 30, 0);
assert.equal(istDateKey(atMidnightUTC), '2026-10-14', '18:30:00 UTC should roll over to 2026-10-14 in IST');

// Test string passthrough for 'YYYY-MM-DD'
assert.equal(istDateKey('2026-10-20'), '2026-10-20', 'istDateKey with YYYY-MM-DD string returns identical string');

// Test istDayStart
const dayStartOct14 = istDayStart('2026-10-14');
assert.equal(dayStartOct14, Date.UTC(2026, 9, 13, 18, 30, 0), '00:00:00 IST for 2026-10-14 is 18:30:00 UTC on 2026-10-13');

// istDayStart for a midday timestamp on 2026-10-14
const middayOct14 = Date.UTC(2026, 9, 14, 8, 30, 0); // 14:00 IST on 2026-10-14
assert.equal(istDayStart(middayOct14), dayStartOct14, 'istDayStart on midday timestamp returns midnight IST');

// Test daysBetween
assert.equal(daysBetween('2026-10-14', '2026-10-14'), 0, 'Same day should return 0 days between');
assert.equal(daysBetween(beforeMidnightUTC, atMidnightUTC), 1, 'Two timestamps 1 second apart across IST midnight should count 1 calendar day');
assert.equal(daysBetween(atMidnightUTC, beforeMidnightUTC), 1, 'daysBetween should be commutative (order-independent)');
assert.equal(daysBetween('2026-10-01', '2026-10-15'), 14, '14 calendar days between 2026-10-01 and 2026-10-15');

console.log('✓ IST Date calculations passed');

// ==========================================
// 2. Slot Snapping: snapToNextDueSlot
// ==========================================
console.log('\n[2/5] Testing snapToNextDueSlot (07:30 & 17:45 IST)...');

// October 14, 2026:
// Slot A: 07:30 IST = 02:00 UTC
// Slot B: 17:45 IST = 12:15 UTC
// Next Slot A (Oct 15): 07:30 IST = 02:00 UTC
const expectedSlotA = Date.UTC(2026, 9, 14, 2, 0, 0);
const expectedSlotB = Date.UTC(2026, 9, 14, 12, 15, 0);
const expectedNextSlotA = Date.UTC(2026, 9, 15, 2, 0, 0);

// Early morning 05:00 IST (23:30 UTC on Oct 13) -> snaps to Slot A today
const earlyMorning = Date.UTC(2026, 9, 13, 23, 30, 0);
assert.equal(snapToNextDueSlot(earlyMorning), expectedSlotA, '05:00 IST snaps to 07:30 IST today');

// Exactly at Slot A (07:30 IST) -> snaps to Slot A today
assert.equal(snapToNextDueSlot(expectedSlotA), expectedSlotA, 'Exact 07:30 IST snaps to 07:30 IST today');

// Midday 12:00 IST (06:30 UTC) -> snaps to Slot B today
const midday = Date.UTC(2026, 9, 14, 6, 30, 0);
assert.equal(snapToNextDueSlot(midday), expectedSlotB, '12:00 IST snaps to 17:45 IST today');

// Exactly at Slot B (17:45 IST) -> snaps to Slot B today
assert.equal(snapToNextDueSlot(expectedSlotB), expectedSlotB, 'Exact 17:45 IST snaps to 17:45 IST today');

// Evening 18:30 IST (13:00 UTC) -> snaps to next morning Slot A
const evening = Date.UTC(2026, 9, 14, 13, 0, 0);
assert.equal(snapToNextDueSlot(evening), expectedNextSlotA, '18:30 IST snaps to 07:30 IST tomorrow');

console.log('✓ Slot snapping passed');

// ==========================================
// 3. Activity Logging: logActivity & getDay
// ==========================================
console.log('\n[3/5] Testing Daylog Activity Logging...');

clearDaylog();

const empty = createEmptyDayRecord('2026-10-14');
assert.deepEqual(empty, {
  date: '2026-10-14',
  reviews: 0,
  newCards: 0,
  minutes: 0,
  pillars: { vocab: 0, kanji: 0, grammar: 0, reading: 0 }
}, 'Empty record has correct initial shape');

// Log a vocab review
const r1 = logActivity({
  pillar: 'vocab',
  type: 'review',
  count: 5,
  minutes: 4,
  date: '2026-10-14'
});
assert.equal(r1.reviews, 5, 'Reviews should be incremented to 5');
assert.equal(r1.newCards, 0, 'newCards should remain 0');
assert.equal(r1.minutes, 4, 'Minutes should be 4');
assert.equal(r1.pillars.vocab, 5, 'Pillars.vocab should be 5');

// Log new kanji cards
const r2 = logActivity({
  pillar: 'kanji',
  type: 'newCards',
  count: 3,
  minutes: 2,
  date: '2026-10-14'
});
assert.equal(r2.reviews, 5, 'Reviews should remain 5');
assert.equal(r2.newCards, 3, 'newCards should be 3');
assert.equal(r2.minutes, 6, 'Minutes should accumulate to 6');
assert.equal(r2.pillars.kanji, 3, 'Pillars.kanji should be 3');

// Log grammar review with default count=1
const r3 = logActivity({
  pillar: 'grammar',
  type: 'review',
  date: '2026-10-14'
});
assert.equal(r3.reviews, 6, 'Reviews should increment to 6');
assert.equal(r3.pillars.grammar, 1, 'Pillars.grammar should be 1');

// Log reading with ms duration (should cap ms at 60s and add ~1 min)
const r4 = logActivity({
  pillar: 'reading',
  count: 1,
  ms: 120000, // 120s -> capped at 60s = 1 min
  date: '2026-10-14'
});
assert.equal(r4.reviews, 7, 'Reviews should increment to 7');
assert.equal(r4.pillars.reading, 1, 'Pillars.reading should be 1');
assert.equal(r4.minutes, 7, 'Duration in ms should be capped and added to minutes');

// Verify getDay retrieves persisted data accurately
const fetched = getDay('2026-10-14');
assert.equal(fetched.reviews, 7);
assert.equal(fetched.newCards, 3);
assert.equal(fetched.minutes, 7);
assert.equal(fetched.pillars.vocab, 5);
assert.equal(fetched.pillars.kanji, 3);
assert.equal(fetched.pillars.grammar, 1);
assert.equal(fetched.pillars.reading, 1);

console.log('✓ Activity logging and retrieval passed');

// ==========================================
// 4. Streak Calculation: getCurrentStreak
// ==========================================
console.log('\n[4/5] Testing Consecutive Streak Calculation...');

clearDaylog();

// Scenario A: No logs -> streak is 0
assert.equal(getCurrentStreak('2026-10-14'), 0, 'Empty daylog should have streak 0');

// Scenario B: Active today only -> streak is 1
logActivity({ date: '2026-10-14', type: 'review', count: 1 });
assert.equal(getCurrentStreak('2026-10-14'), 1, 'Active today gives streak 1');

// Scenario C: Active today and yesterday -> streak is 2
logActivity({ date: '2026-10-13', type: 'review', count: 1 });
assert.equal(getCurrentStreak('2026-10-14'), 2, 'Active today and yesterday gives streak 2');

// Scenario D: Active on Oct 11, Oct 12, Oct 13, Oct 14 -> streak is 4
logActivity({ date: '2026-10-12', type: 'review', count: 3 });
logActivity({ date: '2026-10-11', type: 'newCards', count: 2 });
assert.equal(getCurrentStreak('2026-10-14'), 4, '4 consecutive active days gives streak 4');

// Scenario E: Today (Oct 15) is NOT active yet, but yesterday (Oct 14) and 3 days prior were active
// Ending yesterday preserves streak intact
assert.equal(getCurrentStreak('2026-10-15'), 4, 'Streak ending yesterday when today has not started remains 4');

// Scenario F: User misses today (Oct 16) AND yesterday (Oct 15) -> streak is 0 (broken)
assert.equal(getCurrentStreak('2026-10-16'), 0, 'Missing both today and yesterday breaks the streak to 0');

console.log('✓ Streak calculation passed');

// ==========================================
// 5. Heatmap Array & Idempotent Merge
// ==========================================
console.log('\n[5/5] Testing 30-Day Heatmap & Daylog Merge...');

// Test count to heatmap level mapping
assert.equal(countToHeatmapLevel(0), 0);
assert.equal(countToHeatmapLevel(5), 1);
assert.equal(countToHeatmapLevel(15), 2);
assert.equal(countToHeatmapLevel(35), 3);
assert.equal(countToHeatmapLevel(75), 4);

// Test getHeatmap30 returns exactly 30 days chronologically
const heatmap = getHeatmap30('2026-10-14');
assert.equal(heatmap.length, 30, 'Heatmap should contain exactly 30 days');
assert.equal(heatmap[29].date, '2026-10-14', 'Last item in heatmap should be reference day (today)');
assert.equal(heatmap[0].date, '2026-09-15', 'First item in heatmap should be 29 days before reference day');

// Check that the days with logged activity have positive counts and levels
const oct14Item = heatmap.find(h => h.date === '2026-10-14');
assert.ok(oct14Item, 'Oct 14 item exists in heatmap');
assert.equal(oct14Item.count, 1, 'Oct 14 count matches logged activity');
assert.equal(oct14Item.level, 1, 'Oct 14 level matches intensity level 1');

// Test mergeDaylogs rule (max of each numeric counter)
const localLog = {
  '2026-10-14': {
    date: '2026-10-14',
    reviews: 10,
    newCards: 2,
    minutes: 5,
    pillars: { vocab: 8, kanji: 4, grammar: 0, reading: 0 }
  }
};
const remoteLog = {
  '2026-10-14': {
    date: '2026-10-14',
    reviews: 8,
    newCards: 5,
    minutes: 7,
    pillars: { vocab: 6, kanji: 5, grammar: 2, reading: 0 }
  },
  '2026-10-13': {
    date: '2026-10-13',
    reviews: 12,
    newCards: 0,
    minutes: 6,
    pillars: { vocab: 12, kanji: 0, grammar: 0, reading: 0 }
  }
};

const merged = mergeDaylogs(localLog, remoteLog);
assert.equal(merged['2026-10-14'].reviews, 10, 'Reviews should be max(10, 8) = 10');
assert.equal(merged['2026-10-14'].newCards, 5, 'newCards should be max(2, 5) = 5');
assert.equal(merged['2026-10-14'].minutes, 7, 'Minutes should be max(5, 7) = 7');
assert.equal(merged['2026-10-14'].pillars.vocab, 8, 'Vocab should be max(8, 6) = 8');
assert.equal(merged['2026-10-14'].pillars.kanji, 5, 'Kanji should be max(4, 5) = 5');
assert.equal(merged['2026-10-14'].pillars.grammar, 2, 'Grammar should be max(0, 2) = 2');
assert.equal(merged['2026-10-13'].reviews, 12, 'Non-conflicting remote date should be merged cleanly');

console.log('✓ 30-Day Heatmap & Idempotent Merge passed');

// Window bindings check
assert.ok(N3Time, 'N3Time export is defined');
assert.ok(N3Daylog, 'N3Daylog export is defined');

console.log('\n=======================================================');
console.log('🎉 ALL WP-2 VERIFICATION TESTS PASSED SUCCESSFULLY!');
console.log('=======================================================');
