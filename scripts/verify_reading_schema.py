import glob
import json
import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')


def normalize_question(q, lesson_id, idx):
    """Mirror data-loader.js normalizeQuestion(q, lessonId, idx)."""
    if not q:
        return q
    q_id = q.get('questionId') or q.get('id') or f"{lesson_id}_q{idx + 1}"
    q_ja = q.get('questionText_ja') or q.get('question_ja') or ''
    q_en = q.get('questionText_en') or q.get('question_en') or ''
    raw_options = q.get('options') or []
    options = [
        opt if isinstance(opt, str) else (opt.get('text_ja') or '')
        for opt in raw_options
    ]
    options_en = [
        '' if isinstance(opt, str) else (opt.get('text_en') or '')
        for opt in raw_options
    ]
    correct_ans = int(q.get('correctAnswer')) if q.get('correctAnswer') is not None else None

    res = dict(q)
    res.update({
        'id': q_id,
        'question_ja': q_ja,
        'question_en': q_en,
        'options': options,
        'options_en': options_en,
        'correctAnswer': correct_ans
    })
    return res


def normalize_drill(d, lesson_id, idx):
    """Mirror data-loader.js normalizeDrill(d, lessonId, idx)."""
    if not d:
        return d
    d_id = d.get('drillId') or d.get('id') or f"{lesson_id}_d{idx + 1}"
    q_ja = d.get('questionText_ja') or d.get('question_ja') or d.get('instruction_ja') or d.get('title_ja') or ''
    q_en = d.get('questionText_en') or d.get('question_en') or d.get('instruction_en') or d.get('title_en') or ''
    raw_options = d.get('options') or []
    options = [
        opt if isinstance(opt, str) else (opt.get('text_ja') or '')
        for opt in raw_options
    ]
    options_en = [
        '' if isinstance(opt, str) else (opt.get('text_en') or '')
        for opt in raw_options
    ]

    correct_ans = None
    if d.get('correctAnswer') is not None:
        try:
            correct_ans = int(d.get('correctAnswer'))
        except (ValueError, TypeError):
            pass
    elif d.get('correctKey'):
        key = str(d.get('correctKey')).strip()
        found_idx = -1
        for i, opt in enumerate(raw_options):
            if isinstance(opt, dict) and str(opt.get('key', '')).strip() == key:
                found_idx = i
                break
        if found_idx >= 0:
            correct_ans = found_idx + 1
        elif len(key) == 1 and key.lower() in 'abcd':
            correct_ans = ord(key.lower()) - ord('a') + 1

    res = dict(d)
    res.update({
        'id': d_id,
        'question_ja': q_ja,
        'question_en': q_en,
        'options': options,
        'options_en': options_en,
    })
    if correct_ans is not None:
        res['correctAnswer'] = correct_ans
    return res


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    data_dir = os.path.join(project_root, 'data', 'reading')

    if not os.path.isdir(data_dir):
        print(f"ERROR: Data directory not found: {data_dir}", file=sys.stderr)
        sys.exit(1)

    json_files = sorted(glob.glob(os.path.join(data_dir, '*.json')))
    if not json_files:
        print(f"ERROR: No JSON files found in {data_dir}", file=sys.stderr)
        sys.exit(1)

    total_lessons = 0
    total_questions = 0
    total_drills = 0
    validation_errors = []
    file_summaries = []
    seen_problem_numbers = set()

    for file_path in json_files:
        fname = os.path.basename(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                validation_errors.append(f"{fname}: JSON parse failure: {e}")
                continue

        lessons = data.get('lessons', [])
        f_q_count = 0
        f_drill_count = 0

        for l_idx, lesson in enumerate(lessons):
            lid = lesson.get('id', f'lesson_{l_idx}')
            total_lessons += 1

            prob_num = lesson.get('problemNumber')
            if prob_num is not None:
                seen_problem_numbers.add(prob_num)

            # Passage check if present
            passage = lesson.get('passage', {})
            if passage:
                sentences = passage.get('sentences', [])
                for s_idx, s in enumerate(sentences):
                    if not s.get('text_ja'):
                        validation_errors.append(f"{fname} {lid} sentence {s_idx}: missing text_ja")

            # Validate Comprehension Questions
            comp_questions = lesson.get('comprehensionQuestions', [])
            for q_idx, raw_q in enumerate(comp_questions):
                f_q_count += 1
                norm_q = normalize_question(raw_q, lid, q_idx)
                qid = norm_q.get('id')

                # 1. Non-empty id
                if not qid:
                    validation_errors.append(f"{fname} {lid} Q#{q_idx}: missing id")

                # 2. Non-empty question_ja
                q_ja = norm_q.get('question_ja', '')
                if not isinstance(q_ja, str) or not q_ja.strip():
                    validation_errors.append(f"{fname} {lid} Q#{qid}: question_ja is empty")

                # 3. Exactly 4 valid option strings
                options = norm_q.get('options', [])
                if not isinstance(options, list) or len(options) != 4:
                    validation_errors.append(
                        f"{fname} {lid} Q#{qid}: options length is {len(options) if isinstance(options, list) else type(options)}, expected 4"
                    )
                else:
                    for opt_idx, opt in enumerate(options):
                        if not isinstance(opt, str) or not opt.strip():
                            validation_errors.append(
                                f"{fname} {lid} Q#{qid} Option {opt_idx + 1}: option is not a valid non-empty string"
                            )

                # 4. correctAnswer between 1 and 4
                ca = norm_q.get('correctAnswer')
                if ca is None or not isinstance(ca, int) or ca < 1 or ca > 4:
                    validation_errors.append(
                        f"{fname} {lid} Q#{qid}: correctAnswer must be an integer 1..4 (got {ca})"
                    )

            # Validate Foundation Drills
            drills = lesson.get('drills', [])
            for d_idx, raw_d in enumerate(drills):
                f_drill_count += 1
                norm_d = normalize_drill(raw_d, lid, d_idx)
                did = norm_d.get('id')

                if not did:
                    validation_errors.append(f"{fname} {lid} Drill#{d_idx}: missing id")

                d_ja = norm_d.get('question_ja', '')
                if not isinstance(d_ja, str) or not d_ja.strip():
                    validation_errors.append(f"{fname} {lid} Drill#{did}: question_ja is empty")

                # If drill has options, validate options
                if norm_d.get('options'):
                    opts = norm_d['options']
                    if not all(isinstance(o, str) and o.strip() for o in opts):
                        validation_errors.append(f"{fname} {lid} Drill#{did}: options contains invalid string")
                    if 'correctAnswer' in norm_d:
                        d_ca = norm_d['correctAnswer']
                        if not isinstance(d_ca, int) or d_ca < 1 or d_ca > len(opts):
                            validation_errors.append(
                                f"{fname} {lid} Drill#{did}: invalid correctAnswer {d_ca}"
                            )

        total_questions += f_q_count
        total_drills += f_drill_count
        file_summaries.append({
            'file': fname,
            'lessons': len(lessons),
            'questions': f_q_count,
            'drills': f_drill_count
        })

    # Assert exactly 101 comprehension questions across the database
    if total_questions != 101:
        validation_errors.append(f"Expected exactly 101 comprehension questions, but found {total_questions}")

    # Determine missing problem numbers in real exam range (14 to 64)
    expected_range = set(range(14, 65))
    missing_problems = sorted(list(expected_range - seen_problem_numbers))

    status = "PASS" if len(validation_errors) == 0 else "FAIL"

    report = {
        "status": status,
        "total_files": len(json_files),
        "total_lessons": total_lessons,
        "total_questions": total_questions,
        "expected_questions": 101,
        "questions_matched": total_questions == 101,
        "total_drills": total_drills,
        "missing_problem_numbers": missing_problems,
        "validation_errors": validation_errors,
        "file_summaries": file_summaries
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))

    if validation_errors:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
