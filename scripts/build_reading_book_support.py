#!/usr/bin/env python3
"""Add furigana *_ruby fields to Reading book-mode sections that lack them:
preReading questions, commentary bodies, test advice texts and drill
instructions/titles. Readings come from the lesson vocabulary and the global
N3 vocabulary first (book-consistent), pykakasi as fallback.

Adds (only where the plain field exists and has kanji):
  preReading.question_ja/question      -> *_ruby
  commentary.text_ja/summary_ja/logicFlow -> *_ruby
  testAdvice.advice_ja/traps           -> *_ruby
  testAdvice.analysisSteps[].question_ja/analysis_ja -> *_ruby
  drills[].title_ja/instruction_ja     -> *_ruby
Idempotent: fields are regenerated deterministically.
"""
import json, glob, re, sys
import pykakasi

kakasi = pykakasi.kakasi()
KANJI_RE = re.compile(r'[一-龯々〆ヵヶ㐀-䶿]')
KANA_RE = re.compile(r'[ぁ-んァ-ンー]')

def has_kanji(s): return bool(KANJI_RE.search(s))
def is_kana(ch): return bool(KANA_RE.fullmatch(ch))

def split_runs(s):
    runs, cur, curk = [], '', None
    for ch in s:
        k = has_kanji(ch)
        if curk is None or k == curk:
            cur += ch; curk = k
        else:
            runs.append((cur, curk)); cur = ch; curk = k
    if cur: runs.append((cur, curk))
    return runs

def ruby_token(orig, hira):
    if not has_kanji(orig): return None
    i = 0
    while i < len(orig) and i < len(hira) and is_kana(orig[i]) and orig[i] == hira[i]: i += 1
    j = 0
    while j < len(orig) - i and j < len(hira) - i and is_kana(orig[-1-j]) and orig[-1-j] == hira[-1-j]: j += 1
    pre = orig[:i]; suf = orig[len(orig)-j:] if j else ''
    core_o = orig[i: len(orig)-j if j else len(orig)]
    core_h = hira[i: len(hira)-j if j else len(hira)]
    if not core_o or not has_kanji(core_o): return None
    runs = split_runs(core_o)
    rem = core_h; pieces = []; ok = True
    for text, isk in runs:
        if not isk:
            p = rem.find(text, 1 if (pieces and isinstance(pieces[-1], list)) else 0)
            if p < 0: ok = False; break
            if pieces and isinstance(pieces[-1], list):
                pieces[-1][1] = rem[:p]
            elif p > 0:
                ok = False; break
            pieces.append(text); rem = rem[p+len(text):]
        else:
            pieces.append([text, None])
    if ok:
        if pieces and isinstance(pieces[-1], list): pieces[-1][1] = rem
        elif rem: ok = False
    if not ok or any(isinstance(p, list) and not p[1] for p in pieces):
        return f'{pre}<ruby>{core_o}<rt>{core_h}</rt></ruby>{suf}'
    out = pre
    for p in pieces:
        if isinstance(p, list): out += f'<ruby>{p[0]}<rt>{p[1]}</rt></ruby>'
        else: out += p
    return out + suf

FIXUPS = [
    ('<ruby>朝一<rt>あさいち</rt></ruby><ruby>杯<rt>はい</rt></ruby>', '<ruby>朝一杯<rt>あさいっぱい</rt></ruby>'),
    ('<ruby>除外<rt>じょがい</rt></ruby><ruby>日<rt>ひ</rt></ruby>', '<ruby>除外日<rt>じょがいび</rt></ruby>'),
    ('<ruby>日乗<rt>にちじょう</rt></ruby><ruby>車券<rt>しゃけん</rt></ruby>', '<ruby>日<rt>にち</rt></ruby><ruby>乗車券<rt>じょうしゃけん</rt></ruby>'),
    ('<rt>ちー</rt>', '<rt>ちい</rt>'),
    ('<ruby>化粧<rt>けは</rt></ruby>', '<ruby>化粧<rt>けしょう</rt></ruby>'),
    ('<ruby>体<rt>からだ</rt></ruby>', '<ruby>体<rt>てい</rt></ruby>'),
    ('<ruby>人<rt>にん</rt></ruby>', '<ruby>人<rt>ひと</rt></ruby>'),
    ('<ruby>表<rt>おもて</rt></ruby>', '<ruby>表<rt>ひょう</rt></ruby>'),
    ('<ruby>月<rt>がつ</rt></ruby>', '<ruby>月<rt>げつ</rt></ruby>'),
    ('<ruby>水<rt>みず</rt></ruby>・<ruby>木<rt>き</rt></ruby>', '<ruby>水<rt>すい</rt></ruby>・<ruby>木<rt>もく</rt></ruby>'),
    ('<ruby>歳<rt>とし</rt></ruby>', '<ruby>歳<rt>さい</rt></ruby>'),
    ('<ruby>得<rt>え</rt></ruby>', '<ruby>得<rt>とく</rt></ruby>'),
    ('<ruby>方<rt>ほう</rt></ruby>', '<ruby>方<rt>かた</rt></ruby>'),
    ('9<ruby>時<rt>とき</rt></ruby>', '9<ruby>時<rt>くじ</rt></ruby>'),
    ('10<ruby>時<rt>とき</rt></ruby>', '10<ruby>時<rt>じゅうじ</rt></ruby>'),
    ('<ruby>振替<rt>ふりかえ</rt></ruby><ruby>日<rt>ひ</rt></ruby>', '<ruby>振替日<rt>ふりかえび</rt></ruby>'),
    ('1<ruby>位<rt>くらい</rt></ruby>', '1<ruby>位<rt>い</rt></ruby>'),
    ('<ruby>朝食<rt>ちょうしょく</rt></ruby><ruby>後<rt>のち</rt></ruby>', '<ruby>朝食後<rt>ちょうしょくご</rt></ruby>'),
    ('<ruby>金<rt>きん</rt></ruby>', '<ruby>金<rt>かね</rt></ruby>'),
    ('<ruby>注文<rt>ちゅうもん</rt></ruby><ruby>者<rt>もの</rt></ruby>', '<ruby>注文者<rt>ちゅうもんしゃ</rt></ruby>'),
    ('<ruby>月数<rt>つきすう</rt></ruby>', '<ruby>月数<rt>げっすう</rt></ruby>'),
    ('<ruby>日<rt>ひ</rt></ruby>の<ruby>回数', '<ruby>日<rt>にち</rt></ruby>の<ruby>回数'),
]

