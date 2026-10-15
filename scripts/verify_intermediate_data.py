import json
import os
import re
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

def validate_json_file(file_path):
    print(f"\n--- Checking: {os.path.basename(file_path)} ---")
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return False
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: JSON decoding failed: {e}")
        return False
        
    lessons = data.get('lessons', [])
    print(f"Found {len(lessons)} lesson(s).")
    
    issues = 0
    total_vocab = 0
    total_questions = 0
    total_drills = 0
    
    for i, lesson in enumerate(lessons):
        lid = lesson.get('id', f'idx_{i}')
        
        # Check required titles
        if not lesson.get('title_ja') or not lesson.get('title_en'):
            print(f"  [WARN] Lesson {lid}: Missing title_ja or title_en")
            issues += 1
                
        # Check passage if present
        passage = lesson.get('passage', {})
        if passage:
            sents = passage.get('sentences', [])
            for s_idx, s in enumerate(sents):
                if not s.get('text_ja') or not s.get('text_en'):
                    print(f"  [WARN] Lesson {lid} sentence {s_idx}: missing text_ja or text_en")
                    issues += 1
                # Check ruby matching tags
                ruby_text = s.get('ruby_html', '')
                if ruby_text:
                    open_ruby = ruby_text.count('<ruby>')
                    close_ruby = ruby_text.count('</ruby>')
                    open_rt = ruby_text.count('<rt>')
                    close_rt = ruby_text.count('</rt>')
                    if open_ruby != close_ruby or open_rt != close_rt:
                        print(f"  [WARN] Lesson {lid} sentence {s_idx}: malformed ruby tags (<ruby>:{open_ruby}/{close_ruby}, <rt>:{open_rt}/{close_rt})")
                        issues += 1

        # Check vocabulary
        vocab = lesson.get('vocabulary', [])
        total_vocab += len(vocab)
        for v_idx, v in enumerate(vocab):
            term = v.get('term') or v.get('word')
            reading = v.get('reading')
            meaning = v.get('meaning') or v.get('meaning_en')
            if not term or not reading or not meaning:
                print(f"  [WARN] Lesson {lid} vocab {v_idx}: missing term/reading/meaning")
                issues += 1

        # Check comprehension questions
        questions = lesson.get('comprehensionQuestions', []) or lesson.get('questions', [])
        total_questions += len(questions)
        for q_idx, q in enumerate(questions):
            q_text = q.get('questionText_ja') or q.get('question_ja')
            if not q_text:
                print(f"  [WARN] Lesson {lid} question {q_idx}: missing Japanese question text")
                issues += 1
            opts = q.get('options', [])
            if len(opts) < 2:
                print(f"  [WARN] Lesson {lid} question {q_idx}: fewer than 2 options")
                issues += 1
            # Check correctAnswer id or isCorrect flag
            correct = q.get('correctAnswer')
            has_correct = (correct is not None) or any(opt.get('isCorrect') for opt in opts)
            if not has_correct:
                print(f"  [WARN] Lesson {lid} question {q_idx}: no correct answer defined")
                issues += 1

        # Check drills
        drills = lesson.get('drills', [])
        total_drills += len(drills)
        
    print(f"Summary for {os.path.basename(file_path)}:")
    print(f"  Total Lessons: {len(lessons)}")
    print(f"  Total Vocab: {total_vocab}")
    print(f"  Total Dokkai Questions: {total_questions}")
    print(f"  Total Parsing Drills: {total_drills}")
    print(f"  Validation issues: {issues}")
    return issues == 0

if __name__ == '__main__':
    data_dir = r'c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\reading'
    if not os.path.exists(data_dir):
        print(f"Directory not found: {data_dir}")
        sys.exit(1)
        
    json_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.json')]
    if not json_files:
        print("No JSON data files found to validate.")
        sys.exit(0)
        
    all_ok = True
    for jf in json_files:
        if not validate_json_file(jf):
            all_ok = False
            
    if all_ok:
        print("\nAll data files validated successfully! 100% clean.")
    else:
        print("\nValidation completed with warnings/errors.")
