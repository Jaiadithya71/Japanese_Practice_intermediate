# Vocabulary character meanings

This app uses the KANJIDIC2 dictionary file. It is the property of James William Breen and the Electronic Dictionary Research and Development Group (EDRDG), and is used in conformance with the Group's licence.

- Project/documentation: https://www.edrdg.org/kanjidic/kanjd2index_legacy.html
- Source download: https://www.edrdg.org/kanjidic/kanjidic2.xml.gz
- Licence: https://www.edrdg.org/edrdg/licence.html
- CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/

`vocab_character_meanings.js` is a subset of English character meanings covering every kanji used in the vocabulary list and the kanji book (target kanji and their compounds). Meaning strings are unchanged. This derived data is distributed under CC BY-SA 4.0. Dictionary data is provided without warranty.

Character meanings are memory cues, not a promise that a word's meaning is the sum of its characters. The UI shows up to two dictionary glosses per character. Its title text contains all glosses.

## Refresh procedure

Refresh at least monthly and whenever the vocabulary list or kanji book changes, from the repository root:

```
python3 scripts/refresh-vocab-kanji-meanings.py
node scripts/verify-vocab-kanji-meanings.mjs
```

Inspect the dataset date and diff, then commit/push the refreshed subset. The script refuses to replace the subset if any covered character lacks English meanings. No user study data is involved.

## Shape matching subset

`character_shapes.js` is a Joyo (2,136 character) subset of the official KANJIDIC2 download dated 2026-10-22. It retains classical radical numbers, primary stroke counts, and Japanese readings. These fields support visually related quiz distractors and exclusion of alternate correct readings. This derived data is also CC BY-SA 4.0. Radical matches are a shape heuristic, not a pixel-level glyph comparison; explicit look-alike/component families take precedence. For rare radicals without enough peers, nearest stroke-count candidates form the last ranked tier. Candidate selection is deterministic.
