"""Build data/kanji/kanji_components.js: visual component breakdowns for every
kanji that can appear in the app's kanji-meaning chips.

Component elements come from KRADFILE (JIS X 0208 kanji decomposition,
EDRDG licence). Element meanings come from KANJIDIC2 (CC BY-SA 4.0).
Elements that are bare strokes or kana-shaped glyphs (no dictionary meaning)
are dropped and the kanji is flagged `hidden:true` so the UI can note that
stroke-only elements are not shown. A kanji whose only element is itself is a
building block and gets an empty parts list.

Run from the repository root:
    python3 scripts/build-kanji-components.py
Cache sources to skip downloads:
    KRADFILE=/path/kradfile.eucjp KANJIDIC2_XML=/path/kanjidic2.xml.gz
"""
import gzip, json, os, re, unicodedata, urllib.request
from pathlib import Path

KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'
KANJIDIC2_URL = 'https://www.edrdg.org/kanjidic/kanjidic2.xml.gz'

# Kanji shown in the chips = keys of the KANJIDIC2 subset.
src = Path('data/kanji/vocab_character_meanings.js').read_text(encoding='utf-8')
m = re.search(r'export const entries = (\{.*?\});\nexport const', src, re.S)
universe = sorted(json.loads(m.group(1)))

# KRADFILE (EUC-JP).
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

# KANJIDIC2 meanings for element labels.
import xml.etree.ElementTree as ET
cache = os.environ.get('KANJIDIC2_XML')
raw = Path(cache).read_bytes() if cache else urllib.request.urlopen(KANJIDIC2_URL, timeout=60).read()
root = ET.fromstring(gzip.decompress(raw))
kanjidic = {}
for c in root.findall('character'):
    lit = c.findtext('literal')
    glosses = [g.text for g in c.findall('.//meaning') if 'm_lang' not in g.attrib and g.text]
    if glosses:
        kanjidic[lit] = glosses


def element_meaning(char):
    """Short grounded meaning for a component element, or None."""
    glosses = kanjidic.get(char)
    if glosses:
        return glosses[0]
    try:
        name = unicodedata.name(char)
    except ValueError:
        return None
    for prefix in ('CJK RADICAL ', 'KANGXI RADICAL '):
        if name.startswith(prefix):
            return name[len(prefix):].lower()
    return None


def is_meaningless_glyph(char):
    """Bare strokes and kana-shaped glyphs used as visual elements only."""
    try:
        name = unicodedata.name(char)
    except ValueError:
        return True
    return ('KATAKANA LETTER' in name or 'HIRAGANA LETTER' in name
            or name == 'FULLWIDTH VERTICAL LINE' or char in '丶丿')


components = {}
for kanji in universe:
    elements = krad.get(kanji)
    if elements is None:
        continue  # not in KRADFILE (non-JIS X 0208); UI shows "no data"
    parts, hidden = [], False
    for el in dict.fromkeys(elements):
        if el == kanji:
            continue  # self-reference: a building block, not a part
        if is_meaningless_glyph(el):
            hidden = True
            continue
        parts.append([el, element_meaning(el)])
    components[kanji] = {'parts': parts, 'hidden': hidden}

missing = sorted(set(universe) - set(components))
metadata = {
    'source': 'KRADFILE (component elements) + KANJIDIC2 (element meanings)',
    'copyright': 'KRADFILE: Michael Raine, James Breen and EDRDG; KANJIDIC2: James William Breen and EDRDG',
    'license': 'KRADFILE: EDRDG licence; KANJIDIC2 subset: CC BY-SA 4.0',
    'license_url': 'https://www.edrdg.org/edrdg/licence.html',
    'source_url': 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz',
    'adaptation': ('For each kanji in the app text, the KRADFILE element list with '
                   'self-references, bare strokes and kana-shaped glyphs removed; '
                   'first KANJIDIC2 English gloss per remaining element. '
                   '"hidden" marks kanji where stroke/kana elements were dropped.'),
}
out = '// KRADFILE/KANJIDIC2 component subset, see data/kanji/KANJIDIC2-SOURCES.md.\n'
out += 'export const metadata = ' + json.dumps(metadata, ensure_ascii=False) + ';\n'
out += 'export const components = ' + json.dumps(components, ensure_ascii=False, separators=(',', ':')) + ';\n'
out += 'export const uncovered = ' + json.dumps(missing, ensure_ascii=False) + ';\n'
Path('data/kanji/kanji_components.js').write_text(out, encoding='utf-8')
print(f'kanji: {len(universe)}, with data: {len(components)}, no data: {len(missing)}')
print('no-data sample:', missing[:15])
