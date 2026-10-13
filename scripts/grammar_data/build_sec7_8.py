# -*- coding: utf-8 -*-
"""
Section 7 and Section 8 data for Shin Kanzen Master N3 Grammar.
Section 7: 第7課 〜だそうだ (Patterns 1-5, Drills 1-8)
Section 8: 第8課 絶対〜ない・必ず〜とは言えない (Patterns 1-5, Drills 1-8)
Combined Drills: 練習 7・8課 (Q1-10)
Review Test 2: まとめ問題 1〜8課 (Q1-13)
"""

def make_mc(qid, category, prompt, options, answer, exp_ja, exp_en):
    return {
        "question_id": qid,
        "category": category,
        "question_type": "multiple_choice",
        "prompt": prompt,
        "options": options,
        "correct_answer": answer,
        "explanation_ja": exp_ja,
        "explanation_en": exp_en
    }

def make_star(qid, category, prompt, options, order, star_pos, answer, full_sent, full_sent_en, exp_ja, exp_en):
    return {
        "question_id": qid,
        "category": category,
        "question_type": "star_arrangement",
        "prompt": prompt,
        "options": options,
        "correct_order": order,
        "star_position": star_pos,
        "correct_answer": answer,
        "full_sentence": full_sent,
        "full_sentence_en": full_sent_en,
        "explanation_ja": exp_ja,
        "explanation_en": exp_en
    }

