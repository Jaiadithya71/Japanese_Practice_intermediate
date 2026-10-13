/* =======================================================
   NIHONGO INTERMEDIATE — js/grammar-srs.js
   Grammar Revision Engine, Star Arranger, Contrast & Clusters (WP-9)
   Reference: n3_dev_handoff/02_MEMORY_ENGINE_SPEC.md §9 and WP-9
   ======================================================= */

import { SLOW_MS } from './config.js';
import { state as defaultState } from './state.js';

// --- Card Facet & Type Constants ---
export const FACET_DECISION = 'GD';
export const FACET_STAR     = 'GS';
export const FACET_TEXT     = 'GT';
export const FACET_CONTRAST = 'GC';

// 9 Core Grammar Confusion Clusters (doc 02 §9.6, doc 03 §4.6)
export const DEFAULT_CLUSTERS = [
  {
    id: 'time',
    name_en: 'Time & Timing',
    name_ja: '時間・時期',
    patterns: ['P1-1', 'P1-2', 'P1-3', 'P1-4', 'P1-7', 'P1-9', 'P2-74', 'P2-75', 'P2-76']
  },
  {
    id: 'cause',
    name_en: 'Cause & Reason',
    name_ja: '原因・理由',
    patterns: ['P1-19', 'P1-20', 'P1-21', 'P1-22', 'P1-23', 'P2-71', 'P2-72', 'P3-82', 'P3-83']
  },
  {
    id: 'contrast',
    name_en: 'Contrast & Comparison',
    name_ja: '対比・逆接',
    patterns: ['P1-14', 'P1-15', 'P1-16', 'P1-17', 'P1-18', 'P1-38', 'P2-54', 'P2-55']
  },
  {
    id: 'inability-compulsion',
    name_en: 'Obligation & Impossibility',
    name_ja: '義務・不可・禁止・部分否定',
    patterns: ['P1-34', 'P1-35', 'P1-36', 'P1-37', 'P1-42', 'P1-43', 'P1-44', 'P1-45', 'P2-59']
  },
  {
    id: 'purpose-intent',
    name_en: 'Purpose, Volition & Desires',
    name_ja: '目的・意向・希望・働きかけ',
    patterns: ['P1-39', 'P1-40', 'P1-41', 'P1-46', 'P1-47', 'P1-48', 'P1-49', 'P2-60', 'P2-61']
  },
  {
    id: 'condition',
    name_en: 'Condition & Hypothesis',
    name_ja: '条件・仮定・反実仮想',
    patterns: ['P1-5', 'P1-6', 'P1-8', 'P1-24', 'P1-25', 'P1-26', 'P1-27', 'P1-28', 'P2-56', 'P2-57', 'P2-62']
  },
  {
    id: 'degree-limit',
    name_en: 'Degree & Limit',
    name_ja: '程度・限界・最高',
    patterns: ['P1-10', 'P1-11', 'P1-12', 'P1-13', 'P2-58']
  },
  {
    id: 'viewpoint-attitude',
    name_en: 'Viewpoint, Attitude & Transmission',
    name_ja: '視点・伝聞・敬語',
    patterns: ['P1-29', 'P1-30', 'P1-31', 'P1-32', 'P1-33', 'P1-50', 'P1-51', 'P1-52', 'P1-53', 'P2-65', 'P2-77', 'P2-78', 'P2-79']
  },
  {
    id: 'form-other',
    name_en: 'Sentence Forms & Cohesion',
    name_ja: '文型・構文・文の対応',
    patterns: ['P2-63', 'P2-64', 'P2-66', 'P2-67', 'P2-68', 'P2-69', 'P2-70', 'P2-73', 'P3-80', 'P3-81']
  }
];

// Module-level cache for grammar patterns index & datasets
let cachedGrammarIndex = null;
let cachedDrillTags = null;
let cachedClusters = null;

// =======================================================
// 1. COMPOSITE KEYS & KEY FORMATTING (doc 02 §1.1, §9.4)
// =======================================================

/**
 * Generates canonical SRS item key for grammar cards:
 * - GD:<part>:<sec>:<qid>
 * - GS:<part>:<sec>:<qid>
 * - GT:<passage_id>:<qid> (or GT:<part>:<sec>:<qid>)
 * - GC:<patternId>:<variantIndex>
 *
 * @param {string} facet - 'GD' | 'GS' | 'GT' | 'GC'
 * @param {Object} params
 * @returns {string}
 */
