"""
Module: part3_lessons_5_to_8.py
Part 3: 文章の文法 (Grammar in Text / Passage Cloze)
Lessons 5 to 8 + Review Tests 5-6 & 7-8 (Images 130-141, p. 128-139).
"""

def get_lessons_5_to_8():
    # =========================================================================
    # Lesson 5: 5課 話者が見る位置を動かさない手段-3 受身・使役・使役受身 (p. 128-129, Images 130-131)
    # =========================================================================
    sec5 = {
        "section_number": 5,
        "title": "<ruby>第<rt>だい</rt></ruby>5<ruby>課<rt>か</rt></ruby> <ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かさない<ruby>手段<rt>しゅだん</rt></ruby>-3 <ruby>受身<rt>うけみ</rt></ruby>・<ruby>使役<rt>しえき</rt></ruby>・<ruby>使役受身<rt>しえきうけみ</rt></ruby>",
        "title_en": "Lesson 5: Keeping the Speaker's Perspective Consistent 3 - Passive, Causative, Causative-Passive",
        "theme": "<ruby>受身<rt>うけみ</rt></ruby>・<ruby>使役<rt>しえき</rt></ruby>・<ruby>使役受身<rt>しえきうけみ</rt></ruby>を<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>ければ、<ruby>話者<rt>わしゃ</rt></ruby>の<ruby>立場<rt>たちば</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>すことができます。",
        "theme_en": "The standpoints of the speaker is determined depending on whether the verb is passive, causative and causative passive.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>受身<rt>うけみ</rt></ruby>・<ruby>使役<rt>しえき</rt></ruby>・<ruby>使役受身<rt>しえきうけみ</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>け",
                "title_en": "Differentiating between Passive, Causative, and Causative-Passive",
                "categories": [
                    {
                        "form": "<ruby>受身<rt>うけみ</rt></ruby>",
                        "form_en": "Passive",
                        "concept": "「ほかの<ruby>人<rt>ひと</rt></ruby>の<ruby>行為<rt>こうい</rt></ruby>」や「できごとの<ruby>影響<rt>えいきょう</rt></ruby>」を<ruby>受<rt>う</rt></ruby>ける",
                        "subtypes": [
                            {
                                "subject": "<ruby>人<rt>ひと</rt></ruby>（<ruby>話者<rt>わしゃ</rt></ruby>または<ruby>心理的<rt>しんりてき</rt></ruby>に<ruby>話者<rt>わしゃ</rt></ruby>に<ruby>近<rt>ちか</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>）が<ruby>主語<rt>しゅご</rt></ruby>",
                                "examples": [
                                    "うちの<ruby>子<rt>こ</rt></ruby>は<ruby>先生<rt>せんせい</rt></ruby>にしかられた。",
                                    "わたしはだれかに<ruby>肩<rt>かた</rt></ruby>をたたかれた。",
                                    "<ruby>最後<rt>さいご</rt></ruby>に<ruby>点<rt>てん</rt></ruby>を<ruby>取<rt>と</rt></ruby>られて<ruby>負<rt>ま</rt></ruby>けてしまった。",
                                    "<ruby>突然<rt>とつぜん</rt></ruby><ruby>雨<rt>あめ</rt></ruby>に<ruby>降<rt>ふ</rt></ruby>られてぬれてしまった。"
                                ]
                            },
                            {
                                "subject": "<ruby>物<rt>もの</rt></ruby>が<ruby>主語<rt>しゅご</rt></ruby>",
                                "examples": [
                                    "ワインはぶどうから<ruby>作<rt>つく</rt></ruby>られる。",
                                    "この<ruby>工場<rt>こうじょう</rt></ruby>では<ruby>年間<rt>ねんかん</rt></ruby>25<ruby>万台<rt>まんだい</rt></ruby>の<ruby>車<rt>くるま</rt></ruby>が<ruby>生産<rt>せいさん</rt></ruby>されている。"
                                ]
                            }
                        ]
                    },
                    {
                        "form": "<ruby>使役<rt>しえき</rt></ruby>",
                        "form_en": "Causative",
                        "concept": "ほかの<ruby>人<rt>ひと</rt></ruby>の<ruby>行為<rt>こうい</rt></ruby>や<ruby>感情<rt>かんじょう</rt></ruby>を<ruby>促<rt>うなが</rt></ruby>す",
                        "subtypes": [
                            {
                                "type": "<ruby>行為<rt>こうい</rt></ruby>を<ruby>強制<rt>きょうせい</rt></ruby>する",
                                "examples": [
                                    "わたしは<ruby>犬<rt>いぬ</rt></ruby>にボールを<ruby>取<rt>と</rt></ruby>りに<ruby>行<rt>い</rt></ruby>かせた。",
                                    "<ruby>親<rt>おや</rt></ruby>は<ruby>子<rt>こ</rt></ruby>どもたちに<ruby>家事<rt>かじ</rt></ruby>を<ruby>手伝<rt>てつだ</rt></ruby>わせた。",
                                    "<ruby>田村<rt>たむら</rt></ruby>さんはいつもみんなを<ruby>待<rt>ま</rt></ruby>たせる。"
                                ]
                            },
                            {
                                "type": "<ruby>行為<rt>こうい</rt></ruby>を<ruby>許<rt>ゆる</rt></ruby>す",
                                "examples": [
                                    "<ruby>母<rt>はは</rt></ruby>は<ruby>疲<rt>つか</rt></ruby>れている。あしたは<ruby>一日<rt>いちにち</rt></ruby><ruby>休<rt>やす</rt></ruby>ませてあげよう。",
                                    "<ruby>監督<rt>かんとく</rt></ruby>はぼくたちにジュースを<ruby>飲<rt>の</rt></ruby>ませてくれた。",
                                    "わたしにも<ruby>意見<rt>いけん</rt></ruby>を<ruby>言<rt>い</rt></ruby>わせてもらいたいです。"
                                ]
                            },
                            {
                                "type": "<ruby>感情<rt>かんじょう</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>だ</rt></ruby>す",
                                "examples": [
                                    "<ruby>弟<rt>おとうと</rt></ruby>はよく<ruby>母<rt>はは</rt></ruby>を<ruby>怒<rt>おこ</rt></ruby>らせる。",
                                    "ヤンさんはいつもみんなを<ruby>笑<rt>わら</rt></ruby>わせている。"
                                ]
                            }
                        ]
                    },
                    {
                        "form": "<ruby>使役受身<rt>しえきうけみ</rt></ruby>",
                        "form_en": "Causative-Passive",
                        "concept": "<ruby>促<rt>うなが</rt></ruby>す<ruby>行為<rt>こうい</rt></ruby>を<ruby>受<rt>う</rt></ruby>ける、<ruby>感情<rt>かんじょう</rt></ruby>に<ruby>影響<rt>えいきょう</rt></ruby>を<ruby>受<rt>う</rt></ruby>ける",
                        "subtypes": [
                            {
                                "type": "<ruby>行為<rt>こうい</rt></ruby>の<ruby>強制<rt>きょうせい</rt></ruby>を<ruby>受<rt>う</rt></ruby>ける",
                                "examples": [
                                    "わたしは<ruby>監督<rt>かんとく</rt></ruby>にボールを<ruby>取<rt>と</rt></ruby>りに<ruby>行<rt>い</rt></ruby>かされた。",
                                    "わたしは<ruby>親<rt>おや</rt></ruby>に<ruby>家事<rt>かじ</rt></ruby>を<ruby>手伝<rt>てつだ</rt></ruby>わされた。",
                                    "<ruby>田村<rt>たむら</rt></ruby>さんにはいつも<ruby>待<rt>ま</rt></ruby>たされる。"
                                ]
                            },
                            {
                                "type": "<ruby>感情<rt>かんじょう</rt></ruby>に<ruby>影響<rt>えいきょう</rt></ruby>を<ruby>受<rt>う</rt></ruby>ける",
                                "examples": [
                                    "わたしは<ruby>弟<rt>おとうと</rt></ruby>によく<ruby>泣<rt>な</rt></ruby>かされる。",
                                    "その<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで<ruby>深<rt>ふか</rt></ruby>く<ruby>考<rt>かんが</rt></ruby>えさせられた。"
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30501,
                "category": "第3部 5課 練習",
                "question_type": "fill_conjugation",
                "prompt": "1 <ruby>父<rt>ちち</rt></ruby>の<ruby>店<rt>みせ</rt></ruby>がテレビで（①<ruby>紹介<rt>しょうかい</rt></ruby>する→＿＿＿）たので、<ruby>急<rt>きゅう</rt></ruby>に<ruby>客<rt>きゃく</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えた。そのため、<ruby>父<rt>ちち</rt></ruby>は<ruby>兄<rt>あに</rt></ruby>や<ruby>姉<rt>あね</rt></ruby>にも<ruby>店<rt>みせ</rt></ruby>を（②<ruby>手伝<rt>てつだ</rt></ruby>う→＿＿＿）ている。しかし、わたしには（③<ruby>手伝<rt>てつだ</rt></ruby>う→＿＿＿）つもりはないらしい。",
                "correct_answers": ["① 紹介され", "② 手伝わせ", "③ 手伝わせる"],
                "explanation_ja": "①店がテレビで紹介された（受身）。②兄や姉に手伝わせている（使役）。③わたしには手伝わせるつもりはない（使役）。",
                "explanation_en": "①'紹介され' (passive). ②'手伝わせ' (causative). ③'手伝わせる' (causative)."
            },
            {
                "question_id": 30502,
                "category": "第3部 5課 練習",
                "question_type": "fill_conjugation",
                "prompt": "2 サッカー<ruby>部<rt>ぶ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ったが、なかなかボールに（①<ruby>触<rt>さわ</rt></ruby>る→＿＿＿）てもらえず、<ruby>先輩<rt>せんぱい</rt></ruby>に（②<ruby>走<rt>はし</rt></ruby>る→＿＿＿）てばかりいる。つまらないのでゆっくり<ruby>走<rt>はし</rt></ruby>ると、すぐに<ruby>大<rt>おお</rt></ruby>きな<ruby>声<rt>こえ</rt></ruby>で（③<ruby>注意<rt>ちゅうい</rt></ruby>する→＿＿＿）て、<ruby>練習<rt>れんしゅう</rt></ruby>の<ruby>後<rt>あと</rt></ruby>も<ruby>部屋<rt>へや</rt></ruby>の<ruby>掃除<rt>そうじ</rt></ruby>を（④する→＿＿＿）。もう<ruby>辞<rt>や</rt></ruby>めようかと<ruby>思<rt>おも</rt></ruby>った。でも、<ruby>先日<rt>せんじつ</rt></ruby><ruby>試合<rt>しあい</rt></ruby>に（⑤<ruby>出場<rt>しゅつじょう</rt></ruby>する→＿＿＿）てもらって、<ruby>先輩<rt>せんぱい</rt></ruby>によくがんばったと（⑥ほめる→＿＿＿）たので、もう<ruby>少<rt>すこ</rt></ruby>し<ruby>続<rt>つづ</rt></ruby>けてみようと<ruby>思<rt>おも</rt></ruby>う。",
                "correct_answers": ["① 触らせ", "② 走らされ", "③ 注意され", "④ させられる", "⑤ 出場させ", "⑥ ほめられ"],
                "explanation_ja": "①触らせてもらえず（使役て形＋もらう）。②走らされて（使役受身）。③注意されて（受身）。④させられる（使役受身）。⑤出場させてもらって（使役て形＋もらう）。⑥ほめられた（受身）。",
                "explanation_en": "①'触らせ' (causative). ②'走らされ' (causative-passive). ③'注意され' (passive). ④'させられる' (causative-passive). ⑤'出場させ' (causative). ⑥'ほめられ' (passive)."
            },
            {
                "question_id": 30503,
                "category": "第3部 5課 練習",
                "question_type": "fill_conjugation",
                "prompt": "3 <ruby>急<rt>きゅう</rt></ruby>に<ruby>昔<rt>むかし</rt></ruby>の<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>いたくなったので、メールを（①<ruby>送<rt>おく</rt></ruby>る→＿＿＿）た。じょうだんを<ruby>言<rt>い</rt></ruby>ってよくわたしたちを（②<ruby>笑<rt>わら</rt></ruby>う→＿＿＿）ていた<ruby>人<rt>ひと</rt></ruby>だ。<ruby>会<rt>あ</rt></ruby>って<ruby>話<rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>くと<ruby>今<rt>いま</rt></ruby>は3<ruby>人<rt>にん</rt></ruby>の<ruby>子<rt>こ</rt></ruby>どもを（③<ruby>育<rt>そだ</rt></ruby>てる→＿＿＿）ているそうだが、<ruby>明<rt>あか</rt></ruby>るさは<ruby>昔<rt>むかし</rt></ruby>と<ruby>変<rt>か</rt></ruby>わっていない。あまりきびしいことを（④<ruby>言<rt>い</rt></ruby>う→＿＿＿）ないで、<ruby>子<rt>こ</rt></ruby>どもたちを<ruby>自由<rt>じゆう</rt></ruby>に（⑤<ruby>遊<rt>あそ</rt></ruby>ぶ→＿＿＿）ているのだそうだ。<ruby>彼女<rt>かのじょ</rt></ruby>らしい（⑥<ruby>育<rt>そだ</rt></ruby>てる→＿＿＿）<ruby>方<rt>かた</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>った。",
                "correct_answers": ["① 送っ", "② 笑わせ", "③ 育て", "④ 言わ", "⑤ 遊ばせ", "⑥ 育て"],
                "explanation_ja": "①送った（能動過去）。②笑わせていた（使役）。③育てている（能動）。④言わないで（否定）。⑤遊ばせている（使役）。⑥育て方（連用形＋方）。",
                "explanation_en": "①'送っ' (active). ②'笑わせ' (causative). ③'育て' (active). ④'言わ' (negative). ⑤'遊ばせ' (causative). ⑥'育て' (masu-stem)."
            },
            {
                "question_id": 30504,
                "category": "第3部 5課 練習",
                "question_type": "fill_conjugation",
                "prompt": "4 <ruby>病院<rt>びょういん</rt></ruby>や<ruby>銀行<rt>ぎんこう</rt></ruby>などでは、<ruby>順番<rt>じゅんばん</rt></ruby>を<ruby>待<rt>ま</rt></ruby>つ<ruby>人<rt>ひと</rt></ruby>に<ruby>待<rt>ま</rt></ruby>ち<ruby>時間<rt>じかん</rt></ruby>を<ruby>長<rt>なが</rt></ruby>く（①<ruby>感<rt>かん</rt></ruby>じる→＿＿＿）ないように、いろいろな<ruby>工夫<rt>くふう</rt></ruby>を（②する→＿＿＿）ている。<ruby>待合室<rt>まちあいしつ</rt></ruby>などに（③<ruby>置<rt>お</rt></ruby>く→＿＿＿）てあるテレビや<ruby>雑誌<rt>ざっし</rt></ruby>もその<ruby>一<rt>ひと</rt></ruby>つだ。<ruby>絵本<rt>えほん</rt></ruby>やおもちゃも、<ruby>親<rt>おや</rt></ruby>に<ruby>連<rt>つ</rt></ruby>れて（④くる→＿＿＿）た<ruby>子<rt>こ</rt></ruby>どもを（⑤あきる→＿＿＿）ないためのものだ。しかし、いちばんいいのは、<ruby>病院<rt>びょういん</rt></ruby>や<ruby>銀行<rt>ぎんこう</rt></ruby>が<ruby>人<rt>ひと</rt></ruby>を（⑥<ruby>待<rt>ま</rt></ruby>つ→＿＿＿）ないことだろう。",
                "correct_answers": ["① 感じさせ", "② し", "③ 置い", "④ こられ", "⑤ あきさせ", "⑥ 待たせ"],
                "explanation_ja": "①感じさせないように（使役）。②している（能動）。③置いてある（他動詞て形＋ある）。④連れてこられた（受身）。⑤あきさせない（使役）。⑥待たせない（使役）。",
                "explanation_en": "①'感じさせ' (causative). ②'し' (active). ③'置い' (transitive + aru). ④'こられ' (passive). ⑤'あきさせ' (causative). ⑥'待たせ' (causative)."
            }
        ]
    }

    # =========================================================================
    # Lesson 6: 6課 話者が見る位置を動かさない手段-4 〜てあげる・〜てもらう・〜てくれる (p. 130-131, Images 132-133)
    # =========================================================================
    sec6 = {
        "section_number": 6,
        "title": "<ruby>第<rt>だい</rt></ruby>6<ruby>課<rt>か</rt></ruby> <ruby>話者<rt>わしゃ</rt></ruby>が<ruby>見<rt>み</rt></ruby>る<ruby>位置<rt>いち</rt></ruby>を<ruby>動<rt>うご</rt></ruby>かさない<ruby>手段<rt>しゅだん</rt></ruby>-4 〜てあげる・〜てもらう・〜てくれる",
        "title_en": "Lesson 6: Keeping the Speaker's Perspective Consistent 4 - '~te ageru', '~te morau', '~te kureru'",
        "theme": "<ruby>比<rt>くら</rt></ruby>べて<ruby>考<rt>かんが</rt></ruby>えたとき、<ruby>心理的<rt>しんりてき</rt></ruby>に<ruby>話者<rt>わしゃ</rt></ruby>に<ruby>近<rt>ちか</rt></ruby>い<ruby>方<rt>ほう</rt></ruby>の<ruby>立場<rt>たちば</rt></ruby>に<ruby>立<rt>た</rt></ruby>って<ruby>文<rt>ぶん</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ります。",
        "theme_en": "These forms express relative closeness of relationship. The speaker can choose a standpoint that identifies with a person to whom he is emotionally or personally close.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>心理的<rt>しんりてき</rt></ruby>に<ruby>話者<rt>わしゃ</rt></ruby>に<ruby>近<rt>ちか</rt></ruby>い<ruby>方<rt>ほう</rt></ruby>の<ruby>立場<rt>たちば</rt></ruby>に<ruby>立<rt>た</rt></ruby>つ",
                "rules": [
                    "●は○に〜てあげる: ●→○ (●: 話者／話者に近い人, ○: 話者から遠い人)",
                    "●は○に〜てもらう: ●←○",
                    "○は●に〜てくれる: ○→●",
                    "× 山川さんはわたしの母に服を作ってあげました。（山川さんより母の方が近い）",
                    "○ わたしの母は山川さんに服を作ってもらいました。"
                ]
            },
            {
                "point_number": 2,
                "title": "いやな<ruby>気持<rt>きも</rt></ruby>ちを<ruby>表<rt>あらわ</rt></ruby>すときは、<ruby>話者<rt>わしゃ</rt></ruby>を<ruby>主語<rt>しゅご</rt></ruby>にして<ruby>受身文<rt>うけみぶん</rt></ruby>で<ruby>言<rt>い</rt></ruby>います。",
                "reference": "第3部 5課",
                "examples": [
                    "例・どろぼうに荷物を持っていかれた。（いやな気持ち）",
                    "・（わたしは）カンさんに荷物を外に持っていってもらった。（うれしい気持ち）",
                    "・カンさんが荷物を外に持っていってくれた。（うれしい気持ち）"
                ]
            },
            {
                "point_number": 3,
                "title": "「〜てもらう」の<ruby>文<rt>ぶん</rt></ruby>は、いつも「〈<ruby>人<rt>ひと</rt></ruby>〉に（〜を）〜てもらう」という<ruby>形<rt>かたち</rt></ruby>になります。「〜てあげる・〜てくれる」の<ruby>文<rt>ぶん</rt></ruby>では、<ruby>動詞<rt>どうし</rt></ruby>に<ruby>合<rt>あ</rt></ruby>った<ruby>助詞<rt>じょし</rt></ruby>を<ruby>使<rt>つか</rt></ruby>います。",
                "particle_patterns": [
                    {
                        "structure": "〈人〉を 誘う、起こす、泊める、招待する",
                        "examples": [
                            "わたしは友だちを部屋に泊めてあげた。",
                            "山口さんはわたしをパーティーに招待してくれた。"
                        ]
                    },
                    {
                        "structure": "〈人〉に〜を（注1） 貸す、教える、見せる、紹介する",
                        "note": "注1: 必ず「〈人〉に〜を」を使う動詞",
                        "examples": [
                            "母はおじにお金を貸してあげたようだ。",
                            "ヤンさんはわたしに中国語を教えてくれる。"
                        ]
                    },
                    {
                        "structure": "〈人〉に〜を（注2） 作る、買う、歌う、読む",
                        "note": "注2: 本来は「〜を」を使う動詞だが、ある人のためにその行為をするときだけ「〈人〉に〜を」を使う動詞",
                        "examples": [
                            "わたしは毎晩子どもたちに本を読んでやっている。",
                            "山川さんはわたしに指輪を買ってくれた。"
                        ]
                    },
                    {
                        "structure": "〈人〉の〜を 持つ、運ぶ、直す、手伝う",
                        "examples": [
                            "姉は高橋さんの仕事を手伝ってあげたそうだ。",
                            "ヤンさんがわたしのパソコンを直してくれた。"
                        ]
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30601,
                "category": "第3部 6課 練習",
                "question_type": "three_choice_cloze",
                "prompt": "1 きのうかぜで<ruby>一日中<rt>いちにちじゅう</rt></ruby><ruby>寝<rt>ね</rt></ruby>ていた。<ruby>同<rt>おな</rt></ruby>じアパートのカンさんが、<ruby>晩<rt>ばん</rt></ruby>ご<ruby>飯<rt>はん</rt></ruby>を<ruby>作<rt>つく</rt></ruby>って（① a あげた　b もらった　c くれた）。カンさんは<ruby>料理<rt>りょうり</rt></ruby>が<ruby>上手<rt>じょうず</rt></ruby>で、ときどき<ruby>大家<rt>おおや</rt></ruby>さんにも<ruby>国<rt>くに</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>を<ruby>作<rt>つく</rt></ruby>って（② a あげている　b もらっている　c くれている）。「ぼくは<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>仕事<rt>しごと</rt></ruby>がある<ruby>日<rt>ひ</rt></ruby>は、<ruby>大家<rt>おおや</rt></ruby>さんに<ruby>頼<rt>たの</rt></ruby>んで（③ a <ruby>起<rt>お</rt></ruby>こしてあげて　b <ruby>起<rt>お</rt></ruby>こしてもらって　c <ruby>起<rt>お</rt></ruby>こしてくれて）いるので、そのお<ruby>礼<rt>れい</rt></ruby>なんです。」とカンさんは<ruby>言<rt>い</rt></ruby>う。",
                "correct_answers": ["① c", "② a", "③ b"],
                "explanation_ja": "①カンさんがわたしに「作ってくれた」（c）。②カンさんが大家さんに「作ってあげている」（a）。③大家さんに頼んで「起こしてもらっている」（b）。",
                "explanation_en": "①'作ってくれた' (c). ②'作ってあげている' (a). ③'起こしてもらって' (b)."
            },
            {
                "question_id": 30602,
                "category": "第3部 6課 練習",
                "question_type": "three_choice_cloze",
                "prompt": "2 となりの<ruby>鈴木<rt>すずき</rt></ruby>さんは<ruby>親切<rt>しんせつ</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>だ。わたしは<ruby>前<rt>まえ</rt></ruby>に<ruby>鈴木<rt>すずき</rt></ruby>さんにこわれた<ruby>自転車<rt>じてんしゃ</rt></ruby>を（① a <ruby>直<rt>なお</rt></ruby>してあげた　b <ruby>直<rt>なお</rt></ruby>してもらった　c <ruby>直<rt>なお</rt></ruby>してくれた）ことがある。その<ruby>自転車<rt>じてんしゃ</rt></ruby>は、<ruby>学校<rt>がっこう</rt></ruby>の（② a <ruby>先輩<rt>せんぱい</rt></ruby>にゆずってあげた　b <ruby>先輩<rt>せんぱい</rt></ruby>にゆずってもらった　c <ruby>先輩<rt>せんぱい</rt></ruby>がゆずってあげた）<ruby>物<rt>もの</rt></ruby>だ。<ruby>鈴木<rt>すずき</rt></ruby>さんがこわれていたベルを（③ a <ruby>取<rt>と</rt></ruby>り<ruby>替<rt>か</rt></ruby>えてあげた　b <ruby>取<rt>と</rt></ruby>り<ruby>替<rt>か</rt></ruby>えてもらった　c <ruby>取<rt>と</rt></ruby>り<ruby>替<rt>か</rt></ruby>えてくれた）ので、ずっと<ruby>使<rt>つか</rt></ruby>っていたのだが、この<ruby>間<rt>あいだ</rt></ruby>、だれかにそのベルを（④ a <ruby>盗<rt>ぬす</rt></ruby>んでもらって　b <ruby>盗<rt>ぬす</rt></ruby>ませて　c <ruby>盗<rt>ぬす</rt></ruby>まれて）しまった。",
                "correct_answers": ["① b", "② b", "③ c", "④ c"],
                "explanation_ja": "①わたしは鈴木さんに「直してもらった」（b）。②学校の先輩に「ゆずってもらった」（b）。③鈴木さんが「取り替えてくれた」（c）。④だれかにベルを「盗まれて」（c、被害受身）。",
                "explanation_en": "①'直してもらった' (b). ②'ゆずってもらった' (b). ③'取り替えてくれた' (c). ④'盗まれて' (c, suffering passive)."
            },
            {
                "question_id": 30603,
                "category": "第3部 6課 練習",
                "question_type": "three_choice_cloze",
                "prompt": "3 ある<ruby>日<rt>ひ</rt></ruby>、<ruby>宿題<rt>しゅくだい</rt></ruby>で<ruby>書<rt>か</rt></ruby>いた<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>作文<rt>さくぶん</rt></ruby>をだれかに（① a <ruby>見<rt>み</rt></ruby>てあげたい　b <ruby>見<rt>み</rt></ruby>てもらいたい　c <ruby>見<rt>み</rt></ruby>せてもらいたい）と<ruby>思<rt>おも</rt></ruby>ったので、アルバイトをしている<ruby>店<rt>みせ</rt></ruby>の<ruby>店長<rt>てんちょう</rt></ruby>に<ruby>頼<rt>たの</rt></ruby>んでみた。すると、<ruby>高校生<rt>こうこうせい</rt></ruby>の<ruby>娘<rt>むすめ</rt></ruby>さんを（② a <ruby>紹介<rt>しょうかい</rt></ruby>してあげた　b <ruby>紹介<rt>しょうかい</rt></ruby>してもらった　c <ruby>紹介<rt>しょうかい</rt></ruby>してくれた）。<ruby>娘<rt>むすめ</rt></ruby>さんは<ruby>英語<rt>えいご</rt></ruby>が<ruby>苦<rt>にが</rt></ruby><ruby>手<rt>て</rt></ruby>らしいので、わたしはときどき<ruby>日本語<rt>にほんご</rt></ruby>を（③ a <ruby>教<rt>おし</rt></ruby>えてあげる　b <ruby>教<rt>おし</rt></ruby>えてもらう　c <ruby>教<rt>おし</rt></ruby>えてくれる）かわりに、<ruby>英語<rt>えいご</rt></ruby>を（④ a <ruby>教<rt>おし</rt></ruby>えてあげる　b <ruby>教<rt>おし</rt></ruby>えてもらう　c <ruby>教<rt>おし</rt></ruby>えてくれる）ことにした。",
                "correct_answers": ["① b", "② c", "③ b", "④ a"],
                "explanation_ja": "①だれかに作文を「見てもらいたい」（b）。②店長が娘さんを「紹介してくれた」（c）。③わたしが日本語を「教えてもらう」（b）かわりに、英語を「教えてあげる」（a）。",
                "explanation_en": "①'見てもらいたい' (b). ②'紹介してくれた' (c). ③'教えてもらう' (b). ④'教えてあげる' (a)."
            }
        ]
    }

    # =========================================================================
    # Review Test 5-6: まとめ問題 (5課・6課) (p. 132-133, Images 134-135)
    # =========================================================================
    matome_5_6 = {
        "section_number": 6.5,
        "title": "まとめ<ruby>問題<rt>もんだい</rt></ruby>（5<ruby>課<rt>か</rt></ruby>・6<ruby>課<rt>か</rt></ruby>）",
        "title_en": "Review Exercises (Lessons 5 & 6)",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>総合練習<rt>そうごうれんしゅう</rt></ruby>（<ruby>受身<rt>うけみ</rt></ruby>・<ruby>使役<rt>しえき</rt></ruby>・やりもらい）",
        "theme_en": "Comprehensive text grammar review: Passive, causative, and benefactive expressions",
        "passages": [
            {
                "passage_id": 305,
                "title": "自転車と歩行者",
                "title_en": "Bicycles and Pedestrians",
                "text": "<ruby>先日<rt>せんじつ</rt></ruby>、<ruby>後<rt>うし</rt></ruby>ろから<ruby>来<rt>き</rt></ruby>た<ruby>自転車<rt>じてんしゃ</rt></ruby>に［ 1 ］しまいました。わたしは<ruby>歩道<rt>ほどう</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>いていたのですから、<ruby>悪<rt>わる</rt></ruby>いのはもちろん<ruby>自転車<rt>じてんしゃ</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>です。\n<ruby>次<rt>つぎ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>、その<ruby>歩道<rt>ほどう</rt></ruby>で<ruby>今度<rt>こんど</rt></ruby>はわたしが<ruby>自転車<rt>じてんしゃ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>っていたときのことです。<ruby>小<rt>ちい</rt></ruby>さい<ruby>子<rt>こ</rt></ruby>どもを<ruby>連<rt>つ</rt></ruby>れたお<ruby>母<rt>かあ</rt></ruby>さんが<ruby>前<rt>まえ</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>いていたので、ベルを［ 2 ］。すると、そのお<ruby>母<rt>かあ</rt></ruby>さんは「<ruby>自転車<rt>じてんしゃ</rt></ruby>で<ruby>歩道<rt>ほどう</rt></ruby>を<ruby>走<rt>はし</rt></ruby>らないで。」と<ruby>言<rt>い</rt></ruby>いました。［ 3 ］<ruby>困<rt>こま</rt></ruby>ると<ruby>言<rt>い</rt></ruby>いたそうな<ruby>顔<rt>かお</rt></ruby>で、<ruby>彼女<rt>かのじょ</rt></ruby>はわたしをにらみました。\n<ruby>道路交通法<rt>どうろこうつうほう</rt></ruby>という<ruby>法律<rt>ほうりつ</rt></ruby>がありますが、2008<ruby>年<rt>ねん</rt></ruby>に<ruby>改正<rt>かいせい</rt></ruby>されて、<ruby>歩道<rt>ほどう</rt></ruby>の<ruby>安全<rt>あんぜん</rt></ruby>のために<ruby>自転車<rt>じてんしゃ</rt></ruby>は<ruby>基本的<rt>きほんてき</rt></ruby>に<ruby>車道<rt>しゃどう</rt></ruby>を<ruby>走<rt>はし</rt></ruby>ることになりました。けれども、<ruby>車<rt>くるま</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い<ruby>場合<rt>ばあい</rt></ruby>、<ruby>自転車<rt>じてんしゃ</rt></ruby>で<ruby>車道<rt>しゃどう</rt></ruby>を<ruby>走<rt>はし</rt></ruby>ったら、［ 4 ］<ruby>迷惑<rt>めいわく</rt></ruby>でしょう。この<ruby>法律<rt>ほうりつ</rt></ruby>には<ruby>自転車<rt>じてんしゃ</rt></ruby>に<ruby>乗<rt>の</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>の<ruby>年齢<rt>ねんれい</rt></ruby>などいろいろ<ruby>条件<rt>じょうけん</rt></ruby>があるようですが、わたしは<ruby>自転車<rt>じてんしゃ</rt></ruby>で<ruby>危険<rt>きけん</rt></ruby>な<ruby>車道<rt>しゃどう</rt></ruby>を［ 5 ］いやです。でも、<ruby>歩<rt>ある</rt></ruby>く<ruby>人<rt>ひと</rt></ruby>の<ruby>立場<rt>たちば</rt></ruby>になって<ruby>考<rt>かんが</rt></ruby>えると、<ruby>歩道<rt>ほどう</rt></ruby>を<ruby>走<rt>はし</rt></ruby>る<ruby>自転車<rt>じてんしゃ</rt></ruby>は<ruby>迷惑<rt>めいわく</rt></ruby>です。<ruby>自転車<rt>じてんしゃ</rt></ruby>のための<ruby>道<rt>みち</rt></ruby>がもっと<ruby>増<rt>ふ</rt></ruby>えればいいのに、と<ruby>思<rt>おも</rt></ruby>います。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30501,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　ぶつけて",
                            "2　ぶつけられて",
                            "3　ぶつけさせて",
                            "4　ぶつけさせられて"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "自転車にぶつかられた被害受身。「ぶつけられてしまいました」。2が正解。",
                        "explanation_en": "Suffering passive: 'ぶつけられて' (was bumped into by a bicycle). Choice 2 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30502,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　鳴らしました",
                            "2　鳴らされました",
                            "3　鳴らしてもらいました",
                            "4　鳴らしてくれました"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "自転車に乗っていた話者自身の能動動作なので「鳴らしました」。1が正解。",
                        "explanation_en": "Active action of the speaker riding the bike: '鳴らしました'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30503,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　注意させられないと",
                            "2　注意させないと",
                            "3　注意してあげないと",
                            "4　注意してくれないと"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "母親の立場での発言「（わたしに）注意してくれないと困る」。4が正解。",
                        "explanation_en": "'注意してくれないと困る' reflects the mother's sentiment toward the speaker. Choice 4 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30504,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　車の人には",
                            "2　歩く人には",
                            "3　自転車の人には",
                            "4　子どもやお年寄りには"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "車道に自転車が入ると自動車の運転手にとって迷惑となるので「車の人には迷惑でしょう」。1が正解。",
                        "explanation_en": "Bikes in the car lane cause nuisance for motorists: '車の人には'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30505,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　走れるのは",
                            "2　走らされるのは",
                            "3　走ってあげるのは",
                            "4　走ってもらうのは"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "危険な車道を走るよう強制される使役受身「走らされるのはいやです」。2が正解。",
                        "explanation_en": "Causative-passive indicating being forced to ride on dangerous car roads: '走らされるのは'. Choice 2 is correct."
                    }
                ]
            },
            {
                "passage_id": 306,
                "title": "税金についての意識",
                "title_en": "Awareness of Taxes",
                "text": "わたしたちはどんなときに「<ruby>税金<rt>ぜいきん</rt></ruby>」のことを<ruby>考<rt>かんが</rt></ruby>えるでしょうか。スーパーで<ruby>肉<rt>にく</rt></ruby>や<ruby>野菜<rt>やさい</rt></ruby>を<ruby>買<rt>か</rt></ruby>うときなどは、<ruby>税金<rt>ぜいきん</rt></ruby>（<ruby>消費税<rt>しょうひぜい</rt></ruby>）を<ruby>払<rt>はら</rt></ruby>っているという<ruby>意識<rt>いしき</rt></ruby>はあまり<ruby>高<rt>たか</rt></ruby>くないかもしれません。たばこ<ruby>税<rt>ぜい</rt></ruby>や<ruby>酒税<rt>しゅぜい</rt></ruby>についても、<ruby>値段<rt>ねだん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>に<ruby>初<rt>はじ</rt></ruby>めから<ruby>入<rt>はい</rt></ruby>っているため、<ruby>税金<rt>ぜいきん</rt></ruby>を［ 1 ］という<ruby>意識<rt>いしき</rt></ruby>は<ruby>薄<rt>うす</rt></ruby>いでしょう。\nしかし、<ruby>例<rt>たと</rt></ruby>えば<ruby>何<rt>なに</rt></ruby>かの<ruby>修理<rt>しゅうり</rt></ruby>を<ruby>頼<rt>たの</rt></ruby>むときなどは<ruby>意識<rt>いしき</rt></ruby>が<ruby>強<rt>つよ</rt></ruby>くなるでしょう。<ruby>修理代<rt>しゅうりだい</rt></ruby>のほかに、［ 2 ］ことがわかります。もし<ruby>税金<rt>ぜいきん</rt></ruby>が<ruby>加<rt>くわ</rt></ruby>わらなければもっと<ruby>安<rt>やす</rt></ruby>いりになあ、と<ruby>残念<rt>ざんねん</rt></ruby>な<ruby>気<rt>き</rt></ruby>がします。また、<ruby>会社<rt>かいしゃ</rt></ruby>から<ruby>給料<rt>きゅうりょう</rt></ruby>を［ 3 ］ときも<ruby>同<rt>おな</rt></ruby>じような<ruby>気持<rt>きも</rt></ruby>ちになります。<ruby>全体<rt>ぜんたい</rt></ruby>の<ruby>給料<rt>きゅうりょう</rt></ruby>から<ruby>税金<rt>ぜいきん</rt></ruby>が［ 4 ］、<ruby>実際<rt>じっさい</rt></ruby>に<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>れる<ruby>金額<rt>きんがく</rt></ruby>が<ruby>少<rt>すく</rt></ruby>なくなるからです。\nこのように、わたしたちは<ruby>意識<rt>いしき</rt></ruby>してもしなくても、さまざまな<ruby>場面<rt>ばめん</rt></ruby>で<ruby>税金<rt>ぜいきん</rt></ruby>を<ruby>払<rt>はら</rt></ruby>っています。<ruby>政府<rt>せいふ</rt></ruby>には、わたしたちから<ruby>取<rt>と</rt></ruby>る<ruby>税金<rt>ぜいきん</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>をもっとしっかり［ 5 ］。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30601,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　払わせている",
                            "2　払わされている",
                            "3　払ってもらえる",
                            "4　払ってくれる"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "税金を強制的に支払わされているという使役受身「払わされている」。2が正解。",
                        "explanation_en": "Causative-passive expressing being made to pay: '払わされている'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30602,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　税金が取られる",
                            "2　税金を取らせる",
                            "3　税金を払ってあげる",
                            "4　税金を払ってもらう"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "修理代のほかに税金が徴収される被害受身「税金が取られる」。1が正解。",
                        "explanation_en": "Passive form: '税金が取られる' (tax is taken). Choice 1 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30603,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　払った",
                            "2　あげた",
                            "3　くれた",
                            "4　もらった"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "会社から給料を「もらった」とき（受け取る動作）。4が正解。",
                        "explanation_en": "Receiving salary from the company: '給料をもらったとき'. Choice 4 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30604,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　引かれるので",
                            "2　引かれても",
                            "3　引かせるのに",
                            "4　引かせても"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "給料から税金が差し引かれる理由を述べる受身「引かれるので」。1が正解。",
                        "explanation_en": "Causal passive reason: '引かれるので' (because it is deducted). Choice 1 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30605,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　考えられます",
                            "2　考えてあげたいです",
                            "3　考えてもらいたいです",
                            "4　考えてくれます"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "政府に対して望むことなので「〜てもらいたい」。「考えてもらいたいです」。3が正解。",
                        "explanation_en": "Expressing a request/desire toward the government: '考えてもらいたいです'. Choice 3 is correct."
                    }
                ]
            }
        ]
    }

    # =========================================================================
    # Lesson 7: 7課 こ・そ・あ (p. 134-135, Images 136-137)
    # =========================================================================
    sec7 = {
        "section_number": 7,
        "title": "<ruby>第<rt>だい</rt></ruby>7<ruby>課<rt>か</rt></ruby> こ・そ・あ",
        "title_en": "Lesson 7: Demonstratives (Ko, So, A)",
        "theme": "まとまりのある<ruby>文章<rt>ぶんしょう</rt></ruby>にするために、「こ・そ・あ」を<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>けることが<ruby>大切<rt>たいせつ</rt></ruby>です。",
        "theme_en": "To ensure a sentence is coherent, it is important to correctly distinguish the usage of こ, そ and あ.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>中<rt>なか</rt></ruby>では、<ruby>前<rt>まえ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>の<ruby>語<rt>ご</rt></ruby>や<ruby>文<rt>ぶん</rt></ruby>の<ruby>内容<rt>ないよう</rt></ruby>を<ruby>指<rt>さ</rt></ruby>すとき、ふつう「そ」を<ruby>使<rt>つか</rt></ruby>います。ただし、<ruby>自分<rt>じぶん</rt></ruby>と<ruby>心理的<rt>しんりてき</rt></ruby>に<ruby>近<rt>ちか</rt></ruby>いことを<ruby>示<rt>しめ</rt></ruby>したいときは「こ」を<ruby>使<rt>つか</rt></ruby>うことが<ruby>多<rt>おお</rt></ruby>いです。",
                "examples": [
                    "書類をどこかに置き忘れた。それには大切な情報が書いてあったのだが……。",
                    "実験は安全だろうか。まずそのことを確かめてから始めたい。",
                    "新しい市長が決まった。この人はわたしの高校時代の同級生である。"
                ]
            },
            {
                "point_number": 2,
                "title": "<ruby>個人的<rt>こじんてき</rt></ruby>な<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で、<ruby>思<rt>おも</rt></ruby>い<ruby>出<rt>だ</rt></ruby>している<ruby>物<rt>もの</rt></ruby>を<ruby>指<rt>さ</rt></ruby>すとき、「あ」を<ruby>使<rt>つか</rt></ruby>います。",
                "examples": [
                    "子どものころ、近くの公園でよく遊んだ。あの公園はまだ残っているだろうか。"
                ]
            },
            {
                "point_number": 3,
                "title": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>中<rt>なか</rt></ruby>の「こ・そ」の<ruby>形<rt>かたち</rt></ruby>",
                "forms_table": [
                    {
                        "forms": "それ／これ",
                        "usage": "物・内容を指す",
                        "examples": "友だちから指輪をもらった。これは今、わたしの宝物である。／進学するお金がない。それが問題だ。"
                    },
                    {
                        "forms": "そこ／ここ",
                        "usage": "場所・部分を指す",
                        "examples": "港に着いて船を降りた。そこで母が待っていた。／この曲は初めのメロディがすてきだ。ここは何度聞いてもあきない。"
                    },
                    {
                        "forms": "その／この",
                        "usage": "限定する",
                        "examples": "明日、ある会社の社長に会う。その会社は大阪にある。／今年の誕生日に山に行った。この日は非常に寒かった。"
                    },
                    {
                        "forms": "そんな／こんな／そういう／こういう",
                        "usage": "状況を指す",
                        "examples": "妹は一日12時間も寝る。こんな人は珍しいのではないか。／この川では最近全く魚が釣れない。そういうことは今までなかった。"
                    },
                    {
                        "forms": "こう／そう",
                        "usage": "前の文の内容を指して副詞のように使う",
                        "examples": "困ったとき助けてくれる友だちがいる。そう思うと安心する。／忙しい、時間がない。こう言い訳するのがわたしのくせだ。／毎日朝夕5分間ずつ英語を聞く。こうすると聞き取りが上達する。"
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30701,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>う<ruby>約束<rt>やくそく</rt></ruby>があった。わたしは（a それ　b そこ）を<ruby>忘<rt>わす</rt></ruby>れていた。",
                "options": ["a それ", "b そこ"],
                "correct_answer": "a",
                "explanation_ja": "約束という内容・事柄を指すので「それ」。",
                "explanation_en": "Refers to the promise/fact (thing/content): 'それ'."
            },
            {
                "question_id": 30702,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>中山<rt>なかやま</rt></ruby><ruby>君<rt>くん</rt></ruby>が<ruby>不合格<rt>ふごうかく</rt></ruby>だったそうだ。（a そんな　b あんな）ことは<ruby>信<rt>しん</rt></ruby>じられない。",
                "options": ["a そんな", "b あんな"],
                "correct_answer": "a",
                "explanation_ja": "直前に言及された他者の状況・情報を受けるので「そんな」。",
                "explanation_en": "Refers back to mentioned information: 'そんな'."
            },
            {
                "question_id": 30703,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>朝<rt>あさ</rt></ruby>から<ruby>大雨<rt>おおあめ</rt></ruby>でいやだなあ。（a そういう　b こんな）<ruby>日<rt>ひ</rt></ruby>はどこへも<ruby>出<rt>で</rt></ruby>かけたくない。",
                "options": ["a そういう", "b こんな"],
                "correct_answer": "b",
                "explanation_ja": "話し手が今まさに直面している当日の心理的に近い状況なので「こんな」。",
                "explanation_en": "Points to today's immediately experienced rainy situation: 'こんな'."
            },
            {
                "question_id": 30704,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>図書館<rt>としょかん</rt></ruby>で、<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>本<rt>ほん</rt></ruby>をほかの<ruby>人<rt>ひと</rt></ruby>が<ruby>借<rt>か</rt></ruby>りていることがあります。（a そういう　b それ）の<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>予約<rt>よやく</rt></ruby>をすることができます。",
                "options": ["a そういう", "b それ"],
                "correct_answer": "a",
                "explanation_ja": "名詞「場合」を連体修飾して状況を指すので「そういう場合」。",
                "explanation_en": "Modifies noun '場合' pointing to the situation: 'そういう場合'."
            },
            {
                "question_id": 30705,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>少子化<rt>しょうしか</rt></ruby>というのはそんなに<ruby>悪<rt>わる</rt></ruby>いことではないのではないか。（a こう　b これを）<ruby>考<rt>かんが</rt></ruby>える<ruby>人<rt>ひと</rt></ruby>も<ruby>多<rt>おお</rt></ruby>いだろう。",
                "options": ["a こう", "b これを"],
                "correct_answer": "a",
                "explanation_ja": "「〜と考える」の引用副詞的に前の文の内容を受けるので「こう考える」。",
                "explanation_en": "Acts adverbially with the verb of thinking: 'こう考える'."
            },
            {
                "question_id": 30706,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>世<rt>よ</rt></ruby>の<ruby>中<rt>なか</rt></ruby>には<ruby>自分<rt>じぶん</rt></ruby>とそっくりな<ruby>人<rt>ひと</rt></ruby>が3<ruby>人<rt>にん</rt></ruby>いるという。しかし、わたしは（a その　b そんな）<ruby>人<rt>ひと</rt></ruby>には<ruby>会<rt>あ</rt></ruby>ったことがない。",
                "options": ["a その", "b そんな"],
                "correct_answer": "b",
                "explanation_ja": "「自分とそっくりな人」というタイプ・性質の人を指すので「そんな人」。",
                "explanation_en": "Indicates a person of such a type/nature: 'そんな人'."
            },
            {
                "question_id": 30707,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "パリには<ruby>前<rt>まえ</rt></ruby>に<ruby>一度<rt>いちど</rt></ruby><ruby>行<rt>い</rt></ruby>った。（a その　b そんな）ときわたしは<ruby>二十歳<rt>はたち</rt></ruby>だった。",
                "options": ["a その", "b そんな"],
                "correct_answer": "a",
                "explanation_ja": "前にパリへ行ったその時点を限定して指すので「そのとき」。",
                "explanation_en": "Specifies that particular point in time: 'そのとき'."
            },
            {
                "question_id": 30708,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>眠<rt>ねむ</rt></ruby>れないときは<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>めばいいと<ruby>中川<rt>なかがわ</rt></ruby>さんは<ruby>言<rt>い</rt></ruby>うが、（a そう　b そうするの）がいいとは<ruby>思<rt>おも</rt></ruby>えない。",
                "options": ["a そう", "b そうするの"],
                "correct_answer": "b",
                "explanation_ja": "助詞「が」の主語名詞節として「そうするの（＝そうすること）がいいとは…」で受ける。",
                "explanation_en": "Acts as the nominalized subject before particle 'が': 'そうするの'."
            },
            {
                "question_id": 30709,
                "category": "第3部 7課 練習",
                "question_type": "binary_choice",
                "prompt": "<ruby>天<rt>てん</rt></ruby>ぷらは<ruby>野菜<rt>やさい</rt></ruby>などに<ruby>卵<rt>たまご</rt></ruby>と<ruby>小麦粉<rt>こむぎこ</rt></ruby>をつけて、（a それを　b その）<ruby>油<rt>あぶら</rt></ruby>で<ruby>揚<rt>あ</rt></ruby>げた<ruby>料理<rt>りょうり</rt></ruby>です。",
                "options": ["a それを", "b その"],
                "correct_answer": "a",
                "explanation_ja": "卵と小麦粉をつけた具材を油で揚げるので、目的語として「それを」。",
                "explanation_en": "Object marker indicating the prepared ingredients: 'それを'."
            },
            {
                "question_id": 30710,
                "category": "第3部 7課 練習",
                "question_type": "cloze_demonstrative",
                "prompt": "<ruby>友<rt>とも</rt></ruby>だちが<ruby>映画<rt>えいが</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>をしていたが、わたしは（① a その　b あの）<ruby>映画<rt>えいが</rt></ruby>を<ruby>知<rt>し</rt></ruby>らなかった。とても<ruby>面白<rt>おもしろ</rt></ruby>いそうだ。<ruby>友<rt>とも</rt></ruby>だちが（② a そう　b そうと）<ruby>言<rt>い</rt></ruby>ったのでぜひ<ruby>見<rt>み</rt></ruby>たいと<ruby>思<rt>おも</rt></ruby>い、レンタルショップに<ruby>行<rt>い</rt></ruby>ったが、（③ a それ　b そこ）には<ruby>置<rt>お</rt></ruby>いていなかった。",
                "correct_answers": ["① a", "② a", "③ b"],
                "explanation_ja": "①相手から聞いた未知の映画なので「その映画」（a）。②友だちがそう言った（a、副詞的用法）。③レンタルショップという場所を指すので「そこ」（b）。",
                "explanation_en": "①'その' (a). ②'そう' (a). ③'そこ' (b)."
            }
        ]
    }

    # =========================================================================
    # Lesson 8: 8課 は・が (p. 136-137, Images 138-139)
    # =========================================================================
    sec8 = {
        "section_number": 8,
        "title": "<ruby>第<rt>だい</rt></ruby>8<ruby>課<rt>か</rt></ruby> は・が",
        "title_en": "Lesson 8: Particles 'wa' and 'ga'",
        "theme": "まとまりのある<ruby>文章<rt>ぶんしょう</rt></ruby>にするために、「は・が」を<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>けることが<ruby>大切<rt>たいせつ</rt></ruby>です。",
        "theme_en": "To ensure sentence cohesion, it is important to correctly distinguish between は and が.",
        "points": [
            {
                "point_number": 1,
                "title": "「が」を<ruby>使<rt>つか</rt></ruby>う<ruby>場合<rt>ばあい</rt></ruby>",
                "title_en": "When to use 'ga'",
                "usages": [
                    {
                        "rule": "1. <ruby>初<rt>はじ</rt></ruby>めて<ruby>話題<rt>わだい</rt></ruby>に<ruby>出<rt>で</rt></ruby>たものや<ruby>特<rt>とく</rt></ruby>に<ruby>伝<rt>つた</rt></ruby>えたいことを<ruby>言<rt>い</rt></ruby>うとき",
                        "rule_en": "When describing a topic introduced for the first time or when you particularly want to emphasize something.",
                        "examples": [
                            "昔、ある村に太郎という若者が住んでいた。",
                            "明日、首相がこの市に来る。"
                        ]
                    },
                    {
                        "rule": "2. <ruby>自然現象<rt>しぜんげんしょう</rt></ruby>やその<ruby>場<rt>ば</rt></ruby>で<ruby>見<rt>み</rt></ruby>たこと・<ruby>聞<rt>き</rt></ruby>いたことを<ruby>言<rt>い</rt></ruby>うとき",
                        "rule_en": "In describing natural phenomena and things you have seen or heard in person.",
                        "examples": [
                            "久しぶりに公園を散歩した。桜がとても美しかった。",
                            "ここはいい所だ。さわやかな風が吹いて、木の上で鳥が鳴いている。"
                        ]
                    },
                    {
                        "rule": "3. <ruby>名詞<rt>めいし</rt></ruby>を<ruby>説明<rt>せつめい</rt></ruby>する<ruby>文<rt>ぶん</rt></ruby>や<ruby>条件<rt>じょうけん</rt></ruby>・<ruby>時<rt>とき</rt></ruby>・<ruby>理由<rt>りゆう</rt></ruby>などを<ruby>表<rt>あらわ</rt></ruby>す<ruby>文<rt>ぶん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>の<ruby>主語<rt>しゅご</rt></ruby>を<ruby>言<rt>い</rt></ruby>うとき",
                        "rule_en": "When highlighting the subject in statements in which the noun is modified, or which express conditions, time or reasons.",
                        "examples": [
                            "あの作家が書いた本を一度読んでみるべきだ。",
                            "ヤンさんが来たら、この書類を見せよう。"
                        ]
                    }
                ]
            },
            {
                "point_number": 2,
                "title": "「は」を<ruby>使<rt>つか</rt></ruby>う<ruby>場合<rt>ばあい</rt></ruby>",
                "title_en": "When to use 'wa'",
                "usages": [
                    {
                        "rule": "1. ある<ruby>話題<rt>わだい</rt></ruby>を<ruby>取<rt>と</rt></ruby>り<ruby>上<rt>あ</rt></ruby>げるとき、<ruby>一度<rt>いちど</rt></ruby><ruby>前<rt>まえ</rt></ruby>に<ruby>出<rt>で</rt></ruby>た<ruby>話題<rt>わだい</rt></ruby>を<ruby>言<rt>い</rt></ruby>うとき",
                        "rule_en": "When raising a topic, and when referring back to a topic mentioned before.",
                        "examples": [
                            "日本語能力試験は大勢の人が受験する。",
                            "昔、ある村に太郎という若者が住んでいた。太郎はとても貧乏だった。"
                        ]
                    },
                    {
                        "rule": "2. <ruby>特<rt>とく</rt></ruby>に<ruby>話題<rt>わだい</rt></ruby>にすること・<ruby>強調<rt>きょうちょう</rt></ruby>すること・<ruby>否定<rt>ひてい</rt></ruby>することを<ruby>言<rt>い</rt></ruby>うとき",
                        "rule_en": "When drawing attention to, emphasizing or negating a topic.",
                        "examples": [
                            "日本では車は道の左側を通ることになっています。",
                            "あの人とは結婚しようとは思わない。"
                        ]
                    },
                    {
                        "rule": "3. <ruby>二<rt>ふた</rt></ruby>つのことを<ruby>対比<rt>たいひ</rt></ruby>して<ruby>言<rt>い</rt></ruby>うとき",
                        "rule_en": "To explicitly contrast two things.",
                        "examples": [
                            "梅の花は咲いていますが、桜はまだです。",
                            "雪は降っているが、風はない。",
                            "外ではコートを着ますが、部屋の中では脱ぎます。"
                        ]
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30801,
                "category": "第3部 8課 練習1",
                "question_type": "fill_particles",
                "prompt": "きのう<ruby>授業<rt>じゅぎょう</rt></ruby>①＿＿＿<ruby>終<rt>お</rt></ruby>わってから、クラスのカーンさんと<ruby>本屋<rt>ほんや</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。カーンさん②＿＿＿<ruby>日本語<rt>にほんご</rt></ruby>のテキストを<ruby>買<rt>か</rt></ruby>いたいと<ruby>言<rt>い</rt></ruby>ったので、いっしょに<ruby>買<rt>か</rt></ruby>いに<ruby>行<rt>い</rt></ruby>くことにしたのです。カーンさん③＿＿＿、<ruby>会話<rt>かいわ</rt></ruby>④＿＿＿まあまあ<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>だけれど、<ruby>書<rt>か</rt></ruby>くのはまだ<ruby>下手<rt>へた</rt></ruby>だと<ruby>言<rt>い</rt></ruby>いました。わたしはその<ruby>反対<rt>はんたい</rt></ruby>です。<ruby>本屋<rt>ほんや</rt></ruby>⑤＿＿＿7<ruby>階<rt>かい</rt></ruby>まであります。まっすぐ5<ruby>階<rt>かい</rt></ruby>の<ruby>日本語<rt>にほんご</rt></ruby>のコーナーへ<ruby>行<rt>い</rt></ruby>きました。<ruby>日本語<rt>にほんご</rt></ruby>のテキスト⑥＿＿＿たくさん<ruby>並<rt>なら</rt></ruby>んでいました。その<ruby>中<rt>なか</rt></ruby>に<ruby>松本<rt>まつもと</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>⑦＿＿＿<ruby>紹介<rt>しょうかい</rt></ruby>してくださった<ruby>本<rt>ほん</rt></ruby>⑧＿＿＿ありました。それ⑨＿＿＿<ruby>中級<rt>ちゅうきゅう</rt></ruby>のレベルの<ruby>言葉<rt>ことば</rt></ruby>⑩＿＿＿ていねいに<ruby>説明<rt>せつめい</rt></ruby>されている<ruby>本<rt>ほん</rt></ruby>です。また、カーンさん⑪＿＿＿<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>練習帳<rt>れんしゅうちょう</rt></ruby>も<ruby>必要<rt>ひつよう</rt></ruby>だと<ruby>言<rt>い</rt></ruby>って、<ruby>表紙<rt>ひょうし</rt></ruby>⑫＿＿＿とてもきれいな<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>を<ruby>選<rt>えら</rt></ruby>びました。<ruby>買<rt>か</rt></ruby>う<ruby>本<rt>ほん</rt></ruby>⑬＿＿＿1<ruby>階<rt>かい</rt></ruby>に<ruby>持<rt>も</rt></ruby>っていって、1<ruby>階<rt>かい</rt></ruby>のカウンターでお<ruby>金<rt>かね</rt></ruby>を<ruby>払<rt>はら</rt></ruby>いました。",
                "correct_answers": ["① が", "② が", "③ は", "④ は", "⑤ は", "⑥ が", "⑦ が", "⑧ が", "⑨ は", "⑩ が", "⑪ は", "⑫ が", "⑬ は"],
                "explanation_ja": "解答冊子p.6参照：①が ②が ③は ④は ⑤は ⑥が ⑦が ⑧が ⑨は ⑩が ⑪は ⑫が ⑬は。",
                "explanation_en": "See Answer booklet p.6: ①が ②が ③は ④は ⑤は ⑥が ⑦が ⑧が ⑨は ⑩が ⑪は ⑫が ⑬は."
            },
            {
                "question_id": 30802,
                "category": "第3部 8課 練習2",
                "question_type": "fill_particles",
                "prompt": "<ruby>日本人<rt>にほんじん</rt></ruby>①＿＿＿<ruby>発明<rt>はつめい</rt></ruby>した<ruby>物<rt>もの</rt></ruby>はいろいろあるが、<ruby>胃<rt>い</rt></ruby>の<ruby>中<rt>なか</rt></ruby>を<ruby>写<rt>うつ</rt></ruby>す「<ruby>胃<rt>い</rt></ruby>カメラ」も<ruby>日本人<rt>にほんじん</rt></ruby>の<ruby>発明<rt>はつめい</rt></ruby>であること②＿＿＿あまり<ruby>知<rt>し</rt></ruby>られていない。<ruby>胃<rt>い</rt></ruby>カメラ<ruby>作<rt>づく</rt></ruby>り③＿＿＿<ruby>始<rt>はじ</rt></ruby>まったの④＿＿＿、<ruby>第二次<rt>だいにじ</rt></ruby><ruby>世界大戦<rt>せかいたいせん</rt></ruby>⑤＿＿＿<ruby>終<rt>お</rt></ruby>わったばかりの1949<ruby>年<rt>ねん</rt></ruby>だった。<ruby>光<rt>ひかり</rt></ruby>⑥＿＿＿ない<ruby>胃<rt>い</rt></ruby>の<ruby>中<rt>なか</rt></ruby>の<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ることなどできないとだれもが<ruby>考<rt>かんが</rt></ruby>えたが、<ruby>小<rt>ちい</rt></ruby>さい<ruby>電球<rt>でんきゅう</rt></ruby>の<ruby>弱<rt>よわ</rt></ruby>い<ruby>光<rt>ひかり</rt></ruby>でも<ruby>写真<rt>しゃしん</rt></ruby>⑦＿＿＿<ruby>撮<rt>と</rt></ruby>れる<ruby>方法<rt>ほうほう</rt></ruby>を<ruby>工夫<rt>くふう</rt></ruby>して、1<ruby>年後<rt>ねんご</rt></ruby><ruby>胃<rt>い</rt></ruby>カメラを<ruby>完成<rt>かんせい</rt></ruby>させた。<ruby>胃<rt>い</rt></ruby>カメラ⑧＿＿＿<ruby>胃<rt>い</rt></ruby>の<ruby>病気<rt>びょうき</rt></ruby>を<ruby>早<rt>はや</rt></ruby>く<ruby>発見<rt>はっけん</rt></ruby>するのに<ruby>役立<rt>やくだ</rt></ruby>って、<ruby>世界中<rt>せかいじゅう</rt></ruby>で<ruby>多<rt>おお</rt></ruby>くの<ruby>人<rt>ひと</rt></ruby>を<ruby>助<rt>たす</rt></ruby>けている。",
                "correct_answers": ["① が", "② は", "③ が", "④ は", "⑤ が", "⑥ が", "⑦ が", "⑧ は"],
                "explanation_ja": "解答冊子p.7参照：①が ②は ③が ④は ⑤が ⑥が ⑦が ⑧は。",
                "explanation_en": "See Answer booklet p.7: ①が ②は ③が ④は ⑤が ⑥が ⑦が ⑧は."
            }
        ]
    }

    # =========================================================================
    # Review Test 7-8: まとめ問題 (7課・8課) (p. 138-139, Images 140-141)
    # =========================================================================
    matome_7_8 = {
        "section_number": 8.5,
        "title": "まとめ<ruby>問題<rt>もんだい</rt></ruby>（7<ruby>課<rt>か</rt></ruby>・8<ruby>課<rt>か</rt></ruby>）",
        "title_en": "Review Exercises (Lessons 7 & 8)",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>総合練習<rt>そうごうれんしゅう</rt></ruby>（指示詞と「は・が」）",
        "theme_en": "Comprehensive text grammar review: Demonstratives and 'wa'/'ga'",
        "passages": [
            {
                "passage_id": 307,
                "title": "豚とペンギン",
                "title_en": "The Pig and the Penguin",
                "text": "<ruby>面白<rt>おもしろ</rt></ruby>い［ 1 ］。\nある<ruby>日<rt>ひ</rt></ruby>ある<ruby>所<rt>ところ</rt></ruby>で<ruby>豚<rt>ぶた</rt></ruby>とペンギン（注）が<ruby>出会<rt>であ</rt></ruby>った。ペンギンは<ruby>豚<rt>ぶた</rt></ruby>に「<ruby>今日<rt>きょう</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>いね」と<ruby>言<rt>い</rt></ruby>った。<ruby>豚<rt>ぶた</rt></ruby>は「いや、そんなことはない。<ruby>過<rt>す</rt></ruby>ごしやすい<ruby>日<rt>ひ</rt></ruby>だよ」と<ruby>言<rt>い</rt></ruby>った。「<ruby>違<rt>ちが</rt></ruby>うよ。ほら、<ruby>温度計<rt>おんどけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>ろよ。<ruby>気温<rt>きおん</rt></ruby>は<ruby>高<rt>たか</rt></ruby>いよ。25<ruby>度<rt>ど</rt></ruby>だよ」「25<ruby>度<rt>ど</rt></ruby>？ ちょうどいい<ruby>気温<rt>きおん</rt></ruby>じゃないか」ペンギンと<ruby>豚<rt>ぶた</rt></ruby>はとうとうけんかになってしまった……という<ruby>話<rt>はなし</rt></ruby>である。\nもちろん、<ruby>豚<rt>ぶた</rt></ruby>とペンギンは<ruby>一<rt>ひと</rt></ruby>つのたとえなのだが、［ 2 ］わたしたちの<ruby>日常<rt>にちじょう</rt></ruby>によくあることだ。<ruby>南極<rt>なんきょく</rt></ruby>から<ruby>来<rt>き</rt></ruby>たペンギンと<ruby>暖<rt>あたた</rt></ruby>かい<ruby>所<rt>ところ</rt></ruby>に<ruby>住<rt>す</rt></ruby>む<ruby>豚<rt>ぶた</rt></ruby>の<ruby>感<rt>かん</rt></ruby>じ<ruby>方<rt>かた</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>うように、<ruby>暑<rt>あつ</rt></ruby>さ、うるささ、<ruby>美<rt>うつく</rt></ruby>しさ、<ruby>広<rt>ひろ</rt></ruby>さ、<ruby>便利<rt>べんり</rt></ruby>さなどは、<ruby>人<rt>ひと</rt></ruby>によって<ruby>基準<rt>きじゅん</rt></ruby>が<ruby>違<rt>ちが</rt></ruby>う。その<ruby>基準<rt>きじゅん</rt></ruby>は［ 3 ］<ruby>性格<rt>せいかく</rt></ruby>や<ruby>生<rt>う</rt></ruby>まれ<ruby>育<rt>そだ</rt></ruby>った<ruby>環境<rt>かんきょう</rt></ruby>によってできあがるのだろう。それぞれ［ 4 ］<ruby>違<rt>ちが</rt></ruby>う<ruby>人<rt>ひと</rt></ruby>が<ruby>集<rt>あつ</rt></ruby>まって<ruby>集団<rt>しゅうだん</rt></ruby>をつくり、<ruby>人間<rt>にんげん</rt></ruby>はその<ruby>集団<rt>しゅうだん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で<ruby>生活<rt>せいかつ</rt></ruby>している。このことをよく<ruby>理解<rt>りかい</rt></ruby>しなければ、わたしたちはこの<ruby>話<rt>はなし</rt></ruby>を［ 5 ］。\n（注：ペンギン）\n参考：©小泉吉宏／メディアファクトリー",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30701,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　漫画がある",
                            "2　漫画はある",
                            "3　漫画である",
                            "4　漫画でもある"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "冒頭で新しい話題・存在を導入するので「面白い漫画がある」。1が正解。",
                        "explanation_en": "Introduces a new existence at the beginning: '面白い漫画がある'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30702,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　このことは",
                            "2　このことが",
                            "3　こういうことは",
                            "4　こういうことが"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "豚とペンギンの例のような一般的な同類の出来事を指し、主題として取り上げるので「こういうことは」。3が正解。",
                        "explanation_en": "Refers to such situations in general as a topic: 'こういうことは'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30703,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　そんな",
                            "2　そういう",
                            "3　その人の",
                            "4　そんな人の"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "直前の「人によって基準が違う」の「人」を受けて限定するので「その人の性格や…」。3が正解。",
                        "explanation_en": "Refers to the individual mentioned previously: 'その人の'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30704,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　基準は",
                            "2　基準が",
                            "3　基準でも",
                            "4　基準では"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "名詞「人」を修飾する連体修飾節の中の主語なので「基準が違う人」。2が正解。",
                        "explanation_en": "Subject inside a noun-modifying clause takes 'が': '基準が違う人'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30705,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　怒らないだろう",
                            "2　怒れないだろう",
                            "3　笑わないだろう",
                            "4　笑えないだろう"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "人間も同じ過ちを犯すため他人事として笑うことができない。「笑えないだろう」。4が正解。",
                        "explanation_en": "Cannot laugh it off because humans do the exact same thing: '笑えないだろう'. Choice 4 is correct."
                    }
                ]
            },
            {
                "passage_id": 308,
                "title": "ペットロボット",
                "title_en": "Pet Robots",
                "text": "わたしはロボットに<ruby>関心<rt>かんしん</rt></ruby>があります。ロボットというのは<ruby>工場<rt>こうじょう</rt></ruby>などで<ruby>人間<rt>にんげん</rt></ruby>に<ruby>代<rt>か</rt></ruby>わっていろいろな<ruby>仕事<rt>しごと</rt></ruby>をする<ruby>機械<rt>きかい</rt></ruby>のことだと<ruby>思<rt>おも</rt></ruby>う<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>いかもしれませんが、わたしが<ruby>研究<rt>けんきゅう</rt></ruby>したいのは［ 1 ］、ペットの<ruby>代<rt>か</rt></ruby>わりをするロボットなのです。つまり、［ 2 ］ロボットです。<ruby>動物<rt>どうぶつ</rt></ruby>が<ruby>好<rt>す</rt></ruby>きな<ruby>人<rt>ひと</rt></ruby>はペットと<ruby>遊<rt>あそ</rt></ruby>ぶことで<ruby>心<rt>こころ</rt></ruby>が<ruby>明<rt>あか</rt></ruby>るくなるようです。しかし、ペットを<ruby>飼<rt>か</rt></ruby>いたくても<ruby>飼<rt>か</rt></ruby>えない<ruby>人<rt>ひと</rt></ruby>もいます。［ 3 ］ペットロボットです。\nすでに<ruby>日本<rt>にほん</rt></ruby>ではいくつかのペットロボットが<ruby>売<rt>う</rt></ruby>られています。これらの［ 4 ］<ruby>喜<rt>よろこ</rt></ruby>んだり<ruby>声<rt>こえ</rt></ruby>を<ruby>出<rt>だ</rt></ruby>したりします。ペットロボットは<ruby>病気<rt>びょうき</rt></ruby>の<ruby>子<rt>こ</rt></ruby>どもたちやお<ruby>年寄<rt>としよ</rt></ruby>りを<ruby>元気<rt>げんき</rt></ruby>にするために<ruby>役立<rt>やくだ</rt></ruby>てられています。ある<ruby>研究所<rt>けんきゅうじょ</rt></ruby>の<ruby>調査<rt>ちょうさ</rt></ruby>によると、ペットロボットと<ruby>遊<rt>あそ</rt></ruby>んだ<ruby>後<rt>あと</rt></ruby>は<ruby>気分<rt>きぶん</rt></ruby>がよくなった、ほかの<ruby>人<rt>ひと</rt></ruby>との<ruby>会話<rt>かいわ</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えた、<ruby>話題<rt>わだい</rt></ruby>がペットロボットについての<ruby>明<rt>あか</rt></ruby>るい<ruby>内容<rt>ないよう</rt></ruby>に<ruby>変<rt>か</rt></ruby>わった、などのいい<ruby>効果<rt>こうか</rt></ruby>が<ruby>出<rt>で</rt></ruby>ているとのことです。\nわたしは、［ 5 ］ペットロボットの<ruby>研究<rt>けんきゅう</rt></ruby>を<ruby>一生<rt>いっしょう</rt></ruby>のテーマにしたいと<ruby>思<rt>おも</rt></ruby>っています。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30801,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　このような産業ロボットで",
                            "2　このような産業ロボットではなく",
                            "3　そういう産業ロボットで",
                            "4　あのような産業ロボットではなく"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "直前で述べた工場で使われるロボットを否定して対比するので「このような産業ロボットではなく」。2が正解。",
                        "explanation_en": "Negates and contrasts with the aforementioned factory robots: 'このような産業ロボットではなく'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30802,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　人間をかわいがる",
                            "2　人間はかわいがる",
                            "3　人間にかわいがられる",
                            "4　人間がかわいがられる"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "ペットロボットは人間によってかわいがられる対象なので受身「人間にかわいがられるロボット」。3が正解。",
                        "explanation_en": "Passive modifying noun: '人間にかわいがられるロボット' (cherished by humans). Choice 3 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30803,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　そんな人が作ったのは",
                            "2　この人のために作られたのが",
                            "3　こういう人によって作られたのは",
                            "4　そんな人のために作られたのが"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "「ペットを飼いたくても飼えない人」を受けて目的を表すので「そんな人のために作られたのが」。4が正解。",
                        "explanation_en": "Refers back to people who want pets but cannot have them: 'そんな人のために作られたのが'. Choice 4 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30804,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　ペットロボットは本物の動物のように",
                            "2　ペットロボットが本物のロボットのように",
                            "3　ペットロボットは本物の人間のように",
                            "4　ペットロボットが本物のように"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "これらのロボットの主語として取り上げ、本物の動物に似て行動することを述べるので「ペットロボットは本物の動物のように」。1が正解。",
                        "explanation_en": "'ペットロボットは本物の動物のように' (pet robots, like real animals). Choice 1 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30805,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　このような心理的効果がある",
                            "2　このような心理的効果はなくても",
                            "3　この心理的効果があって",
                            "4　その心理的効果がなくても"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "直前の段落で述べられた気分の改善などの効果を受けて「このような心理的効果があるペットロボットの…」。1が正解。",
                        "explanation_en": "'このような心理的効果がある' modifies the pet robots being researched. Choice 1 is correct."
                    }
                ]
            }
        ]
    }

    return [sec5, sec6, matome_5_6, sec7, sec8, matome_7_8]
