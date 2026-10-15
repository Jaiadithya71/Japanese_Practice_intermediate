// A day click shows only its date and recorded review count.
export function renderActivityDayHtml(day) {
  const reviews = Math.max(0, Number(day.reviews) || 0);
  return `<span class="activity-inline-count">${reviews}</span> ${reviews === 1 ? 'review' : 'reviews'}`;
}