export function formatGrammarKey(facet, params = {}) {
  const f = (facet || '').toUpperCase();
  const part = params.part || params.partId || 'p1a';
  const sec = params.sec || params.sectionId || params.section || '1';
  const qid = params.qid || params.question_id || params.id;

  if (f === 'GS' || f === 'GRAMMAR_STAR') {
    return `GS:${part}:${sec}:${qid}`;
  }
  if (f === 'GT' || f === 'GRAMMAR_TEXT') {
    if (params.passage_id || params.passageId) {
      return `GT:${params.passage_id || params.passageId}:${qid}`;
    }
    return `GT:${part}:${sec}:${qid}`;
  }
  if (f === 'GC' || f === 'GRAMMAR_CONTRAST') {
    const pid = params.patternId || params.pattern_id || part;
    const variant = params.variantIndex || params.variant || 1;
    return `GC:${pid}:${variant}`;
  }

  // Default: GD (Grammar Decision / fill)
  return `GD:${part}:${sec}:${qid}`;
}

/**
 * Parses canonical grammar key into structured components.
 *
 * @param {string} key - e.g. 'GD:p1a:1:101', 'GS:p2:1:701', 'GT:301:30101', 'GT:p3:1:30101'
 * @returns {Object} { facet, part, sec, qid, passage_id, patternId, variantIndex }
 */
export function parseGrammarKey(key) {
  if (!key || typeof key !== 'string') return null;
  const parts = key.split(':');
  const facet = parts[0];

  if (facet === 'GD' || facet === 'GS') {
    return {
      facet,
      part: parts[1] || '',
      sec: parts[2] || '',
      qid: parts[3] ? (isNaN(Number(parts[3])) ? parts[3] : Number(parts[3])) : '',
      compositeKey: `${parts[1] || ''}:${parts[2] || ''}:${parts[3] || ''}`
    };
  }

  if (facet === 'GT') {
    if (parts.length === 3) {
      // GT:<passage_id>:<qid>
      return {
        facet,
        passage_id: isNaN(Number(parts[1])) ? parts[1] : Number(parts[1]),
        qid: parts[2] ? (isNaN(Number(parts[2])) ? parts[2] : Number(parts[2])) : '',
        part: 'p3',
        sec: parts[1] || '1',
        compositeKey: `p3:${parts[1] || '1'}:${parts[2] || ''}`
      };
    } else if (parts.length >= 4) {
      // GT:<part>:<sec>:<qid>
      return {
        facet,
        part: parts[1] || '',
        sec: parts[2] || '',
        qid: parts[3] ? (isNaN(Number(parts[3])) ? parts[3] : Number(parts[3])) : '',
        compositeKey: `${parts[1] || ''}:${parts[2] || ''}:${parts[3] || ''}`
      };
    }
  }

  if (facet === 'GC') {
    return {
      facet,
      patternId: parts[1] || '',
      variantIndex: parts[2] ? Number(parts[2]) : 1
    };
  }

  return { facet, raw: key };
}

/**
 * Creates composite key used in drill_tags.json (<part>:<sec>:<qid>).
 */
export function toCompositeKey(part, sec, qid) {
  return `${part}:${sec}:${qid}`;
}

// =======================================================
// 2. CARD OBJECT BUILDERS (doc 02 §9.4)
// =======================================================

/**
 * Constructs a standardized grammar card object from raw drill data and metadata.
 *
 * @param {Object} drill - Raw question object from JSON
 * @param {Object} meta - Metadata { part, sec, passage_id, tags }
 * @returns {Object} Unified card object
 */
