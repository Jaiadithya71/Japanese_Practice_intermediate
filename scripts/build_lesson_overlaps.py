#!/usr/bin/env python3
"""Build data/vocab_lesson_overlaps.json: for the Home lessons that were
deduplicated against earlier lessons (Reading R22-30, Kanji K31-55), the
words that belong to the lesson's own source list but were left out because
they already appeared in an earlier chapter.

The Home "All lesson words (incl. overlaps)" option adds these back to the
drill pool so chapter-wise class-test prep sees every word of the chosen
lesson.

Overlap words reuse the existing vocabDB word object (same id) whenever the
word already exists somewhere in vocabDB, so SRS progress stays per-word.
"""
import json, glob

VOCAB_FILES = [
    'data/vocabulary/part1_topics_ch01_05.json',
    'data/vocabulary/part1_topics_ch06_10.json',
    'data/vocabulary/part1_topics_ch11_15.json',
    'data/vocabulary/part1_topics_ch16_21.json',
    'data/vocabulary/part1_topics_ch22_30_reading.json',
    'data/vocabulary/part1_topics_ch31_55_kanji.json',
    'data/vocabulary/part2_characteristics_ch01_04.json',
    'data/vocabulary/part2_characteristics_ch05_08.json',
]

chap = {}          # chapter id -> word list
by_term = {}       # (term_ja, reading) -> canonical word object (first occurrence)
for f in VOCAB_FILES:
    d = json.load(open(f))
    for ch in d['chapters']:
        cid = str(ch['metadata']['chapter'])
        ws = [w for s in ch['sections'] for w in s.get('words', [])]
        chap[cid] = ws
        for i, w in enumerate(ws):
            if not w.get('id'):
                w['id'] = 'v' + cid.zfill(2) + '-' + str(i + 1).zfill(3)
            by_term.setdefault((w['term_ja'], w['reading']), w)

overlaps = {}

# --- K lessons: kanji book lesson ln -> chapter 30 + ln ---
for f in sorted(glob.glob('data/kanji/part*_lessons_*.json')):
    d = json.load(open(f))
    for l in d['lessons']:
        ln = l['lesson_number']
        cid = str(30 + ln)
        home_keys = {(w['term_ja'], w['reading']) for w in chap.get(cid, [])}
        seen = set()
        extra = []
        for kj in l['kanji']:
            for w in kj['words']:
                key = (w['term_ja'], w['reading'])
                if key in home_keys or key in seen:
                    continue
                seen.add(key)
                existing = by_term.get(key)
                if existing:
                    extra.append(existing)
                else:
                    nw = {k: w[k] for k in ('term_ja', 'reading', 'ruby_html', 'meaning_en', 'meaning_zh') if k in w}
                    nw['id'] = 'v%s-x%02d' % (cid.zfill(2), len(extra) + 1)
                    extra.append(nw)
        if extra:
            overlaps[cid] = extra

# --- R lessons: reading key vocab excluded from the 22-30 chunks ---
READING_FILES = [
    'data/reading/part1_foundation.json',
    'data/reading/part2_short_1.json',
    'data/reading/part2_short_2.json',
    'data/reading/part2_short_3.json',
    'data/reading/part4_short_medium.json',
    'data/reading/part4_long_info.json',
]
seq = []
seen = set()
r_src = {}
for f in READING_FILES:
    d = json.load(open(f))
    for l in d['lessons']:
        for v in l.get('vocabulary') or []:
            key = (v.get('term'), v.get('reading'))
            if key[0] and key not in seen:
                seen.add(key)
                seq.append(key)
                r_src[key] = v

# flat R word sequence and chunk boundaries
r_flat = []
r_chunks = []  # (cid, start, end)
for n in range(22, 31):
    cid = str(n)
    start = len(r_flat)
    r_flat.extend((w['term_ja'], w['reading']) for w in chap.get(cid, []))
    r_chunks.append((cid, start, len(r_flat)))

# verify R flat order is a subsequence of the reading order
it = iter(range(len(seq)))
pos = 0
ok = True
for key in r_flat:
    while pos < len(seq) and seq[pos] != key:
        pos += 1
    if pos == len(seq):
        ok = False
        print('R word not found in reading order:', key)
        break
    pos += 1
assert ok, 'R flat list is not a subsequence of the reading vocab order'

# walk the full reading sequence; assign each excluded word the chunk of the
# next surviving word (previous chunk when it trails at the end)
r_pos = 0
for key in seq:
    while r_pos < len(r_flat) and r_flat[r_pos] == key:
        r_pos += 1
    if r_pos < len(r_flat) and r_flat[r_pos] != key and key not in set(r_flat):
        # excluded word: chunk containing flat index r_pos (next survivor)
        target = None
        for cid, start, end in r_chunks:
            if start <= r_pos < end:
                target = cid
                break
        if target is None:
            target = r_chunks[-1][0]
        existing = by_term.get(key)
        if not existing:
            # A few reading key words (e.g. 羽) are in no vocab chapter at all;
            # build a word object from the reading source entry.
            v = r_src[key]
            existing = {'term_ja': v['term'], 'reading': v['reading'],
                        'meaning_en': (v.get('meaning') or '').split(' / ')[0],
                        'id': 'v%s-x%02d' % (target, 90 + len(overlaps.get(target, [])))}
        overlaps.setdefault(target, []).append(existing)

out = {'metadata': {'description': 'Words excluded from Home lessons 22-30 (reading) and 31-55 (kanji) because they already appeared in earlier lessons; re-added to the drill pool by the "All lesson words (incl. overlaps)" option.', 'generated_by': 'scripts/build_lesson_overlaps.py'}, 'overlaps': overlaps}
json.dump(out, open('data/vocab_lesson_overlaps.json', 'w'), ensure_ascii=False, indent=1)
total = sum(len(v) for v in overlaps.values())
print('chapters with overlaps:', len(overlaps), 'extra words:', total)
for cid in sorted(overlaps, key=int):
    print(' ', cid, len(overlaps[cid]))
