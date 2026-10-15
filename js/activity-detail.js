// A day click shows only its date and recorded review count.
export function renderActivityDayHtml(day) {
  const reviews = Math.max(0, Number(day.reviews) || 0);
  const date = new Date(`${day.date}T12:00:00+05:30`);
  const label = new Intl.DateTimeFormat('en-GB', {day:'numeric', month:'long', year:'numeric', timeZone:'Asia/Kolkata'}).format(date);
  return `<h4>${label}</h4><p class="activity-day-count"><strong>${reviews}</strong> ${reviews === 1 ? 'review' : 'reviews'}</p>`;
}
