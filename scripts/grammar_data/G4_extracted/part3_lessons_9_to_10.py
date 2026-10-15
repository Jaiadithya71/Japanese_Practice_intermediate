"""
Module: part3_lessons_9_to_10.py
Part 3: 文章の文法 (Grammar in Text / Passage Cloze)
Lessons 9 to 10 + Review Test 9-10 (Images 142-147, p. 140-145).
"""

def get_lessons_9_to_10():
    # =========================================================================
    # Lesson 9: 9課 接続表現 (p. 140-141, Images 142-143)
    # =========================================================================
    sec9 = {
        "section_number": 9,
        "title": "<ruby>第<rt>だい</rt></ruby>9<ruby>課<rt>か</rt></ruby> <ruby>接続表現<rt>せつぞくひょうげん</rt></ruby>",
        "title_en": "Lesson 9: Conjunctions and Connectives",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>で<ruby>使<rt>つか</rt></ruby>うN3レベルの<ruby>接続表現<rt>せつぞくひょうげん</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>を<ruby>整理<rt>せいり</rt></ruby>します。",
        "theme_en": "N3-level conjunctive terms in a sentence are used as follows.",
        "points": [
            {
                "point_number": 1,
                "title": "<ruby>接続表現<rt>せつぞくひょうげん</rt></ruby>の<ruby>分類<rt>ぶんるい</rt></ruby>と<ruby>用例<rt>ようれい</rt></ruby>",
                "title_en": "Categories and Examples of Conjunctions",
                "categories": [
                    {
                        "category_name": "1. <ruby>加<rt>くわ</rt></ruby>えて<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "To add information",
                        "conjunctions": ["また", "さらに", "そのうえ", "しかも", "それも"],
                        "examples": [
                            "ノートパソコンは<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>取<rt>と</rt></ruby>らない。<ruby>また<rt>また</rt></ruby>、<ruby>持<rt>も</rt></ruby>ち<ruby>運<rt>はこ</rt></ruby>びにも<ruby>便利<rt>べんり</rt></ruby>だ。",
                            "<ruby>彼<rt>かれ</rt></ruby>は<ruby>料理<rt>りょうり</rt></ruby>を<ruby>二人分<rt>ふたりぶん</rt></ruby>も<ruby>食<rt>た</rt></ruby>べた。<ruby>さらに<rt>さらに</rt></ruby>、<ruby>食後<rt>しょくご</rt></ruby>にケーキも<ruby>食<rt>た</rt></ruby>べた。",
                            "<ruby>毎日<rt>まいにち</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>が<ruby>大変<rt>たいへん</rt></ruby>だ。<ruby>そのうえ<rt>そのうえ</rt></ruby>、アルバイトもしている。",
                            "<ruby>小川<rt>おがわ</rt></ruby>さんは<ruby>仕事<rt>しごと</rt></ruby>が<ruby>早<rt>はや</rt></ruby>い。<ruby>しかも<rt>しかも</rt></ruby>、<ruby>正確<rt>せいかく</rt></ruby>だ。",
                            "<ruby>作文<rt>さくぶん</rt></ruby>を<ruby>書<rt>か</rt></ruby>き<ruby>直<rt>なお</rt></ruby>させられた。<ruby>それも<rt>それも</rt></ruby>、3<ruby>回<rt>かい</rt></ruby>もだ。"
                        ]
                    },
                    {
                        "category_name": "2. <ruby>結果<rt>けっか</rt></ruby>・<ruby>結論<rt>けつろん</rt></ruby>を<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "To express a result or conclusion",
                        "conjunctions": ["そのため", "したがって", "そこで", "すると"],
                        "examples": [
                            "<ruby>事故<rt>じこ</rt></ruby>があった。<ruby>そのため<rt>そのため</rt></ruby>、<ruby>道<rt>みち</rt></ruby>が<ruby>込<rt>こ</rt></ruby>んでいる。",
                            "この<ruby>調査方法<rt>ちょうさほうほう</rt></ruby>には<ruby>間違<rt>まちが</rt></ruby>いがある。<ruby>したがって<rt>したがって</rt></ruby>、この<ruby>結果<rt>けっか</rt></ruby>は<ruby>正<rt>ただ</rt></ruby>しいとは<ruby>言<rt>い</rt></ruby>えない。",
                            "<ruby>部屋<rt>へや</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えてきた。<ruby>そこで<rt>そこで</rt></ruby>、<ruby>本<rt>ほん</rt></ruby>だなを<ruby>買<rt>か</rt></ruby>うことにした。",
                            "<ruby>紅茶<rt>こうちゃ</rt></ruby>にレモンを<ruby>入<rt>い</rt></ruby>れた。<ruby>すると<rt>すると</rt></ruby>、<ruby>色<rt>いろ</rt></ruby>が<ruby>変<rt>か</rt></ruby>わった。"
                        ]
                    },
                    {
                        "category_name": "3. <ruby>理由<rt>りゆう</rt></ruby>・<ruby>根拠<rt>こんきょ</rt></ruby>を<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "To express a reason or grounds for doing something",
                        "conjunctions": ["なぜなら／なぜかというと…からだ"],
                        "examples": [
                            "<ruby>大学<rt>だいがく</rt></ruby>では<ruby>文学<rt>ぶんがく</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>したい。<ruby>なぜなら<rt>なぜなら</rt></ruby>／<ruby>なぜかというと<rt>なぜかというと</rt></ruby>、<ruby>作家<rt>さっか</rt></ruby>になりたいからだ。"
                        ]
                    },
                    {
                        "category_name": "4. <ruby>別<rt>べつ</rt></ruby>の<ruby>言<rt>い</rt></ruby>い<ruby>方<rt>かた</rt></ruby>で<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "To indicate an alternative way of expressing something",
                        "conjunctions": ["つまり"],
                        "examples": [
                            "この<ruby>仕事<rt>しごと</rt></ruby>は<ruby>土曜日<rt>どようび</rt></ruby>と<ruby>日曜日<rt>にちようび</rt></ruby>が<ruby>休<rt>やす</rt></ruby>みだ。<ruby>つまり<rt>つまり</rt></ruby>、<ruby>週休二日<rt>しゅうきゅうふつか</rt></ruby>だ。"
                        ]
                    },
                    {
                        "category_name": "5. <ruby>比<rt>くら</rt></ruby>べて<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "To compare, or express a contrast",
                        "conjunctions": ["それに対して", "一方"],
                        "examples": [
                            "<ruby>妹<rt>いもうと</rt></ruby>は<ruby>明<rt>あか</rt></ruby>るい。<ruby>それに対して<rt>それに対して</rt></ruby>／<ruby>一方<rt>いっぽう</rt></ruby>、<ruby>姉<rt>あね</rt></ruby>はおとなしい。"
                        ]
                    },
                    {
                        "category_name": "6. どちらかであることを<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "To choose among alternatives",
                        "conjunctions": ["または"],
                        "examples": [
                            "<ruby>出欠<rt>しゅっけつ</rt></ruby>の<ruby>返事<rt>へんじ</rt></ruby>はメールで<ruby>知<rt>し</rt></ruby>らせてください。<ruby>または<rt>または</rt></ruby>、ファクスでもいいです。"
                        ]
                    },
                    {
                        "category_name": "7. <ruby>前<rt>まえ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>から<ruby>予想<rt>よそう</rt></ruby>されることと<ruby>違<rt>ちが</rt></ruby>うことを<ruby>言<rt>い</rt></ruby>う",
                        "category_en": "When an event or situation expected in a previous statement does not occur",
                        "conjunctions": ["だが", "ところが"],
                        "examples": [
                            "<ruby>家<rt>いえ</rt></ruby>に<ruby>電話<rt>でんわ</rt></ruby>をかけた。<ruby>だが<rt>だが</rt></ruby>、だれも<ruby>出<rt>で</rt></ruby>なかった。",
                            "<ruby>彼<rt>かれ</rt></ruby>はもう<ruby>空港<rt>くうこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いているはずだ。<ruby>ところが<rt>ところが</rt></ruby>、まだ<ruby>何<rt>なに</rt></ruby>も<ruby>連絡<rt>れんらく</rt></ruby>がない。"
                        ]
                    },
                    {
                        "category_name": "8. <ruby>条件<rt>じょうけん</rt></ruby>・<ruby>例外<rt>れいがい</rt></ruby>などを<ruby>加<rt>くわ</rt></ruby>える",
                        "category_en": "To express reservations or highlight a disadvantage about something, or to express conditionality or add exceptions",
                        "conjunctions": ["ただ", "ただし"],
                        "examples": [
                            "このアパートはとてもいい。<ruby>ただ<rt>ただ</rt></ruby>、<ruby>家賃<rt>やちん</rt></ruby>が<ruby>高<rt>たか</rt></ruby>い。",
                            "<ruby>試験<rt>しけん</rt></ruby>に<ruby>欠席<rt>けっせき</rt></ruby>したら<ruby>不合格<rt>ふごうかく</rt></ruby>だ。<ruby>ただし<rt>ただし</rt></ruby>、<ruby>特別<rt>とくべつ</rt></ruby>な<ruby>理由<rt>りゆう</rt></ruby>があれば<ruby>別<rt>べつ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>に<ruby>受<rt>う</rt></ruby>けられる。"
                        ]
                    },
                    {
                        "category_name": "9. <ruby>話題<rt>わだい</rt></ruby>を<ruby>変<rt>か</rt></ruby>える",
                        "category_en": "To change the subject",
                        "conjunctions": ["ところで"],
                        "examples": [
                            "いい<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>就職<rt>しゅうしょく</rt></ruby>が<ruby>決<rt>き</rt></ruby>まってよかったですね。<ruby>ところで<rt>ところで</rt></ruby>、ご<ruby>家族<rt>かぞく</rt></ruby>はお<ruby>元気<rt>げんき</rt></ruby>ですか。"
                        ]
                    }
                ]
            }
        ],
        "drills": [
            {
                "question_id": 30901,
                "category": "第3部 9課 練習",
                "question_type": "three_choice",
                "prompt": "1 ある<ruby>調査<rt>ちょうさ</rt></ruby>によると、<ruby>女性<rt>じょせい</rt></ruby>の<ruby>半分<rt>はんぶん</rt></ruby><ruby>以上<rt>いじょう</rt></ruby>が<ruby>結婚式<rt>けっこんしき</rt></ruby>をしたいと<ruby>考<rt>かんが</rt></ruby>えているそうだ。（a <ruby>一方<rt>いっぽう</rt></ruby>　b または　c さらに）、<ruby>男性<rt>だんせい</rt></ruby>はどちらでもいいという<ruby>人<rt>ひと</rt></ruby>が<ruby>多<rt>おお</rt></ruby>かった。",
                "options": ["a 一方", "b または", "c さらに"],
                "correct_answer": "a",
                "explanation_ja": "女性の傾向と男性の傾向を対比して述べているので「一方」（a）。",
                "explanation_en": "Contrasts females' views with males' views: '一方' (a)."
            },
            {
                "question_id": 30902,
                "category": "第3部 9課 練習",
                "question_type": "three_choice",
                "prompt": "2 <ruby>何度<rt>なんど</rt></ruby>もメールをしてみましたが、<ruby>見<rt>み</rt></ruby>ていないのか、<ruby>全<rt>まった</rt></ruby>く<ruby>返事<rt>へんじ</rt></ruby>が<ruby>来<rt>き</rt></ruby>ません。（a つまり　b そこで　c そのうえ）、<ruby>直接<rt>ちょくせつ</rt></ruby><ruby>電話<rt>でんわ</rt></ruby>をかけてみました。",
                "options": ["a つまり", "b そこで", "c そのうえ"],
                "correct_answer": "b",
                "explanation_ja": "返信が来ないという状況を受けて次の行動（電話）を起こすので「そこで」（b）。",
                "explanation_en": "Initiating the next action in response to no reply: 'そこで' (b)."
            },
            {
                "question_id": 30903,
                "category": "第3部 9課 練習",
                "question_type": "three_choice",
                "prompt": "3 ねこにとって<ruby>目<rt>め</rt></ruby>を<ruby>合<rt>あ</rt></ruby>わせることは「<ruby>敵<rt>てき</rt></ruby>」の<ruby>感情<rt>かんじょう</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていることを<ruby>意味<rt>いみ</rt></ruby>する。（a または　b それも　c したがって）、ねこが<ruby>横<rt>よこ</rt></ruby>を<ruby>向<rt>む</rt></ruby>くのは<ruby>逆<rt>ぎゃく</rt></ruby>に<ruby>親<rt>した</rt></ruby>しみを<ruby>表<rt>あらわ</rt></ruby>すと<ruby>考<rt>かんが</rt></ruby>えられる。",
                "options": ["a または", "b それも", "c したがって"],
                "correct_answer": "c",
                "explanation_ja": "前文の前提から論理的な結論を導くので「したがって」（c）。",
                "explanation_en": "Draws a logical conclusion from the preceding fact: 'したがって' (c)."
            },
            {
                "question_id": 30904,
                "category": "第3部 9課 練習",
                "question_type": "two_part_choice",
                "prompt": "4 <ruby>豆腐<rt>とうふ</rt></ruby>は<ruby>安<rt>やす</rt></ruby>くて<ruby>栄養<rt>えいよう</rt></ruby>が<ruby>豊富<rt>ほうふ</rt></ruby>です。（① a すると　b それに対して　c しかも）、いろいろな<ruby>料理<rt>りょうり</rt></ruby>に<ruby>使<rt>つか</rt></ruby>えます。（② a そのため　b ただし　c だが）、<ruby>日本人<rt>にほんじん</rt></ruby>の<ruby>食生活<rt>しょくせいかつ</rt></ruby>には<ruby>欠<rt>か</rt></ruby>かせない<ruby>食品<rt>しょくひん</rt></ruby>になっています。",
                "correct_answers": ["① c", "② a"],
                "explanation_ja": "①利点の追加：「しかも」（c）。②その理由・根拠による結果の結論：「そのため」（a）。",
                "explanation_en": "①Adding merit: 'しかも' (c). ②Resulting consequence: 'そのため' (a)."
            },
            {
                "question_id": 30905,
                "category": "第3部 9課 練習",
                "question_type": "three_part_choice",
                "prompt": "5 <ruby>若者<rt>わかもの</rt></ruby>は、いろいろなことに<ruby>興味<rt>きょうみ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ち、<ruby>何<rt>なん</rt></ruby>でもやってみるというイメージがある。（① a そのため　b ところが　c なぜなら）、<ruby>最近<rt>さいきん</rt></ruby><ruby>日本<rt>にほん</rt></ruby>の<ruby>若者<rt>わかもの</rt></ruby>が<ruby>外国<rt>がいこく</rt></ruby>に<ruby>関心<rt>かんしん</rt></ruby>を<ruby>持<rt>も</rt></ruby>たなくなったという<ruby>話<rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>く。<ruby>海外旅行<rt>かいがいりょこう</rt></ruby>や<ruby>海外留学<rt>かいがいりゅうがく</rt></ruby>をする<ruby>人<rt>ひと</rt></ruby>が<ruby>減<rt>へ</rt></ruby>っているというのだ。（② a だが　b または　c また）、<ruby>海外<rt>かいがい</rt></ruby>で<ruby>仕事<rt>しごと</rt></ruby>をしたいと<ruby>考<rt>かんが</rt></ruby>える<ruby>人<rt>ひと</rt></ruby>も<ruby>少<rt>すく</rt></ruby>なくなっているそうだ。（③ a すると　b ただ　c したがって）、<ruby>若者<rt>わかもの</rt></ruby>の<ruby>数<rt>かず</rt></ruby>そのものが<ruby>減<rt>へ</rt></ruby>っているし、<ruby>経済的<rt>けいざいてき</rt></ruby>、<ruby>社会的<rt>しゃかいてき</rt></ruby>な<ruby>問題<rt>もんだい</rt></ruby>もあると<ruby>考<rt>かんが</rt></ruby>えられるので、<ruby>単純<rt>たんじゅん</rt></ruby>に<ruby>若者<rt>わかもの</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>が<ruby>変<rt>か</rt></ruby>わったとは<ruby>言<rt>い</rt></ruby>えないかもしれない。",
                "correct_answers": ["① b", "② c", "③ b"],
                "explanation_ja": "①一般的なイメージと異なる実態：「ところが」（b）。②留学減少に加えて就職希望減少を追加：「また」（c）。③条件・補足を付加して単純な結論を留保：「ただ」（b）。",
                "explanation_en": "①Contrasts with common image: 'ところが' (b). ②Adding another declining trend: 'また' (c). ③Adding qualification/caveat: 'ただ' (b)."
            }
        ]
    }

    # =========================================================================
    # Lesson 10: 10課 文章の雰囲気の統一 (p. 142-143, Images 144-145)
    # =========================================================================
    sec10 = {
        "section_number": 10,
        "title": "<ruby>第<rt>だい</rt></ruby>10<ruby>課<rt>か</rt></ruby> <ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>雰囲気<rt>ふんいき</rt></ruby>の<ruby>統一<rt>とういつ</rt></ruby>",
        "title_en": "Lesson 10: Unifying the Tone and Register of a Text",
        "theme": "<ruby>文章全体<rt>ぶんしょうぜんたい</rt></ruby>を<ruby>同<rt>おな</rt></ruby>じ<ruby>雰囲気<rt>ふんいき</rt></ruby>にするために、<ruby>気楽<rt>きらく</rt></ruby>な<ruby>話<rt>はな</rt></ruby>し<ruby>言葉<rt>ことば</rt></ruby>と<ruby>硬<rt>かた</rt></ruby>い<ruby>言葉<rt>ことば</rt></ruby>をいっしょに<ruby>使<rt>つか</rt></ruby>いません。また、<ruby>文章全体<rt>ぶんしょうぜんたい</rt></ruby>を「<ruby>丁寧体<rt>ていねいたい</rt></ruby>（です・ます）」か「<ruby>普通体<rt>ふつうたい</rt></ruby>（だ／である）」に<ruby>統一<rt>とういつ</rt></ruby>します。",
        "theme_en": "In order to ensure a unified tone, casual and formal language are not used together. You should also adhere to a single register, whether using丁寧体 (です/ます) or 普通体 (だ/である) verb forms.",
        "points": [
            {
                "point_number": 1,
                "title": "レポートや<ruby>論文<rt>ろんぶん</rt></ruby>などの<ruby>硬<rt>かた</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>では、「<ruby>普通体<rt>ふつうたい</rt></ruby>（だ／である）」を<ruby>使<rt>つか</rt></ruby>います。また、<ruby>文<rt>ぶん</rt></ruby>を<ruby>続<rt>つづ</rt></ruby>けるとき、「て<ruby>形<rt>けい</rt></ruby>」のかわりに<ruby>連用中止形<rt>れんようちゅうしけい</rt></ruby>などを<ruby>使<rt>つか</rt></ruby>うことがあります。",
                "examples": [
                    "<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>説明<rt>せつめい</rt></ruby>を<ruby>読<rt>よ</rt></ruby>み、<ruby>例文<rt>れいぶん</rt></ruby>を<ruby>見<rt>み</rt></ruby>た<ruby>後<rt>あと</rt></ruby>で<ruby>練習問題<rt>れんしゅうもんだい</rt></ruby>を<ruby>解<rt>と</rt></ruby>き、<ruby>答<rt>こた</rt></ruby>えを<ruby>確認<rt>かくにん</rt></ruby>する。",
                    "この<ruby>地方<rt>ちほう</rt></ruby>はほとんど<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>らず、<ruby>昼<rt>ひる</rt></ruby>は<ruby>非常<rt>ひじょう</rt></ruby>に<ruby>暑<rt>あつ</rt></ruby>く、<ruby>夜<rt>よる</rt></ruby>は0<ruby>度<rt>ど</rt></ruby>まで<ruby>気温<rt>きおん</rt></ruby>が<ruby>下<rt>さ</rt></ruby>がる。",
                    "この<ruby>家具<rt>かぐ</rt></ruby>は<ruby>機械<rt>きかい</rt></ruby>を<ruby>使用<rt>しよう</rt></ruby>せず、<ruby>人<rt>ひと</rt></ruby>の<ruby>手<rt>て</rt></ruby>だけで<ruby>作<rt>つく</rt></ruby>られており、<ruby>温<rt>あたた</rt></ruby>かみが<ruby>感<rt>かん</rt></ruby>じられる。"
                ]
            },
            {
                "point_number": 2,
                "title": "<ruby>硬<rt>かた</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>では、ふつうくだけた<ruby>形<rt>かたち</rt></ruby>を<ruby>使<rt>つか</rt></ruby>ったり<ruby>助詞<rt>じょし</rt></ruby>を<ruby>省略<rt>しょうりゃく</rt></ruby>したりしません。",
                "examples": [
                    "× 詳しいこと調べてみなきゃ、結論出せないんじゃない？",
                    "○ 詳しいことを調べてみなければ、結論は出せないのではないか。"
                ]
            },
            {
                "point_number": 3,
                "title": "<ruby>硬<rt>かた</rt></ruby>い<ruby>文章<rt>ぶんしょう</rt></ruby>でよく<ruby>使<rt>つか</rt></ruby>う<ruby>表現<rt>ひょうげん</rt></ruby>と<ruby>日常会話<rt>にちじょうかいわ</rt></ruby>の<ruby>対比<rt>たいひ</rt></ruby>",
                "register_table": [
                    {"category": "副詞・形容詞", "formal": "非常に・大変", "casual": "すごく", "example": "この計画は非常に困難だ。"},
                    {"category": "副詞・形容詞", "formal": "多く・大勢", "casual": "いっぱい", "example": "この食品はビタミンCを多く含む。"},
                    {"category": "副詞・形容詞", "formal": "少し", "casual": "ちょっと", "example": "言葉は少しずつ変化している。"},
                    {"category": "副詞・形容詞", "formal": "やはり", "casual": "やっぱり", "example": "やはり実験は成功しなかった。"},
                    {"category": "副詞・形容詞", "formal": "さまざまな・いろいろな", "casual": "いろんな", "example": "さまざまな考え方がある。"},
                    {"category": "動詞", "formal": "述べる・話す・言う", "casual": "しゃべる", "example": "これからこの物質の特徴を述べる。"},
                    {"category": "動詞", "formal": "行う", "casual": "やる", "example": "大統領選挙は7月に行われた。"},
                    {"category": "接続表現", "formal": "しかし・だが", "casual": "でも・だけど", "example": "これは難しい。だが、挑戦しよう。"},
                    {"category": "疑問詞", "formal": "なぜ", "casual": "なんで", "example": "なぜ我々は働くのだろうか。"},
                    {"category": "助詞", "formal": "〜など", "casual": "なんか", "example": "金属には金や銀などがある。"},
                    {"category": "その他の表現", "formal": "〜と・〜という・〜そうだ", "casual": "〜って", "example": "それは事故だという。"},
                    {"category": "その他の表現", "formal": "〜ようだ・〜らしい", "casual": "〜みたいだ", "example": "彼の言葉は真実ではないようだ。"}
                ]
            }
        ],
        "drills": [
            {
                "question_id": 31001,
                "category": "第3部 10課 練習",
                "question_type": "text_correction",
                "prompt": "<ruby>多<rt>おお</rt></ruby>くの<ruby>外国人<rt>がいこくじん</rt></ruby>にとって<ruby>東京<rt>とうきょう</rt></ruby>のイメージは、どこへ<ruby>行<rt>い</rt></ruby>っても<ruby>人<rt>ひと</rt></ruby>が①いっぱいいて、<ruby>高<rt>たか</rt></ruby>いビルが②すごく<ruby>多<rt>おお</rt></ruby>い<ruby>大都市<rt>だいとし</rt></ruby>だ。③っていうものであろう。④だけど、<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>てみると、その<ruby>考<rt>かんが</rt></ruby>えは⑤ちょっと<ruby>変<rt>か</rt></ruby>わる。<ruby>確<rt>たし</rt></ruby>かに<ruby>東京<rt>とうきょう</rt></ruby>は<ruby>大都市<rt>だいとし</rt></ruby>だが、<ruby>都会的<rt>とかいてき</rt></ruby>な<ruby>場所<rt>ばしょ</rt></ruby>だけではなく、<ruby>林<rt>はやし</rt></ruby>や<ruby>畑<rt>はたけ</rt></ruby>⑥なんか⑦の<ruby>自然<rt>しぜん</rt></ruby>も<ruby>目<rt>め</rt></ruby>にすることが⑧できます。このようなことはテレビを<ruby>見<rt>み</rt></ruby>るだけ⑨じゃわからない。⑩やっぱり<ruby>実際<rt>じっさい</rt></ruby>に<ruby>住<rt>す</rt></ruby>み、⑪いろんな<ruby>所<rt>ところ</rt></ruby>を<ruby>見<rt>み</rt></ruby>てはじめてわかること⑫なんじゃないでしょうか。",
                "corrections": [
                    {"index": "①", "target": "いっぱいいて", "replacement": "大勢／多く", "furigana": "<ruby>大勢<rt>おおぜい</rt></ruby>／<ruby>多<rt>おお</rt></ruby>く"},
                    {"index": "②", "target": "すごく", "replacement": "非常に／大変", "furigana": "<ruby>非常<rt>ひじょう</rt></ruby>に／<ruby>大変<rt>たいへん</rt></ruby>"},
                    {"index": "③", "target": "っていう", "replacement": "と"},
                    {"index": "④", "target": "だけど", "replacement": "しかし／だが"},
                    {"index": "⑤", "target": "ちょっと", "replacement": "少し", "furigana": "<ruby>少<rt>すこ</rt></ruby>し"},
                    {"index": "⑥", "target": "なんか", "replacement": "など"},
                    {"index": "⑦", "target": "できます", "replacement": "できる"},
                    {"index": "⑧", "target": "じゃ", "replacement": "では"},
                    {"index": "⑨", "target": "やっぱり", "replacement": "やはり"},
                    {"index": "⑩", "target": "いろんな", "replacement": "いろいろな／さまざまな"},
                    {"index": "⑪", "target": "なんじゃ", "replacement": "なのでは"},
                    {"index": "⑫", "target": "ないでしょうか", "replacement": "ないだろうか"}
                ],
                "explanation_ja": "解答冊子p.7参照：①大勢／多く ②非常に／大変 ③と ④しかし／だが ⑤少し ⑥など ⑦できる ⑧では ⑨やはり ⑩いろいろな／さまざまな ⑪なのでは ⑫ないだろうか。",
                "explanation_en": "See Answer booklet p.7: Formal register replacements for colloquial/spoken words in a written essay."
            }
        ]
    }

    # =========================================================================
    # Review Test 9-10: まとめ問題 (9課・10課) (p. 144-145, Images 146-147)
    # =========================================================================
    matome_9_10 = {
        "section_number": 10.5,
        "title": "まとめ<ruby>問題<rt>もんだい</rt></ruby>（9<ruby>課<rt>か</rt></ruby>・10<ruby>課<rt>か</rt></ruby>）",
        "title_en": "Review Exercises (Lessons 9 & 10)",
        "theme": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>総合練習<rt>そうごうれんしゅう</rt></ruby>（接続表現と文章の雰囲気）",
        "theme_en": "Comprehensive text grammar review: Conjunctions and consistency of style/register",
        "passages": [
            {
                "passage_id": 309,
                "title": "家族の卵料理",
                "title_en": "Family Egg Cooking",
                "text": "わたしは<ruby>料理<rt>りょうり</rt></ruby>が<ruby>大好<rt>だいす</rt></ruby>きで、<ruby>自分<rt>じぶん</rt></ruby>の<ruby>息子<rt>むすこ</rt></ruby>たちにも<ruby>小<rt>ちい</rt></ruby>さいころから<ruby>料理<rt>りょうり</rt></ruby>を［ 1 ］。ある<ruby>日<rt>ひ</rt></ruby>、<ruby>息子<rt>むすこ</rt></ruby>が<ruby>一人<rt>ひとり</rt></ruby>で<ruby>家族<rt>かぞく</rt></ruby>のために<ruby>卵<rt>たまご</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ってくれた。わたしたちは<ruby>喜<rt>よろこ</rt></ruby>んでさっそく<ruby>一口<rt>ひとくち</rt></ruby><ruby>食<rt>た</rt></ruby>べてみた。［ 2 ］、そのおいしそうな<ruby>料理<rt>りょうり</rt></ruby>は、とても<ruby>辛<rt>から</rt></ruby>かった。<ruby>息子<rt>むすこ</rt></ruby>がトマトケチャップだと<ruby>思<rt>おも</rt></ruby>って<ruby>入<rt>い</rt></ruby>れたのは、<ruby>実<rt>じつ</rt></ruby>は<ruby>辛<rt>から</rt></ruby>いソースだったのだ。<ruby>息子<rt>むすこ</rt></ruby>は<ruby>泣<rt>な</rt></ruby>きそうな<ruby>顔<rt>かお</rt></ruby>をしていた。わたしは、「この<ruby>子<rt>こ</rt></ruby>が<ruby>家族<rt>かぞく</rt></ruby>を<ruby>喜<rt>よろこ</rt></ruby>ばせようと<ruby>思<rt>おも</rt></ruby>ってしたことなのだから、その<ruby>気持<rt>きも</rt></ruby>ちは<ruby>絶対<rt>ぜったい</rt></ruby>に<ruby>無駄<rt>むだ</rt></ruby>にしたくない」と<ruby>思<rt>おも</rt></ruby>った。［ 3 ］、その<ruby>辛<rt>から</rt></ruby>い<ruby>料理<rt>りょうり</rt></ruby>を<ruby>使<rt>つか</rt></ruby>って<ruby>新<rt>あたら</rt></ruby>しい<ruby>料理<rt>りょうり</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ることにした。「<ruby>失敗<rt>しっぱい</rt></ruby>は<ruby>悪<rt>わる</rt></ruby>いことじゃないよ。それに、これは<ruby>失敗<rt>しっぱい</rt></ruby>ではなくて、まだ<ruby>途中<rt>とちゅう</rt></ruby>なんだから」と<ruby>言<rt>い</rt></ruby>いながらスープを［ 4 ］、その<ruby>卵料理<rt>たまごりょうり</rt></ruby>を<ruby>入<rt>い</rt></ruby>れてみた。すると、ふつうのスープが<ruby>本当<rt>ほんとう</rt></ruby>においしいスープに<ruby>変<rt>か</rt></ruby>わった。<ruby>息子<rt>むすこ</rt></ruby>も［ 5 ］。\n参考：青木祐人・青木のぞ美『ゆうとくんちのしあわせごはん』宮帯出版社",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 30901,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　されている",
                            "2　させている",
                            "3　してきた",
                            "4　させられてきた"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "親が息子に料理をさせる使役「料理をさせている」。2が正解。",
                        "explanation_en": "Causative form (allowing/making children cook): 'させている'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 30902,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　ところが",
                            "2　ところで",
                            "3　つまり",
                            "4　しかも"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "喜んで一口食べた予想と異なり、辛かったという意外な展開なので「ところが」。1が正解。",
                        "explanation_en": "Contrasts with expectations of deliciousness: 'ところが'. Choice 1 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 30903,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　さらに",
                            "2　また",
                            "3　そこで",
                            "4　ただ"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "息子の気持ちを無駄にしたくないという思いから次の行動を起こすので「そこで」。3が正解。",
                        "explanation_en": "Prompting a new action in response: 'そこで'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 30904,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　作ったので",
                            "2　作ったが",
                            "3　作った",
                            "4　作り"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "文章の連用中止形（硬い・整った文体）で文をつなぐ「スープを作り、その卵料理を入れてみた」。4が正解。",
                        "explanation_en": "Formal written continuative stem (連用中止): 'スープを作り'. Choice 4 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 30905,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　笑顔になったんだ",
                            "2　笑顔になっていた",
                            "3　笑顔を見ていた",
                            "4　笑顔を見たんだ"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "客観的な記述文体（普通体過去）で結果の状態を表す「笑顔になっていた」。2が正解。",
                        "explanation_en": "Objective descriptive past result: '笑顔になっていた'. Choice 2 is correct."
                    }
                ]
            },
            {
                "passage_id": 310,
                "title": "100年前と今",
                "title_en": "100 Years Ago and Today",
                "text": "100<ruby>年前<rt>ねんまえ</rt></ruby>と<ruby>今<rt>いま</rt></ruby>\nリュウ エイ\n\n100<ruby>年前<rt>ねんまえ</rt></ruby>と<ruby>今<rt>いま</rt></ruby>とを<ruby>比<rt>くら</rt></ruby>べると、いろいろなことが<ruby>変<rt>か</rt></ruby>わってきた。<ruby>今<rt>いま</rt></ruby>、わたしたちはさまざまな<ruby>技術<rt>ぎじゅつ</rt></ruby>のおかげで、<ruby>便利<rt>べんり</rt></ruby>な<ruby>生活<rt>せいかつ</rt></ruby>を<ruby>送<rt>おく</rt></ruby>っている。［ 1 ］、<ruby>人<rt>ひと</rt></ruby>の<ruby>心<rt>こころ</rt></ruby>も<ruby>昔<rt>むかし</rt></ruby>よりよくなったと<ruby>言<rt>い</rt></ruby>えるだろうか。\n<ruby>例<rt>たと</rt></ruby>えば、<ruby>今<rt>いま</rt></ruby>はお<ruby>金<rt>かね</rt></ruby>さえ<ruby>払<rt>はら</rt></ruby>えばいつでも<ruby>自分<rt>じぶん</rt></ruby>の<ruby>食<rt>た</rt></ruby>べたい<ruby>物<rt>もの</rt></ruby>が<ruby>買<rt>か</rt></ruby>えるので、<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>のありがたみがわからなくなってきている。［ 2 ］、<ruby>昔<rt>むかし</rt></ruby>は<ruby>今<rt>いま</rt></ruby>より<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>を<ruby>手<rt>て</rt></ruby>に<ruby>入<rt>い</rt></ruby>れることが<ruby>難<rt>むずか</rt></ruby>しかった。そのため、<ruby>今<rt>いま</rt></ruby>よりもずっと<ruby>感謝<rt>かんしゃ</rt></ruby>の<ruby>心<rt>こころ</rt></ruby>を<ruby>持<rt>も</rt></ruby>っていたはずだ。\nまた、<ruby>今<rt>いま</rt></ruby>は、<ruby>通信手段<rt>つうしんしゅだん</rt></ruby>が<ruby>発達<rt>はったつ</rt></ruby>してきて、<ruby>人<rt>ひと</rt></ruby>と［ 3 ］コミュニケーションが<ruby>取<rt>と</rt></ruby>れるようになった。<ruby>便利<rt>べんり</rt></ruby>にはなったが、その<ruby>分<rt>ぶん</rt></ruby>、<ruby>心<rt>こころ</rt></ruby>の<ruby>距離<rt>きょり</rt></ruby>は<ruby>遠<rt>とお</rt></ruby>くなってしまった。<ruby>昔<rt>むかし</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は、いつも<ruby>相手<rt>あいて</rt></ruby>と<ruby>直接<rt>ちょくせつ</rt></ruby><ruby>会<rt>あ</rt></ruby>って［ 4 ］、<ruby>今<rt>いま</rt></ruby>よりも<ruby>親<rt>した</rt></ruby>しい<ruby>関係<rt>かんけい</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ることができていたのではないだろうか。\n<ruby>今<rt>いま</rt></ruby>のわたしたちも、<ruby>昔<rt>むかし</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>のように<ruby>感謝<rt>かんしゃ</rt></ruby>の<ruby>心<rt>こころ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ち、もっと<ruby>人間関係<rt>にんげんかんけい</rt></ruby>を<ruby>大切<rt>たいせつ</rt></ruby>にすれば、100<ruby>年前<rt>ねんまえ</rt></ruby>と<ruby>同<rt>おな</rt></ruby>じような<ruby>心豊<rt>こころゆた</rt></ruby>かな<ruby>生活<rt>せいかつ</rt></ruby>が<ruby>送<rt>おく</rt></ruby>れるように［ 5 ］と<ruby>思<rt>おも</rt></ruby>う。",
                "questions": [
                    {
                        "blank_number": 1,
                        "question_id": 31001,
                        "prompt": "［ 1 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　すると",
                            "2　それから",
                            "3　しかし",
                            "4　しかも"
                        ],
                        "correct_answer": 3,
                        "explanation_ja": "技術が便利になったことに対し、「しかし人の心も良くなったと言えるだろうか」と逆接の問題提起をする。「しかし」（3）が正解。",
                        "explanation_en": "Raises a counter-question to technological advancement: 'しかし'. Choice 3 is correct."
                    },
                    {
                        "blank_number": 2,
                        "question_id": 31002,
                        "prompt": "［ 2 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　または",
                            "2　一方",
                            "3　ただ",
                            "4　それに"
                        ],
                        "correct_answer": 2,
                        "explanation_ja": "現在の状況と対比して過去の状況を述べるので「一方」（2）が正解。",
                        "explanation_en": "Contrasts the present situation with the past: '一方'. Choice 2 is correct."
                    },
                    {
                        "blank_number": 3,
                        "question_id": 31003,
                        "prompt": "［ 3 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　会わずに",
                            "2　会えず",
                            "3　会えなく",
                            "4　会わなくなり"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "通信手段の発達により直接顔を合わせないでコミュニケーションが取れるので「会わずに」（1）が正解。",
                        "explanation_en": "'会わずに' (without meeting in person). Choice 1 is correct."
                    },
                    {
                        "blank_number": 4,
                        "question_id": 31004,
                        "prompt": "［ 4 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　話していたのが",
                            "2　話していたけど",
                            "3　話していたのに",
                            "4　話していたので"
                        ],
                        "correct_answer": 4,
                        "explanation_ja": "直接会って話していたことが親しい関係を築けた理由なので「話していたので」（4）が正解。",
                        "explanation_en": "Expresses the reason: '話していたので' (because they talked face-to-face). Choice 4 is correct."
                    },
                    {
                        "blank_number": 5,
                        "question_id": 31005,
                        "prompt": "［ 5 ］に<ruby>入<rt>はい</rt></ruby>るもの",
                        "options": [
                            "1　なるのではないか",
                            "2　なるのではないかな",
                            "3　なるのではないだろう",
                            "4　なるのではないでしょう"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "論説文（論文体・硬い文章）における自説の提示「〜なるのではないかと思う」。「なるのではないか」（1）が正解。",
                        "explanation_en": "Formal essay conclusion expression: 'なるのではないか'. Choice 1 is correct."
                    }
                ]
            }
        ]
    }

    return [sec9, sec10, matome_9_10]