export function buildGrammarCard(drill, meta = {}) {
  if (!drill) {
    throw new Error('buildGrammarCard: drill is required');
  }
  const part = meta.part || meta.partId || 'p1a';
  const sec = String(meta.sec || meta.section || meta.section_number || '1');
  const qid = drill.question_id !== undefined ? drill.question_id : (meta.qid || drill.id);
  const qType = drill.question_type || meta.type || 'multiple_choice';

  // Determine facet and type
  let facet = FACET_DECISION;
  let cardType = 'grammar_decision';

  if (qType === 'star_arrangement' || meta.facet === FACET_STAR) {
    facet = FACET_STAR;
    cardType = 'grammar_star';
  } else if (part === 'p3' || meta.passage_id || meta.facet === FACET_TEXT) {
    facet = FACET_TEXT;
    cardType = 'grammar_text';
  }

  const compositeKey = toCompositeKey(part, sec, qid);
  const key = formatGrammarKey(facet, {
    part,
    sec,
    qid,
    passage_id: meta.passage_id || drill.passage_id
  });

  const tags = meta.tags || (cachedDrillTags ? cachedDrillTags[compositeKey] : null) || {};
  const patterns = Array.isArray(tags.patterns) ? tags.patterns : (meta.patterns || []);
  const cluster = tags.cluster || meta.cluster || null;
  const rivals = Array.isArray(tags.rivals) ? tags.rivals : (meta.rivals || []);

  const card = {
    key,
    compositeKey,
    type: cardType,
    facet,
    book: 'grammar',
    part,
    sec,
    qid,
    question_type: qType,
    prompt: drill.prompt || '',
    options: drill.options || [],
    correct_answer: drill.correct_answer !== undefined ? drill.correct_answer : null,
    explanation_ja: drill.explanation_ja || '',
    explanation_en: drill.explanation_en || '',
    patterns,
    primaryPattern: patterns[0] || null,
    cluster,
    rivals,
    confidence: tags.confidence || 'auto'
  };

  // Star arrangement specific enrichment (doc 02 §9.5)
  if (facet === FACET_STAR) {
    const rawOptions = drill.options || [];
    const correctOrder = Array.isArray(drill.correct_order)
      ? drill.correct_order.map(Number)
      : [1, 2, 3, 4];

    // Derive 0-indexed slot index of ★
    let starSlotIndex = -1;
    if (drill.correct_answer !== undefined) {
      starSlotIndex = correctOrder.indexOf(Number(drill.correct_answer));
    }
    if (starSlotIndex === -1 && typeof drill.star_position === 'number') {
      starSlotIndex = (drill.star_position >= 0 && drill.star_position < 4)
        ? drill.star_position
        : drill.star_position - 1;
    }
    if (starSlotIndex < 0 || starSlotIndex >= 4) {
      starSlotIndex = 2; // default 3rd position
    }

    card.correct_order = correctOrder;
    card.star_slot_index = starSlotIndex;
    card.star_position = starSlotIndex;
    card.star_answer = correctOrder[starSlotIndex];
    card.full_sentence = drill.full_sentence || '';
    card.full_sentence_en = drill.full_sentence_en || '';

    // Parsed fragment tiles with id (1-4) and cleaned text
    card.tiles = rawOptions.map((opt, i) => {
      const optStr = typeof opt === 'object' && opt !== null ? (opt.text || String(opt)) : String(opt);
      // Strip "1　" or "1. " or "(1) " prefix
      const cleanText = optStr.replace(/^([1-4][\s\u3000\.\)]|\([1-4]\)\s*)/, '').trim();
      return {
        id: i + 1,
        text: cleanText || optStr,
        raw: optStr
      };
    });
  }

  // Text flow / cohesion specific enrichment
  if (facet === FACET_TEXT) {
    card.passage_id = meta.passage_id || drill.passage_id || null;
    card.passage_text = meta.passage_text || drill.passage_text || '';
    card.blank_number = drill.blank_number || null;
    card.points = drill.points || drill.cohesion_points || [];
  }

  return card;
}

// =======================================================
// 3. STAR QUESTION GRADING LOGIC (doc 02 §9.5, ME-14)
// =======================================================

/**
 * Evaluates Star question tile order submission:
 * - If all 4 tiles placed in correct_order -> Grade 3 (Good)
 * - If full order wrong but the ★ tile is in correct position -> Grade 2 (Hard) and reveal sentence
 * - Else -> Grade 1 (Again)
 *
 * @param {Array<number|Object>} userOrder - Ordered array of tile IDs [4, 3, 2, 1]
 * @param {Object} card - Star card object with correct_order, star_slot_index, etc.
 * @returns {Object} Structured grading result with numeric grade and rationale
 */
export function gradeStarQuestion(userOrder, card) {
  if (!card) {
    throw new Error('gradeStarQuestion: card object is required');
  }

  const expectedOrder = Array.isArray(card.correct_order)
    ? card.correct_order.map(Number)
    : [];

  if (expectedOrder.length !== 4) {
    throw new Error(`gradeStarQuestion: expected 4-item correct_order, got ${expectedOrder.length}`);
  }

  // Normalize userOrder to array of tile numbers (1-4)
  const normalizedUserOrder = (Array.isArray(userOrder) ? userOrder : []).map(item => {
    if (typeof item === 'object' && item !== null && 'id' in item) {
      return Number(item.id);
    }
    return Number(item);
  });

  // Resolve star slot index (0..3)
  let starIdx = -1;
  if (typeof card.star_slot_index === 'number' && card.star_slot_index >= 0 && card.star_slot_index < 4) {
    starIdx = card.star_slot_index;
  } else if (card.correct_answer !== undefined) {
    starIdx = expectedOrder.indexOf(Number(card.correct_answer));
  } else if (typeof card.star_position === 'number') {
    starIdx = (card.star_position >= 0 && card.star_position < 4)
      ? card.star_position
      : card.star_position - 1;
  }
  if (starIdx < 0 || starIdx >= 4) {
    starIdx = 2; // standard 3rd slot default
  }

  const expectedStarAnswer = expectedOrder[starIdx];
  const userStarAnswer = normalizedUserOrder[starIdx];

  // 1. Full match check
  const isFullMatch = normalizedUserOrder.length === 4 &&
    normalizedUserOrder.every((val, idx) => val === expectedOrder[idx]);

  // 2. Lucky star check (star slot contains correct tile)
  const isStarCorrect = userStarAnswer !== undefined && userStarAnswer === expectedStarAnswer;

  let grade;
  let gradeName;
  if (isFullMatch) {
    grade = 3;
    gradeName = 'Good';
  } else if (isStarCorrect) {
    grade = 2;
    gradeName = 'Hard';
  } else {
    grade = 1;
    gradeName = 'Again';
  }

  const result = {
    grade,
    gradeName,
    isFullMatch,
    isStarCorrect,
    starIndex: starIdx,
    expectedStarAnswer,
    userStarAnswer,
    userOrder: normalizedUserOrder,
    correctOrder: expectedOrder,
    fullSentence: card.full_sentence || '',
    fullSentenceEn: card.full_sentence_en || '',
    explanationJa: card.explanation_ja || '',
    explanationEn: card.explanation_en || '',
    valueOf() { return grade; },
    [Symbol.toPrimitive](hint) {
      if (hint === 'number') return grade;
      if (hint === 'string') return gradeName;
      return grade;
    }
  };

  return result;
}

