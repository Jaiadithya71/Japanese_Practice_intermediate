import { entries } from '../data/kanji/vocab_character_meanings.js';
import { components as kanjiComponents } from '../data/kanji/kanji_components.js';

export function vocabularyKanjiMeanings(word = '') {
  return [...new Set([...word].filter(char => /[\u4e00-\u9fff]/.test(char)))].map(kanji => ({
    kanji, meanings: entries[kanji] || []
  })).filter(item => item.meanings.length);
}

function buildPartsPanel(kanji) {
  const panel = document.createElement('div');
  panel.className = 'vocab-kanji-parts';
  panel.setAttribute('aria-label', `${kanji} component parts`);
  panel.addEventListener('click', event => event.stopPropagation());
  const head = document.createElement('b');
  head.className = 'font-ja';
  head.textContent = kanji;
  panel.append(head);
  const entry = kanjiComponents[kanji];
  if (!entry) {
    panel.append(document.createTextNode(' - no component data for this kanji'));
    return panel;
  }
  if (!entry.parts.length) {
    panel.append(document.createTextNode(' is a building block itself - no smaller parts'));
    return panel;
  }
  panel.append(document.createTextNode(' = '));
  entry.parts.forEach(([char, meaning], index) => {
    if (index) panel.append(document.createTextNode(' + '));
    const part = document.createElement('span');
    part.className = 'vocab-kanji-part';
    const partChar = document.createElement('b');
    partChar.className = 'font-ja';
    partChar.textContent = char;
    part.append(partChar, document.createTextNode(meaning ? ` ${meaning}` : ''));
    panel.append(part);
  });
  if (entry.hidden) {
    const note = document.createElement('span');
    note.className = 'vocab-kanji-parts-note';
    note.textContent = ' (stroke-only marks not shown)';
    panel.append(note);
  }
  return panel;
}

export function renderVocabularyKanjiBreakdown(item, revealed) {
  document.getElementById('vocab-kanji-breakdown')?.remove();
  const word = !item ? '' : item.type === 'vocab' ? item.term_ja : item.type === 'kanji_word' ? item.word : '';
  if (!word || !revealed) return;
  const parts = vocabularyKanjiMeanings(word);
  const example = document.getElementById('card-example-box');
  if (!parts.length || !example) return;
  const row = document.createElement('div');
  row.id = 'vocab-kanji-breakdown';
  row.className = 'vocab-kanji-breakdown';
  row.setAttribute('aria-label', 'Kanji character meanings');
  const heading = document.createElement('div');
  heading.className = 'vocab-kanji-heading';
  heading.textContent = 'Kanji meanings · tap a kanji for its parts';
  heading.title = 'Character meanings are memory cues, not a literal translation of the whole word.';
  row.append(heading);
  const chips = document.createElement('div');
  chips.className = 'vocab-kanji-chips';
  let openPanel = null, openKanji = null;
  for (const {kanji, meanings} of parts) {
    const chip = document.createElement('span');
    chip.className = 'vocab-kanji-chip';
    chip.title = `${kanji}: ${meanings.join(', ')} — tap for component parts`;
    const char = document.createElement('b');
    char.className = 'font-ja';
    char.textContent = kanji;
    chip.append(char, document.createTextNode(` ${meanings.slice(0, 2).join(' / ')}`));
    chip.addEventListener('click', event => {
      event.stopPropagation();
      event.preventDefault();
      if (openPanel && openKanji === kanji) {
        openPanel.remove();
        openPanel = openKanji = null;
        return;
      }
      openPanel?.remove();
      openPanel = buildPartsPanel(kanji);
      openKanji = kanji;
      source.before(openPanel);
    });
    chips.append(chip);
  }
  row.append(chips);
  const source = document.createElement('div');
  source.className = 'vocab-kanji-source';
  const kvg = document.createElement('a');
  kvg.href = 'https://kanjivg.tagaini.net';
  kvg.textContent = 'KanjiVG';
  const edrdg = document.createElement('a');
  edrdg.href = 'https://www.edrdg.org/edrdg/licence.html';
  edrdg.textContent = 'KANJIDIC2 · EDRDG';
  for (const link of [kvg, edrdg]) {
    link.target = '_blank';
    link.rel = 'noopener';
    link.addEventListener('click', event => event.stopPropagation());
  }
  source.append(document.createTextNode('parts: '), kvg, document.createTextNode(' · meanings: '), edrdg);
  row.append(source);
  example.before(row);
}
