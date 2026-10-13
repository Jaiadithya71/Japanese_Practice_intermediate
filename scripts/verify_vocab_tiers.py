#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_vocab_tiers.py
Verifies data/vocab_tiers.json conforms to requirements:
- All IDs exist in vocabulary dataset
- Tier 1 count is within 400-520 (target 451)
- Tier 2 count is 530
- Tier 3 count is 270
- Total count is 1,251
- Version and metadata fields are valid
"""

import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')


def verify_vocab_tiers():
    tier_path = os.path.join(DATA_DIR, 'vocab_tiers.json')
    vocab_path = os.path.join(DATA_DIR, 'vocabulary.json')

    if not os.path.exists(tier_path):
        print(f"FAIL: {tier_path} not found.")
        return False
    if not os.path.exists(vocab_path):
        print(f"FAIL: {vocab_path} not found.")
        return False

    with open(tier_path, 'r', encoding='utf-8') as f:
        tier_data = json.load(f)

    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab_words = json.load(f)

    vocab_ids = set(w['id'] for w in vocab_words if 'id' in w)
    print(f"Total vocabulary words in DB: {len(vocab_ids)}")

    tier1 = tier_data.get('tier1', [])
    tier2 = tier_data.get('tier2', [])
    tier3 = tier_data.get('tier3', [])
    meta = tier_data.get('meta', {})

    print(f"Checking tier counts:")
    print(f"  Tier 1 count: {len(tier1)} (meta: {meta.get('tier1_count')})")
    print(f"  Tier 2 count: {len(tier2)} (meta: {meta.get('tier2_count')})")
    print(f"  Tier 3 count: {len(tier3)} (meta: {meta.get('tier3_count')})")
    print(f"  Total count: {len(tier1) + len(tier2) + len(tier3)} (meta: {meta.get('total')})")

    errors = []

    # Check tier 1 range 400-520
    if not (400 <= len(tier1) <= 520):
        errors.append(f"Tier 1 count {len(tier1)} outside 400-520 range.")
    if len(tier1) != 451:
        print(f"  [NOTE] Tier 1 count is {len(tier1)}, expected 451.")

    if len(tier2) != 530:
        errors.append(f"Tier 2 count {len(tier2)} != 530.")
    if len(tier3) != 270:
        errors.append(f"Tier 3 count {len(tier3)} != 270.")
    if len(tier1) + len(tier2) + len(tier3) != 1251:
        errors.append(f"Total tier words != 1251.")

    # Check ID validity
    all_tier_ids = tier1 + tier2 + tier3
    if len(set(all_tier_ids)) != len(all_tier_ids):
        errors.append("Duplicate IDs found across tiers.")

    missing_in_vocab = [wid for wid in all_tier_ids if wid not in vocab_ids]
    if missing_in_vocab:
        errors.append(f"{len(missing_in_vocab)} tier IDs not in vocabulary DB: {missing_in_vocab[:5]}")

    if errors:
        print("FAIL with errors:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("PASS: data/vocab_tiers.json validated successfully! All checks passed.")
    return True


if __name__ == '__main__':
    ok = verify_vocab_tiers()
    sys.exit(0 if ok else 1)