/**
 * Returns numeric grade (1, 2, or 3) for star card.
 */
export function getStarGrade(userOrder, card) {
  return gradeStarQuestion(userOrder, card).grade;
}

/**
 * Auto-grades Decision / Fill MCQ responses (doc 02 §5.2, §9.4).
 * Wrong -> 1, Slow/Hint -> 2, Good -> 3. (Never auto Easy).
 */
export function gradeGrammarDecision(isCorrect, elapsedMs = 0, usedHint = false) {
  if (!isCorrect) return 1;
  if (usedHint || (typeof elapsedMs === 'number' && elapsedMs > SLOW_MS)) return 2;
  return 3;
}

// =======================================================
// 4. CONTRAST "VS" PANEL GENERATOR (doc 02 §9.6)
// =======================================================

/**
 * Extracts target pattern and nearest rivals with 1-line English meanings.
 *
 * @param {string|Object} patternOrCard - Pattern ID (e.g. 'P1-1') or Card object
 * @param {Object} options - { userChoicePattern, customIndex, customTags, customClusters }
 * @returns {Object} { targetPattern, targetPatterns, cluster, rivals, userChoiceNote }
 */
export function getContrastVsData(patternOrCard, options = {}) {
  const grammarIndex = options.customIndex || cachedGrammarIndex || (defaultState.grammarDB ? defaultState.grammarDB.index : []) || [];
  const drillTags = options.customTags || cachedDrillTags || defaultState.drillTags || {};
  const clustersList = options.customClusters || cachedClusters || DEFAULT_CLUSTERS;

  // Build pattern map for quick lookup
  const patternMap = new Map();
  for (const p of grammarIndex) {
    if (p && p.id) patternMap.set(p.id, p);
  }

  // 1. Identify target pattern ID(s) and cluster
  let targetPids = [];
  let clusterId = null;
  let tagRivals = [];

  if (typeof patternOrCard === 'string') {
    if (patternOrCard.startsWith('P1-') || patternOrCard.startsWith('P2-') || patternOrCard.startsWith('P3-')) {
      targetPids = [patternOrCard];
    } else {
      // It's a key e.g. 'GD:p1a:1:101' or 'p1a:1:101'
      const parsed = parseGrammarKey(patternOrCard);
      const compKey = parsed?.compositeKey || patternOrCard;
      const tag = drillTags[compKey];
      if (tag) {
        targetPids = Array.isArray(tag.patterns) ? [...tag.patterns] : [];
        clusterId = tag.cluster || null;
        tagRivals = Array.isArray(tag.rivals) ? [...tag.rivals] : [];
      }
    }
  } else if (typeof patternOrCard === 'object' && patternOrCard !== null) {
    if (Array.isArray(patternOrCard.patterns) && patternOrCard.patterns.length > 0) {
      targetPids = [...patternOrCard.patterns];
    } else if (patternOrCard.primaryPattern) {
      targetPids = [patternOrCard.primaryPattern];
    } else if (patternOrCard.patternId) {
      targetPids = [patternOrCard.patternId];
    } else if (patternOrCard.id && String(patternOrCard.id).startsWith('P')) {
      targetPids = [patternOrCard.id];
    }

    if (patternOrCard.cluster) clusterId = patternOrCard.cluster;
    if (Array.isArray(patternOrCard.rivals)) tagRivals = [...patternOrCard.rivals];

    // If still missing, check tags by composite key
    if (targetPids.length === 0 && patternOrCard.compositeKey && drillTags[patternOrCard.compositeKey]) {
      const tag = drillTags[patternOrCard.compositeKey];
      targetPids = Array.isArray(tag.patterns) ? [...tag.patterns] : [];
      if (!clusterId) clusterId = tag.cluster || null;
      if (tagRivals.length === 0 && Array.isArray(tag.rivals)) tagRivals = [...tag.rivals];
    }
  }

  const primaryPid = targetPids[0] || null;

  // 2. Resolve cluster if not yet known
  let clusterObj = null;
  if (clusterId) {
    clusterObj = clustersList.find(c => c.id === clusterId) || null;
  }
  if (!clusterObj && primaryPid) {
    clusterObj = clustersList.find(c => (c.patterns || []).includes(primaryPid)) || null;
  }
  if (!clusterObj) {
    clusterObj = clustersList[0]; // fallback
  }

  // 3. Resolve rival pattern IDs
  let rivalPids = [];
  if (tagRivals.length > 0) {
    rivalPids = [...tagRivals];
  } else if (clusterObj && Array.isArray(clusterObj.patterns)) {
    // Sibling patterns in cluster excluding targets
    rivalPids = clusterObj.patterns.filter(pid => !targetPids.includes(pid));
  }

  // 4. Resolve details from index
  function resolvePatternInfo(pid) {
    const raw = patternMap.get(pid);
    if (raw) {
      // 1-line English meaning summary
      let cleanEn = raw.meaning_en || '';
      // Take first meaningful sentence if very long
      const dotIdx = cleanEn.indexOf('. ');
      const oneLine = dotIdx > 15 ? cleanEn.slice(0, dotIdx + 1) : cleanEn;

      return {
        id: raw.id,
        pattern: raw.pattern || pid,
        pattern_ruby: raw.pattern_ruby || raw.pattern || pid,
        meaning_en: oneLine,
        meaning_full_en: raw.meaning_en || '',
        meaning_ja: raw.meaning_ja || '',
        connection: raw.connection || '',
        nuance_notes: raw.nuance_notes || ''
      };
    }
    return {
      id: pid,
      pattern: pid,
      pattern_ruby: pid,
      meaning_en: 'N3 grammar pattern',
      meaning_full_en: '',
      meaning_ja: '',
      connection: '',
      nuance_notes: ''
    };
  }

  const targetPatternObjs = targetPids.map(resolvePatternInfo);
  const targetPattern = targetPatternObjs[0] || resolvePatternInfo(primaryPid || 'Unknown');
  const rivalObjs = rivalPids.map(resolvePatternInfo);

  // 5. Evaluate learner's choice comparison if provided
  let userChoiceNote = null;
  let userChoicePatternObj = null;
  if (options.userChoicePattern) {
    const chosenPid = typeof options.userChoicePattern === 'object'
      ? (options.userChoicePattern.id || options.userChoicePattern.patternId)
      : options.userChoicePattern;

    if (chosenPid && !targetPids.includes(chosenPid)) {
      userChoicePatternObj = resolvePatternInfo(chosenPid);
      userChoiceNote = `You chose ${userChoicePatternObj.pattern} (${userChoicePatternObj.id}): it means "${userChoicePatternObj.meaning_en}"`;
    }
  }

  return {
    targetPattern,
    targetPatterns: targetPatternObjs,
    cluster: clusterObj ? {
      id: clusterObj.id,
      name_en: clusterObj.name_en,
      name_ja: clusterObj.name_ja
    } : null,
    rivals: rivalObjs,
    userChoiceNote,
    userChoicePattern: userChoicePatternObj
  };
}

