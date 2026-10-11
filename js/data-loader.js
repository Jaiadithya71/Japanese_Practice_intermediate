/* =======================================================
   NIHONGO INTERMEDIATE — data-loader.js
   Async Loading & Ingestion of Intermediate Datasets
   ======================================================= */

import { state } from './state.js';

const VOCAB_FILES = [
  'data/vocabulary/part1_topics_ch01_05.json',
  'data/vocabulary/part1_topics_ch06_10.json',
  'data/vocabulary/part1_topics_ch11_15.json',
  'data/vocabulary/part1_topics_ch16_21.json',
  'data/vocabulary/part2_characteristics_ch01_04.json',
  'data/vocabulary/part2_characteristics_ch05_08.json'
];

export async function loadIntermediateVocabDB() {
  const allChapters = {};
  const allMetadata = {};

  for (const file of VOCAB_FILES) {
    try {
      const res = await fetch(file);
      if (!res.ok) {
        console.warn(`Could not load ${file}: HTTP ${res.status}`);
        continue;
      }
      const data = await res.json();
      
      const chapters = Array.isArray(data) 
        ? data 
        : (data.chapters || (data.sections ? [data] : []));

      for (const ch of chapters) {
        const meta = ch.metadata || {};
        const chId = meta.chapter || 'unknown';
        
        allMetadata[chId] = {
          chapter: chId,
          topic_ja: meta.topic_ja || '',
          topic_en: meta.topic_en || '',
          pages: meta.pages || []
        };

        const words = [];
        for (const sec of (ch.sections || [])) {
          for (const w of (sec.words || [])) {
            words.push({
              ...w,
              chapter: chId,
              section_id: sec.section_id || '',
              section_title_ja: sec.title_ja || '',
              section_title_en: sec.title_en || ''
            });
          }
        }
        allChapters[chId] = words;
      }
    } catch (err) {
      console.error(`Error loading ${file}:`, err);
    }
  }

  state.vocabDB = allChapters;
  state.chapterMetadata = allMetadata;
  return allChapters;
}

export function getAllWords() {
  const all = [];
  for (const chId in state.vocabDB) {
    all.push(...state.vocabDB[chId]);
  }
  return all;
}
