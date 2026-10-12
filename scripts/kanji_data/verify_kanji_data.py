#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for all Nihongo Intermediate Kanji data files.
Checks:
- JSON syntax and UTF-8 encoding
- Parts 1-5 kanji count (443 total N3 kanji)
- Review 300 kanji count and structure
- Special readings structure
- Mock tests structure and option validity
- Exercises Part 1 schema, question integrity, options consistency, ruby tags
"""

import sys
import os
import json
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

KANJI_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "kanji")

def check_ruby_tags(text, location_info):
    if not text:
        return []
    errors = []
    open_ruby = text.count("<ruby>")
    close_ruby = text.count("</ruby>")
    open_rt = text.count("<rt>")
    close_rt = text.count("</rt>")
    if open_ruby != close_ruby:
        errors.append(f"{location_info}: Mismatched <ruby> tags ({open_ruby} open, {close_ruby} close)")
    if open_rt != close_rt:
        errors.append(f"{location_info}: Mismatched <rt> tags ({open_rt} open, {close_rt} close)")
    if open_ruby != open_rt:
        errors.append(f"{location_info}: Ruby count ({open_ruby}) does not match rt count ({open_rt})")
    return errors

def verify_kanji_parts():
    print("--- Verifying Part 1-5 Kanji Files ---")
    total_kanji = 0
    all_kanji_chars = set()
    errors = []

    for i in range(1, 6):
        fn = f"part{i}_lessons_{str((i-1)*5+1).zfill(2)}_{str(i*5).zfill(2)}.json"
        fp = os.path.join(KANJI_DIR, fn)
        if not os.path.exists(fp):
            errors.append(f"Missing file: {fn}")
            continue
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"Failed to parse {fn}: {e}")
            continue

        lessons = data.get("lessons", [])
        if len(lessons) != 5:
            errors.append(f"{fn}: Expected 5 lessons, got {len(lessons)}")

        part_kanji_count = 0
        for l in lessons:
            k_list = l.get("kanji", [])
            part_kanji_count += len(k_list)
            for k in k_list:
                char = k.get("kanji")
                if not char:
                    errors.append(f"{fn} Lesson {l.get('lesson_number')}: Missing kanji character")
                elif char in all_kanji_chars:
                    if char == "男":
                        # Expected revisit: Lesson 5 (affixes) and Lesson 22 (special sound changes)
                        pass
                    else:
                        errors.append(f"Unexpected duplicate kanji found: {char} in {fn}")
                all_kanji_chars.add(char)
                
                # Check required fields
                for req in ["onyomi", "kunyomi", "words"]:
                    if req not in k:
                        errors.append(f"Kanji {char} missing field: {req}")

        print(f"  {fn}: {len(lessons)} lessons, {part_kanji_count} kanji")
        total_kanji += part_kanji_count

    print(f"Total N3 Target Kanji: {total_kanji} (Expected: 443)")
    if total_kanji != 443:
        errors.append(f"Expected 443 kanji in Parts 1-5, found {total_kanji}")
    return errors

def verify_review_300():
    print("--- Verifying Review 300 N4/N5 Kanji ---")
    errors = []
    fp = os.path.join(KANJI_DIR, "review_300_n4_n5.json")
    if not os.path.exists(fp):
        return ["Missing review_300_n4_n5.json"]
    try:
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Failed to parse review_300_n4_n5.json: {e}"]

    items = data.get("items", [])
    print(f"  review_300_n4_n5.json: {len(items)} kanji items")
    if len(items) != 300:
        errors.append(f"Expected 300 review kanji, got {len(items)}")
    return errors

def verify_special_readings():
    print("--- Verifying Special Readings ---")
    errors = []
    fp = os.path.join(KANJI_DIR, "special_readings.json")
    if not os.path.exists(fp):
        return ["Missing special_readings.json"]
    try:
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Failed to parse special_readings.json: {e}"]

    items = data.get("items", [])
    print(f"  special_readings.json: {len(items)} special reading items")
    if len(items) < 20:
        errors.append(f"Special readings items seems low ({len(items)})")
    return errors

def verify_mock_tests():
    print("--- Verifying Mock Tests ---")
    errors = []
    fp = os.path.join(KANJI_DIR, "kanji_mock_tests.json")
    if not os.path.exists(fp):
        return ["Missing kanji_mock_tests.json"]
    try:
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Failed to parse kanji_mock_tests.json: {e}"]

    chapters = data.get("chapters", [])
    print(f"  kanji_mock_tests.json: {len(chapters)} mock test chapters")
    for chap in chapters:
        ch_meta = chap.get("metadata", {})
        exercises = chap.get("exercises", [])
        total_items = 0
        for ex in exercises:
            for item in ex.get("items", []):
                total_items += 1
                if "options" in item:
                    if len(item["options"]) != 4:
                        errors.append(f"{ch_meta.get('chapter')} Item {item.get('item_id')}: expected 4 options, got {len(item['options'])}")
                    ans = str(item.get("answer"))
                    # answer is "1", "2", "3", or "4"
                    if ans not in ["1", "2", "3", "4"]:
                        errors.append(f"{ch_meta.get('chapter')} Item {item.get('item_id')}: invalid answer '{ans}'")
        print(f"    - {ch_meta.get('topic_ja')}: {len(exercises)} exercises, {total_items} items")
    return errors

def verify_exercises():
    errors = []
    for part in range(1, 6):
        fn = f"exercises_part{part}.json"
        fp = os.path.join(KANJI_DIR, fn)
        if not os.path.exists(fp):
            if part == 1:
                errors.append(f"Missing {fn}")
            continue
        print(f"--- Verifying Exercises Part {part} ---")
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"Failed to parse {fn}: {e}")
            continue

        lessons = data.get("lessons", [])
        print(f"  {fn}: {len(lessons)} lesson/review sections")
        total_exercises = 0
        total_q = 0
        q_ids = set()

        for sec in lessons:
            exercises = sec.get("exercises", [])
            total_exercises += len(exercises)
            for ex in exercises:
                ex_id = ex.get("exercise_id")
                items = ex.get("items", [])
                total_q += len(items)
                for it in items:
                    qid = it.get("id")
                    if not qid:
                        errors.append(f"{ex_id}: Item without id")
                    elif qid in q_ids:
                        errors.append(f"Duplicate question id: {qid}")
                    q_ids.add(qid)

                    # Check ruby tags
                    for key in ["question_ja", "sentence", "ruby_html", "explanation"]:
                        if key in it:
                            errors.extend(check_ruby_tags(it[key], f"{ex_id} Item {qid} [{key}]"))

                    # Check answer existence
                    if "answer" not in it and "reading" not in it and "answers" not in it:
                        errors.append(f"{ex_id} Item {qid}: missing answer or reading")

        print(f"  Total Part {part} exercises: {total_exercises}, total question items: {total_q}")
        min_expected = 140 if part == 1 else 60
        if total_q < min_expected:
            errors.append(f"Part {part} questions count is lower than expected: {total_q}")
    return errors

def main():
    all_errors = []
    all_errors.extend(verify_kanji_parts())
    all_errors.extend(verify_review_300())
    all_errors.extend(verify_special_readings())
    all_errors.extend(verify_mock_tests())
    all_errors.extend(verify_exercises())

    print("\n" + "="*50)
    if not all_errors:
        print("ALL KANJI DATA VERIFICATIONS PASSED SUCCESSFULLY! (0 errors)")
        sys.exit(0)
    else:
        print(f"VERIFICATION FAILED: Found {len(all_errors)} errors:")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()
