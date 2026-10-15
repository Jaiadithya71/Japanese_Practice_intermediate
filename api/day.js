const NORTHSTAR_DAY_API = 'https://northstar-status-26.vercel.app/api/day';
const ALLOWED_ORIGINS = new Set(['https://nihongo-n3-study.vercel.app']);
const json = (res, status, body) => res.status(status).setHeader('Content-Type', 'application/json; charset=utf-8').send(body);
const fail = (res, status, error) => json(res, status, { error });
const todayIST = () => new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date());
const isDate = value => typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(Date.parse(`${value}T00:00:00Z`));
const isInt = (value, min, max) => Number.isInteger(value) && value >= min && value <= max;

export default async function handler(req, res) {
  if (req.method !== 'POST') return fail(res, 405, 'POST required');
  if (!ALLOWED_ORIGINS.has(req.headers.origin)) return fail(res, 403, 'Origin not allowed');
  const body = req.body;
  if (!body || typeof body !== 'object' || Array.isArray(body)) return fail(res, 400, 'JSON object required');
  const { date, reviewsDone, uniqueItems, sessions, minutes, chapters, units } = body;
  if (!isDate(date) || date !== todayIST()) return fail(res, 400, 'date must be today in IST');
  if (!isInt(reviewsDone, 0, 10000) || !isInt(uniqueItems, 0, 10000) || uniqueItems > reviewsDone || !isInt(sessions, 0, 1000) || !isInt(minutes, 0, 600)) return fail(res, 400, 'Invalid daily totals');
  const validList = value => Array.isArray(value) && value.length <= 100 && value.every(item => typeof item === 'string' && item.trim().length > 0 && item.trim().length <= 120);
  if (!validList(chapters) || !validList(units)) return fail(res, 400, 'chapters and units must be string arrays of at most 100 entries');
  const tidy = values => [...new Set(values.map(value => value.trim()))];
  const change = {
    action: 'training', track: 'japanese', entryDate: date,
    status: reviewsDone > 0 ? 'done' : 'partial', reviewsDone, minutes,
    source: `N3 app daily aggregate, ${date}`,
    dayStats: { uniqueItems, sessions, chapters: tidy(chapters), units: tidy(units) }
  };
  const payload = JSON.stringify({ date: todayIST(), validateOnly: false, changes: [change] });
  if (new TextEncoder().encode(payload).byteLength > 8000) return fail(res, 413, 'Daily summary exceeds 8 KB');
  try {
    const response = await fetch(NORTHSTAR_DAY_API, { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json' }, body: payload });
    const text = await response.text();
    res.setHeader('Cache-Control', 'no-store');
    return res.status(response.status).send(text || '{}');
  } catch (_) {
    return fail(res, 502, 'Northstar daily summary unavailable');
  }
}