def rubyize_line(text, vocab_readings, overrides):
    out = []
    for item in kakasi.convert(text):
        o, h = item['orig'], item['hira']
        if has_kanji(o):
            vr = vocab_readings.get(o)
            if vr and vr != h:
                overrides.append((o, h, vr)); h = vr
            r = ruby_token(o, h)
            out.append(r if r else o)
        else:
            out.append(o)
    res = ''.join(out)
    for pat, rep in FIXUPS:
        res = res.replace(pat, rep)
    return res

def rubyize(text, vocab_readings, overrides):
    if not text or not has_kanji(text): return text
    if re.search(r'</?[a-zA-Z]', text):
        print('SKIP (markup inside):', text[:60]); return None
    # kakasi corrupts text across newlines and full-width equals signs;
    # segment on both and rejoin.
    segs = re.split(r'([\n＝])', text)
    out = []
    for s in segs:
        if s in ('\n', '＝') or not s:
            out.append(s)
        else:
            out.append(rubyize_line(s, vocab_readings, overrides))
    return ''.join(out)

def main():
    vocab_readings = {}
    for w in json.load(open('data/vocabulary.json')):
        if w.get('term_ja') and w.get('reading'):
            vocab_readings[w['term_ja']] = w['reading']
    changed_files, review = [], []
    for path in sorted(glob.glob('data/reading/*.json')):
        data = json.load(open(path))
        lessons = data.get('lessons', data if isinstance(data, list) else [])
        changed = False
        for l in lessons:
            local = dict(vocab_readings)
            for v in (l.get('vocabulary') or []):
                if v.get('term') and v.get('reading'): local[v['term']] = v['reading']
            overrides = []
            def do(obj, key):
                nonlocal changed
                val = obj.get(key)
                if isinstance(val, str) and has_kanji(val):
                    r = rubyize(val, local, overrides)
                    if r is None: return
                    if obj.get(key + '_ruby') != r:
                        obj[key + '_ruby'] = r; changed = True
                        review.append((path, l.get('id'), key, val, r))
            pr = l.get('preReading')
            if pr:
                do(pr, 'question_ja'); do(pr, 'question')
            c = l.get('commentary')
            if c:
                for k in ('text_ja', 'summary_ja', 'logicFlow'): do(c, k)
            ta = l.get('testAdvice')
            if ta:
                do(ta, 'advice_ja'); do(ta, 'traps')
                for st in (ta.get('analysisSteps') or []):
                    do(st, 'question_ja'); do(st, 'analysis_ja')
            for dr in (l.get('drills') or []):
                do(dr, 'title_ja'); do(dr, 'instruction_ja')
            # keep (注N) markers visible with furigana off: they live only in
            # ruby_html, so derive the plain text from the ruby when it carries
            # markers the plain text lacks.
            for s in ((l.get('passage') or {}).get('sentences') or []):
                ruby, plain = s.get('ruby_html') or '', s.get('text_ja') or ''
                if '(注' not in ruby or '(注' in plain or not plain: continue
                # drop injected [E]-style vocab markers absent from plain text
                ruby2 = re.sub(r'(<span class="vocab-marker"[^>]*>)\[[A-Z]\]', r'\1', ruby)
                stripped = re.sub(r'<rt>.*?</rt>', '', ruby2)
                stripped = re.sub(r'<[^>]+>', '', stripped)
                if stripped.replace('(注', '').replace(re.search(r'\(注\d+\)', stripped).group(0) if re.search(r'\(注\d+\)', stripped) else '', '') and re.sub(r'\(注\d+\)', '', stripped) == plain:
                    s['text_ja'] = stripped
                    changed = True
                    print('MARKER-SYNC', l.get('id'), stripped[:60])
                elif l.get('id') == 'dokkai-n3-p4-35':
                    # reviewed: plain drops お in お金 and all (注N) markers; ruby base is the curated text
                    s['text_ja'] = stripped
                    changed = True
                    print('MARKER-SYNC-FORCED', l.get('id'), stripped[:60])
                else:
                    print('MARKER-SKIP (base mismatch)', path, l.get('id'))
            for o, h, vr in overrides:
                print(f'OVERRIDE {path} {l.get("id")}: {o} kakasi={h} -> vocab={vr}')
        if changed:
            json.dump(data, open(path, 'w'), ensure_ascii=False, indent=2)
            open(path, 'a').write('\n')
            changed_files.append(path)
    print('CHANGED FILES:', changed_files)
    print('REVIEW COUNT:', len(review))
    for path, lid, key, val, r in review:
        print(f'--- {path} {lid} {key}')
        print('SRC :', val)
        print('RUBY:', r)

if __name__ == '__main__':
    main()
