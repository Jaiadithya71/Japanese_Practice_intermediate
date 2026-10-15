/* =======================================================
   NIHONGO INTERMEDIATE — js/indexes.js
   Derived Memory Indexes & Relational Lookups (WP-3)
   ======================================================= */

import { state as defaultState } from './state.js';

// Fallback confusion clusters if clusters.json is not yet loaded
const DEFAULT_CLUSTERS = [
  { id: 'time', name_en: 'Time & Timing', name_ja: '時間・時期', patterns: ['P1-1', 'P1-2', 'P1-3', 'P1-4', 'P1-7', 'P1-9', 'P2-74', 'P2-75', 'P2-76'] },
  { id: 'cause', name_en: 'Cause & Reason', name_ja: '原因・理由', patterns: ['P1-19', 'P1-20', 'P1-21', 'P1-22', 'P1-23', 'P2-71', 'P2-72', 'P3-82', 'P3-83'] },
  { id: 'contrast', name_en: 'Contrast & Comparison', name_ja: '対比・逆接', patterns: ['P1-14', 'P1-15', 'P1-16', 'P1-17', 'P1-18', 'P1-38', 'P2-54', 'P2-55'] },
  { id: 'inability-compulsion', name_en: 'Obligation & Impossibility', name_ja: '義務・不可・禁止・部分否定', patterns: ['P1-34', 'P1-35', 'P1-36', 'P1-37', 'P1-42', 'P1-43', 'P1-44', 'P1-45', 'P2-59'] },
  { id: 'purpose-intent', name_en: 'Purpose, Volition & Desires', name_ja: '目的・意向・希望・働きかけ', patterns: ['P1-39', 'P1-40', 'P1-41', 'P1-46', 'P1-47', 'P1-48', 'P1-49', 'P2-60', 'P2-61'] },
  { id: 'condition', name_en: 'Condition & Hypothesis', name_ja: '条件・仮定・反実仮想', patterns: ['P1-5', 'P1-6', 'P1-8', 'P1-24', 'P1-25', 'P1-26', 'P1-27', 'P1-28', 'P2-56', 'P2-57', 'P2-62'] },
  { id: 'degree-limit', name_en: 'Degree & Limit', name_ja: '程度・限界・最高', patterns: ['P1-10', 'P1-11', 'P1-12', 'P1-13', 'P2-58'] },
  { id: 'viewpoint-attitude', name_en: 'Viewpoint, Attitude & Transmission', name_ja: '視点・伝聞・敬語', patterns: ['P1-29', 'P1-30', 'P1-31', 'P1-32', 'P1-33', 'P1-50', 'P1-51', 'P1-52', 'P1-53', 'P2-65', 'P2-77', 'P2-78', 'P2-79'] },
  { id: 'form-other', name_en: 'Sentence Forms & Cohesion', name_ja: '文型・構文・文の対応', patterns: ['P2-63', 'P2-64', 'P2-66', 'P2-67', 'P2-68', 'P2-69', 'P2-70', 'P2-73', 'P3-80', 'P3-81'] }
];

/**
 * Attempts to load optional dataset files in either Browser (fetch) or Node.js (fs)
 * Returns loaded object or null on failure (safe fallback).
 */
export async function loadOptionalJson(path) {
  // 1. Browser fetch
  if (typeof fetch === 'function' && typeof window !== 'undefined') {
    try {
      const res = await fetch(path);
      if (res.ok) return await res.json();
    } catch (_) {
      // Quiet fallback
    }
  }

  // 2. Node.js environment
  if (typeof process !== 'undefined' && process.versions && process.versions.node) {
    try {
      const { readFileSync } = await import('fs');
      const { resolve } = await import('path');
      const fullPath = resolve(process.cwd(), path);
      const content = readFileSync(fullPath, 'utf-8');
      return JSON.parse(content);
    } catch (_) {
      // Quiet fallback
    }
  }

  return null;
}

/**
 * Synchronously attempts to read JSON file in Node.js, returns null if unavailable.
 */
function readJsonSyncNode(path) {
  if (typeof process !== 'undefined' && process.versions && process.versions.node) {
    try {
      // Use dynamic require or sync fs if available
      const fs = (typeof require === 'function') ? require('fs') : null;
      if (fs) {
        return JSON.parse(fs.readFileSync(path, 'utf-8'));
      }
    } catch (_) {}
  }
  return null;
}

