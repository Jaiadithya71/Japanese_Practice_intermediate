# Script to generate nihongo-intermediate/data/kanji/kanji_mock_tests.json
import json
import os

mock_tests_data = {
    "metadata": {
        "title": "新完全マスター 漢字 N3 - 実力テスト (第1回・第2回)",
        "part": "mock_tests",
        "exam_count": 2,
        "description": "Kanji mock tests transcribed from Shin Kanzen Master Kanji N3 (実力テスト 1 & 2, pp. 104-107), covering JLPT N3 Kanji Question 1 (Reading) and Question 2 (Kanji Selection).",
        "version": "1.0.0"
    },
    "chapters": [
        {
            "metadata": {
                "chapter": "kanji_mock01",
                "type": "mock_exam",
                "topic_ja": "実力テスト 1",
                "topic_en": "Mock Test 1",
                "pages": [104, 105]
            },
            "sections": [],
            "exercises": [
                {
                    "exercise_id": "kanji_mock01-mondai1",
                    "title_ja": "問題 1 ___のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
                    "title_en": "Question 1: Choose the best reading (1, 2, 3, or 4) for the underlined word.",
                    "type": "multiple_choice",
                    "items": [
                        {
                            "item_id": 1,
                            "question_ja": "父の<u>手術</u>は、無事に終わった。",
                            "target_word": "手術",
                            "options": [
                                "1 しゅじゅつ",
                                "2 しじゅつ",
                                "3 しゅうずっ",
                                "4 しゅずっと"
                            ],
                            "answer": "1",
                            "explanation": "「手術」の正しい読み方は「しゅじゅつ」です。「手（しゅ）」＋「術（じゅつ）」と読みます。"
                        },
                        {
                            "item_id": 2,
                            "question_ja": "病気の<u>予防</u>には、規則正しい生活が大切だ。",
                            "target_word": "予防",
                            "options": [
                                "1 ようほ",
                                "2 よほう",
                                "3 ようぼう",
                                "4 よぼう"
                            ],
                            "answer": "4",
                            "explanation": "「予防」の正しい読み方は「よぼう」です。「予（よ）」＋「防（ぼう）」と読みます。「予」は短音です。"
                        },
                        {
                            "item_id": 3,
                            "question_ja": "<u>震度</u>が５だと、棚から物が落ちることもある。",
                            "target_word": "震度",
                            "options": [
                                "1 じんど",
                                "2 しんど",
                                "3 しんどう",
                                "4 しんとう"
                            ],
                            "answer": "2",
                            "explanation": "「震度」の正しい読み方は「しんど」です。「震（しん）」＋「度（ど）」と読みます。"
                        },
                        {
                            "item_id": 4,
                            "question_ja": "友達に映画の<u>感想</u>を聞かれた。",
                            "target_word": "感想",
                            "options": [
                                "1 かんぞ",
                                "2 かんしょう",
                                "3 かんじょう",
                                "4 かんそう"
                            ],
                            "answer": "4",
                            "explanation": "「感想」の正しい読み方は「かんそう」です。「感（かん）」＋「想（そう）」と読みます。"
                        },
                        {
                            "item_id": 5,
                            "question_ja": "布団を<u>押し入れ</u>にしまってください。",
                            "target_word": "押し入れ",
                            "options": [
                                "1 おしいれ",
                                "2 こしいれ",
                                "3 おしはいれ",
                                "4 こしはいれ"
                            ],
                            "answer": "1",
                            "explanation": "「押し入れ」の正しい読み方は「おしいれ」です。「押（お）す」＋「入（い）れ」の複合語です。"
                        },
                        {
                            "item_id": 6,
                            "question_ja": "ドアがバタンと<u>閉まる</u>音がした。",
                            "target_word": "閉まる",
                            "options": [
                                "1 とじまる",
                                "2 しめまる",
                                "3 しまる",
                                "4 こじまる"
                            ],
                            "answer": "3",
                            "explanation": "「閉まる」の正しい読み方は「しまる」です（自動詞）。他動詞は「閉める（しめる）」です。"
                        },
                        {
                            "item_id": 7,
                            "question_ja": "ケーキを作るときは、砂糖を<u>正確に</u>量ってください。",
                            "target_word": "正確に",
                            "options": [
                                "1 しょがくに",
                                "2 せいがくに",
                                "3 しょうかくに",
                                "4 せいかくに"
                            ],
                            "answer": "4",
                            "explanation": "「正確に」の正しい読み方は「せいかくに」です。「正（せい）」＋「確（かく）」と読みます。"
                        },
                        {
                            "item_id": 8,
                            "question_ja": "よし子さんは、<u>笑顔</u>がすてきですね。",
                            "target_word": "笑顔",
                            "options": [
                                "1 いがお",
                                "2 わらかお",
                                "3 にこがお",
                                "4 えがお"
                            ],
                            "answer": "4",
                            "explanation": "「笑顔」の正しい読み方は「えがお」です。「笑（え）」＋「顔（かお→がお：連濁）」と読みます。"
                        }
                    ]
                },
                {
                    "exercise_id": "kanji_mock01-mondai2",
                    "title_ja": "問題 2 ___のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
                    "title_en": "Question 2: Choose the best kanji (1, 2, 3, or 4) for the underlined word.",
                    "type": "multiple_choice",
                    "items": [
                        {
                            "item_id": 1,
                            "question_ja": "その村には<u>しょうてん</u>が一つあるだけだった。",
                            "target_word": "しょうてん",
                            "options": [
                                "1 商店",
                                "2 帝店",
                                "3 商点",
                                "4 帝点"
                            ],
                            "answer": "1",
                            "explanation": "「しょうてん（店・商店）」の漢字は「商店」です。"
                        },
                        {
                            "item_id": 2,
                            "question_ja": "米を<u>しょうひ</u>する量は、毎年減っている。",
                            "target_word": "しょうひ",
                            "options": [
                                "1 肖貨",
                                "2 消費",
                                "3 消資",
                                "4 肖費"
                            ],
                            "answer": "2",
                            "explanation": "「しょうひ（使うこと・消費）」の漢字は「消費」です。「消（き・しょう）」＋「費（ひ）」。"
                        },
                        {
                            "item_id": 3,
                            "question_ja": "たくさん<u>たんご</u>を知っていれば、いろいろなことが話せる。",
                            "target_word": "たんご",
                            "options": [
                                "1 果語",
                                "2 果詩",
                                "3 単語",
                                "4 単詩"
                            ],
                            "answer": "3",
                            "explanation": "「たんご（言葉・単語）」の漢字は「単語」です。「単（たん）」＋「語（ご）」。"
                        },
                        {
                            "item_id": 4,
                            "question_ja": "明日<u>たたかう</u>相手は、とても強いチームだ。",
                            "target_word": "たたかう",
                            "options": [
                                "1 戒う",
                                "2 戦う",
                                "3 敵う",
                                "4 争う"
                            ],
                            "answer": "2",
                            "explanation": "「たたかう」の漢字は「戦う」です（試合・勝負など）。"
                        },
                        {
                            "item_id": 5,
                            "question_ja": "夏は、<u>くさ</u>が伸びるのが速い。",
                            "target_word": "くさ",
                            "options": [
                                "1 芽",
                                "2 芋",
                                "3 草",
                                "4 苗"
                            ],
                            "answer": "3",
                            "explanation": "「くさ」の漢字は「草」です。「芽」はめ、「芋」はいも、「苗」はなえ。"
                        },
                        {
                            "item_id": 6,
                            "question_ja": "小学生は、<u>きいろい</u>帽子をかぶっていた。",
                            "target_word": "きいろい",
                            "options": [
                                "1 華色い",
                                "2 横色い",
                                "3 昔色い",
                                "4 黄色い"
                            ],
                            "answer": "4",
                            "explanation": "「きいろい」の漢字は「黄色い」です。「黄（き・こう・おう）」です。"
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "chapter": "kanji_mock02",
                "type": "mock_exam",
                "topic_ja": "実力テスト 2",
                "topic_en": "Mock Test 2",
                "pages": [106, 107]
            },
            "sections": [],
            "exercises": [
                {
                    "exercise_id": "kanji_mock02-mondai1",
                    "title_ja": "問題 1 ___のことばの読み方として最もよいものを、1・2・3・4から一つえらびなさい。",
                    "title_en": "Question 1: Choose the best reading (1, 2, 3, or 4) for the underlined word.",
                    "type": "multiple_choice",
                    "items": [
                        {
                            "item_id": 1,
                            "question_ja": "この携帯電話は、山の上でも電波が<u>受信</u>できますか。",
                            "target_word": "受信",
                            "options": [
                                "1 しゅじん",
                                "2 じゅしん",
                                "3 じゅうじん",
                                "4 しゅうじん"
                            ],
                            "answer": "2",
                            "explanation": "「受信」の正しい読み方は「じゅしん」です。「受（じゅ）」＋「信（しん）」と読みます。"
                        },
                        {
                            "item_id": 2,
                            "question_ja": "この食品は<u>保存</u>ができない。",
                            "target_word": "保存",
                            "options": [
                                "1 ほぞん",
                                "2 ほうぞん",
                                "3 ほそん",
                                "4 ほうそん"
                            ],
                            "answer": "1",
                            "explanation": "「保存」の正しい読み方は「ほぞん」です。「保（ほ）」＋「存（ぞん）」と読みます。「保」は短音です。"
                        },
                        {
                            "item_id": 3,
                            "question_ja": "出発の<u>当日</u>は、空港にみんなが見送りに来てくれた。",
                            "target_word": "当日",
                            "options": [
                                "1 とうにち",
                                "2 とうじつ",
                                "3 とっじつ",
                                "4 とんにち"
                            ],
                            "answer": "2",
                            "explanation": "「当日」の正しい読み方は「とうじつ」です。「当（とう）」＋「日（じつ）」と読みます。"
                        },
                        {
                            "item_id": 4,
                            "question_ja": "出張と<u>重なって</u>、子供の運動会を見に行けなかった。",
                            "target_word": "重なって",
                            "options": [
                                "1 うなって",
                                "2 おもなって",
                                "3 かなって",
                                "4 かさなって"
                            ],
                            "answer": "4",
                            "explanation": "「重なって」の正しい読み方は「かさなって」です。動詞「重なる（かさなる）」のテ形です。"
                        },
                        {
                            "item_id": 5,
                            "question_ja": "みんなで食べたので、お菓子の袋はすぐ<u>空</u>になった。",
                            "target_word": "空",
                            "options": [
                                "1 から",
                                "2 そら",
                                "3 あき",
                                "4 くう"
                            ],
                            "answer": "1",
                            "explanation": "中身がないことを表す「空」の読み方は「から」です（「空になる」）。"
                        },
                        {
                            "item_id": 6,
                            "question_ja": "この料理は、<u>冷める</u>とおいしくない。",
                            "target_word": "冷める",
                            "options": [
                                "1 やめる",
                                "2 つめためる",
                                "3 さめる",
                                "4 ひえめる"
                            ],
                            "answer": "3",
                            "explanation": "熱いものが冷たくなることを表す「冷める」の読み方は「さめる」です（自動詞）。"
                        },
                        {
                            "item_id": 7,
                            "question_ja": "子供は、<u>虫歯</u>が痛いと言って、朝から泣いている。",
                            "target_word": "虫歯",
                            "options": [
                                "1 むしは",
                                "2 むしば",
                                "3 ぶしは",
                                "4 ぶしば"
                            ],
                            "answer": "2",
                            "explanation": "「虫歯」の正しい読み方は「むしば」です。「虫（むし）」＋「歯（は→ば：連濁）」と読みます。"
                        },
                        {
                            "item_id": 8,
                            "question_ja": "寒さで、女の子は顔が<u>真っ青</u>だった。",
                            "target_word": "真っ青",
                            "options": [
                                "1 まあっかお",
                                "2 まっあお",
                                "3 まあっあお",
                                "4 まっさお"
                            ],
                            "answer": "4",
                            "explanation": "「真っ青」の正しい読み方は「まっさお」です。「真（まっ）」＋「青（さお：促音＋音変化）」となります。"
                        }
                    ]
                },
                {
                    "exercise_id": "kanji_mock02-mondai2",
                    "title_ja": "問題 2 ___のことばを漢字で書くとき、最もよいものを、1・2・3・4から一つえらびなさい。",
                    "title_en": "Question 2: Choose the best kanji (1, 2, 3, or 4) for the underlined word.",
                    "type": "multiple_choice",
                    "items": [
                        {
                            "item_id": 1,
                            "question_ja": "この工場では、船を<u>せいぞう</u>している。",
                            "target_word": "せいぞう",
                            "options": [
                                "1 制造",
                                "2 製造",
                                "3 制追",
                                "4 製追"
                            ],
                            "answer": "2",
                            "explanation": "「せいぞう（製品を作ること・製造）」の漢字は「製造」です。「製（せい）」＋「造（ぞう）」。"
                        },
                        {
                            "item_id": 2,
                            "question_ja": "このバスの<u>ていいん</u>は60名です。",
                            "target_word": "ていいん",
                            "options": [
                                "1 停員",
                                "2 停人",
                                "3 定員",
                                "4 定人"
                            ],
                            "answer": "3",
                            "explanation": "「ていいん（規定の人員・定員）」の漢字は「定員」です。「定（てい）」＋「員（いん）」。"
                        },
                        {
                            "item_id": 3,
                            "question_ja": "本のもくじをよく見て、どこから読むか考える。",
                            "target_word": "もくじ",
                            "options": [
                                "1 目辞",
                                "2 目字",
                                "3 目録",
                                "4 目次"
                            ],
                            "answer": "4",
                            "explanation": "「もくじ（目次・目録順）」の漢字は「目次」です。「目（もく）」＋「次（じ）」。"
                        },
                        {
                            "item_id": 4,
                            "question_ja": "あの人は、何を考えているか分からないので、<u>つきあい</u>にくい。",
                            "target_word": "つきあい",
                            "options": [
                                "1 着合いにくい",
                                "2 付き合いにくい",
                                "3 着き会いにくい",
                                "4 付き会いにくい"
                            ],
                            "answer": "2",
                            "explanation": "「つきあい（人と交際すること・付き合い）」の漢字は「付き合い」です。「付（つ）く」＋「合（あ）う」。"
                        },
                        {
                            "item_id": 5,
                            "question_ja": "新しいアパートは狭いですが、<u>ひあたり</u>はとてもいいです。",
                            "target_word": "ひあたり",
                            "options": [
                                "1 火向たり",
                                "2 日向たり",
                                "3 火当たり",
                                "4 日当たり"
                            ],
                            "answer": "4",
                            "explanation": "「ひあたり（日光が当たること・日当たり）」の漢字は「日当たり」です。「日（ひ）」＋「当（あ）たり」。"
                        },
                        {
                            "item_id": 6,
                            "question_ja": "植物の<u>ね</u>には、土から水や栄養を取るという重要な役目があります。",
                            "target_word": "ね",
                            "options": [
                                "1 根",
                                "2 恨",
                                "3 株",
                                "4 葉"
                            ],
                            "answer": "1",
                            "explanation": "「ね（根っこ・根）」の漢字は「根」です。「恨」はうらみ、「株」はかぶ、「葉」はは。"
                        }
                    ]
                }
            ]
        }
    ]
}

target_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'kanji', 'kanji_mock_tests.json')
target_file = os.path.normpath(target_file)

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(mock_tests_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_file}")
