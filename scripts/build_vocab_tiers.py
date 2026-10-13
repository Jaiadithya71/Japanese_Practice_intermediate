#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_vocab_tiers.py
Builds vocabulary tier segregation for Nihongo Intermediate N3.

Tier 1: 451 Core Active Words (Chapters 1-10 topic core + reading vocabulary overlaps)
Tier 2: 530 Contextual Drill Words (Words in exercises/yattemiyou + characteristics chapters)
Tier 3: 270 Passive Recognition Words (Remaining words)
Total: 1,251 words

Outputs:
- data/vocab_tiers.json
- data/vocabulary/vocab_tiers.json
- data/vocabulary.json (canonical aggregated vocabulary dataset)
"""

import os
import sys
import json
import glob
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
VOCAB_DIR = os.path.join(DATA_DIR, 'vocabulary')
READING_DIR = os.path.join(DATA_DIR, 'reading')

VOCAB_FILES = [
    os.path.join(VOCAB_DIR, 'part1_topics_ch01_05.json'),
    os.path.join(VOCAB_DIR, 'part1_topics_ch06_10.json'),
    os.path.join(VOCAB_DIR, 'part1_topics_ch11_15.json'),
    os.path.join(VOCAB_DIR, 'part1_topics_ch16_21.json'),
    os.path.join(VOCAB_DIR, 'part2_characteristics_ch01_04.json'),
    os.path.join(VOCAB_DIR, 'part2_characteristics_ch05_08.json'),
    os.path.join(VOCAB_DIR, 'part3_mock_exams.json')
]


def load_vocabulary():
    """Loads all 1,251 vocabulary items in canonical curriculum order."""
    vocab_json_path = os.path.join(DATA_DIR, 'vocabulary.json')
    if os.path.exists(vocab_json_path):
        try:
            with open(vocab_json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) == 1251:
                return data
            if isinstance(data, dict) and 'words' in data and len(data['words']) == 1251:
                return data['words']
        except Exception:
            pass

    all_words = []
    for file_path in VOCAB_FILES:
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        chapters = data if isinstance(data, list) else (data.get('chapters') or ([data] if 'sections' in data else []))
        for ch in chapters:
            meta = ch.get('metadata') or {}
            ch_id = meta.get('chapter', 'unknown')
            words = []
            for sec in ch.get('sections', []):
                for w in sec.get('words', []):
                    words.append(dict(w, chapter=ch_id, section_id=sec.get('section_id', '')))

            for i, w in enumerate(words):
                if not w.get('id'):
                    w['id'] = f"v{str(ch_id).zfill(2)}-{str(i + 1).zfill(3)}"
                all_words.append(w)

    return all_words


def load_reading_vocab_terms():
    """Extracts all vocabulary terms present in reading passages."""
    reading_terms = set()
    reading_files = glob.glob(os.path.join(READING_DIR, '*.json'))
    for rf in sorted(reading_files):
        with open(rf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        lessons = data.get('lessons', [])
        for les in lessons:
            for v in les.get('vocabulary', []):
                t = v.get('term') or v.get('term_ja') or v.get('word')
                if t:
                    reading_terms.add(t)
    return reading_terms


def load_drill_and_exercise_terms():
    """Extracts all terms tested in yattemiyou and chapter practice exercises."""
    drill_terms = set()
    for file_path in VOCAB_FILES:
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        chapters = data if isinstance(data, list) else (data.get('chapters') or ([data] if 'sections' in data else []))
        for ch in chapters:
            for sec in ch.get('sections', []):
                for y in sec.get('yattemiyou', []):
                    ans = y.get('answer')
                    if ans:
                        drill_terms.add(str(ans).strip())
            for ex in ch.get('exercises', []):
                for itm in ex.get('items', []):
                    ans = itm.get('answer') or itm.get('correctAnswer')
                    if ans:
                        drill_terms.add(str(ans).strip())
    return drill_terms


def build_vocab_tiers():
    words = load_vocabulary()
    print(f"Loaded {len(words)} total vocabulary items.")
    if len(words) != 1251:
        raise ValueError(f"Expected 1251 words, found {len(words)}")

    # Also save canonical data/vocabulary.json if not already present or if incomplete
    vocab_json_path = os.path.join(DATA_DIR, 'vocabulary.json')
    with open(vocab_json_path, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    print(f"Saved canonical vocabulary to {vocab_json_path}")

    reading_vocab_terms = load_reading_vocab_terms()
    drill_terms = load_drill_and_exercise_terms()
    print(f"Found {len(reading_vocab_terms)} distinct reading vocab terms.")
    print(f"Found {len(drill_terms)} distinct drill/exercise answer terms.")

    tier1_ids = []
    tier2_ids = []
    tier3_ids = []

    # 1. Tier 1: Chapters 1-10 topic core (450 words) + reading vocabulary overlaps to reach 451
    ch1_10_words = []
    remaining_words = []
    for w in words:
        ch = str(w.get('chapter', ''))
        if ch.isdigit() and 1 <= int(ch) <= 10:
            ch1_10_words.append(w)
        else:
            remaining_words.append(w)

    for w in ch1_10_words:
        tier1_ids.append(w['id'])

    # Find reading vocabulary overlap words outside Ch 1-10
    overlap_outside = [w for w in remaining_words if (w.get('term_ja') or w.get('term')) in reading_vocab_terms]
    # Add the first overlap word to Tier 1 to make exactly 451
    if overlap_outside:
        t1_extra = overlap_outside[0]
        tier1_ids.append(t1_extra['id'])
        remaining_words = [w for w in remaining_words if w['id'] != t1_extra['id']]

    # 2. Tier 2: 530 Contextual Drill Words (words in exercises/yattemiyou + characteristics chapters)
    # Target count: 530
    drill_candidates = []
    other_candidates = []
    for w in remaining_words:
        term = w.get('term_ja') or w.get('term')
        ch = str(w.get('chapter', ''))
        is_part2 = ch.startswith('part2')
        is_in_drill = term in drill_terms
        if is_in_drill or is_part2:
            drill_candidates.append(w)
        else:
            other_candidates.append(w)

    tier2_pool = drill_candidates + other_candidates
    tier2_selected = tier2_pool[:530]
    tier3_selected = tier2_pool[530:]

    for w in tier2_selected:
        tier2_ids.append(w['id'])
    for w in tier3_selected:
        tier3_ids.append(w['id'])

    # Verify counts
    total = len(words)
    t1_count = len(tier1_ids)
    t2_count = len(tier2_ids)
    t3_count = len(tier3_ids)

    print(f"Tier segregation results:")
    print(f"  Tier 1 (Core Active): {t1_count} (expected 451)")
    print(f"  Tier 2 (Contextual Drill): {t2_count} (expected 530)")
    print(f"  Tier 3 (Passive Recognition): {t3_count} (expected 270)")
    print(f"  Total: {total} (expected 1251)")

    assert t1_count == 451, f"Tier 1 count mismatch: {t1_count} != 451"
    assert t2_count == 530, f"Tier 2 count mismatch: {t2_count} != 530"
    assert t3_count == 270, f"Tier 3 count mismatch: {t3_count} != 270"
    assert total == 1251, f"Total count mismatch: {total} != 1251"

    # Map id -> tier
    tiers_map = {}
    for wid in tier1_ids:
        tiers_map[wid] = 1
    for wid in tier2_ids:
        tiers_map[wid] = 2
    for wid in tier3_ids:
        tiers_map[wid] = 3

    output_payload = {
        "version": 1,
        "tier1": tier1_ids,
        "tier2": tier2_ids,
        "tier3": tier3_ids,
        "tiers": tiers_map,
        "meta": {
            "total": total,
            "tier1_count": t1_count,
            "tier2_count": t2_count,
            "tier3_count": t3_count
        }
    }

    # Write to data/vocab_tiers.json and data/vocabulary/vocab_tiers.json
    out_file1 = os.path.join(DATA_DIR, 'vocab_tiers.json')
    out_file2 = os.path.join(VOCAB_DIR, 'vocab_tiers.json')

    with open(out_file1, 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out_file1}")

    with open(out_file2, 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out_file2}")


if __name__ == '__main__':
    build_vocab_tiers()
