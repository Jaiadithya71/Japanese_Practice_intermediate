import { entries } from '../data/kanji/vocab_character_meanings.js';

export function vocabularyKanjiMeanings(word = '') {
  return [...new Set([...word].filter(char => /[\u4e00-\u9fff]/.test(char)))].map(kanji => ({
    kanji, meanings: entries[kanji] || []
  })).filter(item => item.meanings.length);
}

export function renderVocabularyKanjiBreakdown(item, revealed) {
  document.getElementById('vocab-kanji-breakdown')?.remove();
  if (!item || item.type !== 'vocab' || !revealed) return;
  const parts = vocabularyKanjiMeanings(item.term_ja);
  const example = document.getElementById('card-example-box');
  if (!parts.length || !example) return;
  const row = document.createElement('div');
  row.id = 'vocab-kanji-breakdown';
  row.className = 'vocab-kanji-breakdown';
  row.setAttribute('aria-label', 'Kanji character meanings');
  const heading = document.createElement('div');
  heading.className = 'vocab-kanji-heading';
  heading.textContent = 'Kanji meanings';
  heading.title = 'Character meanings are memory cues, not a literal translation of the whole word.';
  row.append(heading);
  const chips = document.createElement('div');
  chips.className = 'vocab-kanji-chips';
  for (const {kanji, meanings} of parts) {
    const chip = document.createElement('span');
    chip.className = 'vocab-kanji-chip';
    chip.title = `${kanji}: ${meanings.join(', ')}`;
    const char = document.createElement('b');
    char.className = 'font-ja';
    char.textContent = kanji;
    chip.append(char, document.createTextNode(` ${meanings.slice(0, 2).join(' / ')}`));
    chips.append(chip);
  }
  row.append(chips);
  const source = document.createElement('a');
  source.href = 'https://www.edrdg.org/edrdg/licence.html';
  source.textContent = 'KANJIDIC2 · EDRDG';
  source.className = 'vocab-kanji-source';
  source.target = '_blank';
  source.rel = 'noopener';
  source.addEventListener('click', event => event.stopPropagation());
  row.append(source);
  example.before(row);
}
