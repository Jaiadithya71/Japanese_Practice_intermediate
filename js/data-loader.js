/* =======================================================
   NIHONGO INTERMEDIATE — data-loader.js
   Async Loading & Ingestion of 5-Pillar Intermediate Datasets
   ======================================================= */

import { state } from './state.js';

// Book 1: Vocabulary Files
const VOCAB_FILES = [
  'data/vocabulary/part1_topics_ch01_05.json',
  'data/vocabulary/part1_topics_ch06_10.json',
  'data/vocabulary/part1_topics_ch11_15.json',
  'data/vocabulary/part1_topics_ch16_21.json',
  'data/vocabulary/part2_characteristics_ch01_04.json',
  'data/vocabulary/part2_characteristics_ch05_08.json',
  'data/vocabulary/part3_mock_exams.json'
];

// Book 2: Reading Comprehension Files
const READING_FILES = [
  { file: 'data/reading/part1_foundation.json', cat: 'foundation' },
  { file: 'data/reading/passages.json', cat: 'foundation' },
  { file: 'data/reading/part2_short_1.json', cat: 'strategy' },
  { file: 'data/reading/part2_short_2.json', cat: 'strategy' },
  { file: 'data/reading/part2_short_3.json', cat: 'strategy' },
  { file: 'data/reading/part4_short_medium.json', cat: 'real_short_medium' },
  { file: 'data/reading/part4_long_info.json', cat: 'real_long_info' }
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
              type: 'vocab',
              book: 'vocab',
              chapter: chId,
              section_id: sec.section_id || '',
              section_title_ja: sec.title_ja || '',
              section_title_en: sec.title_en || ''
            });
          }
        }
        // Some units ship without word ids; derive stable ones so SRS progress is per word
        words.forEach((w, i) => { if (!w.id) w.id = 'v' + String(chId).padStart(2, '0') + '-' + String(i + 1).padStart(3, '0'); });
        allChapters[chId] = words;
        if (!state.chapterExercises) state.chapterExercises = {};
        state.chapterExercises[chId] = ch.exercises || [];
      }
    } catch (err) {
      console.error(`Error loading vocab file ${file}:`, err);
    }
  }

  state.vocabDB = allChapters;
  state.chapterMetadata = allMetadata;
  return allChapters;
}

export async function loadIntermediateReadingDB() {
  const allLessons = {};
  const categories = {
    foundation: [],
    strategy: [],
    real_short: [],
    real_medium: [],
    real_long: [],
    info: []
  };

  for (const item of READING_FILES) {
    try {
      const res = await fetch(item.file);
      if (!res.ok) {
        console.warn(`Could not load ${item.file}: HTTP ${res.status}`);
        continue;
      }
      const data = await res.json();
      const lessons = data.lessons || [];

      for (const l of lessons) {
        if (!l.id) continue;

        // Categorize sub-types for real exam passages
        let targetCat = item.cat;
        if (item.cat === 'real_short_medium') {
          targetCat = (l.problemNumber && l.problemNumber <= 38) ? 'real_short' : 'real_medium';
        } else if (item.cat === 'real_long_info') {
          targetCat = (l.problemNumber && l.problemNumber <= 51) ? 'real_long' : 'info';
        }

        const enrichedLesson = {
          ...l,
          book: 'reading',
          category: targetCat,
          sourceFile: item.file
        };

        allLessons[l.id] = enrichedLesson;
        if (!categories[targetCat]) categories[targetCat] = [];
        categories[targetCat].push(l.id);
      }
    } catch (err) {
      console.error(`Error loading reading file ${item.file}:`, err);
    }
  }

  state.readingDB = allLessons;
  state.readingCategories = categories;
  return allLessons;
}

// Book 4: Kanji Files
const KANJI_PART_FILES = [
  { part: 1, file: 'data/kanji/part1_lessons_01_05.json' },
  { part: 2, file: 'data/kanji/part2_lessons_06_10.json' },
  { part: 3, file: 'data/kanji/part3_lessons_11_15.json' },
  { part: 4, file: 'data/kanji/part4_lessons_16_20.json' },
  { part: 5, file: 'data/kanji/part5_lessons_21_25.json' }
];

