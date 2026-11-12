// Shared lossless adapter for existing grammar exercise answer formats.
// Compound and free-text questions are self-checked, never auto-scored as MC.
export function grammarDrillContent(q = {}) {
  const rawOptions = Array.isArray(q.options) ? q.options.map(o => String(o).replace(/^([a-d]|\d+)[\s　]/, '')) : null;
  const raw = q.correct_answer;
  let correctIndex = /^[a-d]$/i.test(String(raw)) ? String(raw).toLowerCase().charCodeAt(0)-96 : /^\d+$/.test(String(raw)) ? Number(raw) : null;
  if (!rawOptions || !(correctIndex >= 1 && correctIndex <= rawOptions.length)) correctIndex = null;
  const format = value => Array.isArray(value) ? value.map(format).join('<br>') : value && typeof value === 'object' ? Object.entries(value).map(([k,v]) => `${k}: ${format(v)}`).join('<br>') : String(value ?? '');
  const answerText = correctIndex ? rawOptions[correctIndex-1] : (q.corrections ? q.corrections.map(c => `${c.index || ''} ${c.target || ''} → ${c.replacement || ''}`).join('<br>') : format(raw ?? q.correct_answers ?? 'No answer provided'));
  return {
    prompt: (q.prompt || '') + (rawOptions && !correctIndex ? `<div style="font-size:.9rem;margin-top:.75rem">${rawOptions.map((o,i) => `${i+1}. ${o}`).join('<br>')}</div>` : ''),
    options: correctIndex ? rawOptions : null,
    correctIndex,
    answerText,
    explanation_en:q.explanation_en || '', explanation_ja:q.explanation_ja || '',
    // Completed sentence + its book English translation, when the data has one
    // (sentence-ordering and mock-exam questions). Never invented elsewhere.
    full_sentence: q.full_sentence || '', full_sentence_en: q.full_sentence_en || '',
  };
}