/**
 * Renders HTML for post-answer "vs" contrast panel.
 */
export function renderContrastVsPanel(patternOrCard, options = {}) {
  const data = getContrastVsData(patternOrCard, options);
  const target = data.targetPattern;
  const cluster = data.cluster;
  const rivals = data.rivals.slice(0, 4); // show top 4 nearest rivals

  return `
    <div class="grammar-vs-panel">
      <div class="grammar-vs-header">
        <span class="grammar-vs-badge"><i class="fa-solid fa-code-compare"></i> Contrast</span>
        ${cluster ? `<span class="grammar-vs-cluster">${cluster.name_en} (${cluster.name_ja})</span>` : ''}
      </div>

      ${data.userChoiceNote ? `
        <div class="grammar-vs-choice-alert">
          <i class="fa-solid fa-circle-exclamation" style="margin-right: 0.35rem;"></i>
          ${data.userChoiceNote}
        </div>
      ` : ''}

      <div class="grammar-vs-target">
        <div class="grammar-vs-target-title">
          <span>${target.pattern_ruby || target.pattern}</span>
          <span class="grammar-vs-pid">${target.id}</span>
        </div>
        <div class="grammar-vs-target-meaning">${target.meaning_en}</div>
        ${target.connection ? `<div class="grammar-vs-connection">${target.connection}</div>` : ''}
      </div>

      ${rivals.length > 0 ? `
        <div class="grammar-vs-rivals-title">Rival Patterns in Same Cluster:</div>
        <div class="grammar-vs-rivals-list">
          ${rivals.map(r => `
            <div class="grammar-vs-rival-card">
              <div class="grammar-vs-rival-head">
                <span class="grammar-vs-rival-name">${r.pattern_ruby || r.pattern}</span>
                <span class="grammar-vs-pid">${r.id}</span>
              </div>
              <div class="grammar-vs-rival-meaning">${r.meaning_en}</div>
            </div>
          `).join('')}
        </div>
      ` : ''}
    </div>
  `;
}

// =======================================================
// 5. CLUSTER SESSION BUILDER & INTERLEAVING (doc 02 §9.6, ME-16)
// =======================================================