# ==============================================================================
# SECTION 7: 第7課 〜だそうだ
# ==============================================================================
sec7_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜ということだ・〜とのことだ",
        "pattern_name_en": "I heard that / It is said that",
        "meaning_ja": "〜だそうだ。ほかの人から聞いたことを言うときに使う。少し改まった言い方。",
        "meaning_en": "I heard that... Used to report information heard from others. Somewhat formal expression.",
        "connection_forms": [
            "普通形 ＋ ということだ・とのことだ"
        ],
        "nuance_notes": "「〜によると・によれば」「〜の話では」などと一緒に使われることが多い。「とのことだ」は手紙やビジネス文書でよく使われる。",
        "example_sentences": [
            {
                "japanese": "<ruby>市<rt>し</rt></ruby>のお<ruby>知<rt>し</rt></ruby>らせによれば、この<ruby>道路<rt>どうろ</rt></ruby>は<ruby>来週<rt>らいしゅう</rt></ruby>から<ruby>工事<rt>こうじ</rt></ruby>が<ruby>始<rt>はじ</rt></ruby>まるということです。",
                "english": "According to the city notice, construction on this road is said to start next week."
            },
            {
                "japanese": "<ruby>店<rt>みせ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>では、この<ruby>地方<rt>ちほう</rt></ruby>の<ruby>米<rt>こめ</rt></ruby>はとてもおいしいということだ。",
                "english": "According to what the shopkeeper said, the rice from this region is delicious."
            },
            {
                "japanese": "さっき<ruby>川村<rt>かわむら</rt></ruby>さんから<ruby>電話<rt>でんわ</rt></ruby>がありました。<ruby>今日<rt>きょう</rt></ruby>は<ruby>社<rt>しゃ</rt></ruby>に<ruby>戻<rt>もど</rt></ruby>れないとのことです。",
                "english": "Kawamura called a moment ago. He said he won't be able to return to the office today."
            },
            {
                "japanese": "メールによると、<ruby>林<rt>はやし</rt></ruby>さんは<ruby>来週<rt>らいしゅう</rt></ruby>はとても<ruby>忙<rt>いそが</rt></ruby>しいとのことです。",
                "english": "According to the email, Hayashi said she will be very busy next week."
            },
            {
                "japanese": "【<ruby>手紙<rt>てがみ</rt></ruby>】<ruby>新<rt>あたら</rt></ruby>しい<ruby>仕事<rt>しごと</rt></ruby>が<ruby>決<rt>き</rt></ruby>まったとのこと、おめでとうございます。",
                "english": "[Letter] Congratulations on hearing that you've got a new job."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜と言われている",
        "pattern_name_en": "It is said that / People say that",
        "meaning_ja": "世の中で多くの人がそのように言っている。",
        "meaning_en": "It is generally said that... Used when conveying a commonly held opinion or general belief.",
        "connection_forms": [
            "普通形 ＋ と言われている"
        ],
        "nuance_notes": "特定の人ではなく、世間一般の人々がそう言っていることを表す。",
        "example_sentences": [
            {
                "japanese": "<ruby>今年<rt>ことし</rt></ruby>は<ruby>黒<rt>くろ</rt></ruby>い<ruby>服<rt>ふく</rt></ruby>が<ruby>流行<rt>りゅうこう</rt></ruby>すると<ruby>言<rt>い</rt></ruby>われている。",
                "english": "It is said that black clothes will be in fashion this year."
            },
            {
                "japanese": "<ruby>納豆<rt>なっとう</rt></ruby>は<ruby>体<rt>からだ</rt></ruby>にいいと<ruby>言<rt>い</rt></ruby>われている。",
                "english": "It is said that natto is good for health."
            },
            {
                "japanese": "<ruby>今度<rt>こんど</rt></ruby>の<ruby>大会<rt>たいかい</rt></ruby>では<ruby>中川<rt>なかがわ</rt></ruby><ruby>選手<rt>せんしゅ</rt></ruby>が<ruby>優勝<rt>ゆうしょう</rt></ruby>するだろうと<ruby>言<rt>い</rt></ruby>われています。",
                "english": "It is said that player Nakagawa will likely win the upcoming tournament."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜とか",
        "pattern_name_en": "I heard that... (rumor / casual)",
        "meaning_ja": "〜という話を聞いた。不確かな伝聞を表す。",
        "meaning_en": "I heard that... Used to casually pass on information or rumors that the speaker heard but is not completely sure of.",
        "connection_forms": [
            "普通形 ＋ とか"
        ],
        "nuance_notes": "間接的に聞いた噂や不確かな情報を伝える話し言葉。",
        "example_sentences": [
            {
                "japanese": "<ruby>来月<rt>らいげつ</rt></ruby>また<ruby>出張<rt>しゅっちょう</rt></ruby>だとか。<ruby>今度<rt>こんど</rt></ruby>はどちらに<ruby>行<rt>い</rt></ruby>かれるんですか。",
                "english": "I hear that you're going on another business trip next month. Where are you heading this time?"
            },
            {
                "japanese": "お<ruby>宅<rt>たく</rt></ruby>ではいろいろな<ruby>動物<rt>どうぶつ</rt></ruby>を<ruby>飼<rt>か</rt></ruby>っているとか。にぎやかでしょうね。",
                "english": "I heard you keep various animals at home. It must be lively."
            },
            {
                "japanese": "あの<ruby>店<rt>みせ</rt></ruby>のパンはとてもおいしいとか。<ruby>今日<rt>きょう</rt></ruby>、<ruby>帰<rt>かえ</rt></ruby>りに<ruby>買<rt>か</rt></ruby>って<ruby>帰<rt>かえ</rt></ruby>ります。",
                "english": "I heard that shop's bread is delicious. I'll buy some on my way home today."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜って",
        "pattern_name_en": "They say that / Casual hearsay or quote",
        "meaning_ja": "〜と言っていた、〜そうだ。親しい人との会話で使う。",
        "meaning_en": "They say that / Casual form of 〜そうだ or 〜と言っていた. Used in everyday conversational speech among close acquaintances.",
        "connection_forms": [
            "普通形 ＋ って"
        ],
        "nuance_notes": "「〜と言っていた」「〜そうだ」のくだけた口語表現。また「〜って」は「〜と」という引用にも使われる。",
        "example_sentences": [
            {
                "japanese": "<ruby>小川<rt>おがわ</rt></ruby>さん、<ruby>今日<rt>きょう</rt></ruby>は<ruby>休<rt>やす</rt></ruby>むって<ruby>言<rt>い</rt></ruby>ってたよ。",
                "english": "Ogawa said he's taking the day off today."
            },
            {
                "japanese": "<ruby>佐藤<rt>さとう</rt></ruby>さんの<ruby>奥<rt>おく</rt></ruby>さんは<ruby>料理<rt>りょうり</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>だって。",
                "english": "I heard Sato's wife is a cooking teacher."
            },
            {
                "japanese": "<ruby>駅前<rt>えきまえ</rt></ruby>にタイ<ruby>料理<rt>りょうり</rt></ruby>のレストランができたんだって。<ruby>行<rt>い</rt></ruby>ってみようよ。",
                "english": "I hear a Thai restaurant opened in front of the station. Let's go try it."
            },
            {
                "japanese": "<ruby>山川<rt>やまかわ</rt></ruby><ruby>君<rt>くん</rt></ruby>、<ruby>先生<rt>せんせい</rt></ruby>が<ruby>教員室<rt>きょういんしつ</rt></ruby>まで<ruby>来<rt>き</rt></ruby>てくださいって。",
                "english": "Yamakawa, the teacher said to come to the faculty room."
            }
        ]
    },
    {
        "pattern_number": 5,
        "pattern_name": "〜という",
        "pattern_name_en": "It is said that / According to reports",
        "meaning_ja": "〜だそうだ。本やニュースなど、文章でよく使われる硬い表現。",
        "meaning_en": "It is said that... Written, formal expression commonly found in reports, historical descriptions, and news.",
        "connection_forms": [
            "普通形 ＋ という"
        ],
        "nuance_notes": "書き言葉で伝聞・伝承を表す改まった表現。「〜だそうだ」の書き言葉に相当する。",
        "example_sentences": [
            {
                "japanese": "この<ruby>辺<rt>あた</rt></ruby>りは<ruby>昔<rt>むかし</rt></ruby>、<ruby>広<rt>ひろ</rt></ruby>い<ruby>野原<rt>のはら</rt></ruby>だったという。",
                "english": "It is said that this area was a vast open field in the old days."
            },
            {
                "japanese": "この<ruby>祭<rt>まつ</rt></ruby>りは<ruby>村<rt>むら</rt></ruby>で<ruby>古<rt>ふる</rt></ruby>くから<ruby>行<rt>おこな</rt></ruby>われてきたという。",
                "english": "It is said that this festival has been held in the village since ancient times."
            },
            {
                "japanese": "<ruby>豆腐<rt>とうふ</rt></ruby>は1300<ruby>年<rt>ねん</rt></ruby>ぐらい<ruby>前<rt>まえ</rt></ruby>に<ruby>中国<rt>ちゅうごく</rt></ruby>から<ruby>日本<rt>にほん</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>わったという。",
                "english": "It is said that tofu was brought from China to Japan about 1,300 years ago."
            }
        ]
    }
]

# Section 7 Drills (p.40)
sec7_drills = [
    make_mc("sec7_q1", "section_7_practice", "今朝の新聞によると、昨夜東京で大きな地震が（　）。", ["a あったということです", "b あるということです", "c あったことでした"], "a", "新聞による過去の事実の伝聞なので「あったということです」が正しい。", "According to this morning's newspaper, an earthquake 'occurred' last night, so past tense + ということです is correct."),
    make_mc("sec7_q2", "section_7_practice", "先輩からのメールでは、来週の土曜日は都合が（　）とのことです。", ["a 悪かった", "b 悪い", "c 悪いだろう"], "b", "来週の土曜日の予定について「都合が悪いとのことです」と述べるのが適切。", "Reporting future availability: 都合が悪いとのことです is correct."),
    make_mc("sec7_q3", "section_7_practice", "納豆は健康に（　）と言われている。", ["a いい", "b よいこと", "c よかった"], "a", "一般的に体に良いとされているので、現在形の「いいと言われている」が適切。", "General statement of health benefit: いいと言われている."),
    make_mc("sec7_q4", "section_7_practice", "あの映画はとても（　）とか。ぜひ見に行きたいですね。", ["a おもしろい", "b おもしろかった", "c おもしろいだろう"], "a", "評判を聞いた伝聞表現で「おもしろいとか」が自然。", "Casual hearsay about movie's reputation: おもしろいとか."),
    make_mc("sec7_q5", "section_7_practice", "木村さん、明日の飲み会には（　）って。", ["a 来られない", "b 来られないだろう", "c 来られなかった"], "a", "明日の飲み会に来られないという伝聞の引用で「来られないって」が正しい。", "Informal hearsay about tomorrow's event: 来られないって."),
    make_mc("sec7_q6", "section_7_practice", "田中さんの話では、新しい店は来月オープンする（　）。", ["a ということでした", "b ということです", "c とのことでした"], "b", "「〜の話では…ということです」という伝聞の定番表現。", "Hearsay reporting: ということです."),
    make_mc("sec7_q7", "section_7_practice", "緑茶にはビタミンCがたくさん含まれて（　）と言われている。", ["a いる", "b いた", "c いそう"], "a", "客観的な科学的事実・一般通念には現在形「いると言われている」を用いる。", "General knowledge: 含まれていると言われている."),
    make_mc("sec7_q8", "section_7_practice", "このお寺は800年前に（　）という。", ["a 建てられる", "b 建てている", "c 建てられた"], "c", "800年前の過去の出来事なので、受身の過去形「建てられたという」が適切。", "Historical hearsay: 建てられたという.")
]

# ==============================================================================
# SECTION 8: 第8課 絶対〜ない・必ず〜とは言えない
# ==============================================================================
sec8_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜はずがない・〜わけがない",
        "pattern_name_en": "Cannot be / Impossible that",
        "meaning_ja": "絶対に〜ない。話者が強い確信を持って否定する。",
        "meaning_en": "It is impossible that... / There is no way that... Speaker expresses strong certainty in negating something.",
        "connection_forms": [
            "普通形（ナ形だ-な・名だ-の） ＋ はずがない・わけがない"
        ],
        "nuance_notes": "話者の確信に基づく強い否定表現。「わけがない」のほうが「道理としてあり得ない」というニュアンスが強い。",
        "example_sentences": [
            {
                "japanese": "ちゃんと<ruby>鍵<rt>かぎ</rt></ruby>をかけたんだから、<ruby>泥棒<rt>どろぼう</rt></ruby>が<ruby>入<rt>はい</rt></ruby>れるはずがない。",
                "english": "Since I locked it properly, there's no way a thief could get in."
            },
            {
                "japanese": "あんなまじめな<ruby>人<rt>ひと</rt></ruby>が、<ruby>嘘<rt>うそ</rt></ruby>をつくわけがない。",
                "english": "There is no way that such a serious person would tell a lie."
            },
            {
                "japanese": "こんなに<ruby>簡単<rt>かんたん</rt></ruby>なテスト、<ruby>不合格<rt>ふごうかく</rt></ruby>になるはずがない。",
                "english": "It's impossible to fail such an easy test."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜とは限らない",
        "pattern_name_en": "Not necessarily / Not always",
        "meaning_ja": "いつも〜だとは言えない。例外もある（部分否定）。",
        "meaning_en": "It does not necessarily mean that... / Not always. Expresses partial negation, acknowledging exceptions.",
        "connection_forms": [
            "普通形（ナ形(だ)・名(だ)） ＋ とは限らない"
        ],
        "nuance_notes": "「必ずしも」「いつも」などの副詞と一緒に使われることが多い。",
        "example_sentences": [
            {
                "japanese": "<ruby>高<rt>たか</rt></ruby>いものが、<ruby>必<rt>かなら</rt></ruby>ずしもいいものだとは<ruby>限<rt>かぎ</rt></ruby>らない。",
                "english": "Expensive things are not necessarily good things."
            },
            {
                "japanese": "<ruby>日本人<rt>にほんじん</rt></ruby>だからといって、みんな<ruby>納豆<rt>なっとう</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだとは<ruby>限<rt>かぎ</rt></ruby>らない。",
                "english": "Just because someone is Japanese does not mean they necessarily like natto."
            },
            {
                "japanese": "<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>大学<rt>だいがく</rt></ruby>を<ruby>卒業<rt>そつぎょう</rt></ruby>したからといって、<ruby>成功<rt>せいこう</rt></ruby>するとは<ruby>限<rt>かぎ</rt></ruby>らない。",
                "english": "Graduating from a famous university does not guarantee success."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜わけではない・〜というわけではない・〜のではない",
        "pattern_name_en": "It doesn't mean that / It is not the case that",
        "meaning_ja": "すべてが〜だというのではない。全面的に肯定するわけではない。",
        "meaning_en": "It is not that... / It does not mean that... Partial negation softening an absolute statement.",
        "connection_forms": [
            "普通形（ナ形だ-な・名だ-の／な／である） ＋ わけではない",
            "普通形（ナ形(だ)・名(だ)） ＋ というわけではない",
            "普通形（ナ形だ-な・名だ-な） ＋ のではない"
        ],
        "nuance_notes": "相手の誤解を解いたり、完全な肯定を控えめに否定・弁解するときに用いる。",
        "example_sentences": [
            {
                "japanese": "<ruby>甘<rt>あま</rt></ruby>いものが<ruby>嫌<rt>きら</rt></ruby>いなわけではないが、あまり<ruby>食<rt>た</rt></ruby>べない。",
                "english": "It's not that I dislike sweets, but I don't eat them very often."
            },
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>の<ruby>言<rt>い</rt></ruby>うことがすべて<ruby>正<rt>ただ</rt></ruby>しいというわけではない。",
                "english": "It doesn't mean that everything he says is correct."
            },
            {
                "japanese": "<ruby>行<rt>い</rt></ruby>きたくないのではない。<ruby>時間<rt>じかん</rt></ruby>がないのだ。",
                "english": "It's not that I don't want to go. I just don't have the time."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜ないことはない",
        "pattern_name_en": "It's not that... not / Can if pushed",
        "meaning_ja": "少しは〜だ。条件によっては〜できる（二重否定による消極的肯定）。",
        "meaning_en": "It is not that... cannot / Could potentially... Double negation expressing reluctant or conditional affirmation.",
        "connection_forms": [
            "動ない形 ＋ ことはない",
            "イ形いくない ＋ ことはない",
            "ナ形でない ＋ ことはない"
        ],
        "nuance_notes": "「絶対に無理というわけではない」「やろうと思えばできる」という消極的な肯定を表す。",
        "example_sentences": [
            {
                "japanese": "<ruby>食<rt>た</rt></ruby>べられないことはないが、あまりおいしくない。",
                "english": "It's not that I can't eat it, but it isn't very tasty."
            },
            {
                "japanese": "<ruby>走<rt>はし</rt></ruby>れば<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わないこともないが、<ruby>急<rt>いそ</rt></ruby>ごう。",
                "english": "If we run, it's not impossible to make it in time, so let's hurry."
            },
            {
                "japanese": "お<ruby>酒<rt>さけ</rt></ruby>は<ruby>飲<rt>の</rt></ruby>めないことはないが、<ruby>弱<rt>よわ</rt></ruby>いので<ruby>一杯<rt>いっぱい</rt></ruby>だけにする。",
                "english": "It's not that I can't drink alcohol, but I have low tolerance so I'll stick to one glass."
            }
        ]
    },
    {
        "pattern_number": 5,
        "pattern_name": "〜ことは〜が、…",
        "pattern_name_en": "It is true that... but...",
        "meaning_ja": "たしかに〜だが、しかし…。",
        "meaning_en": "It is indeed true that... but... Acknowledges a fact first, then adds a qualification or contrast.",
        "connection_forms": [
            "動・形・名の辞書形 ＋ ことは ＋ 同一の動・形・名 ＋ が／けれど"
        ],
        "nuance_notes": "同じ語を繰り返して「一応その事実は認めるが、十分ではない／問題がある」と続ける構文。",
        "example_sentences": [
            {
                "japanese": "この<ruby>本<rt>ほん</rt></ruby>は<ruby>読<rt>よ</rt></ruby>んだことは<ruby>読<rt>よ</rt></ruby>んだが、あまりよく<ruby>覚<rt>おぼ</rt></ruby>えていない。",
                "english": "I did read this book, but I don't remember it very well."
            },
            {
                "japanese": "おいしいことはおいしいが、ちょっと<ruby>高<rt>たか</rt></ruby>すぎる。",
                "english": "It is indeed delicious, but it's a bit too expensive."
            },
            {
                "japanese": "パソコンを<ruby>使<rt>つか</rt></ruby>えることは<ruby>使<rt>つか</rt></ruby>えるが、メールとネットくらいしかできない。",
                "english": "I can use a computer, but I can only do basic things like email and browsing."
            }
        ]
    }
]

# Section 8 Drills (p.40)
sec8_drills = [
    make_mc("sec8_q1", "section_8_practice", "あんなに一生懸命練習したのだから、負ける（　）。", ["a はずがない", "b はずだ", "c わけだ"], "a", "根拠に基づく強い否定「負けるはずがない」が適切。", "Strong logical negation: 負けるはずがない."),
    make_mc("sec8_q2", "section_8_practice", "お金持ちが必ずしも幸せ（　）。", ["a だ", "b なはずだ", "c だとは限らない"], "c", "「必ずしも〜とは限らない」の部分否定表現。", "Partial negation paired with 必ずしも: だとは限らない."),
    make_mc("sec8_q3", "section_8_practice", "日本料理が好きではない（　）が、刺身は苦手だ。", ["a わけではない", "b はずではない", "c のではない"], "a", "部分否定「好きではないわけではない」が適切。", "Partial negation: わけではない."),
    make_mc("sec8_q4", "section_8_practice", "頼まれれば、手伝わない（　）が、できれば一人でやってほしい。", ["a わけではない", "b ことはない", "c はずがない"], "b", "消極的肯定「手伝わないことはない」（手伝えないこともない）の用法。", "Double negative showing reluctant willingness: ことはない."),
    make_mc("sec8_q5", "section_8_practice", "高いことは（　）が、とても便利な道具だ。", ["a 高くない", "b 高いだろう", "c 高い"], "c", "反復構文「高いことは高いが」が正しい。", "Repetition pattern: 高いことは高いが."),
    make_mc("sec8_q6", "section_8_practice", "あんなに親切な彼が、そんな意地悪をする（　）。", ["a わけだ", "b はずだ", "c わけがない"], "c", "「意地悪をするわけがない」という強い否定。", "Strong negation: わけがない."),
    make_mc("sec8_q7", "section_8_practice", "英語が話せるからといって、通訳ができる（　）。", ["a とは限らない", "b わけだ", "c はずだ"], "a", "「〜からといって…とは限らない」の呼応。", "Partial negation with からといって: とは限らない."),
    make_mc("sec8_q8", "section_8_practice", "車を運転できない（　）が、あまり得意ではない。", ["a わけだ", "b はずだ", "c ことはない"], "c", "「運転できないことはない」という消極的肯定。", "Double negative: ことはない.")
]

# Combined Drills: 練習 7・8課 (p.41)
sec7_8_combined_drills = [
    make_mc("sec7_8_q1", "section_7_8_combined", "天気予報によると、午後から雨が（　）。", ["a 降るだろう", "b 降るそうだ", "c 降るとか"], "b", "天気予報による確実な伝聞の結びには「降るそうだ」が適切。", "Weather forecast hearsay: 降るそうだ."),
    make_mc("sec7_8_q2", "section_7_8_combined", "彼女はフランスへ留学する（　）と言っていた。", ["a 予定だ", "b 予定な", "c 予定の"], "a", "普通形＋と言っていたなので「予定だ」が適切。", "Quotation connection: 予定だと言っていた."),
    make_mc("sec7_8_q3", "section_7_8_combined", "先生の話では、試験はそれほど（　）ということです。", ["a 難しくない", "b 難しいだろう", "c 難しくなかった"], "a", "試験の難易度についての伝聞で「難しくないということです」が自然。", "Hearsay: 難しくないということです."),
    make_mc("sec7_8_q4", "section_7_8_combined", "努力したからといって、必ずしも成功する（　）。", ["a わけだ", "b とは限らない", "c はずがない"], "b", "「必ずしも〜とは限らない」の部分否定。", "Partial negation: とは限らない."),
    make_mc("sec7_8_q5", "section_7_8_combined", "あんなに練習したんだから、失敗する（　）。", ["a はずだ", "b わけだ", "c はずがない"], "c", "強い確信に基づく否定「失敗するはずがない」。", "Strong certainty negation: はずがない."),
    make_mc("sec7_8_q6", "section_7_8_combined", "辛いものが食べられない（　）が、あまり得意ではない。", ["a ことはない", "b わけだ", "c はずだ"], "a", "消極的肯定「食べられないことはない」。", "Reluctant admission: 食べられないことはない."),
    make_mc("sec7_8_q7", "section_7_8_combined", "行くことは（　）が、あまり乗り気ではない。", ["a 行った", "b 行く", "c 行かない"], "b", "同一動詞の繰り返し「行くことは行くが」。", "Repetition pattern: 行くことは行くが."),
    make_mc("sec7_8_q8", "section_7_8_combined", "あの二人が結婚する（　）を聞いてびっくりした。", ["a 噂", "b という話", "c とか"], "b", "名詞修飾節としての「〜という話」。", "Noun phrase: という話."),
    make_mc("sec7_8_q9", "section_7_8_combined", "彼が犯人の（　）。その時間は私と一緒にいたのだから。", ["a はずがない", "b はずだ", "c わけだ"], "a", "アリバイがあるため「犯人のはずがない」。", "Logical impossibility: はずがない."),
    make_mc("sec7_8_q10", "section_7_8_combined", "高いものが（　）良いものだとは限らない。", ["a 必ずしも", "b ぜったい", "c どうしても"], "a", "「〜とは限らない」と呼応する副詞は「必ずしも」。", "Paired adverb for partial negation: 必ずしも.")
]

# Review Test 2: まとめ問題 1〜8課 (p.42-43)
matome_1_to_8_drills = [
    make_mc("matome_1_8_q1", "review_test_1_to_8", "あのまじめな山田さんが、約束を破る（　）。", ["1 はずだ", "2 わけだ", "3 つもりだ", "4 わけがない"], "4", "人柄に基づいた強い否定「破るわけがない」が正しい。", "Strong negation: わけがない."),
    make_mc("matome_1_8_q2", "review_test_1_to_8", "勉強すれば合格できる（　）が、もっと努力が必要だ。", ["1 わけではない", "2 ことはない", "3 はずがない", "4 とは限らない"], "2", "消極的肯定「合格できることはない（合格できないこともない）」文脈。", "Double negative / potential: ことはない."),
    make_mc("matome_1_8_q3", "review_test_1_to_8", "天気予報によれば、明日は全国的に（　）ということです。", ["1 晴れだ", "2 晴れの", "3 晴れ", "4 晴れな"], "3", "名詞＋ということです。名詞に直接「ということです」が接続する。", "Hearsay connection with noun: 晴れということです."),
    make_mc("matome_1_8_q4", "review_test_1_to_8", "いくら安くても、必要のないものは（　）べきではない。", ["1 買う", "2 買う", "3 買わない", "4 買おう"], "2", "動詞辞書形＋べきではない。「買うべきではない」が正しい。", "Connection to べきではない: 辞書形 + べきではない -> 買うべきではない."),
    make_mc("matome_1_8_q5", "review_test_1_to_8", "便利である反面、使い方を誤ると（　）危険もある。", ["1 便利な", "2 便利だ", "3 大きな", "4 大きい"], "3", "「〜反面、大きな危険もある」という対比文脈言及。", "Contrast clause: 大きな危険."),
    make_mc("matome_1_8_q6", "review_test_1_to_8", "日本に来た（　）、ぜひ富士山に登ってみたい。", ["1 からには", "2 ためには", "3 ように", "4 のに"], "1", "「〜からには」は強い決意・希望を表す接続。", "Since / Now that: からには."),
    make_mc("matome_1_8_q7", "review_test_1_to_8", "熱が下がらないなら、病院へ（　）ほうがいい。", ["1 行く", "2 行かない", "3 行った", "4 行こう"], "3", "助言の定番表現「〜たほうがいい」。「行ったほうがいい」が正しい。", "Advice: 〜たほうがいい -> 行ったほうがいい."),
    make_mc("matome_1_8_q8", "review_test_1_to_8", "この薬を（　）うちに、痛みが治まってきた。", ["1 飲んだ", "2 飲んでいる", "3 飲む", "4 飲まない"], "2", "進行中の状態「飲んでいるうちに」。", "While / during: 飲んでいるうちに."),
    make_mc("matome_1_8_q9", "review_test_1_to_8", "彼が来ない（　）を先生に伝えておいた。", ["1 わけ", "2 はず", "3 つもり", "4 こと"], "4", "事態の名詞化「来ないこと」。", "Nominalization: 来ないこと."),
    make_mc("matome_1_8_q10", "review_test_1_to_8", "会議の（　）携帯電話の電源をお切りください。", ["1 あいだ", "2 あいだは", "3 うちに", "4 とき"], "2", "継続期間中の規則「会議の間は」。", "During the continuous period: 間は."),
    make_mc("matome_1_8_q11", "review_test_1_to_8", "雨が（　）うちに、洗濯物を取り込みましょう。", ["1 降らない", "2 降る", "3 降った", "4 降っている"], "1", "状態が変化する前に「降らないうちに」。", "Before condition changes: 降らないうちに."),
    make_mc("matome_1_8_q12", "review_test_1_to_8", "彼は忙しいと言っていたが、来られない（　）。", ["1 はずだ", "2 わけだ", "3 つもりだ", "4 わけではない"], "4", "部分否定「来られないわけではない」。", "Partial negation: 来られないわけではない."),
    make_mc("matome_1_8_q13", "review_test_1_to_8", "新しい技術の（　）生活が便利になった。", ["1 おかげで", "2 せいで", "3 ために", "4 から"], "1", "良い結果の理由を表す「おかげで」。", "Thanks to (positive reason): おかげで.")
]
