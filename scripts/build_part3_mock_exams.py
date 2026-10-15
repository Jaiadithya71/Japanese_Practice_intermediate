import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

# Add parent scripts directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import modules
from vocab_data.part3_mock01 import part3_mock01_data
from vocab_data.part3_mock02 import part3_mock02_data

def build():
    data = {
        "metadata": {
            "title": "新にほんご500問 N3 語彙編 (Vocabulary) - 第3部 模擬試験 (第1回・第2回)",
            "part": "part_3",
            "exam_count": 2,
            "description": "Vocabulary mock exams transcribed from Nihongo 500 Mon N3 Vocabulary Part 3 (Mock Exams 1 and 2), covering JLPT N3 Vocabulary questions 1-20 (Mondai 3: Contextual Blank Fill, Mondai 4: Paraphrasing, Mondai 5: Proper Usage).",
            "version": "1.0.0"
        },
        "chapters": [
            part3_mock01_data,
            part3_mock02_data
        ]
    }

    out_dir = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\vocabulary"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "part3_mock_exams.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated: {out_file}")
    print(f"File size: {os.path.getsize(out_file):,} bytes")

if __name__ == "__main__":
    build()
