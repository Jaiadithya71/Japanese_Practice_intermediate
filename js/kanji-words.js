/* =======================================================
   NIHONGO INTERMEDIATE — js/kanji-words.js
   Kanji Word Drill Engine: Facets, Distractors & Mastery (WP-5)
   Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §1, §2, §7
   ======================================================= */

import { state as defaultState } from './state.js';
import { snapToNextDueSlot } from './time.js';

// Facet Constants
export const FACET_READING = 'KWR';
export const FACET_WRITING = 'KWW';
export const FACET_MEANING = 'KWM';

// Okurigana Regex: kanji followed by trailing hiragana
export const OKURIGANA_REGEX = /[\u4e00-\u9faf]+([ぁ-ん]+)$/;

// Standard High-Yield Phonetic Sound Families (doc 02 §2.4, doc 03 §5)
export const SOUND_FAMILIES = [
  ['反', '坂', '板', '返', '飯', '販'],
  ['寺', '持', '待', '時', '特', '詩', '侍'],
  ['方', '訪', '房', '防', '妨', '芳', '放'],
  ['兆', '挑', '逃', '跳', '眺', '桃'],
  ['同', '胴', '銅', '洞', '筒'],
  ['青', '清', '晴', '静', '精', '情'],
  ['分', '粉', '貧', '扮', '盆'],
  ['包', '抱', '胞', '砲', '泡', '飽'],
  ['交', '校', '郊', '効', '較', '絞'],
  ['化', '花', '貨', '靴', '華'],
  ['古', '固', '故', '苦', '枯', '湖', '居'],
  ['平', '評', '坪', '呼'],
  ['白', '百', '拍', '泊', '迫', '柏'],
  ['中', '仲', '沖', '忠'],
  ['主', '注', '柱', '住', '駐', '往'],
  ['成', '誠', '城', '盛'],
  ['申', '伸', '神', '重'],
  ['占', '点', '店', '粘'],
  ['台', '治', '始', '怠', '胎'],
  ['各', '格', '客', '落', '略', '閣', '路'],
  ['票', '標', '漂', '飄'],
  ['肖', '消', '削', '硝', '宵', '鞘'],
  ['侖', '論', '輪', '倫'],
  ['莫', '幕', '漠', '膜', '墓', '暮'],
  ['完', '院', '冠'],
  ['采', '採', '菜', '彩'],
  ['甫', '捕', '補', '舗', '浦'],
  ['奇', '寄', '騎', '椅', '崎'],
  ['建', '健', '鍵'],
  ['丁', '町', '頂', '灯', '打', '訂', '庁'],
  ['正', '政', '証', '症', '整', '征'],
  ['生', '性', '姓', '星', '醒', '牲'],
  ['義', '儀', '議', '犠'],
  ['令', '冷', '領', '命', '鈴', '零'],
  ['共', '供', '洪', '恭', '港'],
  ['岡', '綱', '鋼', '剛'],
  ['兼', '嫌', '謙', '廉'],
  ['公', '松', '訟', '頌'],
  ['合', '給', '答', '拾'],
  ['可', '河', '何', '苛', '荷', '歌'],
  ['原', '源', '願'],
  ['高', '稿', '豪', '橋']
];

// Pre-index sound families for fast lookup
const SOUND_FAMILY_MAP = new Map();
for (const family of SOUND_FAMILIES) {
  for (const char of family) {
    if (!SOUND_FAMILY_MAP.has(char)) {
      SOUND_FAMILY_MAP.set(char, new Set());
    }
    for (const partner of family) {
      if (partner !== char) {
        SOUND_FAMILY_MAP.get(char).add(partner);
      }
    }
  }
}

// Kana voicing pair mapping for procedural mutation
const VOICING_MAP = {
  'か': 'が', 'が': 'か', 'き': 'ぎ', 'ぎ': 'き', 'く': 'ぐ', 'ぐ': 'く', 'け': 'げ', 'げ': 'け', 'こ': 'ご', 'ご': 'こ',
  'さ': 'ざ', 'ざ': 'さ', 'し': 'じ', 'じ': 'し', 'す': 'ず', 'ず': 'す', 'せ': 'ぜ', 'ぜ': 'せ', 'そ': 'ぞ', 'ぞ': 'そ',
  'た': 'だ', 'だ': 'た', 'ち': 'ぢ', 'ぢ': 'ち', 'つ': 'づ', 'づ': 'つ', 'て': 'で', 'で': 'て', 'と': 'ど', 'ど': 'と',
  'は': 'ば', 'ば': 'は', 'ひ': 'び', 'び': 'ひ', 'ふ': 'ぶ', 'ぶ': 'ふ', 'へ': 'べ', 'べ': 'へ', 'ほ': 'ぼ', 'ぼ': 'ほ',
  'ぱ': 'ば'
};

