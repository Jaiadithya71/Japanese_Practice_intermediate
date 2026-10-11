import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Add parent scripts directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import modules
from vocab_data.ch01 import ch01_data
from vocab_data.ch02 import ch02_data
from vocab_data.ch03 import ch03_data
from vocab_data.ch04 import ch04_data
from vocab_data.ch05 import ch05_data
from vocab_data.review01 import review01_data

def build():
    data = {
        "metadata": {
            "title": "新にほんご500問 N3 語彙編 (Vocabulary) - 第1部 1課〜5課",
            "part": "part_1",
            "chapters_range": "1-5",
            "description": "Vocabulary data transcribed from Nihongo 500 Mon N3 Vocabulary Chapters 1-5 and Review Test 1 with complete ruby furigana, warming up, yattemiyou drills, and exercises.",
            "version": "1.0.0"
        },
        "chapters": [
            ch01_data,
            ch02_data,
            ch03_data,
            ch04_data,
            ch05_data,
            review01_data
        ]
    }

    out_dir = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\vocabulary"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part1_topics_ch01_05.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")

if __name__ == "__main__":
    build()
