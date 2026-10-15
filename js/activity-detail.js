// A day click shows only its date and recorded review count.
export function renderActivityDayHtml(day) {
  const reviews = Math.max(0, Number(day.reviews) || 0);
  const date = new Date(`${day.date}T12:00:00+05:30`);
  const label = new Intl.DateTimeFormat('en-US', {month:'short', day:'numeric', timeZone:'Asia/Kolkata'}).format(date);
  return `${label} - <span class="activity-inline-count">${reviews}</span> ${reviews === 1 ? 'review' : 'reviews'}`;
}
