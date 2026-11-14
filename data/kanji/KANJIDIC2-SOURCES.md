# Vocabulary character meanings

This app uses the KANJIDIC2 dictionary file. It is the property of James William Breen and the Electronic Dictionary Research and Development Group (EDRDG), and is used in conformance with the Group's licence.

- Project/documentation: https://www.edrdg.org/kanjidic/kanjd2index_legacy.html
- Source download: https://www.edrdg.org/kanjidic/kanjidic2.xml.gz
- Licence: https://www.edrdg.org/edrdg/licence.html
- CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/

`vocab_character_meanings.js` is a subset of English character meanings covering every kanji appearing in the app's Japanese text: the vocabulary list, the kanji book (target kanji and their compounds), reading passages and questions, grammar, exercises, word-lookup tables and UI strings. Meaning strings are unchanged. The file also exports `uncovered`: app-text characters intentionally without entries because they are simplified-Chinese characters from embedded Chinese glosses, outside KANJIDIC2's scope. This derived data is distributed under CC BY-SA 4.0. Dictionary data is provided without warranty.

Character meanings are memory cues, not a promise that a word's meaning is the sum of its characters. The UI shows up to two dictionary glosses per character. Its title text contains all glosses.

## Refresh procedure

Refresh at least monthly and whenever any app text changes, from the repository root:

```
python3 scripts/refresh-vocab-kanji-meanings.py
node scripts/verify-vocab-kanji-meanings.mjs
```

Inspect the dataset date and diff, then commit/push the refreshed subset. The script refuses to replace the subset if any covered character lacks English meanings. No user study data is involved.

## Shape matching subset

`character_shapes.js` is a Joyo (2,136 character) subset of the official KANJIDIC2 download dated 2026-10-22. It retains classical radical numbers, primary stroke counts, and Japanese readings. These fields support visually related quiz distractors and exclusion of alternate correct readings. This derived data is also CC BY-SA 4.0. Radical matches are a shape heuristic, not a pixel-level glyph comparison; explicit look-alike/component families take precedence. For rare radicals without enough peers, nearest stroke-count candidates form the last ranked tier. Candidate selection is deterministic.

## Component breakdown subset

`kanji_components.js` lists the visual component parts of every kanji in the
app's kanji-meaning chips, shown when a chip is tapped. Component elements come
from KRADFILE (Copyright Michael Raine, James Breen and EDRDG, used under the
Group's licence at https://www.edrdg.org/edrdg/licence.html; source download
http://ftp.edrdg.org/pub/Nihongo/kradfile.gz). Self-references, bare strokes and
kana-shaped glyphs are dropped (kanji with dropped elements are flagged
`hidden`); each remaining element carries its first KANJIDIC2 English gloss.
Elements are visual parts, not a promise of historical etymology. Rebuild from
the repository root:

```
python3 scripts/build-kanji-components.py
node scripts/verify-kanji-components.mjs
```
