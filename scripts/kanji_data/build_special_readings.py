import json
from pathlib import Path

def build_special_readings():
    items = [
        {
            "id": "SR01",
            "number": 1,
            "word": "明日",
            "reading": "あす",
            "ruby": "<ruby>明日<rt>あす</rt></ruby>",
            "meaning_en": "tomorrow",
            "meaning_zh": "明天"
        },
        {
            "id": "SR02",
            "number": 2,
            "word": "お母さん",
            "reading": "おかあさん",
            "ruby": "お<ruby>母<rt>かあ</rt></ruby>さん",
            "meaning_en": "(someone else's) mother",
            "meaning_zh": "母亲、妈妈"
        },
        {
            "id": "SR03",
            "number": 3,
            "word": "お父さん",
            "reading": "おとうさん",
            "ruby": "お<ruby>父<rt>とう</rt></ruby>さん",
            "meaning_en": "(someone else's) father",
            "meaning_zh": "父亲、爸爸"
        },
        {
            "id": "SR04",
            "number": 4,
            "word": "大人",
            "reading": "おとな",
            "ruby": "<ruby>大人<rt>おとな</rt></ruby>",
            "meaning_en": "adult",
            "meaning_zh": "大人、成年人"
        },
        {
            "id": "SR05",
            "number": 5,
            "word": "今日",
            "reading": "きょう",
            "ruby": "<ruby>今日<rt>きょう</rt></ruby>",
            "meaning_en": "today",
            "meaning_zh": "今天"
        },
        {
            "id": "SR06",
            "number": 6,
            "word": "今朝",
            "reading": "けさ",
            "ruby": "<ruby>今朝<rt>けさ</rt></ruby>",
            "meaning_en": "this morning",
            "meaning_zh": "今天早上"
        },
        {
            "id": "SR07",
            "number": 7,
            "word": "今年",
            "reading": "ことし",
            "ruby": "<ruby>今年<rt>ことし</rt></ruby>",
            "meaning_en": "this year",
            "meaning_zh": "今年"
        },
        {
            "id": "SR08",
            "number": 8,
            "word": "上手",
            "reading": "じょうず",
            "ruby": "<ruby>上手<rt>じょうず</rt></ruby>",
            "meaning_en": "skillful, good at",
            "meaning_zh": "擅长、高明"
        },
        {
            "id": "SR09",
            "number": 9,
            "word": "一日",
            "reading": "ついたち",
            "ruby": "<ruby>一日<rt>ついたち</rt></ruby>",
            "meaning_en": "1st day of the month",
            "meaning_zh": "一日、初一"
        },
        {
            "id": "SR10",
            "number": 10,
            "word": "時計",
            "reading": "とけい",
            "ruby": "<ruby>時計<rt>とけい</rt></ruby>",
            "meaning_en": "clock, watch",
            "meaning_zh": "时钟、手表"
        },
        {
            "id": "SR11",
            "number": 11,
            "word": "兄さん",
            "reading": "にいさん",
            "ruby": "<ruby>兄<rt>にい</rt></ruby>さん",
            "meaning_en": "(older) brother",
            "meaning_zh": "哥哥"
        },
        {
            "id": "SR12",
            "number": 12,
            "word": "姉さん",
            "reading": "ねえさん",
            "ruby": "<ruby>姉<rt>ねえ</rt></ruby>さん",
            "meaning_en": "(older) sister",
            "meaning_zh": "姐姐"
        },
        {
            "id": "SR13",
            "number": 13,
            "word": "二十",
            "reading": "はたち",
            "ruby": "<ruby>二十<rt>はたち</rt></ruby>",
            "meaning_en": "20 years old",
            "meaning_zh": "二十岁"
        },
        {
            "id": "SR14",
            "number": 14,
            "word": "二十日",
            "reading": "はつか",
            "ruby": "<ruby>二十日<rt>はつか</rt></ruby>",
            "meaning_en": "20th day of the month, 20 days",
            "meaning_zh": "二十日、二十号"
        },
        {
            "id": "SR15",
            "number": 15,
            "word": "一人",
            "reading": "ひとり",
            "ruby": "<ruby>一人<rt>ひとり</rt></ruby>",
            "meaning_en": "one person, alone",
            "meaning_zh": "一个人、独自"
        },
        {
            "id": "SR16",
            "number": 16,
            "word": "二人",
            "reading": "ふたり",
            "ruby": "<ruby>二人<rt>ふたり</rt></ruby>",
            "meaning_en": "two people",
            "meaning_zh": "两个人"
        },
        {
            "id": "SR17",
            "number": 17,
            "word": "二日",
            "reading": "ふつか",
            "ruby": "<ruby>二日<rt>ふつか</rt></ruby>",
            "meaning_en": "2nd day of the month, two days",
            "meaning_zh": "二日、二号、两天"
        },
        {
            "id": "SR18",
            "number": 18,
            "word": "下手",
            "reading": "へた",
            "ruby": "<ruby>下手<rt>へた</rt></ruby>",
            "meaning_en": "unskillful, poor at",
            "meaning_zh": "不擅长、拙劣"
        },
        {
            "id": "SR19",
            "number": 19,
            "word": "部屋",
            "reading": "へや",
            "ruby": "<ruby>部屋<rt>へや</rt></ruby>",
            "meaning_en": "room",
            "meaning_zh": "房间"
        },
        {
            "id": "SR20",
            "number": 20,
            "word": "土産",
            "reading": "みやげ",
            "ruby": "<ruby>土産<rt>みやげ</rt></ruby>",
            "meaning_en": "souvenir, local specialty present",
            "meaning_zh": "土特产、伴手礼"
        },
        {
            "id": "SR21",
            "number": 21,
            "word": "八百屋",
            "reading": "やおや",
            "ruby": "<ruby>八百屋<rt>やおや</rt></ruby>",
            "meaning_en": "greengrocer, fruit and vegetable shop",
            "meaning_zh": "蔬菜水果店"
        }
    ]

    out_file = Path(r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\kanji\special_readings.json")
    payload = {
        "title": "特別な読み方をする漢字の言葉",
        "description": "N4までの漢字(300字)で特別な読み方をする漢字の言葉です。",
        "source_page": "Bessatsu p. 36",
        "total_items": len(items),
        "items": items
    }
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Generated {out_file} with {len(items)} items.")

if __name__ == "__main__":
    build_special_readings()
