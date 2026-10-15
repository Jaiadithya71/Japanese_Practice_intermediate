# Part 1: Lessons 01 to 05 data builder
import json
import os

part1_data = {
    "metadata": {
        "part": 1,
        "title_ja": "一つの漢字で言葉になる漢字 & たくさんの言葉を作る漢字",
        "title_en": "Single-Kanji Words & Multi-Word Building Kanji",
        "lessons": [1, 2, 3, 4, 5]
    },
    "lessons": [
        {
            "lesson_number": 1,
            "title_ja": "訓読み：名詞",
            "title_en": "Kunyomi: Nouns",
            "page": 3,
            "kanji": [
                {
                    "kanji": "辺",
                    "onyomi": [],
                    "kunyomi": ["あたり"],
                    "words": [
                        {"term_ja": "辺り", "reading": "あたり", "ruby_html": "<ruby>辺<rt>あた</rt></ruby>り", "meaning_en": "Surroundings", "meaning_zh": "周围", "is_target": True}
                    ]
                },
                {
                    "kanji": "市",
                    "onyomi": ["シ"],
                    "kunyomi": ["いち"],
                    "words": [
                        {"term_ja": "市場", "reading": "いちば", "ruby_html": "<ruby>市場<rt>いちば</rt></ruby>", "meaning_en": "Market", "meaning_zh": "市场", "is_target": True}
                    ]
                },
                {
                    "kanji": "糸",
                    "onyomi": [],
                    "kunyomi": ["いと"],
                    "words": [
                        {"term_ja": "糸", "reading": "いと", "ruby_html": "<ruby>糸<rt>いと</rt></ruby>", "meaning_en": "Thread, yarn", "meaning_zh": "线", "is_target": False},
                        {"term_ja": "毛糸", "reading": "けいと", "ruby_html": "<ruby>毛糸<rt>けいと</rt></ruby>", "meaning_en": "Wool, yarn", "meaning_zh": "毛线", "is_target": True}
                    ]
                },
                {
                    "kanji": "命",
                    "onyomi": [],
                    "kunyomi": ["いのち"],
                    "words": [
                        {"term_ja": "命", "reading": "いのち", "ruby_html": "<ruby>命<rt>いのち</rt></ruby>", "meaning_en": "Life", "meaning_zh": "生命", "is_target": True}
                    ]
                },
                {
                    "kanji": "岩",
                    "onyomi": [],
                    "kunyomi": ["いわ"],
                    "words": [
                        {"term_ja": "岩", "reading": "いわ", "ruby_html": "<ruby>岩<rt>いわ</rt></ruby>", "meaning_en": "Rock", "meaning_zh": "岩石", "is_target": True}
                    ]
                },
                {
                    "kanji": "馬",
                    "onyomi": [],
                    "kunyomi": ["うま"],
                    "words": [
                        {"term_ja": "馬", "reading": "うま", "ruby_html": "<ruby>馬<rt>うま</rt></ruby>", "meaning_en": "Horse", "meaning_zh": "马", "is_target": True}
                    ]
                },
                {
                    "kanji": "貝",
                    "onyomi": [],
                    "kunyomi": ["かい"],
                    "words": [
                        {"term_ja": "貝", "reading": "かい", "ruby_html": "<ruby>貝<rt>かい</rt></ruby>", "meaning_en": "Shellfish", "meaning_zh": "贝", "is_target": True}
                    ]
                },
                {
                    "kanji": "型",
                    "onyomi": [],
                    "kunyomi": ["かた"],
                    "words": [
                        {"term_ja": "型", "reading": "かた", "ruby_html": "<ruby>型<rt>かた</rt></ruby>", "meaning_en": "Type, style", "meaning_zh": "类型", "is_target": True},
                        {"term_ja": "大型", "reading": "おおがた", "ruby_html": "<ruby>大型<rt>おおがた</rt></ruby>", "meaning_en": "Large, big", "meaning_zh": "大型", "is_target": True},
                        {"term_ja": "小型", "reading": "こがた", "ruby_html": "<ruby>小型<rt>こがた</rt></ruby>", "meaning_en": "Small, little", "meaning_zh": "小型", "is_target": True}
                    ]
                },
                {
                    "kanji": "語",
                    "onyomi": ["ゴ"],
                    "kunyomi": ["かた・る"],
                    "words": [
                        {"term_ja": "物語", "reading": "ものがたり", "ruby_html": "<ruby>物語<rt>ものがたり</rt></ruby>", "meaning_en": "Story, tale", "meaning_zh": "故事", "is_target": True}
                    ]
                },
                {
                    "kanji": "側",
                    "onyomi": [],
                    "kunyomi": ["がわ"],
                    "words": [
                        {"term_ja": "〜側", "reading": "〜がわ", "ruby_html": "〜<ruby>側<rt>がわ</rt></ruby>", "meaning_en": "Side", "meaning_zh": "侧", "is_target": False},
                        {"term_ja": "外側", "reading": "そとがわ", "ruby_html": "<ruby>外側<rt>そとがわ</rt></ruby>", "meaning_en": "Outside", "meaning_zh": "外侧", "is_target": True}
                    ]
                },
                {
                    "kanji": "草",
                    "onyomi": [],
                    "kunyomi": ["くさ"],
                    "words": [
                        {"term_ja": "草", "reading": "くさ", "ruby_html": "<ruby>草<rt>くさ</rt></ruby>", "meaning_en": "Grass, herbage", "meaning_zh": "草", "is_target": True}
                    ]
                },
                {
                    "kanji": "組",
                    "onyomi": [],
                    "kunyomi": ["くみ"],
                    "words": [
                        {"term_ja": "組", "reading": "くみ", "ruby_html": "<ruby>組<rt>くみ</rt></ruby>", "meaning_en": "Homeroom, class, group", "meaning_zh": "班级", "is_target": True},
                        {"term_ja": "番組", "reading": "ばんぐみ", "ruby_html": "<ruby>番組<rt>ばんぐみ</rt></ruby>", "meaning_en": "TV/Radio program", "meaning_zh": "节目", "is_target": False}
                    ]
                },
                {
                    "kanji": "雲",
                    "onyomi": [],
                    "kunyomi": ["くも"],
                    "words": [
                        {"term_ja": "雲", "reading": "くも", "ruby_html": "<ruby>雲<rt>くも</rt></ruby>", "meaning_en": "Cloud", "meaning_zh": "云", "is_target": False}
                    ]
                },
                {
                    "kanji": "毛",
                    "onyomi": [],
                    "kunyomi": ["け"],
                    "words": [
                        {"term_ja": "毛", "reading": "け", "ruby_html": "<ruby>毛<rt>け</rt></ruby>", "meaning_en": "Hair, fur, wool", "meaning_zh": "毛", "is_target": False},
                        {"term_ja": "毛糸", "reading": "けいと", "ruby_html": "<ruby>毛糸<rt>けいと</rt></ruby>", "meaning_en": "Wool, yarn", "meaning_zh": "毛线", "is_target": True}
                    ]
                },
                {
                    "kanji": "米",
                    "onyomi": [],
                    "kunyomi": ["こめ"],
                    "words": [
                        {"term_ja": "米", "reading": "こめ", "ruby_html": "<ruby>米<rt>こめ</rt></ruby>", "meaning_en": "Rice (raw grain)", "meaning_zh": "米", "is_target": False}
                    ]
                },
                {
                    "kanji": "酒",
                    "onyomi": [],
                    "kunyomi": ["さけ"],
                    "words": [
                        {"term_ja": "(お)酒", "reading": "(お)さけ", "ruby_html": "(お)<ruby>酒<rt>さけ</rt></ruby>", "meaning_en": "Alcohol, sake", "meaning_zh": "酒", "is_target": False}
                    ]
                },
                {
                    "kanji": "玉",
                    "onyomi": [],
                    "kunyomi": ["たま"],
                    "words": [
                        {"term_ja": "玉", "reading": "たま", "ruby_html": "<ruby>玉<rt>たま</rt></ruby>", "meaning_en": "Ball, sphere", "meaning_zh": "玉、球", "is_target": True}
                    ]
                },
                {
                    "kanji": "妻",
                    "onyomi": [],
                    "kunyomi": ["つま"],
                    "words": [
                        {"term_ja": "妻", "reading": "つま", "ruby_html": "<ruby>妻<rt>つま</rt></ruby>", "meaning_en": "Wife (own)", "meaning_zh": "妻子", "is_target": False}
                    ]
                },
                {
                    "kanji": "寺",
                    "onyomi": [],
                    "kunyomi": ["てら"],
                    "words": [
                        {"term_ja": "寺", "reading": "てら", "ruby_html": "<ruby>寺<rt>てら</rt></ruby>", "meaning_en": "Temple", "meaning_zh": "寺院", "is_target": False}
                    ]
                },
                {
                    "kanji": "供",
                    "onyomi": [],
                    "kunyomi": ["とも"],
                    "words": [
                        {"term_ja": "子供", "reading": "こども", "ruby_html": "<ruby>子供<rt>こども</rt></ruby>", "meaning_en": "Child", "meaning_zh": "孩子", "is_target": False}
                    ]
                },
                {
                    "kanji": "根",
                    "onyomi": [],
                    "kunyomi": ["ね"],
                    "words": [
                        {"term_ja": "根", "reading": "ね", "ruby_html": "<ruby>根<rt>ね</rt></ruby>", "meaning_en": "Root", "meaning_zh": "根", "is_target": True},
                        {"term_ja": "屋根", "reading": "やね", "ruby_html": "<ruby>屋根<rt>やね</rt></ruby>", "meaning_en": "Roof", "meaning_zh": "屋顶", "is_target": True}
                    ]
                },
                {
                    "kanji": "葉",
                    "onyomi": [],
                    "kunyomi": ["は"],
                    "words": [
                        {"term_ja": "葉", "reading": "は", "ruby_html": "<ruby>葉<rt>は</rt></ruby>", "meaning_en": "Leaf", "meaning_zh": "叶子", "is_target": False}
                    ]
                },
                {
                    "kanji": "畑",
                    "onyomi": [],
                    "kunyomi": ["はたけ"],
                    "words": [
                        {"term_ja": "畑", "reading": "はたけ", "ruby_html": "<ruby>畑<rt>はたけ</rt></ruby>", "meaning_en": "Field, vegetable plot", "meaning_zh": "旱田", "is_target": True}
                    ]
                },
                {
                    "kanji": "星",
                    "onyomi": [],
                    "kunyomi": ["ほし"],
                    "words": [
                        {"term_ja": "星", "reading": "ほし", "ruby_html": "<ruby>星<rt>ほし</rt></ruby>", "meaning_en": "Star", "meaning_zh": "星星", "is_target": False}
                    ]
                },
                {
                    "kanji": "窓",
                    "onyomi": [],
                    "kunyomi": ["まど"],
                    "words": [
                        {"term_ja": "窓", "reading": "まど", "ruby_html": "<ruby>窓<rt>まど</rt></ruby>", "meaning_en": "Window", "meaning_zh": "窗户", "is_target": False},
                        {"term_ja": "窓口", "reading": "まどぐち", "ruby_html": "<ruby>窓口<rt>まどぐち</rt></ruby>", "meaning_en": "Window, counter, ticket window", "meaning_zh": "窗口", "is_target": True}
                    ]
                },
                {
                    "kanji": "皆",
                    "onyomi": [],
                    "kunyomi": ["みな"],
                    "words": [
                        {"term_ja": "皆", "reading": "みな", "ruby_html": "<ruby>皆<rt>みな</rt></ruby>", "meaning_en": "Everyone, all", "meaning_zh": "大家", "is_target": False},
                        {"term_ja": "皆さん", "reading": "みなさん", "ruby_html": "<ruby>皆<rt>みな</rt></ruby>さん", "meaning_en": "Everyone (polite)", "meaning_zh": "大家", "is_target": False}
                    ]
                },
                {
                    "kanji": "昔",
                    "onyomi": [],
                    "kunyomi": ["むかし"],
                    "words": [
                        {"term_ja": "昔", "reading": "むかし", "ruby_html": "<ruby>昔<rt>むかし</rt></ruby>", "meaning_en": "Old times, the past", "meaning_zh": "以前", "is_target": False}
                    ]
                },
                {
                    "kanji": "虫",
                    "onyomi": [],
                    "kunyomi": ["むし"],
                    "words": [
                        {"term_ja": "虫", "reading": "むし", "ruby_html": "<ruby>虫<rt>むし</rt></ruby>", "meaning_en": "Insect, bug", "meaning_zh": "虫子", "is_target": False}
                    ]
                },
                {
                    "kanji": "雪",
                    "onyomi": [],
                    "kunyomi": ["ゆき"],
                    "words": [
                        {"term_ja": "雪", "reading": "ゆき", "ruby_html": "<ruby>雪<rt>ゆき</rt></ruby>", "meaning_en": "Snow", "meaning_zh": "雪", "is_target": False},
                        {"term_ja": "大雪", "reading": "おおゆき", "ruby_html": "<ruby>大雪<rt>おおゆき</rt></ruby>", "meaning_en": "Heavy snow, snowstorm", "meaning_zh": "大雪", "is_target": True}
                    ]
                }
            ]
        },
        {
            "lesson_number": 2,
            "title_ja": "訓読み：動詞(1)",
            "title_en": "Kunyomi: Verbs (1)",
            "page": 4,
            "kanji": [
                {
                    "kanji": "打",
                    "onyomi": [],
                    "kunyomi": ["う・つ"],
                    "words": [
                        {"term_ja": "打つ", "reading": "うつ", "ruby_html": "<ruby>打<rt>う</rt></ruby>つ", "meaning_en": "Hit, strike", "meaning_zh": "打", "is_target": True}
                    ]
                },
                {
                    "kanji": "押",
                    "onyomi": [],
                    "kunyomi": ["お・す", "お・さえる"],
                    "words": [
                        {"term_ja": "押す", "reading": "おす", "ruby_html": "<ruby>押<rt>お</rt></ruby>す", "meaning_en": "Push, press", "meaning_zh": "推、按", "is_target": False},
                        {"term_ja": "押し入れ", "reading": "おしいれ", "ruby_html": "<ruby>押<rt>お</rt></ruby>し<ruby>入<rt>い</rt></ruby>れ", "meaning_en": "Closet", "meaning_zh": "壁橱", "is_target": False},
                        {"term_ja": "押さえる", "reading": "おさえる", "ruby_html": "<ruby>押<rt>おさ</rt></ruby>える", "meaning_en": "Hold down, restrain", "meaning_zh": "压", "is_target": True}
                    ]
                },
                {
                    "kanji": "落",
                    "onyomi": [],
                    "kunyomi": ["お・ちる", "お・とす"],
                    "words": [
                        {"term_ja": "落ちる", "reading": "おちる", "ruby_html": "<ruby>落<rt>お</rt></ruby>ちる", "meaning_en": "Fall, drop", "meaning_zh": "掉落", "is_target": False},
                        {"term_ja": "落ち着く", "reading": "おちつく", "ruby_html": "<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>く", "meaning_en": "Calm down, feel more relaxed", "meaning_zh": "镇定", "is_target": True},
                        {"term_ja": "落とす", "reading": "おとす", "ruby_html": "<ruby>落<rt>お</rt></ruby>とす", "meaning_en": "Drop (transitive)", "meaning_zh": "弄掉", "is_target": False},
                        {"term_ja": "落とし物", "reading": "おとしもの", "ruby_html": "<ruby>落<rt>お</rt></ruby>とし<ruby>物<rt>もの</rt></ruby>", "meaning_en": "Lost property", "meaning_zh": "遗失物", "is_target": True}
                    ]
                },
                {
                    "kanji": "折",
                    "onyomi": [],
                    "kunyomi": ["お・る", "お・れる"],
                    "words": [
                        {"term_ja": "折る", "reading": "おる", "ruby_html": "<ruby>折<rt>お</rt></ruby>る", "meaning_en": "Fold, crease", "meaning_zh": "折", "is_target": True},
                        {"term_ja": "折れる", "reading": "おれる", "ruby_html": "<ruby>折<rt>お</rt></ruby>れる", "meaning_en": "Break, snap", "meaning_zh": "折断", "is_target": True}
                    ]
                },
                {
                    "kanji": "比",
                    "onyomi": [],
                    "kunyomi": ["くら・べる"],
                    "words": [
                        {"term_ja": "比べる", "reading": "くらべる", "ruby_html": "<ruby>比<rt>くら</rt></ruby>べる", "meaning_en": "Compare", "meaning_zh": "比较", "is_target": True}
                    ]
                },
                {
                    "kanji": "越",
                    "onyomi": [],
                    "kunyomi": ["こ・す", "こ・える"],
                    "words": [
                        {"term_ja": "乗り越す", "reading": "のりこす", "ruby_html": "<ruby>乗<rt>の</rt></ruby>り<ruby>越<rt>こ</rt></ruby>す", "meaning_en": "Go further than intended", "meaning_zh": "坐过站", "is_target": True},
                        {"term_ja": "引っ越し", "reading": "ひっこし", "ruby_html": "<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>し", "meaning_en": "Moving (house)", "meaning_zh": "搬家", "is_target": False},
                        {"term_ja": "引っ越す", "reading": "ひっこす", "ruby_html": "<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>す", "meaning_en": "Move home, relocate", "meaning_zh": "搬家", "is_target": True},
                        {"term_ja": "越える", "reading": "こえる", "ruby_html": "<ruby>越<rt>こ</rt></ruby>える", "meaning_en": "Go over, cross", "meaning_zh": "越过", "is_target": True}
                    ]
                },
                {
                    "kanji": "込",
                    "onyomi": [],
                    "kunyomi": ["こ・む"],
                    "words": [
                        {"term_ja": "込む", "reading": "こむ", "ruby_html": "<ruby>込<rt>こ</rt></ruby>む", "meaning_en": "Be crowded", "meaning_zh": "拥挤", "is_target": False}
                    ]
                },
                {
                    "kanji": "殺",
                    "onyomi": [],
                    "kunyomi": ["ころ・す"],
                    "words": [
                        {"term_ja": "殺す", "reading": "ころす", "ruby_html": "<ruby>殺<rt>ころ</rt></ruby>す", "meaning_en": "Kill", "meaning_zh": "杀", "is_target": True}
                    ]
                },
                {
                    "kanji": "泣",
                    "onyomi": [],
                    "kunyomi": ["な・く"],
                    "words": [
                        {"term_ja": "泣く", "reading": "なく", "ruby_html": "<ruby>泣<rt>な</rt></ruby>く", "meaning_en": "Cry, weep", "meaning_zh": "哭", "is_target": False}
                    ]
                },
                {
                    "kanji": "投",
                    "onyomi": [],
                    "kunyomi": ["な・げる"],
                    "words": [
                        {"term_ja": "投げる", "reading": "なげる", "ruby_html": "<ruby>投<rt>な</rt></ruby>げる", "meaning_en": "Throw, cast", "meaning_zh": "扔", "is_target": False}
                    ]
                },
                {
                    "kanji": "並",
                    "onyomi": [],
                    "kunyomi": ["なら・べる", "なら・ぶ"],
                    "words": [
                        {"term_ja": "並べる", "reading": "ならべる", "ruby_html": "<ruby>並<rt>なら</rt></ruby>べる", "meaning_en": "Line up, set out (transitive)", "meaning_zh": "摆放", "is_target": False},
                        {"term_ja": "並ぶ", "reading": "ならぶ", "ruby_html": "<ruby>並<rt>なら</rt></ruby>ぶ", "meaning_en": "Stand in line", "meaning_zh": "排队", "is_target": False}
                    ]
                },
                {
                    "kanji": "払",
                    "onyomi": [],
                    "kunyomi": ["はら・う"],
                    "words": [
                        {"term_ja": "払う", "reading": "はらう", "ruby_html": "<ruby>払<rt>はら</rt></ruby>う", "meaning_en": "Pay, wipe off", "meaning_zh": "付", "is_target": False}
                    ]
                },
                {
                    "kanji": "迎",
                    "onyomi": [],
                    "kunyomi": ["むか・える"],
                    "words": [
                        {"term_ja": "迎える", "reading": "むかえる", "ruby_html": "<ruby>迎<rt>むか</rt></ruby>える", "meaning_en": "Welcome, meet, greet", "meaning_zh": "迎接", "is_target": False}
                    ]
                },
                {
                    "kanji": "呼",
                    "onyomi": [],
                    "kunyomi": ["よ・ぶ"],
                    "words": [
                        {"term_ja": "呼ぶ", "reading": "よぶ", "ruby_html": "<ruby>呼<rt>よ</rt></ruby>ぶ", "meaning_en": "Call, summon", "meaning_zh": "叫", "is_target": False}
                    ]
                },
                {
                    "kanji": "渡",
                    "onyomi": [],
                    "kunyomi": ["わた・る", "わた・す"],
                    "words": [
                        {"term_ja": "渡る", "reading": "わたる", "ruby_html": "<ruby>渡<rt>わた</rt></ruby>る", "meaning_en": "Cross over", "meaning_zh": "渡过", "is_target": False},
                        {"term_ja": "渡す", "reading": "わたす", "ruby_html": "<ruby>渡<rt>わた</rt></ruby>す", "meaning_en": "Hand over", "meaning_zh": "递交", "is_target": False}
                    ]
                },
                {
                    "kanji": "笑",
                    "onyomi": [],
                    "kunyomi": ["わら・う"],
                    "words": [
                        {"term_ja": "笑う", "reading": "わらう", "ruby_html": "<ruby>笑<rt>わら</rt></ruby>う", "meaning_en": "Laugh, smile", "meaning_zh": "笑", "is_target": False}
                    ]
                }
            ]
        },
        {
            "lesson_number": 3,
            "title_ja": "訓読み：動詞(2)",
            "title_en": "Kunyomi: Verbs (2)",
            "page": 5,
            "kanji": [
                {
                    "kanji": "効",
                    "onyomi": [],
                    "kunyomi": ["き・く"],
                    "words": [
                        {"term_ja": "効く", "reading": "きく", "ruby_html": "<ruby>効<rt>き</rt></ruby>く", "meaning_en": "Be effective", "meaning_zh": "有效", "is_target": True}
                    ]
                },
                {
                    "kanji": "困",
                    "onyomi": [],
                    "kunyomi": ["こま・る"],
                    "words": [
                        {"term_ja": "困る", "reading": "こまる", "ruby_html": "<ruby>困<rt>こま</rt></ruby>る", "meaning_en": "Be troubled, have problems", "meaning_zh": "为难", "is_target": False}
                    ]
                },
                {
                    "kanji": "助",
                    "onyomi": [],
                    "kunyomi": ["たす・ける", "たす・かる"],
                    "words": [
                        {"term_ja": "助ける", "reading": "たすける", "ruby_html": "<ruby>助<rt>たす</rt></ruby>ける", "meaning_en": "Help, assist", "meaning_zh": "帮助", "is_target": True},
                        {"term_ja": "助かる", "reading": "たすかる", "ruby_html": "<ruby>助<rt>たす</rt></ruby>かる", "meaning_en": "Get out of difficulty, be helped out", "meaning_zh": "得救", "is_target": True}
                    ]
                },
                {
                    "kanji": "付",
                    "onyomi": [],
                    "kunyomi": ["つ・ける", "つ・く"],
                    "words": [
                        {"term_ja": "付ける", "reading": "つける", "ruby_html": "<ruby>付<rt>つ</rt></ruby>ける", "meaning_en": "Apply, put on", "meaning_zh": "戴上、挂上", "is_target": True},
                        {"term_ja": "日付", "reading": "ひづけ", "ruby_html": "<ruby>日付<rt>ひづけ</rt></ruby>", "meaning_en": "Date", "meaning_zh": "日期", "is_target": True},
                        {"term_ja": "付く", "reading": "つく", "ruby_html": "<ruby>付<rt>つ</rt></ruby>く", "meaning_en": "Stick, adhere", "meaning_zh": "附着", "is_target": True},
                        {"term_ja": "付き合う", "reading": "つきあう", "ruby_html": "<ruby>付<rt>つ</rt></ruby>き<ruby>合<rt>あ</rt></ruby>う", "meaning_en": "Socialize with, see one another, date", "meaning_zh": "交往；谈恋爱", "is_target": True},
                        {"term_ja": "気付く", "reading": "きづく", "ruby_html": "<ruby>気付<rt>きづ</rt></ruby>く", "meaning_en": "Notice, perceive", "meaning_zh": "发现", "is_target": True},
                        {"term_ja": "近付く", "reading": "ちかづく", "ruby_html": "<ruby>近付<rt>ちかづ</rt></ruby>く", "meaning_en": "Approach, draw closer", "meaning_zh": "靠近", "is_target": True}
                    ]
                },
                {
                    "kanji": "続",
                    "onyomi": [],
                    "kunyomi": ["つづ・く", "つづ・ける"],
                    "words": [
                        {"term_ja": "続く", "reading": "つづく", "ruby_html": "<ruby>続<rt>つづ</rt></ruby>く", "meaning_en": "Continue (intransitive)", "meaning_zh": "持续", "is_target": False},
                        {"term_ja": "続き", "reading": "つづき", "ruby_html": "<ruby>続<rt>つづ</rt></ruby>き", "meaning_en": "Continuation, next part", "meaning_zh": "后续", "is_target": True},
                        {"term_ja": "手続き", "reading": "てつづき", "ruby_html": "<ruby>手続<rt>てつづ</rt></ruby>き", "meaning_en": "Carry out a procedure", "meaning_zh": "手续", "is_target": True},
                        {"term_ja": "続ける", "reading": "つづける", "ruby_html": "<ruby>続<rt>つづ</rt></ruby>ける", "meaning_en": "Continue (transitive)", "meaning_zh": "继续", "is_target": False}
                    ]
                },
                {
                    "kanji": "届",
                    "onyomi": [],
                    "kunyomi": ["とど・ける", "とど・く"],
                    "words": [
                        {"term_ja": "届ける", "reading": "とどける", "ruby_html": "<ruby>届<rt>とど</rt></ruby>ける", "meaning_en": "Deliver, report (transitive)", "meaning_zh": "送到", "is_target": False},
                        {"term_ja": "届け", "reading": "とどけ", "ruby_html": "<ruby>届<rt>とど</rt></ruby>け", "meaning_en": "Report, notification", "meaning_zh": "申请表", "is_target": True},
                        {"term_ja": "届く", "reading": "とどく", "ruby_html": "<ruby>届<rt>とど</rt></ruby>く", "meaning_en": "Reach, arrive", "meaning_zh": "到达", "is_target": True}
                    ]
                },
                {
                    "kanji": "泊",
                    "onyomi": [],
                    "kunyomi": ["と・まる"],
                    "words": [
                        {"term_ja": "泊まる", "reading": "とまる", "ruby_html": "<ruby>泊<rt>と</rt></ruby>まる", "meaning_en": "Stay overnight", "meaning_zh": "住宿", "is_target": False}
                    ]
                },
                {
                    "kanji": "鳴",
                    "onyomi": [],
                    "kunyomi": ["な・く", "な・る"],
                    "words": [
                        {"term_ja": "鳴く", "reading": "なく", "ruby_html": "<ruby>鳴<rt>な</rt></ruby>く", "meaning_en": "Sing, cry (animal)", "meaning_zh": "叫", "is_target": False},
                        {"term_ja": "鳴る", "reading": "なる", "ruby_html": "<ruby>鳴<rt>な</rt></ruby>る", "meaning_en": "Ring, chime", "meaning_zh": "响", "is_target": False}
                    ]
                },
                {
                    "kanji": "逃",
                    "onyomi": [],
                    "kunyomi": ["に・げる"],
                    "words": [
                        {"term_ja": "逃げる", "reading": "にげる", "ruby_html": "<ruby>逃<rt>に</rt></ruby>げる", "meaning_en": "Escape, flee", "meaning_zh": "逃跑", "is_target": False}
                    ]
                },
                {
                    "kanji": "願",
                    "onyomi": [],
                    "kunyomi": ["ねが・う"],
                    "words": [
                        {"term_ja": "願う", "reading": "ねがう", "ruby_html": "<ruby>願<rt>ねが</rt></ruby>う", "meaning_en": "Hope, wish", "meaning_zh": "请求", "is_target": True}
                    ]
                },
                {
                    "kanji": "計",
                    "onyomi": ["ケイ"],
                    "kunyomi": ["はか・る"],
                    "words": [
                        {"term_ja": "計る", "reading": "はかる", "ruby_html": "<ruby>計<rt>はか</rt></ruby>る", "meaning_en": "Measure, keep time", "meaning_zh": "测量", "is_target": True}
                    ]
                },
                {
                    "kanji": "晴",
                    "onyomi": [],
                    "kunyomi": ["は・れる"],
                    "words": [
                        {"term_ja": "晴れる", "reading": "はれる", "ruby_html": "<ruby>晴<rt>は</rt></ruby>れる", "meaning_en": "Clear up, be sunny", "meaning_zh": "放晴", "is_target": False},
                        {"term_ja": "晴れ", "reading": "はれ", "ruby_html": "<ruby>晴<rt>は</rt></ruby>れ", "meaning_en": "Clear weather", "meaning_zh": "晴天", "is_target": False}
                    ]
                },
                {
                    "kanji": "減",
                    "onyomi": [],
                    "kunyomi": ["へ・る", "へ・らす"],
                    "words": [
                        {"term_ja": "減る", "reading": "へる", "ruby_html": "<ruby>減<rt>へ</rt></ruby>る", "meaning_en": "Decrease, grow smaller", "meaning_zh": "缩减", "is_target": True},
                        {"term_ja": "減らす", "reading": "へらす", "ruby_html": "<ruby>減<rt>へ</rt></ruby>らす", "meaning_en": "Reduce, make smaller", "meaning_zh": "减少", "is_target": True}
                    ]
                },
                {
                    "kanji": "負",
                    "onyomi": [],
                    "kunyomi": ["ま・ける"],
                    "words": [
                        {"term_ja": "負ける", "reading": "まける", "ruby_html": "<ruby>負<rt>ま</rt></ruby>ける", "meaning_en": "Lose, be defeated", "meaning_zh": "输", "is_target": False}
                    ]
                },
                {
                    "kanji": "学",
                    "onyomi": ["ガク"],
                    "kunyomi": ["まな・ぶ"],
                    "words": [
                        {"term_ja": "学ぶ", "reading": "まなぶ", "ruby_html": "<ruby>学<rt>まな</rt></ruby>ぶ", "meaning_en": "Study, learn", "meaning_zh": "学习", "is_target": True}
                    ]
                },
                {
                    "kanji": "申",
                    "onyomi": [],
                    "kunyomi": ["もう・す"],
                    "words": [
                        {"term_ja": "申す", "reading": "もうす", "ruby_html": "<ruby>申<rt>もう</rt></ruby>す", "meaning_en": "Say, tell (humble)", "meaning_zh": "说", "is_target": False},
                        {"term_ja": "申し上げる", "reading": "もうしあげる", "ruby_html": "<ruby>申<rt>もう</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げる", "meaning_en": "Say, express (humble)", "meaning_zh": "说", "is_target": False},
                        {"term_ja": "申し込み", "reading": "もうしこみ", "ruby_html": "<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>み", "meaning_en": "Application", "meaning_zh": "申请", "is_target": True},
                        {"term_ja": "申し込む", "reading": "もうしこむ", "ruby_html": "<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>む", "meaning_en": "Apply, propose", "meaning_zh": "申请", "is_target": True}
                    ]
                },
                {
                    "kanji": "喜",
                    "onyomi": [],
                    "kunyomi": ["よろこ・ぶ"],
                    "words": [
                        {"term_ja": "喜ぶ", "reading": "よろこぶ", "ruby_html": "<ruby>喜<rt>よろこ</rt></ruby>ぶ", "meaning_en": "Be glad, rejoice", "meaning_zh": "高兴", "is_target": False}
                    ]
                }
            ]
        },
        {
            "lesson_number": 4,
            "title_ja": "訓読み：形容詞など",
            "title_en": "Kunyomi: Adjectives & Others",
            "page": 6,
            "kanji": [
                {
                    "kanji": "暖",
                    "onyomi": [],
                    "kunyomi": ["あたた・かい", "あたた・まる", "あたた・める"],
                    "words": [
                        {"term_ja": "暖かい", "reading": "あたたかい", "ruby_html": "<ruby>暖<rt>あたた</rt></ruby>かい", "meaning_en": "Warm (climate)", "meaning_zh": "温暖", "is_target": False},
                        {"term_ja": "暖まる", "reading": "あたたまる", "ruby_html": "<ruby>暖<rt>あたた</rt></ruby>まる", "meaning_en": "Be warm up, heated", "meaning_zh": "暖和", "is_target": True},
                        {"term_ja": "暖める", "reading": "あたためる", "ruby_html": "<ruby>暖<rt>あたた</rt></ruby>める", "meaning_en": "Warm up, heat", "meaning_zh": "温暖", "is_target": True}
                    ]
                },
                {
                    "kanji": "厚",
                    "onyomi": [],
                    "kunyomi": ["あつ・い"],
                    "words": [
                        {"term_ja": "厚い", "reading": "あつい", "ruby_html": "<ruby>厚<rt>あつ</rt></ruby>い", "meaning_en": "Thick, bulky", "meaning_zh": "厚", "is_target": False}
                    ]
                },
                {
                    "kanji": "忙",
                    "onyomi": [],
                    "kunyomi": ["いそが・しい"],
                    "words": [
                        {"term_ja": "忙しい", "reading": "いそがしい", "ruby_html": "<ruby>忙<rt>いそが</rt></ruby>しい", "meaning_en": "Busy", "meaning_zh": "忙碌", "is_target": False}
                    ]
                },
                {
                    "kanji": "悲",
                    "onyomi": [],
                    "kunyomi": ["かな・しい"],
                    "words": [
                        {"term_ja": "悲しい", "reading": "かなしい", "ruby_html": "<ruby>悲<rt>かな</rt></ruby>しい", "meaning_en": "Sad, sorrowful", "meaning_zh": "悲伤", "is_target": False}
                    ]
                },
                {
                    "kanji": "黄",
                    "onyomi": [],
                    "kunyomi": ["き"],
                    "words": [
                        {"term_ja": "黄色", "reading": "きいろ", "ruby_html": "<ruby>黄色<rt>きいろ</rt></ruby>", "meaning_en": "Yellow color", "meaning_zh": "黄色", "is_target": False},
                        {"term_ja": "黄色い", "reading": "きいろい", "ruby_html": "<ruby>黄色<rt>きいろ</rt></ruby>い", "meaning_en": "Yellow", "meaning_zh": "黄色", "is_target": False}
                    ]
                },
                {
                    "kanji": "静",
                    "onyomi": [],
                    "kunyomi": ["しず・か"],
                    "words": [
                        {"term_ja": "静か(な)", "reading": "しずか(な)", "ruby_html": "<ruby>静<rt>しず</rt></ruby>か(な)", "meaning_en": "Quiet, silent", "meaning_zh": "安静", "is_target": False}
                    ]
                },
                {
                    "kanji": "涼",
                    "onyomi": [],
                    "kunyomi": ["すず・しい"],
                    "words": [
                        {"term_ja": "涼しい", "reading": "すずしい", "ruby_html": "<ruby>涼<rt>すず</rt></ruby>しい", "meaning_en": "Cool, refreshing", "meaning_zh": "凉爽", "is_target": False}
                    ]
                },
                {
                    "kanji": "久",
                    "onyomi": [],
                    "kunyomi": ["ひさ・しい"],
                    "words": [
                        {"term_ja": "久しぶり(な)", "reading": "ひさしぶり(な)", "ruby_html": "<ruby>久<rt>ひさ</rt></ruby>しぶり(な)", "meaning_en": "After a long time", "meaning_zh": "久违", "is_target": False}
                    ]
                },
                {
                    "kanji": "真",
                    "onyomi": ["シン"],
                    "kunyomi": ["ま"],
                    "words": [
                        {"term_ja": "真っ暗(な)", "reading": "まっくら(な)", "ruby_html": "<ruby>真<rt>ま</rt></ruby>っ<ruby>暗<rt>くら</rt></ruby>(な)", "meaning_en": "Pitch dark", "meaning_zh": "漆黑", "is_target": True}
                    ]
                },
                {
                    "kanji": "全",
                    "onyomi": ["ゼン"],
                    "kunyomi": ["まった・く", "すべ・て"],
                    "words": [
                        {"term_ja": "全て", "reading": "すべて", "ruby_html": "<ruby>全<rt>すべ</rt></ruby>て", "meaning_en": "All", "meaning_zh": "全部", "is_target": True}
                    ]
                },
                {
                    "kanji": "丸",
                    "onyomi": [],
                    "kunyomi": ["まる", "まる・い"],
                    "words": [
                        {"term_ja": "丸", "reading": "まる", "ruby_html": "<ruby>丸<rt>まる</rt></ruby>", "meaning_en": "Circle", "meaning_zh": "圆", "is_target": True},
                        {"term_ja": "丸い", "reading": "まるい", "ruby_html": "<ruby>丸<rt>まる</rt></ruby>い", "meaning_en": "Round, circular", "meaning_zh": "圆的", "is_target": False}
                    ]
                },
                {
                    "kanji": "難",
                    "onyomi": [],
                    "kunyomi": ["むずか・しい"],
                    "words": [
                        {"term_ja": "難しい", "reading": "むずかしい", "ruby_html": "<ruby>難<rt>むずか</rt></ruby>しい", "meaning_en": "Difficult", "meaning_zh": "难", "is_target": False}
                    ]
                },
                {
                    "kanji": "者",
                    "onyomi": ["シャ"],
                    "kunyomi": ["もの"],
                    "words": [
                        {"term_ja": "若者", "reading": "わかもの", "ruby_html": "<ruby>若者<rt>わかもの</rt></ruby>", "meaning_en": "Young people, youths", "meaning_zh": "年轻人", "is_target": True}
                    ]
                },
                {
                    "kanji": "若",
                    "onyomi": [],
                    "kunyomi": ["わか・い"],
                    "words": [
                        {"term_ja": "若い", "reading": "わかい", "ruby_html": "<ruby>若<rt>わか</rt></ruby>い", "meaning_en": "Young", "meaning_zh": "年轻", "is_target": False},
                        {"term_ja": "若者", "reading": "わかもの", "ruby_html": "<ruby>若者<rt>わかもの</rt></ruby>", "meaning_en": "Young people, youths", "meaning_zh": "年轻人", "is_target": True}
                    ]
                }
            ]
        },
        {
            "lesson_number": 5,
            "title_ja": "たくさんの言葉を作る漢字：音読み",
            "title_en": "Multi-Word Building Kanji: Onyomi",
            "page": 7,
            "kanji": [
                {
                    "kanji": "各",
                    "onyomi": ["カク"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "各〜", "reading": "かく〜", "ruby_html": "<ruby>各<rt>かく</rt></ruby>〜", "meaning_en": "Each, every", "meaning_zh": "各自", "is_target": True}
                    ]
                },
                {
                    "kanji": "感",
                    "onyomi": ["カン"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "感情", "reading": "かんじょう", "ruby_html": "<ruby>感情<rt>かんじょう</rt></ruby>", "meaning_en": "Feelings, emotion", "meaning_zh": "感情", "is_target": True},
                        {"term_ja": "感じる", "reading": "かんじる", "ruby_html": "<ruby>感<rt>かん</rt></ruby>じる", "meaning_en": "Feel, have sense of", "meaning_zh": "感觉", "is_target": True},
                        {"term_ja": "感心", "reading": "かんしん", "ruby_html": "<ruby>感心<rt>かんしん</rt></ruby>", "meaning_en": "Admire, be impressed", "meaning_zh": "佩服", "is_target": True},
                        {"term_ja": "感動", "reading": "かんどう", "ruby_html": "<ruby>感動<rt>かんどう</rt></ruby>", "meaning_en": "Be impressed, inspired", "meaning_zh": "感动", "is_target": True}
                    ]
                },
                {
                    "kanji": "記",
                    "onyomi": ["キ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "記事", "reading": "きじ", "ruby_html": "<ruby>記事<rt>きじ</rt></ruby>", "meaning_en": "Article, news story", "meaning_zh": "新闻报道", "is_target": True},
                        {"term_ja": "記者", "reading": "きしゃ", "ruby_html": "<ruby>記者<rt>きしゃ</rt></ruby>", "meaning_en": "Reporter", "meaning_zh": "记者", "is_target": True},
                        {"term_ja": "記入", "reading": "きにゅう", "ruby_html": "<ruby>記入<rt>きにゅう</rt></ruby>", "meaning_en": "Fill in, complete", "meaning_zh": "录入", "is_target": True},
                        {"term_ja": "日記", "reading": "にっき", "ruby_html": "<ruby>日記<rt>にっき</rt></ruby>", "meaning_en": "Diary", "meaning_zh": "日记", "is_target": False}
                    ]
                },
                {
                    "kanji": "期",
                    "onyomi": ["キ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "期間", "reading": "きかん", "ruby_html": "<ruby>期間<rt>きかん</rt></ruby>", "meaning_en": "Period", "meaning_zh": "期间", "is_target": True},
                        {"term_ja": "学期", "reading": "がっき", "ruby_html": "<ruby>学期<rt>がっき</rt></ruby>", "meaning_en": "Semester, term", "meaning_zh": "学期", "is_target": True},
                        {"term_ja": "時期", "reading": "じき", "ruby_html": "<ruby>時期<rt>じき</rt></ruby>", "meaning_en": "Period, time of year", "meaning_zh": "时期", "is_target": True}
                    ]
                },
                {
                    "kanji": "具",
                    "onyomi": ["グ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "具合", "reading": "ぐあい", "ruby_html": "<ruby>具合<rt>ぐあい</rt></ruby>", "meaning_en": "Condition, state of health", "meaning_zh": "情况", "is_target": False},
                        {"term_ja": "具体的な", "reading": "ぐたいてきな", "ruby_html": "<ruby>具体的<rt>ぐたいてき</rt></ruby>な", "meaning_en": "Concrete, specific", "meaning_zh": "具体的", "is_target": True},
                        {"term_ja": "家具", "reading": "かぐ", "ruby_html": "<ruby>家具<rt>かぐ</rt></ruby>", "meaning_en": "Furniture", "meaning_zh": "家具", "is_target": True},
                        {"term_ja": "道具", "reading": "どうぐ", "ruby_html": "<ruby>道具<rt>どうぐ</rt></ruby>", "meaning_en": "Tool, implement", "meaning_zh": "道具", "is_target": False}
                    ]
                },
                {
                    "kanji": "実",
                    "onyomi": ["ジツ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "実験", "reading": "じっけん", "ruby_html": "<ruby>実験<rt>じっけん</rt></ruby>", "meaning_en": "Experiment, do a test", "meaning_zh": "实验", "is_target": True},
                        {"term_ja": "実は", "reading": "じつは", "ruby_html": "<ruby>実<rt>じつ</rt></ruby>は", "meaning_en": "Actually, in fact", "meaning_zh": "实际上", "is_target": True},
                        {"term_ja": "実力", "reading": "じつりょく", "ruby_html": "<ruby>実力<rt>じつりょく</rt></ruby>", "meaning_en": "Ability, strength", "meaning_zh": "实际能力", "is_target": True},
                        {"term_ja": "事実", "reading": "じじつ", "ruby_html": "<ruby>事実<rt>じじつ</rt></ruby>", "meaning_en": "Fact", "meaning_zh": "事实", "is_target": True}
                    ]
                },
                {
                    "kanji": "女",
                    "onyomi": ["ジョ"],
                    "kunyomi": ["おんな"],
                    "words": [
                        {"term_ja": "女性", "reading": "じょせい", "ruby_html": "<ruby>女性<rt>じょせい</rt></ruby>", "meaning_en": "Female, woman", "meaning_zh": "女性", "is_target": False},
                        {"term_ja": "長女", "reading": "ちょうじょ", "ruby_html": "<ruby>長女<rt>ちょうじょ</rt></ruby>", "meaning_en": "Eldest or oldest daughter", "meaning_zh": "长女", "is_target": True}
                    ]
                },
                {
                    "kanji": "情",
                    "onyomi": ["ジョウ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "情報", "reading": "じょうほう", "ruby_html": "<ruby>情報<rt>じょうほう</rt></ruby>", "meaning_en": "Information", "meaning_zh": "信息", "is_target": True},
                        {"term_ja": "感情", "reading": "かんじょう", "ruby_html": "<ruby>感情<rt>かんじょう</rt></ruby>", "meaning_en": "Feelings, emotion", "meaning_zh": "感情", "is_target": True},
                        {"term_ja": "事情", "reading": "じじょう", "ruby_html": "<ruby>事情<rt>じじょう</rt></ruby>", "meaning_en": "Situation", "meaning_zh": "原因", "is_target": True},
                        {"term_ja": "友情", "reading": "ゆうじょう", "ruby_html": "<ruby>友情<rt>ゆうじょう</rt></ruby>", "meaning_en": "Friendship, fellowship", "meaning_zh": "友情", "is_target": True}
                    ]
                },
                {
                    "kanji": "信",
                    "onyomi": ["シン"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "信号", "reading": "しんごう", "ruby_html": "<ruby>信号<rt>しんごう</rt></ruby>", "meaning_en": "Signal", "meaning_zh": "红绿灯", "is_target": True},
                        {"term_ja": "信じる", "reading": "しんじる", "ruby_html": "<ruby>信<rt>しん</rt></ruby>じる", "meaning_en": "Believe", "meaning_zh": "相信", "is_target": True},
                        {"term_ja": "信用", "reading": "しんよう", "ruby_html": "<ruby>信用<rt>しんよう</rt></ruby>", "meaning_en": "Have faith, trust, confidence in", "meaning_zh": "相信", "is_target": True},
                        {"term_ja": "自信", "reading": "じしん", "ruby_html": "<ruby>自信<rt>じしん</rt></ruby>", "meaning_en": "Self-confidence", "meaning_zh": "自信", "is_target": True},
                        {"term_ja": "返信", "reading": "へんしん", "ruby_html": "<ruby>返信<rt>へんしん</rt></ruby>", "meaning_en": "Reply, respond", "meaning_zh": "回信", "is_target": True}
                    ]
                },
                {
                    "kanji": "性",
                    "onyomi": ["セイ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "性質", "reading": "せいしつ", "ruby_html": "<ruby>性質<rt>せいしつ</rt></ruby>", "meaning_en": "Nature, character", "meaning_zh": "性质", "is_target": True},
                        {"term_ja": "性別", "reading": "せいべつ", "ruby_html": "<ruby>性別<rt>せいべつ</rt></ruby>", "meaning_en": "Gender", "meaning_zh": "性别", "is_target": True},
                        {"term_ja": "女性", "reading": "じょせい", "ruby_html": "<ruby>女性<rt>じょせい</rt></ruby>", "meaning_en": "Female, woman", "meaning_zh": "女性", "is_target": False},
                        {"term_ja": "男性", "reading": "だんせい", "ruby_html": "<ruby>男性<rt>だんせい</rt></ruby>", "meaning_en": "Male, man", "meaning_zh": "男性", "is_target": False}
                    ]
                },
                {
                    "kanji": "製",
                    "onyomi": ["セイ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "〜製", "reading": "〜せい", "ruby_html": "〜<ruby>製<rt>せい</rt></ruby>", "meaning_en": "Made in, made of", "meaning_zh": "制作", "is_target": False},
                        {"term_ja": "製品", "reading": "せいひん", "ruby_html": "<ruby>製品<rt>せいひん</rt></ruby>", "meaning_en": "Product", "meaning_zh": "产品", "is_target": True}
                    ]
                },
                {
                    "kanji": "線",
                    "onyomi": ["セン"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "線", "reading": "せん", "ruby_html": "<ruby>線<rt>せん</rt></ruby>", "meaning_en": "Line", "meaning_zh": "线", "is_target": False},
                        {"term_ja": "下線", "reading": "かせん", "ruby_html": "<ruby>下線<rt>かせん</rt></ruby>", "meaning_en": "Underline", "meaning_zh": "下画线", "is_target": True},
                        {"term_ja": "電線", "reading": "でんせん", "ruby_html": "<ruby>電線<rt>でんせん</rt></ruby>", "meaning_en": "Electric wire", "meaning_zh": "电线", "is_target": True}
                    ]
                },
                {
                    "kanji": "第",
                    "onyomi": ["ダイ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "第〜", "reading": "だい〜", "ruby_html": "<ruby>第<rt>だい</rt></ruby>〜", "meaning_en": "Cardinal number marker (equivalent to -st, -nd, etc)", "meaning_zh": "第…", "is_target": True}
                    ]
                },
                {
                    "kanji": "男",
                    "onyomi": ["ダン"],
                    "kunyomi": ["おとこ"],
                    "words": [
                        {"term_ja": "男性", "reading": "だんせい", "ruby_html": "<ruby>男性<rt>だんせい</rt></ruby>", "meaning_en": "Male, man", "meaning_zh": "男性", "is_target": False}
                    ]
                },
                {
                    "kanji": "的",
                    "onyomi": ["テキ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "〜的", "reading": "〜てき", "ruby_html": "〜<ruby>的<rt>てき</rt></ruby>", "meaning_en": "Of (possessive particle), relating to", "meaning_zh": "…的", "is_target": True},
                        {"term_ja": "具体的(な)", "reading": "ぐたいてき(な)", "ruby_html": "<ruby>具体的<rt>ぐたいてき</rt></ruby>(な)", "meaning_en": "Concrete, specific", "meaning_zh": "具体的", "is_target": True}
                    ]
                },
                {
                    "kanji": "費",
                    "onyomi": ["ヒ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "費用", "reading": "ひよう", "ruby_html": "<ruby>費用<rt>ひよう</rt></ruby>", "meaning_en": "Cost, expense", "meaning_zh": "花费", "is_target": True},
                        {"term_ja": "会費", "reading": "かいひ", "ruby_html": "<ruby>会費<rt>かいひ</rt></ruby>", "meaning_en": "Membership fee", "meaning_zh": "会费", "is_target": True},
                        {"term_ja": "学費", "reading": "がくひ", "ruby_html": "<ruby>学費<rt>がくひ</rt></ruby>", "meaning_en": "Tuition fee", "meaning_zh": "学费", "is_target": True}
                    ]
                },
                {
                    "kanji": "副",
                    "onyomi": ["フク"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "副〜", "reading": "ふく〜", "ruby_html": "<ruby>副<rt>ふく</rt></ruby>〜", "meaning_en": "Vice-, deputy-", "meaning_zh": "副…", "is_target": True}
                    ]
                },
                {
                    "kanji": "報",
                    "onyomi": ["ホウ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "情報", "reading": "じょうほう", "ruby_html": "<ruby>情報<rt>じょうほう</rt></ruby>", "meaning_en": "Information", "meaning_zh": "信息", "is_target": True},
                        {"term_ja": "注意報", "reading": "ちゅういほう", "ruby_html": "<ruby>注意報<rt>ちゅういほう</rt></ruby>", "meaning_en": "Advisory, warning (disaster, etc.)", "meaning_zh": "(灾害等)警报", "is_target": True},
                        {"term_ja": "電報", "reading": "でんぽう", "ruby_html": "<ruby>電報<rt>でんぽう</rt></ruby>", "meaning_en": "Telegram", "meaning_zh": "电报", "is_target": False}
                    ]
                },
                {
                    "kanji": "友",
                    "onyomi": ["ユウ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "友情", "reading": "ゆうじょう", "ruby_html": "<ruby>友情<rt>ゆうじょう</rt></ruby>", "meaning_en": "Friendship, fellowship", "meaning_zh": "友情", "is_target": True},
                        {"term_ja": "友人", "reading": "ゆうじん", "ruby_html": "<ruby>友人<rt>ゆうじん</rt></ruby>", "meaning_en": "Friend", "meaning_zh": "朋友", "is_target": True},
                        {"term_ja": "親友", "reading": "しんゆう", "ruby_html": "<ruby>親友<rt>しんゆう</rt></ruby>", "meaning_en": "Best, closest friend", "meaning_zh": "挚友", "is_target": True}
                    ]
                },
                {
                    "kanji": "両",
                    "onyomi": ["リョウ"],
                    "kunyomi": [],
                    "words": [
                        {"term_ja": "両〜", "reading": "りょう〜", "ruby_html": "<ruby>両<rt>りょう</rt></ruby>〜", "meaning_en": "Both", "meaning_zh": "两…", "is_target": True},
                        {"term_ja": "両側", "reading": "りょうがわ", "ruby_html": "<ruby>両側<rt>りょうがわ</rt></ruby>", "meaning_en": "Both sides", "meaning_zh": "两侧", "is_target": True},
                        {"term_ja": "両親", "reading": "りょうしん", "ruby_html": "<ruby>両親<rt>りょうしん</rt></ruby>", "meaning_en": "Parents", "meaning_zh": "父母", "is_target": False},
                        {"term_ja": "両方", "reading": "りょうほう", "ruby_html": "<ruby>両方<rt>りょうほう</rt></ruby>", "meaning_en": "Both sides, both ways", "meaning_zh": "两边", "is_target": False}
                    ]
                },
                {
                    "kanji": "力",
                    "onyomi": ["リョク"],
                    "kunyomi": ["ちから"],
                    "words": [
                        {"term_ja": "学力", "reading": "がくりょく", "ruby_html": "<ruby>学力<rt>がくりょく</rt></ruby>", "meaning_en": "Academic ability", "meaning_zh": "学识能力", "is_target": True},
                        {"term_ja": "実力", "reading": "じつりょく", "ruby_html": "<ruby>実力<rt>じつりょく</rt></ruby>", "meaning_en": "Ability, strength", "meaning_zh": "实际能力", "is_target": True},
                        {"term_ja": "全力", "reading": "ぜんりょく", "ruby_html": "<ruby>全力<rt>ぜんりょく</rt></ruby>", "meaning_en": "Full force", "meaning_zh": "全力", "is_target": True},
                        {"term_ja": "体力", "reading": "たいりょく", "ruby_html": "<ruby>体力<rt>たいりょく</rt></ruby>", "meaning_en": "Physical fitness, bodily strength", "meaning_zh": "体力", "is_target": True}
                    ]
                }
            ]
        }
    ]
}

os.makedirs("nihongo-intermediate/data/kanji", exist_ok=True)
out_file = "nihongo-intermediate/data/kanji/part1_lessons_01_05.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_file} with {len(part1_data['lessons'])} lessons!")
