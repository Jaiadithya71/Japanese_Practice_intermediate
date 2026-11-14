"""Build data/kanji/kanji_components.js: component breakdowns for every kanji
that can appear in the app's kanji-meaning chips.

Primary source is KanjiVG (CC BY-SA 3.0): its stroke groups carry a component
hierarchy, so each kanji is shown as its top-level split into 1-4 recognizable
parts (e.g. 製 = 制 + 衣, 合 = 人 + 一 + 口). Part meanings are KANJIDIC2
English glosses (CC BY-SA 4.0); a variant element (e.g. ⻌) takes the meaning
of its original form (辶). Kanji outside KanjiVG fall back to the flat
KRADFILE element list (EDRDG licence), the previous behaviour. Ungrouped bare
strokes are dropped and the kanji is flagged `hidden:true` so the UI can note
that stroke-only marks are not shown. A kanji with no named sub-structure is a
building block and gets an empty parts list.

Run from the repository root:
    python3 scripts/build-kanji-components.py
Cache sources to skip downloads:
    KANJIVG_XML=/path/kanjivg.xml KRADFILE=/path/kradfile.eucjp KANJIDIC2_XML=/path/kanjidic2.xml.gz
"""
import gzip, json, os, re, unicodedata, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

KVG = '{http://kanjivg.tagaini.net}'
KANJIVG_URL = 'https://github.com/KanjiVG/kanjivg/releases/download/r20260714/kanjivg-20260714.xml.gz'
KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'
KANJIDIC2_URL = 'https://www.edrdg.org/kanjidic/kanjidic2.xml.gz'

# Kanji shown in the chips = keys of the KANJIDIC2 subset.
src = Path('data/kanji/vocab_character_meanings.js').read_text(encoding='utf-8')
m = re.search(r'export const entries = (\{.*?\});\nexport const', src, re.S)
universe = sorted(json.loads(m.group(1)))

# KANJIDIC2 meanings for part labels.
cache = os.environ.get('KANJIDIC2_XML')
raw = Path(cache).read_bytes() if cache else urllib.request.urlopen(KANJIDIC2_URL, timeout=60).read()
root = ET.fromstring(gzip.decompress(raw))
kanjidic = {}
for c in root.findall('character'):
    lit = c.findtext('literal')
    glosses = [g.text for g in c.findall('.//meaning') if 'm_lang' not in g.attrib and g.text]
    if glosses:
        kanjidic[lit] = glosses

RADICAL_NOTE = re.compile(r'\s*radical( variant)? \(no\.\s*\d+\)\s*$')

def clean_gloss(text):
    return RADICAL_NOTE.sub('', text).strip()

def glosses_of(char, original=None):
    """Up to two short grounded meanings for a component character. A variant
    element with no KANJIDIC2 entry, or with only a bare radical label
    (亻 -> 'radical number 9'), takes its original form's gloss (⻌ -> 辶,
    亻 -> 人) before falling back to the Unicode radical name."""
    own = kanjidic.get(char) if len(char) == 1 else None
    if original and own and own[0] and 'radical' in own[0]:
        char, own = original, kanjidic.get(original)
    candidates = (char,) if own else (char, original)
    for cand in candidates:
        if cand and len(cand) == 1 and cand in kanjidic:
            out = []
            for g in kanjidic[cand]:
                g = clean_gloss(g)
                if g and g not in out:
                    out.append(g)
            return out[:2]
    try:
        name = unicodedata.name(char)
    except (ValueError, TypeError):
        return []
    for prefix in ('CJK RADICAL ', 'KANGXI RADICAL '):
        if name.startswith(prefix):
            return [name[len(prefix):].lower()]
    return []

# KanjiVG component hierarchy.
cache = os.environ.get('KANJIVG_XML')
raw = Path(cache).read_bytes() if cache else urllib.request.urlopen(KANJIVG_URL, timeout=120).read()
if raw[:2] == b'\x1f\x8b':
    raw = gzip.decompress(raw)
kvg = {}
for kanji_el in ET.fromstring(raw):
    g = kanji_el.find(KVG + 'g') or kanji_el.find('g')
    if g is not None and g.get(KVG + 'element'):
        kvg[g.get(KVG + 'element')] = g

def child_groups(g):
    return [c for c in g if c.tag in (KVG + 'g', 'g')]

def top_level_parts(g):
    """The kanji's immediate components: named sub-groups, part-split elements
    merged, unnamed structural groups (e.g. the top of 合) opened one level."""
    out = []
    for c in child_groups(g):
        el = c.get(KVG + 'element')
        if el and len(el) != 1:
            el = None  # composite/CDP label: open the group like an unnamed one
        if el and c.get(KVG + 'part') == '2':
            continue  # second half of a split element, merged with part 1
        if el:
            out.append(c)
        else:
            out.extend(top_level_parts(c))
    return out

