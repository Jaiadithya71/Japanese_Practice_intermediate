import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Import modules
from vocab_data.ch06 import ch06_data
from vocab_data.ch07 import ch07_data
from vocab_data.ch08 import ch08_data
from vocab_data.ch09 import ch09_data
from vocab_data.ch10 import ch10_data
from vocab_data.review02 import review02_data

def build():
    data = {
        "metadata": {
            "title": "新にほんご500問 N3 語彙編 (Vocabulary) - 第1部 6課〜10課",
            "part": "part_1",
            "chapters_range": "6-10",
            "description": "Vocabulary data transcribed from Nihongo 500 Mon N3 Vocabulary Chapters 6-10 and Review Test 2 with complete ruby furigana, warming up, yattemiyou drills, and exercises.",
            "version": "1.0.0"
        },
        "chapters": [
            ch06_data,
            ch07_data,
            ch08_data,
            ch09_data,
            ch10_data,
            review02_data
        ]
    }

    out_dir = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\vocabulary"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part1_topics_ch06_10.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")

if __name__ == "__main__":
    build()
