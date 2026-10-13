#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_word_contexts.py
Builds context sentences for N3 kanji words.

Search order (first hit wins):
1. The word's own vocab example (the 254 vocab overlaps)
2. Kanji exercise question_ja
3. Reading passage sentences
4. Grammar example sentences
5. Any vocab example containing the term

Constraints:
- Sentence length: 8-60 characters
- HTML stripped clean (<ruby>, etc.)
- Shorter preferred when multiple candidates exist

Outputs:
- data/word_contexts.json
- data/kanji/word_contexts.json
Schema:
  {
    "<term_ja>": [
      {
        "sentence_ja": "...",
        "meaning": "...",
        "source": "...",
        "ja": "...",
        "en": "...",
        "src": "..."
      }
    ]
  }
"""

import os
import sys
import json
import glob
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
KANJI_DIR = os.path.join(DATA_DIR, 'kanji')
VOCAB_DIR = os.path.join(DATA_DIR, 'vocabulary')
READING_DIR = os.path.join(DATA_DIR, 'reading')
GRAMMAR_DIR = os.path.join(DATA_DIR, 'grammar')


def strip_html(text):
    if not text:
        return ""
    cleaned = re.sub(r'<[^>]+>', '', str(text))
    # Normalize whitespaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned


def load_all_kanji_words():
    kanji_files = sorted(glob.glob(os.path.join(KANJI_DIR, 'part*_lessons_*.json')))
    all_terms = set()
    target_terms = set()

    for kf in kanji_files:
        with open(kf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for les in data.get('lessons', []):
            for k in les.get('kanji', []):
                for w in k.get('words', []):
                    t = w.get('term_ja') or w.get('term')
                    if t:
                        all_terms.add(t)
                        if w.get('is_target'):
                            target_terms.add(t)

    return all_terms, target_terms


def load_vocab_data():
    vocab_by_exact_term = {}
    all_vocab_examples = []

    vocab_json_path = os.path.join(DATA_DIR, 'vocabulary.json')
    words = []
    if os.path.exists(vocab_json_path):
        with open(vocab_json_path, 'r', encoding='utf-8') as f:
            words = json.load(f)
    else:
        vocab_files = sorted(glob.glob(os.path.join(VOCAB_DIR, '*.json')))
        for vf in vocab_files:
            with open(vf, 'r', encoding='utf-8') as f:
                d = json.load(f)
            chs = d if isinstance(d, list) else (d.get('chapters') or ([d] if 'sections' in d else []))
            for ch in chs:
                meta = ch.get('metadata') or {}
                chId = meta.get('chapter', 'unknown')
                for sec in ch.get('sections', []):
                    for i, w in enumerate(sec.get('words', [])):
                        wid = w.get('id') or f"v{str(chId).zfill(2)}-{str(i+1).zfill(3)}"
                        words.append(dict(w, id=wid))

    for w in words:
        wid = w.get('id', 'vocab')
        term = w.get('term_ja') or w.get('term')
        ex_ja = strip_html(w.get('example_ja', ''))
        ex_en = strip_html(w.get('example_en', ''))
        if term and ex_ja:
            item = {
                'sentence_ja': ex_ja,
                'meaning': ex_en,
                'source': f"vocab:{wid}",
                'ja': ex_ja,
                'en': ex_en,
                'src': f"vocab:{wid}"
            }
            if term not in vocab_by_exact_term:
                vocab_by_exact_term[term] = item
            all_vocab_examples.append(item)

    return vocab_by_exact_term, all_vocab_examples


def load_kanji_exercises():
    ex_files = sorted(glob.glob(os.path.join(KANJI_DIR, 'exercises_part*.json')))
    exercises = []
    for ef in ex_files:
        with open(ef, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for les in data.get('lessons', []):
            l_num = les.get('lesson_number') or les.get('lesson') or les.get('lesson_id') or ''
            for ex in les.get('exercises', []):
                for itm in ex.get('items', []):
                    q_raw = itm.get('question_ja') or itm.get('sentence_ja') or itm.get('target') or ''
                    m_raw = itm.get('meaning_en') or itm.get('question_en') or itm.get('explanation_en') or ''
                    qid = itm.get('id') or f"L{l_num}"
                    clean_q = strip_html(q_raw)
                    clean_m = strip_html(m_raw)
                    if clean_q:
                        exercises.append({
                            'sentence_ja': clean_q,
                            'meaning': clean_m,
                            'source': f"kanji_ex:{qid}",
                            'ja': clean_q,
                            'en': clean_m,
                            'src': f"kanji_ex:{qid}"
                        })
    return exercises


def load_reading_sentences():
    reading_files = sorted(glob.glob(os.path.join(READING_DIR, '*.json')))
    sentences = []
    for rf in reading_files:
        with open(rf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for les in data.get('lessons', []):
            lid = les.get('id', 'reading')
            passage = les.get('passage', {})
            s_list = passage.get('sentences', []) if isinstance(passage, dict) else []
            for s in s_list:
                ja_raw = s.get('text_ja') or s.get('ja') or s.get('sentence_ja') or ''
                en_raw = s.get('text_en') or s.get('en') or s.get('sentence_en') or ''
                clean_ja = strip_html(ja_raw)
                clean_en = strip_html(en_raw)
                if clean_ja:
                    sentences.append({
                        'sentence_ja': clean_ja,
                        'meaning': clean_en,
                        'source': f"reading:{lid}",
                        'ja': clean_ja,
                        'en': clean_en,
                        'src': f"reading:{lid}"
                    })
    return sentences


def load_grammar_sentences():
    grammar_files = sorted(glob.glob(os.path.join(GRAMMAR_DIR, '*.json')))
    sentences = []
    for gf in grammar_files:
        with open(gf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = []
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            if 'patterns' in data:
                items = data['patterns']
            elif 'sections' in data:
                for s in data['sections']:
                    items.extend(s.get('patterns', []))
        for itm in items:
            pid = itm.get('pattern_id') or itm.get('id') or 'grammar'
            for ex in itm.get('example_sentences', []):
                ja_raw = ex.get('japanese') or ex.get('ja') or ex.get('sentence_ja') or ''
                en_raw = ex.get('english') or ex.get('en') or ex.get('meaning_en') or ''
                clean_ja = strip_html(ja_raw)
                clean_en = strip_html(en_raw)
                if clean_ja:
                    sentences.append({
                        'sentence_ja': clean_ja,
                        'meaning': clean_en,
                        'source': f"grammar:{pid}",
                        'ja': clean_ja,
                        'en': clean_en,
                        'src': f"grammar:{pid}"
                    })
    return sentences


def build_word_contexts():
    all_terms, target_terms = load_all_kanji_words()
    print(f"Loaded {len(all_terms)} distinct terms ({len(target_terms)} target terms) from Kanji DB.")

    vocab_by_exact_term, all_vocab_examples = load_vocab_data()
    kanji_exercises = load_kanji_exercises()
    reading_sentences = load_reading_sentences()
    grammar_sentences = load_grammar_sentences()

    print(f"Candidate pools loaded:")
    print(f"  Vocab exact terms: {len(vocab_by_exact_term)}")
    print(f"  Vocab all examples: {len(all_vocab_examples)}")
    print(f"  Kanji exercises: {len(kanji_exercises)}")
    print(f"  Reading sentences: {len(reading_sentences)}")
    print(f"  Grammar sentences: {len(grammar_sentences)}")

    contexts = {}

    for term in sorted(all_terms):
        found = None

        # 1. The word's own vocab example (exact match)
        if term in vocab_by_exact_term:
            found = vocab_by_exact_term[term]

        # 2. Kanji exercise question_ja
        if not found:
            cands = [s for s in kanji_exercises if term in s['sentence_ja'] and 8 <= len(s['sentence_ja']) <= 60]
            if cands:
                found = min(cands, key=lambda s: len(s['sentence_ja']))

        # 3. Reading passage sentence
        if not found:
            cands = [s for s in reading_sentences if term in s['sentence_ja'] and 8 <= len(s['sentence_ja']) <= 60]
            if cands:
                found = min(cands, key=lambda s: len(s['sentence_ja']))

        # 4. Grammar example sentence
        if not found:
            cands = [s for s in grammar_sentences if term in s['sentence_ja'] and 8 <= len(s['sentence_ja']) <= 60]
            if cands:
                found = min(cands, key=lambda s: len(s['sentence_ja']))

        # 5. Any vocab example containing term
        if not found:
            cands = [s for s in all_vocab_examples if term in s['sentence_ja'] and 8 <= len(s['sentence_ja']) <= 60]
            if cands:
                found = min(cands, key=lambda s: len(s['sentence_ja']))

        if found:
            # Wrap in array conforming to prompt schema
            contexts[term] = [found]

    total_covered = len(contexts)
    target_covered = sum(1 for t in target_terms if t in contexts)
    target_pct = (target_covered / len(target_terms) * 100) if target_terms else 0
    total_pct = (total_covered / len(all_terms) * 100) if all_terms else 0

    print(f"Context sentence building complete:")
    print(f"  Total terms covered: {total_covered}/{len(all_terms)} ({total_pct:.1f}%)")
    print(f"  Target terms covered: {target_covered}/{len(target_terms)} ({target_pct:.1f}%)")

    assert target_pct >= 60.0, f"Target coverage {target_pct:.1f}% below required 60%!"

    out1 = os.path.join(DATA_DIR, 'word_contexts.json')
    out2 = os.path.join(KANJI_DIR, 'word_contexts.json')

    with open(out1, 'w', encoding='utf-8') as f:
        json.dump(contexts, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out1}")

    with open(out2, 'w', encoding='utf-8') as f:
        json.dump(contexts, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {out2}")


if __name__ == '__main__':
    build_word_contexts()
