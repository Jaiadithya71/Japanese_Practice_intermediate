#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fills in missing English for vocab example sentences (Part 1 ch11-21).

The transcribed source modules ship example_ja without example_en for these
chapters. data/vocabulary/example_translations.json maps example_ja -> English.
This only fills EMPTY example_en fields; English that ships with the source
is never overwritten. Builders call apply_to_file() after writing their JSON,
and running this script directly repairs data/vocabulary/*.json and
data/vocabulary.json in place.
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSLATIONS = os.path.join(ROOT, 'data', 'vocabulary', 'example_translations.json')


def _load():
    with open(TRANSLATIONS, 'r', encoding='utf-8') as f:
        return json.load(f)


def _fill(obj, tr, stats):
    if isinstance(obj, list):
        for v in obj:
            _fill(v, tr, stats)
    elif isinstance(obj, dict):
        ja = obj.get('example_ja')
        if isinstance(ja, str) and ja.strip() and not (obj.get('example_en') or '').strip():
            en = tr.get(ja)
            if en:
                obj['example_en'] = en
                stats['filled'] += 1
            else:
                stats['missing'] += 1
        for v in obj.values():
            _fill(v, tr, stats)


def apply_to_file(path):
    tr = _load()
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    stats = {'filled': 0, 'missing': 0}
    _fill(data, tr, stats)
    if stats['filled']:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print(f"{os.path.basename(path)}: filled {stats['filled']} example_en, "
          f"{stats['missing']} still without a translation")
    return stats


if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(ROOT, 'data', 'vocabulary', 'part*.json')))
    files.append(os.path.join(ROOT, 'data', 'vocabulary.json'))
    bad = 0
    for p in files:
        bad += apply_to_file(p)['missing']
    raise SystemExit(1 if bad else 0)
