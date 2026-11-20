const STORAGE_KEY = 'nihongo_intermediate_review_again_by_lesson_v1';

export function loadSavedReviewAgainByLesson() {
  try {
    const value = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    return value && typeof value === 'object' && !Array.isArray(value) ? value : {};
  } catch (_) {
    return {};
  }
}

function validItems(items) {
  const seen = new Set();
  return (Array.isArray(items) ? items : []).filter(item => {
    const key = item?.key || (item?.id ? `V:${item.id}` : '');
    if (!key || seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

export function saveReviewAgainForLesson(chapterId, items) {
  const chapter = String(chapterId || '');
  if (!chapter) return;
  const saved = loadSavedReviewAgainByLesson();
  const list = validItems(items);
  if (!list.length) delete saved[chapter];
  else saved[chapter] = { items: list, updatedAt: Date.now() };
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(saved)); } catch (_) {}
}

export function clearReviewAgainForLesson(chapterId) {
  const saved = loadSavedReviewAgainByLesson();
  delete saved[String(chapterId || '')];
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(saved)); } catch (_) {}
}
