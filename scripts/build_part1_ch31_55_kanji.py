#!/usr/bin/env python3
"""Rebuild the Home K (kanji-book) lessons so they map 1:1 to the kanji book's
own 25 lessons (data/kanji/part*_lessons_*.json).

Input:  data/vocabulary/part1_topics_ch31_45_kanji.json  (578 words that are
        not already covered by other Home lessons, in kanji-book order)
Output: data/vocabulary/part1_topics_ch31_55_kanji.json  (chapter id = 30 +
        book lesson number, so Home label K<n> == kanji book lesson <n>)

Word ids from the previous file are preserved explicitly, so SRS progress
keyed by word id survives the regrouping.
"""
import json
from collections import Counter, defaultdict

KANJI_FILES = [
    'data/kanji/part1_lessons_01_05.json',
    'data/kanji/part2_lessons_06_10.json',
    'data/kanji/part3_lessons_11_15.json',
    'data/kanji/part4_lessons_16_20.json',
    'data/kanji/part5_lessons_21_25.json',
]
OLD_FILE = 'data/vocabulary/part1_topics_ch31_45_kanji.json'
NEW_FILE = 'data/vocabulary/part1_topics_ch31_55_kanji.json'

# Kanji book lessons in order: (lesson_number, title_ja, title_en, page, words)
book = []
for f in KANJI_FILES:
    d = json.load(open(f))
    for l in d['lessons']:
        ws = [(w['term_ja'], w['reading']) for kj in l['kanji'] for w in kj['words']]
        book.append((l['lesson_number'], l['title_ja'], l['title_en'], l.get('page'), ws))
assert len(book) == 25, len(book)

# First book lesson each (term, reading) appears in
word2lesson = {}
for ln, _tj, _te, _pg, ws in book:
    for term, reading in ws:
        word2lesson.setdefault((term, reading), ln)

# Current K words with the ids the app derived for them (loader: v<ch>-<idx>)
old = json.load(open(OLD_FILE))['chapters']
by_lesson = defaultdict(list)
total = 0
for ch in old:
    n = ch['metadata']['chapter']
    for i, w in enumerate(ch['sections'][0]['words']):
        w = dict(w)
        w['id'] = w.get('id') or 'v' + str(n).zfill(2) + '-' + str(i + 1).zfill(3)
        ln = word2lesson.get((w['term_ja'], w['reading']))
        assert ln, f"no book lesson for {w['term_ja']} {w['reading']}"
        w['kanji_lesson'] = ln
        by_lesson[ln].append(w)
        total += 1

chapters = []
for ln, tj, te, pg, _ws in book:
    words = by_lesson.get(ln)
    if not words:
        continue
    ch_num = 30 + ln
    chapters.append({
        'metadata': {
            'chapter': ch_num,
            'part': 1,
            'topic_ja': tj,
            'topic_en': te,
            'pages': [pg] if pg else [],
        },
        'sections': [{
            'section_id': f'ch{ch_num}_s1',
            'title_ja': tj,
            'title_en': te,
            'words': words,
        }],
    })

ids = [w['id'] for c in chapters for w in c['sections'][0]['words']]
assert len(ids) == len(set(ids)) == total, 'id uniqueness broken'

json.dump({'chapters': chapters}, open(NEW_FILE, 'w'), ensure_ascii=False, indent=2)
print(f'wrote {NEW_FILE}: {len(chapters)} chapters, {total} words')
for c in chapters:
    m = c['metadata']
    print(f"  ch{m['chapter']} (K{m['chapter']-30:2d}) {len(c['sections'][0]['words']):3d}w  {m['topic_en']}")
