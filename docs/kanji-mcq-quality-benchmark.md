# Kanji MCQ quality benchmark (writing direction, kana -> kanji)

Captured 2026-11-04 from a certification-style mock exam the user supplied as
the quality reference for this app's Kanji section multiple choice. The source
image is personal study material and is kept in private storage only; this file
records the transferable design rules so the generator in `js/distractors.js`
can be checked against them. The full question-by-question tactic catalogue
lives in private storage with the image; this file is the non-sensitive
summary.

## Reference pattern

Question: a sentence with the target word given in kana, e.g.
`彼は中学生のとき [だんたい] で旅行したことがなつかしいと言っている。`
Four options, all two-kanji compounds: `困休` `国地` `困体` `団体` (exactly
one is a real word).

Second question: `[くやくしょ]` -> options `医投所` `市役所` `区役所` `匡股所`
(exactly one is spelled for くやくしょ; 市役所 is a real word read
しやくしょ).

## Why these are hard (the rules the generator follows)

1. **No pure-recognition shortcut.** Most distractors are fake compounds:
   real kanji combined into non-words (`困体`, `国地`, `匡股所`). A learner
   cannot pick the answer by recognizing a familiar word among unfamiliar
   ones; they must recall the exact spelling of the target. (Recognition
   still helps a learner who knows the target - the pattern shifts the
   advantage to spelling recall, it does not remove recognition.)
2. **Every substitution is a glyph look-alike.** Each swapped kanji shares a
   radical or component with the one it replaces: 団/困/国 all sit inside 囗,
   体/休 both sit on 亻 (the difference is 本 vs 木), 区/医/匡 share 匚.
   Nothing looks broken or random.
3. **Same length and shape.** All options have the target's character count
   and morphological shape (compound for compound, okurigana kept).
4. **Real-word bait, in varying counts.** Some options are real words: a
   near-reading word (市役所 しやくしょ against くやくしょ), or even several
   real homophones of the prompt at once (a かちょう row with 家長 and
   科長), where the sentence context is what disambiguates. The reference
   form does NOT cap real words at one per question.
5. **Positional variety.** Distractors do not all differ from the answer in
   the same place or all share the same wrong kanji (at most two options may
   carry the same substitute character at the same position, or swap the same
   position). A uniform row would spotlight the answer by elimination.
6. **Never a second correct answer.** No distractor is a valid spelling of
   the prompt's reading. In the reference form this holds because its
   homophone rows come with sentence context; this app's prompts are bare
   kana without context, so the rule here is stricter: no option may be
   readable as the prompt at all.
7. **Externally validated non-words.** Corpus absence is not proof that a
   synthetic compound is not a word. Generated distractors are audited
   against JMdict (rev 1.09): any synthetic option attested as a word or
   alternate spelling readable like the prompt is excluded at generation
   time (see JM_AUDIT_EXCLUSIONS in `js/distractors.js`; four collisions were
   found across all 971 kanji words: 越える/超える, 少女/小女, 少々/小々,
   受験/受検). Synthetic options that are real words only under other
   readings (e.g. 市報 しほう against いちば) are allowed but counted as real
   words, not synthetics, when judging a row's difficulty.

## Implementation

`pickDistractors(target, 'writing', universe, opts)` in `js/distractors.js`:

- multi-kanji targets: single-position glyph-swap compounds rank highest
  (70 + 3 x shape similarity), two-position swaps next (45 + 2 x sum), one
  eligible real word last (same length, aligned or shared kanji required);
  other real words sink below every synthetic candidate and only fill gaps.
  The one-real-word ranking is this app's difficulty choice (rule 4 shows
  the reference form varies), not a benchmark-derived law.
- single-kanji targets: unchanged - distractors are real look-alike kanji.
- homophone exclusion: any corpus word whose reading variants intersect the
  prompt's is forbidden, plus the JMdict audit exclusions (rule 6/7).
- selection is deterministic (stable hash tie-breaks, never Math.random) and
  enforces rule 5 via per-position and per-substitute counters.

## Verification (2026-11-04, node, all 971 kanji words)

- 971/971 words get a full 3-distractor row.
- 0 violations: no option equals the target, no corpus homophone, no
  duplicate, at most one corpus-real word per multi-kanji row (single-kanji
  rows use real look-alike characters by design).
- 0 JMdict-attested alternate answers (rule 7 audit).
