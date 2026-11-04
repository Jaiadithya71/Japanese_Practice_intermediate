# Kanji MCQ quality benchmark (writing direction, kana -> kanji)

Captured 2026-11-04 from a certification-style mock exam the user supplied as
the quality reference for this app's Kanji section multiple choice. The source
image is personal study material and is kept in private storage only; this file
records the transferable design rules so the generator in `js/distractors.js`
can be checked against them.

## Reference pattern

Question: a sentence with the target word given in kana, e.g.
`彼は中学生のとき [だんたい] で旅行したことがなつかしいと言っている。`
Four options, all two-kanji compounds: `困休` `国地` `困体` `団体` (correct).

Second question: `[くやくしょ]` -> options `医投所` `市役所` `区役所` (correct)
`匡股所`.

## Why these are hard (the rules the generator follows)

1. **No recognition shortcut.** Most distractors are fake compounds: real kanji
   combined into non-words (`困体`, `国地`, `匡股所`). A learner cannot
   eliminate an option because "I know that word is read differently" - they
   must recall the exact spelling of the target.
2. **Every substitution is a glyph look-alike.** Each swapped kanji shares a
   radical or component with the one it replaces: 団/困/国 all sit inside 囗,
   体/休 share 亻, 区/医/匡 share 匚. Nothing looks broken or random.
3. **Same length and shape.** All options have the target's character count and
   morphological shape (compound for compound, okurigana kept).
4. **At most one real word.** One option may be a genuine word that nearly
   matches, e.g. 市役所 (しやくしょ) against 区役所 (くやくしょ) - same suffix,
   near reading. More than one real word re-opens the recognition shortcut.
5. **Positional variety.** Distractors do not all differ from the answer in the
   same place or all share the same wrong kanji (at most two options may carry
   the same substitute character at the same position, or swap the same
   position). A uniform row would spotlight the answer by elimination.
6. **Never a second correct answer.** No distractor is a real spelling of the
   prompt's reading (homophones excluded).

## Implementation

`pickDistractors(target, 'writing', universe, opts)` in `js/distractors.js`:

- multi-kanji targets: single-position glyph-swap compounds rank highest
  (70 + 3 x shape similarity), two-position swaps next (45 + 2 x sum), one
  eligible real word last (same length, aligned or shared kanji required);
  other real words sink below every synthetic candidate and only fill gaps.
- single-kanji targets: unchanged - distractors are real look-alike kanji.
- selection is deterministic (stable hash tie-breaks, never Math.random) and
  enforces rule 5 via per-position and per-substitute counters.
