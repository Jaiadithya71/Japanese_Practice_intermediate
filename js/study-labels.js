/* Keep a section label only when it adds information to the chapter title. */
export function vocabularyLessonLabel(topic, section, fallback = '') {
  const chapter = String(topic || fallback || '').trim();
  const part = String(section || '').trim();
  if (!part || chapter.includes(part)) return chapter;
  return [chapter, part].filter(Boolean).join(' · ');
}
