/* Lossless compact wire format for N3 per-item progress stats. */

export const STATS_FORMAT_MARKER = '$';
export const STATS_FORMAT_ID = 'n3s';
export const STATS_FORMAT_VERSION = 1;

// Fixed, versioned wire names. Unknown fields are retained with their original names.
const FIELDS = [
  ['correct', 'c', 0],
  ['incorrect', 'i', 0],
  ['weight', 'w', 1],
  ['reps', 'r', 0],
  ['interval', 'n', 0],
  ['easeFactor', 'e', 2.5],
  ['nextDue', 'd', 0],
  ['isHard', 'h', false],
  ['lapses', 'l', 0],
  ['streak', 't', 0],
  ['learnState', 'q', 'learning'],
  ['relearnBase', 'b', null],
  ['leech', 'j', false],
  ['firstSeen', 'f', 0],
  ['hist', 'H', []],
  ['note', 'o', ''],
  ['cause', 'a', ''],
  ['lastSeen', 'z', 0],
  ['reads', 'R', 0],
  ['bestAcc', 'A', 0],
  ['lastAcc', 'B', 0],
  ['bestCpm', 'C', 0],
  ['lastCpm', 'D', 0],
  ['step', 'E', 0],
  ['reading', 'T', ''],
  ['meaning', 'U', ''],
  ['term', 'N', ''],
  ['mastered', 'M', false]
];
const FIELD_BY_NAME = new Map(FIELDS.map(([name, alias, defaultValue], index) => [name, { alias, defaultValue, index }]));
const FIELD_BY_ALIAS = new Map(FIELDS.map(([name, alias]) => [alias, name]));
const ALIAS_SET = new Set(FIELD_BY_ALIAS.keys());

function isRecord(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function jsonEqual(a, b) {
  const stable = value => {
    if (Array.isArray(value)) return value.map(stable);
    if (isRecord(value)) {
      const out = {};
      for (const key of Object.keys(value).sort()) out[key] = stable(value[key]);
      return out;
    }
    return value;
  };
  return JSON.stringify(stable(a)) === JSON.stringify(stable(b));
}

function sameJsonValue(a, b) {
  return jsonEqual(a, b);
}

function validateStats(stats) {
  if (!isRecord(stats)) throw new Error('Progress stats must be a JSON object.');
  for (const [key, value] of Object.entries(stats)) {
    if (!isRecord(value)) throw new Error(`Progress record ${key} is not an object.`);
  }
}

function encodeRecord(record) {
  let mask = 0;
  const values = {};
  for (const [key, value] of Object.entries(record)) {
    const field = FIELD_BY_NAME.get(key);
    if (field) {
      mask += 2 ** field.index;
      if (!sameJsonValue(value, field.defaultValue)) values[field.alias] = value;
    } else {
      // Escape unknown properties that could otherwise be mistaken for a wire alias.
      const encodedKey = (ALIAS_SET.has(key) || key.startsWith('~')) ? `~${key}` : key;
      values[encodedKey] = value;
    }
  }
  return [mask.toString(36), values];
}

function decodeRecord(entry, itemKey) {
  if (!Array.isArray(entry) || entry.length !== 2 || typeof entry[0] !== 'string' || !isRecord(entry[1])) {
    throw new Error(`Compact progress record ${itemKey} has an invalid shape.`);
  }
  if (!/^[0-9a-z]+$/i.test(entry[0])) throw new Error(`Compact progress record ${itemKey} has an invalid presence mask.`);
  const mask = Number.parseInt(entry[0], 36);
  if (!Number.isSafeInteger(mask) || mask < 0 || mask >= 2 ** FIELDS.length) {
    throw new Error(`Compact progress record ${itemKey} has an unsupported presence mask.`);
  }

  const record = {};
  const consumed = new Set();
  for (const [name, alias, defaultValue, index] of FIELDS.map(([name, alias, value], index) => [name, alias, value, index])) {
    const present = Math.floor(mask / (2 ** index)) % 2 === 1;
    const hasValue = Object.prototype.hasOwnProperty.call(entry[1], alias);
    if (present) {
      if (hasValue) {
        record[name] = entry[1][alias];
        consumed.add(alias);
      } else {
        record[name] = defaultValue;
      }
    } else if (hasValue) {
      throw new Error(`Compact progress record ${itemKey} contains a value without its presence bit.`);
    }
  }

  for (const [encodedKey, value] of Object.entries(entry[1])) {
    if (consumed.has(encodedKey)) continue;
    if (FIELD_BY_ALIAS.has(encodedKey)) {
      throw new Error(`Compact progress record ${itemKey} contains an unknown reserved alias.`);
    }
    const key = encodedKey.startsWith('~') ? encodedKey.slice(1) : encodedKey;
    if (Object.prototype.hasOwnProperty.call(record, key)) {
      throw new Error(`Compact progress record ${itemKey} contains a duplicate field.`);
    }
    record[key] = value;
  }
  return record;
}

export function encodeStats(stats) {
  validateStats(stats);
  const compactStats = {};
  for (const [key, record] of Object.entries(stats)) compactStats[key] = encodeRecord(record);
  const payload = JSON.stringify({ [STATS_FORMAT_MARKER]: STATS_FORMAT_ID, v: STATS_FORMAT_VERSION, s: compactStats });

  // Fail closed if our wire codec ever stops preserving the input object.
  const roundTrip = decodeStatsPayload(JSON.parse(payload));
  if (!jsonEqual(stats, roundTrip)) throw new Error('Compact progress validation failed; nothing was written.');
  return payload;
}

export function decodeStatsPayload(parsed) {
  if (!isRecord(parsed)) throw new Error('Progress payload must be a JSON object.');
  if (!Object.prototype.hasOwnProperty.call(parsed, STATS_FORMAT_MARKER)) {
    validateStats(parsed); // Legacy verbose JSON from older app versions.
    return parsed;
  }
  if (parsed[STATS_FORMAT_MARKER] !== STATS_FORMAT_ID) {
    throw new Error('Progress payload uses an unknown format marker; refusing to sync.');
  }
  if (parsed.v !== STATS_FORMAT_VERSION) {
    throw new Error(`Progress payload version ${parsed.v} is unsupported; refusing to sync.`);
  }
  if (!isRecord(parsed.s)) throw new Error('Compact progress stats must be an object.');
  const stats = {};
  for (const [key, entry] of Object.entries(parsed.s)) stats[key] = decodeRecord(entry, key);
  return stats;
}

export function decodeStatsText(content) {
  let parsed;
  try {
    parsed = JSON.parse(content);
  } catch (error) {
    throw error;
  }
  return decodeStatsPayload(parsed);
}
