#!/usr/bin/env python3
"""Build read-only lookup boundaries from checked-in Japanese content.
Requires: pip install fugashi unidic-lite; a local JMdict_e.gz (EDRDG).
Usage: python scripts/build-reading-lookup.py /path/to/JMdict_e.gz
No progress, questions, answers or textbook source fields are modified.
"""
import gzip, hashlib, html, json, re, sys
from pathlib import Path
import xml.etree.ElementTree as ET
import fugashi
ROOT = Path(__file__).resolve().parents[1]
tag = fugashi.Tagger()
JA = re.compile('[一-龯々ぁ-んァ-ヶ]')
def plain(s):
    s = re.sub(r'<(rt|rp|sup)\b[^>]*>.*?</\1>', '', s, flags=re.S)
    return html.unescape(re.sub('<[^>]*>', '', s))
def chunks(s):
    return [x for x in re.findall(r'[^。！？!?\n]+[。！？!?]?|[。！？!?]', s) if JA.search(x)]
def hira(s):
    return ''.join(chr(ord(c)-96) if 'ァ' <= c <= 'ヶ' else c for c in s)
def hash32(s):
    h = 2166136261
    for c in s:
        # Browser hash uses UTF-16 code units.
        for i in range(0, len(c.encode('utf-16-le')), 2):
            h = ((h ^ int.from_bytes(c.encode('utf-16-le')[i:i+2], 'little')) * 16777619) & 0xffffffff
    return str(h)
strings = set()
def visit(v):
    if isinstance(v, str) and JA.search(v):
        strings.update(chunks(plain(v)))
    elif isinstance(v, list):
        for x in v: visit(x)
    elif isinstance(v, dict):
        for x in v.values(): visit(x)
for p in sorted((ROOT/'data'/'reading').rglob('*.json')):
    if p.name.startswith(('dict-', 'reading-lookup')): continue
    visit(json.loads(p.read_text()))
# Preserve a compound only when the full dictionary confirms it.
xml = ET.fromstring(gzip.open(sys.argv[1]).read())
dictionary = {}
scores = {}
by_reading = {}
for e in xml.findall('entry'):
    readings = [x.text for x in e.findall('r_ele/reb')]
    senses = e.findall('sense')
    meaning = '; '.join(x.text for sense in senses[:2] for x in sense.findall('gloss') if x.text)[:260]
    kanji = [x.text for x in e.findall('k_ele/keb')]
    common = bool(e.findall('k_ele/ke_pri') or e.findall('r_ele/re_pri'))
    for key in kanji + readings:
        score = (100 if key in kanji else 0) + (50 if not kanji else 0) + (10 if common else 0) + (20 if key in [r.findtext('reb') for r in e.findall('r_ele') if r.find('re_pri') is not None] else 0) + (20 if any('usually written using kana' in (x.text or '') for x in e.findall('sense/misc')) else 0)
        # Kana lookups must prefer the matching reading, never the first
        # unrelated reading of a homographic/archaic entry.
        reading = key if key in readings else (readings[0] if readings else '')
        for r in readings:
            if (key, hira(r)) not in by_reading or score > by_reading[(key,hira(r))][0]: by_reading[(key,hira(r))] = (score, [r, meaning])
        if key not in scores or score > scores[key]:
            dictionary[key] = [reading, meaning]; scores[key] = score
entries, ids, records, collision = [], {}, {}, {}
for s in sorted(strings):
    words = list(tag(s)); out = []; i = 0; offset = 0
    while i < len(words):
        w = words[i]; start = s.find(w.surface, offset)
        if start < 0: raise ValueError(s)
        surface = w.surface; f = w.feature; raw_lemma = (f.lemma or surface).split('-')[0]; lemma = raw_lemma
        lemma = {'為る':'する','居る':'いる','有る':'ある','此の':'この','其の':'その','何れ':'どれ'}.get(lemma, lemma)
        reading = hira(f.kana or ''); labels = []; j = i + 1
        # Join verb/adjective auxiliaries so the popup teaches the actual form,
        # not an isolated stem. Keep content nouns/particles as separate words.
        if f.pos1 in ('動詞', '形容詞'):
            while j < len(words):
                n = words[j]; nf = n.feature
                if nf.pos1 == '助動詞':
                    aux = nf.lemma
                    label = {'たい':'want to', 'ない':'negative', 'ぬ':'negative', 'た':'past / completed', 'ます':'polite', 'られる':'potential / passive', 'れる':'passive / potential', 'せる':'causative', 'させる':'causative'}.get(aux)
                    if label and label not in labels: labels.append(label)
                elif n.surface in ('て','で') and nf.pos2 == '接続助詞':
                    if 'te-form' not in labels: labels.append('te-form')
                else: break
                surface += n.surface; reading += hira(nf.kana or ''); j += 1
        # Dictionary-confirmed adjacent noun/suffix compounds, e.g. 注意書き.
        elif f.pos1 in ('名詞','接頭辞'):
            for end in range(min(i+4,len(words)),i+1,-1):
                candidate = ''.join(x.surface for x in words[i:end])
                if candidate in dictionary and all(x.feature.pos1 in ('名詞','接尾辞') for x in words[i+1:end]):
                    surface = candidate; reading = ''.join(hira(x.feature.kana or '') for x in words[i:end]); lemma = candidate; raw_lemma = candidate; j = end; break
        offset = start + len(surface)
        # Never fabricate whole-word definitions. Unknowns stay explicit.
        expected = hira(f.lForm or '') if j == i+1 or f.pos1 in ('動詞','形容詞') else reading
        match = by_reading.get((raw_lemma, expected)) or by_reading.get((lemma, expected)) or by_reading.get((surface, reading)) or by_reading.get((raw_lemma, hira(f.kana or '')))
        pair = match[1] if match else None
        if j > i+1 and f.pos1 in ('名詞','接頭辞'):
            pair = dictionary.get(surface)
            if pair: reading = hira(pair[0])
        if f.pos1 not in ('補助記号','記号','空白','助詞','助動詞') and JA.search(surface):
            data = [surface, lemma, reading, ' · '.join(labels), *(pair or ['', ''])]
            key = json.dumps(data, ensure_ascii=False)
            if key not in ids: ids[key] = len(entries); entries.append(data)
            out.append([len(s[:start].encode('utf-16-le'))//2, len(s[:offset].encode('utf-16-le'))//2, ids[key]])
        i = j
    h = hash32(s)
    if h in collision and collision[h] != s: raise ValueError('Hash collision')
    collision[h] = s; records[h] = [len(s.encode('utf-16-le'))//2, out]
result = {'entries':entries, 'chunks':records}
path = ROOT/'data/reading-lookup.js'
digest = hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest()
path.write_text('// Generated by scripts/build-reading-lookup.py. JMdict: CC BY-SA 4.0; UniDic: BSD.\n// JMdict_e.gz SHA256: '+digest+'\nexport default '+json.dumps(result,ensure_ascii=False,separators=(',',':'))+';\n')
print(f'{len(strings)} chunks, {len(entries)} forms, {path.stat().st_size} bytes')
