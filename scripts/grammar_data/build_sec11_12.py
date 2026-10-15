# -*- coding: utf-8 -*-
"""
Section 11 and Section 12 data for Shin Kanzen Master N3 Grammar.
Section 11: 第11課 〜(よ)うと思う (Patterns 1-4, Drills 1-9)
Section 12: 第12課 敬語 (Patterns 1-4, Drills 1-9)
Combined Drills: 練習 11・12課 (Q1-8)
Review Test 3: まとめ問題 1〜12課 (Q1-13)
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

# ==============================================================================
# SECTION 11: 第11課 〜(よ)うと思う
# ==============================================================================
sec11_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜ことにする・〜ことにしている",
        "pattern_name_en": "Decide to do / Make it a rule to do",
        "meaning_ja": "〜と決める。「〜ことにした」はその場の決心や決定、「〜ことにしている」は決心した習慣を続けていることを表す。",
        "meaning_en": "I have decided to do... / Make it a personal rule to do... 〜ことにした expresses a past decision or on-the-spot resolve; 〜ことにしている expresses a sustained personal habit or principle.",
        "connection_forms": [
            "動辞書形 / ている / ない形 ＋ ことにする",
            "動辞書形 / ない形 ＋ ことにしている"
        ],
        "nuance_notes": "話者の主体的な意志による決定を表す。習慣として続けている自己のルールには「〜ことにしている」を使う。",
        "example_sentences": [
            {
                "japanese": "<ruby>冷蔵庫<rt>れいぞうこ</rt></ruby>がこわれたので、<ruby>新<rt>あたら</rt></ruby>しいのを<ruby>買<rt>か</rt></ruby>うことにした。",
                "english": "Since the refrigerator broke, I decided to buy a new one."
            },
            {
                "japanese": "<ruby>口<rt>くち</rt></ruby>を<ruby>出<rt>だ</rt></ruby>すと<ruby>怒<rt>おこ</rt></ruby>られるので、<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わないで<ruby>黙<rt>だま</rt></ruby>っていることにした。",
                "english": "Since interfering gets me scolded, I decided to keep quiet and say nothing."
            },
            {
                "japanese": "<ruby>娘<rt>むすめ</rt></ruby>「お<ruby>父<rt>とう</rt></ruby>さん、<ruby>今度<rt>こんど</rt></ruby>の<ruby>休<rt>やす</rt></ruby>みにディズニーランドに<ruby>連<rt>つ</rt></ruby>れていってよ。」\n<ruby>父<rt>ちち</rt></ruby>「よし、わかった。じゃ、<ruby>友<rt>とも</rt></ruby>だちとゴルフに<ruby>行<rt>い</rt></ruby>く<ruby>約束<rt>やくそく</rt></ruby>は<ruby>断<rt>ことわ</rt></ruby>ることにするよ。」",
                "english": "Daughter: 'Dad, take me to Disneyland next holiday!' Father: 'All right, then I'll decide to cancel my golf plans with my friend.'"
            },
            {
                "japanese": "<ruby>部長<rt>ぶちょう</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>はいつもとてもきびしいが、わたしは<ruby>気<rt>き</rt></ruby>にしないことにしている。",
                "english": "The director's words are always harsh, but I make it a rule not to take them to heart."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜ようにする・〜ようにしている",
        "pattern_name_en": "Try to / Make an effort to",
        "meaning_ja": "〜する／しないことを心がける。努力を続けていることを表す。",
        "meaning_en": "Make an effort to... / Make sure to... Indicates intentional commitment and sustained effort toward a goal or habit.",
        "connection_forms": [
            "動辞書形 / ない形 ＋ ようにする・ようにしている"
        ],
        "nuance_notes": "「〜ようにしている」は現在進行中の継続的な努力・心がけを表す。意志動詞に接続する。",
        "example_sentences": [
            {
                "japanese": "<ruby>水<rt>みず</rt></ruby>や<ruby>電気<rt>でんき</rt></ruby>は<ruby>大切<rt>たいせつ</rt></ruby>に<ruby>使<rt>つか</rt></ruby>うようにしましょう。",
                "english": "Let's make sure to use water and electricity conservatively."
            },
            {
                "japanese": "<ruby>妻<rt>つま</rt></ruby>「あなたの<ruby>帰<rt>かえ</rt></ruby>りが<ruby>毎日<rt>まいにち</rt></ruby><ruby>遅<rt>おそ</rt></ruby>いから、<ruby>子<rt>こ</rt></ruby>どもたちがさびしがっているわ。」\n<ruby>夫<rt>おっと</rt></ruby>「そうか。これからはもっと<ruby>早<rt>はや</rt></ruby>く<ruby>帰<rt>かえ</rt></ruby>るようにするよ。」",
                "english": "Wife: 'The kids feel lonely because you come home late every day.' Husband: 'I see. From now on, I will make an effort to return earlier.'"
            },
            {
                "japanese": "<ruby>集合時間<rt>しゅうごうじかん</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れないようにしてください。",
                "english": "Please make sure not to be late for the meeting time."
            },
            {
                "japanese": "わたしはなるべく<ruby>自分<rt>じぶん</rt></ruby>で<ruby>料理<rt>りょうり</rt></ruby>を<ruby>作<rt>つく</rt></ruby>って<ruby>食<rt>た</rt></ruby>べるようにしている。",
                "english": "I make an effort to cook and eat my own food as much as possible."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜(よ)うとする",
        "pattern_name_en": "Be about to / Try to / Refuse to (in negative)",
        "meaning_ja": "〜を実現させることを試みる。または、行為の直前であることを表す。否定形（〜ようとしない）は全くその意志がないことを表す。",
        "meaning_en": "Be about to do... / Attempt to do... In the negative form (〜ようとしない), expresses total refusal or complete absence of intent by a third person.",
        "connection_forms": [
            "動う・よう形 ＋ とする"
        ],
        "nuance_notes": "「〜ようとしたとき／としたら」は行為直前の契機。「〜ようとしない」の主語は第三者となる。",
        "example_sentences": [
            {
                "japanese": "あの<ruby>子<rt>こ</rt></ruby>は<ruby>一生<rt>いっしょう</rt></ruby>けんめい<ruby>手<rt>て</rt></ruby>を<ruby>伸<rt>の</rt></ruby>ばして、テーブルの<ruby>上<rt>うえ</rt></ruby>のおもちゃを<ruby>取<rt>と</rt></ruby>ろうとしている。",
                "english": "That child is reaching with all his might, trying to grab the toy on the table."
            },
            {
                "japanese": "きのうの<ruby>夜<rt>よる</rt></ruby>は<ruby>眠<rt>ねむ</rt></ruby>ろうとしてもなかなか<ruby>眠<rt>ねむ</rt></ruby>れなかった。",
                "english": "Last night, even though I tried to sleep, I couldn't fall asleep easily."
            },
            {
                "japanese": "<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>ようとしたとき、<ruby>突然<rt>とつぜん</rt></ruby><ruby>大雨<rt>おおあめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。",
                "english": "Just as I was about to leave the house, sudden heavy rain began to fall."
            },
            {
                "japanese": "<ruby>重<rt>おも</rt></ruby>い<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>げようとしたら、<ruby>腰<rt>こし</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>くなってしまった。",
                "english": "Just as I tried to lift the heavy baggage, my lower back hurt."
            },
            {
                "japanese": "いくら<ruby>勧<rt>すす</rt></ruby>めても<ruby>夫<rt>おっと</rt></ruby>は<ruby>病院<rt>びょういん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>こうとしない。",
                "english": "No matter how much I encourage him, my husband shows no intention of going to the hospital."
            },
            {
                "japanese": "<ruby>父<rt>ちち</rt></ruby>に<ruby>事情<rt>じじょう</rt></ruby>を<ruby>説明<rt>せつめい</rt></ruby>しようとしたが、<ruby>父<rt>ちち</rt></ruby>は<ruby>話<rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>こうとはしなかった。",
                "english": "I tried to explain the situation to my father, but he refused to listen."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜つもりだ",
        "pattern_name_en": "Feel as if / Believe that one has done",
        "meaning_ja": "実際はそうではないが、自分では〜の気持ちを持っている。また相手を非難する言い方にもなる。",
        "meaning_en": "Under the impression that... / Believe that one is... In one's mind, one feels or intends it that way, even if objective reality differs. Can also imply criticism.",
        "connection_forms": [
            "普通形（ナ形だ-な・名だ-の） ＋ つもりだ  ＊この使い方は動辞書形・ない形にはつかない"
        ],
        "nuance_notes": "自己の主観的な思い込みを表す。相手に対して「〜たつもりですか」と使うと非難・皮肉になる。",
        "example_sentences": [
            {
                "japanese": "わたしは<ruby>今年<rt>ことし</rt></ruby>77<ruby>歳<rt>さい</rt></ruby>ですが、まだまだ<ruby>若<rt>わか</rt></ruby>いつもりです。",
                "english": "I am 77 years old this year, but I still consider myself young at heart."
            },
            {
                "japanese": "じょうだんで<ruby>言<rt>い</rt></ruby>ったつもりの<ruby>言葉<rt>ことば</rt></ruby>だったが、<ruby>彼<rt>かれ</rt></ruby>は<ruby>怒<rt>おこ</rt></ruby>ったような<ruby>顔<rt>かお</rt></ruby>をした。",
                "english": "It were words meant as a joke, but he made an angry face."
            },
            {
                "japanese": "<ruby>先<rt>さき</rt></ruby>に<ruby>入社<rt>にゅうしゃ</rt></ruby>した<ruby>由美<rt>ゆみ</rt></ruby>は<ruby>先輩<rt>せんぱい</rt></ruby>のつもりらしいが、<ruby>本当<rt>ほんとう</rt></ruby>はわたしの<ruby>方<rt>ほう</rt></ruby>が<ruby>年上<rt>としうえ</rt></ruby>なのだ。",
                "english": "Yumi, who joined the company earlier, seems to consider herself my senior, but actually I am older."
            },
            {
                "japanese": "こんなに<ruby>汚<rt>きたな</rt></ruby>いのに、それでも<ruby>掃除<rt>そうじ</rt></ruby>したつもりですか。",
                "english": "It's so dirty, and yet do you really think you've cleaned it?"
            }
        ]
    }
]

# Section 11 Drills (p.54)
sec11_drills = [
    make_mc("sec11_q1", "section_11_practice", "今度の日曜日はどこへも行かないで家で（　）ことにした。", ["a ゆっくりできる", "b ゆっくり休む", "c ゆっくり休んでいられる"], "b", "意志的動作「休む」に接続する「休むことにした」が正しい。", "Volitional verb with ことにした: ゆっくり休む."),
    make_mc("sec11_q2", "section_11_practice", "今、週18時間もアルバイトをしている。もうこれ以上（　）ことにした。", ["a 増えない", "b 増やさない", "c 増やせない"], "b", "自分の意志でこれ以上増やさないと決めたので他動詞否定「増やさないことにした」。", "Volitional negative decision: 増やさないことにした."),
    make_mc("sec11_q3", "section_11_practice", "わたしはもう油の多い料理は（　）ようにしよう。", ["a 食べない", "b 食べられない", "c 食べていない"], "a", "心がけを表す意志的動作の否定「食べないようにしよう」。", "Effort/habit resolution: 食べないようにしよう."),
    make_mc("sec11_q4", "section_11_practice", "健康のために1日40分は（　）いる。", ["a 歩くようにして", "b 歩けるようになって", "c 歩くようになって"], "a", "心がけ・努力の継続「歩くようにしている」。", "Continuous habit/effort: 歩くようにしている."),
    make_mc("sec11_q5", "section_11_practice", "薬は好きじゃないと言って、（　）病院から出た薬を飲もうとしない。", ["a わたしは", "b 山口さんは", "c わたしも夫も"], "b", "「〜ようとしない」は話者以外の第三者の拒絶を表すので「山口さんは」が正しい。", "Third-person refusal (〜ようとしない): 山口さんは."),
    make_mc("sec11_q6", "section_11_practice", "電車に乗ろうとしたら、（　）。", ["a 電車が来た", "b 電車のドアが開いた", "c 電車のドアが閉まった"], "c", "乗ろうとした直前の妨害・出来事として「ドアが閉まった」が自然。", "Action interruption: 電車のドアが閉まった."),
    make_mc("sec11_q7", "section_11_practice", "これ、ねずみに見えますか。自分ではねこを（　）つもりですが……。", ["a かく", "b かいた", "c かこうという"], "b", "完了した主観的行為「かいたつもりですが」。", "Subjective impression of completed action: かいたつもり."),
    make_mc("sec11_q8", "section_11_practice", "この靴下はていねいに（　）つもりだが、まだ完全にはきれいになっていない。", ["a 洗濯する", "b 洗濯される", "c 洗濯した"], "c", "すでに行った行為に対する「洗濯したつもりだが」。", "Subjective belief about past action: 洗濯したつもりだが."),
    make_mc("sec11_q9", "section_11_practice", "あなたはそれでも（　）つもりですか。プロならきちんと仕事をしてください。", ["a プロの", "b プロだと思う", "c プロらしい"], "a", "名詞＋の＋つもり。「プロのつもりですか」が正しい。", "Noun connection: プロのつもりですか.")
]

# ==============================================================================
# SECTION 12: 第12課 敬語
# ==============================================================================
sec12_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "尊敬語（目上の人の行為を言う）",
        "pattern_name_en": "Respectful Language (Sonkeigo)",
        "meaning_ja": "目上の人の行為を言うときに使う敬語表現。相手を高める。",
        "meaning_en": "Respectful language used to refer to the actions of superiors, elevating the person spoken about.",
        "connection_forms": [
            "お ＋ 動（ます形語幹） ＋ になる",
            "ご ＋ 名 ＋ になる",
            "動詞受身形（〜れる／〜られる）",
            "お ＋ 動（ます形語幹） ＋ ください",
            "ご ＋ 名 ＋ ください",
            "特別な尊敬語動詞（いらっしゃる、おいでになる、なさる、ご覧になる、召し上がる、おっしゃる、ご存じ）"
        ],
        "nuance_notes": "相手や第三者の行為について敬意を払って述べる。自分自身の行為には使えない。",
        "example_sentences": [
            {
                "japanese": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>何時<rt>なんじ</rt></ruby>ごろお<ruby>帰<rt>かえ</rt></ruby>りになりますか。",
                "english": "Around what time will you be returning home today?"
            },
            {
                "japanese": "<ruby>何年<rt>なんねん</rt></ruby>に<ruby>大学<rt>だいがく</rt></ruby>をご<ruby>卒業<rt>そつぎょう</rt></ruby>になったのですか。",
                "english": "In what year did you graduate from university?"
            },
            {
                "japanese": "<ruby>明日<rt>あす</rt></ruby>の<ruby>会議<rt>かいぎ</rt></ruby>には<ruby>出席<rt>しゅっせき</rt></ruby>されますか。",
                "english": "Will you attend tomorrow's meeting?"
            },
            {
                "japanese": "こちらにお<ruby>名前<rt>なまえ</rt></ruby>をお<ruby>書<rt>か</rt></ruby>きください。",
                "english": "Please write your name here."
            },
            {
                "japanese": "ぜひご<ruby>連絡<rt>れんらく</rt></ruby>ください。",
                "english": "Please be sure to contact us."
            },
            {
                "japanese": "<ruby>研究会<rt>けんきゅうかい</rt></ruby>の<ruby>会長<rt>かいちょう</rt></ruby>でいらっしゃいます。",
                "english": "He is the chairman of the research society."
            },
            {
                "japanese": "お<ruby>元気<rt>げんき</rt></ruby>でいらっしゃるそうです。",
                "english": "I hear that he is in good health."
            },
            {
                "japanese": "<ruby>京都<rt>きょうと</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいらっしゃいます。",
                "english": "He is living in Kyoto."
            },
            {
                "japanese": "<ruby>何<rt>なに</rt></ruby>をお<ruby>探<rt>さが</rt></ruby>しですか。",
                "english": "What are you looking for?"
            },
            {
                "japanese": "<ruby>新<rt>しん</rt></ruby>エネルギーを<ruby>研究<rt>けんきゅう</rt></ruby>しておいでになります。",
                "english": "He is doing research on new energy."
            },
            {
                "japanese": "<ruby>推薦書<rt>すいせんしょ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてくださいました。",
                "english": "He kindly wrote a letter of recommendation for me."
            },
            {
                "japanese": "いつわたしの<ruby>国<rt>くに</rt></ruby>へいらっしゃいましたか。",
                "english": "When did you come to my country?"
            },
            {
                "japanese": "いつわたしの<ruby>国<rt>くに</rt></ruby>へおいでになりますか。",
                "english": "When will you come to my country?"
            },
            {
                "japanese": "さきほど<ruby>見<rt>み</rt></ruby>えましたよ。",
                "english": "He arrived just a moment ago."
            },
            {
                "japanese": "<ruby>来月<rt>らいげつ</rt></ruby>アメリカへいらっしゃいます。",
                "english": "He is going to America next month."
            },
            {
                "japanese": "<ruby>来月<rt>らいげつ</rt></ruby>アメリカへおいでになるようです。",
                "english": "It appears he is going to America next month."
            },
            {
                "japanese": "<ruby>今晩<rt>こんばん</rt></ruby>はお<ruby>宅<rt>たく</rt></ruby>にいらっしゃるでしょう。",
                "english": "He will probably be at home tonight."
            },
            {
                "japanese": "<ruby>今晩<rt>こんばん</rt></ruby>はお<ruby>宅<rt>たく</rt></ruby>においでになりますか。",
                "english": "Will you be at home tonight?"
            },
            {
                "japanese": "ゴルフをなさいますか。",
                "english": "Do you play golf?"
            },
            {
                "japanese": "この<ruby>雑誌<rt>ざっし</rt></ruby>をご<ruby>覧<rt>らん</rt></ruby>になりますか。",
                "english": "Would you like to look at this magazine?"
            },
            {
                "japanese": "<ruby>和食<rt>わしょく</rt></ruby>を<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります。お<ruby>酒<rt>さけ</rt></ruby>も<ruby>召<rt>め</rt></ruby>し<ruby>上<rt>あ</rt></ruby>がります。",
                "english": "He eats Japanese food and also drinks sake."
            },
            {
                "japanese": "お<ruby>名前<rt>なまえ</rt></ruby>は<ruby>何<rt>なん</rt></ruby>とおっしゃいますか。",
                "english": "What is your name?"
            },
            {
                "japanese": "あの<ruby>方<rt>かた</rt></ruby>をご<ruby>存<rt>ぞん</rt></ruby>じですか。",
                "english": "Do you know that person?"
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "謙譲語1（目上の人に関係のある、自分の行為を言う）",
        "pattern_name_en": "Humble Language 1 (Kenjougo I)",
        "meaning_ja": "目上の人に関係のある、自分の行為を言うときに使う表現。自分をへりくだることで相手を高める。",
        "meaning_en": "Humble language used to describe the speaker's own behavior when it involves or affects a superior.",
        "connection_forms": [
            "お ＋ 動（ます形語幹） ＋ する",
            "ご ＋ 名 ＋ する",
            "お ＋ 動（ます形語幹） ＋ できる",
            "動て形 ＋ いただく",
            "特別な謙譲語動詞（拝見する、申し上げる、伺う、お目にかかる、さしあげる）"
        ],
        "nuance_notes": "自分の行為の受け手（相手）が高位であるときに用いる。",
        "example_sentences": [
            {
                "japanese": "（<ruby>先生<rt>せんせい</rt></ruby>の）ご<ruby>本<rt>ほん</rt></ruby>をお<ruby>借<rt>か</rt></ruby>りします。（<ruby>先生<rt>せんせい</rt></ruby>を）<ruby>会場<rt>かいじょう</rt></ruby>へご<ruby>案内<rt>あんない</rt></ruby>します。",
                "english": "I will borrow your book. I will guide you to the hall."
            },
            {
                "japanese": "<ruby>完成品<rt>かんせいひん</rt></ruby>はまだ（<ruby>先生<rt>せんせい</rt></ruby>に）お<ruby>見<rt>み</rt></ruby>せできません。",
                "english": "I cannot show the finished product to you yet."
            },
            {
                "japanese": "（<ruby>先生<rt>せんせい</rt></ruby>に）ピアノを<ruby>教<rt>おし</rt></ruby>えていただきました。",
                "english": "I had the teacher teach me the piano."
            },
            {
                "japanese": "（<ruby>先生<rt>せんせい</rt></ruby>の<ruby>写真<rt>しゃしん</rt></ruby>を）ちょっと<ruby>拝見<rt>はいけん</rt></ruby>します。",
                "english": "Let me take a look at your photograph."
            },
            {
                "japanese": "（<ruby>先生<rt>せんせい</rt></ruby>に）お<ruby>礼<rt>れい</rt></ruby>を<ruby>申<rt>もう</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げます。",
                "english": "I express my gratitude to you."
            },
            {
                "japanese": "（<ruby>先生<rt>せんせい</rt></ruby>に）ちょっと<ruby>伺<rt>うかが</rt></ruby>いますが……。",
                "english": "Excuse me, may I ask you something?"
            },
            {
                "japanese": "あした3<ruby>時<rt>じ</rt></ruby>に（<ruby>先生<rt>せんせい</rt></ruby>の）お<ruby>宅<rt>たく</rt></ruby>に<ruby>伺<rt>うかが</rt></ruby>います。",
                "english": "I will visit your house tomorrow at 3 o'clock."
            },
            {
                "japanese": "あした3<ruby>時<rt>じ</rt></ruby>に（<ruby>先生<rt>せんせい</rt></ruby>に）お<ruby>目<rt>め</rt></ruby>にかかります。",
                "english": "I will meet with you tomorrow at 3 o'clock."
            },
            {
                "japanese": "（<ruby>先生<rt>せんせい</rt></ruby>に）<ruby>本<rt>ほん</rt></ruby>をさしあげます。",
                "english": "I will give you a book."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "謙譲語2（自分の行為をていねいに言う・丁重語）",
        "pattern_name_en": "Humble Language 2 / Courteous Language (Teichougo)",
        "meaning_ja": "自分の行為を聞き手に対してていねいに言う表現。",
        "meaning_en": "Courteous verb forms used to politely or modestly describe the speaker's own behavior to the listener.",
        "connection_forms": [
            "特別な丁重語動詞（参る、おる、いたす、いただく、申す、存じる、存じておる）"
        ],
        "nuance_notes": "行為の向かう先が特定の目上でなくても、話を聞いている相手に対して丁寧に述べる際に用いる。",
        "example_sentences": [
            {
                "japanese": "あした3<ruby>時<rt>じ</rt></ruby>に<ruby>参<rt>まい</rt></ruby>ります。",
                "english": "I will come/go tomorrow at 3 o'clock."
            },
            {
                "japanese": "<ruby>夜<rt>よる</rt></ruby>は<ruby>家<rt>いえ</rt></ruby>におります。",
                "english": "I will be at home in the evening."
            },
            {
                "japanese": "<ruby>片付<rt>かたづ</rt></ruby>けは<ruby>後<rt>あと</rt></ruby>でわたしがいたします。",
                "english": "I will do the cleanup later."
            },
            {
                "japanese": "<ruby>刺身<rt>さしみ</rt></ruby>も<ruby>日本酒<rt>にほんしゅ</rt></ruby>もいただきます。",
                "english": "I eat sashimi and drink sake."
            },
            {
                "japanese": "<ruby>山中<rt>やまなか</rt></ruby>と<ruby>申<rt>もう</rt></ruby>します。",
                "english": "My name is Yamanaka."
            },
            {
                "japanese": "<ruby>行<rt>い</rt></ruby>き<ruby>先<rt>さき</rt></ruby>はよく<ruby>存<rt>ぞん</rt></ruby>じております。",
                "english": "I know the destination well."
            },
            {
                "japanese": "いくつか<ruby>方法<rt>ほうほう</rt></ruby>があると<ruby>存<rt>ぞん</rt></ruby>じます。",
                "english": "I think there are several methods."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "丁寧語（自分や相手に関係なく、ものごとをていねいに言う）",
        "pattern_name_en": "Polite Language (Teineigo)",
        "meaning_ja": "自分や相手に関係なく、ものごとをていねいに言う表現。",
        "meaning_en": "Polite language used to say things politely, without consideration of hierarchy of relationship.",
        "connection_forms": [
            "でございます（〜だ）",
            "ございます（ある）"
        ],
        "nuance_notes": "日常の改まった場面や接客などで、状況や存在を丁寧に述べる。",
        "example_sentences": [
            {
                "japanese": "これは<ruby>新製品<rt>しんせいひん</rt></ruby>でございます。",
                "english": "This is a new product."
            },
            {
                "japanese": "パソコン<ruby>用品<rt>ようひん</rt></ruby>は3<ruby>階<rt>かい</rt></ruby>にございます。",
                "english": "Computer supplies are on the 3rd floor."
            }
        ]
    }
]

# Section 12 Drills (p.54-55)
sec12_drills = [
    make_mc("sec12_q1", "section_12_practice", "高橋先生が先週水曜日に帰国（　）。", ["a いたしました", "b されました", "c いたされました"], "b", "高橋先生の行為に対する尊敬語は受身形「されました」。", "Respectful form for teacher's action: されました."),
    make_mc("sec12_q2", "section_12_practice", "客「あの、わたしの番はまだでしょうか。20分ぐらい待っているんですけど。」\n銀行員「何番の紙を（　）。ああ、12番ですね。では、次です。」", ["a お持ちされますか", "b お持ちですか", "c お持ちしていますか"], "b", "相手（客）の所有・状態に対する尊敬語「お持ちですか」。", "Respectful form towards customer: お持ちですか."),
    make_mc("sec12_q3", "section_12_practice", "お父様はあなたに何と（　）。", ["a 申されましたか", "b 申し上げましたか", "c おっしゃいましたか"], "c", "相手の父親の行為に対する尊敬語動詞は「おっしゃいましたか」。", "Respectful form for someone else's father: おっしゃいましたか."),
    make_mc("sec12_q4", "section_12_practice", "わたしはリーと（　）。台湾からの留学生です。", ["a 申します", "b 申し上げます", "c おっしゃいます"], "c", "自分の名前を名乗る丁重語は「申します」。", "Humble name introduction: 申します."),
    make_mc("sec12_q5", "section_12_practice", "客「すみません。牛乳はどこですか。」\n店員「あ、牛乳ですか。牛乳はあそこのパン売り場のとなりに（　）。」", ["a いたします", "b ございます", "c おります"], "b", "物の存在をていねいに言う丁寧語は「ございます」。", "Polite existence form for goods: ございます."),
    make_mc("sec12_q6", "section_12_practice", "どうぞご自由にパンフレットをお（　）ください。", ["a お取り", "b いただいて", "c お持ちして"], "a", "相手への勧め「お取りください（お＋ます語幹＋ください）」。", "Polite invitation to take: お取りください."),
    make_mc("sec12_q7", "section_12_practice", "お忙しいとは（　）が、できるだけ早くお返事をいただけますか。", ["a ご存じます", "b ご存じです", "c 存じます"], "c", "自分の判断・心情を述べる丁重語は「存じます」。", "Courteous mental state (think): 存じます."),
    make_mc("sec12_q8", "section_12_practice", "では次に、こちらのグラフを（　）。", ["a ごらんください", "b ごらんでください", "c ごらんしてください"], "a", "「見る」の尊敬表現「ごらんください」。", "Respectful request to look: ごらんください."),
    make_mc("sec12_q9", "section_12_practice", "来月国から両親が（　）。", ["a 見えます", "b 参ります", "c おいでです"], "b", "自分の身内（両親）の行為を聞き手に言うので丁重語「参ります」。", "Courteous form for own family's arrival: 参ります.")
]

# Combined Drills: 練習 11・12課 (p.55)
sec11_12_combined_drills = [
    make_mc("sec11_12_q1", "section_11_12_combined", "駅の改札を（　）したとき、切符をなくしたことに気がついた。", ["a 出るつもりにて", "b 出ようと", "c 出るように"], "b", "「〜出ようとしたとき」という行為直前の契機表現。", "Just as about to exit: 出ようと."),
    make_mc("sec11_12_q2", "section_11_12_combined", "あさっては大雨が降るそうだよ。ハイキングは来週（　）。", ["a 行こうとしようよ", "b 行くことにしようよ", "c 行くようになろうよ"], "b", "意志的決定を提案する「行くことにしようよ」。", "Joint decision: 行くことにしようよ."),
    make_mc("sec11_12_q3", "section_11_12_combined", "弟はさっきからテーブルの上に卵を（　）しているが、難しいだろう。", ["a 立てようと", "b 立てることに", "c 立てたつもりに"], "a", "試み「立てようとしている」。", "Attempting to do: 立てようと."),
    make_mc("sec11_12_q4", "section_11_12_combined", "教えていただいたときは（　）が、後で自分でやってみたらできませんでした。", ["a わかろうとなさいました", "b おわかりのことでした", "c わかったつもりでした"], "c", "主観的な思い込み「わかったつもりでした」。", "Thought I understood: わかったつもりでした."),
    make_mc("sec11_12_q5", "section_11_12_combined", "3月3日にうちでパーティーを開く（　）ので、ぜひおいでください。", ["a ようになさいました", "b ようにしておりました", "c ことにいたしました"], "c", "自分の決定を丁寧に伝える「ことにいたしました」。", "Humble reporting of decision: ことにいたしました."),
    make_mc("sec11_12_q6", "section_11_12_combined", "わたしはいつも必ず朝7時のニュースを（　）います。", ["a 見るようにして", "b 拝見するようにして", "c ごらんになることにして"], "a", "日頃の習慣・心がけ「見るようにしています」。", "Daily intentional habit: 見るようにして."),
    make_mc("sec11_12_q7", "section_11_12_combined", "では、今度は来週の月曜日に（　）しましょう。", ["a お会いすることに", "b お会いになることに", "c お会いしようと"], "a", "自分と相手の会合の取り決め「お会いすることにしましょう」。", "Humble arrangement to meet: お会いすることに."),
    make_mc("sec11_12_q8", "section_11_12_combined", "あの、お荷物が多くて大変でしょう。一つ、（　）。", ["a お持ちになるようにしますよ", "b お持ちしますよ", "c お持ちになりますよ"], "b", "相手のために手伝う謙譲表現「お持ちしますよ」。", "Humble offer to carry luggage: お持ちしますよ.")
]

# Review Test 3: まとめ問題 1〜12課 (p.56-57)
matome_1_to_12_drills = [
    make_mc("matome_1_12_q1", "review_test_1_to_12", "課長、今度の工場見学にはわたしもいっしょに（　）んですが、いいでしょうか。", ["1 行ってほしい", "2 行っていただきたい", "3 行かせたい", "4 行かせていただきたい"], "4", "自分が同行する許可を求める謙譲表現「行かせていただきたい」。", "Asking permission humbly: 行かせていただきたい."),
    make_mc("matome_1_12_q2", "review_test_1_to_12", "日本語をたくさん話したいから、教室では自分の国の言葉を（　）。", ["1 使うとは限らない", "2 使わないようにしている", "3 使うことではない", "4 使わないわけではない"], "2", "習慣・努力の心がけ「使わないようにしている」。", "Intentional continuous habit: 使わないようにしている."),
    make_mc("matome_1_12_q3", "review_test_1_to_12", "5時ごろ空港から電話があったのだから、そろそろ家に着く（　）だ。", ["1 ばかり", "2 つもり", "3 はず", "4 べき"], "3", "確実な根拠に基づく論理的推測「着くはずだ」。", "Logical certainty: はず."),
    make_mc("matome_1_12_q4", "review_test_1_to_12", "【図書館で】あ、それは持ち出し禁止の資料ですので、（　）。", ["1 お借りできません", "2 お貸しできません", "3 お借りしません", "4 お貸しになりません"], "2", "図書館側が客に貸し出す行為の謙譲可能表現「お貸しできません」。", "Humble inability to lend: お貸しできません."),
    make_mc("matome_1_12_q5", "review_test_1_to_12", "A「すみません、ちょっとその辞書を（　）。」\nB「いいですよ。どうぞ。」", ["1 借りてもいいですか", "2 借りたらどうですか", "3 借りてほしいんですが", "4 借りるといいですよ"], "1", "使用の許可を求める「借りてもいいですか」。", "Asking permission to borrow: 借りてもいいですか."),
    make_mc("matome_1_12_q6", "review_test_1_to_12", "先生「皆さん、この書類は大切なので、絶対に（　）。わかりましたか。」", ["1 なくすわけではありません", "2 なくさないべき", "3 なくすことはありません", "4 なくさないこと"], "4", "指示・規則を表す「なくさないこと」。", "Instruction/rule: なくさないこと."),
    make_mc("matome_1_12_q7", "review_test_1_to_12", "会社を（　）、課長に呼び止められた。", ["1 出るようにしたら", "2 出ている間", "3 出ようとしたら", "4 出ているうちに"], "3", "行為の直前契機「出ようとしたら」。", "Just as about to leave: 出ようとしたら."),
    make_mc("matome_1_12_q8", "review_test_1_to_12", "A「もしもし、田中ですが、これからお宅に（　）よろしいですか。」\nB「ええ、どうぞ。お待ちしています。」", ["1 おいでになっても", "2 伺っても", "3 いらっしゃっても", "4 お目にかかっても"], "2", "相手の家を訪問する謙譲表現「伺っても」。", "Humble visiting expression: 伺っても."),
    make_mc("matome_1_12_q9", "review_test_1_to_12", "A「お宅のこうちゃん、薬飲まないの？」\nB「そうなの。あの子、（　）、いやがって口を開けないのよ。」", ["1 飲むことにしても", "2 飲むつもりでも", "3 飲ませたつもりでも", "4 飲ませようとしても"], "4", "飲ませる試みをした契機「飲ませようとしても」。", "Trying to make child drink medicine: 飲ませようとしても."),
    make_mc("matome_1_12_q10", "review_test_1_to_12", "A「あした、柔道の試合に出るんです。」\nB「そうですか。自分の力が（　）。」", ["1 出せるといいですね", "2 出せたらどうですか", "3 出るといいですよ", "4 出ればよかったですね"], "1", "相手への願望・祈り「力が出せるといいですね」。", "Wishing success for other person: 出せるといいですね."),
    make_mc("matome_1_12_q11", "review_test_1_to_12", "店に入りたかったが、もう閉店時間だった。もっと早く来る（　）だった。", ["1 ほど", "2 はず", "3 こと", "4 べき"], "4", "過去の後悔「来るべきだった」。", "Past regret: べき."),
    make_mc("matome_1_12_q12", "review_test_1_to_12", "【美術館で】あの、お客様、どちらへ（　）。この奥は関係者以外は入れませんが。", ["1 行かれますか", "2 参りますか", "3 おられますか", "4 見えますか"], "1", "客の進行に対する尊敬動詞「行かれますか」。", "Respectful form of 行く for customer: 行かれますか."),
    make_mc("matome_1_12_q13", "review_test_1_to_12", "一度失敗しただけで（　）よ。もう少しがんばって。", ["1 あきらめたわけがない", "2 あきらめたはずがない", "3 あきらめるわけではない", "4 あきらめるべきではない"], "4", "忠告・助言の否定「あきらめるべきではない」。", "Advice / should not give up: あきらめるべきではない.")
]
