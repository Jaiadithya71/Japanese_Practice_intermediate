# -*- coding: utf-8 -*-
"""
Section 9 and Section 10 data for Shin Kanzen Master N3 Grammar.
Section 9: 第9課 〜と望む (Patterns 1-3, Drills 1-8)
Section 10: 第10課 〜したほうがいい・〜なさい (Patterns 1-4, Drills 1-10)
Combined Drills: 練習 9・10課 (Q1-9)
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
# SECTION 9: 第9課 〜と望む
# ==============================================================================
sec9_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "〜てもらいたい・〜ていただきたい・〜てほしい",
        "pattern_name_en": "Want someone to do something",
        "meaning_ja": "相手にその行為をしてほしいという希望を表す。「〜ていただきたい」は敬語表現。",
        "meaning_en": "I want (someone) to do... / Would like (someone) to do... Expresses speaker's wish for another person to perform an action. 〜ていただきたい is polite/respectful.",
        "connection_forms": [
            "動て形 / ないで ＋ もらいたい・いただきたい・ほしい"
        ],
        "nuance_notes": "話者が他者に対して行動を期待・希望するときに用いる。目上の人に対して直接「〜てほしい」と言うのは失礼にあたる。",
        "example_sentences": [
            {
                "japanese": "この<ruby>仕事<rt>しごと</rt></ruby>はだれにも<ruby>手伝<rt>てつだ</rt></ruby>ってもらいたくない。",
                "english": "I don't want anyone to help me with this job."
            },
            {
                "japanese": "これからは<ruby>自分<rt>じぶん</rt></ruby>の<ruby>力<rt>ちから</rt></ruby>で<ruby>生活<rt>せいかつ</rt></ruby>していってほしい。",
                "english": "From now on, I want you to make a living on your own strength."
            },
            {
                "japanese": "<ruby>娘<rt>むすめ</rt></ruby>には、あまり<ruby>遠<rt>とお</rt></ruby>くの<ruby>町<rt>まち</rt></ruby>には<ruby>嫁<rt>よめ</rt></ruby>に<ruby>行<rt>い</rt></ruby>かないでほしい。",
                "english": "I want my daughter not to marry someone living in a town far away."
            },
            {
                "japanese": "<ruby>国<rt>くに</rt></ruby>の<ruby>両親<rt>りょうしん</rt></ruby>に、わたしの<ruby>活躍<rt>かつやく</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていただきたい。",
                "english": "I would like my parents back home to see my success."
            },
            {
                "japanese": "このような<ruby>犯罪<rt>はんざい</rt></ruby>は<ruby>二度<rt>にど</rt></ruby>と<ruby>起<rt>お</rt></ruby>こってほしくない。",
                "english": "I don't want crimes like this ever to happen again."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜(さ)せてもらいたい・〜(さ)せていただきたい・〜(さ)せてほしい",
        "pattern_name_en": "Let me do / I would like permission to do",
        "meaning_ja": "自分がある行為をすることを許可してほしい、させてもらいたいという希望を表す。",
        "meaning_en": "Please allow me to... / I would like to be permitted to do... Expresses speaker's wish for permission to do something.",
        "connection_forms": [
            "動使役て形 ＋ もらいたい・いただきたい・ほしい"
        ],
        "nuance_notes": "使役形（〜せる／〜させる）に「てほしい／てもらいたい／ていただきたい」を接続して、相手の許可や容認を求める。",
        "example_sentences": [
            {
                "japanese": "<ruby>店員<rt>てんいん</rt></ruby>「<ruby>少<rt>すこ</rt></ruby>し<ruby>考<rt>かんが</rt></ruby>えさせてほしいんですが。」",
                "english": "Clerk: 'Could you please let me think for a moment?'"
            },
            {
                "japanese": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>体調<rt>たいちょう</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>いので、<ruby>早退<rt>そうたい</rt></ruby>させていただきたいのですが。",
                "english": "Since I'm not feeling well today, I would like permission to leave early."
            },
            {
                "japanese": "この<ruby>仕事<rt>しごと</rt></ruby>は、ぜひわたしにやらせてください。",
                "english": "Please let me do this job by all means."
            },
            {
                "japanese": "<ruby>話<rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いてもらいたい。<ruby>少<rt>すこ</rt></ruby>し<ruby>時間<rt>じかん</rt></ruby>をくれないか。",
                "english": "I want you to hear me out. Could you give me some time?"
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜といい・〜ばいい・〜たらいい",
        "pattern_name_en": "I hope that... / It would be nice if... / You should...",
        "meaning_ja": "A: （自分ではどうにもならないことについて）そうなることを願う。B: 相手にある行為を勧める・促す。",
        "meaning_en": "A: I hope that / Wish that (for circumstances beyond one's control). B: It would be good to / You should (giving advice or encouragement).",
        "connection_forms": [
            "動辞書形 / ない形 ＋ といい・ばいい・たらいい",
            "イ形い / ない ＋ といい・ばいい・たらいい",
            "ナ形だ / 名だ ＋ といい・ならいい・たらいい"
        ],
        "nuance_notes": "A用法は話者の願望・祈り（「〜といいな」など）。B用法は「〜すればいい」という助言・解決策の提示。",
        "example_sentences": [
            {
                "japanese": "あしたは<ruby>晴<rt>は</rt></ruby>れるといいね。",
                "english": "I hope it will be sunny tomorrow."
            },
            {
                "japanese": "<ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>できればいいのだが。",
                "english": "I hope I can pass the exam."
            },
            {
                "japanese": "<ruby>早<rt>はや</rt></ruby>く<ruby>風邪<rt>かぜ</rt></ruby>が<ruby>治<rt>なお</rt></ruby>ったらいいですね。",
                "english": "I hope your cold gets better soon."
            },
            {
                "japanese": "<ruby>疲<rt>つか</rt></ruby>れているなら、<ruby>早<rt>はや</rt></ruby>く<ruby>寝<rt>ね</rt></ruby>るといいよ。",
                "english": "If you are tired, you should go to sleep early."
            },
            {
                "japanese": "わからないときは、<ruby>先生<rt>せんせい</rt></ruby>に<ruby>聞<rt>き</rt></ruby>けばいい。",
                "english": "When you don't understand, you should just ask the teacher."
            }
        ]
    }
]

# Section 9 Drills (p.48)
sec9_drills = [
    make_mc("sec9_q1", "section_9_practice", "ずっと（　）所に父が連れていってくれた。とても楽しかった。", ["a 行きたかった", "b 行ってほしかった", "c 行ってもらいたかった"], "a", "自分自身の願望「行きたかった所」が正しい。", "Speaker's own past wish: 行きたかった."),
    make_mc("sec9_q2", "section_9_practice", "だれかわからないけど、道にごみを（　）もらいたいなあ。", ["a 捨てられて", "b 捨てないで", "c 捨てられないで"], "b", "他者に対してゴミを捨てないでほしいので「捨てないでもらいたい」が正しい。", "Asking others not to litter: 捨てないでもらいたい."),
    make_mc("sec9_q3", "section_9_practice", "卒業式では写真を撮ったんでしょう。ぜひ（　）ほしいです。", ["a 見て", "b 見せて", "c 見られて"], "b", "相手に見せてほしいので「見せてほしい」が適切。", "Asking someone to show: 見せてほしい."),
    make_mc("sec9_q4", "section_9_practice", "今日はおなかが痛いので、アルバイトを（　）いただきたいのですが。", ["a 休んで", "b 休まれて", "c 休ませて"], "c", "自分が休む許可を求めるので使役て形「休ませていただきたい」が正しい。", "Asking permission to take leave: 休ませていただきたい."),
    make_mc("sec9_q5", "section_9_practice", "説明がよくわかりませんでした。もう一度（　）ほしいのですが。", ["a 教えて", "b 教えさせて", "c 教わって"], "a", "相手に教えてほしいので「教えてほしい」が正しい。", "Asking someone to explain: 教えてほしい."),
    make_mc("sec9_q6", "section_9_practice", "あのう、お客様、店内のガラス製品に（　）いただきたいのですが……。", ["a 触って", "b 触らせて", "c 触らないで"], "c", "客に対して触らないよう丁重にお願いするので「触らないでいただきたい」が正しい。", "Politely asking customer not to touch: 触らないでいただきたい."),
    make_mc("sec9_q7", "section_9_practice", "来週からご旅行ですか。（　）いいですね。", ["a 天気がいいと", "b 天気がいいなら", "c 天気がいいのは"], "a", "天候への願望を表す「天気がいいといいですね」が正しい。", "Wishing good weather: 天気がいいといいですね."),
    make_mc("sec9_q8", "section_9_practice", "おめでとうございます。（　）よかったですね。", ["a 合格できると", "b 合格できて", "c 合格できれば"], "b", "すでに合格した過去の事実に対して「合格できてよかったですね」と祝う。", "Congratulating on achieved result: 合格できてよかったですね.")
]

# ==============================================================================
# SECTION 10: 第10課 〜したほうがいい・〜なさい
# ==============================================================================
sec10_patterns = [
    {
        "pattern_number": 1,
        "pattern_name": "命令（しろ）/ 禁止（〜な）",
        "pattern_name_en": "Imperative (command) / Prohibitive (do not)",
        "meaning_ja": "命令形：強く指示・命令する。禁止形（動辞書形＋な）：強く禁止する。",
        "meaning_en": "Imperative (しろ): strongly commands an action. Prohibitive (〜な): strongly forbids an action.",
        "connection_forms": [
            "動詞Ⅰ：動（え段）",
            "動詞Ⅱ：動（ろ）",
            "動詞Ⅲ：する→しろ、来る→来い（例外：くれる→くれ）",
            "禁止：動辞書形 ＋ な"
        ],
        "nuance_notes": "日常会話では目上の人には使えない。標識・立て札・緊急時・男性同士の親しい会話・間接引用（〜と言われた）などで用いられる。",
        "example_sentences": [
            {
                "japanese": "【<ruby>試合<rt>しあい</rt></ruby>で】<ruby>監督<rt>かんとく</rt></ruby>「<ruby>走<rt>はし</rt></ruby>れ、<ruby>走<rt>はし</rt></ruby>れ！」",
                "english": "[At a match] Coach: 'Run, run!'"
            },
            {
                "japanese": "<ruby>犬<rt>いぬ</rt></ruby>に「<ruby>降<rt>お</rt></ruby>りろ。」と<ruby>命令<rt>めいれい</rt></ruby>した。<ruby>犬<rt>いぬ</rt></ruby>は<ruby>命令<rt>めいれい</rt></ruby>に<ruby>従<rt>したが</rt></ruby>った。",
                "english": "I commanded the dog, 'Get down.' The dog obeyed the command."
            },
            {
                "japanese": "<ruby>赤信号<rt>あかしんごう</rt></ruby>は<ruby>止<rt>と</rt></ruby>まれという<ruby>意味<rt>いみ</rt></ruby>です。",
                "english": "A red light means 'Stop'."
            },
            {
                "japanese": "<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しを<ruby>手伝<rt>てつだ</rt></ruby>ってくれと<ruby>友<rt>とも</rt></ruby>だちに<ruby>頼<rt>たの</rt></ruby>んでみよう。",
                "english": "Let's ask a friend to please help with the move."
            },
            {
                "japanese": "<ruby>立<rt>た</rt></ruby>て<ruby>札<rt>ふだ</rt></ruby>に「スピードを<ruby>出<rt>だ</rt></ruby>すな！」と<ruby>書<rt>か</rt></ruby>いてある。",
                "english": "The signboard says, 'Do not speed!'"
            },
            {
                "japanese": "<ruby>父<rt>ちち</rt></ruby>は<ruby>医者<rt>いしゃ</rt></ruby>にお<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>むなと<ruby>言<rt>い</rt></ruby>われている。",
                "english": "My father was told by his doctor not to drink alcohol."
            }
        ]
    },
    {
        "pattern_number": 2,
        "pattern_name": "〜こと",
        "pattern_name_en": "Must do / Must not do (written rules / instructions)",
        "meaning_ja": "規則・指示・注意事項などを文書や掲示で伝えるときに使う（〜しなさい／〜してはいけない）。",
        "meaning_en": "Must / Do not... Used in written notices, rules, and formal instructions to command or forbid actions.",
        "connection_forms": [
            "動辞書形 / ない形 ＋ こと"
        ],
        "nuance_notes": "張り紙・規則書・試験の指示文などでよく使われる書き言葉の命令表現。",
        "example_sentences": [
            {
                "japanese": "【<ruby>学校<rt>がっこう</rt></ruby>で】<ruby>先生<rt>せんせい</rt></ruby>「レポートは<ruby>来週<rt>らいしゅう</rt></ruby><ruby>月曜日<rt>げつようび</rt></ruby>に<ruby>必<rt>かなら</rt></ruby>ず<ruby>出<rt>だ</rt></ruby>すこと。<ruby>遅<rt>おく</rt></ruby>れないこと。」",
                "english": "[At school] Teacher: 'Make sure to submit your reports next Monday without fail. Do not be late.'"
            },
            {
                "japanese": "<ruby>申込書<rt>もうしこみしょ</rt></ruby>を<ruby>書<rt>か</rt></ruby>く<ruby>前<rt>まえ</rt></ruby>に<ruby>注意書<rt>ちゅういが</rt></ruby>きをよく<ruby>読<rt>よ</rt></ruby>むこと。",
                "english": "Be sure to read the instructions carefully before filling out the application form."
            },
            {
                "japanese": "【<ruby>立<rt>た</rt></ruby>て<ruby>札<rt>ふだ</rt></ruby>】<ruby>危<rt>あぶ</rt></ruby>ないからこの<ruby>川<rt>かわ</rt></ruby>で<ruby>泳<rt>およ</rt></ruby>がないこと。",
                "english": "[Signboard] Dangerous: Do not swim in this river."
            }
        ]
    },
    {
        "pattern_number": 3,
        "pattern_name": "〜べきだ・〜べき／〜べきではない",
        "pattern_name_en": "Should / Ought to / Must not",
        "meaning_ja": "〜するのが当然だ・〜したほうがいい／〜してはいけない。話者の主張を言うときに使う。過去形は反省や後悔を表す。",
        "meaning_en": "It is a matter of course to / Should / Should not. Reflects the speaker's judgment or strong opinion. When used in past tense (〜べきだった), expresses regret.",
        "connection_forms": [
            "動辞書形 ＋ べきだ・べきではない  ＊例外：する→するべきだ・すべきだ",
            "動辞書形 ＋ べき・べきではない ＋ 名"
        ],
        "nuance_notes": "道徳・常識・社会的義務から見て当然そうすべきだと話者が主張する表現。目上の人に対する直接の指示には使わない。",
        "example_sentences": [
            {
                "japanese": "これは<ruby>大事<rt>だいじ</rt></ruby>なことですから、もう<ruby>少<rt>すこ</rt></ruby>し<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>ってから<ruby>決<rt>き</rt></ruby>めるべきだと<ruby>思<rt>おも</rt></ruby>いますよ。",
                "english": "Since this is an important matter, I believe we should decide after discussing it a bit more."
            },
            {
                "japanese": "<ruby>仕事<rt>しごと</rt></ruby>はたくさんあるが、まず、<ruby>今日中<rt>きょうじゅう</rt></ruby>にやるべきことから<ruby>始<rt>はじ</rt></ruby>めよう。",
                "english": "There is a lot of work, but let's start with the things that should be done today."
            },
            {
                "japanese": "せっかく<ruby>入<rt>はい</rt></ruby>った<ruby>会社<rt>かいしゃ</rt></ruby>なのだから、<ruby>簡単<rt>かんたん</rt></ruby>に<ruby>辞<rt>や</rt></ruby>めるべきではない。",
                "english": "Since it's a company you went through great efforts to enter, you shouldn't quit so easily."
            },
            {
                "japanese": "<ruby>子<rt>こ</rt></ruby>どもは<ruby>夜遅<rt>よるおそ</rt></ruby>くまで<ruby>外<rt>そと</rt></ruby>にいるべきではない。",
                "english": "Children should not stay outside late at night."
            },
            {
                "japanese": "あしたまでのレポートがまだ<ruby>書<rt>か</rt></ruby>き<ruby>終<rt>お</rt></ruby>わらない。もっと<ruby>早<rt>はや</rt></ruby>くから<ruby>始<rt>はじ</rt></ruby>めるべきだった。",
                "english": "The report due tomorrow isn't finished yet. I should have started earlier."
            }
        ]
    },
    {
        "pattern_number": 4,
        "pattern_name": "〜たらどうか",
        "pattern_name_en": "Why don't you...? / How about...?",
        "meaning_ja": "〜するのがいいですよ。助言や忠告の気持ちで相手にある行為を軽く勧めるときに使う。非難の気持ちを表すこともある。",
        "meaning_en": "Why don't you...? / How about doing...? Used to give mild advice or suggestions. Can also imply gentle criticism for not doing something.",
        "connection_forms": [
            "動たら ＋ どうか"
        ],
        "nuance_notes": "目上の人に対して直接使うと失礼になる場合がある。親しい相手への提案・アドバイスに適する。",
        "example_sentences": [
            {
                "japanese": "<ruby>体<rt>からだ</rt></ruby>のことが<ruby>心配<rt>しんぱい</rt></ruby>なら、<ruby>一度<rt>いちど</rt></ruby><ruby>健康診断<rt>けんこうしんだん</rt></ruby>を<ruby>受<rt>う</rt></ruby>けたらどうでしょうか。",
                "english": "If you are worried about your health, why don't you get a medical checkup once?"
            },
            {
                "japanese": "<ruby>疲<rt>つか</rt></ruby>れているみたいですね。<ruby>少<rt>すこ</rt></ruby>し<ruby>休<rt>やす</rt></ruby>んだらどうですか。",
                "english": "You look tired. Why don't you rest a bit?"
            },
            {
                "japanese": "<ruby>迷惑<rt>めいわく</rt></ruby>メールが<ruby>多<rt>おお</rt></ruby>いの？じゃ、アドレスを<ruby>変<rt>か</rt></ruby>えたらどう？",
                "english": "Getting a lot of spam emails? Then why don't you change your email address?"
            },
            {
                "japanese": "<ruby>悪<rt>わる</rt></ruby>いのはそっちですよ。<ruby>一言<rt>ひとこと</rt></ruby><ruby>謝<rt>あやま</rt></ruby>ったらどうですか。",
                "english": "You're the one in the wrong. Why don't you say a word of apology?"
            }
        ]
    }
]

# Section 10 Drills (p.48-49)
sec10_drills = [
    make_mc("sec10_q1", "section_10_practice", "先生が「話を（　）。」と言っているのに、まだみんなしゃべっています。", ["a やめ", "b やめれ", "c やめろ"], "c", "グループⅡ動詞「やめる」の命令形は「やめろ」。", "Group 2 verb imperative form: やめろ."),
    make_mc("sec10_q2", "section_10_practice", "今すぐ金を（　）と言われても困ります。来週必ず払いますから、待ってください。", ["a 払う", "b 払え", "c 払える"], "b", "グループⅠ動詞「払う」の命令形「払え」。", "Group 1 verb imperative form: 払え."),
    make_mc("sec10_q3", "section_10_practice", "A「そんなに笑わないでくださいよ。」\nB「（　）と言われても、おかしくてどうしても笑ってしまいますよ。」", ["a 笑って", "b 笑え", "c 笑うな"], "c", "「笑わないで」を命令形引用で受ける禁止形「笑うな」。", "Prohibitive quotation form: 笑うな."),
    make_mc("sec10_q4", "section_10_practice", "【張り紙】部屋を出るときは電気を（　）こと。", ["a 消す", "b 消している", "c 消した"], "a", "掲示による指示・規則には辞書形＋こと。「消すこと」。", "Written rule/instruction: 消すこと."),
    make_mc("sec10_q5", "section_10_practice", "【立て札】芝生に（　）。", ["a 入らないこと", "b 入れないこと", "c 入らないことだ"], "a", "禁止の規則掲示「入らないこと」。", "Prohibition notice: 入らないこと."),
    make_mc("sec10_q6", "section_10_practice", "森田君、いつも遅いね。新入社員はもっと早く会社に（　）だよ。", ["a 来べき", "b 来るべき", "c 来べき"], "b", "動詞「来る」は「来るべき（くるべき）」と接続する。", "Connection with べき: 来るべき."),
    make_mc("sec10_q7", "section_10_practice", "そんなにたくさんのお金を友だちから（　）。友だちも困るだろう。", ["a 借りるべきではない", "b 借りるべきだ", "c 借りないべきだ"], "a", "否定の義務・助言は「借りるべきではない」。", "Negative obligation: 借りるべきではない."),
    make_mc("sec10_q8", "section_10_practice", "日本の法律では、二十歳になっていない人はお酒を（　）。", ["a 飲めません", "b 飲むべきではありません", "c 飲むことではありません"], "a", "法律上の禁止・不可を表す「飲めません（飲んではいけません）」。", "Legal incapacity/rule: 飲めません."),
    make_mc("sec10_q9", "section_10_practice", "机の上が暗すぎませんか。もう少し（　）どうですか。", ["a 明るくなったら", "b 明るくしたら", "c 明るかったら"], "b", "意図的な行為の提案なので「明るくしたらどうですか」。", "Suggestion: 明るくしたらどうですか."),
    make_mc("sec10_q10", "section_10_practice", "ちょっと調べたいことがあるんですが、このパソコンを（　）。", ["a 使ったらどうですか", "b 使うのがどうですか", "c 使ってもいいですか"], "c", "自分がパソコンを使う許可を求めているので「使ってもいいですか」が適切。", "Asking permission: 使ってもいいですか.")
]

# Combined Drills: 練習 9・10課 (p.49)
sec9_10_combined_drills = [
    make_mc("sec9_10_q1", "section_9_10_combined", "わあ。ゆう子さん、着物が似合いますね。国の家族に見せたいので、写真を（　）。", ["a 撮ってもいいですか", "b 撮ったらどうですか", "c 撮ってほしいのですが"], "a", "写真を撮影する許可を求める「撮ってもいいですか」。", "Asking permission to take photo: 撮ってもいいですか."),
    make_mc("sec9_10_q2", "section_9_10_combined", "来月わたしたちのダンスの発表会があります。ぜひ皆さんで見に（　）です。", ["a 来たい", "b 来てほしい", "c 来させてほしい"], "b", "相手に見に来てもらいたい希望「見に来てほしい」。", "Wishing for audience to attend: 来てほしい."),
    make_mc("sec9_10_q3", "section_9_10_combined", "じょうだんを（　）です。わたしはまじめに話しているんです。", ["a 言わないといい", "b 言わないでもらいたい", "c 言わせないでほしい"], "b", "相手に対する要求「言わないでもらいたい」。", "Requesting not to joke: 言わないでもらいたい."),
    make_mc("sec9_10_q4", "section_9_10_combined", "すみません。このピアノ練習室をわたしにも（　）のですが。", ["a 使ってもらいたい", "b 使われるといい", "c 使わせてほしい"], "c", "自分が使用する許可の希望「使わせてほしい」。", "Asking permission for oneself: 使わせてほしい."),
    make_mc("sec9_10_q5", "section_9_10_combined", "どの学校を選ぶか、もっとよく考えて（　）と今では残念に思っている。", ["a 決めるべきだった", "b 決めるといい", "c 決めたらどうか"], "a", "過去の行動に対する後悔・反省「決めるべきだった」。", "Past regret: 決めるべきだった."),
    make_mc("sec9_10_q6", "section_9_10_combined", "店長、わたしたちにもう少し休みを（　）。働きすぎです。", ["a とったらどうですか", "b とればいいです", "c とらせていただきたいです"], "c", "休暇を許可してもらう謙譲の希望「とらせていただきたいです」。", "Polite humble request: とらせていただきたいです."),
    make_mc("sec9_10_q7", "section_9_10_combined", "彼女にあんなことを言う（　）。きっと彼女は怒っているだろう。", ["a べきではなかった", "b ことではなかった", "c わけではなかった"], "a", "言ったことに対する後悔・反省「言うべきではなかった」。", "Past regret for saying something hurtful: べきではなかった."),
    make_mc("sec9_10_q8", "section_9_10_combined", "入国するときも出国するときも、空港でパスポートを（　）。", ["a 見せるべきです", "b 見せるといいです", "c 見せなければなりません"], "c", "義務・法的規則「見せなければなりません」。", "Legal obligation: 見せなければなりません."),
    make_mc("sec9_10_q9", "section_9_10_combined", "9時半か。弟の試験は9時からだと言っていたから、もう始まっている（　）。", ["a といい", "b はずだ", "c べきだ"], "b", "確実な推測・論理的帰結「始まっているはずだ」。", "Logical expectation: はずだ.")
]