/**
 * Interleaves an array of cards so that NO TWO CONSECUTIVE CARDS
 * belong to the same pattern while alternatives exist (ME-16).
 *
 * Uses a greedy max-heap-style selection to maximize separation.
 *
 * @param {Array<Object>} cards - Array of card objects
 * @param {Function} [getPatternFn] - Extractor function for card pattern ID
 * @returns {Array<Object>} Interleaved array of cards
 */
export function interleaveByPattern(cards, getPatternFn = null) {
  if (!Array.isArray(cards) || cards.length <= 1) {
    return Array.isArray(cards) ? [...cards] : [];
  }

  const getPat = getPatternFn || (c => {
    if (c.patterns && Array.isArray(c.patterns) && c.patterns.length > 0) return c.patterns[0];
    if (c.primaryPattern) return c.primaryPattern;
    if (c.patternId) return c.patternId;
    return 'unknown';
  });

  // 1. Group cards by pattern
  const groups = new Map();
  for (const card of cards) {
    const pat = getPat(card);
    if (!groups.has(pat)) {
      groups.set(pat, []);
    }
    groups.get(pat).push(card);
  }

  // Shuffle within each pattern group
  for (const list of groups.values()) {
    list.sort(() => Math.random() - 0.5);
  }

  const result = [];
  let lastPattern = null;
  const totalCards = cards.length;

  while (result.length < totalCards) {
    // Find all patterns that still have cards available
    const availablePatterns = [];
    for (const [pat, list] of groups.entries()) {
      if (list.length > 0) {
        availablePatterns.push(pat);
      }
    }

    if (availablePatterns.length === 0) break;

    // Filter to patterns distinct from lastPattern
    const validChoices = availablePatterns.filter(p => p !== lastPattern);

    let chosenPattern;
    if (validChoices.length > 0) {
      // Pick pattern with most remaining cards to minimize future collisions
      validChoices.sort((a, b) => {
        const diff = groups.get(b).length - groups.get(a).length;
        if (diff !== 0) return diff;
        return Math.random() - 0.5;
      });
      chosenPattern = validChoices[0];
    } else {
      // Forced to pick the same pattern only when NO alternatives exist
      chosenPattern = availablePatterns[0];
    }

    const nextCard = groups.get(chosenPattern).shift();
    result.push(nextCard);
    lastPattern = chosenPattern;
  }

  return result;
}

/**
 * Builds a revision session that interleaves cards from patterns in one cluster.
 * Interleaving similar patterns builds discrimination (doc 02 §9.6).
 *
 * @param {string} clusterNameOrId - 'time' | 'cause' | 'Time & Timing' etc.
 * @param {Object} options - { maxCards, cardPool, customClusters }
 * @returns {Array<Object>} Interleaved cards for session
 */
export function buildClusterSession(clusterNameOrId, options = {}) {
  const clustersList = options.customClusters || cachedClusters || DEFAULT_CLUSTERS;
  const query = (clusterNameOrId || '').toLowerCase().trim();

  // Find cluster by id, English name, or Japanese name
  const cluster = clustersList.find(c =>
    c.id.toLowerCase() === query ||
    (c.name_en && c.name_en.toLowerCase().includes(query)) ||
    (c.name_ja && c.name_ja.includes(query))
  );

  if (!cluster) {
    console.warn(`buildClusterSession: cluster '${clusterNameOrId}' not found.`);
    return [];
  }

  const clusterPatterns = new Set(cluster.patterns || []);

  // Use provided cardPool or extract from prebuilt cards
  let pool = options.cardPool;
  if (!pool || !Array.isArray(pool)) {
    // Extract from state.idx if available
    if (defaultState.idx && defaultState.idx.grammar && defaultState.idx.grammar.cards) {
      const idxCards = defaultState.idx.grammar.cards;
      pool = Array.from(idxCards.values());
    } else {
      pool = [];
    }
  }

  // Filter cards belonging to this cluster
  const matchingCards = pool.filter(card => {
    if (card.cluster && card.cluster === cluster.id) return true;
    const pats = card.patterns || (card.primaryPattern ? [card.primaryPattern] : []);
    return pats.some(p => clusterPatterns.has(p));
  });

  if (matchingCards.length === 0) {
    return [];
  }

  // Interleave
  const interleaved = interleaveByPattern(matchingCards);

  // Cap at maxCards if specified
  const max = options.maxCards || 20;
  return interleaved.slice(0, max);
}

// =======================================================
// 6. PATTERN MASTERY & "LEARNED" CRITERIA (doc 02 §9.2, §9.8, ME-15)
// =======================================================

/**
 * Computes individual card score (doc 02 §7.1):
 * - 0.0: unseen
 * - 0.3: learning / relearning (reps > 0 || correct > 0 || incorrect > 0)
 * - 0.7: review (interval >= 6 or reps >= 2)
 * - 1.0: mastered (reps >= 4 && interval >= 21 && weight <= 0.8)
 *
 * @param {Object} cardStats
 * @returns {number} 0.0, 0.3, 0.7, or 1.0
 */