/**
 * Returns facet key formatted per specification (doc 02 §1.1):
 * KWR:<term>, KWW:<term>, KWM:<term>
 */
export function getFacetKey(facet, term) {
  if (!facet || !term) return '';
  const cleanTerm = typeof term === 'object' ? (term.term_ja || term.term || term.word || '') : String(term).trim();
  let prefix = facet.toUpperCase();
  if (prefix === 'READING' || prefix === 'R') prefix = FACET_READING;
  else if (prefix === 'WRITING' || prefix === 'W') prefix = FACET_WRITING;
  else if (prefix === 'MEANING' || prefix === 'M') prefix = FACET_MEANING;
  return `${prefix}:${cleanTerm}`;
}

/**
 * Extracts okurigana suffix if target term ends in okurigana.
 * Example: '辺り' -> 'り', '割る' -> 'る', '市場' -> null
 */
export function getOkurigana(termJa) {
  if (!termJa || typeof termJa !== 'string') return null;
  const match = termJa.match(OKURIGANA_REGEX);
  return match ? match[1] : null;
}

/**
 * Normalizes input word list into array of uniform word records.
 */
function normalizeWordList(input) {
  if (!input) return [];
  if (Array.isArray(input)) {
    return input.map(item => {
      if (typeof item === 'string') {
        return { term_ja: item, term: item, reading: '', meaning_en: '' };
      }
      return {
        ...item,
        term_ja: item.term_ja || item.term || item.word || '',
        reading: item.reading || item.kana || '',
        meaning_en: item.meaning_en || item.meaning || ''
      };
    }).filter(w => w.term_ja);
  }
  if (typeof input === 'object') {
    return Object.values(input).map(item => {
      if (typeof item === 'string') {
        return { term_ja: item, term: item, reading: '', meaning_en: '' };
      }
      return {
        ...item,
        term_ja: item.term_ja || item.term || item.word || '',
        reading: item.reading || item.kana || '',
        meaning_en: item.meaning_en || item.meaning || ''
      };
    }).filter(w => w.term_ja);
  }
  return [];
}

/**
 * Extracts all unique kanji characters from a Japanese text string.
 */
export function extractKanjiChars(text) {
  if (!text || typeof text !== 'string') return [];
  const matches = text.match(/[\u4e00-\u9faf]/g) || [];
  return Array.from(new Set(matches));
}

/**
 * Procedurally generates reading mutations for voicing & length traps (doc 02 §2.4 Rule 4).
 * If reqOkurigana is specified, all mutations strictly preserve the trailing okurigana!
 */
