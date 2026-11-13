"""Refresh the KANJIDIC2 subset so every kanji in the app's Japanese text has
English meanings: vocabulary, the kanji book, reading passages and questions,
grammar, exercises, lookup tables and UI strings. Run at least monthly and
whenever app text changes.

Data copyright James William Breen and EDRDG, CC BY-SA 4.0.
"""
import gzip, json, glob, os, re, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

KANJI = re.compile(r'[一-鿿]')
KANA = re.compile(r'[ぁ-んァ-ヶー]')

def strings_in(obj, key=''):
    if isinstance(obj, str):
        yield key, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from strings_in(v, k)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v, key)

def is_jis_x_0208(char):
    try:
        char.encode('iso2022_jp')
        return True
    except UnicodeEncodeError:
        return False

chars = set()
# All app data, excluding Chinese translation fields (*_zh, meaning_zh):
# they are glosses, never tappable Japanese text.
for f in glob.glob('data/**/*.json', recursive=True):
    for k, s in strings_in(json.load(open(f, encoding='utf-8'))):
        if k.endswith('_zh') or k == 'meaning_zh':
            continue
        chars.update(KANJI.findall(s))

# Word-lookup table. Real entries carry a kana reading; entries whose
# "reading" repeats the surface are Chinese gloss leftovers, not words.
lookup_src = Path('data/reading-lookup.js').read_text(encoding='utf-8')
for surface, reading in re.findall(r'\["((?:[^"\\]|\\.)*)","((?:[^"\\]|\\.)*)"', lookup_src):
    if KANA.search(reading):
        chars.update(KANJI.findall(surface))

# UI strings in scripts and pages.
for f in glob.glob('js/*.js') + glob.glob('*.html'):
    chars.update(KANJI.findall(Path(f).read_text(encoding='utf-8')))

cache = os.environ.get('KANJIDIC2_XML')
raw = Path(cache).read_bytes() if cache else urllib.request.urlopen('https://www.edrdg.org/kanjidic/kanjidic2.xml.gz', timeout=60).read()
root = ET.fromstring(gzip.decompress(raw))
kanjidic = {}
for c in root.findall('character'):
    lit = c.findtext('literal')
    kanjidic[lit] = [m.text for m in c.findall('.//meaning') if 'm_lang' not in m.attrib and m.text]

entries = {lit: kanjidic[lit] for lit in sorted(chars) if lit in kanjidic and kanjidic[lit]}
uncovered = sorted(chars - set(entries))
# Every Japanese (JIS X 0208) character must have meanings. The only allowed
# gaps are simplified-Chinese characters from embedded Chinese glosses, which
# a Japanese kanji dictionary does not cover.
japanese_gaps = [c for c in uncovered if is_jis_x_0208(c)]
assert not japanese_gaps, f'Japanese characters without dictionary meanings: {japanese_gaps}'
assert entries and all(entries.values())

metadata = {
    'source': 'KANJIDIC2',
    'copyright': 'James William Breen and Electronic Dictionary Research and Development Group',
    'license': 'CC BY-SA 4.0',
    'license_url': 'https://www.edrdg.org/edrdg/licence.html',
    'source_url': 'https://www.edrdg.org/kanjidic/kanjd2index_legacy.html',
    'database_date': root.findtext('header/date_of_creation'),
    'adaptation': 'English meanings for every kanji appearing in the app\'s Japanese text (vocabulary, kanji book, reading, grammar, exercises, lookup tables, UI); meanings unmodified.',
}
out = '// KANJIDIC2 English subset, CC BY-SA 4.0. See KANJIDIC2-SOURCES.md.\n'
out += 'export const metadata = ' + json.dumps(metadata, ensure_ascii=False) + ';\n'
out += 'export const entries = ' + json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + ';\n'
# App-text characters intentionally without entries: simplified-Chinese-only
# characters from embedded Chinese glosses, outside KANJIDIC2's scope.
out += 'export const uncovered = ' + json.dumps(uncovered, ensure_ascii=False) + ';\n'
Path('data/kanji/vocab_character_meanings.js').write_text(out, encoding='utf-8')
print(f'{len(entries)} characters with meanings; source date {metadata["database_date"]}')
print(f'{len(uncovered)} Chinese-gloss characters intentionally uncovered: {"".join(uncovered)}')
