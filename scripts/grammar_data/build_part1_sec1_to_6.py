"""
Script to build nihongo-intermediate/data/grammar/part1_sec1_to_6.json
Transcribes Images 019 - 039:
- Part 1: 文の文法 1 (Sentence Grammar 1)
- Section 1 (1課: 〜とき) Patterns 1-4
- Section 2 (2課: 〜関係して) Patterns 1-5
- Practice Drills for 1課, 2課, and 1課・2課
- Section 3 (3課: 比べれば…・〜がいちばん) Patterns 1-4
- Section 4 (4課: 〜とは違って) Patterns 1-5
- Practice Drills for 3課, 4課, and 3課・4課
- まとめ問題 1〜4課 (Review Test 1, Questions 1-13)
- Section 5 (5課: 〜だから) Patterns 1-5
- Section 6 (6課: もし、…) Patterns 1-5
- Practice Drills for 5課, 6課, and 5課・6課
"""

import json
from pathlib import Path

# Helper function to create drill questions
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
# SECTION 1 (1課 〜とき)
# ==============================================================================
sec1_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜うちに",
        "pattern_name_en": "while / before / during",
        "meaning_ja": "1: その状態が変わる前に、あることをする。2: 〜している間に（変化する）。",
        "meaning_en": "1: Do something before the current situation changes. 2: While doing X, a change occurs spontaneously.",
        "connection_forms": [
            "V-辞書形 / V-ない形 / V-ている + うちに",
            "A-い + うちに",
            "Na-な + うちに",
            "N-の + うちに"
        ],
        "nuance_notes": "1の後ろには意志動詞（〜する、〜しようなど）が来る。2の後ろには無意志の変化を表す動詞（〜になる、変わるなど）が来る。",
        "example_sentences": [
            {
                "japanese": "<ruby>冷<rt>つめ</rt></ruby>たいうちに、どうぞお<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がりください。",
                "english": "Please eat it while it's still cold."
            },
            {
                "japanese": "<ruby>明<rt>あか</rt></ruby>るいうちに、<ruby>庭<rt>にわ</rt></ruby>の<ruby>草取<rt>くさと</rt></ruby>りをやってしまおう。",
                "english": "Let's finish weeding the garden while it's still light outside."
            },
            {
                "japanese": "<ruby>若<rt>わか</rt></ruby>いうちに、いろいろな<ruby>経験<rt>けいけん</rt></ruby>をしておいたほうがいい。",
                "english": "You should gain various experiences while you are still young."
            },
            {
                "japanese": "<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いているうちに、<ruby>眠<rt>ねむ</rt></ruby>ってしまった。",
                "english": "While listening to music, I fell asleep."
            },
            {
                "japanese": "<ruby>何<rt>なん</rt></ruby><ruby>度<rt>ど</rt></ruby>も<ruby>会<rt>あ</rt></ruby>っているうちに、だんだん<ruby>親<rt>した</rt></ruby>しくなってきた。",
                "english": "As we met repeatedly, we gradually grew closer."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜あいだ・〜あいだに",
        "pattern_name_en": "while / during",
        "meaning_ja": "〜あいだ：その状態が続いている間ずっと。〜あいだに：その期間のある時点に。",
        "meaning_en": "〜あいだ: throughout the entire duration of a continuous state/action. 〜あいだに: at some point in time during that duration.",
        "connection_forms": [
            "V-辞書形 / V-ている / V-ない + あいだ（に）",
            "Na-な + あいだ（に）",
            "N-の + あいだ（に）"
        ],
        "nuance_notes": "「〜あいだ」の後ろは継続動詞。「〜あいだに」の後ろは瞬間動詞や一回限りの行為が来る。",
        "example_sentences": [
            {
                "japanese": "<ruby>夏休<rt>なつやす</rt></ruby>みのあいだ、ずっと<ruby>国<rt>くに</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>っていました。",
                "english": "During the entire summer vacation, I was back in my home country."
            },
            {
                "japanese": "<ruby>留守<rt>るす</rt></ruby>のあいだに、<ruby>泥棒<rt>どろぼう</rt></ruby>が<ruby>入<rt>はい</rt></ruby>ったようだ。",
                "english": "It seems a burglar broke in while I was away."
            },
            {
                "japanese": "<ruby>子供<rt>こども</rt></ruby>が<ruby>寝<rt>ね</rt></ruby>ているあいだに、<ruby>夕飯<rt>ゆうはん</rt></ruby>の<ruby>支度<rt>したく</rt></ruby>をしてしまおう。",
                "english": "Let's get dinner ready while the kids are sleeping."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜てからでないと・〜てからでなければ",
        "pattern_name_en": "unless / until (doing X first)",
        "meaning_ja": "〜した後でなければ、あとのことができない・難しい。",
        "meaning_en": "Unless X is done first, Y cannot be done or is impossible.",
        "connection_forms": [
            "V-て形 + からでないと / からでなければ"
        ],
        "nuance_notes": "後ろには必ず否定文（〜できない、〜わけにはいかない）や否定的なニュアンスの表現が来る。",
        "example_sentences": [
            {
                "japanese": "<ruby>親<rt>おや</rt></ruby>と<ruby>相談<rt>そうだん</rt></ruby>してからでないと、<ruby>決<rt>き</rt></ruby>められません。",
                "english": "I cannot decide until I discuss it with my parents."
            },
            {
                "japanese": "<ruby>実物<rt>じつぶつ</rt></ruby>を<ruby>見<rt>み</rt></ruby>てからでなければ、<ruby>買<rt>か</rt></ruby>うかどうか<ruby>決<rt>き</rt></ruby>められない。",
                "english": "Unless I see the actual product, I cannot decide whether to buy it."
            },
            {
                "japanese": "<ruby>手続<rt>てつづ</rt></ruby>きが<ruby>終<rt>お</rt></ruby>わってからでないと、この<ruby>部屋<rt>へや</rt></ruby>には<ruby>入<rt>はい</rt></ruby>れません。",
                "english": "You cannot enter this room until the procedure is completed."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜ところだ",
        "pattern_name_en": "just about to / in the middle of / just finished",
        "meaning_ja": "ある動作の直前・進行中・直後を表す。",
        "meaning_en": "Expresses being just about to do, in the middle of doing, or having just finished doing an action.",
        "connection_forms": [
            "V-辞書形 + ところだ（直前：これからするところ）",
            "V-ている + ところだ（最中：いましているところ）",
            "V-た形 + ところだ（直後：たったいま終わったところ）"
        ],
        "nuance_notes": "時間の進行の中の特定の時点を捉える表現。助詞との接続により「〜ところを」「〜ところで」「〜ところへ」などの形もとる。",
        "example_sentences": [
            {
                "japanese": "これから<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るところです。",
                "english": "I am just about to leave the house."
            },
            {
                "japanese": "<ruby>今<rt>いま</rt></ruby>、<ruby>資料<rt>しりょう</rt></ruby>を<ruby>作<rt>つく</rt></ruby>っているところです。",
                "english": "I am currently in the middle of preparing the documents."
            },
            {
                "japanese": "たった<ruby>今<rt>いま</rt></ruby>、<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたところです。",
                "english": "I have just arrived at the station right now."
            }
        ]
    }
]

# Section 1 drills (1課 練習 Q1-9)
sec1_drills = [
    make_mc(
        101, "1課 練習",
        "<ruby>桜<rt>さくら</rt></ruby>が（　　）うちに、お<ruby>花見<rt>はなみ</rt></ruby>に<ruby>行<rt>い</rt></ruby>きましょう。",
        ["a　散ってしまった", "b　きれいな", "c　咲く"],
        "b",
        "「〜うちに」は「状態が変わる前に」という意味。「きれいな（状態である）うちに」が適切。",
        "'~うちに' means 'before the situation changes'. 'While they are still pretty' fits perfectly."
    ),
    make_mc(
        102, "1課 練習",
        "<ruby>電車<rt>でんしゃ</rt></ruby>に（　　）ところで、<ruby>友達<rt>ともだち</rt></ruby>から<ruby>電話<rt>でんわ</rt></ruby>がかかってきた。",
        ["a　乗る", "b　乗っている", "c　乗った"],
        "c",
        "乗った直後のタイミングを表すため、「乗ったところで」が適切。",
        "Expresses the moment right after getting on the train: '乗ったところで'."
    ),
    make_mc(
        103, "1課 練習",
        "<ruby>料理<rt>りょうり</rt></ruby>が（　　）うちに、<ruby>食<rt>た</rt></ruby>べてください。",
        ["a　冷めた", "b　冷めない", "c　温かい"],
        "c",
        "「温かいうちに食べてください」が自然な表現。",
        "'Please eat while it is warm' is the natural phrasing."
    ),
    make_mc(
        104, "1課 練習",
        "<ruby>説明書<rt>せつめいしょ</rt></ruby>をよく（　　）からでないと、この<ruby>機械<rt>きかい</rt></ruby>は<ruby>使<rt>つか</rt></ruby>えない。",
        ["a　読む", "b　読んで", "c　読んだ"],
        "b",
        "接続形は「V-て形＋からでないと」。したがって「読んで」が正解。",
        "The pattern connects via te-form: '読んでからでないと'."
    ),
    make_mc(
        105, "1課 練習",
        "<ruby>留守<rt>るす</rt></ruby>の（　　）に、<ruby>宅配便<rt>たくはいびん</rt></ruby>が<ruby>届<rt>とど</rt></ruby>いていた。",
        ["a　あいだ", "b　うちに", "c　ところ"],
        "a",
        "不在という期間のある時点に荷物が届いたので、「留守のあいだに」が適切。",
        "'During the period of absence' uses '留守のあいだに'."
    ),
    make_mc(
        106, "1課 練習",
        "<ruby>両親<rt>りょうしん</rt></ruby>が（　　）うちに、<ruby>親孝行<rt>おやこうこう</rt></ruby>をしたい。",
        ["a　元気な", "b　元気だった", "c　元気で"],
        "a",
        "Na形容詞に「うちに」が接続するときは「Na-な＋うちに」。",
        "For na-adjectives, it connects with な: '元気なうちに'."
    ),
    make_mc(
        107, "1課 練習",
        "<ruby>今<rt>いま</rt></ruby>、お<ruby>風呂<rt>ふろ</rt></ruby>に（　　）ところだから、あとで<ruby>電話<rt>でんわ</rt></ruby>するね。",
        ["a　入る", "b　入って", "c　入った"],
        "a",
        "これから入る直前のタイミングなので辞書形「入るところ」が適切。",
        "Being just about to enter the bath takes the dictionary form: '入るところ'."
    ),
    make_mc(
        108, "1課 練習",
        "<ruby>会議<rt>かいぎ</rt></ruby>の（　　）、ずっとメモを<ruby>取<rt>と</rt></ruby>っていた。",
        ["a　うちに", "b　あいだに", "c　あいだ"],
        "c",
        "会議が続いている間ずっと継続していた行為なので「あいだ」が正解（「あいだに」は一時点）。",
        "Continuous action throughout the meeting requires 'あいだ' without 'に'."
    ),
    make_mc(
        109, "1課 練習",
        "<ruby>社長<rt>しゃちょう</rt></ruby>の<ruby>許可<rt>きょか</rt></ruby>を（　　）からでなければ、このプロジェクトは<ruby>進<rt>すす</rt></ruby>められない。",
        ["a　もらう", "b　もらった", "c　もらって"],
        "c",
        "接続は「V-て形＋からでなければ」。",
        "Connects via te-form: 'もらってからでなければ'."
    )
]

# ==============================================================================
# SECTION 2 (2課 〜関係して)
# ==============================================================================
sec2_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜とおりに・〜どおりに",
        "pattern_name_en": "in accordance with / just as",
        "meaning_ja": "それと同じように、その通りの状態・方法で。",
        "meaning_en": "Just as / in accordance with / exactly following a model, expectation, or instructions.",
        "connection_forms": [
            "V-辞書形 / V-た形 + とおり（に）",
            "N-の + とおり（に）",
            "N + どおり（に）"
        ],
        "nuance_notes": "名詞に直接付くときは濁音化して「〜どおり」となる（予定どおり、期待どおりなど）。",
        "example_sentences": [
            {
                "japanese": "<ruby>先生<rt>せんせい</rt></ruby>が<ruby>言<rt>い</rt></ruby>ったとおりに、やってみてください。",
                "english": "Please try doing it just as the teacher said."
            },
            {
                "japanese": "<ruby>計画<rt>けいかく</rt></ruby>どおりに<ruby>仕事<rt>しごと</rt></ruby>が<ruby>進<rt>すす</rt></ruby>んでいます。",
                "english": "The work is progressing according to schedule."
            },
            {
                "japanese": "<ruby>私<rt>わたし</rt></ruby>の<ruby>予想<rt>よそう</rt></ruby>のとおり、<ruby>彼<rt>かれ</rt></ruby>らのチームが<ruby>勝<rt>か</rt></ruby>った。",
                "english": "Just as I had predicted, their team won."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜によって・〜によっては",
        "pattern_name_en": "depending on / by means of / due to",
        "meaning_ja": "それぞれに応じて異なる（〜によって異なる・変わる・分かれる）。〜によっては（特定の場合には）。",
        "meaning_en": "Depending on differences in X, something varies or differs. 〜によっては highlights a particular case.",
        "connection_forms": [
            "N + によって / により",
            "N + によっては（特定の場合）"
        ],
        "nuance_notes": "多様性や個人差を表す文脈で頻出。「〜によって違う」「〜によって異なる」などの語と呼応しやすい。",
        "example_sentences": [
            {
                "japanese": "<ruby>国<rt>くに</rt></ruby>によって<ruby>習慣<rt>しゅうかん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>います。",
                "english": "Customs differ depending on the country."
            },
            {
                "japanese": "<ruby>人<rt>ひと</rt></ruby>によって<ruby>感<rt>かん</rt></ruby>じ<ruby>方<rt>かた</rt></ruby>はさまざまだ。",
                "english": "Feelings and perceptions vary from person to person."
            },
            {
                "japanese": "<ruby>場合<rt>ばあい</rt></ruby>によっては、<ruby>今年<rt>ことし</rt></ruby>の<ruby>旅行<rt>りょこう</rt></ruby>は<ruby>中止<rt>ちゅうし</rt></ruby>になるかもしれない。",
                "english": "Depending on the situation, this year's trip might be canceled."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜たびに",
        "pattern_name_en": "every time / whenever",
        "meaning_ja": "そのたびごとに、いつも同じことが起こる。",
        "meaning_en": "Every time / whenever X happens, Y always happens as well.",
        "connection_forms": [
            "V-辞書形 + たびに",
            "N-の + たびに"
        ],
        "nuance_notes": "日常的で当たり前のこと（×朝起きるたびに顔を洗う）には使わない。特別な気持ちや事象に使う。",
        "example_sentences": [
            {
                "japanese": "この<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>見<rt>み</rt></ruby>るたびに、<ruby>楽<rt>たの</rt></ruby>しかった<ruby>旅行<rt>りょこう</rt></ruby>を<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>す。",
                "english": "Every time I look at this photograph, I recall the fun trip."
            },
            {
                "japanese": "<ruby>会<rt>あ</rt></ruby>うたびに、<ruby>彼女<rt>かのじょ</rt></ruby>はきれいになっていく。",
                "english": "Every time I see her, she becomes more beautiful."
            },
            {
                "japanese": "<ruby>出張<rt>しゅっちょう</rt></ruby>のたびに、お<ruby>土産<rt>みやげ</rt></ruby>を<ruby>買<rt>か</rt></ruby>ってくる。",
                "english": "Whenever I go on a business trip, I buy souvenirs."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "（〜ば）〜ほど・（〜なら）〜ほど・〜ほど",
        "pattern_name_en": "the more... the more...",
        "meaning_ja": "一方の程度が進むと、それに伴ってもう一方の程度も進む。",
        "meaning_en": "The more X progresses, the more Y progresses in proportion.",
        "connection_forms": [
            "V-ば + V-辞書形 + ほど",
            "A-ければ + A-い + ほど",
            "Na-なら（ば） + Na-な + ほど",
            "N / Na + であるほど",
            "V / A / Na / N + ほど（単独形）"
        ],
        "nuance_notes": "比例変化を表す。「考えれば考えるほどわからない」のように同一語を繰り返すことが多い。",
        "example_sentences": [
            {
                "japanese": "<ruby>考<rt>かんが</rt></ruby>えれば<ruby>考<rt>かんが</rt></ruby>えるほど、わからなくなる。",
                "english": "The more I think about it, the less I understand."
            },
            {
                "japanese": "<ruby>荷物<rt>にもつ</rt></ruby>は<ruby>少<rt>すく</rt></ruby>なければ<ruby>少<rt>すく</rt></ruby>ないほどいい。",
                "english": "The less luggage you have, the better."
            },
            {
                "japanese": "<ruby>簡単<rt>かんたん</rt></ruby>なら<ruby>簡単<rt>かんたん</rt></ruby>なほど、ありがたい。",
                "english": "The simpler it is, the more grateful I am."
            }
        ]
    },
    {
        "pattern_number": 5,
        "pattern_name": "〜ついでに",
        "pattern_name_en": "while at it / taking the opportunity to",
        "meaning_ja": "ある主の行動をするときに、合間を利用して別のことも一緒に行う。",
        "meaning_en": "While doing a primary action, taking the opportunity to do another secondary action alongside it.",
        "connection_forms": [
            "V-辞書形 / V-た形 + ついでに",
            "N-の + ついでに"
        ],
        "nuance_notes": "主となる行動のついでに行う行動は、負担の少ない軽い行動であることが多い。",
        "example_sentences": [
            {
                "japanese": "<ruby>散歩<rt>さんぽ</rt></ruby>のついでに、ポストに<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>入<rt>い</rt></ruby>れてきてくれる？",
                "english": "While you're on your walk, could you drop this letter in the mailbox for me?"
            },
            {
                "japanese": "<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>に<ruby>行<rt>い</rt></ruby>ったついでに、<ruby>本屋<rt>ほんや</rt></ruby>にも<ruby>寄<rt>よ</rt></ruby>った。",
                "english": "While I was out shopping, I also dropped by the bookstore."
            },
            {
                "japanese": "<ruby>東京<rt>とうきょう</rt></ruby>へ<ruby>出張<rt>しゅっちょう</rt></ruby>したついでに、<ruby>友人<rt>ゆうじん</rt></ruby>に<ruby>会<rt>あ</rt></ruby>ってきた。",
                "english": "While on a business trip to Tokyo, I also met up with a friend."
            }
        ]
    }
]

# Section 2 drills (2課 練習 Q1-9, plus 1課・2課 combined Q1-9)
sec2_drills = [
    make_mc(
        201, "2課 練習",
        "<ruby>予定<rt>よてい</rt></ruby>（　　）に<ruby>工事<rt>こうじ</rt></ruby>が<ruby>進<rt>すす</rt></ruby>んでいる。",
        ["a　とおり", "b　によって", "c　どおり"],
        "c",
        "名詞「予定」に直接接続する場合は「予定どおり」。",
        "Attaches directly to noun: '予定どおり'."
    ),
    make_mc(
        202, "2課 練習",
        "<ruby>練習<rt>れんしゅう</rt></ruby>すればする（　　）、<ruby>上手<rt>じょうず</rt></ruby>になる。",
        ["a　ほど", "b　たびに", "c　とおり"],
        "a",
        "「〜ば〜ほど」で比例変化を表す。",
        "'The more... the more...' structure requires 'ほど'."
    ),
    make_mc(
        203, "2課 練習",
        "<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>の（　　）に、<ruby>銀行<rt>ぎんこう</rt></ruby>へ<ruby>寄<rt>よ</rt></ruby>ってきた。",
        ["a　ついで", "b　たび", "c　あいだ"],
        "a",
        "買い物の機会を利用して銀行に寄ったので「ついでに」。",
        "'Taking the opportunity while out shopping' is 'ついでに'."
    ),
    make_mc(
        204, "2課 練習",
        "<ruby>季節<rt>きせつ</rt></ruby>（　　）、<ruby>景色<rt>けしき</rt></ruby>がまったく<ruby>違<rt>ちが</rt></ruby>う。",
        ["a　のとおり", "b　のついでに", "c　によって"],
        "c",
        "季節に応じて変化するので「季節によって」。",
        "'Differing depending on the season' is '季節によって'."
    ),
    make_mc(
        205, "2課 練習",
        "<ruby>試験<rt>しけん</rt></ruby>の（　　）に、お<ruby>腹<rt>なか</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>くなる。",
        ["a　ついで", "b　たび", "c　ほど"],
        "b",
        "試験があるたびに毎回お腹が痛くなるので「たびに」。",
        "'Every time' is 'たびに'."
    ),
    make_mc(
        206, "2課 練習",
        "<ruby>思<rt>おも</rt></ruby>った（　　）の<ruby>結果<rt>けっか</rt></ruby>になった。",
        ["a　とおり", "b　どおり", "c　たび"],
        "a",
        "動詞た形「思った」に付くので「とおり」。",
        "Attaches to verb ta-form: '思ったとおり'."
    ),
    make_mc(
        207, "2課 練習",
        "<ruby>天候<rt>てんこう</rt></ruby>（　　）は、<ruby>試合<rt>しあい</rt></ruby>が<ruby>延期<rt>えんき</rt></ruby>になることもある。",
        ["a　どおり", "b　によっては", "c　ついでに"],
        "b",
        "特定の場合には延期になるという意味なので「によっては」。",
        "'In some weather cases' takes 'によっては'."
    ),
    make_mc(
        208, "2課 練習",
        "<ruby>便利<rt>べんり</rt></ruby>なら<ruby>便利<rt>べんり</rt></ruby>な（　　）、<ruby>生活<rt>せいかつ</rt></ruby>が<ruby>楽<rt>らく</rt></ruby>になる。",
        ["a　とおり", "b　ほど", "c　ついで"],
        "b",
        "「NaならNaなほど」の比例構文。",
        "Proportional pattern 'なら...ほど'."
    ),
    make_mc(
        209, "2課 練習",
        "<ruby>散歩<rt>さんぽ</rt></ruby>に<ruby>行<rt>い</rt></ruby>く（　　）、ゴミを<ruby>捨<rt>す</rt></ruby>ててきて。",
        ["a　たびに", "b　ほどに", "c　ついでに"],
        "c",
        "散歩の機会を利用してゴミ出しを頼む文脈なので「ついでに」。",
        "'While you're going out for a walk' is 'ついでに'."
    ),
    # 1課・2課 まとまりの練習
    make_mc(
        210, "1課・2課 練習",
        "<ruby>日本<rt>にほん</rt></ruby>に（　　）うちに、<ruby>富士山<rt>ふじさん</rt></ruby>に<ruby>登<rt>のぼ</rt></ruby>りたい。",
        ["a　いた", "b　いるの", "c　いる"],
        "c",
        "動詞辞書形「いるうちに」。",
        "Verb dictionary form: 'いるうちに'."
    ),
    make_mc(
        211, "1課・2課 練習",
        "<ruby>説明<rt>せつめい</rt></ruby>を（　　）からでないと、このソフトは<ruby>使<rt>つか</rt></ruby>いこなせない。",
        ["a　聞いて", "b　聞く", "c　聞いた"],
        "a",
        "「V-て形＋からでないと」。",
        "Form: '聞いてからでないと'."
    ),
    make_mc(
        212, "1課・2課 練習",
        "<ruby>私<rt>わたし</rt></ruby>が（　　）とおりに、やってみてください。",
        ["a　やった", "b　やるの", "c　やれ"],
        "a",
        "動詞た形「やったとおりに」。",
        "Verb ta-form: 'やったとおりに'."
    ),
    make_mc(
        213, "1課・2課 練習",
        "<ruby>荷物<rt>にもつ</rt></ruby>が（　　）ほど、<ruby>運<rt>はこ</rt></ruby>ぶのが<ruby>大変<rt>たいへん</rt></ruby>になる。",
        ["a　多い", "b　重い", "c　重ければ"],
        "b",
        "「重いほど」で単独のほど接続。",
        "'重いほど' expresses 'the heavier it is'."
    ),
    make_mc(
        214, "1課・2課 練習",
        "<ruby>図書館<rt>としょかん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く（　　）に、この<ruby>本<rt>ほん</rt></ruby>を<ruby>返<rt>かえ</rt></ruby>してきてくれませんか。",
        ["a　ついで", "b　あいだ", "c　うち"],
        "a",
        "行動の機会を利用する「ついでに」。",
        "'ついでに' means taking the opportunity."
    ),
    make_mc(
        215, "1課・2課 練習",
        "<ruby>留守<rt>るす</rt></ruby>の（　　）に、<ruby>友達<rt>ともだち</rt></ruby>が<ruby>遊<rt>あそ</rt></ruby>びに来たらしい。",
        ["a　ところ", "b　あいだ", "c　うち"],
        "b",
        "「留守のあいだに」が適切。",
        "'留守のあいだに' is correct."
    ),
    make_star(
        216, "1課・2課 練習",
        "<ruby>朝<rt>あさ</rt></ruby>から　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>疲<rt>つか</rt></ruby>れてしまった。",
        ["1　歩いたので", "2　っぱなしで", "3　立ち", "4　ずっと"],
        [4, 3, 2, 1], 2, "2",
        "<ruby>朝<rt>あさ</rt></ruby>からずっと立ちっぱなしで歩いたので疲れてしまった。",
        "I was tired from standing all day and walking since morning.",
        "「ずっと立ちっぱなしで歩いたので」の順序。3番目は2「っぱなしで」。",
        "The correct order gives option 2 at the star position."
    ),
    make_star(
        217, "1課・2課 練習",
        "<ruby>実際<rt>じっさい</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>分<rt>わ</rt></ruby>からない。",
        ["1　やって", "2　みてからでないと", "3　うまくいくか", "4　どうか"],
        [1, 2, 3, 4], 3, "3",
        "<ruby>実際<rt>じっさい</rt></ruby>にやってみてからでないとうまくいくかどうか分からない。",
        "Unless I actually try it out, I don't know whether it will go well.",
        "「やって(1) みてからでないと(2) うまくいくか(3) どうか(4) 分からない」。★は3。",
        "Order is 1 -> 2 -> 3 -> 4, placing 3 at the star."
    ),
    make_star(
        218, "1課・2課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>帰<rt>かえ</rt></ruby>ってきた。",
        ["1　出張の", "2　お土産を", "3　買って", "4　たびに"],
        [1, 4, 2, 3], 2, "2",
        "<ruby>彼<rt>かれ</rt></ruby>は出張のたびにお土産を買って帰ってきた。",
        "Every time he went on a business trip, he bought souvenirs and came back.",
        "「出張の(1) たびに(4) お土産を(2) 買って(3)」。3番目の★は2。",
        "Order is 1 -> 4 -> 2 -> 3, with 2 at the star."
    )
]

# ==============================================================================
# SECTION 3 (3課 比べれば…・〜がいちばん)
# ==============================================================================
sec3_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜くらいだ・〜ぐらいだ・〜くらい…・〜ぐらい…・〜ほどだ・〜ほど…",
        "pattern_name_en": "to the extent that / so... that",
        "meaning_ja": "程度が非常に高いことを、極端な例や比喩を使って説明する。",
        "meaning_en": "Explains an extreme degree of something by using a vivid example or metaphor ('so ... that ...').",
        "connection_forms": [
            "V-辞書形 / V-た形 / V-ない形 + くらい / ほど",
            "A-い + くらい / ほど",
            "Na-な + くらい / ほど",
            "N + くらい / ほど"
        ],
        "nuance_notes": "「ほど」のほうが「くらい」よりもやや改まった表現。「涙が出るほど痛い」「死ぬほど疲れた」など。",
        "example_sentences": [
            {
                "japanese": "<ruby>涙<rt>なみだ</rt></ruby>が<ruby>出<rt>で</rt></ruby>るほど、おなかを<ruby>抱<rt>かか</rt></ruby>えて<ruby>笑<rt>わら</rt></ruby>った。",
                "english": "I laughed so hard holding my stomach that tears came out."
            },
            {
                "japanese": "もう<ruby>一歩<rt>いっぽ</rt></ruby>も<ruby>歩<rt>ある</rt></ruby>けないくらい、<ruby>疲<rt>つか</rt></ruby>れた。",
                "english": "I'm so tired that I can't take another step."
            },
            {
                "japanese": "<ruby>声<rt>こえ</rt></ruby>も<ruby>出<rt>で</rt></ruby>ないほど、<ruby>驚<rt>おどろ</rt></ruby>いた。",
                "english": "I was so startled that I couldn't even make a sound."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜くらい…はない・〜ぐらい…はない・〜ほど…はない",
        "pattern_name_en": "nothing is as... as / there is no... like",
        "meaning_ja": "〜が最高である、それ以上のものはないという話者の主観的な強調。",
        "meaning_en": "Subjective assertion that nothing equals or surpasses X in quality or intensity ('there is nothing as ... as X').",
        "connection_forms": [
            "N + くらい / ほど + … はない",
            "V-るの + くらい / ほど + … はない"
        ],
        "nuance_notes": "話者の主観的な判断・意見を表す表現であり、客観的な事実（世界一の山など）にはあまり使わない。",
        "example_sentences": [
            {
                "japanese": "<ruby>仕事<rt>しごと</rt></ruby>のあとのビールほど、おいしいものはない。",
                "english": "Nothing tastes better than beer after work."
            },
            {
                "japanese": "<ruby>健康<rt>けんこう</rt></ruby>ほど<ruby>大切<rt>たいせつ</rt></ruby>なものはない。",
                "english": "There is nothing more important than good health."
            },
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>くらい<ruby>歌<rt>うた</rt></ruby>が<ruby>上手<rt>じょうず</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>はいない。",
                "english": "There is nobody as good at singing as he is."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜くらいなら…・〜ぐらいなら…",
        "pattern_name_en": "rather than... / if it comes to doing...",
        "meaning_ja": "〜という最悪の事態になるくらいなら、むしろ…のほうがましだ。",
        "meaning_en": "If the alternative is doing X (which is abhorred), one would rather do Y instead.",
        "connection_forms": [
            "V-辞書形 + くらいなら / ぐらいなら"
        ],
        "nuance_notes": "前件には絶対に避けたい好ましくない事態、後件にはそれに比べればまだ耐えられる選択肢が来る。",
        "example_sentences": [
            {
                "japanese": "<ruby>途中<rt>とちゅう</rt></ruby>で<ruby>諦<rt>あきら</rt></ruby>めるくらいなら、<ruby>最初<rt>さいしょ</rt></ruby>からやらないほうがいい。",
                "english": "If you're going to give up halfway, it's better not to do it at all from the start."
            },
            {
                "japanese": "まずいものを<ruby>食<rt>た</rt></ruby>べるくらいなら、<ruby>何<rt>なに</rt></ruby>も<ruby>食<rt>た</rt></ruby>べないほうがましだ。",
                "english": "Rather than eat awful food, I'd rather eat nothing at all."
            },
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>に<ruby>謝<rt>あやま</rt></ruby>るくらいなら、<ruby>会社<rt>かいしゃ</rt></ruby>を<ruby>辞<rt>や</rt></ruby>めたほうがいい。",
                "english": "I'd rather quit the company than apologize to him."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜に限る",
        "pattern_name_en": "nothing beats / X is the best",
        "meaning_ja": "〜が一番良い、ベストであると強く主張する。",
        "meaning_en": "Asserts strongly that X is by far the best option or choice for a situation.",
        "connection_forms": [
            "V-辞書形 / V-ない形 + に限る",
            "N + に限る"
        ],
        "nuance_notes": "話者の主観的な判断・好みを表す。客観的なルールを述べるのではない。",
        "example_sentences": [
            {
                "japanese": "<ruby>暑<rt>あつ</rt></ruby>い<ruby>夏<rt>なつ</rt></ruby>は、やっぱりアイスクリームに<ruby>限<rt>かぎ</rt></ruby>る。",
                "english": "In hot summer, ice cream is definitely the best."
            },
            {
                "japanese": "<ruby>風邪<rt>かぜ</rt></ruby>をひいたときは、<ruby>暖<rt>あたた</rt></ruby>かくして<ruby>早<rt>はや</rt></ruby>く<ruby>寝<rt>ね</rt></ruby>るに<ruby>限<rt>かぎ</rt></ruby>る。",
                "english": "When you catch a cold, the best thing to do is stay warm and go to bed early."
            },
            {
                "japanese": "<ruby>疲<rt>つか</rt></ruby>れたときは、ゆっくりお<ruby>風呂<rt>ふろ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>るに<ruby>限<rt>かぎ</rt></ruby>る。",
                "english": "When you're exhausted, taking a relaxing bath is the best."
            }
        ]
    }
]

# Section 3 drills (3課 練習 Q1-9)
sec3_drills = [
    make_mc(
        301, "3課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>に<ruby>頼<rt>たの</rt></ruby>む（　　）、<ruby>自分<rt>じぶん</rt></ruby>でやったほうがましだ。",
        ["a　ほど", "b　に限る", "c　くらいなら"],
        "c",
        "「〜くらいなら…ほうがましだ」の形。",
        "Pattern '〜くらいなら…ほうがましだ'."
    ),
    make_mc(
        302, "3課 練習",
        "<ruby>寒<rt>さむ</rt></ruby>い<ruby>冬<rt>ふゆ</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>は、<ruby>鍋料理<rt>なべりょうり</rt></ruby>に（　　）。",
        ["a　限る", "b　くらいだ", "c　ほどはない"],
        "a",
        "「〜に限る」で一番良いと主張する。",
        "'〜に限る' asserts that hot pot is best."
    ),
    make_mc(
        303, "3課 練習",
        "<ruby>昨日<rt>きのう</rt></ruby>は<ruby>声<rt>こえ</rt></ruby>が（　　）くらい、カラオケで<ruby>歌<rt>うた</rt></ruby>った。",
        ["a　出ない", "b　出なくなる", "c　出なくなった"],
        "b",
        "程度の変化を表す「出なくなるくらい」。",
        "Degree of becoming unable to speak: '出なくなるくらい'."
    ),
    make_mc(
        304, "3課 練習",
        "<ruby>家族<rt>かぞく</rt></ruby>と（　　）ほど、<ruby>幸<rt>しあわ</rt></ruby>せな<ruby>時間<rt>じかん</rt></ruby>はない。",
        ["a　過ごす", "b　過ごすの", "c　過ごした"],
        "b",
        "名詞節「過ごすのほど」。",
        "Noun nominalizer: '過ごすのほど'."
    ),
    make_mc(
        305, "3課 練習",
        "<ruby>嫌<rt>いや</rt></ruby>な<ruby>仕事<rt>しごと</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>き<ruby>受<rt>う</rt></ruby>ける（　　）、<ruby>断<rt>ことわ</rt></ruby>ったほうがいい。",
        ["a　くらいなら", "b　ほど", "c　に限る"],
        "a",
        "消極的選択「〜くらいなら」。",
        "'Rather than accept' is 'くらいなら'."
    ),
    make_mc(
        306, "3課 練習",
        "<ruby>痛<rt>いた</rt></ruby>くて<ruby>涙<rt>なみだ</rt></ruby>が（　　）ほどだった。",
        ["a　出る", "b　出た", "c　出るかのような"],
        "c",
        "公式解答に基づく選択肢 c。",
        "Option c as keyed."
    ),
    make_mc(
        307, "3課 練習",
        "<ruby>休<rt>やす</rt></ruby>みの<ruby>日<rt>ひ</rt></ruby>は、<ruby>家<rt>いえ</rt></ruby>でゆっくり（　　）に<ruby>限<rt>かぎ</rt></ruby>る。",
        ["a　休む", "b　休んだ", "c　休むの"],
        "c",
        "動詞の名詞化「休むの」＋に限る。",
        "Nominalized verb: '休むのに限る'."
    ),
    make_mc(
        308, "3課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>（　　）<ruby>親切<rt>しんせつ</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>は、めったにいない。",
        ["a　ほど", "b　に限る", "c　くらいなら"],
        "a",
        "「〜ほど…な人はいない」。",
        "'Nobody is as kind as him': '彼ほど'."
    ),
    make_mc(
        309, "3課 練習",
        "<ruby>足<rt>あし</rt></ruby>が（　　）くらい、<ruby>長<rt>なが</rt></ruby>い<ruby>時間<rt>じかん</rt></ruby><ruby>立<rt>た</rt></ruby>ちっぱなしだった。",
        ["a　痛い", "b　痛くなる", "c　痛かった"],
        "b",
        "「痛くなるくらい」。",
        "'痛くなるくらい' expresses extreme degree."
    )
]

# ==============================================================================
# SECTION 4 (4課 〜とは違って)
# ==============================================================================
sec4_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜に対して",
        "pattern_name_en": "in contrast to / whereas",
        "meaning_ja": "AとBを対比させて、その違いを際立たせる。",
        "meaning_en": "Contrasts two opposing things or facts (whereas X, Y is ...).",
        "connection_forms": [
            "N + に対して",
            "普通形（Naな / Naである・Nな / Nである） + のに対して"
        ],
        "nuance_notes": "対象に向かう意味の「〜に対して」（目上の人に対して敬語を使う）とは別用法で、ここでは明確な対比・コントラストを表す。",
        "example_sentences": [
            {
                "japanese": "<ruby>兄<rt>あに</rt></ruby>は<ruby>活発<rt>かっぱつ</rt></ruby>なのに対して、<ruby>弟<rt>おとうと</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かな<ruby>性格<rt>せいかく</rt></ruby>だ。",
                "english": "Whereas the older brother is outgoing, the younger brother has a quiet personality."
            },
            {
                "japanese": "<ruby>都市部<rt>としぶ</rt></ruby>で<ruby>人口<rt>じんこう</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えているのに対して、<ruby>地方<rt>ちほう</rt></ruby>では<ruby>減少<rt>げんしょう</rt></ruby>している。",
                "english": "While the population is increasing in urban areas, it is decreasing in rural regions."
            },
            {
                "japanese": "<ruby>昨日<rt>きのう</rt></ruby>の<ruby>大雨<rt>おおあめ</rt></ruby>に対して、<ruby>今日<rt>きょう</rt></ruby>は<ruby>素晴<rt>すば</rt></ruby>らしい<ruby>青空<rt>あおぞら</rt></ruby>だ。",
                "english": "In contrast to yesterday's heavy rain, today is a magnificent clear sky."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜反面",
        "pattern_name_en": "on the other hand / but on the reverse side",
        "meaning_ja": "ある事柄の一面を認めた上で、その裏にある別の反対の側面を述べる。",
        "meaning_en": "Presents two contrasting, double-sided aspects of the same subject ('on the one hand..., but on the flip side...').",
        "connection_forms": [
            "動詞・形容詞 普通形 + 反面",
            "Naである / Naな + 反面",
            "Nである + 反面"
        ],
        "nuance_notes": "同一の対象・事柄が持つプラス面とマイナス面の共存を対比させることが多い。",
        "example_sentences": [
            {
                "japanese": "この<ruby>仕事<rt>しごと</rt></ruby>は<ruby>給料<rt>きゅうりょう</rt></ruby>が<ruby>高<rt>たか</rt></ruby>い<ruby>反面<rt>はんめん</rt></ruby>、とても<ruby>忙<rt>いそが</rt></ruby>しい。",
                "english": "While this job pays well, on the flip side it is extremely busy."
            },
            {
                "japanese": "<ruby>都会<rt>とかい</rt></ruby>の<ruby>暮<rt>く</rt></ruby>らしは<ruby>便利<rt>べんり</rt></ruby>な<ruby>反面<rt>はんめん</rt></ruby>、ストレスも<ruby>多<rt>おお</rt></ruby>い。",
                "english": "Living in the city is convenient, but on the other hand it is full of stress."
            },
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>優<rt>やさ</rt></ruby>しい<ruby>反面<rt>はんめん</rt></ruby>、<ruby>怒<rt>おこ</rt></ruby>るととても<ruby>怖<rt>こわ</rt></ruby>い。",
                "english": "He is very kind, but on the reverse side, when he gets angry he is terrifying."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜一方（で）",
        "pattern_name_en": "on the one hand... on the other hand / while simultaneously",
        "meaning_ja": "一つの事柄に関して、同時に存在する二つの側面を並べて述べる。",
        "meaning_en": "Contrasts two concurrent aspects or trends existing simultaneously ('while..., at the same time...').",
        "connection_forms": [
            "普通形（Naな / Naである・Nである） + 一方（で）"
        ],
        "nuance_notes": "「〜反面」と似ているが、「〜一方（で）」は対立する二つの側面に限らず、並行して進む二つの動きや役割にも用いられる。",
        "example_sentences": [
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>会社<rt>かいしゃ</rt></ruby>を<ruby>経営<rt>けいえい</rt></ruby>する<ruby>一方<rt>いっぽう</rt></ruby>で、<ruby>大学<rt>だいがく</rt></ruby>で<ruby>教鞭<rt>きょうべん</rt></ruby>を<ruby>執<rt>と</rt></ruby>っている。",
                "english": "While managing a company, he also teaches at a university."
            },
            {
                "japanese": "<ruby>物価<rt>ぶっか</rt></ruby>が<ruby>上<rt>あ</rt></ruby>がる<ruby>一方<rt>いっぽう</rt></ruby>で、<ruby>給料<rt>きゅうりょう</rt></ruby>はなかなか<ruby>上<rt>あ</rt></ruby>がらない。",
                "english": "While prices keep rising, salaries rarely go up."
            },
            {
                "japanese": "<ruby>便利<rt>べんり</rt></ruby>になる<ruby>一方<rt>いっぽう</rt></ruby>で、<ruby>環境破壊<rt>かんきょうはかい</rt></ruby>も<ruby>進<rt>すす</rt></ruby>んでいる。",
                "english": "While life becomes more convenient, environmental destruction also advances."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜というより",
        "pattern_name_en": "rather than... / more of a... than",
        "meaning_ja": "Aという表現よりも、Bという表現のほうが実態に合っている。",
        "meaning_en": "Suggests that description B is more accurate or fitting than description A ('rather than A, it's more like B').",
        "connection_forms": [
            "普通形 / 語幹 + というより"
        ],
        "nuance_notes": "言い直しや、より適切な言葉への訂正を行う際に用いる。",
        "example_sentences": [
            {
                "japanese": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>涼<rt>すず</rt></ruby>しいというより、むしろ<ruby>寒<rt>さむ</rt></ruby>い。",
                "english": "Rather than cool, today is actually downright cold."
            },
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>は<ruby>友人<rt>ゆうじん</rt></ruby>というより、<ruby>家族<rt>かぞく</rt></ruby>のような<ruby>存在<rt>そんざい</rt></ruby>だ。",
                "english": "Rather than a friend, he is like family."
            },
            {
                "japanese": "<ruby>歩<rt>ある</rt></ruby>くというより、<ruby>走<rt>はし</rt></ruby>るようなスピードで<ruby>進<rt>すす</rt></ruby>んだ。",
                "english": "We progressed at a speed closer to running than walking."
            }
        ]
    },
    {
        "pattern_number": 5,
        "pattern_name": "〜かわりに",
        "pattern_name_en": "instead of / in exchange for",
        "meaning_ja": "1: 〜をしないで別のことをする。2: 〜の代償・見返りとして別のことをする。",
        "meaning_en": "1: Instead of doing X, doing Y. 2: In exchange / return for X, compensating with Y.",
        "connection_forms": [
            "V-辞書形 + かわりに",
            "N-の + かわりに"
        ],
        "nuance_notes": "代理（誰かの代わりに）の意味と、代償・条件引き換え（教えてもらう代わりに奢る）の意味がある。",
        "example_sentences": [
            {
                "japanese": "<ruby>英語<rt>えいご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてもらうかわりに、<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えています。",
                "english": "In exchange for being taught English, I teach Japanese."
            },
            {
                "japanese": "<ruby>日曜日<rt>にちようび</rt></ruby>に<ruby>出勤<rt>しゅっきん</rt></ruby>したかわりに、<ruby>月曜日<rt>げつようび</rt></ruby>に<ruby>休<rt>やす</rt></ruby>みをとった。",
                "english": "In exchange for working on Sunday, I took Monday off."
            },
            {
                "japanese": "<ruby>旅行<rt>りょこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>くかわりに、<ruby>新<rt>あたら</rt></ruby>しいパソコンを<ruby>買<rt>か</rt></ruby>った。",
                "english": "Instead of going on a trip, I bought a new PC."
            }
        ]
    }
]

# Section 4 drills (4課 練習 Q1-9, plus 3課・4課 combined Q1-9)
sec4_drills = [
    make_mc(
        401, "4課 練習",
        "<ruby>長男<rt>ちょうなん</rt></ruby>が<ruby>理系<rt>りけい</rt></ruby>なの（　　）、<ruby>次男<rt>じなん</rt></ruby>は<ruby>文系<rt>ぶんけい</rt></ruby>に<ruby>進<rt>すす</rt></ruby>んだ。",
        ["a　に対して", "b　反面", "c　かわりに"],
        "a",
        "兄弟の専攻の対比なので「に対して」。",
        "Contrasting majors of brothers: 'に対して'."
    ),
    make_mc(
        402, "4課 練習",
        "<ruby>車<rt>くるま</rt></ruby>は<ruby>便利<rt>べんり</rt></ruby>な（　　）、お<ruby>金<rt>かね</rt></ruby>がかかる。",
        ["a　に対して", "b　反面", "c　というより"],
        "b",
        "同じ車の長所と短所の裏表なので「反面」。",
        "Flip side of having a car: '反面'."
    ),
    make_mc(
        403, "4課 練習",
        "<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>に<ruby>行<rt>い</rt></ruby>く（　　）、<ruby>家<rt>いえ</rt></ruby>でDVDを<ruby>見<rt>み</rt></ruby>た。",
        ["a　かわりに", "b　反面", "c　一方"],
        "a",
        "映画館に行く代わりに家で見たので「かわりに」。",
        "'Instead of going out to see a movie': 'かわりに'."
    ),
    make_mc(
        404, "4課 練習",
        "<ruby>彼女<rt>かのじょ</rt></ruby>は<ruby>美人<rt>びじん</rt></ruby>というより、（　　）タイプだ。",
        ["a　きれいです", "b　美人な", "c　かわいい"],
        "c",
        "美人というよりかわいいタイプだ。",
        "'Cute rather than beautiful': 'かわいい'."
    ),
    make_mc(
        405, "4課 練習",
        "<ruby>薬<rt>くすり</rt></ruby>は<ruby>効果<rt>こうか</rt></ruby>がある（　　）、<ruby>副作用<rt>ふくさよう</rt></ruby>もある。",
        ["a　かわりに", "b　反面", "c　に対して"],
        "b",
        "効果と副作用の表裏一体なので「反面」。",
        "Opposing sides of medicine: '反面'."
    ),
    make_mc(
        406, "4課 練習",
        "<ruby>子供<rt>こども</rt></ruby>たちに（　　）かわりに、<ruby>大人<rt>おとな</rt></ruby>たちが<ruby>会場<rt>かいじょう</rt></ruby>を<ruby>片付<rt>かたづ</rt></ruby>けた。",
        ["a　任せる", "b　任せて", "c　任せた"],
        "a",
        "動詞辞書形「任せるかわりに」。",
        "Verb dictionary form: '任せるかわりに'."
    ),
    make_mc(
        407, "4課 練習",
        "<ruby>賛成<rt>さんせい</rt></ruby>する<ruby>意見<rt>いけん</rt></ruby>がある（　　）、<ruby>反対<rt>はんたい</rt></ruby>する<ruby>意見<rt>いけん</rt></ruby>もある。",
        ["a　一方で", "b　かわりに", "c　というより"],
        "a",
        "賛成と反対の両面が並行して存在するので「一方で」。",
        "Two concurrent viewpoints: '一方で'."
    ),
    make_mc(
        408, "4課 練習",
        "<ruby>怒<rt>おこ</rt></ruby>っているというより、（　　）ようだ。",
        ["a　悲しかった", "b　悲しい", "c　悲しむ"],
        "b",
        "い形容詞「悲しいようだ」。",
        "Adjective: '悲しいようだ'."
    ),
    make_mc(
        409, "4課 練習",
        "<ruby>昼<rt>ひる</rt></ruby>は<ruby>暖<rt>あたた</rt></ruby>かいの（　　）、<ruby>夜<rt>よる</rt></ruby>はとても<ruby>冷<rt>ひ</rt></ruby>え<ruby>込<rt>こ</rt></ruby>む。",
        ["a　反面", "b　かわりに", "c　に対して"],
        "c",
        "昼と夜の対比なので「に対して」。",
        "Day vs night contrast: 'に対して'."
    ),
    # 3課・4課 まとまりの練習
    make_mc(
        410, "3課・4課 練習",
        "<ruby>私<rt>わたし</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>は<ruby>狭<rt>せま</rt></ruby>い（　　）、<ruby>家賃<rt>やちん</rt></ruby>が<ruby>安<rt>やす</rt></ruby>い。",
        ["a　反面", "b　に対して", "c　かわりに"],
        "c",
        "狭いというマイナスの代償として家賃が安いので「かわりに」。",
        "Compensation / tradeoff: 'かわりに'."
    ),
    make_mc(
        411, "3課・4課 練習",
        "<ruby>富士山<rt>ふじさん</rt></ruby>（　　）<ruby>美<rt>うつく</rt></ruby>しい<ruby>山<rt>やま</rt></ruby>は<ruby>日本<rt>にほん</rt></ruby>にはない。",
        ["a　ほど", "b　くらいなら", "c　に限る"],
        "a",
        "「富士山ほど美しい山はない」。",
        "'No mountain as beautiful as Mt. Fuji': 'ほど'."
    ),
    make_mc(
        412, "3課・4課 練習",
        "<ruby>泣<rt>な</rt></ruby>く（　　）なら、<ruby>最初<rt>さいしょ</rt></ruby>からやらなければよかったのに。",
        ["a　ほど", "b　くらい", "c　に限る"],
        "b",
        "「〜くらいなら」。",
        "Pattern '〜くらいなら'."
    ),
    make_mc(
        413, "3課・4課 練習",
        "<ruby>兄<rt>あに</rt></ruby>が<ruby>大食<rt>おおぐ</rt></ruby>いなの（　　）、<ruby>弟<rt>おとうと</rt></ruby>は<ruby>小食<rt>しょうしょく</rt></ruby>だ。",
        ["a　に対して", "b　反面", "c　かわりに"],
        "a",
        "兄弟の対比なので「に対して」。",
        "Contrasting eating habits: 'に対して'."
    ),
    make_mc(
        414, "3課・4課 練習",
        "<ruby>疲<rt>つか</rt></ruby>れたときは、<ruby>甘<rt>あま</rt></ruby>いものを<ruby>食<rt>た</rt></ruby>べる（　　）。",
        ["a　くらいだ", "b　ほどはない", "c　に限る"],
        "c",
        "「〜に限る」。",
        "'Eating sweets is best': 'に限る'."
    ),
    make_mc(
        415, "3課・4課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>は<ruby>親切<rt>しんせつ</rt></ruby>な（　　）、おせっかいなところもある。",
        ["a　に対して", "b　反面", "c　かわりに"],
        "b",
        "親切の裏にあるマイナス面なので「反面」。",
        "Flip side of kindness: '反面'."
    ),
    make_star(
        416, "3課・4課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>人気<rt>にんき</rt></ruby>がある。",
        ["1　学者というより", "2　タレントとして", "3　テレビの", "4　むしろ"],
        [1, 4, 3, 2], 3, "3",
        "<ruby>彼<rt>かれ</rt></ruby>は学者というよりむしろテレビのタレントとして人気がある。",
        "He is popular more as a television personality rather than as a scholar.",
        "「学者というより(1) むしろ(4) テレビの(3) タレントとして(2)」。★は3。",
        "Order is 1 -> 4 -> 3 -> 2, star is 3."
    ),
    make_star(
        417, "3課・4課 練習",
        "<ruby>自分<rt>じぶん</rt></ruby>で　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>料理<rt>りょうり</rt></ruby>はない。",
        ["1　作った", "2　ほど", "3　おいしい", "4　料理"],
        [1, 4, 2, 3], 2, "2",
        "<ruby>自分<rt>じぶん</rt></ruby>で作った料理ほどおいしい料理はない。",
        "Nothing tastes as delicious as a meal made by oneself.",
        "「作った(1) 料理(4) ほど(2) おいしい(3) 料理はない」。★は2。",
        "Order is 1 -> 4 -> 2 -> 3, star is 2."
    ),
    make_star(
        418, "3課・4課 練習",
        "<ruby>無理<rt>むり</rt></ruby>をして　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>休<rt>やす</rt></ruby>んだほうがいい。",
        ["1　くらいなら", "2　病気になってしまう", "3　会社を", "4　働く"],
        [4, 2, 1, 3], 1, "1",
        "<ruby>無理<rt>むり</rt></ruby>をして働いて病気になってしまうくらいなら会社を休んだほうがいい。",
        "Rather than overworking and falling ill, you should take time off work.",
        "「働いて(4) 病気になってしまう(2) くらいなら(1) 会社を(3) 休んだほうがいい」。★は1。",
        "Order gives 1 at the star position."
    )
]

# ==============================================================================
# REVIEW TEST 1 (まとめ問題 1〜4課, Q1-13)
# ==============================================================================
review_test_1_drills = [
    make_mc(
        451, "まとめ問題 1〜4課",
        "<ruby>熱<rt>ねつ</rt></ruby>が（　　）うちに、<ruby>病院<rt>びょういん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったほうがいい。",
        ["1　ある", "2　あった", "3　あがる", "4　あがらない"],
        "3",
        "熱があがる（高くなる）前に病院へ行くべきという意味。",
        "Go to the doctor before the fever rises."
    ),
    make_mc(
        452, "まとめ問題 1〜4課",
        "<ruby>部長<rt>ぶちょう</rt></ruby>が（　　）とおりに、<ruby>企画書<rt>きかくしょ</rt></ruby>を<ruby>修正<rt>しゅうせい</rt></ruby>した。",
        ["1　指示する", "2　指示して", "3　指示の", "4　指示した"],
        "4",
        "「部長が指示したとおりに」た形接続。",
        "Ta-form connection: '指示したとおりに'."
    ),
    make_mc(
        453, "まとめ問題 1〜4課",
        "<ruby>声<rt>こえ</rt></ruby>が（　　）くらい、<ruby>大声<rt>おおごえ</rt></ruby>で<ruby>応援<rt>おうえん</rt></ruby>した。",
        ["1　枯れて", "2　枯れる", "3　枯れた", "4　枯れよう"],
        "2",
        "程度の極端さを表す「枯れるくらい」。",
        "Extreme degree: '枯れるくらい'."
    ),
    make_mc(
        454, "まとめ問題 1〜4課",
        "<ruby>彼<rt>かれ</rt></ruby>は<ruby>仕事<rt>しごと</rt></ruby>が<ruby>速<rt>はや</rt></ruby>いの（　　）、ミスも<ruby>多<rt>おお</rt></ruby>い。",
        ["1　にとって", "2　に対して", "3　反面", "4　かわりに"],
        "2",
        "速いのに対してミスが多いという対比関係。",
        "Contrast: 'に対して'."
    ),
    make_mc(
        455, "まとめ問題 1〜4課",
        "<ruby>散歩<rt>さんぽ</rt></ruby>の（　　）に、ポストに<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>投函<rt>とうかん</rt></ruby>した。",
        ["1　ついで", "2　あいだ", "3　たび", "4　ほど"],
        "1",
        "散歩の機会を利用したので「ついでに」。",
        "Taking the opportunity: 'ついでに'."
    ),
    make_mc(
        456, "まとめ問題 1〜4課",
        "<ruby>彼<rt>かれ</rt></ruby>に<ruby>謝<rt>あやま</rt></ruby>る（　　）なら、<ruby>絶交<rt>ぜっこう</rt></ruby>したほうがいい。",
        ["1　くらい", "2　ほど", "3　とおり", "4　ばかり"],
        "1",
        "「〜くらいなら…ほうがいい」。",
        "Pattern 'くらいなら'."
    ),
    make_mc(
        457, "まとめ問題 1〜4課",
        "<ruby>夏<rt>なつ</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>は、冷たいビールに（　　）。",
        ["1　かぎらない", "2　限る", "3　ほどだ", "4　反面だ"],
        "2",
        "「〜に限る」で最高を主張する。",
        "'〜に限る' asserts the best choice."
    ),
    make_mc(
        458, "まとめ問題 1〜4課",
        "<ruby>使<rt>つか</rt></ruby>えば<ruby>使<rt>つか</rt></ruby>う（　　）、<ruby>愛着<rt>あいちゃく</rt></ruby>が<ruby>湧<rt>わ</rt></ruby>いてくる。",
        ["1　ついでに", "2　とおりに", "3　ほど", "4　うちに"],
        "3",
        "「〜ば〜ほど」比例構文。",
        "Proportional pattern 'ほど'."
    ),
    make_mc(
        459, "まとめ問題 1〜4課",
        "<ruby>契約書<rt>けいやくしょ</rt></ruby>をよく（　　）からでないと、サインできない。",
        ["1　読んだ", "2　読む", "3　読んで", "4　読まない"],
        "3",
        "「V-て形＋からでないと」。",
        "Form '読んでからでないと'."
    ),
    make_mc(
        460, "まとめ問題 1〜4課",
        "<ruby>兄<rt>あに</rt></ruby>は<ruby>几帳面<rt>きちょうめん</rt></ruby>な（　　）、<ruby>弟<rt>おとうと</rt></ruby>は大雑把だ。",
        ["1　のに対して", "2　反面", "3　かわりに", "4　ほど"],
        "1",
        "二人の対比なので「のに対して」。",
        "Contrast: 'のに対して'."
    ),
    make_star(
        461, "まとめ問題 1〜4課",
        "<ruby>彼女<rt>かのじょ</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>泣<rt>な</rt></ruby>き<ruby>出<rt>だ</rt></ruby>してしまった。",
        ["1　声も", "2　出ない", "3　ほど", "4　悔しがって"],
        [4, 1, 2, 3], 4, "4",
        "<ruby>彼女<rt>かのじょ</rt></ruby>は悔しがって声も出ないほど泣き出してしまった。",
        "She was so frustrated that, unable to even speak, she burst into tears.",
        "「悔しがって(4) 声も(1) 出ない(2) ほど(3)」。★は4。",
        "Order places 4 at the star position."
    ),
    make_star(
        462, "まとめ問題 1〜4課",
        "<ruby>健康<rt>けんこう</rt></ruby>で　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>幸<rt>しあわ</rt></ruby>せなことはない。",
        ["1　暮らせる", "2　ほど", "3　毎日を", "4　こと"],
        [3, 1, 4, 2], 2, "2",
        "<ruby>健康<rt>けんこう</rt></ruby>で毎日を暮らせることほど幸せなことはない。",
        "There is nothing happier than being able to live each day in good health.",
        "「毎日を(3) 暮らせる(1) こと(4) ほど(2)」。★は2。",
        "Order puts 2 at the star position."
    ),
    make_star(
        463, "まとめ問題 1〜4課",
        "<ruby>自分<rt>じぶん</rt></ruby>の　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>後悔<rt>こうかい</rt></ruby>はしない。",
        ["1　選んだ", "2　道なら", "3　失敗しても", "4　とおりに"],
        [4, 1, 2, 3], 1, "1",
        "<ruby>自分<rt>じぶん</rt></ruby>のとおりに選んだ道なら失敗しても後悔はしない。",
        "If it is a path chosen according to my own will, I will have no regrets even if I fail.",
        "「とおりに(4) 選んだ(1) 道なら(2) 失敗しても(3)」。★は1。",
        "Order puts 1 at the star position."
    )
]

# ==============================================================================
# SECTION 5 (5課 〜だから)
# ==============================================================================
sec5_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜ため（に）",
        "pattern_name_en": "because of / due to",
        "meaning_ja": "原因・理由を表す。改まった書き言葉に多い。",
        "meaning_en": "Expresses a formal cause or reason ('because of...', 'due to...'). Often used in news and formal writing.",
        "connection_forms": [
            "普通形（Naな / Naである・Nの / Nである） + ため（に）"
        ],
        "nuance_notes": "話者の希望・意志・依頼などの働きかけの文（〜してください、〜したい）は後ろ件に来ない。客観的な因果関係を述べる。",
        "example_sentences": [
            {
                "japanese": "<ruby>大雪<rt>おおゆき</rt></ruby>のため、<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まっています。",
                "english": "Trains are stopped due to heavy snow."
            },
            {
                "japanese": "<ruby>事故<rt>じこ</rt></ruby>が<ruby>起<rt>お</rt></ruby>きたため、<ruby>道路<rt>どうろ</rt></ruby>が<ruby>渋滞<rt>じゅうたい</rt></ruby>している。",
                "english": "Because an accident occurred, the road is congested."
            },
            {
                "japanese": "<ruby>台風<rt>たいふう</rt></ruby>の<ruby>接近<rt>せっきん</rt></ruby>のために、<ruby>試合<rt>しあい</rt></ruby>が<ruby>中止<rt>ちゅうし</rt></ruby>となった。",
                "english": "Due to the approaching typhoon, the match was called off."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜によって・〜による",
        "pattern_name_en": "caused by / due to / through",
        "meaning_ja": "原因・理由・手段を表す。〜による＋名詞の形もある。",
        "meaning_en": "Expresses cause, reason, or means. Modifies nouns in the form '〜による + Noun'.",
        "connection_forms": [
            "N + によって",
            "N + による + N"
        ],
        "nuance_notes": "災害、事故、事件などの重大な原因や公的な事態の説明に頻出する硬い表現。",
        "example_sentences": [
            {
                "japanese": "<ruby>地震<rt>じしん</rt></ruby>によって、<ruby>多<rt>おお</rt></ruby>くの<ruby>家屋<rt>かおく</rt></ruby>が<ruby>倒壊<rt>とうかい</rt></ruby>した。",
                "english": "Due to the earthquake, many houses collapsed."
            },
            {
                "japanese": "<ruby>不注意<rt>ふちゅうい</rt></ruby>による<ruby>事故<rt>じこ</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐ。",
                "english": "Prevent accidents caused by carelessness."
            },
            {
                "japanese": "インターネットの<ruby>普及<rt>ふきゅう</rt></ruby>によって、<ruby>生活<rt>せいかつ</rt></ruby>が<ruby>便利<rt>べんり</rt></ruby>になった。",
                "english": "Through the spread of the internet, life has become convenient."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜から・〜ことから",
        "pattern_name_en": "from the fact that / judged from",
        "meaning_ja": "〜という事実・根拠に基づいて、判断したり名前がついたりする。",
        "meaning_en": "Expresses that a fact serves as the origin, reason for naming, or basis of judgment.",
        "connection_forms": [
            "普通形（Naな / Naである・Nである） + ことから",
            "N + から"
        ],
        "nuance_notes": "由来（名前の由来など）や客観的な判断根拠（〜と判断される、〜と呼ばれる）を示す文脈で多用される。",
        "example_sentences": [
            {
                "japanese": "<ruby>道<rt>みち</rt></ruby>が<ruby>濡<rt>ぬ</rt></ruby>れていることから、<ruby>夜<rt>よる</rt></ruby>の<ruby>間<rt>あいだ</rt></ruby>に<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったことがわかる。",
                "english": "From the fact that the roads are wet, one can tell it rained during the night."
            },
            {
                "japanese": "<ruby>富士山<rt>ふじさん</rt></ruby>が<ruby>見<rt>み</rt></ruby>えることから、「<ruby>富士見町<rt>ふじみちょう</rt></ruby>」と<ruby>名付<rt>なづ</rt></ruby>けられた。",
                "english": "It was named 'Fujimi-cho' from the fact that Mt. Fuji is visible."
            },
            {
                "japanese": "<ruby>声<rt>こえ</rt></ruby>が<ruby>震<rt>ふる</rt></ruby>えていることから、<ruby>彼<rt>かれ</rt></ruby>の<ruby>緊張<rt>きんちょう</rt></ruby>が<ruby>伝<rt>つた</rt></ruby>わってきた。",
                "english": "From the trembling of his voice, his nervousness was readily felt."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜おかげだ・〜せいだ",
        "pattern_name_en": "thanks to... / fault of... (blame)",
        "meaning_ja": "おかげ：良い結果をもたらした原因に感謝する。せい：悪い結果をもたらした原因を非難する。",
        "meaning_en": "〜おかげ: expresses gratitude for a positive outcome ('thanks to...'). 〜せい: assigns blame for a negative outcome ('due to the fault of...').",
        "connection_forms": [
            "普通形（Naな・Nの） + おかげだ / おかげで",
            "普通形（Naな・Nの） + せいだ / せいで"
        ],
        "nuance_notes": "皮肉で「〜のおかげで（ひどい目にあった）」と言うこともあるが、基本規則はおかげ＝好結果、せい＝悪結果。",
        "example_sentences": [
            {
                "japanese": "<ruby>先生<rt>せんせい</rt></ruby>のおかげで、<ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>できました。",
                "english": "Thanks to the teacher, I was able to pass the exam."
            },
            {
                "japanese": "<ruby>寝坊<rt>ねぼう</rt></ruby>したせいで、<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>り<ruby>遅<rt>おく</rt></ruby>れてしまった。",
                "english": "Because I overslept, I ended up missing the train."
            },
            {
                "japanese": "<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだおかげで、<ruby>熱<rt>ねつ</rt></ruby>が<ruby>下<rt>さ</rt></ruby>がった。",
                "english": "Thanks to taking the medicine, my fever went down."
            }
        ]
    },
    {
        "pattern_number": 5,
        "pattern_name": "〜のだから・〜んだから",
        "pattern_name_en": "since... naturally / as you know",
        "meaning_ja": "相手も知っている当然の事実を理由にして、主張・催促・助言などを述べる。",
        "meaning_en": "States a shared, obvious fact as a given premise to justify an advice, encouragement, or inevitable conclusion.",
        "connection_forms": [
            "普通形（Naな・Nな） + のだから / んだから"
        ],
        "nuance_notes": "後件には話者の意志、勧め、判断、命令などが来ることが多い（「〜のは当然だ」「〜しなさい」など）。",
        "example_sentences": [
            {
                "japanese": "もう<ruby>子供<rt>こども</rt></ruby>じゃないんだから、<ruby>自分<rt>じぶん</rt></ruby>のことは<ruby>自分<rt>じぶん</rt></ruby>でやりなさい。",
                "english": "Since you're not a child anymore, do your own things yourself."
            },
            {
                "japanese": "<ruby>一生懸命<rt>いっしょうけんめい</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>したのだから、きっと<ruby>勝<rt>か</rt></ruby>てるよ。",
                "english": "Since you practiced so hard, you will surely win."
            },
            {
                "japanese": "<ruby>高<rt>たか</rt></ruby>いお<ruby>金<rt>かね</rt></ruby>を<ruby>払<rt>はら</rt></ruby>ったんだから、<ruby>元<rt>もと</rt></ruby>を<ruby>取<rt>と</rt></ruby>らないともったいない。",
                "english": "Since we paid a lot of money, it's a waste if we don't get our money's worth."
            }
        ]
    }
]

# Section 5 drills (5課 練習 Q1-9)
sec5_drills = [
    make_mc(
        501, "5課 練習",
        "<ruby>台風<rt>たいふう</rt></ruby>の（　　）、<ruby>飛行機<rt>ひこうき</rt></ruby>が<ruby>欠航<rt>けっこう</rt></ruby>になった。",
        ["a　おかげで", "b　ため", "c　こと"],
        "b",
        "台風という客観的原因により欠航になったので「ため」。",
        "Objective cause of flight cancellation: 'ため'."
    ),
    make_mc(
        502, "5課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>の（　　）、みんなが<ruby>迷惑<rt>めいわく</rt></ruby>した。",
        ["a　せいで", "b　おかげで", "c　ために"],
        "a",
        "迷惑という悪い結果を招いたので「せいで」。",
        "Blame for negative outcome: 'せいで'."
    ),
    make_mc(
        503, "5課 練習",
        "<ruby>毎日<rt>まいにち</rt></ruby><ruby>練習<rt>れんしゅう</rt></ruby>した（　　）、<ruby>合格<rt>ごうかく</rt></ruby>できた。",
        ["a　おかげで", "b　せいで", "c　ことから"],
        "a",
        "合格という良い結果なので「おかげで」。",
        "Gratitude for passing: 'おかげで'."
    ),
    make_mc(
        504, "5課 練習",
        "<ruby>地震<rt>じしん</rt></ruby>（　　）<ruby>被害<rt>ひがい</rt></ruby>が<ruby>広<rt>ひろ</rt></ruby>がった。",
        ["a　による", "b　によって", "c　のために"],
        "a",
        "名詞「被害」を修飾するので「地震による被害」。",
        "Modifying noun '被害': 'による'."
    ),
    make_mc(
        505, "5課 練習",
        "<ruby>星<rt>ほし</rt></ruby>がよく<ruby>見<rt>み</rt></ruby>える（　　）、「<ruby>星見台<rt>ほしみだい</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>ばれる。",
        ["a　おかげで", "b　せいで", "c　ことから"],
        "c",
        "地名の由来・根拠を表すので「ことから」。",
        "Origin / naming justification: 'ことから'."
    ),
    make_mc(
        506, "5課 練習",
        "もう<ruby>大人<rt>おとな</rt></ruby>な（　　）、<ruby>責任<rt>せきにん</rt></ruby>を<ruby>持<rt>も</rt></ruby>ちなさい。",
        ["a　ために", "b　せいで", "c　んだから"],
        "c",
        "既知の当然の前提からの催促・忠告なので「んだから」。",
        "Given obvious premise: 'んだから'."
    ),
    make_mc(
        507, "5課 練習",
        "<ruby>長雨<rt>ながあめ</rt></ruby>の（　　）、<ruby>野菜<rt>やさい</rt></ruby>が<ruby>高騰<rt>こうとう</rt></ruby>した。",
        ["a　ため", "b　おかげで", "c　ことによって"],
        "a",
        "名詞「長雨」＋のため。",
        "Noun connection: '長雨のため'."
    ),
    make_mc(
        508, "5課 練習",
        "<ruby>君<rt>きみ</rt></ruby>が<ruby>応援<rt>おうえん</rt></ruby>してくれた（　　）、<ruby>頑張<rt>がんば</rt></ruby>れたよ。",
        ["a　せいで", "b　おかげで", "c　ことから"],
        "b",
        "励ましへの感謝を表す「おかげで」。",
        "Gratitude: 'おかげで'."
    ),
    make_mc(
        509, "5課 練習",
        "<ruby>火災<rt>かさい</rt></ruby>（　　）煙が<ruby>立<rt>た</rt></ruby>ち<ruby>込<rt>こ</rt></ruby>めた。",
        ["a　によって", "b　による", "c　のおかげで"],
        "a",
        "原因「火災によって」。",
        "Cause: '火災によって'."
    )
]

# ==============================================================================
# SECTION 6 (6課 もし、…)
# ==============================================================================
sec6_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜（の）なら",
        "pattern_name_en": "if it is the case that / if you are going to",
        "meaning_ja": "相手の話や状況を前提・条件として受けて、話者の判断・助言・要求を述べる。",
        "meaning_en": "Accepts a situation or the interlocutor's statement as a premise to give advice, opinion, or request ('if that's the case, then...').",
        "connection_forms": [
            "普通形（Naなら / Naであるなら・Nなら / Nであるなら） + なら",
            "動詞・形容詞 + のなら"
        ],
        "nuance_notes": "後件には話者の判断・忠告・希望が来やすい。これからする行動（後）について、先に準備する文脈でも使われる（日本へ行くなら、カメラを買ったほうがいい）。",
        "example_sentences": [
            {
                "japanese": "<ruby>京都<rt>きょうと</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くなら、<ruby>新幹線<rt>しんかんせん</rt></ruby>が<ruby>便利<rt>べんり</rt></ruby>ですよ。",
                "english": "If you're going to Kyoto, the Shinkansen is very convenient."
            },
            {
                "japanese": "<ruby>嫌<rt>いや</rt></ruby>なら、<ruby>無理<rt>むり</rt></ruby>に<ruby>食<rt>た</rt></ruby>べなくてもいいですよ。",
                "english": "If you dislike it, you don't have to force yourself to eat it."
            },
            {
                "japanese": "<ruby>彼<rt>かれ</rt></ruby>がそう<ruby>言<rt>い</rt></ruby>うのなら、<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いない。",
                "english": "If he says so, it must definitely be true."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜ては・〜（の）では",
        "pattern_name_en": "if... then (bad result / cannot continue)",
        "meaning_ja": "もしそのような状態になったら・していたら、困った結果になる。",
        "meaning_en": "Hypothesizes an undesirable condition or repeated action that leads to bad consequences ('if this keeps happening, it will be trouble').",
        "connection_forms": [
            "V-て形 + は",
            "A-く + ては",
            "Na-で + は",
            "N-で + は",
            "普通形 + のでは"
        ],
        "nuance_notes": "後件には必ず否定的な結果や「〜困る」「〜できない」「〜大変だ」などが来る。",
        "example_sentences": [
            {
                "japanese": "そんなに<ruby>遊<rt>あそ</rt></ruby>んでばかりいては、<ruby>試験<rt>しけん</rt></ruby>に<ruby>落<rt>お</rt></ruby>ちてしまうよ。",
                "english": "If you keep playing around like that, you'll fail the exam."
            },
            {
                "japanese": "<ruby>雨<rt>あめ</rt></ruby>がこんなに<ruby>強<rt>つよ</rt></ruby>くては、<ruby>出<rt>で</rt></ruby>かけられない。",
                "english": "If the rain is this heavy, we can't go out."
            },
            {
                "japanese": "<ruby>毎日<rt>まいにち</rt></ruby>こんなに<ruby>残業<rt>ざんぎょう</rt></ruby>があっては、<ruby>体<rt>からだ</rt></ruby>がもたない。",
                "english": "If there's this much overtime every day, my body won't hold up."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜さえ〜ば・〜さえ〜なら",
        "pattern_name_en": "if only... / as long as...",
        "meaning_ja": "その最低限の条件一つが成り立ちさえすれば、他は問題ない・十分だ。",
        "meaning_en": "Expresses that one sole, minimum condition is all that is required for success ('if only...', 'as long as...').",
        "connection_forms": [
            "N + さえ + V-ば / A-ければ / Na-なら",
            "V-ます語幹 + さえすれば",
            "V-て + さえいれば"
        ],
        "nuance_notes": "「これさえあれば、他には何もいらない」という唯一・必須の条件を提示する。",
        "example_sentences": [
            {
                "japanese": "お<ruby>金<rt>かね</rt></ruby>さえあれば、<ruby>何<rt>なに</rt></ruby>でも<ruby>買<rt>か</rt></ruby>えるというわけではない。",
                "english": "It doesn't mean you can buy anything as long as you have money."
            },
            {
                "japanese": "<ruby>体<rt>からだ</rt></ruby>さえ<ruby>健康<rt>けんこう</rt></ruby>なら、どんなことも<ruby>乗<rt>の</rt></ruby>り<ruby>越<rt>こ</rt></ruby>えられる。",
                "english": "As long as one is healthy, any hardship can be overcome."
            },
            {
                "japanese": "<ruby>時間<rt>じかん</rt></ruby>さえあれば、もっとゆっくり<ruby>旅行<rt>りょこう</rt></ruby>できたのに。",
                "english": "If only we had time, we could have traveled more leisurely."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜たとえ〜ても・〜たとえ〜でも",
        "pattern_name_en": "even if... / even supposing that...",
        "meaning_ja": "仮に極端な条件が生じても、結論や決意は変わらない。",
        "meaning_en": "Even if an extreme hypothetical situation were to occur, the outcome or resolve remains unaltered ('even if...').",
        "connection_forms": [
            "たとえ + V-て形 + も",
            "たとえ + A-く + ても",
            "たとえ + Na-で + も",
            "たとえ + N-で + も"
        ],
        "nuance_notes": "強い決意、原則、普遍的な心理を述べる。「たとえ」は省略されることもあるが、強調のために呼応する。",
        "example_sentences": [
            {
                "japanese": "たとえ<ruby>失敗<rt>しっぱい</rt></ruby>しても、<ruby>諦<rt>あきら</rt></ruby>めずにやり<ruby>直<rt>なお</rt></ruby>す。",
                "english": "Even if I fail, I will not give up and will start over."
            },
            {
                "japanese": "たとえ<ruby>両親<rt>りょうしん</rt></ruby>に<ruby>反対<rt>はんたい</rt></ruby>されても、<ruby>彼<rt>かれ</rt></ruby>と<ruby>結婚<rt>けっこん</rt></ruby>したい。",
                "english": "Even if my parents oppose it, I want to marry him."
            },
            {
                "japanese": "たとえ<ruby>給料<rt>きゅうりょう</rt></ruby>が<ruby>安<rt>やす</rt></ruby>くても、やりがいのある<ruby>仕事<rt>しごと</rt></ruby>がしたい。",
                "english": "Even if the salary is low, I want to do rewarding work."
            }
        ]
    },
    {
        "pattern_number": 5,
        "pattern_name": "〜ば…・〜たら…・〜なら…（事実と反対の仮定）",
        "pattern_name_en": "if only... (counterfactual conditional)",
        "meaning_ja": "実際はそうではなかったが、もしそうだったら…（反実仮想・後悔・残念な気持ち）。",
        "meaning_en": "Expresses counterfactual conditionals indicating regret or relief about an unrealized past situation ('if only X had happened, Y would have...').",
        "connection_forms": [
            "V-ば / A-ければ / Na・N-なら + よかった（のに）",
            "V-たら / A-かったら + よかった（のに）"
        ],
        "nuance_notes": "「〜のに」「〜のだが」などを伴って、現実とは異なる結果への未練や後悔を強くにじませる。",
        "example_sentences": [
            {
                "japanese": "もっと<ruby>早<rt>はや</rt></ruby>く<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>ていれば、<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>ったのに。",
                "english": "If only I had left home earlier, I would have caught the train in time."
            },
            {
                "japanese": "あのとき<ruby>彼<rt>かれ</rt></ruby>の<ruby>忠告<rt>ちゅうこく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いていれば、こんなことにはならなかった。",
                "english": "If I had listened to his advice back then, this wouldn't have happened."
            },
            {
                "japanese": "<ruby>昨日<rt>きのう</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>らなければ、バーベキューができたのに。",
                "english": "If it hadn't rained yesterday, we could have had a barbecue."
            }
        ]
    }
]

# Section 6 drills (6課 練習 Q1-8, plus 5課・6課 combined Q1-10)
sec6_drills = [
    make_mc(
        601, "6課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>が（　　）なら、<ruby>私<rt>わたし</rt></ruby>も<ruby>行<rt>い</rt></ruby>きません。",
        ["a　行かない", "b　行かないの", "c　行かない"],
        "c",
        "公式解答 c。",
        "Option c as keyed."
    ),
    make_mc(
        602, "6課 練習",
        "<ruby>天候<rt>てんこう</rt></ruby>が（　　）ては、<ruby>登山<rt>とざん</rt></ruby>は<ruby>危険<rt>きけん</rt></ruby>だ。",
        ["a　悪く", "b　悪くて", "c　悪い"],
        "a",
        "い形容詞「悪くては」の接続形「悪く」。",
        "Adjective te-form connection: '悪くては'."
    ),
    make_mc(
        603, "6課 練習",
        "<ruby>健康<rt>けんこう</rt></ruby>（　　）あれば、ほかに<ruby>望<rt>のぞ</rt></ruby>むものはない。",
        ["a　なら", "b　でさえ", "c　さえ"],
        "b",
        "名詞「健康でさえあれば」。",
        "Noun connection: '健康でさえあれば'."
    ),
    make_mc(
        604, "6課 練習",
        "たとえ（　　）ても、<ruby>約束<rt>やくそく</rt></ruby>は<ruby>守<rt>まも</rt></ruby>るべきだ。",
        ["a　忙しい", "b　忙しく", "c　忙しかった"],
        "b",
        "い形容詞「たとえ忙しくても」。",
        "Adjective te-form: '忙しくても'."
    ),
    make_mc(
        605, "6課 練習",
        "もっと<ruby>安<rt>やす</rt></ruby>（　　）ば、<ruby>買<rt>か</rt></ruby>ったのに。",
        ["a　い", "b　けれ", "c　かっ"],
        "b",
        "い形容詞ば形「安ければ」。",
        "Ba-form: '安ければ'."
    ),
    make_mc(
        606, "6課 練習",
        "<ruby>君<rt>きみ</rt></ruby>が（　　）さえすれば、うまくいくよ。",
        ["a　やり", "b　やる", "c　やって"],
        "a",
        "ます形語幹「やりさえすれば」。",
        "Masu stem: 'やりさえすれば'."
    ),
    make_mc(
        607, "6課 練習",
        "こんなに<ruby>散<rt>ち</rt></ruby>らかって（　　）、<ruby>勉強<rt>べんきょう</rt></ruby>に<ruby>集中<rt>しゅうちゅう</rt></ruby>できない。",
        ["a　なら", "b　さえ", "c　いては"],
        "c",
        "「〜ていては」で好ましくない条件を示す。",
        "Negative condition: '散らかっていては'."
    ),
    make_mc(
        608, "6課 練習",
        "<ruby>薬<rt>くすり</rt></ruby>を（　　）たら、すぐに<ruby>治<rt>なお</rt></ruby>ったのに。",
        ["a　飲む", "b　飲ん", "c　飲んだら"],
        "c",
        "公式解答 c。",
        "Option c as keyed."
    ),
    # 5課・6課 まとまりの練習
    make_mc(
        609, "5課・6課 練習",
        "<ruby>急<rt>いそ</rt></ruby>な<ruby>用事<rt>ようじ</rt></ruby>の（　　）、<ruby>欠席<rt>けっせき</rt></ruby>いたします。",
        ["a　おかげで", "b　ため", "c　せいで"],
        "b",
        "改まった欠席理由の表現「用事のため」。",
        "Formal reason: '用事のため'."
    ),
    make_mc(
        610, "5課・6課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>が<ruby>手伝<rt>てつだ</rt></ruby>ってくれた（　　）、<ruby>早<rt>はや</rt></ruby>く<ruby>終<rt>お</rt></ruby>わった。",
        ["a　せいで", "b　ことから", "c　おかげで"],
        "c",
        "手助けへの感謝を表す「おかげで」。",
        "Gratitude: 'おかげで'."
    ),
    make_mc(
        611, "5課・6課 練習",
        "<ruby>自分<rt>じぶん</rt></ruby>で<ruby>決<rt>き</rt></ruby>めた（　　）、最後までやりなさい。",
        ["a　んだから", "b　せいで", "c　ために"],
        "a",
        "当然の理由からの指示「んだから」。",
        "Given premise: 'んだから'."
    ),
    make_mc(
        612, "5課・6課 練習",
        "<ruby>無理<rt>むり</rt></ruby>をして（　　）、<ruby>体<rt>からだ</rt></ruby>を<ruby>壊<rt>こわ</rt></ruby>してしまうよ。",
        ["a　いても", "b　いさえすれば", "c　いては"],
        "c",
        "好ましくない事態の継続「無理をしていては」。",
        "Negative conditional: '無理をしていては'."
    ),
    make_mc(
        613, "5課・6課 練習",
        "<ruby>準備<rt>じゅんび</rt></ruby>（　　）しておけば、<ruby>安心<rt>あんしん</rt></ruby>だ。",
        ["a　でも", "b　さえ", "c　なら"],
        "b",
        "最低限の条件「準備さえしておけば」。",
        "Sole condition: '準備さえ'."
    ),
    make_mc(
        614, "5課・6課 練習",
        "たとえ<ruby>雨<rt>あめ</rt></ruby>が（　　）、<ruby>出発<rt>しゅっぱつ</rt></ruby>します。",
        ["a　降れば", "b　降っても", "c　降るなら"],
        "b",
        "「たとえ〜ても」。",
        "Concession: 'たとえ降っても'."
    ),
    make_mc(
        615, "5課・6課 練習",
        "<ruby>地図<rt>ちず</rt></ruby>を<ruby>持<rt>も</rt></ruby>って（　　）、<ruby>道<rt>みち</rt></ruby>に<ruby>迷<rt>まよ</rt></ruby>わなかったのに。",
        ["a　くれば", "b　きていれば", "c　きたらば"],
        "b",
        "反実仮想「持ってきていれば」。",
        "Counterfactual: '持ってきていれば'."
    ),
    make_star(
        616, "5課・6課 練習",
        "<ruby>彼<rt>かれ</rt></ruby>の　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>助<rt>たす</rt></ruby>かった。",
        ["1　的確な", "2　おかげで", "3　アドバイスの", "4　本当に"],
        [1, 3, 2, 4], 2, "2",
        "<ruby>彼<rt>かれ</rt></ruby>の的確なアドバイスのおかげで本当に助かった。",
        "Thanks to his precise advice, I was truly saved.",
        "「的確な(1) アドバイスの(3) おかげで(2) 本当に(4) 助かった」。★は2。",
        "Star is at position 2."
    ),
    make_star(
        617, "5課・6課 練習",
        "<ruby>時間<rt>じかん</rt></ruby>が　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>行<rt>い</rt></ruby>きたい。",
        ["1　許す", "2　旅行に", "3　のなら", "4　ぜひ"],
        [1, 3, 4, 2], 4, "4",
        "<ruby>時間<rt>じかん</rt></ruby>が許すのならぜひ旅行に行きたい。",
        "If time permits, I definitely want to go on a trip.",
        "「許す(1) のなら(3) ぜひ(4) 旅行に(2) 行きたい」。★は4。",
        "Star is option 4 (keyed answer b in 4-choice layout, which maps to 1:a, 2:b, 3:c, 4:d).",
    ),
    make_star(
        618, "5課・6課 練習",
        "<ruby>君<rt>きみ</rt></ruby>が　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>文句<rt>もんく</rt></ruby>はない。",
        ["1　賛成して", "2　さえ", "3　何も", "4　くれれば"],
        [1, 2, 4, 3], 2, "2",
        "<ruby>君<rt>きみ</rt></ruby>が賛成してさえくれれば何も文句はない。",
        "As long as you agree, I have no complaints whatsoever.",
        "「賛成して(1) さえ(2) くれれば(4) 何も(3) 文句はない」。★は2。",
        "Star is at position 2 (keyed answer b)."
    )
]

# Assemble the sections data structure
sections_data = [
    {
        "section_number": 1,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>課<rt>か</rt></ruby> 〜とき",
        "title_en": "Lesson 1: Time & Timing",
        "theme": "<ruby>時<rt>とき</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec1_patterns,
        "drills": sec1_drills
    },
    {
        "section_number": 2,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>課<rt>か</rt></ruby> 〜<ruby>関係<rt>かんけい</rt></ruby>して",
        "title_en": "Lesson 2: In Relation / Proportions / Opportunities",
        "theme": "<ruby>関連<rt>かんれん</rt></ruby>・<ruby>比例<rt>ひれい</rt></ruby>・ついでを<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec2_patterns,
        "drills": sec2_drills
    },
    {
        "section_number": 3,
        "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>課<rt>か</rt></ruby> <ruby>比<rt>くら</rt></ruby>べれば…・〜がいちばん",
        "title_en": "Lesson 3: Comparison, Extreme Degree & The Best Choice",
        "theme": "<ruby>比較<rt>ひかく</rt></ruby>・<ruby>程度<rt>ていど</rt></ruby>・<ruby>最高<rt>さいこう</rt></ruby>の<ruby>選択<rt>せんたく</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec3_patterns,
        "drills": sec3_drills
    },
    {
        "section_number": 4,
        "title": "<ruby>第<rt>だい</rt></ruby>4<ruby>課<rt>か</rt></ruby> 〜とは<ruby>違<rt>ちが</rt></ruby>って",
        "title_en": "Lesson 4: Contrast, Opposing Aspects & Alternates",
        "theme": "<ruby>対比<rt>たいひ</rt></ruby>・<ruby>裏表<rt>うらおもて</rt></ruby>・<ruby>代償<rt>だいしょう</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec4_patterns,
        "drills": sec4_drills + review_test_1_drills
    },
    {
        "section_number": 5,
        "title": "<ruby>第<rt>だい</rt></ruby>5<ruby>課<rt>か</rt></ruby> 〜だから",
        "title_en": "Lesson 5: Causes, Reasons & Grounds",
        "theme": "<ruby>原因<rt>げんいん</rt></ruby>・<ruby>理由<rt>りゆう</rt></ruby>・<ruby>根拠<rt>こんきょ</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec5_patterns,
        "drills": sec5_drills
    },
    {
        "section_number": 6,
        "title": "<ruby>第<rt>だい</rt></ruby>6<ruby>課<rt>か</rt></ruby> もし、…",
        "title_en": "Lesson 6: Conditions, Hypotheses & Counterfactuals",
        "theme": "<ruby>条件<rt>じょうけん</rt></ruby>・<ruby>仮定<rt>かてい</rt></ruby>・<ruby>反実仮想<rt>はんじつかそう</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>表現<rt>ひょうげん</rt></ruby>",
        "patterns": sec6_patterns,
        "drills": sec6_drills
    }
]

final_output = {
    "metadata": {
        "book_title": "<ruby>新完全<rt>しんかんぜん</rt></ruby>マスター<ruby>文法<rt>ぶんぽう</rt></ruby> <ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby> N3",
        "part_number": 1,
        "part_name": "<ruby>実力養成編<rt>じつりょくようせいへん</rt></ruby> <ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>1",
        "part_name_en": "Part 1: Sentence Grammar 1 (Meaning & Function)",
        "sections_included": [1, 2, 3, 4, 5, 6],
        "pages_covered": "p.15 - p.35 (Images 019-039)"
    },
    "sections": sections_data
}

target_file = Path("nihongo-intermediate/data/grammar/part1_sec1_to_6.json")
target_file.parent.mkdir(parents=True, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_file}")
