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

export function normalizeQuestion(q, lessonId, idx) {
  if (!q) return q;
  return {
    ...q,
    id: q.questionId || q.id || `${lessonId}_q${idx + 1}`,
    question_ja: q.questionText_ja || q.question_ja || '',
    question_en: q.questionText_en || q.question_en || '',
    options: (q.options || []).map(o => typeof o === 'string' ? o : (o.text_ja || '')),
    options_en: (q.options || []).map(o => typeof o === 'string' ? '' : (o.text_en || '')),
    correctAnswer: parseInt(q.correctAnswer, 10)
  };
}

export function normalizeDrill(d, lessonId, idx) {
  if (!d) return d;
  const options = (d.options || []).map(o => typeof o === 'string' ? o : (o.text_ja || ''));
  const options_en = (d.options || []).map(o => typeof o === 'string' ? '' : (o.text_en || ''));

  let correctAnswer = d.correctAnswer !== undefined ? parseInt(d.correctAnswer, 10) : undefined;
  if ((correctAnswer === undefined || isNaN(correctAnswer)) && d.correctKey) {
    const optIdx = (d.options || []).findIndex(o => o.key === d.correctKey);
    if (optIdx >= 0) {
      correctAnswer = optIdx + 1;
    } else if (typeof d.correctKey === 'string' && /^[a-d]$/i.test(d.correctKey)) {
      correctAnswer = d.correctKey.toLowerCase().charCodeAt(0) - 96;
    }
  }

  const normalized = {
    ...d,
    id: d.drillId || d.id || `${lessonId}_d${idx + 1}`,
    question_ja: d.questionText_ja || d.question_ja || d.instruction_ja || d.title_ja || '',
    question_en: d.questionText_en || d.question_en || d.instruction_en || d.title_en || '',
    options,
    options_en
  };
  if (correctAnswer !== undefined && !isNaN(correctAnswer)) {
    normalized.correctAnswer = correctAnswer;
  }
  return normalized;
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

        if (Array.isArray(l.comprehensionQuestions)) {
          enrichedLesson.comprehensionQuestions = l.comprehensionQuestions.map((q, idx) => {
            const normQ = normalizeQuestion(q, l.id, idx);
            // Migration M4: if old key exists in state.stats and new key does not, copy it over
            if (state && state.stats) {
              const oldKey = `R_Q:${l.id}_q${idx + 1}`;
              const newKey = `R_Q:${normQ.id}`;
              if (state.stats[oldKey] && !state.stats[newKey]) {
                state.stats[newKey] = { ...state.stats[oldKey] };
              }
            }
            return normQ;
          });
        }

        if (Array.isArray(l.drills)) {
          enrichedLesson.drills = l.drills.map((d, idx) =>
            normalizeDrill(d, l.id, idx)
          );
        }

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

// Book 3: Grammar Files Loader
export async function loadIntermediateGrammarDB() {
  try {
    const [indexRes, introRes, p1_1Res, p1_2Res, p2Res, p3Res, mockRes] = await Promise.all([
      fetch('data/grammar/grammar_index.json'),
      fetch('data/grammar/intro_and_guide.json'),
      fetch('data/grammar/part1_sec1_to_6.json'),
      fetch('data/grammar/part1_sec7_to_12.json'),
      fetch('data/grammar/part2_sentence_grammar2.json'),
      fetch('data/grammar/part3_text_grammar.json'),
      fetch('data/grammar/mock_test.json')
    ]);

    if (indexRes.ok) state.grammarDB.index = await indexRes.json();
    if (introRes.ok) state.grammarDB.intro = await introRes.json();
    if (p1_1Res.ok) state.grammarDB.part1_1_6 = await p1_1Res.json();
    if (p1_2Res.ok) state.grammarDB.part1_7_12 = await p1_2Res.json();
    if (p2Res.ok) state.grammarDB.part2 = await p2Res.json();
    if (p3Res.ok) state.grammarDB.part3 = await p3Res.json();
    if (mockRes.ok) state.grammarDB.mock = await mockRes.json();

    console.log(`Loaded grammar DB: ${state.grammarDB.index.length} indexed patterns.`);
  } catch (err) {
    console.error('Error loading grammar DB:', err);
  }
}

// Master All-Books Ingestion
export async function loadAllActiveBooks() {
  await Promise.all([
    loadIntermediateVocabDB(),
    loadIntermediateReadingDB(),
    loadIntermediateGrammarDB(),
    loadIntermediateKanjiDB()
  ]);
  console.log(`Loaded ${Object.keys(state.vocabDB).length} vocab chapters, ${Object.keys(state.readingDB).length} reading lessons, ${state.grammarDB.index?.length || 0} grammar patterns, and ${Object.keys(state.kanjiDB).length} kanji.`);
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
