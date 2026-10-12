import json
import re
import sys
from pathlib import Path

def verify_ruby_tags(text, location=""):
    """Verify that all <ruby> and <rt> tags are properly paired and non-empty."""
    ruby_opens = len(re.findall(r'<ruby>', text))
    ruby_closes = len(re.findall(r'</ruby>', text))
    rt_opens = len(re.findall(r'<rt>', text))
    rt_closes = len(re.findall(r'</rt>', text))
    
    errors = []
    if ruby_opens != ruby_closes:
        errors.append(f"Mismatched <ruby> tags ({ruby_opens} open vs {ruby_closes} close) at {location}")
    if rt_opens != rt_closes:
        errors.append(f"Mismatched <rt> tags ({rt_opens} open vs {rt_closes} close) at {location}")
    if ruby_opens != rt_opens:
        errors.append(f"Unequal <ruby> and <rt> counts ({ruby_opens} ruby vs {rt_opens} rt) at {location}")
        
    # Check for empty rt tags
    if re.search(r'<rt>\s*</rt>', text):
        errors.append(f"Empty <rt> tag found at {location}")
        
    return errors

def verify_grammar_data():
    grammar_dir = Path("nihongo-intermediate/data/grammar")
    if not grammar_dir.exists():
        print(f"Error: {grammar_dir} does not exist.")
        return False
        
    files = list(grammar_dir.glob("*.json"))
    if not files:
        print(f"Warning: No JSON files found in {grammar_dir} yet.")
        return True
        
    total_errors = []
    total_items = 0
    total_drills = 0
    
    for f in sorted(files):
        print(f"\n--- Checking {f.name} ---")
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except Exception as e:
            total_errors.append(f"JSON syntax error in {f.name}: {e}")
            continue
            
        # Recursive string scanner for ruby tags
        def scan_obj(obj, path=""):
            errs = []
            if isinstance(obj, str):
                if "<ruby>" in obj or "<rt>" in obj:
                    errs.extend(verify_ruby_tags(obj, f"{f.name}:{path}"))
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    errs.extend(scan_obj(v, f"{path}.{k}"))
            elif isinstance(obj, list):
                for idx, v in enumerate(obj):
                    errs.extend(scan_obj(v, f"{path}[{idx}]"))
            return errs

        file_tag_errors = scan_obj(data, f.stem)
        total_errors.extend(file_tag_errors)
        
        # Specific structure checks
        if f.name == "grammar_index.json":
            if isinstance(data, list):
                total_items += len(data)
                print(f"  grammar_index: {len(data)} grammar patterns indexed.")
            elif isinstance(data, dict) and "patterns" in data:
                total_items += len(data["patterns"])
                print(f"  grammar_index: {len(data['patterns'])} grammar patterns indexed.")
        elif "part1" in f.name:
            sections = data.get("sections", [])
            print(f"  Part 1 sections: {len(sections)}")
            for sec in sections:
                pats = sec.get("patterns", [])
                drills = sec.get("drills", [])
                total_items += len(pats)
                total_drills += len(drills)
        elif "part2" in f.name:
            sections = data.get("sections", [])
            print(f"  Part 2 sections: {len(sections)}")
            for sec in sections:
                drills = sec.get("drills", [])
                total_drills += len(drills)
        elif "part3" in f.name:
            passages = data.get("passages", [])
            print(f"  Part 3 passages: {len(passages)}")
        elif "mock_test" in f.name:
            questions = data.get("questions", [])
            print(f"  Mock test questions: {len(questions)}")
        elif "intro" in f.name:
            print("  Intro & Usage guide loaded.")

    if total_errors:
        print("\n==========================================")
        print(f"VERIFICATION FAILED: {len(total_errors)} errors detected:")
        for err in total_errors[:20]:
            print("  -", err)
        if len(total_errors) > 20:
            print(f"  ... and {len(total_errors) - 20} more errors.")
        print("==========================================")
        return False
    else:
        print("\n==========================================")
        print("VERIFICATION PASSED: All grammar datasets are structurally sound and tags are valid!")
        print(f"Total grammar items tracked: {total_items}")
        print(f"Total drills/questions tracked: {total_drills}")
        print("==========================================")
        return True

if __name__ == "__main__":
    success = verify_grammar_data()
    sys.exit(0 if success else 1)