function generateReadingMutations(reading, reqOkurigana) {
  const mutations = new Set();
  if (!reading) return [];

  if (reqOkurigana && reading.endsWith(reqOkurigana)) {
    const stem = reading.slice(0, reading.length - reqOkurigana.length);
    if (!stem) return [];

    // 1. Voicing mutations on stem characters
    for (let i = 0; i < stem.length; i++) {
      const char = stem[i];
      if (VOICING_MAP[char]) {
        const mutatedStem = stem.slice(0, i) + VOICING_MAP[char] + stem.slice(i + 1);
        mutations.add(mutatedStem + reqOkurigana);
      }
    }

    // 2. Length/Chouon mutations on stem (within ±1 length of reading)
    if (stem.includes('っ')) {
      mutations.add(stem.replace('っ', '') + reqOkurigana);
    } else if (stem.length >= 2) {
      mutations.add(stem[0] + 'っ' + stem.slice(1) + reqOkurigana);
    }
    if (stem.includes('う')) {
      mutations.add(stem.replace('う', '') + reqOkurigana);
    } else if (stem.includes('ー')) {
      mutations.add(stem.replace('ー', '') + reqOkurigana);
    } else if (stem.length <= 3) {
      mutations.add(stem + 'う' + reqOkurigana);
    }

    // 3. Fallback vowel shift variants for small stems
    const vowelReplacements = ['お', 'い', 'あ', 'え', 'う', 'ま', 'み', 'り', 'し', 'か', 'た'];
    for (const vr of vowelReplacements) {
      if (mutations.size >= 6) break;
      if (stem[0] !== vr) {
        const altStem = vr + (stem.slice(1) || '');
        if (altStem !== stem) {
          mutations.add(altStem + reqOkurigana);
        }
      }
    }
  } else {
    // Non-okurigana compound reading mutations
    // 1. Voicing mutations
    for (let i = 0; i < reading.length; i++) {
      const char = reading[i];
      if (VOICING_MAP[char]) {
        const mut = reading.slice(0, i) + VOICING_MAP[char] + reading.slice(i + 1);
        mutations.add(mut);
      }
    }

    // 2. Chouon / length traps (e.g. しょう -> じょう / しょ)
    if (reading.endsWith('う') && reading.length > 2) {
      mutations.add(reading.slice(0, -1)); // short vowel
    } else if (reading.endsWith('ー') && reading.length > 2) {
      mutations.add(reading.slice(0, -1));
    } else if (reading.length <= 4) {
      mutations.add(reading + 'う'); // long vowel
    }

    if (reading.includes('っ')) {
      mutations.add(reading.replace('っ', ''));
    } else if (reading.length >= 3) {
      mutations.add(reading.slice(0, 1) + 'っ' + reading.slice(2));
    }

    // 3. Common sound confusion endings
    if (reading.endsWith('ん') && reading.length >= 3) {
      mutations.add(reading.slice(0, -1) + 'う');
    }
    if (reading.endsWith('つ') && reading.length >= 3) {
      mutations.add(reading.slice(0, -1) + 'ち');
    }
  }

  // Filter out exact duplicate of original reading
  mutations.delete(reading);
  return Array.from(mutations);
}

/**
 * Generates 3 high-quality distractors for Reading (KWR) or Writing (KWW).
 * doc 02 §2.4:
 * For Reading:
 *   1. Okurigana rule: if target ends in okurigana (regex /[\u4e00-\u9faf]+([ぁ-ん]+)$/),
 *      all distractors MUST end with the same okurigana!
 *   2. Length within ±1 kana of correct reading.
 *   3. Same-kanji confusion first (different on/kun reading).
 *   4. Voicing/chouon mutations if pool is small.
 *   5. Fall back to same lesson, then any lesson.
 * For Writing:
 *   1. Prefer words sharing one kanji or sound-family kanji.
 *   2. Words with same kana length from same lesson.
 *   3. Any target word.
 */
