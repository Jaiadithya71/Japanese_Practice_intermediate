# Vocabulary character meanings

This app uses the KANJIDIC2 dictionary file. It is the property of James William Breen and the Electronic Dictionary Research and Development Group (EDRDG), and is used in conformance with the Group's licence.

- Project/documentation: https://www.edrdg.org/kanjidic/kanjd2index_legacy.html
- Source download: https://www.edrdg.org/kanjidic/kanjidic2.xml.gz
- Licence: https://www.edrdg.org/edrdg/licence.html
- CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/

`vocab_character_meanings.js` is a vocabulary-only subset of English character meanings. Meaning strings are unchanged. This derived data is distributed under CC BY-SA 4.0. Dictionary data is provided without warranty.

Character meanings are memory cues, not a promise that a word's meaning is the sum of its characters. The UI shows up to two dictionary glosses per character. Its title text contains all glosses.

## Refresh procedure

Refresh at least monthly and whenever the vocabulary list changes, from the repository root:

```
python3 scripts/refresh-vocab-kanji-meanings.py
node scripts/verify-vocab-kanji-meanings.mjs
```

Inspect the dataset date and diff, then commit/push the refreshed subset. The script refuses to replace the subset if vocabulary characters lack English meanings. No user study data is involved.