const KANJI_EXERCISE_FILES = [
  'data/kanji/exercises_part1.json',
  'data/kanji/exercises_part2.json',
  'data/kanji/exercises_part3.json',
  'data/kanji/exercises_part4.json',
  'data/kanji/exercises_part5.json'
];

export async function loadIntermediateKanjiDB() {
  const kanjiMap = {};
  const allLessons = [];
  const exercisesMap = {};

  // 1. Load Parts 1-5 target kanji
  for (const item of KANJI_PART_FILES) {
    try {
      const res = await fetch(item.file);
      if (!res.ok) continue;
      const data = await res.json();
      const lessons = data.lessons || [];
      for (const les of lessons) {
        allLessons.push({
          part: item.part,
          lesson_number: les.lesson_number,
          title_ja: les.title_ja,
          title_en: les.title_en,
          page: les.page,
          kanjiCount: (les.kanji || []).length
        });
        for (const k of (les.kanji || [])) {
          const char = k.kanji;
          kanjiMap[char] = {
            ...k,
            type: 'kanji',
            book: 'kanji',
            part: item.part,
            lesson_number: les.lesson_number,
            lesson_title_ja: les.title_ja,
            lesson_title_en: les.title_en
          };
        }
      }
    } catch (err) {
      console.error(`Error loading kanji part ${item.file}:`, err);
    }
  }

  // 2. Load Exercises
  for (const exFile of KANJI_EXERCISE_FILES) {
    try {
      const res = await fetch(exFile);
      if (!res.ok) continue;
      const data = await res.json();
      const lessons = data.lessons || [];
      for (const les of lessons) {
        const lNum = les.lesson_number || les.lesson || les.lesson_id;
        if (!exercisesMap[lNum]) exercisesMap[lNum] = [];
        for (const ex of (les.exercises || [])) {
          exercisesMap[lNum].push({
            ...ex,
            part: data.metadata ? data.metadata.part : 1,
            lesson_number: lNum,
            lesson_title_ja: les.title_ja || les.title || `Lesson ${lNum}`
          });
        }
      }
    } catch (err) {
      // Quiet fail if exercise parts are pending
    }
  }

  // 3. Load Review 300
  try {
    const res = await fetch('data/kanji/review_300_n4_n5.json');
    if (res.ok) {
      const data = await res.json();
      state.kanjiReview300 = data.items || [];
    }
  } catch (err) {
    console.error('Error loading review 300:', err);
  }

  // 4. Load Special Readings
  try {
    const res = await fetch('data/kanji/special_readings.json');
    if (res.ok) {
      const data = await res.json();
      state.kanjiSpecialReadings = data.items || [];
    }
  } catch (err) {
    console.error('Error loading special readings:', err);
  }

  // 5. Load Mock Tests
  try {
    const res = await fetch('data/kanji/kanji_mock_tests.json');
    if (res.ok) {
      const data = await res.json();
      state.kanjiMockTests = data.chapters || [];
    }
  } catch (err) {
    console.error('Error loading mock tests:', err);
  }

  state.kanjiDB = kanjiMap;
  state.kanjiLessons = allLessons;
  state.kanjiExercisesDB = exercisesMap;
  return kanjiMap;
}

// Master All-Books Ingestion
export async function loadAllActiveBooks() {
  await Promise.all([
    loadIntermediateVocabDB(),
    loadIntermediateReadingDB(),
    loadIntermediateKanjiDB()
  ]);
  console.log(`Loaded ${Object.keys(state.vocabDB).length} vocab chapters, ${Object.keys(state.readingDB).length} reading lessons, and ${Object.keys(state.kanjiDB).length} kanji.`);
}

export function getAllWords() {
  const all = [];
  for (const chId in state.vocabDB) {
    all.push(...state.vocabDB[chId]);
  }
  return all;
}

export function getAllReadingLessons() {
  return Object.values(state.readingDB);
}

export function getAllKanji() {
  return Object.values(state.kanjiDB);
}
