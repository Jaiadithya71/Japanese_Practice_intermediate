"""Refresh Joyo radical/stroke/reading subset from KANJIDIC2 (EDRDG, CC BY-SA 4.0)."""
import gzip,json,urllib.request,xml.etree.ElementTree as E
from pathlib import Path
url='https://www.edrdg.org/kanjidic/kanjidic2.xml.gz'
r=E.fromstring(gzip.decompress(urllib.request.urlopen(url,timeout=30).read()))
out={}
for c in r.findall('character'):
    if c.find('misc/grade') is None or int(c.findtext('misc/grade'))>8: continue
    out[c.findtext('literal')]={'radical':int(c.findtext('radical/rad_value[@rad_type="classical"]') or 0),'strokes':int(c.findtext('misc/stroke_count') or 0),'readings':[x.text for x in c.findall('reading_meaning/rmgroup/reading') if x.attrib.get('r_type') in ['ja_on','ja_kun']]}
assert len(out)>=2136
Path('data/kanji/character_shapes.js').write_text('// KANJIDIC2 Joyo radical/stroke/reading subset, CC BY-SA 4.0. See KANJIDIC2-SOURCES.md.\nexport const characterShapes = '+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n')
print(len(out),r.findtext('header/date_of_creation'))