export function computeCardScore(cardStats) {
  if (!cardStats) return 0.0;
  const reps = cardStats.reps || 0;
  const correct = cardStats.correct || 0;
  const incorrect = cardStats.incorrect || 0;
  const interval = cardStats.interval || 0;
  const weight = cardStats.weight !== undefined ? cardStats.weight : 1.0;

  if (reps === 0 && correct === 0 && incorrect === 0) {
    return 0.0;
  }

  // Mastered
  if (cardStats.status === 'mastered' || (reps >= 4 && interval >= 21 && weight <= 0.8)) {
    return 1.0;
  }

  // Review solid
  if (cardStats.status === 'review' || interval >= 6 || reps >= 2) {
    return 0.7;
  }

  // Learning / relearning
  if (reps > 0 || correct > 0 || incorrect > 0) {
    return 0.3;
  }

  return 0.0;
}

/**
 * Checks whether a drill card has been passed (at least 1 correct response).
 */
export function isCardPassed(cardStats) {
  if (!cardStats) return false;
  return (cardStats.correct || 0) > 0 || (cardStats.reps || 0) > 0;
}

/**
 * Derives pattern mastery score and "Learned" status (doc 02 §9.2, §9.8):
 * - Unit of learning = pattern; Unit of scheduling = drill cards.
 * - Pattern score = mean(scores of tagged cards).
 * - A pattern counts as "Learned" ONLY when at least 2 different drill cards have been passed.
 * - Score is capped at 0.6 until at least 2 cards have been passed.
 *
 * @param {string} patternId - e.g. 'P1-1'
 * @param {Object} [stats=defaultState.stats] - SRS stats map
 * @param {Array<Object>} [taggedCards=null] - Cards tagged to this pattern
 * @returns {Object} Mastery status package
 */
export function getPatternMastery(patternId, stats = null, taggedCards = null) {
  const userStats = stats || defaultState.stats || {};

  // Resolve tagged cards for this pattern
  let cards = taggedCards;
  if (!cards) {
    if (defaultState.idx && defaultState.idx.grammar) {
      const byPat = defaultState.idx.grammar.byPattern[patternId] || [];
      const cardsMap = defaultState.idx.grammar.cards;
      cards = byPat.map(k => cardsMap.get(k)).filter(Boolean);
    }
  }

  if (!cards || cards.length === 0) {
    return {
      patternId,
      score: 0.0,
      rawMean: 0.0,
      isLearned: false,
      passedCount: 0,
      totalCards: 0,
      capped: false
    };
  }

  let totalScore = 0;
  let passedCount = 0;
  const evaluatedCards = [];

  for (const card of cards) {
    const cardKey = card.key || card.compositeKey;
    const st = userStats[cardKey] || (card.compositeKey ? userStats[card.compositeKey] : null);
    const score = computeCardScore(st);
    const passed = isCardPassed(st);

    if (passed) {
      passedCount++;
    }

    totalScore += score;
    evaluatedCards.push({ key: cardKey, score, passed });
  }

  const rawMean = Number((totalScore / cards.length).toFixed(3));

  // Acceptance Criterion ME-15 & §9.2:
  // A pattern counts as Learned ONLY when at least 2 different drill cards for it have been passed.
  // Pattern mastery capped at 0.6 until at least 2 cards have been passed.
  const isLearned = passedCount >= 2;
  const score = isLearned ? rawMean : Math.min(rawMean, 0.6);
  const capped = !isLearned && rawMean > 0.6;

  return {
    patternId,
    score,
    rawMean,
    isLearned,
    passedCount,
    totalCards: cards.length,
    capped,
    cards: evaluatedCards
  };
}

/**
 * Returns boolean indicating if pattern satisfies the "Learned" criterion (passed >= 2 distinct cards).
 */
export function isPatternLearned(patternId, stats = null, taggedCards = null) {
  return getPatternMastery(patternId, stats, taggedCards).isLearned;
}

// =======================================================
// 7. DATASETS & CACHE MANAGEMENT
// =======================================================

/**
 * Initializes or sets module datasets in runtime.
 */
export function setGrammarDatasets({ grammarIndex, drillTags, clusters }) {
  if (grammarIndex) cachedGrammarIndex = grammarIndex;
  if (drillTags) cachedDrillTags = drillTags;
  if (clusters) cachedClusters = clusters;
}

export function getAllClusters() {
  return cachedClusters || DEFAULT_CLUSTERS;
}

export function getCluster(clusterIdOrName) {
  const clusters = getAllClusters();
  const q = (clusterIdOrName || '').toLowerCase().trim();
  return clusters.find(c =>
    c.id.toLowerCase() === q ||
    (c.name_en && c.name_en.toLowerCase().includes(q)) ||
    (c.name_ja && c.name_ja.includes(q))
  ) || null;
}

