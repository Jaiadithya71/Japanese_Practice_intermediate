"""
Part 3 Lessons 1 to 3 + Review Test (1課・2課)
Sections 12 to 15 for Shin Kanzen Master JLPT N3 Grammar
Worker G3 scope
"""

def get_part3_lessons_sections():
    return [
        # =========================================================================
        # SECTION 12: 第3部 第1課 文の始めと終わりの対応 (p. 114-115)
        # =========================================================================
        {
            "section_number": 12,
            "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>1<ruby>課<rt>か</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>始<rt>はじ</rt></ruby>めと<ruby>終<rt>お</rt></ruby>わりの<ruby>対応<rt>たいおう</rt></ruby>",
            "title_en": "Part 3 Lesson 1: Correspondence of Sentence Beginning and Ending",
            "theme": "文章のまとまりをつくるための、文の始めと終わりの呼応・対応",
            "patterns": [
                {
                    "pattern_number": 1,
                    "pattern_name": "〜には ＋ …がいる／…がある／…が多い",
                    "pattern_name_en": "ni wa + ga iru / ga aru / ga ooi",
                    "meaning_ja": "場所や対象を取り立てて、そこに存在するものや多い事柄を述べる。",
                    "meaning_en": "Highlights a topic or location and describes what exists or is abundant there.",
                    "connection_forms": ["N + には ＋ …がいる／ある／多い"],
                    "nuance_notes": "「〜には」で始まった文は、後ろに存在動詞や数量の多い状態を表す言葉が呼応する。",
                    "example_sentences": [
                        {
                            "japanese": "<ruby>世界<rt>せかい</rt></ruby>にはいろいろな<ruby>文化<rt>ぶんか</rt></ruby>を<ruby>持<rt>も</rt></ruby>った<ruby>国<rt>くに</rt></ruby>がある。",
                            "english": "In the world, there are countries with various cultures."
                        },
                        {
                            "japanese": "この<ruby>計画<rt>けいかく</rt></ruby>には<ruby>問題点<rt>もんだいてん</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。",
                            "english": "There are many issues with this plan."
                        }
                    ]
                },
                {
                    "pattern_number": 2,
                    "pattern_name": "〜には／〜のに（は） ＋ …が必要だ／…が便利だ／…なければならない／…がかかる",
                    "pattern_name_en": "ni wa / no ni (wa) + ga hitsuyou da / ga benri da / nakereba naranai / ga kakaru",
                    "meaning_ja": "目的や用途を取り立てて、それに必要なこと・条件を述べる。",
                    "meaning_en": "States a purpose or requirement, followed by necessary conditions or costs.",
                    "connection_forms": ["V-辞書形 + には / のに（は）", "N + には"],
                    "nuance_notes": "目的や行為の実現に不可欠な条件・義務を表す表現が結びに呼応する。",
                    "example_sentences": [
                        {
                            "japanese": "この<ruby>仕事<rt>しごと</rt></ruby>をするには<ruby>車<rt>くるま</rt></ruby>の<ruby>運転<rt>うんてん</rt></ruby>ができなければならない。",
                            "english": "To do this job, one must be able to drive a car."
                        },
                        {
                            "japanese": "<ruby>外国<rt>がいこく</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くのにはパスポートが<ruby>必要<rt>ひつよう</rt></ruby>だ。",
                            "english": "A passport is necessary to go abroad."
                        }
                    ]
                },
                {
                    "pattern_number": 3,
                    "pattern_name": "〜のは ＋ …だ／…からだ／…ためだ",
                    "pattern_name_en": "no wa + ... da / kara da / tame da",
                    "meaning_ja": "取り上げた事柄について、その内容・理由・原因を述べる（分裂文）。",
                    "meaning_en": "Focuses on a topic and provides its content, cause, or reason at the end.",
                    "connection_forms": ["V-普通形 / A-い / Na-な / N-な + のは ＋ Nだ / 普通形+からだ / ためだ"],
                    "nuance_notes": "文頭に「〜のは」を置くことで、焦点となる理由や事象を文末で強調する。",
                    "example_sentences": [
                        {
                            "japanese": "わたしが<ruby>祖母<rt>そぼ</rt></ruby>について<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>せるのは、<ruby>優<rt>やさ</rt></ruby>しい<ruby>笑顔<rt>えがお</rt></ruby>だけだ。",
                            "english": "What I can recall about my grandmother is only her gentle smile."
                        },
                        {
                            "japanese": "<ruby>昨夜<rt>さくや</rt></ruby><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>れなかったのは、<ruby>急<rt>いそ</rt></ruby>ぎの<ruby>仕事<rt>しごと</rt></ruby>が<ruby>終<rt>お</rt></ruby>わらなかったからです。",
                            "english": "The reason I couldn't return home last night was that urgent work didn't finish."
                        }
                    ]
                },
                {
                    "pattern_number": 4,
                    "pattern_name": "どうして／なぜ〜かというと ＋ …からだ",
                    "pattern_name_en": "doushite / naze ~ ka to iu to + kara da",
                    "meaning_ja": "理由の疑問を提示して、後ろでその理由を説明する。",
                    "meaning_en": "Poses the question of 'why', and explains the reason at the end with 'kara da'.",
                    "connection_forms": ["どうして / なぜ + 普通形 + かというと ＋ …からだ / からです"],
                    "nuance_notes": "話し言葉・書き言葉ともに、理由を際立たせて説明する際によく用いられる。",
                    "example_sentences": [
                        {
                            "japanese": "どうしてこの<ruby>植物<rt>しょくぶつ</rt></ruby>にあまり<ruby>水<rt>みず</rt></ruby>をやらないかというと、その<ruby>方<rt>ほう</rt></ruby>がきれいに<ruby>花<rt>はな</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>くからです。",
                            "english": "If you ask why I don't give this plant much water, it's because flowers bloom more beautifully that way."
                        },
                        {
                            "japanese": "なぜこの<ruby>仕事<rt>しごと</rt></ruby>を<ruby>選<rt>えら</rt></ruby>んだかというと、<ruby>子<rt>こ</rt></ruby>どものときから<ruby>動物<rt>どうぶつ</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだったからだ。",
                            "english": "If asked why I chose this job, it's because I have loved animals since childhood."
                        }
                    ]
                },
                {
                    "pattern_number": 5,
                    "pattern_name": "助詞と動詞の呼応（受身文・使役文などの対応）",
                    "pattern_name_en": "Correspondence between particles and verbs (Passive, Causative, etc.)",
                    "meaning_ja": "文が長くなっても、助詞（〜に／〜を）と対応する動詞の態（能動・受身・使役）を正確に対応させる。",
                    "meaning_en": "Ensures particles correctly match the verb voice (active, passive, causative) across long clauses.",
                    "connection_forms": ["〜に ＋ （人）を紹介してもらう / 片付けさせる / 読まされる"],
                    "nuance_notes": "助詞と動詞が離れると対応を誤りやすいため、誰が誰に対して行為を行うのかを明確に意識する。",
                    "example_sentences": [
                        {
                            "japanese": "あしたリーさんに、だれか<ruby>中国料理<rt>ちゅうごくりょうり</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれる<ruby>人<rt>ひと</rt></ruby>を<ruby>紹介<rt>しょうかい</rt></ruby>してもらおう。",
                            "english": "Tomorrow I'll ask Mr. Lee to introduce someone who will teach me Chinese cuisine."
                        },
                        {
                            "japanese": "<ruby>母親<rt>ははおや</rt></ruby>は<ruby>子<rt>こ</rt></ruby>どもたちに、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>を<ruby>毎週<rt>まいしゅう</rt></ruby>1<ruby>回<rt>かい</rt></ruby>きれいに<ruby>片付<rt>かたづ</rt></ruby>けさせた。",
                            "english": "The mother made the children clean their rooms thoroughly once a week."
                        },
                        {
                            "japanese": "わたしは<ruby>先生<rt>せんせい</rt></ruby>に、その<ruby>文<rt>ぶん</rt></ruby>をすらすら<ruby>読<rt>よ</rt></ruby>めるようになるまで<ruby>何度<rt>なんど</rt></ruby>も<ruby>読<rt>よ</rt></ruby>まされた。",
                            "english": "I was made by the teacher to read that sentence over and over until I could read it smoothly."
                        }
                    ]
                }
            ],
            "drills": [
                {
                    "question_id": 1201,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>今<rt>いま</rt></ruby>、<ruby>困<rt>こま</rt></ruby>っているのは、（　）。",
                    "options": ["a　<ruby>お金<rt>かね</rt></ruby>のことだ。", "b　<ruby>お金<rt>かね</rt></ruby>が<ruby>足<rt>た</rt></ruby>りない。"],
                    "correct_answer": "a",
                    "explanation_ja": "「〜のは」の述語には「〜ことだ」や「〜からだ」などの名詞述語が対応する。「お金のことだ」が正しい。",
                    "explanation_en": "The predicate for '〜のは' corresponds with noun-predicate forms like '〜ことだ'. Thus 'お金のことだ' is correct."
                },
                {
                    "question_id": 1202,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>初<rt>はじ</rt></ruby>めて<ruby>飛行機<rt>ひこうき</rt></ruby>に<ruby>乗<rt>の</rt></ruby>ったのは、20<ruby>年前<rt>ねんまえ</rt></ruby>に（　）。",
                    "options": ["a　<ruby>両親<rt>りょうしん</rt></ruby>とアメリカへ<ruby>行<rt>い</rt></ruby>った。", "b　<ruby>両親<rt>りょうしん</rt></ruby>とアメリカへ<ruby>行<rt>い</rt></ruby>ったときだ。"],
                    "correct_answer": "b",
                    "explanation_ja": "「〜のは」に対応して時を表す名詞節「〜ときだ」が述語として呼応する。",
                    "explanation_en": "Corresponds to '〜のは' with the temporal noun predicate '〜ときだ'."
                },
                {
                    "question_id": 1203,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "（　）<ruby>昨夜<rt>さくや</rt></ruby>お<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みすぎたからだ。",
                    "options": ["a　<ruby>今朝<rt>けさはや</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きられなくて、", "b　<ruby>今朝<rt>けさはや</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>起<rt>お</rt></ruby>きられなかったのは、"],
                    "correct_answer": "b",
                    "explanation_ja": "理由を表す「〜からだ」に呼応して、主語節として「〜のは」が適切。",
                    "explanation_en": "Matches the reason-ending '〜からだ' with the subject clause '〜のは'."
                },
                {
                    "question_id": 1204,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "どうしてこの<ruby>計画<rt>けいかく</rt></ruby>が<ruby>中止<rt>ちゅうし</rt></ruby>になったかというと、（　）。",
                    "options": ["a　<ruby>予算<rt>よさん</rt></ruby>が<ruby>足<rt>た</rt></ruby>りません。", "b　<ruby>予算<rt>よさん</rt></ruby>が<ruby>足<rt>た</rt></ruby>りないからです。"],
                    "correct_answer": "b",
                    "explanation_ja": "文頭の「どうして〜かというと」に対応して文末は「〜からです」となる。",
                    "explanation_en": "'どうして〜かというと' corresponds with the concluding '〜からです'."
                },
                {
                    "question_id": 1205,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "この<ruby>地方<rt>ちほう</rt></ruby>には<ruby>昔<rt>むかし</rt></ruby>から<ruby>続<rt>つづ</rt></ruby>いている（　）。",
                    "options": ["a　<ruby>伝統的<rt>でんとうてき</rt></ruby>な<ruby>行事<rt>ぎょうじ</rt></ruby>がある。", "b　<ruby>伝統的<rt>でんとうてき</rt></ruby>な<ruby>行事<rt>ぎょうじ</rt></ruby>を<ruby>見<rt>み</rt></ruby>ることができる。"],
                    "correct_answer": "a",
                    "explanation_ja": "場所の主題提示「〜には」に対応して存在「〜がある」が呼応する。「見ることができる」の場合は「この地方では」となる。",
                    "explanation_en": "'〜には' pairs with existential predicate '〜がある'. For '見ることができる', 'この地方では' would be used."
                },
                {
                    "question_id": 1206,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>山<rt>やま</rt></ruby>の<ruby>頂上<rt>ちょうじょう</rt></ruby>まで<ruby>行<rt>い</rt></ruby>くには、ここからさらに2<ruby>時間<rt>じかん</rt></ruby>ぐらい（　）。",
                    "options": ["a　<ruby>登<rt>のぼ</rt></ruby>っていこう。", "b　<ruby>登<rt>のぼ</rt></ruby>らなければならない。"],
                    "correct_answer": "b",
                    "explanation_ja": "目的・条件の「〜には」に対応して義務・必要性を表す「〜なければならない」が呼応する。",
                    "explanation_en": "Purpose '〜には' pairs with necessity/obligation '〜なければならない'."
                },
                {
                    "question_id": 1207,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "つよしはじょうだんを<ruby>言<rt>い</rt></ruby>っていつもみんなを（　）。",
                    "options": ["a　<ruby>笑<rt>わら</rt></ruby>わせるから、クラスの<ruby>人気者<rt>にんきもの</rt></ruby>だ。", "b　<ruby>笑<rt>わら</rt></ruby>われるのは、なんだかかわいそうだ。"],
                    "correct_answer": "a",
                    "explanation_ja": "「みんなを」という対象・目的語をとる動詞として使役動詞「笑わせる」が呼応する。",
                    "explanation_en": "'みんなを' serves as the object of the causative verb '笑わせる' (makes everyone laugh)."
                },
                {
                    "question_id": 1208,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>林<rt>はやし</rt></ruby>さんはピアノが<ruby>好<rt>す</rt></ruby>きで、<ruby>子<rt>こ</rt></ruby>どもにも<ruby>小<rt>ちい</rt></ruby>さいときからずっと（　）。",
                    "options": ["a　<ruby>習<rt>なら</rt></ruby>っていた。", "b　<ruby>習<rt>なら</rt></ruby>わせていた。"],
                    "correct_answer": "b",
                    "explanation_ja": "「子どもにも」に対応して使役「習わせていた」（習うようにさせていた）が呼応する。",
                    "explanation_en": "With '子どもにも' as recipient of action, causative '習わせていた' (made/had the child learn) is required."
                },
                {
                    "question_id": 1209,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "この<ruby>学校<rt>がっこう</rt></ruby>ではバイクで<ruby>通学<rt>つうがく</rt></ruby>することを（　）。",
                    "options": ["a　10<ruby>年前<rt>ねんまえ</rt></ruby>から<ruby>校則<rt>こうそく</rt></ruby>で<ruby>禁止<rt>きんし</rt></ruby>している。", "b　<ruby>生徒会<rt>せいとかい</rt></ruby>で<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>った<ruby>結果<rt>けっか</rt></ruby>、<ruby>禁止<rt>きんし</rt></ruby>された。"],
                    "correct_answer": "a",
                    "explanation_ja": "「〜通学することを」という「を」格に対応して他動詞「禁止している」が呼応する。「禁止された」なら主格は「通学することが／は」となる。",
                    "explanation_en": "Direct object marker 'を' corresponds with transitive active verb '禁止している'."
                },
                {
                    "question_id": 1210,
                    "category": "Part3 1課 練習",
                    "question_type": "multiple_choice",
                    "prompt": "わたしは<ruby>母<rt>はは</rt></ruby>に、<ruby>寒<rt>さむ</rt></ruby>い<ruby>朝<rt>あさ</rt></ruby>でも<ruby>向<rt>む</rt></ruby>こうの<ruby>角<rt>かど</rt></ruby>の<ruby>所<rt>ところ</rt></ruby>までごみを<ruby>出<rt>だ</rt></ruby>しに（　）。",
                    "options": ["a　<ruby>行<rt>い</rt></ruby>かされる。", "b　<ruby>行<rt>い</rt></ruby>くことになる。"],
                    "correct_answer": "a",
                    "explanation_ja": "「わたしは母に〜（使役受身）」の呼応。母から強制・指示されてゴミ出しに行かされるので「行かされる」が正解。",
                    "explanation_en": "'わたしは母に〜' corresponds with causative-passive '行かされる' (am made to go)."
                }
            ]
        },

        # =========================================================================
        # SECTION 13: 第3部 第2課 時制・〜ている (p. 116-117)
        # =========================================================================
        {
            "section_number": 13,
            "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>2<ruby>課<rt>か</rt></ruby> <ruby>時制<rt>じせい</rt></ruby>・〜ている",
            "title_en": "Part 3 Lesson 2: Tense and -te iru",
            "theme": "文章における時制（テンス）の前後関係と「〜ている」（アスペクト）の使い分け",
            "patterns": [
                {
                    "pattern_number": 1,
                    "pattern_name": "時間を表す言葉と動詞の時制（過去形・現在形・〜ている）",
                    "pattern_name_en": "Time expressions and verb tense agreement",
                    "meaning_ja": "時間を表す副詞や連用句に合わせて動詞の時制を決定する。",
                    "meaning_en": "Matches verb tense with temporal adverbs and time indicators.",
                    "connection_forms": [
                        "間もなく / もうすぐ / 来年など ＋ 現在形（辞書形）",
                        "今 / 現在など ＋ 〜ている",
                        "去年 / 先週 / 4月1日になど ＋ 過去形（〜た）"
                    ],
                    "nuance_notes": "未来の出来事には非過去形、現在進行や継続状態には「〜ている」、過去の確定した出来事には「〜た」を用いる。",
                    "example_sentences": [
                        {
                            "japanese": "<ruby>間<rt>ま</rt></ruby>もなくこの<ruby>子<rt>こ</rt></ruby>は5<ruby>歳<rt>さい</rt></ruby>になる。",
                            "english": "Soon, this child will turn 5 years old."
                        },
                        {
                            "japanese": "<ruby>今<rt>いま</rt></ruby><ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っている。",
                            "english": "Snow is falling right now."
                        },
                        {
                            "japanese": "<ruby>去年<rt>きょねん</rt></ruby>わたしは<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>た。",
                            "english": "I came to Japan last year."
                        }
                    ]
                },
                {
                    "pattern_number": 2,
                    "pattern_name": "「〜ている」の諸用法（進行・習慣・結果残存・状態・完了未完了）",
                    "pattern_name_en": "Various functions of '~te iru'",
                    "meaning_ja": "進行中の動作、習慣、動作結果の残存状態、形状・様子、完了・未完了を表す。",
                    "meaning_en": "Expresses ongoing action, habitual action, continuing resultant state, appearance/form, or completion/incompletion.",
                    "connection_forms": ["V-て ＋ いる / いた / いない"],
                    "nuance_notes": "動詞の性質（瞬間動詞か継続動詞か）によって、「〜ている」が表す意味が異なる点に注意する。",
                    "example_sentences": [
                        {
                            "japanese": "わたしはそのとき<ruby>旅行<rt>りょこう</rt></ruby>の<ruby>準備<rt>じゅんび</rt></ruby>をしていた。",
                            "english": "I was preparing for the trip at that time (action in progress)."
                        },
                        {
                            "japanese": "<ruby>弟<rt>おとうと</rt></ruby>は<ruby>毎日<rt>まいにち</rt></ruby>サッカーの<ruby>練習<rt>れんしゅう</rt></ruby>に<ruby>行<rt>い</rt></ruby>っている。",
                            "english": "My younger brother goes to soccer practice every day (habit)."
                        },
                        {
                            "japanese": "<ruby>駅<rt>えき</rt></ruby>のホームに<ruby>財布<rt>さいふ</rt></ruby>が<ruby>落<rt>お</rt></ruby>ちていた。",
                            "english": "A wallet was lying on the train platform (resultant state)."
                        },
                        {
                            "japanese": "<ruby>町田<rt>まちだ</rt></ruby>さんはめがねをかけている。",
                            "english": "Machida is wearing glasses (resultant state)."
                        },
                        {
                            "japanese": "この<ruby>道<rt>みち</rt></ruby>は<ruby>海<rt>うみ</rt></ruby>に<ruby>続<rt>つづ</rt></ruby>いている。",
                            "english": "This road continues to the sea (form and appearance)."
                        },
                        {
                            "japanese": "9<ruby>時<rt>じ</rt></ruby>に<ruby>会場<rt>かいじょう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いた。もうみんな<ruby>来<rt>き</rt></ruby>ていた。",
                            "english": "I arrived at the venue at 9:00. Everyone had already arrived (completion)."
                        },
                        {
                            "japanese": "この<ruby>子<rt>こ</rt></ruby>はまだ5<ruby>歳<rt>さい</rt></ruby>になっていません。",
                            "english": "This child has not yet turned 5 years old (incompletion)."
                        }
                    ]
                },
                {
                    "pattern_number": 3,
                    "pattern_name": "「〜とき」や名詞修飾節における前後関係と時制",
                    "pattern_name_en": "Tense agreement in 'toki' clauses and relative clauses",
                    "meaning_ja": "主節の動作より先に起こるか後に起こるかによって、従属節の動詞の形（辞書形か〜た形か）を決める。",
                    "meaning_en": "Determines whether relative or 'toki' clauses take non-past or past forms depending on relative event order.",
                    "connection_forms": [
                        "V-る ＋ とき（主節の動作より後に起きる場合）",
                        "V-た ＋ とき（主節の動作より先に起きた場合）"
                    ],
                    "nuance_notes": "主文の時制が過去であっても、従属節のできごとが主文より後なら辞書形を使う。",
                    "example_sentences": [
                        {
                            "japanese": "ご<ruby>飯<rt>はん</rt></ruby>を<ruby>食<rt>た</rt></ruby>べたとき、「ごちそうさま」と<ruby>言<rt>い</rt></ruby>います。",
                            "english": "When we have finished eating, we say 'Gochisousama' (eating happens before saying)."
                        },
                        {
                            "japanese": "ご<ruby>飯<rt>はん</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるとき、「いただきます」と<ruby>言<rt>い</rt></ruby>います。",
                            "english": "When we eat, we say 'Itadakimasu' (saying happens before eating)."
                        },
                        {
                            "japanese": "<ruby>新幹線<rt>しんかんせん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>飲<rt>の</rt></ruby>むお<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>駅<rt>えき</rt></ruby>の<ruby>売店<rt>ばいてん</rt></ruby>で<ruby>買<rt>か</rt></ruby>った。",
                            "english": "I bought tea at the station shop to drink on the Shinkansen (bought first, drinking later)."
                        }
                    ]
                }
            ],
            "drills": [
                # 練習1 (p. 117)
                {
                    "question_id": 1301,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>置<rt>お</rt></ruby>いておいたぼくの<ruby>大事<rt>だいじ</rt></ruby>な<ruby>本<rt>ほん</rt></ruby>はどこに（　）のだろう。",
                    "options": ["a　<ruby>行<rt>い</rt></ruby>く", "b　<ruby>行<rt>い</rt></ruby>った"],
                    "correct_answer": "b",
                    "explanation_ja": "本がどこかへなくなってしまった過去の事象を表すので「行った」が正解。",
                    "explanation_en": "Refers to where the book has gone (past event/disappearance): '行った'."
                },
                {
                    "question_id": 1302,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>来月<rt>らいげつ</rt></ruby>、わたしがこの5<ruby>年間<rt>ねんかん</rt></ruby>で（　）<ruby>作品<rt>さくひん</rt></ruby>の<ruby>展覧会<rt>てんらんかい</rt></ruby>が<ruby>開<rt>ひら</rt></ruby>かれます。",
                    "options": ["a　<ruby>作<rt>つく</rt></ruby>る", "b　<ruby>作<rt>つく</rt></ruby>った"],
                    "correct_answer": "b",
                    "explanation_ja": "展覧会は来月だが、作品を制作したのは過去5年間の完了した行為なので「作った」が適切。",
                    "explanation_en": "Although the exhibition is next month, the creation of works occurred during the past 5 years: '作った'."
                },
                {
                    "question_id": 1303,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>駅<rt>えき</rt></ruby>まで<ruby>遠<rt>とお</rt></ruby>いですから、<ruby>歩<rt>ある</rt></ruby>いていくのでは（　）。",
                    "options": ["a　<ruby>疲<rt>つか</rt></ruby>れますよ", "b　<ruby>疲<rt>つか</rt></ruby>れていますよ"],
                    "correct_answer": "a",
                    "explanation_ja": "これから歩いて行った場合の結果・予想を述べるので非過去形「疲れますよ」が適切。",
                    "explanation_en": "Predicts a future outcome from walking: '疲れますよ' (you will get tired)."
                },
                {
                    "question_id": 1304,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "きのうわたしは12<ruby>時<rt>じ</rt></ruby><ruby>過<rt>す</rt></ruby>ぎまで（　）。",
                    "options": ["a　<ruby>起<rt>お</rt></ruby>きた", "b　<ruby>起<rt>お</rt></ruby>きていた"],
                    "correct_answer": "b",
                    "explanation_ja": "12時過ぎまで覚醒した状態が継続していたことを表すため「起きていた」が正解。「起きた」は起床の瞬間動作を表す。",
                    "explanation_en": "'起きていた' denotes staying awake continuously until past 12:00. '起きた' means waking up."
                },
                {
                    "question_id": 1305,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "まだ<ruby>昼<rt>ひる</rt></ruby>ご<ruby>飯<rt>はん</rt></ruby>を（　）のなら、いっしょにどうですか。",
                    "options": ["a　<ruby>食<rt>た</rt></ruby>べない", "b　<ruby>食<rt>た</rt></ruby>べていない"],
                    "correct_answer": "b",
                    "explanation_ja": "「まだ」とともに用いて未完了の状態を表すため「食べていない」が適切。",
                    "explanation_en": "With 'まだ', incompleteness of an action is expressed by '〜ていない': '食べていない'."
                },
                {
                    "question_id": 1306,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "うちに（　）ときは、<ruby>連絡<rt>れんらく</rt></ruby>してください。<ruby>駅<rt>えき</rt></ruby>まで<ruby>迎<rt>むか</rt></ruby>えに<ruby>行<rt>い</rt></ruby>きます。",
                    "options": ["a　<ruby>来<rt>く</rt></ruby>る", "b　<ruby>来<rt>き</rt></ruby>た"],
                    "correct_answer": "a",
                    "explanation_ja": "駅に迎えに行くため、家に来る前（連絡する→家に来る）に連絡してもらう必要があるので辞書形「来る」が正しい。",
                    "explanation_en": "Because the speaker will pick them up at the station, the calling must happen before arriving home: '来る'."
                },
                {
                    "question_id": 1307,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>彼<rt>かれ</rt></ruby>が<ruby>港<rt>みなと</rt></ruby>に（①　）ときには、<ruby>船<rt>ふね</rt></ruby>はもう（②　）。",
                    "options": [
                        "① a <ruby>着<rt>つ</rt></ruby>いた / b <ruby>着<rt>つ</rt></ruby>いている",
                        "② a <ruby>出<rt>で</rt></ruby>た / b <ruby>出<rt>で</rt></ruby>ていた"
                    ],
                    "correct_answer": "① a　② b",
                    "explanation_ja": "彼が港に到着した過去の一時点において、船はすでに出発してしまっていた（完了状態）ため、①は「着いた」、②は「出ていた」となる。",
                    "explanation_en": "When he arrived at the port (past point: 着いた), the ship had already departed (resultant past state: 出ていた)."
                },
                {
                    "question_id": 1308,
                    "category": "Part3 2課 練習1",
                    "question_type": "multiple_choice",
                    "prompt": "あした、<ruby>林<rt>はやし</rt></ruby>さんに（①　）ときに、この<ruby>本<rt>ほん</rt></ruby>を（②　）。",
                    "options": [
                        "① a <ruby>会<rt>あ</rt></ruby>う / b <ruby>会<rt>あ</rt></ruby>った",
                        "② a <ruby>返<rt>かえ</rt></ruby>そう / b <ruby>返<rt>かえ</rt></ruby>した"
                    ],
                    "correct_answer": "① b　② a",
                    "explanation_ja": "明日林さんに会ったその時点で本を返そうという意図を表す。林さんに会う行為が成立したとき（会ったとき）に本を返す（返そう）ため、①は「会った」、②は「返そう」となる。",
                    "explanation_en": "At the point when meeting Hayashi takes place (会ったとき), the speaker intends to return the book (返そう)."
                },

                # 練習2 (p. 117) - Fill in the blank paragraph
                {
                    "question_id": 1309,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>子<rt>こ</rt></ruby>どものころ、わたしのうちにはいろいろな<ruby>動物<rt>どうぶつ</rt></ruby>が（①いる→［　］）。",
                    "correct_answer": "いた",
                    "explanation_ja": "「子どものころ」という過去の継続状態を表すので過去形「いた」となる。",
                    "explanation_en": "Describes a past continuing state during childhood: 'いた'."
                },
                {
                    "question_id": 1310,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>犬<rt>いぬ</rt></ruby>はもちろん、うさぎ、<ruby>鳥<rt>とり</rt></ruby>、にわとりなど、みんな<ruby>母<rt>はは</rt></ruby>がどこからか（②もらってくる→［　］）<ruby>動物<rt>どうぶつ</rt></ruby>だった。",
                    "correct_answer": "もらってきた",
                    "explanation_ja": "動物をもらってきた過去の動作が完了した結果の修飾節なので「もらってきた」となる。",
                    "explanation_en": "Past completed action modifying '動物': 'もらってきた'."
                },
                {
                    "question_id": 1311,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>母<rt>はは</rt></ruby>は<ruby>動物<rt>どうぶつ</rt></ruby>の<ruby>世話<rt>せわ</rt></ruby>にとても<ruby>興味<rt>きょうみ</rt></ruby>を（③<ruby>持<rt>も</rt></ruby>つ→［　］）が、これらの<ruby>動物<rt>どうぶつ</rt></ruby>にえさを（④やる→［　］）のはわたしの<ruby>仕事<rt>しごと</rt></ruby>だった。",
                    "correct_answer": "持っていた",
                    "explanation_ja": "母が当時興味を持っていたという過去の心理的継続状態を表すので「持っていた」となる。",
                    "explanation_en": "Describes the mother's past state of interest: '持っていた'."
                },
                {
                    "question_id": 1312,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "これらの<ruby>動物<rt>どうぶつ</rt></ruby>にえさを（④やる→［　］）のはわたしの<ruby>仕事<rt>しごと</rt></ruby>だった。",
                    "correct_answer": "やる",
                    "explanation_ja": "「えさを〜のはわたしの仕事だった」という名詞節では、行為内容を表す辞書形「やる」を用いる。",
                    "explanation_en": "In the noun clause 'えさを〜のは', the dictionary form 'やる' denotes the recurring task."
                },
                {
                    "question_id": 1313,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "わたしは<ruby>母<rt>はは</rt></ruby>が<ruby>入<rt>い</rt></ruby>れ<ruby>物<rt>もの</rt></ruby>に（⑤<ruby>入<rt>い</rt></ruby>れる→［　］）えさを<ruby>自分<rt>じぶん</rt></ruby>の<ruby>手<rt>て</rt></ruby>で<ruby>動物<rt>どうぶつ</rt></ruby>たちに<ruby>与<rt>あた</rt></ruby>えた。",
                    "correct_answer": "入れた",
                    "explanation_ja": "母が事前に餌を入れ物に入れた（完了した動作）後で与えたので、過去形「入れた」となる。",
                    "explanation_en": "The food that the mother had previously put into the container: '入れた'."
                },
                {
                    "question_id": 1314,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>当時<rt>とうじ</rt></ruby>わたしはまだ<ruby>小学生<rt>しょうがくせい</rt></ruby>に（⑥なる→［　］）が、<ruby>母<rt>はは</rt></ruby>の<ruby>影響<rt>えいきょう</rt></ruby>でいつの<ruby>間<rt>ま</rt></ruby>にか<ruby>大<rt>だい</rt></ruby>の<ruby>動物好<rt>どうぶつず</rt></ruby>きになっていた。",
                    "correct_answer": "なっていなかった",
                    "explanation_ja": "「当時まだ小学生になっていなかった」（未完了の過去状態）を表すので「なっていなかった」となる。",
                    "explanation_en": "Past incomplete state (had not yet become an elementary school student): 'なっていなかった'."
                },
                {
                    "question_id": 1315,
                    "category": "Part3 2課 練習2",
                    "question_type": "fill_in_the_blank",
                    "prompt": "だから、<ruby>動物園<rt>どうぶつえん</rt></ruby>に（⑦<ruby>就職<rt>しゅうしょく</rt></ruby>できる→［　］）ときは、<ruby>本当<rt>ほんとう</rt></ruby>にうれしかった。",
                    "correct_answer": "就職できた",
                    "explanation_ja": "就職することが確定・実現した過去の時点（〜できたとき）を指すので過去形「就職できた」となる。",
                    "explanation_en": "When gaining employment was successfully accomplished in the past: '就職できた'."
                }
            ]
        },

        # =========================================================================
        # SECTION 14: 第3部 まとめ問題（1課・2課） (p. 118-121)
        # =========================================================================
        {
            "section_number": 14,
            "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby> まとめ<ruby>問題<rt>もんだい</rt></ruby>（1<ruby>課<rt>か</rt></ruby>・2<ruby>課<rt>か</rt></ruby>）",
            "title_en": "Part 3 Review Exercises (Lessons 1 & 2)",
            "theme": "文章全体の文脈を捉えた時制・文の始めと終わりの対応の総合問題",
            "patterns": [],
            "passages": [
                {
                    "passage_number": 1,
                    "title": "文章 1: 外国語の勉強についてのアドバイス",
                    "text": "わたしは<ruby>言葉<rt>ことば</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。<ruby>今<rt>いま</rt></ruby>までにいくつかの<ruby>外国語<rt>がいこくご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>したことがあります。<ruby>日本語<rt>にほんご</rt></ruby>は<ruby>国<rt>くに</rt></ruby>にいるとき1<ruby>年<rt>ねん</rt></ruby>ぐらい<ruby>勉強<rt>べんきょう</rt></ruby>しましたが、<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>てからも<ruby>続<rt>つづ</rt></ruby>けています。<ruby>今<rt>いま</rt></ruby>、<ruby>毎週火曜日<rt>まいしゅうかようび</rt></ruby>と<ruby>木曜日<rt>もくようび</rt></ruby>の<ruby>夜<rt>よる</rt></ruby>、<ruby>市民<rt>しみん</rt></ruby>センターに<ruby>行<rt>い</rt></ruby>って、<ruby>田中<rt>たなか</rt></ruby>さんから<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おそ</rt></ruby>わっています。レッスンのときに［ 1-a ］ことは<ruby>前<rt>まえ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に<ruby>予習<rt>よしゅう</rt></ruby>し、［ 1-b ］ことは<ruby>必<rt>かなら</rt></ruby>ず<ruby>復習<rt>ふくしゅう</rt></ruby>しています。\n<ruby>外国語<rt>がいこくご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>しようとする<ruby>人<rt>ひと</rt></ruby>にアドバイスすることが<ruby>三<rt>みっ</rt></ruby>つあります。まずするべきこととは、いい<ruby>先生<rt>せんせい</rt></ruby>を［ 2 ］。<ruby>何回<rt>なんかい</rt></ruby>かレッスンを<ruby>受<rt>う</rt></ruby>ければ、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>スタイルに<ruby>合<rt>あ</rt></ruby>う<ruby>先生<rt>せんせい</rt></ruby>かどうかわかります。どういう<ruby>教<rt>おし</rt></ruby>え<ruby>方<rt>かた</rt></ruby>をしてほしいか<ruby>先生<rt>せんせい</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えてもいいと<ruby>思<rt>おも</rt></ruby>います。\nまた、<ruby>勉強<rt>べんきょう</rt></ruby>が<ruby>難<rt>むずか</rt></ruby>しくなると、なかなか<ruby>次<rt>つぎ</rt></ruby>に<ruby>進<rt>すす</rt></ruby>めなくなります。しかし、<ruby>同<rt>おな</rt></ruby>じところばかりずっと［ 3 ］、だんだんあきてきます。そういうときは<ruby>全部<rt>ぜんぶ</rt></ruby>［ 4 ］、<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>先<rt>さき</rt></ruby>に<ruby>進<rt>すす</rt></ruby>んだほうがいいです。そして、<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は、<ruby>習<rt>なら</rt></ruby>ったことをどれぐらい<ruby>覚<rt>おぼ</rt></ruby>えているかということより、どれだけ［ 5 ］ということの<ruby>方<rt>ほう</rt></ruby>が<ruby>大切<rt>たいせつ</rt></ruby>だということです。<ruby>勉強<rt>べんきょう</rt></ruby>したことを<ruby>実際<rt>じっさい</rt></ruby>にどんどん<ruby>使<rt>つか</rt></ruby>ってみることが<ruby>大事<rt>だいじ</rt></ruby>です。",
                    "text_en": "I like studying languages. So far I have studied several foreign languages. I studied Japanese for about a year while in my home country, and have continued since coming to Japan. Now, every Tuesday and Thursday evening, I go to the community center to be taught Japanese by Mr. Tanaka. I preview the things to be studied in the lesson on the preceding day, and always review what I have studied. I have three pieces of advice for people trying to study a foreign language. First, what you should do is find a good teacher. After taking several lessons, you will see whether the teacher matches your study style. I think it is also fine to tell the teacher how you want them to teach. Also, when study gets difficult, it is hard to move on. However, if you keep doing only the same part constantly, you will gradually get bored. At such times, even if you can't remember everything, it is better to move forward little by little. And third, rather than how much of what you learned you remember, how much you are using it is what matters. It is important to actually try using what you studied more and more."
                },
                {
                    "passage_number": 2,
                    "title": "文章 2: 公園のありの巣の観察",
                    "text": "<ruby>先日<rt>せんじつ</rt></ruby>、<ruby>公園<rt>こうえん</rt></ruby>で、ありが<ruby>忙<rt>いそが</rt></ruby>しそうに<ruby>働<rt>はたら</rt></ruby>いているのを<ruby>見<rt>み</rt></ruby>た。<ruby>白<rt>しろ</rt></ruby>い<ruby>小<rt>ちい</rt></ruby>さなものを［ 1 ］。<ruby>行列<rt>ぎょうれつ</rt></ruby>の<ruby>先<rt>さき</rt></ruby>を<ruby>見<rt>み</rt></ruby>ると、<ruby>地面<rt>じめん</rt></ruby>に<ruby>小<rt>ちい</rt></ruby>さな<ruby>穴<rt>あな</rt></ruby>が<ruby>開<rt>あ</rt></ruby>いていた。ありの<ruby>巣<rt>す</rt></ruby>だ。<ruby>穴<rt>あな</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りには、<ruby>穴<rt>あな</rt></ruby>を<ruby>掘<rt>ほ</rt></ruby>ったときに<ruby>出<rt>で</rt></ruby>た<ruby>土<rt>つち</rt></ruby>が<ruby>盛<rt>も</rt></ruby>られていた。この<ruby>土<rt>つち</rt></ruby>の<ruby>山<rt>やま</rt></ruby>があるので、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っても<ruby>周<rt>まわ</rt></ruby>りから<ruby>雨水<rt>あまみず</rt></ruby>が<ruby>入<rt>はい</rt></ruby>りにくくなっているようだ。<ruby>穴<rt>あな</rt></ruby>の<ruby>中<rt>なか</rt></ruby>は［ 2 ］。<ruby>自分<rt>じぶん</rt></ruby>で<ruby>中<rt>なか</rt></ruby>を<ruby>見<rt>み</rt></ruby>ることはできないので、<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってインターネットで<ruby>調<rt>しら</rt></ruby>べてみた。\nある<ruby>専門家<rt>せんもんか</rt></ruby>のページによると、ありの<ruby>巣<rt>す</rt></ruby>は、<ruby>初<rt>はじ</rt></ruby>めは<ruby>女王<rt>じょおう</rt></ruby>ありがたった1<ruby>匹<rt>ぴき</rt></ruby>で［ 3 ］。<ruby>最初<rt>さいしょ</rt></ruby>は<ruby>一部屋<rt>ひとへや</rt></ruby>だけで、<ruby>女王<rt>じょおう</rt></ruby>はそこで<ruby>卵<rt>たまご</rt></ruby>を<ruby>産<rt>う</rt></ruby>んで［ 4 ］。<ruby>卵<rt>たまご</rt></ruby>は1か<ruby>月<rt>げつ</rt></ruby>ぐらいで<ruby>働<rt>はたら</rt></ruby>きありに<ruby>成長<rt>せいちょう</rt></ruby>し、この<ruby>働<rt>はたら</rt></ruby>きありが<ruby>巣<rt>す</rt></ruby>を<ruby>大<rt>おお</rt></ruby>きくしていくらしい。<ruby>卵<rt>たまご</rt></ruby>を<ruby>置<rt>お</rt></ruby>いておく<ruby>部屋<rt>へや</rt></ruby>、えさを<ruby>置<rt>お</rt></ruby>いておく<ruby>部屋<rt>へや</rt></ruby>、<ruby>子<rt>こ</rt></ruby>ども<ruby>部屋<rt>べや</rt></ruby>など、<ruby>人間<rt>にんげん</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>よりも［ 5 ］。<ruby>女王<rt>じょおう</rt></ruby>ありの<ruby>部屋<rt>へや</rt></ruby>はいちばん<ruby>奥<rt>おく</rt></ruby>で、<ruby>女王<rt>じょおう</rt></ruby>はここで<ruby>出産<rt>しゅっさん</rt></ruby>と<ruby>子育<rt>こそだ</rt></ruby>てに<ruby>集中<rt>しゅうちゅう</rt></ruby>するのだそうだ。",
                    "text_en": "The other day, I saw ants working busily in the park. They were carrying small white objects. Looking ahead in the line, there was a small hole open in the ground. It was an ant nest. Around the hole, earth dug out when making the hole was piled up. Because of this mound of earth, even if it rains, rainwater seems unlikely to enter from around it. How might the inside of the hole be structured? Since I could not look inside myself, I went home and looked it up on the Internet. According to an expert's webpage, an ant nest is initially built by just one queen ant. At first there is only one room, where the queen lays eggs and raises them. In about one month, the eggs grow into worker ants, and these worker ants supposedly enlarge the nest. With rooms for placing eggs, rooms for storing food, nurseries, and so forth, it has more rooms than a human house. The queen ant's chamber is the deepest within, where the queen reportedly concentrates on giving birth and raising offspring."
                }
            ],
            "drills": [
                # Passage 1 (p. 120)
                {
                    "question_id": 1401,
                    "category": "Part3 まとめ問題 1課・2課 文章1",
                    "question_type": "multiple_choice",
                    "prompt": "レッスンのときに［ 1-a ］ことは<ruby>前<rt>まえ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に<ruby>予習<rt>よしゅう</rt></ruby>し、［ 1-b ］ことは<ruby>必<rt>かなら</rt></ruby>ず<ruby>復習<rt>ふくしゅう</rt></ruby>しています。",
                    "options": [
                        "1　a <ruby>勉強<rt>べんきょう</rt></ruby>する／b <ruby>勉強<rt>べんきょう</rt></ruby>した",
                        "2　a <ruby>勉強<rt>べんきょう</rt></ruby>した／b <ruby>勉強<rt>べんきょう</rt></ruby>する",
                        "3　a <ruby>勉強<rt>べんきょう</rt></ruby>している／b <ruby>勉強<rt>べんきょう</rt></ruby>した",
                        "4　a <ruby>勉強<rt>べんきょう</rt></ruby>していた／b <ruby>勉強<rt>べんきょう</rt></ruby>する"
                    ],
                    "correct_answer": "1",
                    "explanation_ja": "予習はレッスンより前に「これから勉強すること」なので辞書形（勉強する）、復習はレッスン後に「すでに勉強したこと」なので過去形（勉強した）となる。したがって1が正解。",
                    "explanation_en": "Preview (予習) applies to what will be studied in the upcoming lesson (勉強する), and review (復習) applies to what has already been studied (勉強した). Thus 1 is correct."
                },
                {
                    "question_id": 1402,
                    "category": "Part3 まとめ問題 1課・2課 文章1",
                    "question_type": "multiple_choice",
                    "prompt": "まずするべきこととは、いい<ruby>先生<rt>せんせい</rt></ruby>を［ 2 ］。",
                    "options": [
                        "1　<ruby>探<rt>さが</rt></ruby>します",
                        "2　<ruby>探<rt>さが</rt></ruby>すことです",
                        "3　<ruby>探<rt>さが</rt></ruby>しています",
                        "4　<ruby>探<rt>さが</rt></ruby>していることです"
                    ],
                    "correct_answer": "2",
                    "explanation_ja": "文頭の「まずするべきこととは〜」に呼応して、文末は「〜（動詞辞書形＋）ことです」となる。",
                    "explanation_en": "'まずするべきこととは〜' at the beginning matches the conclusion '〜探すことです'."
                },
                {
                    "question_id": 1403,
                    "category": "Part3 まとめ問題 1課・2課 文章1",
                    "question_type": "multiple_choice",
                    "prompt": "しかし、<ruby>同<rt>おな</rt></ruby>じところばかりずっと［ 3 ］、だんだんあきてきます。",
                    "options": [
                        "1　やっていると",
                        "2　やっていたので",
                        "3　やってみると",
                        "4　やってみたので"
                    ],
                    "correct_answer": "1",
                    "explanation_ja": "同じところばかり継続して行っていると飽きてくるという仮定・条件の呼応なので「やっていると」が適切。",
                    "explanation_en": "'やっていると' presents the continuing condition that naturally leads to getting bored."
                },
                {
                    "question_id": 1404,
                    "category": "Part3 まとめ問題 1課・2課 文章1",
                    "question_type": "multiple_choice",
                    "prompt": "そういうときは<ruby>全部<rt>ぜんぶ</rt></ruby>［ 4 ］、<ruby>少<rt>すこ</rt></ruby>しずつ<ruby>先<rt>さき</rt></ruby>に<ruby>進<rt>すす</rt></ruby>んだほうがいいです。",
                    "options": [
                        "1　<ruby>覚<rt>おぼ</rt></ruby>えられないと",
                        "2　<ruby>覚<rt>おぼ</rt></ruby>えられなくても",
                        "3　<ruby>覚<rt>おぼ</rt></ruby>えられたら",
                        "4　<ruby>覚<rt>おぼ</rt></ruby>えられたので"
                    ],
                    "correct_answer": "2",
                    "explanation_ja": "「全部覚えられなくても（たとえ全部覚えられなくても）、少しずつ先に進んだほうがいい」という逆接の仮定条件「〜ても」が文脈に適合する。",
                    "explanation_en": "'覚えられなくても' (even if you cannot memorize everything) establishes the concession matching '先に進んだほうがいい'."
                },
                {
                    "question_id": 1405,
                    "category": "Part3 まとめ問題 1課・2課 文章1",
                    "question_type": "multiple_choice",
                    "prompt": "そして、<ruby>三<rt>みっ</rt></ruby>つ<ruby>目<rt>め</rt></ruby>は、<ruby>習<rt>なら</rt></ruby>ったことをどれぐらい<ruby>覚<rt>おぼ</rt></ruby>えているかということより、どれだけ［ 5 ］ということの<ruby>方<rt>ほう</rt></ruby>が<ruby>大切<rt>たいせつ</rt></ruby>だということです。",
                    "options": [
                        "1　<ruby>使<rt>つか</rt></ruby>ってみる",
                        "2　<ruby>使<rt>つか</rt></ruby>ってみるの",
                        "3　<ruby>使<rt>つか</rt></ruby>っている",
                        "4　<ruby>使<rt>つか</rt></ruby>っているか"
                    ],
                    "correct_answer": "4",
                    "explanation_ja": "前節の「どれぐらい覚えているかということより」と対比して、「どれだけ〜かということ」の呼応が必要なので「使っているか」が正解。",
                    "explanation_en": "Matches the parallel interrogative clause structure 'どれぐらい覚えているか' with 'どれだけ使っているか'."
                },

                # Passage 2 (p. 121)
                {
                    "question_id": 1406,
                    "category": "Part3 まとめ問題 1課・2課 文章2",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>白<rt>しろ</rt></ruby>い<ruby>小<rt>ちい</rt></ruby>さなものを［ 1 ］。",
                    "options": [
                        "1　<ruby>運<rt>はこ</rt></ruby>んだ",
                        "2　<ruby>運<rt>はこ</rt></ruby>んでいた",
                        "3　<ruby>運<rt>はこ</rt></ruby>ばれた",
                        "4　<ruby>運<rt>はこ</rt></ruby>ばれていた"
                    ],
                    "correct_answer": "2",
                    "explanation_ja": "直前の「ありが忙しそうに働いているのを見た」に呼応し、ありが白いものを運んでいる進行中の様子を目撃したので「運んでいた」が適切。",
                    "explanation_en": "Describes the ongoing action witnessed at that moment: '運んでいた' (were carrying)."
                },
                {
                    "question_id": 1407,
                    "category": "Part3 まとめ問題 1課・2課 文章2",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>穴<rt>あな</rt></ruby>の<ruby>中<rt>なか</rt></ruby>は［ 2 ］。<ruby>自分<rt>じぶん</rt></ruby>で<ruby>中<rt>なか</rt></ruby>を<ruby>見<rt>み</rt></ruby>ることはできないので、<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってインターネットで<ruby>調<rt>しら</rt></ruby>べてみた。",
                    "options": [
                        "1　どうなるのだろう",
                        "2　どうしたのだろう",
                        "3　どうなっているのだろう",
                        "4　どうしていたのだろう"
                    ],
                    "correct_answer": "3",
                    "explanation_ja": "巣の内部の現在の構造や状態に対する疑問・好奇心を表すので「どうなっているのだろう」が正解。",
                    "explanation_en": "Inquires about the internal condition and structure of the nest: 'どうなっているのだろう'."
                },
                {
                    "question_id": 1408,
                    "category": "Part3 まとめ問題 1課・2課 文章2",
                    "question_type": "multiple_choice",
                    "prompt": "ある<ruby>専門家<rt>せんもんか</rt></ruby>のページによると、ありの<ruby>巣<rt>す</rt></ruby>は、<ruby>初<rt>はじ</rt></ruby>めは<ruby>女王<rt>じょおう</rt></ruby>ありがたった1<ruby>匹<rt>ぴき</rt></ruby>で［ 3 ］。",
                    "options": [
                        "1　<ruby>作<rt>つく</rt></ruby>るそうだ",
                        "2　<ruby>作<rt>つく</rt></ruby>ったそうだ",
                        "3　<ruby>作<rt>つく</rt></ruby>られるそうだ",
                        "4　<ruby>作<rt>つく</rt></ruby>られたそうだ"
                    ],
                    "correct_answer": "1",
                    "explanation_ja": "専門家の説明による伝聞で、生物の一般的な習性・営巣プロセスを述べているため、非過去の能動形「作るそうだ」が適切。",
                    "explanation_en": "Hearsay report describing general ecological habits of ants: '作るそうだ' (they say it builds)."
                },
                {
                    "question_id": 1409,
                    "category": "Part3 まとめ問題 1課・2課 文章2",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>最初<rt>さいしょ</rt></ruby>は<ruby>一部屋<rt>ひとへや</rt></ruby>だけで、<ruby>女王<rt>じょおう</rt></ruby>はそこで<ruby>卵<rt>たまご</rt></ruby>を<ruby>産<rt>う</rt></ruby>んで［ 4 ］。",
                    "options": [
                        "1　<ruby>育<rt>そだ</rt></ruby>てる",
                        "2　<ruby>育<rt>そだ</rt></ruby>てた",
                        "3　<ruby>育<rt>そだ</rt></ruby>てられる",
                        "4　<ruby>育<rt>そだ</rt></ruby>てられた"
                    ],
                    "correct_answer": "1",
                    "explanation_ja": "女王ありが自ら卵を産んで育てる習性を説明する文文脈のため、非過去能動形「育てる」が適切。",
                    "explanation_en": "Active non-past verb describing the queen ant's habit of raising offspring: '育てる'."
                },
                {
                    "question_id": 1410,
                    "category": "Part3 まとめ問題 1課・2課 文章2",
                    "question_type": "multiple_choice",
                    "prompt": "<ruby>卵<rt>たまご</rt></ruby>を<ruby>置<rt>お</rt></ruby>いておく<ruby>部屋<rt>へや</rt></ruby>、えさを<ruby>置<rt>お</rt></ruby>いておく<ruby>部屋<rt>へや</rt></ruby>、<ruby>子<rt>こ</rt></ruby>ども<ruby>部屋<rt>べや</rt></ruby>など、<ruby>人間<rt>にんげん</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>よりも［ 5 ］。",
                    "options": [
                        "1　よく<ruby>働<rt>はたら</rt></ruby>く",
                        "2　<ruby>子<rt>こ</rt></ruby>どもが<ruby>多<rt>おお</rt></ruby>い",
                        "3　<ruby>簡単<rt>かんたん</rt></ruby>に<ruby>作<rt>つく</rt></ruby>った",
                        "4　<ruby>部屋<rt>へや</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い"
                    ],
                    "correct_answer": "4",
                    "explanation_ja": "直前で様々な用途の部屋（卵の部屋、餌の部屋、子ども部屋）が列挙されているので、「人間の家よりも部屋が多い」が意味的に正解。",
                    "explanation_en": "Refers to the variety of specialized rooms listed immediately prior: '部屋が多い' (has more rooms)."
                }
            ]
        },

        # =========================================================================
        # SECTION 15: 第3部 第3課 話者が見る位置を動かさない手段-1 他動詞・自動詞 (p. 122-123)
        # =========================================================================
        {
            "section_number": 15,
            "title": "<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>3<ruby>課<rt>か</rt></ruby> <ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かさない<ruby>手段<rt>しゅだん</rt></ruby>-1 <ruby>他動詞<rt>たどうし</rt></ruby>・<ruby>自動詞<rt>じどうし</rt></ruby>",
            "title_en": "Part 3 Lesson 3: Techniques to Maintain Speaker's Viewpoint 1 - Transitive and Intransitive Verbs",
            "theme": "視点を一貫させるための他動詞と自動詞の使い分け（動作への注目 vs 結果・自然現象、受身・使役との連携）",
            "patterns": [
                {
                    "pattern_number": 1,
                    "pattern_name": "他動詞の文（変化を起こす動作に注目／人や物への働きかけ）",
                    "pattern_name_en": "Transitive sentences: focus on action causing change / affecting others",
                    "meaning_ja": "主体が対象に対して変化を起こす動作、または人や物へ働きかける動作を表す。",
                    "meaning_en": "Expresses an action causing a change to an object, or impelling other people or things.",
                    "connection_forms": ["N（人/物）を ＋ 他動詞", "N（人）に ＋ N（物）を ＋ 他動詞"],
                    "nuance_notes": "動作主の意図的な働きかけに焦点を当てるときに他動詞を選択する。",
                    "example_sentences": [
                        {
                            "japanese": "ヤンさんはタクシーを<ruby>止<rt>と</rt></ruby>めた。",
                            "english": "Mr. Yang stopped a taxi."
                        },
                        {
                            "japanese": "わたしはろうそくの<ruby>火<rt>ひ</rt></ruby>を<ruby>消<rt>け</rt></ruby>した。",
                            "english": "I blew out/extinguished the candlelight."
                        },
                        {
                            "japanese": "わたしはドアを<ruby>開<rt>あ</rt></ruby>けた。",
                            "english": "I opened the door."
                        },
                        {
                            "japanese": "<ruby>先生<rt>せんせい</rt></ruby>が<ruby>子<rt>こ</rt></ruby>どもをしかった。",
                            "english": "The teacher scolded the child."
                        },
                        {
                            "japanese": "わたしはリーさんに<ruby>仕事<rt>しごと</rt></ruby>を<ruby>頼<rt>たの</rt></ruby>んだ。",
                            "english": "I asked Mr. Lee for a favor / to do some work."
                        }
                    ]
                },
                {
                    "pattern_number": 2,
                    "pattern_name": "自動詞の文（結果に注目／自然現象／働きかけのない動作）",
                    "pattern_name_en": "Intransitive sentences: focus on results / natural occurrences / non-impelling actions",
                    "meaning_ja": "動作の結果生じた状態、自然に起こる現象、または他者への働きかけがない動作を表す。",
                    "meaning_en": "Expresses resultant states, naturally occurring events, or actions without impelling effect.",
                    "connection_forms": ["N が ＋ 自動詞"],
                    "nuance_notes": "動作そのものよりも、生じた結果や自然な推移・情景に焦点を置く。",
                    "example_sentences": [
                        {
                            "japanese": "タクシーが<ruby>止<rt>と</rt></ruby>まった。",
                            "english": "The taxi stopped."
                        },
                        {
                            "japanese": "ろうそくの<ruby>火<rt>ひ</rt></ruby>が<ruby>消<rt>き</rt></ruby>えた。",
                            "english": "The candlelight went out."
                        },
                        {
                            "japanese": "ドアが<ruby>開<rt>あ</rt></ruby>いた。",
                            "english": "The door opened."
                        },
                        {
                            "japanese": "<ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>った。",
                            "english": "Snow fell."
                        },
                        {
                            "japanese": "<ruby>庭<rt>にわ</rt></ruby>にきれいなばらの<ruby>花<rt>はな</rt></ruby>が<ruby>咲<rt>さ</rt></ruby>いた。",
                            "english": "Beautiful roses bloomed in the garden."
                        },
                        {
                            "japanese": "<ruby>今夜<rt>こんや</rt></ruby>は<ruby>月<rt>つき</rt></ruby>が<ruby>明<rt>あか</rt></ruby>るく<ruby>輝<rt>かがや</rt></ruby>いている。",
                            "english": "Tonight the moon is shining brightly."
                        },
                        {
                            "japanese": "<ruby>子<rt>こ</rt></ruby>どもたちはいすに<ruby>座<rt>すわ</rt></ruby>った。",
                            "english": "The children sat on chairs."
                        },
                        {
                            "japanese": "<ruby>飛行機<rt>ひこうき</rt></ruby>が<ruby>空<rt>そら</rt></ruby>を<ruby>飛<rt>と</rt></ruby>んでいる。",
                            "english": "An airplane is flying in the sky."
                        }
                    ]
                },
                {
                    "pattern_number": 3,
                    "pattern_name": "視点を固定する手段（受身文・使役文への転換）",
                    "pattern_name_en": "Shifting to passive or causative to maintain a consistent viewpoint",
                    "meaning_ja": "対応する自動詞や他動詞がない場合、または話者の視点を変えずに文を続けるために受身文や使役文を用いる。",
                    "meaning_en": "Uses passive or causative voice to preserve speaker perspective when no intransitive/transitive counterpart exists.",
                    "connection_forms": [
                        "他動詞受身: タクシーが止められた / 子どもは先生にしかられた",
                        "自動詞使役: 先生は子どもたちをいすに座らせた"
                    ],
                    "nuance_notes": "主語や視点を統一することで文章のまとまり（結束性）を保つ手法である。",
                    "example_sentences": [
                        {
                            "japanese": "タクシーが<ruby>止<rt>と</rt></ruby>められた。",
                            "english": "The taxi was stopped (passive form focusing on the taxi)."
                        },
                        {
                            "japanese": "<ruby>子<rt>こ</rt></ruby>どもは<ruby>先生<rt>せんせい</rt></ruby>にしかられた。",
                            "english": "The child was scolded by the teacher (passive form focusing on child)."
                        },
                        {
                            "japanese": "<ruby>先生<rt>せんせい</rt></ruby>は<ruby>子<rt>こ</rt></ruby>どもたちをいすに<ruby>座<rt>すわ</rt></ruby>らせた。",
                            "english": "The teacher made the children sit on the chairs (causative form)."
                        }
                    ]
                }
            ],
            "drills": [
                {
                    "question_id": 1501,
                    "category": "Part3 3課 練習",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>読<rt>よ</rt></ruby>み<ruby>終<rt>お</rt></ruby>わった<ruby>本<rt>ほん</rt></ruby>は、<ruby>棚<rt>たな</rt></ruby>に①［　］てください。<ruby>部屋<rt>へや</rt></ruby>を<ruby>出<rt>で</rt></ruby>るときは、<ruby>電気<rt>でんき</rt></ruby>が②［　］ているかどうか<ruby>確認<rt>かくにん</rt></ruby>してください。（<ruby>戻<rt>もど</rt></ruby>る・<ruby>戻<rt>もど</rt></ruby>す、<ruby>消<rt>き</rt></ruby>える・<ruby>消<rt>け</rt></ruby>す）",
                    "correct_answer": "① 戻し　② 消え",
                    "explanation_ja": "①本を棚に戻す働きかけ（他動詞「戻す」→戻してください）。②電気が消えている状態（自動詞「消える」→消えている）。",
                    "explanation_en": "① Action impelling object back: transitive '戻す' -> 戻してください. ② State of electricity: intransitive '消える' -> 消えている."
                },
                {
                    "question_id": 1502,
                    "category": "Part3 3課 練習",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>登山靴<rt>とざんぐつ</rt></ruby>には、<ruby>丈夫<rt>じょうぶ</rt></ruby>で<ruby>簡単<rt>かんたん</rt></ruby>には①［　］ひもを<ruby>使<rt>つか</rt></ruby>っています。ひもはお<ruby>客様<rt>きゃくさま</rt></ruby>の<ruby>注文<rt>ちゅうもん</rt></ruby>に<ruby>合<rt>あ</rt></ruby>わせてちょうどいい<ruby>長<rt>なが</rt></ruby>さに②［　］こともできますので、まず、はいてみてください。（<ruby>切<rt>き</rt></ruby>れる・<ruby>切<rt>き</rt></ruby>る）",
                    "correct_answer": "① 切れない　② 切る",
                    "explanation_ja": "①ひもが自然には切れない（自動詞「切れる」否定形）。②人がひもを切る（他動詞「切る」辞書形）。",
                    "explanation_en": "① String doesn't break easily: intransitive '切れない'. ② Adjusting length by cutting: transitive '切る'."
                },
                {
                    "question_id": 1503,
                    "category": "Part3 3課 練習",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってびっくりした。<ruby>窓<rt>まど</rt></ruby>が①［　］ていた。だれかが②［　］んだと<ruby>思<rt>おも</rt></ruby>った。そうだった。わたしが、<ruby>家<rt>いえ</rt></ruby>を③［　］とき、④［　］のを<ruby>忘<rt>わす</rt></ruby>れたのだ。（<ruby>開<rt>あ</rt></ruby>く・<ruby>開<rt>あ</rt></ruby>ける、<ruby>出<rt>で</rt></ruby>る・<ruby>出<rt>だ</rt></ruby>す、<ruby>閉<rt>し</rt></ruby>まる・<ruby>閉<rt>し</rt></ruby>める）",
                    "correct_answer": "① 開き　② 開けた　③ 出る　④ 閉める",
                    "explanation_ja": "①窓が開いている状態（自動詞「開く」→開いていた）。②誰かが開けた動作（他動詞「開ける」→開けた）。③家を出るとき（自動詞「出る」）。④窓を閉めること（他動詞「閉める」）。",
                    "explanation_en": "① Window open: intransitive '開く' -> 開いていた. ② Someone opened it: transitive '開ける' -> 開けた. ③ Leaving house: intransitive '出る'. ④ Forgetting to close: transitive '閉める'."
                },
                {
                    "question_id": 1504,
                    "category": "Part3 3課 練習",
                    "question_type": "fill_in_the_blank",
                    "prompt": "わたしは1990<ruby>年<rt>ねん</rt></ruby>にある<ruby>小<rt>ちい</rt></ruby>さい<ruby>島<rt>しま</rt></ruby>で①［　］。<ruby>病院<rt>びょういん</rt></ruby>も<ruby>店<rt>みせ</rt></ruby>もなく<ruby>知<rt>し</rt></ruby>り<ruby>合<rt>あ</rt></ruby>いもいない<ruby>島<rt>しま</rt></ruby>で<ruby>子<rt>こ</rt></ruby>どもを②［　］ことができるだろうかと、<ruby>母<rt>はは</rt></ruby>はわたしを③［　］<ruby>後<rt>あと</rt></ruby>、<ruby>悩<rt>なや</rt></ruby>んだそうだ。でも、わたしは<ruby>元気<rt>げんき</rt></ruby>に④［　］て、<ruby>母<rt>はは</rt></ruby>を<ruby>安心<rt>あんしん</rt></ruby>させた。（<ruby>生<rt>う</rt></ruby>まれる・<ruby>産<rt>う</rt></ruby>む、<ruby>育<rt>そだ</rt></ruby>つ・<ruby>育<rt>そだ</rt></ruby>てる）",
                    "correct_answer": "① 生まれた　② 育てる　③ 産んだ　④ 育っ",
                    "explanation_ja": "①わたしが島で生まれた（自動詞「生まれる」過去形）。②子どもを育てる（他動詞「育てる」辞書形）。③母がわたしを産んだ後（他動詞「産む」過去形）。④元気に育って（自動詞「育つ」て形）。",
                    "explanation_en": "① I was born: intransitive '生まれた'. ② Raising a child: transitive '育てる'. ③ After mother gave birth to me: transitive '産んだ'. ④ Grew up healthily: intransitive '育つ' -> 育って."
                },
                {
                    "question_id": 1505,
                    "category": "Part3 3課 練習",
                    "question_type": "fill_in_the_blank",
                    "prompt": "<ruby>今朝<rt>けさ</rt></ruby>は<ruby>遅刻<rt>ちこく</rt></ruby>してしまった。きのう、<ruby>遅<rt>おそ</rt></ruby>くまで①［　］ていたし、<ruby>目覚<rt>めざ</rt></ruby>まし<ruby>時計<rt>どけい</rt></ruby>がいつの<ruby>間<rt>ま</rt></ruby>にか②［　］ていたのだ。<ruby>電池<rt>でんち</rt></ruby>はちゃんと③［　］ておいたはずなのに……。あしたは<ruby>試験<rt>しけん</rt></ruby>だから、<ruby>母<rt>はは</rt></ruby>に7<ruby>時<rt>じ</rt></ruby>に④［　］てほしいと<ruby>頼<rt>たの</rt></ruby>んでおこう。（<ruby>起<rt>お</rt></ruby>きる・<ruby>起<rt>お</rt></ruby>こす、<ruby>止<rt>と</rt></ruby>まる・<ruby>止<rt>と</rt></ruby>める、<ruby>入<rt>はい</rt></ruby>る・<ruby>入<rt>い</rt></ruby>れる）",
                    "correct_answer": "① 起き　② 止まっ　③ 入れ　④ 起こし",
                    "explanation_ja": "①遅くまで起きていた（自動詞「起きる」）。②目覚まし時計が止まっていた（自動詞「止まる」促音便）。③電池を入れておいた（他動詞「入れる」）。④母に起こしてほしい（他動詞「起こす」）。",
                    "explanation_en": "① Staying up late: intransitive '起きる' -> 起きていた. ② Alarm clock stopped: intransitive '止まる' -> 止まっていた. ③ Had inserted battery: transitive '入れる' -> 入れておいた. ④ Want mother to wake me up: transitive '起こす' -> 起こしてほしい."
                }
            ]
        }
    ]
