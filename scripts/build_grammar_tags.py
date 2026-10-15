#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_grammar_tags.py
Builds pattern tagging and confusion clusters for Nihongo Intermediate N3 Grammar Drills.

Maps 495 practice drills across Parts 1-3 to grammar pattern IDs and confusion clusters.
Normalisation rule:
- Strip 〜, ~, V-, N-, A-, Na-, +, parentheses, and spaces
- Split alternatives on ・, /, ／
- Match against drill options, prompt, full_sentence, and explanation_ja
- Unmatched drills receive patterns: [], rivals: [], confidence: "auto"

Outputs:
- data/drill_tags.json and data/grammar/drill_tags.json
- data/clusters.json and data/grammar/clusters.json
"""

import os
import sys
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
GRAMMAR_DIR = os.path.join(DATA_DIR, 'grammar')

INDEX_FILE = os.path.join(GRAMMAR_DIR, 'grammar_index.json')

DRILL_FILES = [
    ('p1a', os.path.join(GRAMMAR_DIR, 'part1_sec1_to_6.json')),
    ('p1b', os.path.join(GRAMMAR_DIR, 'part1_sec7_to_12.json')),
    ('p2', os.path.join(GRAMMAR_DIR, 'part2_sentence_grammar2.json')),
    ('p3', os.path.join(GRAMMAR_DIR, 'part3_text_grammar.json'))
]

# 9 Core Grammar Confusion Clusters
CLUSTERS_SEED = [
    {
        "id": "time",
        "name_en": "Time & Timing",
        "name_ja": "時間・時期",
        "patterns": ["P1-1", "P1-2", "P1-3", "P1-4", "P1-7", "P1-9", "P2-74", "P2-75", "P2-76"]
    },
    {
        "id": "cause",
        "name_en": "Cause & Reason",
        "name_ja": "原因・理由",
        "patterns": ["P1-19", "P1-20", "P1-21", "P1-22", "P1-23", "P2-71", "P2-72", "P3-82", "P3-83"]
    },
    {
        "id": "contrast",
        "name_en": "Contrast & Comparison",
        "name_ja": "対比・逆接",
        "patterns": ["P1-14", "P1-15", "P1-16", "P1-17", "P1-18", "P1-38", "P2-54", "P2-55"]
    },
    {
        "id": "inability-compulsion",
        "name_en": "Obligation & Impossibility",
        "name_ja": "義務・不可・禁止・部分否定",
        "patterns": ["P1-34", "P1-35", "P1-36", "P1-37", "P1-42", "P1-43", "P1-44", "P1-45", "P2-59"]
    },
    {
        "id": "purpose-intent",
        "name_en": "Purpose, Volition & Desires",
        "name_ja": "目的・意向・希望・働きかけ",
        "patterns": ["P1-39", "P1-40", "P1-41", "P1-46", "P1-47", "P1-48", "P1-49", "P2-60", "P2-61"]
    },
    {
        "id": "condition",
        "name_en": "Condition & Hypothesis",
        "name_ja": "条件・仮定・反実仮想",
        "patterns": ["P1-5", "P1-6", "P1-8", "P1-24", "P1-25", "P1-26", "P1-27", "P1-28", "P2-56", "P2-57", "P2-62"]
    },
    {
        "id": "degree-limit",
        "name_en": "Degree & Limit",
        "name_ja": "程度・限界・最高",
        "patterns": ["P1-10", "P1-11", "P1-12", "P1-13", "P2-58"]
    },
    {
        "id": "viewpoint-attitude",
        "name_en": "Viewpoint, Attitude & Transmission",
        "name_ja": "視点・伝聞・敬語",
        "patterns": ["P1-29", "P1-30", "P1-31", "P1-32", "P1-33", "P1-50", "P1-51", "P1-52", "P1-53", "P2-65", "P2-77", "P2-78", "P2-79"]
    },
    {
        "id": "form-other",
        "name_en": "Sentence Forms & Cohesion",
        "name_ja": "文型・構文・文の対応",
        "patterns": ["P2-63", "P2-64", "P2-66", "P2-67", "P2-68", "P2-69", "P2-70", "P2-73", "P3-80", "P3-81"]
    }
]


def normalize_pattern(pat_str):
    cleaned = re.sub(r'<[^>]+>', '', pat_str)
    cleaned = cleaned.replace('〜', '').replace('~', '')
    cleaned = re.sub(r'[VNA]-(辞書形|ない形|た形|ている|い|な|の|\w+)?', '', cleaned)
    cleaned = cleaned.replace('+', '').replace('（', '(').replace('）', ')').strip()
    tokens = re.split(r'[・/／]', cleaned)
    res = []
    for t in tokens:
        t = re.sub(r'\(.*?\)', '', t)
        t = t.replace('…', '').strip()
        if len(t) >= 2:
            res.append(t)
    return res


def build_grammar_tags():
    if not os.path.exists(INDEX_FILE):
        raise FileNotFoundError(f"Missing grammar index file: {INDEX_FILE}")

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        grammar_index = json.load(f)

    print(f"Loaded {len(grammar_index)} patterns from grammar_index.json.")
    index_pattern_ids = set(p['id'] for p in grammar_index)

    # Validate all cluster pattern IDs exist in grammar_index
    pattern_to_cluster = {}
    cluster_to_patterns = {}
    for c in CLUSTERS_SEED:
        cid = c['id']
        cluster_to_patterns[cid] = c['patterns']
        for pid in c['patterns']:
            if pid not in index_pattern_ids:
                raise ValueError(f"Cluster '{cid}' contains unknown pattern '{pid}'")
            pattern_to_cluster[pid] = cid

    print("All cluster pattern IDs validated against grammar_index.")

    # Prepare pattern tokens
    pat_tokens = {p['id']: normalize_pattern(p['pattern']) for p in grammar_index}

    # Process all drills across 4 parts
    drill_tags = {}
    total_drills = 0
    matched_drills = 0

    for part_code, file_path in DRILL_FILES:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Missing drill file: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        sections = data.get('sections', [])
        for sec in sections:
            s_num = sec.get('section_number')
            s_str = str(int(s_num)) if isinstance(s_num, (int, float)) and s_num == int(s_num) else str(s_num)
            drills = sec.get('drills', []) or sec.get('practice_drills', [])
            sec_pat_ids = [p['id'] for p in sec.get('patterns', []) if 'id' in p]

            for d_idx, dr in enumerate(drills):
                total_drills += 1
                qid = dr.get('question_id')
                if qid is None:
                    qid = d_idx + 1

                composite_key = f"{part_code}:{s_str}:{qid}"
                if composite_key in drill_tags:
                    raise ValueError(f"Duplicate composite key detected: {composite_key}")

                # Build search blob from options, prompt, full_sentence, explanation_ja
                texts = []
                if 'options' in dr:
                    for opt in dr['options']:
                        texts.append(opt.get('text', '') if isinstance(opt, dict) else str(opt))
                texts.append(dr.get('full_sentence', ''))
                texts.append(dr.get('explanation_ja', ''))
                texts.append(dr.get('prompt', ''))
                search_blob = ' '.join(str(t) for t in texts if t)

                # Find matching pattern IDs
                hits = []
                # First check section patterns
                for pid in sec_pat_ids:
                    for tok in pat_tokens.get(pid, []):
                        if tok in search_blob and pid not in hits:
                            hits.append(pid)

                # Then check all other patterns
                for pid, toks in pat_tokens.items():
                    if pid not in hits:
                        for tok in toks:
                            if tok in search_blob:
                                hits.append(pid)
                                break

                # Determine primary cluster and rivals
                primary_cluster = None
                rivals = []
                if hits:
                    matched_drills += 1
                    primary_pid = hits[0]
                    primary_cluster = pattern_to_cluster.get(primary_pid)
                    if primary_cluster:
                        cluster_pats = cluster_to_patterns.get(primary_cluster, [])
                        rivals = [p for p in cluster_pats if p not in hits]
                else:
                    # Unmatched drill: fallback to section's own patterns or section cluster
                    if sec_pat_ids:
                        primary_cluster = pattern_to_cluster.get(sec_pat_ids[0])

                drill_tags[composite_key] = {
                    "patterns": hits,
                    "cluster": primary_cluster,
                    "rivals": rivals,
                    "section": s_str,
                    "confidence": "auto"
                }

    coverage_pct = (matched_drills / total_drills * 100) if total_drills else 0
    print(f"Grammar tagging complete:")
    print(f"  Total drills processed: {total_drills} (expected 495)")
    print(f"  Drills with pattern match: {matched_drills} ({coverage_pct:.1f}%)")
    print(f"  Unique composite keys: {len(drill_tags)}")

    assert total_drills == 495, f"Expected 495 drills, found {total_drills}"
    assert len(drill_tags) == 495, f"Expected 495 keys, found {len(drill_tags)}"
    assert coverage_pct >= 50.0, f"Coverage {coverage_pct:.1f}% below minimum 50%!"

    # Write drill tags
    out_tags1 = os.path.join(DATA_DIR, 'drill_tags.json')
    out_tags2 = os.path.join(GRAMMAR_DIR, 'drill_tags.json')
    with open(out_tags1, 'w', encoding='utf-8') as f:
        json.dump(drill_tags, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out_tags1}")
    with open(out_tags2, 'w', encoding='utf-8') as f:
        json.dump(drill_tags, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out_tags2}")

    # Write clusters
    clusters_payload = {"clusters": CLUSTERS_SEED}
    out_clus1 = os.path.join(DATA_DIR, 'clusters.json')
    out_clus2 = os.path.join(GRAMMAR_DIR, 'clusters.json')
    with open(out_clus1, 'w', encoding='utf-8') as f:
        json.dump(clusters_payload, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out_clus1}")
    with open(out_clus2, 'w', encoding='utf-8') as f:
        json.dump(clusters_payload, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out_clus2}")


if __name__ == '__main__':
    build_grammar_tags()