export function getPatternsInCluster(clusterIdOrName) {
  const clus = getCluster(clusterIdOrName);
  return clus ? [...clus.patterns] : [];
}

// =======================================================
// 8. BROWSER DOM INTERACTION FOR STAR QUESTIONS (WP-9b)
// =======================================================

/**
 * Generates the complete HTML workspace for a Star arrangement drill.
 *
 * @param {Object} card - Star card
 * @param {Array<number>} [placedTiles=[]] - Currently placed tile IDs in slots 0..3
 * @returns {string} HTML string
 */
export function renderStarWorkspaceHTML(card, placedTiles = []) {
  const prompt = card.prompt || '';
  const starSlotIdx = card.star_slot_index !== undefined ? card.star_slot_index : 2;
  const tiles = card.tiles || [];

  // Parse prompt to split prefix and suffix around blanks if possible
  // Prompt usually contains "＿＿＿　＿＿＿　＿★＿　＿＿＿"
  let prefix = '';
  let suffix = '';
  const blankMatch = prompt.match(/^(.*?)(?:＿＿＿.*)(.*)$/);
  if (blankMatch) {
    prefix = blankMatch[1].trim();
    suffix = blankMatch[2].replace(/[＿★\s]/g, '').trim();
  } else {
    prefix = prompt;
  }

  const placedSet = new Set(placedTiles.filter(t => t !== null && t !== undefined));

  return `
    <div class="grammar-star-workspace" data-key="${card.key}">
      <div class="star-sentence-line">
        ${prefix ? `<span class="star-sentence-prefix">${prefix}</span>` : ''}
        <div class="star-slots-container">
          ${[0, 1, 2, 3].map(slotIdx => {
            const isTarget = slotIdx === starSlotIdx;
            const tileId = placedTiles[slotIdx];
            const tileObj = tileId ? tiles.find(t => t.id === tileId) : null;
            const isFilled = !!tileObj;

            return `
              <div class="star-slot ${isTarget ? 'star-target' : ''} ${isFilled ? 'filled' : ''}"
                   data-slot="${slotIdx}"
                   onclick="window.N3GrammarSRS && window.N3GrammarSRS.onSlotClick && window.N3GrammarSRS.onSlotClick(${slotIdx})">
                <span class="star-slot-index">${slotIdx + 1}</span>
                <span class="star-slot-text">${tileObj ? tileObj.text : ''}</span>
              </div>
            `;
          }).join('')}
        </div>
        ${suffix ? `<span class="star-sentence-suffix">${suffix}</span>` : ''}
      </div>

      <div class="star-tiles-pool">
        ${tiles.map(tile => {
          const isPlaced = placedSet.has(tile.id);
          return `
            <button class="star-tile ${isPlaced ? 'placed' : ''}"
                    data-tile-id="${tile.id}"
                    ${isPlaced ? 'disabled' : ''}
                    onclick="window.N3GrammarSRS && window.N3GrammarSRS.onTileClick && window.N3GrammarSRS.onTileClick(${tile.id})">
              <span class="star-tile-num">${tile.id}</span>
              <span>${tile.text}</span>
            </button>
          `;
        }).join('')}
      </div>

      <div class="star-actions-bar">
        <button class="star-btn star-btn-clear"
                onclick="window.N3GrammarSRS && window.N3GrammarSRS.onClearClick && window.N3GrammarSRS.onClearClick()">
          <i class="fa-solid fa-rotate-left"></i> Clear
        </button>
        <button class="star-btn star-btn-check"
                ${placedTiles.filter(t => t != null).length === 4 ? '' : 'disabled'}
                onclick="window.N3GrammarSRS && window.N3GrammarSRS.onCheckClick && window.N3GrammarSRS.onCheckClick()">
          <i class="fa-solid fa-check"></i> Check
        </button>
      </div>

      <div id="star-feedback-area"></div>
    </div>
  `;
}

// =======================================================
// 9. EXPORTS & GLOBAL BINDING
// =======================================================

export const N3GrammarSRS = {
  FACET_DECISION,
  FACET_STAR,
  FACET_TEXT,
  FACET_CONTRAST,
  DEFAULT_CLUSTERS,
  formatGrammarKey,
  parseGrammarKey,
  toCompositeKey,
  buildGrammarCard,
  gradeStarQuestion,
  getStarGrade,
  gradeGrammarDecision,
  getContrastVsData,
  renderContrastVsPanel,
  interleaveByPattern,
  buildClusterSession,
  computeCardScore,
  isCardPassed,
  getPatternMastery,
  isPatternLearned,
  setGrammarDatasets,
  getAllClusters,
  getCluster,
  getPatternsInCluster,
  renderStarWorkspaceHTML
};

if (typeof window !== 'undefined') {
  window.N3GrammarSRS = N3GrammarSRS;
}

export default N3GrammarSRS;