/**
 * Builds derived runtime lookup indexes:
 * - idx.words: keyed by term_ja (canonical word index)
 * - idx.kanjiWords: keyed by kanji character (targets first)
 * - idx.lessonWords: keyed by lesson number (targets first)
 * - idx.grammar: { cards, byPattern, byCluster }
 * - idx.vocabTiers: tier lists and mapping
 * - idx.wordContexts: context sentences map
 *
 * @param {Object} db - Application state object (defaults to central state)
 * @param {Object} optionalData - Preloaded optional datasets ({ vocabTiers, wordContexts, drillTags, clusters })
 * @returns {Object} Built index object (also assigned to db.idx)
 */
export function buildIndexes(db = defaultState, optionalData = {}) {
  const startTime = (typeof performance !== 'undefined' && performance.now) ? performance.now() : Date.now();

  const kanjiDB = db.kanjiDB || {};
  const kanjiLessons = db.kanjiLessons || [];
  const vocabDB = db.vocabDB || {};
  const grammarDB = db.grammarDB || {};

  // Resolve optional datasets from optionalData -> db -> sync node fallback
  const vocabTiers = optionalData.vocabTiers || db.vocabTiers || readJsonSyncNode('data/vocab_tiers.json');
  const wordContexts = optionalData.wordContexts || db.wordContexts || readJsonSyncNode('data/word_contexts.json');
  const drillTags = optionalData.drillTags || db.drillTags || readJsonSyncNode('data/drill_tags.json');
  const clustersData = optionalData.clusters || db.clusters || readJsonSyncNode('data/clusters.json');

  // 1. Build Vocab Lookups: term_ja -> vocabId
  const vocabTermToId = {};
  for (const chId in vocabDB) {
    const wordsList = Array.isArray(vocabDB[chId]) ? vocabDB[chId] : [];
    for (const w of wordsList) {
      const term = w.term_ja || w.term;
      if (term && !vocabTermToId[term]) {
        vocabTermToId[term] = w.id || null;
      }
    }
  }

  // 2. Build Kanji-Word Index
  const wordsIndex = {};
  const kanjiWords = {};
  const lessonWords = {};

  // Set of all target kanji characters
  const allKanjiChars = new Set(Object.keys(kanjiDB));

  // Initialize kanjiWords containers
  for (const char of allKanjiChars) {
    kanjiWords[char] = [];
  }

  // Process all kanji entries
  for (const char in kanjiDB) {
    const kEntry = kanjiDB[char];
    const words = Array.isArray(kEntry.words) ? kEntry.words : [];
    const lessonNo = kEntry.lesson_number || 1;
    const partNo = kEntry.part || 1;

    if (!lessonWords[lessonNo]) {
      lessonWords[lessonNo] = [];
    }

    for (const w of words) {
      const term = w.term_ja || w.term;
      if (!term) continue;

      const isTargetOccur = Boolean(w.is_target);

      if (!wordsIndex[term]) {
        // Collect every N3 target kanji present in term
        const kanjiRefs = [];
        for (const ch of term) {
          if (allKanjiChars.has(ch) && !kanjiRefs.includes(ch)) {
            kanjiRefs.push(ch);
          }
        }

        // Context lookup
        let context = null;
        if (wordContexts && wordContexts[term]) {
          const rawCtx = wordContexts[term];
          const c = Array.isArray(rawCtx) ? rawCtx[0] : rawCtx;
          if (c) {
            context = {
              ja: c.ja || c.sentence_ja || '',
              en: c.en || c.meaning || '',
              src: c.src || c.source || ''
            };
          }
        }

        wordsIndex[term] = {
          term,
          reading: w.reading || '',
          ruby_html: w.ruby_html || '',
          meaning_en: w.meaning_en || '',
          meaning_zh: w.meaning_zh || '',
          isTarget: isTargetOccur,
          kanjiRefs,
          homeKanji: char,
          lesson: lessonNo,
          part: partNo,
          vocabId: vocabTermToId[term] || null,
          context
        };
      } else {
        // Update isTarget if any occurrence has is_target: true
        if (isTargetOccur) {
          wordsIndex[term].isTarget = true;
        }
        // Update homeKanji if taught under a lower lesson number
        if (lessonNo < wordsIndex[term].lesson) {
          wordsIndex[term].homeKanji = char;
          wordsIndex[term].lesson = lessonNo;
          wordsIndex[term].part = partNo;
        }
        // Fill missing readings or meanings if available
        if (!wordsIndex[term].reading && w.reading) wordsIndex[term].reading = w.reading;
        if (!wordsIndex[term].ruby_html && w.ruby_html) wordsIndex[term].ruby_html = w.ruby_html;
        if (!wordsIndex[term].meaning_en && w.meaning_en) wordsIndex[term].meaning_en = w.meaning_en;
        if (!wordsIndex[term].meaning_zh && w.meaning_zh) wordsIndex[term].meaning_zh = w.meaning_zh;
      }

      // Add to kanjiWords if not already present
      if (!kanjiWords[char].includes(term)) {
        kanjiWords[char].push(term);
      }

      // Add to lessonWords if not already present
      if (!lessonWords[lessonNo].includes(term)) {
        lessonWords[lessonNo].push(term);
      }
    }
  }

  // Sort kanjiWords arrays: target terms first
  for (const char in kanjiWords) {
    kanjiWords[char].sort((a, b) => {
      const isTargetA = wordsIndex[a]?.isTarget ? 0 : 1;
      const isTargetB = wordsIndex[b]?.isTarget ? 0 : 1;
      return isTargetA - isTargetB;
    });
  }

  // Sort lessonWords arrays: target terms first
  for (const lNo in lessonWords) {
    lessonWords[lNo].sort((a, b) => {
      const isTargetA = wordsIndex[a]?.isTarget ? 0 : 1;
      const isTargetB = wordsIndex[b]?.isTarget ? 0 : 1;
      return isTargetA - isTargetB;
    });
  }

  // 3. Compute Kanji-Word Summary Statistics
  const distinctTermsCount = Object.keys(wordsIndex).length;
  let targetTermsCount = 0;
  let vocabOverlapCount = 0;

  for (const term in wordsIndex) {
    if (wordsIndex[term].isTarget) targetTermsCount++;
    if (wordsIndex[term].vocabId !== null) vocabOverlapCount++;
  }

  const wordsPerKanjiCounts = Object.values(kanjiWords).map(list => list.length);
  const totalKanjiCount = kanjiLessons.length > 0
    ? kanjiLessons.reduce((acc, l) => acc + (l.kanjiCount || (l.kanji || []).length || 0), 0)
    : allKanjiChars.size;

  const avgWordsPerKanji = wordsPerKanjiCounts.length > 0
    ? Number((wordsPerKanjiCounts.reduce((a, b) => a + b, 0) / wordsPerKanjiCounts.length).toFixed(2))
    : 0;
  const maxWordsPerKanji = wordsPerKanjiCounts.length > 0 ? Math.max(...wordsPerKanjiCounts) : 0;
  const minWordsPerKanji = wordsPerKanjiCounts.length > 0 ? Math.min(...wordsPerKanjiCounts) : 0;

  // 4. Build Grammar Indexes
  const grammarCards = new Map();
  const grammarByPattern = {};
  const grammarByCluster = {};

  // Build byCluster mapping
  const clustersList = (clustersData && clustersData.clusters) ? clustersData.clusters : DEFAULT_CLUSTERS;
  for (const clus of clustersList) {
    grammarByCluster[clus.id] = Array.isArray(clus.patterns) ? [...clus.patterns] : [];
  }

  // Build cards and byPattern from drillTags and grammarDB
  if (drillTags) {
    for (const compositeKey in drillTags) {
      const tag = drillTags[compositeKey];
      const patterns = Array.isArray(tag.patterns) ? tag.patterns : [];

      grammarCards.set(compositeKey, {
        key: `GD:${compositeKey}`,
        compositeKey,
        patterns,
        cluster: tag.cluster || null,
        rivals: Array.isArray(tag.rivals) ? tag.rivals : [],
        section: tag.section || '',
        confidence: tag.confidence || 'auto'
      });

      for (const pid of patterns) {
        if (!grammarByPattern[pid]) {
          grammarByPattern[pid] = [];
        }
        if (!grammarByPattern[pid].includes(compositeKey)) {
          grammarByPattern[pid].push(compositeKey);
        }
      }
    }
  }

  const endTime = (typeof performance !== 'undefined' && performance.now) ? performance.now() : Date.now();
  const buildDurationMs = Math.round((endTime - startTime) * 10) / 10;

  // 5. Construct Index Package
  const idx = {
    words: wordsIndex,
    kanjiWords,
    lessonWords,
    grammar: {
      cards: grammarCards,
      byPattern: grammarByPattern,
      byCluster: grammarByCluster
    },
    vocabTiers: vocabTiers || null,
    wordContexts: wordContexts || null,
    drillTags: drillTags || null,
    clusters: clustersData || null,
    meta: {
      totalKanji: totalKanjiCount,
      distinctKanjiChars: allKanjiChars.size,
      distinctTerms: distinctTermsCount,
      targetTerms: targetTermsCount,
      vocabOverlap: vocabOverlapCount,
      avgWordsPerKanji,
      maxWordsPerKanji,
      minWordsPerKanji,
      buildDurationMs
    }
  };

  // Mount on db.idx
  db.idx = idx;

  return idx;
}
