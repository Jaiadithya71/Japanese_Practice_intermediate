import lookupData from '../data/reading-lookup.js';

// Build-time MeCab/UniDic analysis keeps the phone lightweight and offline.
// Hashes address exact content, not a greedy dictionary substring match.
export function lookupHash(s) {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619) >>> 0;
  return String(h);
}
export function lookupEntry(id) { return lookupData.entries[id] || null; }
export function textLookupTokens(text, protectedTerms = new Set(), dictionary = new Map()) {
  const tokens = [];
  const chunks = text.match(/[^。！？!?\n]+[。！？!?]?|[。！？!?]/g) || [];
  let offset = 0;
  for (const chunk of chunks) {
    const at = text.indexOf(chunk, offset);
    const record = lookupData.chunks[lookupHash(chunk)];
    if (record && record[0] === chunk.length) {
      for (const [start, end, id] of record[1]) tokens.push({ start: at + start, end: at + end, id, term: lookupEntry(id)[0] });
    } else {
      // New/unanalysed text: only whole, dictionary-backed segment matches.
      // Never invent a word by grouping an arbitrary run of kanji.
      const segmenter = typeof Intl?.Segmenter === 'function' ? new Intl.Segmenter('ja', { granularity: 'word' }) : null;
      const segments = segmenter ? [...segmenter.segment(chunk)] : [];
      for (const s of segments) if (s.isWordLike && dictionary.has(s.segment)) {
        tokens.push({ start: at + s.index, end: at + s.index + s.segment.length, term: s.segment, id: null });
      }
    }
    offset = at + chunk.length;
  }
  // Protect every occurrence, including a lemma/form inside a longer token.
  const excluded = [];
  for (const term of protectedTerms) {
    let at = -1;
    while ((at = text.indexOf(term, at + 1)) !== -1) excluded.push([at, at + term.length]);
  }
  return tokens.filter(t => !excluded.some(([a,b]) => t.start < b && t.end > a));
}
const escapeAttr = s => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const namedEntities = {amp:'&',lt:'<',gt:'>',quot:'"',apos:"'",nbsp:'\u00a0'};
function decodedText(raw) {
  let text = '', boundaries = [0];
  for (const match of raw.matchAll(/&(?:#x[0-9a-f]+|#\d+|[a-z]+);|[\s\S]/gi)) {
    const value = match[0];
    let decoded = value;
    if (value[0] === '&') {
      const key = value.slice(1,-1);
      if (key[0] === '#') {
        const n = key[1]?.toLowerCase() === 'x' ? parseInt(key.slice(2),16) : parseInt(key.slice(1),10);
        if (n > 0 && n <= 0x10ffff) decoded = String.fromCodePoint(n);
      } else if (Object.hasOwn(namedEntities,key)) decoded = namedEntities[key];
    }
    text += decoded;
    for (let i = 0; i < decoded.length; i++) boundaries.push(match.index + value.length);
  }
  return {text,boundaries};
}

export function wrapReadingGloss(html, gloss) {
  if (!html) return html;
  // Collect base text across ruby boundaries before choosing word boundaries.
  // Keep the original markup/rt/sup bytes intact; wrap only base fragments.
  const parts = html.split(/(<[^>]+>)/g), nodes = [];
  let text = '', skip = 0, glossDepth = 0;
  for (let i = 0; i < parts.length; i++) {
    const part = parts[i];
    if (part[0] === '<') {
      if (/^<(rt|rp|sup|script|style)\b/i.test(part)) skip++;
      else if (/^<\/(rt|rp|sup|script|style)>/i.test(part)) skip = Math.max(0, skip-1);
      if (/^<span\b[^>]*\bgloss-term\b/i.test(part)) glossDepth++;
      else if (glossDepth && /^<span\b/i.test(part)) glossDepth++;
      else if (glossDepth && /^<\/span>/i.test(part)) glossDepth--;
      continue;
    }
    if (skip || glossDepth || !part) continue;
    const decoded = decodedText(part);
    nodes.push({i,start:text.length,end:text.length+decoded.text.length,...decoded});
    text += decoded.text;
  }
  const tokens = textLookupTokens(text, gloss?.protected, gloss?.map);
  for (const {i,start,end,boundaries} of nodes) {
    const relevant = tokens.filter(t => t.start < end && t.end > start);
    let cursor = 0, out = '';
    for (const token of relevant) {
      const a = boundaries[Math.max(start,token.start)-start], b = boundaries[Math.min(end,token.end)-start];
      out += parts[i].slice(cursor,a);
      const onclick = `event.stopPropagation(); showWordGloss(${JSON.stringify(token.term)}, this, '', ${token.id === null ? 'null' : token.id})`;
      out += `<span class="gloss-term"${token.start >= start ? ' data-gloss-start=""' : ''} data-gloss="${escapeAttr(token.term)}"${token.id === null ? '' : ` data-lookup-id="${token.id}"`} onclick="${escapeAttr(onclick)}">${parts[i].slice(a,b)}</span>`;
      cursor = b;
    }
    parts[i] = out + parts[i].slice(cursor);
  }
  return parts.join('');
}
