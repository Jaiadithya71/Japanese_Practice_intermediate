# -*- coding: utf-8 -*-
"""
Builder script to assemble JLPT N3 Reading Comprehension Part 4
(実力養成編 第4部 実戦問題: 長文・情報検索 / Long Passages & Information Retrieval, Problems 49-64, pp. 114-145)
into nihongo-intermediate/data/reading/part4_long_info.json
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

# Import batches from part4_data
from part4_data.p49_51 import lessons as lessons_49_51
from part4_data.p52_57 import lessons as lessons_52_57
from part4_data.p58_64 import lessons as lessons_58_64


def build():
    all_lessons = lessons_49_51 + lessons_52_57 + lessons_58_64

    data = {
        "metadata": {
            "bookTitle": "新完全マスター JLPT N3 読解",
            "bookTitleRomaji": "Shin Kanzen Master JLPT N3 Dokkai",
            "englishTitle": "New Complete Master JLPT N3 Reading Comprehension",
            "level": "JLPT N3 (Intermediate)",
            "section": "実力養成編 第4部 実戦問題",
            "subSection": "長文・情報検索 (Long Texts & Information Retrieval)",
            "description": "Comprehensive transcription of Shin Kanzen Master JLPT N3 Dokkai Part 4: Practical Test Problems (Problems 49-64, pp. 114-145) including Long Passages (Problems 49-51) and Information Retrieval (Problems 52-64) with complete ruby furigana, comprehensive questions, and bilingual explanations.",
            "version": "1.0.0",
            "lastUpdated": "2026-10-12"
        },
        "lessons": all_lessons
    }

    out_dir = os.path.abspath(os.path.join(script_dir, '../data/reading'))
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part4_long_info.json")

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