export function generateDistractors(targetTerm, facet, pool = [], allWords = []) {
  const normalizedFacet = (facet || 'KWR').toUpperCase();
  const isReading = normalizedFacet === 'KWR' || normalizedFacet === 'READING';
  const isWriting = normalizedFacet === 'KWW' || normalizedFacet === 'WRITING';

  // Extract target word details
  let termJa = '';
  let targetReading = '';
  let targetLesson = null;

  if (typeof targetTerm === 'object' && targetTerm !== null) {
    termJa = (targetTerm.term_ja || targetTerm.term || targetTerm.word || '').trim();
    targetReading = (targetTerm.reading || targetTerm.kana || '').trim();
    targetLesson = targetTerm.lesson || targetTerm.lesson_number || null;
  } else {
    termJa = String(targetTerm || '').trim();
  }

  const poolList = normalizeWordList(pool);
  const allList = normalizeWordList(allWords);

  // Fallback lookup from defaultState if empty
  const statePool = poolList.length > 0 ? poolList : (
    (typeof defaultState !== 'undefined' && defaultState?.idx?.words)
      ? normalizeWordList(defaultState.idx.words)
      : []
  );
  const fullUniverse = allList.length > 0 ? allList : statePool;

  // Resolve reading if missing
  if (!targetReading) {
    const match = fullUniverse.find(w => w.term_ja === termJa);
    if (match && match.reading) {
      targetReading = match.reading.trim();
      if (!targetLesson) targetLesson = match.lesson;
    }
  }

  const targetKanji = extractKanjiChars(termJa);
  const distractors = [];
  const seen = new Set();

  if (isReading) {
    // ==========================================
    // READING DISTRACTORS (Kanji -> Kana)
    // ==========================================
    seen.add(targetReading);

    const reqOkurigana = getOkurigana(termJa);
    const targetLen = targetReading.length;

    // Helper: validate reading candidate against okurigana & length rule
    const isValidReadingCandidate = (reading, enforceLength = true) => {
      if (!reading || reading === targetReading || seen.has(reading)) return false;
      if (reqOkurigana && !reading.endsWith(reqOkurigana)) return false;
      if (enforceLength && Math.abs(reading.length - targetLen) > 1) return false;
      return true;
    };

    // Stage 1: Same-kanji confusion (words sharing any target kanji)
    const sameKanjiWords = fullUniverse.filter(w => {
      if (!w.term_ja || w.term_ja === termJa) return false;
      const wKanji = extractKanjiChars(w.term_ja);
      return wKanji.some(k => targetKanji.includes(k));
    });

    for (const w of sameKanjiWords) {
      if (distractors.length >= 3) break;
      if (isValidReadingCandidate(w.reading, true)) {
        distractors.push(w.reading);
        seen.add(w.reading);
      }
    }

    // Stage 2: Pool words (same chunk/lesson) matching okurigana and length ±1
    if (distractors.length < 3) {
      for (const w of poolList) {
        if (distractors.length >= 3) break;
        if (isValidReadingCandidate(w.reading, true)) {
          distractors.push(w.reading);
          seen.add(w.reading);
        }
      }
    }

    // Stage 3: Full universe words matching okurigana and length ±1
    if (distractors.length < 3) {
      for (const w of fullUniverse) {
        if (distractors.length >= 3) break;
        if (isValidReadingCandidate(w.reading, true)) {
          distractors.push(w.reading);
          seen.add(w.reading);
        }
      }
    }

    // Stage 4: Voicing / Chouon mutations (strictly obeying okurigana if present)
    if (distractors.length < 3 && targetReading) {
      const mutations = generateReadingMutations(targetReading, reqOkurigana);
      for (const mut of mutations) {
        if (distractors.length >= 3) break;
        if (isValidReadingCandidate(mut, true)) {
          distractors.push(mut);
          seen.add(mut);
        }
      }
    }

    // Stage 5: Relaxed length constraint on universe words (must still respect okurigana rule!)
    if (distractors.length < 3) {
      for (const w of fullUniverse) {
        if (distractors.length >= 3) break;
        if (isValidReadingCandidate(w.reading, false)) {
          distractors.push(w.reading);
          seen.add(w.reading);
        }
      }
    }

    // Stage 6: Procedural synthetic fallback (never violates okurigana!)
    if (distractors.length < 3) {
      const syntheticStems = ['あさ', 'ひる', 'よる', 'やま', 'かわ', 'ひと', 'もの', 'こと', 'みち', 'はな', 'もり', 'そら'];
      for (const stem of syntheticStems) {
        if (distractors.length >= 3) break;
        const candidate = reqOkurigana ? (stem + reqOkurigana) : (stem + 'い');
        if (candidate !== targetReading && !seen.has(candidate)) {
          distractors.push(candidate);
          seen.add(candidate);
        }
      }
    }

    return distractors.slice(0, 3);
  } else if (isWriting) {
    // ==========================================
    // WRITING DISTRACTORS (Kana -> Kanji)
    // ==========================================
    seen.add(termJa);

    // Build sound-family partners for all kanji in target word
    const soundPartners = new Set();
    for (const k of targetKanji) {
      const partners = SOUND_FAMILY_MAP.get(k);
      if (partners) {
        for (const p of partners) soundPartners.add(p);
      }
    }

    // Stage 1: Words sharing one kanji with target, or sound-family kanji
    const sharedOrSoundWords = fullUniverse.filter(w => {
      if (!w.term_ja || w.term_ja === termJa || seen.has(w.term_ja)) return false;
      const wKanji = extractKanjiChars(w.term_ja);
      const sharesKanji = wKanji.some(k => targetKanji.includes(k));
      const hasSoundFamily = wKanji.some(k => soundPartners.has(k));
      return sharesKanji || hasSoundFamily;
    });

    for (const w of sharedOrSoundWords) {
      if (distractors.length >= 3) break;
      distractors.push(w.term_ja);
      seen.add(w.term_ja);
    }

    // Stage 2: Words from same lesson with similar reading length
    if (distractors.length < 3 && targetLesson) {
      const sameLessonWords = fullUniverse.filter(w => {
        if (!w.term_ja || seen.has(w.term_ja)) return false;
        return (w.lesson === targetLesson) && Math.abs((w.reading || '').length - targetReading.length) <= 1;
      });
      for (const w of sameLessonWords) {
        if (distractors.length >= 3) break;
        distractors.push(w.term_ja);
        seen.add(w.term_ja);
      }
    }

    // Stage 3: Pool words
    if (distractors.length < 3) {
      for (const w of poolList) {
        if (distractors.length >= 3) break;
        if (w.term_ja && !seen.has(w.term_ja)) {
          distractors.push(w.term_ja);
          seen.add(w.term_ja);
        }
      }
    }

    // Stage 4: Any target word in full universe
    if (distractors.length < 3) {
      for (const w of fullUniverse) {
        if (distractors.length >= 3) break;
        if (w.term_ja && !seen.has(w.term_ja)) {
          distractors.push(w.term_ja);
          seen.add(w.term_ja);
        }
      }
    }

    // Stage 5: Procedural kanji substitution fallback using sound family
    if (distractors.length < 3 && targetKanji.length > 0) {
      for (const k of targetKanji) {
        if (distractors.length >= 3) break;
        const partners = Array.from(SOUND_FAMILY_MAP.get(k) || []);
        for (const partner of partners) {
          if (distractors.length >= 3) break;
          const candidate = termJa.replace(k, partner);
          if (candidate !== termJa && !seen.has(candidate)) {
            distractors.push(candidate);
            seen.add(candidate);
          }
        }
      }
    }

    return distractors.slice(0, 3);
  }

  // Meaning or fallback
  return [];
}

