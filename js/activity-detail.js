// Read-only daily summary. Do not infer accuracy from aggregate review counts.
export function renderActivityDayHtml(day) {
  const number = value => Math.max(0, Number(value) || 0);
  const date = new Date(`${day.date}T12:00:00+05:30`);
  const label = new Intl.DateTimeFormat('en-GB', {day:'numeric', month:'long', year:'numeric', timeZone:'Asia/Kolkata'}).format(date);
  const reviews = number(day.reviews), fresh = number(day.newCards), minutes = number(day.minutes);
  const metrics = [[reviews, 'Reviews'], [fresh, 'New cards'], [Number(minutes.toFixed(1)), 'Minutes']];
  const pillars = [['vocab','Vocabulary'],['kanji','Kanji'],['grammar','Grammar'],['reading','Reading']];
  return `<h4>${label}</h4>
    <div class="activity-day-metrics">${metrics.map(([value,name]) => `<div><strong>${value}</strong><span>${name}</span></div>`).join('')}</div>
    ${reviews + fresh + minutes === 0 ? '<p class="activity-day-empty">No study activity recorded for this day.</p>' : ''}
    <dl class="activity-day-pillars">${pillars.map(([key,name]) => `<div><dt>${name}</dt><dd>${number(day.pillars?.[key])}</dd></div>`).join('')}</dl>
    ${day.wrong !== undefined ? `<p class="activity-day-note">Wrong attempts recorded: ${number(day.wrong)}</p>` : ''}
    <p class="activity-day-note">Subject counts include reviews and new cards. Dates use IST.</p>`;
}
