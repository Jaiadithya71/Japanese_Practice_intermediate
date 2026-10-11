import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Add parent scripts directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import modules
from vocab_data.part2_ch05 import part2_ch05_data
from vocab_data.part2_ch06 import part2_ch06_data
from vocab_data.part2_ch07 import part2_ch07_data
from vocab_data.part2_ch08 import part2_ch08_data

def build():
    data = {
        "metadata": {
            "title": "新にほんご500問 N3 語彙編 (Vocabulary) - 第2部 性質別 5課〜8課",
            "part": "part_2",
            "chapters_range": "5-8",
            "description": "Vocabulary data transcribed from Nihongo 500 Mon N3 Vocabulary Part 2 (Characteristics) Chapters 5-8 with complete ruby furigana, warming up, yattemiyou drills, and exercises.",
            "version": "1.0.0"
        },
        "chapters": [
            part2_ch05_data,
            part2_ch06_data,
            part2_ch07_data,
            part2_ch08_data
        ]
    }

    out_dir = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\vocabulary"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part2_characteristics_ch05_08.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")

if __name__ == "__main__":
    build()
