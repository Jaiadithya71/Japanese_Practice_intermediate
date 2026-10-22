import { characterShapes } from '../data/kanji/character_shapes.js';
/* =======================================================
   NIHONGO INTERMEDIATE - js/distractors.js
   Exam-style confusable options for kanji-word multiple choice.
   Pure functions (no DOM, no app state) so they run under node tests.

   Reading (kanji -> kana): same okurigana ending, same kana count,
     overlapping kana, near-identical readings (voicing, long vowel,
     small tsu), readings of words that share a kanji.
   Writing (kana -> kanji): same character count, same ending,
     words sharing a kanji, and look-alike / sound-family kanji swaps.
   Selection is deterministic: the same word always gets the same
   distractors (ties broken by a stable hash, never Math.random).
   A distractor is never a correct answer: any other word with the
   same reading (writing) or the same spelling (reading) is excluded.
   ======================================================= */

export const SOUND_FAMILIES = [
  ['反', '坂', '板', '返', '飯', '販'], ['寺', '持', '待', '時', '特', '詩'],
  ['方', '訪', '房', '防', '妨', '放'], ['兆', '挑', '逃', '跳', '眺', '桃'],
  ['同', '胴', '銅', '洞', '筒'], ['青', '清', '晴', '静', '精', '情'],
  ['分', '粉', '貧', '盆'], ['包', '抱', '胞', '砲', '泡', '飽'],
  ['交', '校', '郊', '効', '較', '絞'], ['化', '花', '貨', '靴', '華'],
  ['古', '固', '故', '苦', '枯', '湖'], ['平', '評', '坪', '呼'],
  ['白', '百', '拍', '泊', '迫'], ['中', '仲', '沖', '忠'],
  ['主', '注', '柱', '住', '駐', '往'], ['成', '誠', '城', '盛'],
  ['申', '伸', '神'], ['占', '点', '店'], ['台', '治', '始', '胎'],
  ['各', '格', '客', '落', '略', '路'], ['票', '標', '漂'],
  ['肖', '消', '削', '宵'], ['莫', '幕', '漠', '膜', '墓', '暮'],
  ['甫', '捕', '補', '舗', '浦'], ['奇', '寄', '騎', '椅', '崎'],
  ['建', '健', '鍵'], ['丁', '町', '頂', '灯', '打', '訂'],
  ['正', '政', '証', '症', '整'], ['生', '性', '姓', '星'],
  ['義', '儀', '議', '犠'], ['令', '冷', '領', '命', '鈴', '零'],
  ['共', '供', '恭', '港'], ['兼', '嫌', '謙', '廉'],
  ['合', '給', '答', '拾'], ['可', '河', '何', '荷', '歌'],
  ['原', '源', '願'], ['官', '館', '管', '棺'], ['相', '想', '箱', '湘'],
  ['青', '責', '積', '績', '債'], ['式', '試', '拭'], ['良', '浪', '朗', '郎'],
  ['長', '張', '帳', '脹'], ['期', '基', '旗', '欺', '棋'], ['区', '駆', '枢'],
  ['里', '理', '裏', '埋', '厘'], ['工', '功', '攻', '貢', '項'], ['羊', '洋', '祥', '詳', '養']
];

// Visually confusable kanji (shape, not sound)
export const LOOKALIKE_GROUPS = [
  ['毛','手','乞','七'], ['未', '末', '朱'], ['土', '士', '工'], ['日', '曰', '目', '白'], ['己', '已', '巳'],
  ['大', '太', '犬', '天', '夫'], ['午', '牛', '干', '千'], ['万', '方', '力', '刀'],
  ['待', '持', '特', '侍'], ['貝', '見', '員'], ['休', '体', '林'], ['人', '入', '八'],
  ['雨', '雪', '雲'], ['困', '因', '囚'], ['矢', '失', '夫'], ['王', '玉', '主'],
  ['末', '未'], ['微', '徴', '徹'], ['境', '鏡', '竟'], ['検', '険', '験', '倹'],
  ['税', '説', '脱', '悦', '鋭'], ['招', '紹', '昭', '照', '詔'], ['燃', '然', '撚'],
  ['低', '抵', '底', '氏'], ['拾', '捨', '給'], ['候', '侯', '喉'], ['折', '析', '祈', '近'],
  ['係', '孫', '系'], ['優', '憂', '擾'], ['衣', '依', '哀', '表'], ['辺', '込', '迫', '返'],
  ['糸', '系', '紙'], ['割', '害', '憲'], ['増', '僧', '贈', '憎'], ['栄', '営', '学', '労'],
  ['勤', '謹', '僅', '勲'], ['象', '像', '豪'], ['担', '但', '旦', '胆'], ['移', '秒', '称']
];

