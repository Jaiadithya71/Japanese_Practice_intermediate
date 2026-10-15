/* =======================================================
   NIHONGO INTERMEDIATE — time.js
   IST (Indian Standard Time, UTC+5:30) Scheduling & Date Utilities
   ======================================================= */

import {
  IST_SLOT_A_HOUR as CFG_SLOT_A_HOUR,
  IST_SLOT_A_MINUTE as CFG_SLOT_A_MINUTE,
  IST_SLOT_B_HOUR as CFG_SLOT_B_HOUR,
  IST_SLOT_B_MINUTE as CFG_SLOT_B_MINUTE
} from './config.js';

export const IST_OFFSET_MS = 5.5 * 60 * 60 * 1000; // 19,800,000 ms (+5:30)

export const IST_SLOT_A_HOUR = typeof CFG_SLOT_A_HOUR === 'number' ? CFG_SLOT_A_HOUR : 7;
export const IST_SLOT_A_MINUTE = typeof CFG_SLOT_A_MINUTE === 'number' ? CFG_SLOT_A_MINUTE : 30; // 07:30 IST
export const IST_SLOT_B_HOUR = typeof CFG_SLOT_B_HOUR === 'number' ? CFG_SLOT_B_HOUR : 17;
export const IST_SLOT_B_MINUTE = typeof CFG_SLOT_B_MINUTE === 'number' ? CFG_SLOT_B_MINUTE : 45; // 17:45 IST

/**
 * Converts various date/timestamp input types into UTC milliseconds.
 * Respects internal __isIST markers on adjusted Date objects.
 */
function toTimestamp(val) {
  if (val == null) {
    return Date.now();
  }
  if (typeof val === 'number') {
    return val;
  }
  if (val instanceof Date) {
    if (val.__isIST) {
      return val.getTime() - IST_OFFSET_MS;
    }
    return val.getTime();
  }
  if (typeof val === 'string') {
    const trimmed = val.trim();
    if (/^\d{4}-\d{2}-\d{2}$/.test(trimmed)) {
      const [y, m, d] = trimmed.split('-').map(Number);
      return Date.UTC(y, m - 1, d, 0, 0, 0, 0) - IST_OFFSET_MS;
    }
    const parsed = Date.parse(trimmed);
    if (!Number.isNaN(parsed)) {
      return parsed;
    }
  }
  return Date.now();
}

/**
 * Returns current Date converted/adjusted to IST.
 * Its UTC getters/methods represent the wall-clock IST time, and local getters
 * are proxied so standard methods (.getHours(), .getDate(), etc.) match IST.
 */
export function istNow() {
  const istMs = Date.now() + IST_OFFSET_MS;
  const d = new Date(istMs);
  d.__isIST = true;

  // Proxy local getters to UTC getters so local wall-clock calls match IST regardless of machine locale
  d.getFullYear = function getFullYearIST() { return this.getUTCFullYear(); };
  d.getMonth = function getMonthIST() { return this.getUTCMonth(); };
  d.getDate = function getDateIST() { return this.getUTCDate(); };
  d.getDay = function getDayIST() { return this.getUTCDay(); };
  d.getHours = function getHoursIST() { return this.getUTCHours(); };
  d.getMinutes = function getMinutesIST() { return this.getUTCMinutes(); };
  d.getSeconds = function getSecondsIST() { return this.getUTCSeconds(); };
  d.getMilliseconds = function getMillisecondsIST() { return this.getUTCMilliseconds(); };

  return d;
}

/**
 * Returns 'YYYY-MM-DD' formatted date string in IST for a given date or timestamp.
 * Defaults to current time if no argument provided.
 */
export function istDateKey(date) {
  if (typeof date === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(date.trim())) {
    return date.trim();
  }
  const ms = toTimestamp(date);
  const istMs = ms + IST_OFFSET_MS;
  const d = new Date(istMs);
  const y = d.getUTCFullYear();
  const m = String(d.getUTCMonth() + 1).padStart(2, '0');
  const day = String(d.getUTCDate()).padStart(2, '0');
  return `${y}-${m}-${day}`;
}

/**
 * Returns the timestamp (ms since epoch) of 00:00:00.000 IST for the specified date.
 * If date is omitted, returns 00:00:00.000 IST for today.
 */
export function istDayStart(date) {
  if (typeof date === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(date.trim())) {
    const [y, m, d] = date.trim().split('-').map(Number);
    return Date.UTC(y, m - 1, d, 0, 0, 0, 0) - IST_OFFSET_MS;
  }
  const ms = toTimestamp(date);
  return Math.floor((ms + IST_OFFSET_MS) / 86400000) * 86400000 - IST_OFFSET_MS;
}

/**
 * Returns the number of whole calendar days between two timestamps in IST.
 * Difference is non-negative and based on IST calendar boundaries.
 */
export function daysBetween(t1, t2) {
  const start1 = istDayStart(t1);
  const start2 = istDayStart(t2);
  return Math.round(Math.abs(start2 - start1) / 86400000);
}

/**
 * Aligns next due timestamp to India Standard Time (IST UTC + 5:30) study slots:
 * Slot A: 07:30 IST
 * Slot B: 17:45 IST
 *
 * If ms <= Slot A today: snaps to Slot A today.
 * If ms <= Slot B today: snaps to Slot B today.
 * If ms > Slot B today: snaps to Slot A tomorrow.
 */
export function snapToNextDueSlot(timestamp) {
  const ms = toTimestamp(timestamp);
  const istMs = ms + IST_OFFSET_MS;
  const d = new Date(istMs);

  const year = d.getUTCFullYear();
  const month = d.getUTCMonth();
  const date = d.getUTCDate();

  const slotAMs = Date.UTC(year, month, date, IST_SLOT_A_HOUR, IST_SLOT_A_MINUTE, 0, 0) - IST_OFFSET_MS;
  const slotBMs = Date.UTC(year, month, date, IST_SLOT_B_HOUR, IST_SLOT_B_MINUTE, 0, 0) - IST_OFFSET_MS;

  if (ms <= slotAMs) {
    return slotAMs;
  } else if (ms <= slotBMs) {
    return slotBMs;
  } else {
    // Next day Slot A
    return Date.UTC(year, month, date + 1, IST_SLOT_A_HOUR, IST_SLOT_A_MINUTE, 0, 0) - IST_OFFSET_MS;
  }
}

export const N3Time = {
  IST_OFFSET_MS,
  IST_SLOT_A_HOUR,
  IST_SLOT_A_MINUTE,
  IST_SLOT_B_HOUR,
  IST_SLOT_B_MINUTE,
  istNow,
  istDateKey,
  istDayStart,
  daysBetween,
  snapToNextDueSlot
};

if (typeof window !== 'undefined') {
  window.N3Time = N3Time;
}

export default N3Time;
