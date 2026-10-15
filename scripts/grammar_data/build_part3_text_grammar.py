"""
Builds nihongo-intermediate/data/grammar/part3_text_grammar.json
Combines Lessons 1-10 and Review Tests (まとめ問題) with full reading passages, cloze questions, and explanations.
"""
import json
import os
import sys

# Ensure utf-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Import extracted modules
sys.path.append(os.path.dirname(__file__))
from G4_extracted.part3_lessons_1_to_4 import get_lessons_1_to_4
from G4_extracted.part3_lessons_5_to_8 import get_lessons_5_to_8
from G4_extracted.part3_lessons_9_to_10 import get_lessons_9_to_10

def build_part3_text_grammar():
    l1_4 = get_lessons_1_to_4()
    l5_8 = get_lessons_5_to_8()
    l9_10 = get_lessons_9_to_10()

    all_sections = l1_4 + l5_8 + l9_10

    # Extract all passages into top-level passages list
    all_passages = []
    for section in all_sections:
        if "passages" in section:
            for p in section["passages"]:
                all_passages.append(p)

    output_data = {
        "metadata": {
            "part": 3,
            "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby> <ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>",
            "title_en": "Part 3: Text Grammar (Passage-level Grammar & Cloze Reading)",
            "description": "Comprehensive dataset for Shin Kanzen Master JLPT N3 Grammar Part 3 (文章の文法). Covers sentence structure, cohesion, tense/aspect, viewpoint markers, demonstratives, topic/subject particles, conjunctions, style consistency, plus 10 complete cloze reading comprehension passages with questions, answers, and explanations.",
            "source_pages": "P116 ~ P145 (Images 118 ~ 147)",
            "total_lessons": 10,
            "total_review_sections": 5,
            "total_passages": len(all_passages),
            "total_cloze_questions": sum(len(p.get("questions", [])) for p in all_passages),
        },
        "sections": all_sections,
        "passages": all_passages
    }

    out_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "grammar", "part3_text_grammar.json")
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {out_path}")
    print(f"Sections: {len(all_sections)}, Passages: {len(all_passages)}, Questions: {output_data['metadata']['total_cloze_questions']}")

if __name__ == "__main__":
    build_part3_text_grammar()