const SOUND_MAP = buildGroupMap(SOUND_FAMILIES);
const SHAPE_MAP = buildGroupMap(LOOKALIKE_GROUPS);

function buildGroupMap(groups) {
  const m = new Map();
  for (const g of groups) {
    for (const c of g) {
      if (!m.has(c)) m.set(c, new Set());
      for (const p of g) if (p !== c) m.get(c).add(p);
    }
  }
  return m;
}

// Rank actual glyph families, with dictionary radical and stroke data covering every Joyo character.
const RADICAL_MAP = new Map();
for (const [ch, info] of Object.entries(characterShapes)) {
  if (!RADICAL_MAP.has(info.radical)) RADICAL_MAP.set(info.radical, []);
  RADICAL_MAP.get(info.radical).push(ch);
}
const hira = s => String(s || '').replace(/[ァ-ヶ]/g, c => String.fromCharCode(c.charCodeAt(0) - 0x60)).replace(/[-.]/g, '');
export function shapeSimilarity(a, b) {
  if (a === b) return 0;
  const x = characterShapes[a], y = characterShapes[b];
  let score = SHAPE_MAP.get(a)?.has(b) ? 20 : 0;
  if (SOUND_MAP.get(a)?.has(b)) score = Math.max(score, 15);
  if (x && y && x.radical === y.radical) score = Math.max(score, 12 + Math.max(0, 6 - Math.abs(x.strokes - y.strokes)));
  if (!score && x && y && Math.abs(x.strokes-y.strokes) <= 1) score = 2 - Math.abs(x.strokes-y.strokes);
  return score;
}
const SHAPE_CANDIDATES = new Map();
function shapeCandidates(ch) {
  if (!SHAPE_CANDIDATES.has(ch)) {
    const list = new Set([...(SHAPE_MAP.get(ch) || []), ...(SOUND_MAP.get(ch) || []), ...(RADICAL_MAP.get(characterShapes[ch]?.radical) || [])]);
    // Rare radicals may have fewer than three Joyo members. Fill by nearest stroke count,
    // never by random same-lesson words. Strong radical/component matches always outrank this tier.
    if (list.size < 6) for (const [candidate, info] of Object.entries(characterShapes)) {
      if (Math.abs(info.strokes - (characterShapes[ch]?.strokes || 0)) <= 1) list.add(candidate);
    }
    list.delete(ch);
    SHAPE_CANDIDATES.set(ch, [...list].sort((a,b) => shapeSimilarity(ch,b)-shapeSimilarity(ch,a) || a.localeCompare(b)).slice(0,16));
  }
  return SHAPE_CANDIDATES.get(ch);
}

const KANJI_RE = /[\u3400-\u9fff々]/;
const isKanji = ch => KANJI_RE.test(ch);

export function kanjiChars(text) {
  return Array.from(new Set(Array.from(text || '').filter(isKanji)));
}

/** Trailing hiragana after the last kanji ("割る" -> "る"), or '' when none. */
export function okuriganaOf(term) {
  const m = String(term || '').match(/[\u3400-\u9fff々]+([\u3041-\u3096]+)$/);
  return m ? m[1] : '';
}

