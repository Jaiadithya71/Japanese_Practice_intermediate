# -*- coding: utf-8 -*-
"""
Builder script to assemble Chapters 16-21 and Review Tests 4 & 5
into nihongo-intermediate/data/vocabulary/part1_topics_ch16_21.json
"""

import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Ensure script directory is on sys.path so vocab_data modules can be imported
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from vocab_data.ch16 import ch16_data
from vocab_data.ch17 import ch17_data
from vocab_data.ch18 import ch18_data
from vocab_data.ch19 import ch19_data
from vocab_data.review04 import review04_data
from vocab_data.ch20 import ch20_data
from vocab_data.ch21 import ch21_data
from vocab_data.review05 import review05_data

def build():
    data = {
        "title": "Part 1 Topics Chapters 16-21 & Review Tests 4 & 5",
        "part": 1,
        "metadata": {
            "title": "新にほんご500問 N3 語彙編 (Vocabulary) - 第1部 16課〜21課 & 実力を試そう4・5",
            "part": "part_1",
            "chapters_range": "16-21",
            "description": "Vocabulary data transcribed from Nihongo 500 Mon N3 Vocabulary Chapters 16-21 and Review Tests 4 and 5 with complete ruby furigana, warming up, yattemiyou drills, and exercises.",
            "version": "1.0.0"
        },
        "chapters": [
            ch16_data,
            ch17_data,
            ch18_data,
            ch19_data,
            review04_data,
            ch20_data,
            ch21_data,
            review05_data
        ]
    }

    out_dir = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\vocabulary"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part1_topics_ch16_21.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")
    print(f"Total units included: {len(data['chapters'])}")

if __name__ == "__main__":
    build()