def kvg_parts(kanji):
    """(parts, hidden) from KanjiVG, or None when the kanji is absent.
    parts is a list of [char, meaning]; empty list = building block."""
    g = kvg.get(kanji)
    if g is None:
        return None
    groups = top_level_parts(g)
    # Ungrouped strokes sitting beside the named parts (之, 久, 夫 ...).
    hidden = any(c.tag in (KVG + 'path', 'path') for c in g)
    elements = [gr.get(KVG + 'element') for gr in groups]
    if not elements or (len(elements) == 1 and elements[0] == kanji):
        return [], False  # building block: nothing shown, nothing dropped
    parts, counts = [], {}
    for gr in groups:
        el = gr.get(KVG + 'element')
        counts[el] = counts.get(el, 0) + 1
        if counts[el] > 1:
            continue
        meaning = glosses_of(el, gr.get(KVG + 'original'))
        label = ' / '.join(meaning) if meaning else None
        if counts[el] and counts.get(el) and list(counts).count(el):
            pass
        parts.append([el, label])
    # Mark repeated elements with their count (器 = 口 x4 + 大).
    for part in parts:
        n = counts[part[0]]
        if n > 1:
            part[1] = (part[1] + ' ' if part[1] else '') + f'x{n}'
        if part[1] is None:
            hidden = True
    return parts, hidden

# KRADFILE fallback for kanji KanjiVG does not cover.
cache = os.environ.get('KRADFILE')
if cache:
    krad_text = Path(cache).read_text(encoding='euc_jp')
else:
    krad_text = gzip.decompress(
        urllib.request.urlopen(KRADFILE_URL, timeout=60).read()).decode('euc_jp')
krad = {}
for line in krad_text.splitlines():
    if not line or line.startswith('#') or ' : ' not in line:
        continue
    kanji, elements = line.split(' : ', 1)
    krad[kanji.strip()] = elements.split()

def is_meaningless_glyph(char):
    try:
        name = unicodedata.name(char)
    except ValueError:
        return True
    return ('KATAKANA LETTER' in name or 'HIRAGANA LETTER' in name
            or name == 'FULLWIDTH VERTICAL LINE' or char in '丶丿')

def krad_parts(kanji):
    elements = krad.get(kanji)
    if elements is None:
        return None
    parts, hidden = [], False
    for el in dict.fromkeys(elements):
        if el == kanji:
            continue
        if is_meaningless_glyph(el):
            hidden = True
            continue
        g = glosses_of(el)
        parts.append([el, g[0] if g else None])
        if not g:
            hidden = True
    return parts, hidden

components, from_krad = {}, []
for kanji in universe:
    built = kvg_parts(kanji)
    if built is None:
        built = krad_parts(kanji)
        if built is not None:
            from_krad.append(kanji)
    if built is None:
        continue  # no data anywhere; UI shows "no data"
    parts, hidden = built
    components[kanji] = {'parts': parts, 'hidden': hidden}

missing = sorted(set(universe) - set(components))
metadata = {
    'source': 'KanjiVG r20260714 (component hierarchy) + KANJIDIC2 (part meanings); KRADFILE fallback for kanji outside KanjiVG',
    'copyright': 'KanjiVG: Ulrich Apel; KANJIDIC2: James William Breen and EDRDG; KRADFILE: Michael Raine, James Breen and EDRDG',
    'license': 'KanjiVG subset: CC BY-SA 3.0; KANJIDIC2 subset: CC BY-SA 4.0; KRADFILE: EDRDG licence',
    'license_url': 'https://creativecommons.org/licenses/by-sa/3.0/',
    'source_url': 'https://github.com/KanjiVG/kanjivg',
    'adaptation': ('For each kanji in the app text, the KanjiVG top-level component '
                   'split with unnamed structural groups opened one level and '
                   'split-position elements merged; bare ungrouped strokes dropped '
                   '("hidden" marks kanji where stroke-only marks were dropped); '
                   'repeated elements carry an xN count; up to two KANJIDIC2 English '
                   'glosses per part, a variant element taking its original form\'s '
                   'gloss. Kanji outside KanjiVG keep the flat KRADFILE element list.'),
}
out = '// KanjiVG/KANJIDIC2 component subset, see data/kanji/KANJIDIC2-SOURCES.md.\n'
out += 'export const metadata = ' + json.dumps(metadata, ensure_ascii=False) + ';\n'
out += 'export const components = ' + json.dumps(components, ensure_ascii=False, separators=(',', ':')) + ';\n'
out += 'export const uncovered = ' + json.dumps(missing, ensure_ascii=False) + ';\n'
Path('data/kanji/kanji_components.js').write_text(out, encoding='utf-8')
print(f'kanji: {len(universe)}, with data: {len(components)} (KRADFILE fallback: {len(from_krad)}), no data: {len(missing)}')
print('krad fallback sample:', from_krad[:15])
print('no-data sample:', missing[:15])
for k in ['製', '知', '夫', '婦', '造', '合']:
    print(k, components.get(k))