/** Stable 32-bit string hash (FNV-1a) for deterministic tie-breaking. */
export function stableHash(str) {
  let h = 0x811c9dc5;
  for (const ch of String(str)) {
    h ^= ch.codePointAt(0);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h >>> 0;
}

const VOICING = {
  か: 'が', き: 'ぎ', く: 'ぐ', け: 'げ', こ: 'ご', さ: 'ざ', し: 'じ', す: 'ず', せ: 'ぜ', そ: 'ぞ',
  た: 'だ', ち: 'ぢ', つ: 'づ', て: 'で', と: 'ど', は: 'ば', ひ: 'び', ふ: 'ぶ', へ: 'べ', ほ: 'ぼ',
  が: 'か', ぎ: 'き', ぐ: 'く', げ: 'け', ご: 'こ', ざ: 'さ', じ: 'し', ず: 'す', ぜ: 'せ', ぞ: 'そ',
  だ: 'た', ぢ: 'ち', づ: 'つ', で: 'て', ど: 'と', ば: 'は', び: 'ひ', ぶ: 'ふ', べ: 'へ', ぼ: 'ほ',
  ぱ: 'ば'
};
const SEMI = { は: 'ぱ', ひ: 'ぴ', ふ: 'ぷ', へ: 'ぺ', ほ: 'ぽ', ば: 'ぱ', び: 'ぴ', ぶ: 'ぷ', べ: 'ぺ', ぼ: 'ぽ' };
const SMALL = { や: 'ゃ', ゆ: 'ゅ', よ: 'ょ', ゃ: 'や', ゅ: 'ゆ', ょ: 'よ' };
const LONG_V = { あ: 'あ', い: 'い', う: 'う', え: 'い', お: 'う' };
const VOWEL_OF = {};
for (const [v, row] of Object.entries({
  あ: 'あかさたなはまやらわがざだばぱぁゃ', い: 'いきしちにひみりぎじぢびぴぃ', う: 'うくすつぬふむゆるぐずづぶぷぅゅ',
  え: 'えけせてねへめれげぜでべぺぇ', お: 'おこそとのほもよろをごぞどぼぽぉょ'
})) for (const ch of row) VOWEL_OF[ch] = v;

/** Near-identical variants of a reading, protecting the fixed okurigana tail. */
export function readingMutations(reading, okurigana = '') {
  const out = new Set();
  const stem = okurigana && reading.endsWith(okurigana) ? reading.slice(0, reading.length - okurigana.length) : reading;
  const tail = reading.slice(stem.length);
  const chars = Array.from(stem);
  const add = arr => { const s = arr.join('') + tail; if (s !== reading && Array.from(s).length >= 2) out.add(s); };
  const RENDAKU = { か: 'が', き: 'ぎ', く: 'ぐ', け: 'げ', こ: 'ご', さ: 'ざ', し: 'じ', す: 'ず', せ: 'ぜ', そ: 'ぞ', た: 'だ', ち: 'じ', つ: 'ず', て: 'で', と: 'ど', は: 'ば', ひ: 'び', ふ: 'ぶ', へ: 'べ', ほ: 'ぼ' };
  const UNVOICE = { が: 'か', ぎ: 'き', ぐ: 'く', げ: 'け', ご: 'こ', ざ: 'さ', じ: 'し', ず: 'す', ぜ: 'せ', ぞ: 'そ', だ: 'た', で: 'て', ど: 'と', ば: 'は', び: 'ひ', ぶ: 'ふ', べ: 'へ', ぼ: 'ほ' };
  const HANDAKU = { は: 'ぱ', ひ: 'ぴ', ふ: 'ぷ', へ: 'ぺ', ほ: 'ぽ' };
  chars.forEach((c, i) => {
    if (i > 0 && RENDAKU[c]) { const a = chars.slice(); a[i] = RENDAKU[c]; add(a); }
    if (UNVOICE[c]) { const a = chars.slice(); a[i] = UNVOICE[c]; add(a); }
    if (i > 0 && HANDAKU[c] && (chars[i - 1] === 'っ' || chars[i - 1] === 'ん')) { const a = chars.slice(); a[i] = HANDAKU[c]; add(a); }
    // long vowel: おう / えい added or dropped
    if (i > 0 && ((c === 'う' && VOWEL_OF[chars[i - 1]] === 'お') || (c === 'い' && VOWEL_OF[chars[i - 1]] === 'え'))) { const a = chars.slice(); a.splice(i, 1); add(a); }
    if (i < chars.length - 1 && VOWEL_OF[c] === 'お' && !'ょ'.includes(c) && chars[i + 1] !== 'う') { const a = chars.slice(); a.splice(i + 1, 0, 'う'); add(a); }
    if (i < chars.length - 1 && VOWEL_OF[c] === 'え' && chars[i + 1] !== 'い') { const a = chars.slice(); a.splice(i + 1, 0, 'い'); add(a); }
    // sokuon dropped or inserted before a voiceless consonant
    if (c === 'っ') { const a = chars.slice(); a.splice(i, 1); add(a); }
    if (i > 0 && 'かきくけこさしすせそたちつてとぱぴぷぺぽ'.includes(c) && chars[i - 1] !== 'っ' && !'ゃゅょ'.includes(chars[i - 1])) {
      const a = chars.slice(); a.splice(i, 0, 'っ'); add(a);
    }
    // small ya/yu/yo swap (きょう / きゅう / きゃう)
    if ('ゃゅょ'.includes(c)) for (const alt of 'ゃゅょ') if (alt !== c) { const a = chars.slice(); a[i] = alt; add(a); }
  });
  return Array.from(out);
}

function bigrams(s) {
  const a = Array.from(s), r = [];
  for (let i = 0; i + 1 < a.length; i++) r.push(a[i] + a[i + 1]);
  return r;
}
function dice(a, b) {
  const x = bigrams(a), y = bigrams(b);
  if (!x.length || !y.length) return 0;
  const pool = new Map();
  for (const g of y) pool.set(g, (pool.get(g) || 0) + 1);
  let hit = 0;
  for (const g of x) if ((pool.get(g) || 0) > 0) { hit++; pool.set(g, pool.get(g) - 1); }
  return (2 * hit) / (x.length + y.length);
}
function commonPrefix(a, b) { let i = 0; const x = Array.from(a), y = Array.from(b); while (i < x.length && i < y.length && x[i] === y[i]) i++; return i; }
function commonSuffix(a, b) { let i = 0; const x = Array.from(a), y = Array.from(b); while (i < x.length && i < y.length && x[x.length - 1 - i] === y[y.length - 1 - i]) i++; return i; }
const len = s => Array.from(s || '').length;

/** A reading field can list alternatives ("あした/あす", "にち、じつ"). */
export function readingVariants(reading) {
  return String(reading || '').split(/[\/／、,・;；\s]+/).map(s => s.trim()).filter(Boolean);
}

function norm(w) {
  return {
    term: String(w.term_ja || w.term || w.word || '').trim(),
    reading: String(w.reading || w.kana || '').trim(),
    meaning: String(w.meaning_en || w.meaning || '').trim(),
    lesson: w.lesson ?? w.lesson_number ?? null
  };
}

/**
 * Pick `count` confusable distractor strings for one word.
 * @param {{term_ja|word, reading, lesson?, meaning_en?}} target
 * @param {'reading'|'writing'|'meaning'} kind  what the options are
 * @param {Array} universe all candidate words
 * @param {{count?:number, pool?:Array}} opts pool = same-lesson/chunk words (tie-break bonus)
 * @returns {string[]} unique, never equal to a correct answer
 */
export function pickDistractors(target, kind, universe = [], opts = {}) {
  const count = opts.count || 3;
  const t = norm(target);
  const words = (universe || []).map(norm).filter(w => w.term && !/[^\u3041-\u3096\u30a0-\u30ff\u3400-\u9fff々ー]/.test(w.term));
  const poolTerms = new Set((opts.pool || []).map(w => norm(w).term));
  const tKanji = kanjiChars(t.term);
  const tOkuri = okuriganaOf(t.term);
  const tEnd = tOkuri ? Array.from(tOkuri).pop() : ''; // hard rule: same final okurigana kana; longer shared endings score higher

  // Everything that is a correct answer for this prompt must never appear as a distractor.
  const forbidden = new Set();
  let scored = [];
  const push = (value, score, source) => {
    if (!value || forbidden.has(value)) return;
    scored.push({ value, score, tie: stableHash(t.term + '|' + value), source });
  };

  if (kind === 'reading') {
    const tVariants = readingVariants(t.reading);
    tVariants.forEach(v => forbidden.add(v));
    forbidden.add(t.reading);
    // other entries spelled the same way: their readings are valid alternatives
    for (const w of words) if (w.term === t.term) readingVariants(w.reading).forEach(v => forbidden.add(v));
    const R = tVariants[0] || t.reading;
    for (const w of words) {
      if (w.term === t.term) continue;
      for (const v of readingVariants(w.reading)) {
        if (forbidden.has(v)) continue;
        const endMiss = tEnd && !v.endsWith(tEnd);        // exam rule: same okurigana ending (relaxed only when too few candidates)
        if (/[^\u3041-\u3096ー]/.test(v)) continue;          // kana only
        let s = 0;
        const d = Math.abs(len(v) - len(R));
        if (d === 0) s += 6; else if (d === 1) s += 2; else s -= 4 * (d - 1);
        s += 8 * dice(v, R) + 1.5 * commonPrefix(v, R) + 1.5 * commonSuffix(v, R);
        if (!Array.from(v).some(ch => R.includes(ch))) s -= 5;  // no shared kana at all: not a sound-alike
        const wKanji = kanjiChars(w.term);
        const shared = wKanji.filter(k => tKanji.includes(k)).length;
        s += 4 * shared;                                     // same kanji, other reading
        if (tOkuri && okuriganaOf(w.term) === tOkuri) s += 2 * len(tOkuri);
        if (!tOkuri && okuriganaOf(w.term)) s -= 3;           // different word shape
        if (len(w.term) === len(t.term)) s += 1;
        if (poolTerms.has(w.term) || (t.lesson != null && w.lesson === t.lesson)) s += 1;
        push(v, endMiss ? s - 50 : s, 'word');
      }
    }
    // near-identical readings (voicing, long vowel, small kana, sokuon)
    for (const m of readingMutations(R, tOkuri)) {
      if (tEnd && !m.endsWith(tEnd)) continue;
      const d = Math.abs(len(m) - len(R));
      push(m, 9 + (d === 0 ? 1 : 0), 'mutation');
    }
  } else if (kind === 'writing') {
    forbidden.add(t.term);
    const tRead = readingVariants(t.reading).map(hira);
    if (len(t.term) === 1) {
      for (const [ch, info] of Object.entries(characterShapes)) if (info.readings.some(r => tRead.includes(hira(r)))) forbidden.add(ch);
    }
    // homophones are valid answers for a kana prompt
    for (const w of words) if (readingVariants(w.reading).some(v => tRead.includes(hira(v)))) forbidden.add(w.term);
    const tLen = len(t.term);
    for (const w of words) {
      if (forbidden.has(w.term)) continue;
      let s = 0;
      const d = Math.abs(len(w.term) - tLen);
      if (d === 0) s += 16; else s -= 12 * d;
      if (tLen === 1 && len(w.term) !== 1) s -= 100;
      const wKanji = kanjiChars(w.term);
      const shared = wKanji.filter(k => tKanji.includes(k)).length;
      s += 12 * shared;
      const aligned = Array.from(w.term).filter((c, i) => Array.from(t.term)[i] === c && isKanji(c)).length;
      s += 16 * aligned;
      let sim = 0;
      for (let i = 0; i < Math.min(len(w.term),tLen); i++) {
        const a = Array.from(t.term)[i], b = Array.from(w.term)[i];
        if (a !== b && isKanji(a) && isKanji(b)) sim += shapeSimilarity(a,b);
      }
      s += 2 * sim;
      if (okuriganaOf(w.term) === tOkuri) s += tOkuri ? 3 : 0.5; else if (tOkuri) s -= 3;
      s += 3 * dice(w.term, t.term) + commonPrefix(w.term, t.term) + commonSuffix(w.term, t.term);
      s += 3 * dice(w.reading, t.reading);                    // sounds similar too
      if (poolTerms.has(w.term) || (t.lesson != null && w.lesson === t.lesson)) s += 1;
      push(w.term, s, 'word');
    }
    // synthetic look-alike / sound-family swaps, as the real exam uses near-miss characters
    const chars = Array.from(t.term);
    chars.forEach((c, i) => {
      if (!isKanji(c)) return;
      const subs = shapeCandidates(c);
      for (const p of subs) {
        const a = chars.slice(); a[i] = p;
        const cand = a.join('');
        if (cand === t.term) continue;
        const real = words.some(w => w.term === cand);
        push(cand, 16 + 28 * (tKanji.length - 1) + 2 * shapeSimilarity(c,p) + (real ? 2 : 0), 'shape');
      }
    });
  } else {
    // meaning: English glosses of confusable words
    const tm = t.meaning.toLowerCase();
    forbidden.add(t.meaning);
    for (const w of words) if (w.term === t.term && w.meaning) forbidden.add(w.meaning);
    for (const w of words) {
      if (!w.meaning || w.term === t.term || w.meaning.toLowerCase() === tm) continue;
      let s = 0;
      const shared = kanjiChars(w.term).filter(k => tKanji.includes(k)).length;
      s += 5 * shared + 3 * dice(w.reading, t.reading);
      s -= Math.min(6, Math.abs(w.meaning.length - t.meaning.length) / 4);
      if (poolTerms.has(w.term) || (t.lesson != null && w.lesson === t.lesson)) s += 1;
      push(w.meaning, s, 'word');
    }
  }

  scored.sort((a, b) => b.score - a.score || a.tie - b.tie || (a.value < b.value ? -1 : 1));
  const out = [], seen = new Set();
  let synthetic = 0;
  for (const c of scored) {
    if (seen.has(c.value) || forbidden.has(c.value)) continue;
    if (kind !== 'writing' && c.source !== 'word') { if (synthetic >= 2) continue; synthetic++; }
    seen.add(c.value);
    out.push(c.value);
    if (out.length >= count) break;
  }
  return out;
}
