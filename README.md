# Japanese Practice Intermediate (日本語 中級学習プラットフォーム)

An intermediate-level (JLPT N3) Japanese language learning and practice platform built with modern web technologies, based on structured transcriptions of two core textbooks:
1. **新完全マスター 読解 日本語能力試験 N3** (*Shin Kanzen Master JLPT N3 Reading Comprehension*)
2. **新完全マスター 語彙 日本語能力試験 N3** (*Shin Kanzen Master JLPT N3 Vocabulary*)

---

## 📖 Project Modules

### 1. 読解 (Reading Comprehension)
- **Part 1: 基礎編 (Foundation)**: Grammatical breakdown, clause parsing, conjunctions, reference words, and sentence structure drills.
- **Part 2: 短文 (Short Passages)**: Private emails, formal letters, office memos, instructions, opinion pieces, announcements, adverts, and pamphlets.
- **Part 3: 中文・長文・情報検索 (Medium/Long Passages & Information Retrieval)**: Extended essays, comparative articles, and table/schedule lookups.
- **Features**:
  - Full HTML `<ruby>` furigana annotations with toggle support.
  - Sentence-by-sentence bilingual translations.
  - Contextual vocabulary glosses.
  - Official 4-option Dokkai comprehension questions with detailed answer rationales.

### 2. 語彙 (Vocabulary Mastery)
- **Part 1: 話題別に言葉を学ぼう (Words by Topic)**: 21 thematic chapters (family, personality, daily life, work, community, nature, society).
  - Warming-up discussion prompts.
  - Collocations and compound expressions.
  - `やってみよう` in-context fill-in drills.
  - `練習しよう` multi-type practice exercises (synonyms, traits, collocations, categories, dialogue completion).
- **Part 2: 性質別に言葉を学ぼう (Words by Characteristic)**: 8 characteristic units (native verbs, adverbs, affixes, onomatopoeia).
- **Part 3: 模擬試験 (Mock Examinations)**: Official test format drills.

---

## 📂 Repository Structure

```
nihongo-intermediate/
├── css/                  # Application styling (responsive design, dark/light mode)
├── js/                   # Core application logic, SRS engine, state management
├── data/
│   ├── reading/          # Validated Dokkai JSON datasets
│   │   ├── part1_foundation.json
│   │   ├── part2_short_1.json
│   │   ├── part2_short_2.json
│   │   └── part2_short_3.json
│   └── vocabulary/       # Validated Vocabulary JSON datasets
├── scripts/              # Dataset builders and integrity validators
│   ├── verify_intermediate_data.py
│   └── verify_vocabulary_data.py
├── .gitignore
└── README.md
```

---

## 🛠️ Verification & Quality Assurance

All data files must pass automated integrity tests before committing:
```bash
# Verify Reading Comprehension dataset
python scripts/verify_intermediate_data.py

# Verify Vocabulary dataset
python scripts/verify_vocabulary_data.py
```

The validation suite verifies:
- Strict JSON schema adherence.
- Symmetrical HTML `<ruby>` / `<rt>` markup with 0 malformed tags.
- 100% presence of Japanese terms, kana readings, English meanings, and quiz solutions.
