"""
Script to build nihongo-intermediate/data/grammar/part1_sec7_to_12.json
Transcribes Images 040 - 061:
- Part 1: 文の文法 1 (Sentence Grammar 1)
- Section 7 (7課: 〜だそうだ) Patterns 1-5, Drills (Q1-8)
- Section 8 (8課: 絶対〜ない・必ず〜とは言えない) Patterns 1-5, Drills (Q1-8)
- Practice Drills 7・8課 (Q1-10)
- まとめ問題 1〜8課 (Review Test 2, Q1-13)
- Section 9 (9課: 〜と望む) Patterns 1-3, Drills (Q1-8)
- Section 10 (10課: 〜したほうがいい・〜なさい) Patterns 1-4, Drills (Q1-10)
- Practice Drills 9・10課 (Q1-9)
- Section 11 (11課: 〜(よ)うと思う) Patterns 1-4, Drills (Q1-9)
- Section 12 (12課: 敬語) Patterns 1-4, Drills (Q1-9)
- Practice Drills 11・12課 (Q1-8)
- まとめ問題 1〜12課 (Review Test 3, Q1-13)
"""

import json
import sys
from pathlib import Path

# Add script directory to sys.path
sys.path.append(str(Path(__file__).parent))

from build_sec7_8 import (
    sec7_patterns, sec7_drills,
    sec8_patterns, sec8_drills,
    sec7_8_combined_drills, matome_1_to_8_drills
)
from build_sec9_10 import (
    sec9_patterns, sec9_drills,
    sec10_patterns, sec10_drills,
    sec9_10_combined_drills
)
from build_sec11_12 import (
    sec11_patterns, sec11_drills,
    sec12_patterns, sec12_drills,
    sec11_12_combined_drills, matome_1_to_12_drills
)

# Assemble sections data
sections_data = [
    {
        "section_number": 7,
        "title": "<ruby>第<rt>だい</rt></ruby>7<ruby>課<rt>か</rt></ruby> 〜だそうだ",
        "title_en": "Lesson 7: Hearsay",
        "theme": "<ruby>伝聞<rt>でんぶん</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec7_patterns,
        "drills": sec7_drills
    },
    {
        "section_number": 8,
        "title": "<ruby>第<rt>だい</rt></ruby>8<ruby>課<rt>か</rt></ruby> <ruby>絶対<rt>ぜったい</rt></ruby>〜ない・<ruby>必<rt>かなら</rt></ruby>ず〜とは<ruby>言<rt>い</rt></ruby>えない",
        "title_en": "Lesson 8: Absolute & Partial Negation",
        "theme": "<ruby>否定<rt>ひてい</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec8_patterns,
        "drills": sec8_drills + sec7_8_combined_drills + matome_1_to_8_drills
    },
    {
        "section_number": 9,
        "title": "<ruby>第<rt>だい</rt></ruby>9<ruby>課<rt>か</rt></ruby> 〜と<ruby>望<rt>のぞ</rt></ruby>む",
        "title_en": "Lesson 9: Desires & Wishes",
        "theme": "<ruby>希望<rt>きぼう</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec9_patterns,
        "drills": sec9_drills
    },
    {
        "section_number": 10,
        "title": "<ruby>第<rt>だい</rt></ruby>10<ruby>課<rt>か</rt></ruby> 〜したほうがいい・〜なさい",
        "title_en": "Lesson 10: Suggestions, Advice & Commands",
        "theme": "<ruby>勧誘<rt>かんゆう</rt></ruby>・<ruby>助言<rt>じょげん</rt></ruby>・<ruby>命令<rt>めいれい</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec10_patterns,
        "drills": sec10_drills + sec9_10_combined_drills
    },
    {
        "section_number": 11,
        "title": "<ruby>第<rt>だい</rt></ruby>11<ruby>課<rt>か</rt></ruby> 〜（よ）うと<ruby>思<rt>おも</rt></ruby>う",
        "title_en": "Lesson 11: Intentions & Decisions",
        "theme": "<ruby>意図<rt>いと</rt></ruby>・<ruby>決意<rt>けつい</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec11_patterns,
        "drills": sec11_drills
    },
    {
        "section_number": 12,
        "title": "<ruby>第<rt>だい</rt></ruby>12<ruby>課<rt>か</rt></ruby> <ruby>敬語<rt>けいご</rt></ruby>",
        "title_en": "Lesson 12: Honorific Language (Keigo)",
        "theme": "<ruby>敬語<rt>けいご</rt></ruby>",
        "patterns": sec12_patterns,
        "drills": sec12_drills + sec11_12_combined_drills + matome_1_to_12_drills
    }
]

final_output = {
    "metadata": {
        "book_title": "<ruby>新完全<rt>しんかんぜん</rt></ruby>マスター<ruby>文法<rt>ぶんぽう</rt></ruby> <ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby> N3",
        "part_number": 1,
        "part_name": "<ruby>実力養成編<rt>じつりょくようせいへん</rt></ruby> <ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>1",
        "part_name_en": "Part 1: Sentence Grammar 1 (Meaning & Function)",
        "sections_included": [7, 8, 9, 10, 11, 12],
        "pages_covered": "p.36 - p.57 (Images 040-061)"
    },
    "sections": sections_data
}

if __name__ == "__main__":
    target_file = Path("nihongo-intermediate/data/grammar/part1_sec7_to_12.json")
    target_file.parent.mkdir(parents=True, exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {target_file}")
    print(f"Total sections: {len(sections_data)}")
    total_patterns = sum(len(sec["patterns"]) for sec in sections_data)
    total_drills = sum(len(sec["drills"]) for sec in sections_data)
    print(f"Total patterns: {total_patterns}")
    print(f"Total drills: {total_drills}")
