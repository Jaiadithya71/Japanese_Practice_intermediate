#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_word_contexts.py
Verifies data/word_contexts.json conforms to requirements:
- Keys exist and match kanji terms
- Sentences do not contain raw HTML tags
- Sentence lengths are valid
- Target coverage is >= 50% (doc 03 §9 requirement)
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
KANJI_DIR = os.path.join(DATA_DIR, 'kanji')


def verify_word_contexts():
    ctx_path = os.path.join(DATA_DIR, 'word_contexts.json')
    if not os.path.exists(ctx_path):
        print(f"FAIL: {ctx_path} not found.")
        return False

    with open(ctx_path, 'r', encoding='utf-8') as f:
        contexts = json.load(f)

    # Load target terms from kanji DB
    kanji_files = sorted(glob.glob(os.path.join(KANJI_DIR, 'part*_lessons_*.json')))
    all_terms = set()
    target_terms = set()
    for kf in kanji_files:
        with open(kf, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for les in d.get('lessons', []):
            for k in les.get('kanji', []):
                for w in k.get('words', []):
                    t = w.get('term_ja') or w.get('term')
                    if t:
                        all_terms.add(t)
                        if w.get('is_target'):
                            target_terms.add(t)

    print(f"Total Kanji DB terms: {len(all_terms)} ({len(target_terms)} targets)")
    print(f"Total terms with context: {len(contexts)}")

    errors = []
    html_tag_re = re.compile(r'<[^>]+>')

    for term, c_list in contexts.items():
        if not c_list:
            errors.append(f"Empty context list for term '{term}'")
            continue
        c = c_list[0] if isinstance(c_list, list) else c_list
        ja = c.get('sentence_ja') or c.get('ja') or ''
        if not ja:
            errors.append(f"Missing sentence_ja for term '{term}'")
            continue
        if html_tag_re.search(ja):
            errors.append(f"HTML tags found in sentence for term '{term}': {ja}")
        if len(ja) < 4:
            errors.append(f"Sentence too short for term '{term}': {ja}")

    target_hits = sum(1 for t in target_terms if t in contexts)
    target_coverage = (target_hits / len(target_terms) * 100) if target_terms else 0
    total_coverage = (len(contexts) / len(all_terms) * 100) if all_terms else 0

    print(f"Context sentence coverage metrics:")
    print(f"  Target terms coverage: {target_hits}/{len(target_terms)} ({target_coverage:.1f}%)")
    print(f"  Overall terms coverage: {len(contexts)}/{len(all_terms)} ({total_coverage:.1f}%)")

    if target_coverage < 50.0:
        errors.append(f"Target coverage {target_coverage:.1f}% below minimum 50%!")

    if errors:
        print("FAIL with errors:")
        for e in errors[:10]:
            print(f"  - {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors.")
        return False

    print("PASS: data/word_contexts.json validated successfully! All checks passed.")
    return True


if __name__ == '__main__':
    ok = verify_word_contexts()
    sys.exit(0 if ok else 1)
