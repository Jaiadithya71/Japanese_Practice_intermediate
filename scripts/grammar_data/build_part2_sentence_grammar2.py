"""
Builder script for Shin Kanzen Master JLPT N3 Grammar:
Part 1 Review Units F-J, Part 2 Lessons 1-4, and Part 3 Lessons 1-3.
Images 086 to 125 inclusive.

Outputs to: nihongo-intermediate/data/grammar/part2_sentence_grammar2.json
"""

import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Add G3_extracted to path
current_dir = Path(__file__).resolve().parent
extracted_dir = current_dir / "G3_extracted"
sys.path.insert(0, str(extracted_dir))

from part1_review_f_to_j import get_part1_review_sections
from part2_lessons_1_to_4 import get_part2_lessons_sections
from part3_lessons_1_to_3 import get_part3_lessons_sections

def build_part2_sentence_grammar2():
    print("Loading Section 1-6 (Part 1 Review F to J + まとめ問題 A〜J)...")
    sec_1_to_6 = get_part1_review_sections()
    print(f"Loaded {len(sec_1_to_6)} sections, {sum(len(s.get('drills', [])) for s in sec_1_to_6)} drills.")

    print("Loading Section 7-11 (Part 2 Lessons 1-4 + まとめ問題 1〜4課)...")
    sec_7_to_11 = get_part2_lessons_sections()
    print(f"Loaded {len(sec_7_to_11)} sections, {sum(len(s.get('drills', [])) for s in sec_7_to_11)} drills.")

    print("Loading Section 12-15 (Part 3 Lessons 1-3 + まとめ問題 1〜2課)...")
    sec_12_to_15 = get_part3_lessons_sections()
    print(f"Loaded {len(sec_12_to_15)} sections, {sum(len(s.get('drills', [])) for s in sec_12_to_15)} drills.")

    all_sections = sec_1_to_6 + sec_7_to_11 + sec_12_to_15

    total_drills = sum(len(s.get('drills', [])) for s in all_sections)
    total_patterns = sum(len(s.get('patterns', [])) for s in all_sections)

    dataset = {
        "part_title": "<ruby>実力養成編<rt>じつりょくようせいへん</rt></ruby> <ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>〜<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby>（<ruby>復習<rt>ふくしゅう</rt></ruby>F〜J・<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby>・<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby>1〜3<ruby>課<rt>か</rt></ruby>）",
        "part_title_en": "Shin Kanzen Master JLPT N3 Grammar: Part 1 Review F-J, Part 2 (Lessons 1-4 & Review), Part 3 (Lessons 1-3 & Review)",
        "scope_images": "086 to 125",
        "total_sections": len(all_sections),
        "total_grammar_patterns": total_patterns,
        "total_drills": total_drills,
        "sections": all_sections
    }

    # Determine output path
    base_dir = Path(__file__).resolve().parent.parent.parent
    output_path = base_dir / "data" / "grammar" / "part2_sentence_grammar2.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Writing {len(all_sections)} sections ({total_drills} drills) to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {output_path} ({os.path.getsize(output_path)} bytes).")
    return output_path

if __name__ == "__main__":
    build_part2_sentence_grammar2()
