# -*- coding: utf-8 -*-
"""
Builder script to assemble JLPT N3 Reading Comprehension Part 4
(実力養成編 第4部 実戦問題: 短文・中文 / Short & Medium Passages, Problems 29-41, pp. 76-99)
into nihongo-intermediate/data/reading/part4_short_medium.json
"""

import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Ensure script directory and parent directories are in sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# Import batches from part4_data or fallback to scratch
try:
    from part4_data.batch1 import batch1_lessons
    from part4_data.batch2 import batch2_lessons
    from part4_data.batch3 import batch3_lessons
    from part4_data.batch4 import batch4_lessons
except ImportError:
    scratch_dir = os.path.abspath(os.path.join(script_dir, '../../scratch'))
    if scratch_dir not in sys.path:
        sys.path.insert(0, scratch_dir)
    from data_part4_batch1 import batch1_lessons
    from data_part4_batch2 import batch2_lessons
    from data_part4_batch3 import batch3_lessons
    from data_part4_batch4 import batch4_lessons


def build():
    all_lessons = batch1_lessons + batch2_lessons + batch3_lessons + batch4_lessons

    data = {
        "metadata": {
            "bookTitle": "新完全マスター JLPT N3 読解",
            "bookTitleRomaji": "Shin Kanzen Master JLPT N3 Dokkai",
            "englishTitle": "New Complete Master JLPT N3 Reading Comprehension",
            "level": "JLPT N3 (Intermediate)",
            "section": "実力養成編 第4部 実戦問題",
            "subSection": "短文・中文 (Short Texts & Mid-length Texts)",
            "description": "Comprehensive transcription of Shin Kanzen Master JLPT N3 Dokkai Part 4: Practical Test Problems (Problems 29-41, pp. 76-99) including Short Texts (Problems 29-32) and Mid-length Texts (Problems 33-41) with complete ruby furigana, comprehensive questions, and bilingual explanations.",
            "version": "1.0.0",
            "lastUpdated": "2026-10-12"
        },
        "lessons": all_lessons
    }

    out_dir = os.path.abspath(os.path.join(script_dir, '../data/reading'))
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part4_short_medium.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total_sentences = sum(len(l.get('passage', {}).get('sentences', [])) for l in all_lessons)
    total_questions = sum(len(l.get('comprehensionQuestions', [])) for l in all_lessons)
    total_vocab = sum(len(l.get('vocabulary', [])) for l in all_lessons)

    print(f"Successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")
    print(f"Total lessons: {len(all_lessons)}")
    print(f"Total sentences: {total_sentences}")
    print(f"Total comprehension questions: {total_questions}")
    print(f"Total vocabulary items: {total_vocab}")


if __name__ == '__main__':
    build()