/**
 * Builds breakdown strip pills for any kanji in a word (doc 02 §2.3).
 * Pill: { kanji: '市', meaning: 'City, Market' }
 */
export function getKanjiBreakdownPills(text, db = null) {
  if (!text) return [];
  const kanjiChars = extractKanjiChars(text);
  const kanjiDB = db || (typeof defaultState !== 'undefined' ? defaultState?.kanjiDB : null) || {};
  const review300 = (typeof defaultState !== 'undefined' ? defaultState?.kanjiReview300 : null) || [];

  return kanjiChars.map(char => {
    let meaning = '';
    const entry = kanjiDB[char];
    if (entry) {
      if (Array.isArray(entry.meanings) && entry.meanings.length > 0) {
        meaning = entry.meanings[0];
      } else if (entry.meaning_en) {
        meaning = entry.meaning_en;
      } else if (Array.isArray(entry.words) && entry.words.length > 0) {
        meaning = entry.words[0].meaning_en || '';
      }
    }
    if (!meaning) {
      const rMatch = review300.find(r => r.kanji === char);
      if (rMatch && rMatch.meaning) meaning = rMatch.meaning;
    }
    return {
      kanji: char,
      meaning: meaning || ''
    };
  });
}

/**
 * Builds a structured word card for SRS or runner stages (doc 02 §2.3).
 */
