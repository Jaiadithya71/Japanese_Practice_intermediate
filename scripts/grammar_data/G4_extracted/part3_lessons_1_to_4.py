"""
Module: part3_lessons_1_to_4.py
Part 3: 文章の文法 (Grammar in Text / Passage Cloze)
Lessons 1 to 4 + Review Tests 1-2 & 3-4 (Images 118-129, p. 116-127).
"""

def get_lessons_1_to_4():
    # =========================================================================
    # Lesson 1: 1課 文の始めと終わりの対応 (p. 116-117, Images 118-119)
    # =========================================================================
    sec1 = {
        "section_number": 1,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>課<rt>か</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>始<rt>はじ</rt></ruby>めと<ruby>終<rt>お</rt></ruby>わりの<ruby>対応<rt>たいおう</rt></ruby>",
        "title_en": "Lesson 1: Correspondence Between the Beginning and End of a Sentence",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>にはまとまりが<ruby>必要<rt>ひつよう</rt></ruby>です。その<ruby>基本<rt>きほん</rt></ruby>は、<ruby>一<rt>ひと</rt></ruby>つ<ruby>一<rt>ひと</rt></ruby>つの<ruby>文<rt>ぶん</rt></ruby>で<ruby>始<rt>はじ</rt></ruby>めと<ruby>終<rt>お</rt></ruby>わりが<ruby>正<rt>ただ</rt></ruby>しく<ruby>対応<rt>たいおう</rt></ruby>していることです。",
        "theme_en": "Paragraphs and statements need to be cohesive. The basic means to achieve this is to ensure that beginning and final grammatical patterns correspond for each sentence.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>始<rt>はじ</rt></ruby>めと<ruby>終<rt>お</rt></ruby>わりの<ruby>対応<rt>たいおう</rt></ruby>にはいくつかの<ruby>型<rt>かた</rt></ruby>があります。",
                "title_en": "There are a number of patterns for ensuring the beginning and end of a sentence correspond.",
                "patterns": [
                    {
                        "pattern": "〜には　＋…がいる・…がある・…が<ruby>多<rt>おお</rt></ruby>い",
                        "examples": [
                            {
                                "japanese": "<ruby>世界<rt>せかい</rt></ruby>にはいろいろな<ruby>文化<rt>ぶんか</rt></ruby>を<ruby>持<rt>も</rt></ruby>った<ruby>国<rt>くに</rt></ruby>がある。",
                                "english": "In the world, there are countries with various cultures."
                            },
                            {
                                "japanese": "この<ruby>計画<rt>けいかく</rt></ruby>には<ruby>問題点<rt>もんだいてん</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。",
                                "english": "There are many problematic points in this plan."
                            }
                        ]
                    },
                    {
                        "pattern": "〜には・〜のに（は）　＋…が<ruby>必要<rt>ひつよう</rt></ruby>だ・…が<ruby>便利<rt>べんり</rt></ruby>だ・…なければならない・…がかかる",
                        "reference": "第1部 C",
                        "examples": [
                            {
                                "japanese": "この<ruby>仕事<rt>しごと</rt></ruby>をするには<ruby>車<rt>くるま</rt></ruby>の<ruby>運転<rt>うんてん</rt></ruby>ができなければならない。",
                                "english": "In order to do this job, one must be able to drive a car."
                            },
                            {
                                "japanese": "<ruby>外国<rt>がいこく</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くのにはパスポートが<ruby>必要<rt>ひつよう</rt></ruby>だ。",
                                "english": "A passport is necessary to travel abroad."
                            }
                        ]
                    },
                    {
                        "pattern": "〜のは　＋…だ・…からだ・…ためだ",
                        "reference": "第1部 C",
                        "examples": [
                            {
                                "japanese": "わたしが<ruby>祖母<rt>そば</rt></ruby>について<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>せるのは、<ruby>優<rt>やさ</rt></ruby>しい<ruby>笑顔<rt>えがお</rt></ruby>だけだ。",
                                "english": "What I can remember about my grandmother is only her gentle smile."
                            },
                            {
                                "japanese": "<ruby>昨夜<rt>さくや</rt></ruby><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>れなかったのは、<ruby>急<rt>いそ</rt></ruby>ぎの<ruby>仕事<rt>しごと</rt></ruby>が<ruby>終<rt>お</rt></ruby>わらなかったからです。",
                                "english": "The reason I could not go home last night was because urgent work did not finish."
                            }
                        ]
                    },
                    {
                        "pattern": "どうして／なぜ〜かというと　＋…からだ",
                        "reference": "第2部 1課・4",
                        "examples": [
                            {
                                "japanese": "どうしてこの<ruby>植物<rt>しょくぶつ</rt></ruby>にあまり<ruby>水<rt>みず</rt></ruby>をやらないかというと、その<ruby>方<rt>ほう</rt></ruby>がきれいに<ruby>花<rt>はな</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>くからです。",
                                "english": "If you ask why I don't give much water to this plant, it's because doing so makes prettier flowers bloom."
                            },
                            {
                                "japanese": "なぜこの<ruby>仕事<rt>しごと</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んだかというと、<ruby>子<rt>こ</rt></ruby>どものときから<ruby>動物<rt>どうぶつ</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだったからだ。",
                                "english": "If you ask why I chose this job, it's because I've loved animals since childhood."
                            }
                        ]
                    }
                ]
            },
            {
                "point_number": 2,
                "title": "<ruby>長<rt>なが</rt></ruby>い<ruby>文<rt>ぶん</rt></ruby>では<ruby>助詞<rt>じょし</rt></ruby>と、それに<ruby>対応<rt>たいおう</rt></ruby>する<ruby>動詞<rt>どうし</rt></ruby>が<ruby>離<rt>はな</rt></ruby>れていることがあります。<ruby>受身文<rt>うけみぶん</rt></ruby>や<ruby>使役文<rt>しえきぶん</rt></ruby>などでは<ruby>助詞<rt>じょし</rt></ruby>と<ruby>動詞<rt>どうし</rt></ruby>の<ruby>対応<rt>たいおう</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えると、<ruby>言<rt>い</rt></ruby>いたいことが<ruby>正<rt>ただ</rt></ruby>しく<ruby>伝<rt>つた</rt></ruby>えられないことがあるので<ruby>特<rt>とく</rt></ruby>に<ruby>注意<rt>ちゅうい</rt></ruby>しましょう。",
                "title_en": "In longer sentences, the particle and the verb that goes with it can be far apart. Pay particular attention to passive and causative sentences, ensuring correct correspondence between particle and verb.",
                "reference": "第3部 5課",
                "examples": [
                    {
                        "japanese": "あしたリーさんに、だれか<ruby>中国料理<rt>ちゅうごくりょうり</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれる<ruby>人<rt>ひと</rt></ruby>を<ruby>紹介<rt>しょうかい</rt></ruby>してもらおう。",
                        "english": "Tomorrow I will ask Mr. Lee to introduce someone who will teach me Chinese cooking."
                    },
                    {
                        "japanese": "<ruby>母親<rt>ははおや</rt></ruby>は<ruby>子<rt>こ</rt></ruby>どもたちに、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>を<ruby>毎週<rt>まいしゅう</rt></ruby>1<ruby>回<rt>かい</rt></ruby>きれいに<ruby>片付<rt>かたづ</rt></ruby>けさせた。",
                        "english": "The mother made her children clean their rooms thoroughly once a week."
                    },
                    {
                        "japanese": "わたしは<ruby>先生<rt>せんせい</rt></ruby>に、その<ruby>文<rt>ぶん</rt></ruby>をすらすら<ruby>読<rt>よ</rt></ruby>めるようになるまで<ruby>何度<rt>なんど</rt></ruby>も<ruby>読<rt>よ</rt></ruby>まされた。",
                        "english": "I was made by the teacher to read that sentence over and over until I could read it fluently."
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30101,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>今<rt>いま</rt></ruby>、<ruby>困<rt>こま</rt></ruby>っているのは、＿＿＿。",
                "options": [
                    "a　<ruby>お金<rt>かね</rt></ruby>のことだ。",
                    "b　<ruby>お金<rt>かね</rt></ruby>が<ruby>足<rt>た</rt></ruby>りない。"
                ],
                "correct_answer": "a",
                "explanation_ja": "「〜のは…だ」の文型。「困っているのは、お金のことだ」と名詞で受ける。",
                "explanation_en": "Matches the pattern '〜のは…だ'. Must conclude with a noun predicate ('お金のことだ')."
            },
            {
                "question_id": 30102,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>初<rt>はじ</rt></ruby>めて<ruby>飛行機<rt>ひこうき</rt></ruby>に<ruby>乗<rt>の</rt></ruby>ったのは、20<ruby>年前<rt>ねんまえ</rt></ruby>に＿＿＿。",
                "options": [
                    "a　<ruby>両親<rt>りょうしん</rt></ruby>とアメリカへ<ruby>行<rt>い</rt></ruby>った。",
                    "b　<ruby>両親<rt>りょうしん</rt></ruby>とアメリカへ<ruby>行<rt>い</rt></ruby>ったときだ。"
                ],
                "correct_answer": "b",
                "explanation_ja": "「〜のは…ときだ」の対応。「〜たときだ」が正しい結び。",
                "explanation_en": "Corresponds to '〜のは…ときだ'. The predicate must describe the time ('〜たときだ')."
            },
            {
                "question_id": 30103,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>今朝<rt>けさはや</rt></ruby><ruby>早<rt>はや</rt></ruby>く＿＿＿、<ruby>昨夜<rt>さくや</rt></ruby>お<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みすぎたからだ。",
                "options": [
                    "a　<ruby>起<rt>お</rt></ruby>きられなくて、",
                    "b　<ruby>起<rt>お</rt></ruby>きられなかったのは、"
                ],
                "correct_answer": "b",
                "explanation_ja": "文末が「〜からだ」（理由）なので、文頭は「〜のは…からだ」の形をとる。",
                "explanation_en": "Because the sentence ends with '〜からだ' (reason), the beginning must correspond with '〜のは'."
            },
            {
                "question_id": 30104,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "どうしてこの<ruby>計画<rt>けいかく</rt></ruby>が<ruby>中止<rt>ちゅうし</rt></ruby>になったかというと、＿＿＿。",
                "options": [
                    "a　<ruby>予算<rt>よさん</rt></ruby>が<ruby>足<rt>た</rt></ruby>りません。",
                    "b　<ruby>予算<rt>よさん</rt></ruby>が<ruby>足<rt>た</rt></ruby>りないからです。"
                ],
                "correct_answer": "b",
                "explanation_ja": "「どうして〜かというと…からだ」の定型呼応。",
                "explanation_en": "'どうして〜かというと' corresponds with '〜からだ' at the end."
            },
            {
                "question_id": 30105,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "この<ruby>地方<rt>ちほう</rt></ruby>には<ruby>昔<rt>むかし</rt></ruby>から<ruby>続<rt>つづ</rt></ruby>いている＿＿＿。",
                "options": [
                    "a　<ruby>伝統的<rt>でんとうてき</rt></ruby>な<ruby>行事<rt>ぎょうじ</rt></ruby>がある。",
                    "b　<ruby>伝統的<rt>でんとうてき</rt></ruby>な<ruby>行事<rt>ぎょうじ</rt></ruby>を<ruby>見<rt>み</rt></ruby>ることができる。"
                ],
                "correct_answer": "a",
                "explanation_ja": "「この地方には…がある」の対応。「〜には」に対して「〜がある」で受ける。",
                "explanation_en": "'この地方には' pairs with '…がある' to indicate existence in this region."
            },
            {
                "question_id": 30106,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>山<rt>やま</rt></ruby>の<ruby>頂上<rt>ちょうじょう</rt></ruby>まで<ruby>行<rt>い</rt></ruby>くには、ここからさらに2<ruby>時間<rt>じかん</rt></ruby>ぐらい＿＿＿。",
                "options": [
                    "a　<ruby>登<rt>のぼ</rt></ruby>っていこう。",
                    "b　<ruby>登<rt>のぼ</rt></ruby>らなければならない。"
                ],
                "correct_answer": "b",
                "explanation_ja": "「〜には…なければならない／かかる」の対応。目的達成の必要条件を表す。",
                "explanation_en": "'〜には' pairs with '…なければならない' to state a necessary condition for reaching the destination."
            },
            {
                "question_id": 30107,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "つよしは冗談を言っていつもみんなを＿＿＿。",
                "options": [
                    "a　<ruby>笑<rt>わら</rt></ruby>わせるから、クラスの<ruby>人気者<rt>にんきもの</rt></ruby>だ。",
                    "b　<ruby>笑<rt>わら</rt></ruby>われるのは、なんだかわいそうだ。"
                ],
                "correct_answer": "a",
                "explanation_ja": "「つよしは…みんなを［笑わせる］」と使役が呼応する（助詞「を」に対応）。",
                "explanation_en": "Takes 'みんなを笑わせる' (causative) corresponding to particle 'を'."
            },
            {
                "question_id": 30108,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>林<rt>はやし</rt></ruby>さんはピアノが<ruby>好<rt>す</rt></ruby>きで、<ruby>子<rt>こ</rt></ruby>どもにも<ruby>小<rt>ちい</rt></ruby>さいときからずっと＿＿＿。",
                "options": [
                    "a　<ruby>習<rt>なら</rt></ruby>っていた。",
                    "b　<ruby>習<rt>なら</rt></ruby>わせていた。"
                ],
                "correct_answer": "b",
                "explanation_ja": "「子どもにも…習わせていた」（使役）。「〜に…させる」の助詞と動詞の対応。",
                "explanation_en": "'子どもにも…習わせていた' (causative) matches particle 'に'."
            },
            {
                "question_id": 30109,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "この<ruby>学校<rt>がっこう</rt></ruby>ではバイクで<ruby>通学<rt>つうがく</rt></ruby>することを＿＿＿。",
                "options": [
                    "a　10<ruby>年前<rt>ねんまえ</rt></ruby>から<ruby>校則<rt>こうそく</rt></ruby>で<ruby>禁止<rt>きんし</rt></ruby>している。",
                    "b　<ruby>生徒会<rt>せいとかい</rt></ruby>で<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>った<ruby>結果<rt>けっか</rt></ruby>、<ruby>禁止<rt>きんし</rt></ruby>された。"
                ],
                "correct_answer": "a",
                "explanation_ja": "「通学することを…禁止している」（他動詞・能動）。「を」と呼応するのは他動詞句。",
                "explanation_en": "'…通学することを禁止している' (active transitive verb) corresponds to particle 'を'."
            },
            {
                "question_id": 30110,
                "category": "第3部 1課 練習",
                "question_type": "binary_choice",
                "prompt": "わたしは<ruby>母<rt>はは</rt></ruby>に、<ruby>寒<rt>さむ</rt></ruby>い<ruby>朝<rt>あさ</rt></ruby>でも<ruby>向<rt>む</rt></ruby>こうの<ruby>角<rt>かど</rt></ruby>の<ruby>所<rt>ところ</rt></ruby>までごみを<ruby>出<rt>だ</rt></ruby>しに＿＿＿。",
                "options": [
                    "a　<ruby>行<rt>い</rt></ruby>かされる。",
                    "b　<ruby>行<rt>い</rt></ruby>くことになる。"
                ],
                "correct_answer": "a",
                "explanation_ja": "「わたしは母に…行かされる」（使役受身）。「〜は…に〜させられる」の呼応。",
                "explanation_en": "'わたしは母に…行かされる' (causative-passive) corresponds to '〜は…に'."
            }
        ]
    }

    # =========================================================================
    # Lesson 2: 2課 時制・〜ている (p. 118-119, Images 120-121)
    # =========================================================================
    sec2 = {
        "section_number": 2,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>課<rt>か</rt></ruby> <ruby>時制<rt>じせい</rt></ruby>・〜ている",
        "title_en": "Lesson 2: Tense & '~te iru'",
        "theme": "まとまりのある<ruby>文章<rt>ぶんしょう</rt></ruby>にするためには、できごとの<ruby>時間的<rt>じかんてき</rt></ruby><ruby>前後関係<rt>ぜんごかんけい</rt></ruby>に<ruby>注意<rt>ちゅうい</rt></ruby>して<ruby>文<rt>ぶん</rt></ruby>を<ruby>続<rt>つづ</rt></ruby>けなければなりません。また、ある<ruby>時点<rt>じてん</rt></ruby>で<ruby>起<rt>お</rt></ruby>こったことか、<ruby>続<rt>つづ</rt></ruby>いている<ruby>状態<rt>じょうたい</rt></ruby>かを<ruby>確<rt>たし</rt></ruby>かめて、「〜ている」を<ruby>正<rt>ただ</rt></ruby>しく<ruby>使<rt>つか</rt></ruby>うことが<ruby>大切<rt>たいせつ</rt></ruby>です。",
        "theme_en": "To make a cohesive statement, you have to pay attention to the timing of actions and events of preceding and following sentences. In addition, it is important to correctly use the ~te iru form for things that happened at a certain point in time, or are ongoing.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>時間<rt>じかん</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>言葉<rt>ことば</rt></ruby>と<ruby>動詞<rt>どうし</rt></ruby>の<ruby>形<rt>かたち</rt></ruby>とを<ruby>合<rt>あ</rt></ruby>わせます。",
                "title_en": "Words that express time and verb forms must agree.",
                "examples": [
                    {
                        "japanese": "・まもなく／もうすぐ／やがて／<ruby>来年<rt>らいねん</rt></ruby>など　＋この<ruby>子<rt>こ</rt></ruby>は5<ruby>歳<rt>さい</rt></ruby>になる。（<ruby>現在形<rt>げんざいけい</rt></ruby>）",
                        "english": "Soon / shortly / next year, etc. + This child will turn 5 years old. (Present/non-past form)"
                    },
                    {
                        "japanese": "・<ruby>今<rt>いま</rt></ruby>／<ruby>現在<rt>げんざい</rt></ruby>など　＋<ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っている。（〜ている）",
                        "english": "Now / currently, etc. + Snow is falling. (~te iru)"
                    },
                    {
                        "japanese": "・<ruby>去年<rt>きょねん</rt></ruby>／<ruby>先週<rt>せんしゅう</rt></ruby>／4<ruby>月<rt>がつ</rt></ruby>1<ruby>日<rt>ついたち</rt></ruby>になど　＋わたしは<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>た。（<ruby>過去形<rt>かこけい</rt></ruby>）",
                        "english": "Last year / last week / on April 1st, etc. + I came to Japan. (Past form)"
                    }
                ]
            },
            {
                "point_number": 2,
                "title": "「〜ている」の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>",
                "title_en": "Usage of '~te iru'",
                "usage_table": [
                    {
                        "meaning": "<ruby>進行中<rt>しんこうちゅう</rt></ruby>の<ruby>動作<rt>どうさ</rt></ruby>",
                        "meaning_en": "Actions in progress",
                        "example": "わたしはそのとき<ruby>旅行<rt>りょこう</rt></ruby>の<ruby>準備<rt>じゅんび</rt></ruby>をしていた。"
                    },
                    {
                        "meaning": "<ruby>習慣<rt>しゅうかん</rt></ruby>",
                        "meaning_en": "Custom / habitual action",
                        "example": "<ruby>弟<rt>おとうと</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby>サッカーの<ruby>練習<rt>れんしゅう</rt></ruby>に<ruby>行<rt>い</rt></ruby>っている。"
                    },
                    {
                        "meaning": "<ruby>結果<rt>けっか</rt></ruby>が<ruby>残<rt>のこ</rt></ruby>っている<ruby>状態<rt>じょうたい</rt></ruby>",
                        "meaning_en": "State resulting from an action continues",
                        "example": "<ruby>駅<rt>えき</rt></ruby>のホームに<ruby>財布<rt>さいふ</rt></ruby>が<ruby>落<rt>お</rt></ruby>ちていた。／<ruby>町田<rt>まちだ</rt></ruby>さんはめがねをかけている。"
                    },
                    {
                        "meaning": "<ruby>形<rt>かたち</rt></ruby>・<ruby>様子<rt>ようす</rt></ruby>",
                        "meaning_en": "Form and appearance",
                        "example": "この<ruby>道<rt>みち</rt></ruby>は<ruby>海<rt>うみ</rt></ruby>に<ruby>続<rt>つづ</rt></ruby>いている。／<ruby>弟<rt>おとうと</rt></ruby>とぼくはあまり<ruby>似<rt>に</rt></ruby>ていない。"
                    },
                    {
                        "meaning": "<ruby>完了<rt>かんりょう</rt></ruby>・<ruby>未完了<rt>みかんりょう</rt></ruby>",
                        "meaning_en": "Expresses completion or incompleteness",
                        "example": "10<ruby>年後<rt>ねんご</rt></ruby>、<ruby>彼女<rt>かのじょ</rt></ruby>も<ruby>母親<rt>ははおや</rt></ruby>になっているだろうか。／9<ruby>時<rt>じ</rt></ruby>に<ruby>会場<rt>かいじょう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いた。もうみんな<ruby>来<rt>き</rt></ruby>ていた。／この<ruby>子<rt>こ</rt></ruby>はまだ5<ruby>歳<rt>さい</rt></ruby>になっていません。"
                    }
                ]
            },
            {
                "point_number": 3,
                "title": "「〜とき」の<ruby>前<rt>まえ</rt></ruby>の<ruby>動詞<rt>どうし</rt></ruby>や、<ruby>名詞<rt>めいし</rt></ruby>を<ruby>説明<rt>せつめい</rt></ruby>する<ruby>文<rt>ぶん</rt></ruby>の<ruby>動詞<rt>どうし</rt></ruby>の<ruby>時制<rt>じせい</rt></ruby>は、<ruby>文全体<rt>ぶんぜんたい</rt></ruby>の<ruby>最後<rt>さいご</rt></ruby>の<ruby>動詞<rt>どうし</rt></ruby>のできごとより<ruby>先<rt>さき</rt></ruby>に<ruby>起<rt>お</rt></ruby>こることか、<ruby>後<rt>あと</rt></ruby>に<ruby>起<rt>お</rt></ruby>こることかを<ruby>考<rt>かんが</rt></ruby>えて<ruby>決<rt>き</rt></ruby>めます。",
                "title_en": "The tense of the verb coming before とき, and of the verb that modifies the noun, depends on whether the actions happen before or after the event described by the verb at the end of the sentence.",
                "examples": [
                    {
                        "japanese": "ご<ruby>飯<rt>はん</rt></ruby>を<ruby>食<rt>た</rt></ruby>べたとき、「ごちそうさま」と<ruby>言<rt>い</rt></ruby>います。（<ruby>食<rt>た</rt></ruby>べる→<ruby>言<rt>い</rt></ruby>う）",
                        "english": "When we have finished eating, we say 'Gochisousama'. (eat -> say)"
                    },
                    {
                        "japanese": "ご<ruby>飯<rt>はん</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるとき、「いただきます」と<ruby>言<rt>い</rt></ruby>います。（<ruby>言<rt>い</rt></ruby>う→<ruby>食<rt>た</rt></ruby>べる）",
                        "english": "When we are about to eat, we say 'Itadakimasu'. (say -> eat)"
                    },
                    {
                        "japanese": "いつもいちばん<ruby>早<rt>はや</rt></ruby>く<ruby>来<rt>き</rt></ruby>た<ruby>人<rt>ひと</rt></ruby>がエアコンをつけます。（<ruby>来<rt>く</rt></ruby>る→つける）",
                        "english": "The person who arrived first always turns on the air conditioner."
                    },
                    {
                        "japanese": "<ruby>新幹線<rt>しんかんせん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>飲<rt>の</rt></ruby>むお<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>駅<rt>えき</rt></ruby>の<ruby>売店<rt>ばいてん</rt></ruby>で<ruby>買<rt>か</rt></ruby>った。（<ruby>買<rt>か</rt></ruby>う→<ruby>飲<rt>の</rt></ruby>む）",
                        "english": "I bought tea at the station kiosk to drink inside the Shinkansen."
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30201,
                "category": "第3部 2課 練習1",
                "question_type": "binary_choice",
                "prompt": "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>いておいたぼくの<ruby>大事<rt>だいじ</rt></ruby>な<ruby>本<rt>ほん</rt></ruby>はどこに（a <ruby>行<rt>い</rt></ruby>く　b <ruby>行<rt>い</rt></ruby>った）のだろう。",
                "options": ["a 行く", "b 行った"],
                "correct_answer": "b",
                "explanation_ja": "本がなくなった過去の事実を指すため過去形「行った」が適切。",
                "explanation_en": "Refers to the past fact that the book is gone; past tense '行った' is correct."
            },
            {
                "question_id": 30202,
                "category": "第3部 2課 練習1",
                "question_type": "binary_choice",
                "prompt": "<ruby>来月<rt>らいげつ</rt></ruby>、わたしがこの5<ruby>年間<rt>ねんかん</rt></ruby>で（a <ruby>作<rt>つく</rt></ruby>る　b <ruby>作<rt>つく</rt></ruby>った）<ruby>作品<rt>さくひん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>かれます。",
                "options": ["a 作る", "b 作った"],
                "correct_answer": "b",
                "explanation_ja": "「この5年間ですでに作った作品」なので過去形修飾。",
                "explanation_en": "Modifies works already created over the past 5 years; past form '作った'."
            },
            {
                "question_id": 30203,
                "category": "第3部 2課 練習1",
                "question_type": "binary_choice",
                "prompt": "<ruby>駅<rt>えき</rt></ruby>まで<ruby>遠<rt>とお</rt></ruby>いですから、<ruby>歩<rt>ある</rt></ruby>いていくのでは（a <ruby>疲<rt>つか</rt></ruby>れますよ　b <ruby>疲<rt>つか</rt></ruby>れていますよ）。",
                "options": ["a 疲れますよ", "b 疲れていますよ"],
                "correct_answer": "a",
                "explanation_ja": "これからの動作の結果を予想して注意を促すので「疲れますよ」。",
                "explanation_en": "Predicts a future state of getting tired; '疲れますよ'."
            },
            {
                "question_id": 30204,
                "category": "第3部 2課 練習1",
                "question_type": "binary_choice",
                "prompt": "きのうわたしは12<ruby>時<rt>じ</rt></ruby><ruby>過<rt>す</rt></ruby>ぎまで（a <ruby>起<rt>お</rt></ruby>きた　b <ruby>起<rt>お</rt></ruby>きていた）。",
                "options": ["a 起きた", "b 起きていた"],
                "correct_answer": "b",
                "explanation_ja": "12時過ぎまで起きている状態が継続していたので「起きていた」。",
                "explanation_en": "A continuous state of staying awake until past midnight; '起きていた'."
            },
            {
                "question_id": 30205,
                "category": "第3部 2課 練習1",
                "question_type": "binary_choice",
                "prompt": "まだ<ruby>昼<rt>ひる</rt></ruby>ご<ruby>飯<rt>はん</rt></ruby>を（a <ruby>食<rt>た</rt></ruby>べない　b <ruby>食<rt>た</rt></ruby>べていない）のなら、いっしょにどうですか。",
                "options": ["a 食べない", "b 食べていない"],
                "correct_answer": "b",
                "explanation_ja": "「まだ〜ていない」（未完了）。",
                "explanation_en": "'まだ〜ていない' indicates an action not yet completed."
            },
            {
                "question_id": 30206,
                "category": "第3部 2課 練習1",
                "question_type": "binary_choice",
                "prompt": "うちに（a <ruby>来<rt>く</rt></ruby>る　b <ruby>来<rt>き</rt></ruby>た）ときは、<ruby>連絡<rt>れんらく</rt></ruby>してください。<ruby>駅<rt>えき</rt></ruby>まで<ruby>迎<rt>むか</rt></ruby>えに<ruby>行<rt>い</rt></ruby>きます。",
                "options": ["a 来る", "b 来た"],
                "correct_answer": "a",
                "explanation_ja": "「うちに来る前に駅で連絡する」ので、来る前の動作として辞書形「来る」。",
                "explanation_en": "Contact before actually arriving; dictionary form '来る'."
            },
            {
                "question_id": 30207,
                "category": "第3部 2課 練習1",
                "question_type": "two_part_choice",
                "prompt": "<ruby>彼<rt>かれ</rt></ruby>が<ruby>港<rt>みなと</rt></ruby>に（① a <ruby>着<rt>つ</rt></ruby>いた　b <ruby>着<rt>つ</rt></ruby>いている）ときには、<ruby>船<rt>ふね</rt></ruby>はもう（② a <ruby>出<rt>で</rt></ruby>た　b <ruby>出<rt>で</rt></ruby>ていた）。",
                "options": ["① a 着いた / ② b 出ていた", "① b 着いている / ② a 出た"],
                "correct_answer": "①a, ②b",
                "explanation_ja": "彼が港に到着した時点で、船はすでに出航した結果の状態だった（①着いた、②出ていた）。",
                "explanation_en": "When he arrived at the port (着いた), the ship had already departed (出ていた)."
            },
            {
                "question_id": 30208,
                "category": "第3部 2課 練習1",
                "question_type": "two_part_choice",
                "prompt": "あした、<ruby>林<rt>はやし</rt></ruby>さんに（① a <ruby>会<rt>あ</rt></ruby>う　b <ruby>会<rt>あ</rt></ruby>った）ときに、この<ruby>本<rt>ほん</rt></ruby>を（② a <ruby>返<rt>かえ</rt></ruby>そう　b <ruby>返<rt>かえ</rt></ruby>した）。",
                "options": ["① a 会う / ② a 返そう", "① b 会った / ② b 返した"],
                "correct_answer": "①b, ②a",
                "explanation_ja": "「あした会ったときに返そう」（会うという事態が成立した時点で返す意向）。①b 会った、②a 返そう。",
                "explanation_en": "At the point when I meet Hayashi tomorrow (会ったとき), I intend to return the book (返そう)."
            },
            {
                "question_id": 30209,
                "category": "第3部 2課 練習2",
                "question_type": "cloze_conjugation",
                "prompt": "<ruby>子<rt>こ</rt></ruby>どものころ、わたしのうちにはいろいろな<ruby>動物<rt>どうぶつ</rt></ruby>が（①いる→＿＿＿）。<ruby>犬<rt>いぬ</rt></ruby>はもちろん、うさぎ、<ruby>鳥<rt>とり</rt></ruby>、にわとりなど、みんな<ruby>母<rt>はは</rt></ruby>がどこからか（②もらう・くる→＿＿＿）が、これらの<ruby>動物<rt>どうぶつ</rt></ruby>にえさを（③やる→＿＿＿）のはわたしの<ruby>仕事<rt>しごと</rt></ruby>だった。わたしは<ruby>母<rt>はは</rt></ruby>が<ruby>入<rt>い</rt></ruby>れ<ruby>物<rt>もの</rt></ruby>に（④入る・入れる→＿＿＿）えさを<ruby>自分<rt>じぶん</rt></ruby>の<ruby>手<rt>て</rt></ruby>で<ruby>動物<rt>どうぶつ</rt></ruby>たちに<ruby>与<rt>あた</rt></ruby>えた。<ruby>当時<rt>とうじ</rt></ruby>わたしはまだ<ruby>小学生<rt>しょうがくせい</rt></ruby>に（⑤なる→＿＿＿）が、<ruby>母<rt>はは</rt></ruby>の<ruby>影響<rt>えいきょう</rt></ruby>でいつの<ruby>間<rt>ま</rt></ruby>にか<ruby>大<rt>だい</rt></ruby>の<ruby>動物<rt>どうぶつ</rt></ruby><ruby>好<rt>す</rt></ruby>きになっていた。だから、<ruby>動物園<rt>どうぶつえん</rt></ruby>に（⑥<ruby>就職<rt>しゅうしょく</rt></ruby>できる→＿＿＿）ときは、<ruby>本当<rt>ほんとう</rt></ruby>にうれしかった。",
                "sub_questions": [
                    {"blank": "①", "correct": "いた"},
                    {"blank": "②", "correct": "もらってきた"},
                    {"blank": "③", "correct": "持っていた / やる"},
                    {"blank": "④", "correct": "やる / 入れた"},
                    {"blank": "⑤", "correct": "なっていなかった"},
                    {"blank": "⑥", "correct": "就職できた"}
                ],
                "correct_answers": ["1. いた", "2. もらってきた", "3. 持っていた", "4. やる", "5. 入れた", "6. なっていなかった", "7. 就職できた"],
                "explanation_ja": "解答冊子p.6参照：1.いた 2.もらってきた 3.持っていた 4.やる 5.入れた 6.なっていなかった 7.就職できた。",
                "explanation_en": "See Answer booklet p.6: 1.いた 2.もらってきた 3.持っていた 4.やる 5.入れた 6.なっていなかった 7.就職できた."
            }
        ]
    }

    # =========================================================================
    # Review Test 1-2: まとめ問題 (1課・2課) (p. 120-121, Images 122-123)
    # =========================================================================
    matome_1_2 = {
        "section_number": 2.5,
        "title": "まとめ<ruby>問題<rt>もんだい</rt></ruby>（1<ruby>課<rt>か</rt></ruby>・2<ruby>課<rt>か</rt></ruby>）",
        "title_en": "Review Exercises (Lessons 1 & 2)",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>総合練習<rt>そうごうれんしゅう</rt></ruby>（<ruby>文<rt>ぶん</rt></ruby>の<ruby>対応<rt>たいおう</rt></ruby>と<ruby>時制<rt>じせい</rt></ruby>）",
        "theme_en": "Comprehensive text grammar review: Sentence correspondence and tense",
        "passages": [
            {
                "passage_id": 301,
                "title": "外国語の勉強",
                "title_en": "Studying Foreign Languages",
                "text": "わたしは<ruby>言葉<rt>ことば</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>今<rt>いま</rt></ruby>までにいくつかの<ruby>外国語<rt>がいこくご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>したことがあります。<ruby>日本語<rt>にほんご</rt></ruby>は<ruby>国<rt>くに</rt></ruby>にいるとき1<ruby>年<rt>ねん</rt></ruby>ぐらい<ruby>勉強<rt>べんきょう</rt></ruby>しましたが、<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>てからも<ruby>続<rt>つづ</rt></ruby>けています。<ruby>今<rt>いま</rt></ruby>、<ruby>毎週<rt>まいしゅう</rt></ruby><ruby>火曜日<rt>かようび</rt></ruby>と<ruby>木曜日<rt>もくようび</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、<ruby>市民<rt>しみん</rt></ruby>センターに<ruby>行<rt>い</rt></ruby>って、<ruby>田中<rt>たなか</rt></ruby>さんから<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>わっています。レッスンのときに［ 1-a ］ことは<ruby>前<rt>まえ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に<ruby>予習<rt>よしゅう</rt></ruby>し、［ 1-b ］ことは<ruby>必<rt>かなら</rt></ruby>ず<ruby>復習<rt>ふくしゅう</rt></ruby>しています。\n\n<ruby>外国語<rt>がいこくご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>しようとする<ruby>人<rt>ひと</rt></ruby>にアドバイスすることが<ruby>三<rt>みっ</rt></ruby>つあります。まずするべきこととは、いい<ruby>先生<rt>せんせい</rt></ruby>を［ 2 ］。<ruby>何回<rt>なんかい</rt></ruby>かレッスンを<ruby>受<rt>う</rt></ruby>ければ、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>スタイルに<ruby>合<rt>あ</rt></ruby>う<ruby>先生<rt>せんせい</rt></ruby>かどうかわかります。どういう<ruby>教<rt>おし</rt></ruby>え<ruby>方<rt>かた</rt></ruby>をしてほしいか<ruby>先生<rt>せんせい</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えてもいいと<ruby>思<rt>おも</rt></ruby>います。\nまた、<ruby>勉強<rt>べんきょう</rt></ruby>が<ruby>難<rt>むずか</rt></ruby>しくなると、なかなか<ruby>次<rt>つぎ</rt></ruby>に<ruby>進<rt>すす</rt></ruby>めなくなります。しかし、<ruby>同<rt>おな</rt></ruby>じところばかりずっと［ 3 ］、だんだんあきてきます。そういうときは<ruby>全部<rt>ぜんぶ</rt></ruby>［ 4 ］、<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>先<rt>さき</rt></ruby>に<ruby>進<rt>すす</rt></ruby>んだほうがいいです。そして、<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は、<ruby>習<rt>なら</rt></ruby>ったことをどれぐらい<ruby>覚<rt>おぼ</rt></ruby>えているかということより、どれだけ［ 5 ］ということの<ruby>方<rt>ほう</rt></ruby>が<ruby>大切<rt>たいせつ</rt></ruby>だということです。<ruby>勉強<rt>べんきょう</rt></ruby>したことを<ruby>実際<rt>じっさい</rt></ruby>にどんどん<ruby>使<rt>つか</rt></ruby>ってみることが<ruby>大事<rt>だいじ</rt></ruby>です。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30101,
                        "prompt": "［ 1 ］（1-a / 1-b）に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　a 勉強する / b 勉強した",
                            "2　a 勉強した / b 勉強する",
                            "3　a 勉強している / b 勉強した",
                            "4　a 勉強していた / b 勉強する"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "これからレッスンで「勉強する」ことは前日に予習し、レッスンですでに「勉強した」ことは復習するので、1が正解。",
                        "explanation_en": "You prepare for what you 'will study' (勉強する) and review what you 'studied' (勉強した). Correct choice is 1."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30102,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　探します",
                            "2　探すことです",
                            "3　探しています",
                            "4　探していることです"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "文頭が「まずするべきこととは、…」とあるので、述語は「〜（動詞辞書形）ことだ／ことです」で受ける。2が正解。",
                        "explanation_en": "The sentence begins with 'まずするべきこととは', requiring a predicate in '〜ことです'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30103,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　やっていると",
                            "2　やっていたので",
                            "3　やってみると",
                            "4　やってみたので",
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "「ずっとやっていると、だんだんあきてきます」（仮定・条件「〜と」）。継続状態を表す1が正解。",
                        "explanation_en": "'〜ていると' denotes a continuing condition resulting in getting tired of it. Choice 1 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30104,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　覚えられないと",
                            "2　覚えられなくても",
                            "3　覚えられたら",
                            "4　覚えられたので"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "「全部覚えられなくても、少しずつ先に進んだほうがいい」（逆接条件「〜ても」）。2が正解。",
                        "explanation_en": "'Even if you cannot memorize everything (覚えられなくても), it is better to move forward'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30105,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　使ってみる",
                            "2　使ってみるの",
                            "3　使っている",
                            "4　使っているか"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "「どれぐらい覚えているかということより、どれだけ［使っているか］ということの方が大切」。疑問詞「どれだけ」に呼応して「〜か」で受ける。4が正解。",
                        "explanation_en": "Corresponds with the question word 'どれだけ' taking '使っているか'. Choice 4 is correct."
                    }
                ]
            },
            {
                "passage_id": 302,
                "title": "ありの巣の観察",
                "title_en": "Observing an Ant Colony",
                "text": "<ruby>先日<rt>せんじつ</rt></ruby>、<ruby>公園<rt>こうえん</rt></ruby>で、ありが<ruby>忙<rt>いそが</rt></ruby>しそうに<ruby>働<rt>はたら</rt></ruby>いているのを<ruby>見<rt>み</rt></ruby>た。<ruby>白<rt>しろ</rt></ruby>い<ruby>小<rt>ちい</rt></ruby>さなものを［ 1 ］。<ruby>行列<rt>ぎょうれつ</rt></ruby>の<ruby>先<rt>さき</rt></ruby>を<ruby>見<rt>み</rt></ruby>ると、<ruby>地面<rt>じめん</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さな<ruby>穴<rt>あな</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>いていた。ありの<ruby>巣<rt>す</rt></ruby>だ。<ruby>穴<rt>あな</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りには、<ruby>穴<rt>あな</rt></ruby>を<ruby>掘<rt>ほ</rt></ruby>ったときに<ruby>出<rt>で</rt></ruby>た<ruby>土<rt>つち</rt></ruby>が<ruby>盛<rt>も</rt></ruby>られていた。この<ruby>土<rt>つち</rt></ruby>の<ruby>山<rt>やま</rt></ruby>があるので、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っても<ruby>周<rt>まわ</rt></ruby>りから<ruby>雨水<rt>あまみず</rt></ruby>が<ruby>入<rt>はい</rt></ruby>りにくくなっているようだ。<ruby>穴<rt>あな</rt></ruby>の<ruby>中<rt>なか</rt></ruby>は［ 2 ］。<ruby>自分<rt>じぶん</rt></ruby>で<ruby>中<rt>なか</rt></ruby>を<ruby>見<rt>み</rt></ruby>ることはできないので、<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってインターネットで<ruby>調<rt>しら</rt></ruby>べてみた。\nある<ruby>専門家<rt>せんもんか</rt></ruby>のページによると、ありの<ruby>巣<rt>す</rt></ruby>は、<ruby>初<rt>はじ</rt></ruby>めは<ruby>女王<rt>じょおう</rt></ruby>ありがたった1<ruby>匹<rt>ぴき</rt></ruby>で［ 3 ］。<ruby>最初<rt>さいしょ</rt></ruby>は<ruby>一部屋<rt>ひとへや</rt></ruby>だけで、<ruby>女王<rt>じょおう</rt></ruby>はそこで<ruby>卵<rt>たまご</rt></ruby>を<ruby>産<rt>う</rt></ruby>んで［ 4 ］。<ruby>卵<rt>たまご</rt></ruby>は1か<ruby>月<rt>げつ</rt></ruby>ぐらいで<ruby>働<rt>はたら</rt></ruby>きありに<ruby>成長<rt>せいちょう</rt></ruby>し、この<ruby>働<rt>はたら</rt></ruby>きありが<ruby>巣<rt>す</rt></ruby>を<ruby>大<rt>おお</rt></ruby>きくしていくらしい。<ruby>卵<rt>たまご</rt></ruby>を<ruby>置<rt>お</rt></ruby>いておく<ruby>部屋<rt>へや</rt></ruby>、えさを<ruby>置<rt>お</rt></ruby>いておく<ruby>部屋<rt>へや</rt></ruby>、<ruby>子<rt>こ</rt></ruby>ども<ruby>部屋<rt>べや</rt></ruby>など、<ruby>人間<rt>にんげん</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>よりも［ 5 ］。<ruby>女王<rt>じょおう</rt></ruby>ありの<ruby>部屋<rt>へや</rt></ruby>はいちばん<ruby>奥<rt>おく</rt></ruby>で、<ruby>女王<rt>じょおう</rt></ruby>はここで<ruby>出産<rt>しゅっさん</rt></ruby>と<ruby>子育<rt>こそだ</rt></ruby>てに<ruby>集中<rt>しゅうちゅう</rt></ruby>するのだそうだ。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30201,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　運んだ",
                            "2　運んでいた",
                            "3　運ばれた",
                            "4　運ばれていた"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "「白い小さなものを運んでいた」（その時進行中だった動作）。2が正解。",
                        "explanation_en": "Ants were in the process of carrying small white objects; past continuous '運んでいた'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30202,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　どうなるのだろう",
                            "2　どうしたのだろう",
                            "3　どうなっているのだろう",
                            "4　どうしていたのだろう"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "穴の中が現在どのような状態になっているかを表すので「どうなっているのだろう」。3が正解。",
                        "explanation_en": "Expresses wondering about the current state inside the hole; 'どうなっているのだろう'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30203,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　作るそうだ",
                            "2　作ったそうだ",
                            "3　作られるそうだ",
                            "4　作られたそうだ"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "専門家の説明による一般的な巣作りの習性を述べているので現在形「作るそうだ」。1が正解。",
                        "explanation_en": "Describes the general habit of queen ants starting colonies from scratch; '作るそうだ'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30204,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　育てる",
                            "2　育てた",
                            "3　育てられる",
                            "4　育てられた"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "「卵を産んで育てる」（一般的なプロセス）。1が正解。",
                        "explanation_en": "Continuous process in general explanation: '卵を産んで育てる'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30205,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　よく働く",
                            "2　子どもが多い",
                            "3　簡単に作った",
                            "4　部屋が多い"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "直前に「卵を置いておく部屋、えさを置いておく部屋、子ども部屋など」と部屋の種類が列挙されているので、「人間の家よりも部屋が多い」が文脈に適合。4が正解。",
                        "explanation_en": "Listing multiple rooms immediately before leads to '部屋が多い' (has more rooms than human houses). Choice 4 is correct."
                    }
                ]
            }
        ]
    }

    # =========================================================================
    # Lesson 3: 3課 話者が見る位置を動かさない手段-1 他動詞・自動詞 (p. 122-123, Images 124-125)
    # =========================================================================
    sec3 = {
        "section_number": 3,
        "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>課<rt>か</rt></ruby> <ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かさない<ruby>手段<rt>しゅだん</rt></ruby>-1 <ruby>他動詞<rt>たどうし</rt></ruby>・<ruby>自動詞<rt>じどうし</rt></ruby>",
        "title_en": "Lesson 3: Keeping the Speaker's Perspective Consistent 1 - Transitive and Intransitive Verbs",
        "theme": "まとまりのある<ruby>文章<rt>ぶんしょう</rt></ruby>にするためには、<ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かさないで<ruby>文<rt>ぶん</rt></ruby>を<ruby>続<rt>つづ</rt></ruby>けなければなりません。<ruby>他動詞<rt>たどうし</rt></ruby>・<ruby>自動詞<rt>じどうし</rt></ruby>は、<ruby>何<rt>なに</rt></ruby>に<ruby>注目<rt>ちゅうもく</rt></ruby>するかによって<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>けます。",
        "theme_en": "To form a cohesive sentence, the standpoint of the speaker must remain consistent in each sentence. Depending on where the focus is, a transitive or intransitive verb is used.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>他動詞<rt>たどうし</rt></ruby>・<ruby>自動詞<rt>じどうし</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>け",
                "title_en": "Differentiating between transitive and intransitive verbs",
                "rules": [
                    {
                        "category": "<ruby>変化<rt>へんか</rt></ruby>を<ruby>起<rt>お</rt></ruby>こす<ruby>動作<rt>どうさ</rt></ruby>／結果",
                        "transitive": "<ruby>変化<rt>へんか</rt></ruby>を<ruby>起<rt>お</rt></ruby>こす<ruby>動作<rt>どうさ</rt></ruby>に<ruby>注目<rt>ちゅうもく</rt></ruby>して<ruby>言<rt>い</rt></ruby>う（他動詞の文）: ヤンさんはタクシーを<ruby>止<rt>と</rt></ruby>めた。／わたしはろうそくの<ruby>火<rt>ひ</rt></ruby>を<ruby>消<rt>け</rt></ruby>した。／わたしはドアを<ruby>開<rt>あ</rt></ruby>けた。",
                        "intransitive": "<ruby>変化<rt>へんか</rt></ruby>を<ruby>起<rt>お</rt></ruby>こす<ruby>動作<rt>どうさ</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>に<ruby>注目<rt>ちゅうもく</rt></ruby>して<ruby>言<rt>い</rt></ruby>う（自動詞の文）: タクシーが<ruby>止<rt>と</rt></ruby>まった。／ろうそくの<ruby>火<rt>ひ</rt></ruby>が<ruby>消<rt>き</rt></ruby>えた。／ドアが<ruby>開<rt>あ</rt></ruby>いた。（注1: 受身文でも表すことができる。例・タクシーが止められた。→第3部 5課）"
                    },
                    {
                        "category": "<ruby>自然<rt>しぜん</rt></ruby>に<ruby>起<rt>お</rt></ruby>こること",
                        "transitive": "（<ruby>対応<rt>たいおう</rt></ruby>する<ruby>他動詞<rt>たどうし</rt></ruby>がない<ruby>場合<rt>ばあい</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い）",
                        "intransitive": "<ruby>自然<rt>しぜん</rt></ruby>に<ruby>起<rt>お</rt></ruby>こることを<ruby>表<rt>あらわ</rt></ruby>す: <ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>った。／<ruby>庭<rt>にわ</rt></ruby>にきれいなばらの<ruby>花<rt>はな</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>いた。／<ruby>今夜<rt>こんや</rt></ruby>は<ruby>月<rt>つき</rt></ruby>が<ruby>明<rt>あか</rt></ruby>るく<ruby>輝<rt>かがや</rt></ruby>いている。"
                    },
                    {
                        "category": "<ruby>人<rt>ひと</rt></ruby>や<ruby>物<rt>もの</rt></ruby>への<ruby>働<rt>はたら</rt></ruby>きかけ",
                        "transitive": "<ruby>人<rt>ひと</rt></ruby>や<ruby>物<rt>もの</rt></ruby>への<ruby>働<rt>はたら</rt></ruby>きかけがある<ruby>動作<rt>どうさ</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す: <ruby>先生<rt>せんせい</rt></ruby>が<ruby>子<rt>こ</rt></ruby>どもをしかった。／わたしはリーさんに<ruby>仕事<rt>しごと</rt></ruby>を<ruby>頼<rt>たの</rt></ruby>んだ。（注2: 受身文でも表すことができる。例・子どもは先生にしかられた。→第3部 5課）",
                        "intransitive": "（<ruby>対応<rt>たいおう</rt></ruby>する<ruby>自動詞<rt>じどうし</rt></ruby>はない）"
                    },
                    {
                        "category": "<ruby>人<rt>ひと</rt></ruby>や<ruby>物<rt>もの</rt></ruby>への<ruby>働<rt>はたら</rt></ruby>きかけがない<ruby>動作<rt>どうさ</rt></ruby>",
                        "transitive": "（<ruby>対応<rt>たいおう</rt></ruby>する<ruby>他動詞<rt>たどうし</rt></ruby>はない）（注3: 使役文で表すことができる。例・先生は子どもたちをいすに座らせた。→第3部 5課）",
                        "intransitive": "<ruby>人<rt>ひと</rt></ruby>や<ruby>物<rt>もの</rt></ruby>への<ruby>働<rt>はたら</rt></ruby>きかけがない<ruby>動作<rt>どうさ</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す: <ruby>子<rt>こ</rt></ruby>どもたちはいすに<ruby>座<rt>すわ</rt></ruby>った。／<ruby>飛行機<rt>ひこうき</rt></ruby>が<ruby>空<rt>そら</rt></ruby>を<ruby>飛<rt>と</rt></ruby>んでいる。"
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30301,
                "category": "第3部 3課 練習",
                "question_type": "fill_conjugation",
                "prompt": "1 <ruby>読<rt>よ</rt></ruby>み<ruby>終<rt>お</rt></ruby>わった<ruby>本<rt>ほん</rt></ruby>は、<ruby>棚<rt>たな</rt></ruby>に①＿＿＿てください。<ruby>部屋<rt>へや</rt></ruby>を<ruby>出<rt>で</rt></ruby>るときは、<ruby>電気<rt>でんき</rt></ruby>が②＿＿＿ているかどうか<ruby>確認<rt>かくにん</rt></ruby>してください。（戻る・戻す、消える・消す）",
                "correct_answers": ["① 戻し", "② 消え"],
                "explanation_ja": "①本を棚に戻す（他動詞のて形：戻して）。②電気が消えている（自動詞の結果状態：消えている）。",
                "explanation_en": "①'戻して' (transitive). ②'消えている' (intransitive state)."
            },
            {
                "question_id": 30302,
                "category": "第3部 3課 練習",
                "question_type": "fill_conjugation",
                "prompt": "2 <ruby>登山靴<rt>とざんぐつ</rt></ruby>には、<ruby>丈夫<rt>じょうぶ</rt></ruby>で<ruby>簡単<rt>かんたん</rt></ruby>には①＿＿＿ひもを<ruby>使<rt>つか</rt></ruby>っています。ひもはお<ruby>客様<rt>きゃくさま</rt></ruby>の<ruby>注文<rt>ちゅうもん</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせてちょうどいい<ruby>長<rt>なが</rt></ruby>さに②＿＿＿こともできますので、まず、はいてみてください。（切れる・切る）",
                "correct_answers": ["① 切れない", "② 切る"],
                "explanation_ja": "①簡単には切れない（自然に切れる：自動詞可能否定）。②長さに切る（他動詞）。",
                "explanation_en": "①'切れない' (intransitive). ②'切る' (transitive)."
            },
            {
                "question_id": 30303,
                "category": "第3部 3課 練習",
                "question_type": "fill_conjugation",
                "prompt": "3 <ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってびっくりした。<ruby>窓<rt>まど</rt></ruby>が①＿＿＿ていた。だれかが②＿＿＿んだそうと<ruby>思<rt>おも</rt></ruby>った。そうだった。わたしが、<ruby>家<rt>いえ</rt></ruby>を③＿＿＿とき、④＿＿＿のを<ruby>忘<rt>わす</rt></ruby>れたのだ。（開く・開ける、出る・出す、閉まる・閉める）",
                "correct_answers": ["① 開い", "② 開けた", "③ 出る", "④ 閉める"],
                "explanation_ja": "①窓が開いていた（自動詞）。②だれかが開けた（他動詞）。③家を出るとき（自動詞）。④閉めるのを忘れた（他動詞）。",
                "explanation_en": "①'開いていた' (intransitive). ②'開けた' (transitive). ③'出る' (intransitive). ④'閉める' (transitive)."
            },
            {
                "question_id": 30304,
                "category": "第3部 3課 練習",
                "question_type": "fill_conjugation",
                "prompt": "4 わたしは1990<ruby>年<rt>ねん</rt></ruby>にある<ruby>小<rt>ちい</rt></ruby>さい<ruby>島<rt>しま</rt></ruby>で①＿＿＿。<ruby>病院<rt>びょういん</rt></ruby>も<ruby>店<rt>みせ</rt></ruby>もなく<ruby>知<rt>し</rt></ruby>り<ruby>合<rt>あ</rt></ruby>いもいない<ruby>島<rt>しま</rt></ruby>で<ruby>子<rt>こ</rt></ruby>どもを②＿＿＿ことができるだろうかと、<ruby>母<rt>はは</rt></ruby>はわたしを③＿＿＿<ruby>後<rt>あと</rt></ruby>、<ruby>悩<rt>なや</rt></ruby>んだそうだ。でも、わたしは<ruby>元気<rt>げんき</rt></ruby>に④＿＿＿て、<ruby>母<rt>はは</rt></ruby>を<ruby>安心<rt>あんしん</rt></ruby>させた。（生まれる・産む、育つ・育てる）",
                "correct_answers": ["① 生まれた", "② 育てる", "③ 産んだ", "④ 育っ"],
                "explanation_ja": "①小さい島で生まれた（自動詞）。②子どもを育てる（他動詞）。③わたしを産んだ後（他動詞）。④元気に育って（自動詞）。",
                "explanation_en": "①'生まれた' (intransitive). ②'育てる' (transitive). ③'産んだ' (transitive). ④'育って' (intransitive)."
            },
            {
                "question_id": 30305,
                "category": "第3部 3課 練習",
                "question_type": "fill_conjugation",
                "prompt": "5 <ruby>今朝<rt>けさ</rt></ruby>は<ruby>遅刻<rt>ちこく</rt></ruby>してしまった。きのう、<ruby>遅<rt>おそ</rt></ruby>くまで①＿＿＿ていたし、<ruby>目覚<rt>めざ</rt></ruby>まし<ruby>時計<rt>どけい</rt></ruby>がいつの<ruby>間<rt>ま</rt></ruby>にか②＿＿＿ていたのだ。<ruby>電池<rt>でんち</rt></ruby>はちゃんと③＿＿＿ておいたはずなのに……。あしたは<ruby>試験<rt>しけん</rt></ruby>だから、<ruby>母<rt>はは</rt></ruby>に7<ruby>時<rt>じ</rt></ruby>に④＿＿＿てほしいと<ruby>頼<rt>たの</rt></ruby>んでおこう。（起きる・起こす、止まる・止める、入る・入れる）",
                "correct_answers": ["① 起き", "② 止まっ", "③ 入れ", "④ 起こし"],
                "explanation_ja": "①遅くまで起きていた（自動詞）。②時計が止まっていた（自動詞）。③電池を入れておいた（他動詞）。④母に起こしてほしい（他動詞）。",
                "explanation_en": "①'起きていた' (intransitive). ②'止まっていた' (intransitive). ③'入れておいた' (transitive). ④'起こしてほしい' (transitive)."
            }
        ]
    }

    # =========================================================================
    # Lesson 4: 4課 話者が見る位置を動かさない手段-2 〜てくる・〜ていく (p. 124-125, Images 126-127)
    # =========================================================================
    sec4 = {
        "section_number": 4,
        "title": "<ruby>第<rt>だい</rt></ruby>4<ruby>課<rt>か</rt></ruby> <ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かさない<ruby>手段<rt>しゅだん</rt></ruby>-2 〜てくる・〜ていく",
        "title_en": "Lesson 4: Keeping the Speaker's Perspective Consistent 2 - '~te kuru' & '~te iku'",
        "theme": "「〜てくる・〜ていく」を<ruby>使<rt>つか</rt></ruby>えば、<ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>・<ruby>時点<rt>じてん</rt></ruby>がはっきりします。",
        "theme_en": "Use of ~te kuru and ~te iku forms to specify the position of the speaker and the time at which a statement is made.",
        "points": [
            {
                "point_number": 1,
                "title": "「〜てくる・〜ていく」の<ruby>整理<rt>せいり</rt></ruby>",
                "title_en": "Organization of '~te kuru' and '~te iku'",
                "usage_table": [
                    {
                        "meaning": "ある<ruby>動作<rt>どうさ</rt></ruby>の<ruby>後<rt>あと</rt></ruby>の<ruby>移動<rt>いどう</rt></ruby>",
                        "meaning_en": "A movement or shift occurring after an action.",
                        "te_kuru": "出かけるとき、天気予報を見てきました。／コンビニでジュースを買ってきます。（出発点に戻る）／ちょっと外でたばこを吸ってきます。",
                        "te_iku": "荷物はここに預けていこう。／空港へ行く途中でお金をおろしていこう。（出発点に戻らない）／途中の郵便局で書留を出していった。"
                    },
                    {
                        "meaning": "<ruby>移動<rt>いどう</rt></ruby>の<ruby>方向<rt>ほうこう</rt></ruby>",
                        "meaning_en": "Expresses direction of movement.",
                        "note": "移動の動詞につく (Affixed to verb of motion)",
                        "te_kuru": "川上から帽子が流れてきた。／エレベーターが1階から上がってくる。",
                        "te_iku": "飛行機が南の方へ飛んでいった。／エレベーターが上の階へ上がっていく。"
                    },
                    {
                        "meaning": "<ruby>話者<rt>わしゃ</rt></ruby>へのものごとの<ruby>接近<rt>せっきん</rt></ruby>・<ruby>到達<rt>とうたつ</rt></ruby>",
                        "meaning_en": "Means the speaker is the person affected by an action or event coming from elsewhere.",
                        "note": "「〜てくる」だけ",
                        "te_kuru": "友だちから電話がかかってきた。／どこからか鐘の音が聞こえてきた。／新しい心配ごとが出てきた。"
                    },
                    {
                        "meaning": "<ruby>変化<rt>へんか</rt></ruby>や<ruby>状態<rt>じょうたい</rt></ruby>の<ruby>持続<rt>じぞく</rt></ruby>",
                        "meaning_en": "Indicates the continuation of a process of change or of a state.",
                        "note": "変化を表す動詞・継続を表す動詞を使う",
                        "te_kuru": "この地方も交通がだんだん便利になってきた。／この村の人たちは昔からずっと村の伝統を守ってきた。",
                        "te_iku": "これからは観光客が多くなっていくと思う。／今後も守っていくだろう。"
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30401,
                "category": "第3部 4課 練習",
                "question_type": "fill_conjugation",
                "prompt": "1 <ruby>最近<rt>さいきん</rt></ruby>だんだん<ruby>会社<rt>かいしゃ</rt></ruby>での<ruby>責任<rt>せきにん</rt></ruby>が<ruby>重<rt>おも</rt></ruby>くなって①＿＿＿。これからはさらに<ruby>忙<rt>いそが</rt></ruby>しくなるだろう。でも、この<ruby>仕事<rt>しごと</rt></ruby>をずっと<ruby>続<rt>つづ</rt></ruby>けて②＿＿＿よかったと<ruby>思<rt>おも</rt></ruby>う。（くる・いく）",
                "correct_answers": ["① きた", "② きて"],
                "explanation_ja": "①過去から現在への変化の進行：「重くなってきた」。②過去から現在までの継続：「続けてきてよかった」。",
                "explanation_en": "①'重くなってきた' (continuation of change up to present). ②'続けてきて' (continuation of action up to present)."
            },
            {
                "question_id": 30402,
                "category": "第3部 4課 練習",
                "question_type": "fill_conjugation",
                "prompt": "2 <ruby>今夜<rt>こんや</rt></ruby>、わたしの<ruby>家<rt>いえ</rt></ruby>で<ruby>忘年会<rt>ぼうねんかい</rt></ruby>をします。わたしはケーキを<ruby>作<rt>つく</rt></ruby>ります。みきさんは<ruby>珍<rt>めずら</rt></ruby>しい<ruby>料理<rt>りょうり</rt></ruby>を<ruby>持<rt>も</rt></ruby>って①＿＿＿くれるらしいです。<ruby>山本<rt>やまもと</rt></ruby><ruby>君<rt>くん</rt></ruby>は<ruby>途中<rt>とちゅう</rt></ruby>でスーパーに<ruby>寄<rt>よ</rt></ruby>って、<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>を<ruby>買<rt>か</rt></ruby>って②＿＿＿ことになっています。10<ruby>年前<rt>ねんまえ</rt></ruby>から<ruby>毎年<rt>まいとし</rt></ruby><ruby>同<rt>おな</rt></ruby>じメンバーで<ruby>忘年会<rt>ぼうねんかい</rt></ruby>をして③＿＿＿ので、<ruby>今年<rt>ことし</rt></ruby>もとても<ruby>楽<rt>たの</rt></ruby>しみです。（くる・いく）",
                "correct_answers": ["① きて", "② くる", "③ きた"],
                "explanation_ja": "①持ってきてくれる。②買って（家に）くることになっている。③忘年会をしてきたので（過去10年間の継続）。",
                "explanation_en": "①'持ってきて' (bring here). ②'買ってくる' (buy and come). ③'してきた' (done continually for 10 years)."
            },
            {
                "question_id": 30403,
                "category": "第3部 4課 練習",
                "question_type": "fill_conjugation",
                "prompt": "3 となりに<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>して①＿＿＿<ruby>学生<rt>がくせい</rt></ruby>さんは<ruby>音楽<rt>おんがく</rt></ruby>が<ruby>専門<rt>せんもん</rt></ruby>らしい。<ruby>夜中<rt>よなか</rt></ruby>も<ruby>彼<rt>かれ</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>から<ruby>音楽<rt>おんがく</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえて②＿＿＿。<ruby>今朝<rt>けさ</rt></ruby>もわたしが<ruby>外<rt>そと</rt></ruby>へごみを<ruby>出<rt>だ</rt></ruby>しに<ruby>行<rt>い</rt></ruby>くと、<ruby>大<rt>おお</rt></ruby>きな<ruby>楽器<rt>がっき</rt></ruby>を<ruby>持<rt>も</rt></ruby>って<ruby>部屋<rt>へや</rt></ruby>から<ruby>出<rt>で</rt></ruby>て③＿＿＿、<ruby>駅<rt>えき</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>へ<ruby>歩<rt>ある</rt></ruby>いて④＿＿＿。<ruby>重<rt>おも</rt></ruby>そうな<ruby>楽器<rt>がっき</rt></ruby>だ。<ruby>学校<rt>がっこう</rt></ruby>に<ruby>置<rt>お</rt></ruby>いて⑤＿＿＿ばいいのに、と<ruby>思<rt>おも</rt></ruby>うが、<ruby>夜<rt>よる</rt></ruby>も<ruby>練習<rt>れんしゅう</rt></ruby>しなければならないのだろう。（くる・いく）",
                "correct_answers": ["① きた", "② くる", "③ きて", "④ いった", "⑤ くれ (くれ／いけ)"],
                "explanation_ja": "解答冊子p.6参照：①きた ②くる ③きて ④いった ⑤くれ（または、おいていけば）。",
                "explanation_en": "See Answer booklet p.6: ①きた ②くる ③きて ④いった ⑤くれ."
            },
            {
                "question_id": 30404,
                "category": "第3部 4課 練習",
                "question_type": "fill_conjugation",
                "prompt": "4 どこからかニャーニャーという<ruby>鳴<rt>な</rt></ruby>き<ruby>声<rt>ごえ</rt></ruby>がしたので、<ruby>家<rt>いえ</rt></ruby>の<ruby>外<rt>そと</rt></ruby>に<ruby>出<rt>で</rt></ruby>てみると、うちの<ruby>車<rt>くるま</rt></ruby>の<ruby>下<rt>した</rt></ruby>から<ruby>小<rt>ちい</rt></ruby>さいねこが<ruby>出<rt>で</rt></ruby>て①＿＿＿。とてもかわいいので、<ruby>台所<rt>だいどころ</rt></ruby>からミルクとお<ruby>皿<rt>さら</rt></ruby>を<ruby>取<rt>と</rt></ruby>って②＿＿＿、<ruby>子<rt>こ</rt></ruby>ねこの<ruby>前<rt>まえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>いた。<ruby>子<rt>こ</rt></ruby>ねこはミルクを<ruby>飲<rt>の</rt></ruby>むと、また<ruby>車<rt>くるま</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>逃<rt>に</rt></ruby>げていってしまった。それから<ruby>毎日<rt>まいにち</rt></ruby>、わたしの<ruby>姿<rt>すがた</rt></ruby>を<ruby>見<rt>み</rt></ruby>つけると<ruby>近<rt>ちか</rt></ruby>づいて③＿＿＿ミルクを<ruby>飲<rt>の</rt></ruby>んでいたが、きのう、<ruby>飼<rt>か</rt></ruby>い<ruby>主<rt>ぬし</rt></ruby>が<ruby>現<rt>あらわ</rt></ruby>れて、<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>子<rt>こ</rt></ruby>ねこを<ruby>連<rt>つ</rt></ruby>れて④＿＿＿。（くる・いく）",
                "correct_answers": ["① きた", "② きて", "③ きて", "④ いった"],
                "explanation_ja": "①出てきた（話者に接近）。②取ってきた（戻る移動）。③近づいてきて（話者に接近）。④連れていった（遠ざかる移動）。",
                "explanation_en": "①'出てきた' (approach). ②'取ってきて' (fetch and return). ③'近づいてきて' (approach). ④'連れていった' (move away)."
            }
        ]
    }

    # =========================================================================
    # Review Test 3-4: まとめ問題 (3課・4課) (p. 126-127, Images 128-129)
    # =========================================================================
    matome_3_4 = {
        "section_number": 4.5,
        "title": "まとめ<ruby>問題<rt>もんだい</rt></ruby>（3<ruby>課<rt>か</rt></ruby>・4<ruby>課<rt>か</rt></ruby>）",
        "title_en": "Review Exercises (Lessons 3 & 4)",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>総合練習<rt>そうごうれんしゅう</rt></ruby>（<ruby>視点<rt>してん</rt></ruby>と<ruby>自動詞<rt>じどうし</rt></ruby>・<ruby>他動詞<rt>たどうし</rt></ruby>、〜てくる・〜ていく）",
        "theme_en": "Comprehensive text grammar review: Standpoint, transitive/intransitive verbs, and te-kuru / te-iku",
        "passages": [
            {
                "passage_id": 303,
                "title": "蒸し料理用のなべ",
                "title_en": "A Steaming Pot for Cooking",
                "text": "<ruby>一人暮<rt>ひとりぐ</rt></ruby>らしだと、どうしても<ruby>野菜不足<rt>やさいぶそく</rt></ruby>になります。<ruby>健康<rt>けんこう</rt></ruby>のために1<ruby>日<rt>にち</rt></ruby>に350グラムの<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるといいと<ruby>言<rt>い</rt></ruby>いますが、サラダだけではそんなに<ruby>食<rt>た</rt></ruby>べられません。でも、<ruby>時間<rt>じかん</rt></ruby>をかけて<ruby>野菜<rt>やさい</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>を<ruby>作<rt>つく</rt></ruby>るのは<ruby>面倒<rt>めんどう</rt></ruby>だし、<ruby>油<rt>あぶら</rt></ruby>や<ruby>塩<rt>しお</rt></ruby>、しょうゆを<ruby>使<rt>つか</rt></ruby>いすぎると、<ruby>別<rt>べつ</rt></ruby>の［ 1 ］。\nそこで、わたしは<ruby>考<rt>かんが</rt></ruby>えました。<ruby>栄養<rt>えいよう</rt></ruby>を<ruby>逃<rt>に</rt></ruby>がさないで、<ruby>味付<rt>あじつ</rt></ruby>けも<ruby>簡単<rt>かんたん</rt></ruby>な<ruby>野菜料理<rt>やさいりょうり</rt></ruby>を<ruby>作<rt>つく</rt></ruby>るには<ruby>蒸<rt>む</rt></ruby>すのがいいと。さっそく<ruby>蒸<rt>む</rt></ruby>し<ruby>料理用<rt>りょうりよう</rt></ruby>のなべを<ruby>買<rt>か</rt></ruby>ってきました。このなべはふたが<ruby>三角帽子<rt>さんかくぼうし</rt></ruby>のような<ruby>形<rt>かたち</rt></ruby>に［ 2 ］。<ruby>野菜<rt>やさい</rt></ruby>を<ruby>入<rt>い</rt></ruby>れてふたをし、<ruby>弱火<rt>よわび</rt></ruby>で7、8<ruby>分<rt>ぷん</rt></ruby>。<ruby>火<rt>ひ</rt></ruby>を<ruby>止<rt>と</rt></ruby>めてしばらくしてからふたを<ruby>開<rt>あ</rt></ruby>けると、<ruby>野菜<rt>やさい</rt></ruby>はすっかり<ruby>軟<rt>やわ</rt></ruby>らかくなっていました。なべに<ruby>水<rt>みず</rt></ruby>を<ruby>入<rt>い</rt></ruby>れなくても、<ruby>野菜<rt>やさい</rt></ruby>から<ruby>出<rt>で</rt></ruby>た<ruby>水<rt>みず</rt></ruby>が<ruby>水蒸気<rt>すいじょうき</rt></ruby>になって<ruby>上<rt>うえ</rt></ruby>に<ruby>上<rt>あ</rt></ruby>がります。そして、ふたに<ruby>当<rt>あ</rt></ruby>たって<ruby>温度<rt>おんど</rt></ruby>が<ruby>下<rt>さ</rt></ruby>がり、［ 3 ］というわけです。<ruby>少<rt>すこ</rt></ruby>し<ruby>塩<rt>しお</rt></ruby>を<ruby>振<rt>ふ</rt></ruby>っただけで<ruby>十分<rt>じゅうぶん</rt></ruby>おいしくて、<ruby>野菜本来<rt>やさいほんらい</rt></ruby>の<ruby>味<rt>あじ</rt></ruby>を<ruby>楽<rt>たの</rt></ruby>しむことができました。<ruby>気<rt>き</rt></ruby>に<ruby>入<rt>い</rt></ruby>って、この1か<ruby>月<rt>げつ</rt></ruby><ruby>毎日<rt>まいにち</rt></ruby><ruby>蒸<rt>む</rt></ruby>し<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べ<ruby>続<rt>つづ</rt></ruby>けたら、<ruby>体<rt>からだ</rt></ruby>が［ 4 ］。なべに［ 5 ］<ruby>説明書<rt>せつめいしょ</rt></ruby>によると、できるだけいろいろな<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるのがいいそうです。ですから、これからは、<ruby>今<rt>いま</rt></ruby>まであまり<ruby>食<rt>た</rt></ruby>べなかったほかの<ruby>野菜<rt>やさい</rt></ruby>も<ruby>食<rt>た</rt></ruby>べてみようと<ruby>思<rt>おも</rt></ruby>っています。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30301,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　問題が出てきます",
                            "2　問題が出ていきます",
                            "3　問題を出してきます",
                            "4　問題を出していきます"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "油や塩を使いすぎると「別の問題が生じる（話者に降りかかる）」。自動詞＋てくる「問題が出てきます」。1が正解。",
                        "explanation_en": "A new problem arises for the speaker; intransitive + te-kuru: '問題が出てきます'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30302,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　なってきます",
                            "2　なってきました",
                            "3　なっています",
                            "4　なりました"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "鍋のふたの形状・状態を表すので「三角帽子のような形になっています」。3が正解。",
                        "explanation_en": "Describes the existing shape/state of the lid: '三角帽子のような形になっています'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30303,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　ふたの上に落ちる",
                            "2　野菜の上に落ちる",
                            "3　野菜の上から落とす",
                            "4　ふたの上に落とす"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "水蒸気がふたに当たって水滴になり、自然に「野菜の上に落ちる」（自動詞）。2が正解。",
                        "explanation_en": "The cooled water drops naturally fall onto the vegetables; '野菜の上に落ちる'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30304,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　軽くしてきました",
                            "2　軽くしていきました",
                            "3　軽くなってきました",
                            "4　軽くなっていきました"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "1か月食べ続けたら身体が自然に軽くなる変化が現在に至ったので「軽くなってきました」（自動詞変化＋てきた）。3が正解。",
                        "explanation_en": "Intransitive change continuing up to the present: '軽くなってきました'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30305,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　ついていく",
                            "2　ついてきた",
                            "3　つけてくる",
                            "4　つけていった"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "買った鍋に付属していた説明書なので、自動詞＋過去・話者への移動「ついてきた説明書」。2が正解。",
                        "explanation_en": "The instruction manual that came with the purchased pot: 'ついてきた説明書'. Choice 2 is correct."
                    }
                ]
            },
            {
                "passage_id": 304,
                "title": "ベランダのゴーヤ栽培",
                "title_en": "Growing Bitter Gourd on the Balcony",
                "text": "<ruby>今年<rt>ことし</rt></ruby>の<ruby>夏<rt>なつ</rt></ruby>はベランダでゴーヤを<ruby>育<rt>そだ</rt></ruby>ててみることにした。ゴーヤというのは<ruby>大<rt>おお</rt></ruby>きいきゅうりのような［ 1 ］<ruby>野菜<rt>やさい</rt></ruby>だ。<ruby>暑<rt>あつ</rt></ruby>さに<ruby>強<rt>つよ</rt></ruby>くて、<ruby>病気<rt>びょうき</rt></ruby>や<ruby>虫<rt>むし</rt></ruby>の<ruby>心配<rt>しんぱい</rt></ruby>もあまりないという。\nまず、<ruby>種<rt>たね</rt></ruby>の<ruby>先<rt>さき</rt></ruby>を<ruby>切<rt>き</rt></ruby>り<ruby>落<rt>お</rt></ruby>とし、<ruby>水<rt>みず</rt></ruby>を<ruby>少<rt>すこ</rt></ruby>し<ruby>入<rt>い</rt></ruby>れた<ruby>皿<rt>さら</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>いて、<ruby>根<rt>ね</rt></ruby>が<ruby>出<rt>で</rt></ruby>てくるのを<ruby>待<rt>ま</rt></ruby>った。<ruby>四日目<rt>よっかめ</rt></ruby>に<ruby>白<rt>しろ</rt></ruby>いものが［ 2 ］。これがゴーヤの<ruby>根<rt>ね</rt></ruby>だ。<ruby>土<rt>つち</rt></ruby>を<ruby>入<rt>い</rt></ruby>れたポットにそっと<ruby>植<rt>う</rt></ruby>えた。さらに1<ruby>週間後<rt>しゅうかんご</rt></ruby>、<ruby>重<rt>おも</rt></ruby>い<ruby>土<rt>つち</rt></ruby>を<ruby>持<rt>も</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>げてかわいい<ruby>芽<rt>め</rt></ruby>が<ruby>出<rt>で</rt></ruby>てきた。<ruby>葉<rt>は</rt></ruby>が4<ruby>枚<rt>まい</rt></ruby>になったところで、<ruby>大<rt>おお</rt></ruby>きい<ruby>植木鉢<rt>うえきばち</rt></ruby>に<ruby>植<rt>う</rt></ruby>え<ruby>替<rt>か</rt></ruby>えた。<ruby>毎日<rt>まいにち</rt></ruby>どんどん［ 3 ］、とても<ruby>楽<rt>たの</rt></ruby>しみだった。\nそのうち、つる（注）が<ruby>伸<rt>の</rt></ruby>びてきた。<ruby>棒<rt>ぼう</rt></ruby>を<ruby>立<rt>た</rt></ruby>てて、このつるを<ruby>巻<rt>ま</rt></ruby>いてやった。<ruby>折<rt>お</rt></ruby>れないように<ruby>注意<rt>ちゅうい</rt></ruby>しながら、<ruby>伸<rt>の</rt></ruby>びた<ruby>部分<rt>ぶぶん</rt></ruby>をなるべく<ruby>横<rt>よこ</rt></ruby>に［ 4 ］いいそうだ。やがて<ruby>直径<rt>ちょっけい</rt></ruby>2センチぐらいの<ruby>黄色<rt>きいろ</rt></ruby>い<ruby>花<rt>はな</rt></ruby>がたくさん<ruby>咲<rt>さ</rt></ruby>いた。1<ruby>日<rt>にち</rt></ruby>だけ<ruby>咲<rt>さ</rt></ruby>いて<ruby>落<rt>お</rt></ruby>ちてしまう<ruby>花<rt>はな</rt></ruby>もあるし、ずっと<ruby>咲<rt>さ</rt></ruby>いている<ruby>花<rt>はな</rt></ruby>もある。<ruby>見<rt>み</rt></ruby>ると、<ruby>咲<rt>さ</rt></ruby>き<ruby>続<rt>つづ</rt></ruby>けている<ruby>花<rt>はな</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さい［ 5 ］。<ruby>感動的<rt>かんどうてき</rt></ruby>な<ruby>発見<rt>はっけん</rt></ruby>だった。\n（注：つる）",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30401,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　形をする",
                            "2　形をしている",
                            "3　形をしてきた",
                            "4　形をしていく"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "形状を表す表現「〜形をしている」。名詞を修飾して「きゅうりのような形をしている野菜」。2が正解。",
                        "explanation_en": "Expresses shape/appearance: '〜形をしている野菜'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30402,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　見ている",
                            "2　見られていった",
                            "3　見えてきた",
                            "4　見えていった"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "根が成長して話者の目に次第に見えるようになったので「見えてきた」。3が正解。",
                        "explanation_en": "The white roots became visible to the speaker; '見えてきた'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30403,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　大きくしていけば",
                            "2　大きくしていくので",
                            "3　大きくなっていけば",
                            "4　大きくなっていくので"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "毎日どんどん自然に成長していく様子が楽しみだった理由を述べるので、「大きくなっていくので」。4が正解。",
                        "explanation_en": "'大きくなっていくので' expresses the reason for excitement as it grew larger day by day. Choice 4 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30404,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　広げると",
                            "2　広がると",
                            "3　広げてくると",
                            "4　広がっていくと"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "人間が意図的につるを横に広げる動作（他動詞）＋条件「〜と」。「広げるといいそうだ」。1が正解。",
                        "explanation_en": "Deliberately spreading the vines horizontally (transitive): '広げると'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30405,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　ゴーヤの実がついていた",
                            "2　ゴーヤの実がつけてあった",
                            "3　ゴーヤの実をつけてきた",
                            "4　ゴーヤの実がつけてきた"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "自然に実がなっている状態を発見したので自動詞「ゴーヤの実がついていた」。1が正解。",
                        "explanation_en": "Discovering small bitter gourd fruits naturally attached: 'ゴーヤの実がついていた'. Choice 1 is correct."
                    }
                ]
            }
        ]
    }

    return [sec1, sec2, matome_1_2, sec3, sec4, matome_3_4]
