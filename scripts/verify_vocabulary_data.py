import json
import os
import re
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

def validate_ruby_tags(html_str, context_info=""):
    """Validates that all <ruby> tags have matching <rt> and closing tags."""
    if not html_str:
        return True, []
    errors = []
    ruby_opens = len(re.findall(r'<ruby>', html_str))
    ruby_closes = len(re.findall(r'</ruby>', html_str))
    rt_opens = len(re.findall(r'<rt>', html_str))
    rt_closes = len(re.findall(r'</rt>', html_str))
    
    if ruby_opens != ruby_closes:
        errors.append(f"{context_info}: Mismatched <ruby> tags (opens: {ruby_opens}, closes: {ruby_closes})")
    if rt_opens != rt_closes:
        errors.append(f"{context_info}: Mismatched <rt> tags (opens: {rt_opens}, closes: {rt_closes})")
    if ruby_opens != rt_opens:
        errors.append(f"{context_info}: Mismatched ruby/rt counts (ruby: {ruby_opens}, rt: {rt_opens})")
        
    return len(errors) == 0, errors

def validate_vocab_file(file_path):
    print(f"\n--- Checking Vocabulary File: {os.path.basename(file_path)} ---")
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return False
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: JSON decoding failed: {e}")
        return False
        
    chapters = data.get('chapters', [])
    if not chapters and 'sections' in data:
        # Single chapter file
        chapters = [data]
        
    print(f"Found {len(chapters)} chapter/unit structure(s).")
    
    issues = 0
    total_words = 0
    total_yattemiyou = 0
    total_exercises = 0
    
    for c_idx, ch in enumerate(chapters):
        cid = ch.get('metadata', {}).get('chapter', f'unit_{c_idx}')
        topic = ch.get('metadata', {}).get('topic_ja') or ch.get('topic_ja', 'Untitled')
        
        # Check sections
        sections = ch.get('sections', [])
        for s_idx, sec in enumerate(sections):
            words = sec.get('words', [])
            total_words += len(words)
            for w_idx, w in enumerate(words):
                term = w.get('term_ja') or w.get('term')
                reading = w.get('reading')
                meaning_en = w.get('meaning_en') or w.get('en_meaning')
                if not term or not reading or not meaning_en:
                    print(f"  [WARN] Ch {cid} Sec {s_idx} word {w_idx}: Missing term/reading/meaning_en ({w})")
                    issues += 1
                
                # Check ruby tags
                ruby = w.get('ruby_html')
                if ruby:
                    valid, errs = validate_ruby_tags(ruby, f"Ch {cid} Word {term}")
                    if not valid:
                        for err in errs:
                            print(f"  [WARN] {err}")
                            issues += 1
                            
            # Check yattemiyou
            yatte = sec.get('yattemiyou', [])
            total_yattemiyou += len(yatte)
            for y_idx, y in enumerate(yatte):
                q = y.get('question_ja')
                ans = y.get('answer')
                if not q or not ans:
                    print(f"  [WARN] Ch {cid} Sec {s_idx} yattemiyou {y_idx}: Missing question_ja or answer")
                    issues += 1
                    
        # Check exercises
        exercises = ch.get('exercises', [])
        for e_idx, ex in enumerate(exercises):
            items = ex.get('items', [])
            total_exercises += len(items)
            for item_idx, itm in enumerate(items):
                q = itm.get('question_ja') or itm.get('sentence_ja') or itm.get('context_ja') or itm.get('target')
                ans = itm.get('answer') or itm.get('correctAnswer')
                if not q or not ans:
                    print(f"  [WARN] Ch {cid} Ex {e_idx+1} item {item_idx+1}: Missing question/target or answer")
                    issues += 1
                    
    print(f"Summary for {os.path.basename(file_path)}:")
    print(f"  Total Words: {total_words}")
    print(f"  Total 'やってみよう' Drills: {total_yattemiyou}")
    print(f"  Total Practice Exercise Items: {total_exercises}")
    print(f"  Validation issues: {issues}")
    return issues == 0

if __name__ == '__main__':
    data_dir = r'c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\vocabulary'
    if not os.path.exists(data_dir):
        print(f"Directory not found: {data_dir}")
        sys.exit(1)
        
    json_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.json')]
    if not json_files:
        print("No vocabulary JSON data files found to validate yet.")
        sys.exit(0)
        
    all_ok = True
    for jf in json_files:
        if not validate_vocab_file(jf):
            all_ok = False
            
    if all_ok:
        print("\nAll vocabulary data files validated successfully! 100% clean.")
    else:
        print("\nValidation completed with warnings/errors.")