export function buildWordCard(wordData, facet = 'KWR', pool = [], allWords = []) {
  if (!wordData) return null;

  const termJa = (wordData.term_ja || wordData.term || wordData.word || '').trim();
  const reading = (wordData.reading || wordData.kana || '').trim();
  const meaningEn = (wordData.meaning_en || wordData.meaning || '').trim();
  const meaningZh = wordData.meaning_zh || '';
  const rubyHtml = wordData.ruby_html || `<ruby>${termJa}<rt>${reading}</rt></ruby>`;

  const normalizedFacet = (facet || 'KWR').toUpperCase();
  const key = getFacetKey(normalizedFacet, termJa);

  const distractors = generateDistractors(wordData, normalizedFacet, pool, allWords);
  const correctAnswerText = (normalizedFacet === 'KWR' || normalizedFacet === 'READING')
    ? reading
    : termJa;

  // Build 4 MCQ options and shuffle
  const rawOptions = [
    { text: correctAnswerText, isCorrect: true },
    ...distractors.map(d => ({ text: d, isCorrect: false }))
  ];

  // Stable pseudo-random shuffle for card options
  const options = rawOptions.sort(() => Math.random() - 0.5);
  const correctIndex = options.findIndex(opt => opt.isCorrect);

  const breakdown = getKanjiBreakdownPills(termJa);
  const context = wordData.context || null;

  let clozeJa = null;
  if (context && context.ja) {
    if (normalizedFacet === 'KWW' || normalizedFacet === 'WRITING') {
      clozeJa = context.ja.replace(termJa, '（　）');
    } else {
      clozeJa = context.ja.replace(termJa, `<span class="target-underline">${termJa}</span>`);
    }
  }

  // Construct structured card
  const card = {
    key,
    type: 'kanji_word',
    facet: normalizedFacet,
    term: termJa,
    term_ja: termJa,
    reading,
    meaning_en: meaningEn,
    meaning_zh: meaningZh,
    ruby_html: rubyHtml,
    lesson: wordData.lesson || wordData.lesson_number || 1,
    part: wordData.part || 1,
    homeKanji: wordData.homeKanji || (extractKanjiChars(termJa)[0] || null),
    kanjiRefs: wordData.kanjiRefs || extractKanjiChars(termJa),
    vocabId: wordData.vocabId || null,
    context: context ? { ...context, clozeJa } : null,
    breakdown,
    distractors,
    options,
    correctIndex,
    isTarget: Boolean(wordData.isTarget ?? wordData.is_target ?? true),
    banner: normalizedFacet === 'KWR'
      ? '問題：２ (漢字 → 正しい 読み方)'
      : (normalizedFacet === 'KWW' ? '問題：１ (ひらがな → 正しい 漢字)' : '漢字 → 意味'),
    direction: normalizedFacet === 'KWR'
      ? 'ja-kana'
      : (normalizedFacet === 'KWW' ? 'kana-ja' : 'ja-en'),
    front: {
      // Reading front MUST be kanji-only, NO ruby (doc 02 §2.3)
      term: termJa,
      reading: normalizedFacet === 'KWW' ? reading : null,
      subPrompt: normalizedFacet === 'KWW' ? `[ ${meaningEn} ]` : null,
      banner: normalizedFacet === 'KWR'
        ? '問題：２ (漢字 → 正しい 読み方)'
        : (normalizedFacet === 'KWW' ? '問題：１ (ひらがな → 正しい 漢字)' : '漢字 → 意味')
    },
    back: {
      term: termJa,
      reading,
      ruby_html: rubyHtml,
      meaning_en: meaningEn,
      breakdown,
      context
    }
  };

  return card;
}

/**
 * Checks if a facet is unlocked for a given term (doc 02 §1.1):
 * - KWR: unlocked at learn time.
 * - KWW: unlocked when KWR has reps >= 2.
 * - KWM: unlocked at learn time if not shared with vocab DB.
 */
export function isFacetUnlocked(term, facet, stats = {}, wordData = null) {
  if (!term || !facet) return false;

  const cleanTerm = typeof term === 'object' ? (term.term_ja || term.term || '') : String(term).trim();
  const normalizedFacet = facet.toUpperCase();

  // Reading facet unlocks at learn time
  if (normalizedFacet === 'KWR' || normalizedFacet === 'READING') {
    return true;
  }

  // Writing facet unlocks when KWR has reps >= 2
  if (normalizedFacet === 'KWW' || normalizedFacet === 'WRITING') {
    const kwrKey = `KWR:${cleanTerm}`;
    const kwrStats = stats ? stats[kwrKey] : null;
    return Boolean(kwrStats && (kwrStats.reps || 0) >= 2);
  }

  // Meaning facet unlocks at learn time ONLY if NOT in vocab DB
  if (normalizedFacet === 'KWM' || normalizedFacet === 'MEANING') {
    // 1. Check explicit wordData
    if (wordData && wordData.vocabId) {
      return false; // shared with vocab DB
    }

    // 2. Check state.idx.words if available
    if (typeof defaultState !== 'undefined' && defaultState?.idx?.words) {
      const idxEntry = defaultState.idx.words[cleanTerm];
      if (idxEntry && idxEntry.vocabId) {
        return false;
      }
    }

    // 3. Check vocabDB overlap
    if (typeof defaultState !== 'undefined' && defaultState?.vocabDB) {
      for (const chId in defaultState.vocabDB) {
        const list = defaultState.vocabDB[chId];
        if (Array.isArray(list) && list.some(v => v.kanji === cleanTerm || v.word === cleanTerm)) {
          return false;
        }
      }
    }

    return true;
  }

  return false;
}

