"""Refresh the vocabulary-only KANJIDIC2 subset. Run at least monthly.
Data copyright James William Breen and EDRDG, CC BY-SA 4.0.
"""
import gzip,json,glob,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
words=[w for f in glob.glob('data/vocabulary/*.json') for c in json.load(open(f)).get('chapters',[]) for s in c.get('sections',[]) for w in s.get('words',[])]
chars={c for w in words for c in w.get('term_ja','') if '\u4e00'<=c<='\u9fff'}
url='https://www.edrdg.org/kanjidic/kanjidic2.xml.gz'
root=ET.fromstring(gzip.decompress(urllib.request.urlopen(url,timeout=30).read()))
entries={c.findtext('literal'):[m.text for m in c.findall('.//meaning') if 'm_lang' not in m.attrib] for c in root.findall('character') if c.findtext('literal') in chars}
missing=chars-set(entries)
assert not missing and all(entries.values()), f'Missing dictionary meanings: {missing}'
metadata={'source':'KANJIDIC2','copyright':'James William Breen and Electronic Dictionary Research and Development Group','license':'CC BY-SA 4.0','license_url':'https://www.edrdg.org/edrdg/licence.html','source_url':'https://www.edrdg.org/kanjidic/kanjd2index_legacy.html','database_date':root.findtext('header/date_of_creation'),'adaptation':'Vocabulary-character English subset; meanings unmodified.'}
Path('data/kanji/vocab_character_meanings.js').write_text('// KANJIDIC2 English subset, CC BY-SA 4.0. See KANJIDIC2-SOURCES.md.\nexport const metadata = '+json.dumps(metadata,ensure_ascii=False)+';\nexport const entries = '+json.dumps(entries,ensure_ascii=False,separators=(',',':'))+';\n')
print(f'{len(entries)} characters; source date {metadata["database_date"]}')
