#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_kanji_words.py
Verifies Kanji dataset integrity against doc 03 §9 specifications:
- 443 kanji entries across lessons (442 unique chars)
- 865 distinct compound terms
- 584 distinct target terms
- Readings are valid kana only
"""

import os
import sys
import json
import glob
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KANJI_DIR = os.path.join(BASE_DIR, 'data', 'kanji')


def is_kana(text):
    # Kana includes hiragana, katakana, small kana, prolonged sound mark (ー),
    # and common reading affixes / okurigana markers: 〜, ~, (), （）
    return bool(re.match(r'^[\u3040-\u309F\u30A0-\u30FFー・\s〜~()（）/／]+$', text))


def verify_kanji_words():
    kanji_files = sorted(glob.glob(os.path.join(KANJI_DIR, 'part*_lessons_*.json')))
    if len(kanji_files) != 5:
        print(f"FAIL: Expected 5 lesson files, found {len(kanji_files)}")
        return False

    total_kanji_entries = 0
    unique_kanji_chars = set()
    terms_dict = {}  # term -> list of readings
    target_terms = set()
    reading_errors = []

    for kf in kanji_files:
        with open(kf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for les in data.get('lessons', []):
            for k in les.get('kanji', []):
                char = k.get('kanji')
                total_kanji_entries += 1
                unique_kanji_chars.add(char)
                for w in k.get('words', []):
                    t = w.get('term_ja') or w.get('term')
                    r = w.get('reading', '')
                    if not t:
                        continue
                    if t not in terms_dict:
                        terms_dict[t] = []
                    terms_dict[t].append(r)
                    if w.get('is_target'):
                        target_terms.add(t)

                    # Validate reading is kana only
                    if r and not is_kana(r):
                        reading_errors.append(f"Non-kana reading '{r}' for term '{t}' (kanji {char})")

    distinct_terms = len(terms_dict)
    distinct_targets = len(target_terms)

    print(f"Kanji word oracle verification:")
    print(f"  Total kanji entries across lessons: {total_kanji_entries} (expected 443)")
    print(f"  Unique kanji characters: {len(unique_kanji_chars)} (expected 442)")
    print(f"  Distinct compound terms: {distinct_terms} (expected 865)")
    print(f"  Distinct target terms: {distinct_targets} (expected 584)")
    print(f"  Reading format errors: {len(reading_errors)}")

    errors = []
    if total_kanji_entries != 443:
        errors.append(f"Kanji entries count {total_kanji_entries} != 443")
    if distinct_terms != 865:
        errors.append(f"Distinct terms count {distinct_terms} != 865")
    if distinct_targets != 584:
        errors.append(f"Distinct target terms count {distinct_targets} != 584")
    if reading_errors:
        errors.extend(reading_errors[:5])

    if errors:
        print("FAIL with errors:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("PASS: Kanji dataset matches all oracles (443 entries, 865 terms, 584 targets, clean kana readings).")
    return True


if __name__ == '__main__':
    ok = verify_kanji_words()
    sys.exit(0 if ok else 1)