/**
 * Calculates Kanji Mastery score and tile status from active word facets (doc 02 §7.1):
 * - score(f) = 0 unseen; 0.3 learning/relearning; 0.7 review with interval >= 6; 1.0 mastered (reps>=4, interval>=21, weight<=0.8).
 * - kanjiMastery(k) = mean( score(f) for f in F(k) )
 * - Tile status:
 *     0 -> 'grey' (unseen)
 *     < 0.4 -> 'amber' (learning)
 *     0.4–0.8 -> 'blue' (solid)
 *     >= 0.8 -> 'green' (mastered)
 * - hasLeech: true if any facet has leech || lapses >= 5 || weight >= 1.8 (red dot)
 */
export function calculateKanjiMastery(kanjiChar, wordsForKanji = [], stats = {}) {
  const targetWords = (wordsForKanji || []).filter(w => {
    if (typeof w === 'string') return true;
    return w.isTarget !== false && w.is_target !== false;
  });

  const wordTerms = targetWords.map(w => {
    return typeof w === 'object' ? (w.term_ja || w.term || '') : String(w);
  }).filter(Boolean);

  if (wordTerms.length === 0) {
    return {
      kanji: kanjiChar,
      score: 0.0,
      mean: 0.0,
      status: 'grey',
      hasLeech: false,
      totalFacets: 0,
      activeFacets: []
    };
  }

  const activeFacets = [];
  let sumScores = 0;
  let hasLeech = false;

  for (const term of wordTerms) {
    // 1. Reading facet
    const kwrKey = `KWR:${term}`;
    activeFacets.push(kwrKey);

    // 2. Writing facet
    const kwwKey = `KWW:${term}`;
    activeFacets.push(kwwKey);

    // 3. Meaning facet (KWM if non-vocab, or V: if vocab)
    const matchingWord = targetWords.find(w => (w.term_ja || w.term) === term);
    const vocabId = (matchingWord && typeof matchingWord === 'object') ? matchingWord.vocabId : null;
    if (vocabId) {
      activeFacets.push(`V:${vocabId}`);
    } else {
      activeFacets.push(`KWM:${term}`);
    }
  }

  for (const fKey of activeFacets) {
    const s = stats ? stats[fKey] : null;

    if (!s || ((s.reps || 0) === 0 && (s.correct || 0) === 0 && (s.incorrect || 0) === 0)) {
      // unseen -> 0.0
      sumScores += 0.0;
    } else {
      const reps = s.reps || 0;
      const interval = s.interval || 0;
      const weight = typeof s.weight === 'number' ? s.weight : 1.0;
      const lapses = s.lapses || 0;

      // Leech / Hard red dot check (doc 02 §7.1)
      if (s.leech || lapses >= 5 || weight >= 1.8 || s.isHard) {
        hasLeech = true;
      }

      // Mastered check (doc 02 §3: reps >= 4 and interval >= 21d and weight <= 0.8)
      if (reps >= 4 && interval >= 21 && weight <= 0.8) {
        sumScores += 1.0;
      } else if (interval >= 6) {
        // Review with interval >= 6
        sumScores += 0.7;
      } else {
        // Learning / Relearning
        sumScores += 0.3;
      }
    }
  }

  const mean = activeFacets.length > 0 ? (sumScores / activeFacets.length) : 0.0;
  const roundedScore = Math.round(mean * 100) / 100;

  // Determine tile status colour (doc 02 §7.1)
  let status = 'grey';
  if (roundedScore === 0) {
    status = 'grey';
  } else if (roundedScore < 0.4) {
    status = 'amber';
  } else if (roundedScore < 0.8) {
    status = 'blue';
  } else {
    status = 'green';
  }

  return {
    kanji: kanjiChar,
    score: roundedScore,
    mean: roundedScore,
    status,
    hasLeech,
    totalFacets: activeFacets.length,
    activeFacets
  };
}

export const N3KanjiWords = {
  FACET_READING,
  FACET_WRITING,
  FACET_MEANING,
  OKURIGANA_REGEX,
  SOUND_FAMILIES,
  getFacetKey,
  getOkurigana,
  extractKanjiChars,
  generateDistractors,
  getKanjiBreakdownPills,
  buildWordCard,
  isFacetUnlocked,
  calculateKanjiMastery
};

if (typeof window !== 'undefined') {
  window.N3KanjiWords = N3KanjiWords;
}

export default N3KanjiWords;
