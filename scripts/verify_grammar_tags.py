#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_grammar_tags.py
Verifies grammar tags and clusters integrity against doc 03 §9 specifications:
- Composite keys are unique (495 drills -> 495 keys)
- Every tagged pattern id exists in grammar_index.json
- Every cluster pattern exists in grammar_index.json
- Coverage % is printed (fails if below 50%)
- Star items have correct_order of length 4
"""

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
GRAMMAR_DIR = os.path.join(DATA_DIR, 'grammar')


def verify_grammar_tags():
    tags_path = os.path.join(DATA_DIR, 'drill_tags.json')
    clus_path = os.path.join(DATA_DIR, 'clusters.json')
    idx_path = os.path.join(GRAMMAR_DIR, 'grammar_index.json')
    p2_path = os.path.join(GRAMMAR_DIR, 'part2_sentence_grammar2.json')

    for p in [tags_path, clus_path, idx_path, p2_path]:
        if not os.path.exists(p):
            print(f"FAIL: Missing file {p}")
            return False

    with open(idx_path, 'r', encoding='utf-8') as f:
        grammar_index = json.load(f)
    index_ids = set(p['id'] for p in grammar_index)

    with open(clus_path, 'r', encoding='utf-8') as f:
        clusters_data = json.load(f)
    clusters = clusters_data.get('clusters', [])

    with open(tags_path, 'r', encoding='utf-8') as f:
        drill_tags = json.load(f)

    with open(p2_path, 'r', encoding='utf-8') as f:
        p2_data = json.load(f)

    errors = []

    # 1. Check composite keys count and uniqueness
    keys = list(drill_tags.keys())
    print(f"Total drill keys: {len(keys)}")
    if len(keys) != 495:
        errors.append(f"Expected 495 drill keys, found {len(keys)}")
    if len(set(keys)) != len(keys):
        errors.append("Duplicate keys found in drill_tags.json")

    # 2. Check cluster patterns
    cluster_pattern_ids = set()
    for c in clusters:
        for pid in c.get('patterns', []):
            if pid not in index_ids:
                errors.append(f"Cluster pattern '{pid}' not in grammar_index.json")
            cluster_pattern_ids.add(pid)
    print(f"Verified {len(clusters)} clusters ({len(cluster_pattern_ids)} pattern mappings).")

    # 3. Check tagged pattern IDs and coverage
    matched_drills = 0
    for k, tag in drill_tags.items():
        pats = tag.get('patterns', [])
        if pats:
            matched_drills += 1
            for pid in pats:
                if pid not in index_ids:
                    errors.append(f"Drill {k} tagged with unknown pattern '{pid}'")
        rivs = tag.get('rivals', [])
        for r in rivs:
            if r not in index_ids:
                errors.append(f"Drill {k} has unknown rival pattern '{r}'")

    coverage_pct = (matched_drills / len(keys) * 100) if keys else 0
    print(f"Drill coverage: {matched_drills}/{len(keys)} ({coverage_pct:.1f}%)")
    if coverage_pct < 50.0:
        errors.append(f"Coverage {coverage_pct:.1f}% below minimum 50%!")

    # 4. Check star items have correct_order of length 4
    star_items_checked = 0
    for sec in p2_data.get('sections', []):
        for dr in sec.get('drills', []):
            if 'correct_order' in dr:
                star_items_checked += 1
                order = dr['correct_order']
                if not isinstance(order, list) or len(order) != 4:
                    errors.append(f"Star item {dr.get('question_id')} has invalid correct_order: {order}")

    print(f"Verified {star_items_checked} star items with 4-item correct_order.")
    if star_items_checked == 0:
        errors.append("No star items with correct_order found in Part 2 data.")

    if errors:
        print("FAIL with errors:")
        for e in errors[:10]:
            print(f"  - {e}")
        return False

    print("PASS: Grammar tags, clusters, and star items verified successfully!")
    return True


if __name__ == '__main__':
    ok = verify_grammar_tags()
    sys.exit(0 if ok else 1)
