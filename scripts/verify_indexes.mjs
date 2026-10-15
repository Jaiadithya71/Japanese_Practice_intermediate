#!/usr/bin/env node
/**
 * scripts/verify_indexes.mjs
 * Verification test harness for js/indexes.js runtime memory lookups.
 * Asserts the test oracles defined in n3_dev_handoff/03_DATA_MODEL_AND_MIGRATION.md §4.1:
 * - 443 kanji entries across lessons (442 unique characters)
 * - 865 distinct compound terms
 * - 584 distinct target terms
 * - 254 terms also in vocab DB
 * - 2.19 words per kanji on average, max 9, none with zero words
 * - Execution speed under 150 ms
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildIndexes } from '../js/indexes.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DATA_DIR = path.join(ROOT_DIR, 'data');

function readJson(relPath) {
  const full = path.join(DATA_DIR, relPath);
  return JSON.parse(fs.readFileSync(full, 'utf-8'));
}

async function runVerification() {
  console.log('--- Verifying js/indexes.js in Node.js ---');

  // 1. Ingest Kanji Data
  const kanjiDB = {};
  const kanjiLessons = [];
  const kanjiPartFiles = [
    'kanji/part1_lessons_01_05.json',
    'kanji/part2_lessons_06_10.json',
    'kanji/part3_lessons_11_15.json',
    'kanji/part4_lessons_16_20.json',
    'kanji/part5_lessons_21_25.json'
  ];

  for (let pIdx = 0; pIdx < kanjiPartFiles.length; pIdx++) {
    const partNum = pIdx + 1;
    const file = kanjiPartFiles[pIdx];
    const data = readJson(file);
    const lessons = data.lessons || [];

    for (const les of lessons) {
      kanjiLessons.push({
        part: partNum,
        lesson_number: les.lesson_number,
        title_ja: les.title_ja,
        kanjiCount: (les.kanji || []).length
      });

      for (const k of (les.kanji || [])) {
        const char = k.kanji;
        kanjiDB[char] = {
          ...k,
          type: 'kanji',
          book: 'kanji',
          part: partNum,
          lesson_number: les.lesson_number
        };
      }
    }
  }

  // 2. Ingest Vocabulary Data
  const vocabDB = {};
  const vocabJson = readJson('vocabulary.json');
  for (const w of vocabJson) {
    const ch = w.chapter || 'unknown';
    if (!vocabDB[ch]) vocabDB[ch] = [];
    vocabDB[ch].push(w);
  }

  // 3. Load Optional Tag Datasets
  const vocabTiers = readJson('vocab_tiers.json');
  const wordContexts = readJson('word_contexts.json');
  const drillTags = readJson('drill_tags.json');
  const clusters = readJson('clusters.json');

  const db = {
    kanjiDB,
    kanjiLessons,
    vocabDB,
    grammarDB: {}
  };

  // 4. Run buildIndexes(db)
  const startTime = performance.now();
  const idx = buildIndexes(db, { vocabTiers, wordContexts, drillTags, clusters });
  const duration = performance.now() - startTime;

  console.log(`Execution time: ${duration.toFixed(2)} ms (oracle requirement: < 150 ms)`);

  const meta = idx.meta;
  console.log('Index Metadata results:');
  console.log(`  Kanji entries: ${meta.totalKanji} (expected 443)`);
  console.log(`  Distinct kanji characters: ${meta.distinctKanjiChars} (expected 442)`);
  console.log(`  Distinct terms: ${meta.distinctTerms} (expected 865)`);
  console.log(`  Distinct target terms: ${meta.targetTerms} (expected 584)`);
  console.log(`  Vocab DB overlap terms: ${meta.vocabOverlap} (expected 254)`);
  console.log(`  Average words per kanji: ${meta.avgWordsPerKanji} (expected 2.19)`);
  console.log(`  Max words per kanji: ${meta.maxWordsPerKanji} (expected 9)`);
  console.log(`  Min words per kanji: ${meta.minWordsPerKanji} (expected 1, none zero)`);

  const errors = [];

  // Assertions against doc 03 §4.1
  if (meta.totalKanji !== 443) errors.push(`Oracle failed: totalKanji ${meta.totalKanji} !== 443`);
  if (meta.distinctKanjiChars !== 442) errors.push(`Oracle failed: distinctKanjiChars ${meta.distinctKanjiChars} !== 442`);
  if (meta.distinctTerms !== 865) errors.push(`Oracle failed: distinctTerms ${meta.distinctTerms} !== 865`);
  if (meta.targetTerms !== 584) errors.push(`Oracle failed: targetTerms ${meta.targetTerms} !== 584`);
  if (meta.vocabOverlap !== 254) errors.push(`Oracle failed: vocabOverlap ${meta.vocabOverlap} !== 254`);
  if (meta.avgWordsPerKanji !== 2.19) errors.push(`Oracle failed: avgWordsPerKanji ${meta.avgWordsPerKanji} !== 2.19`);
  if (meta.maxWordsPerKanji !== 9) errors.push(`Oracle failed: maxWordsPerKanji ${meta.maxWordsPerKanji} !== 9`);
  if (meta.minWordsPerKanji < 1) errors.push(`Oracle failed: minWordsPerKanji ${meta.minWordsPerKanji} < 1`);
  if (duration > 150) errors.push(`Performance failed: ${duration.toFixed(2)} ms exceeded 150 ms limit`);

  // Assert Schema of idx.words
  const sampleTerm = Object.keys(idx.words)[0];
  const sampleWord = idx.words[sampleTerm];
  const requiredWordProps = ['term', 'reading', 'ruby_html', 'meaning_en', 'isTarget', 'kanjiRefs', 'homeKanji', 'lesson', 'part', 'vocabId', 'context'];
  for (const prop of requiredWordProps) {
    if (!(prop in sampleWord)) {
      errors.push(`Missing property '${prop}' in idx.words['${sampleTerm}']`);
    }
  }

  // Assert kanjiWords targets-first ordering
  for (const char in idx.kanjiWords) {
    const terms = idx.kanjiWords[char];
    let seenNonTarget = false;
    for (const t of terms) {
      const isTarget = idx.words[t].isTarget;
      if (seenNonTarget && isTarget) {
        errors.push(`Ordering violation in idx.kanjiWords['${char}']: non-target precedes target '${t}'`);
        break;
      }
      if (!isTarget) seenNonTarget = true;
    }
  }

  // Assert grammar cards count
  const grammarCardsCount = idx.grammar.cards.size;
  console.log(`Grammar cards indexed: ${grammarCardsCount} (expected 495)`);
  if (grammarCardsCount !== 495) {
    errors.push(`Grammar cards count ${grammarCardsCount} !== 495`);
  }

  // Assert vocab tiers counts
  const t1 = idx.vocabTiers?.tier1?.length || 0;
  const t2 = idx.vocabTiers?.tier2?.length || 0;
  const t3 = idx.vocabTiers?.tier3?.length || 0;
  console.log(`Vocab tiers indexed: T1=${t1}, T2=${t2}, T3=${t3} (total=${t1 + t2 + t3})`);
  if (t1 !== 451 || t2 !== 530 || t3 !== 270) {
    errors.push(`Vocab tiers count mismatch: T1=${t1}, T2=${t2}, T3=${t3}`);
  }

  if (errors.length > 0) {
    console.error('\nVerification FAILED with errors:');
    for (const err of errors) console.error(`  - ${err}`);
    process.exit(1);
  }

  console.log('\nSUCCESS: All oracles (443 / 865 / 584 / 254 / 2.19 / 9 / 1) and schemas verified!');
  process.exit(0);
}

runVerification().catch(err => {
  console.error('Unhandled verification error:', err);
  process.exit(1);
});
