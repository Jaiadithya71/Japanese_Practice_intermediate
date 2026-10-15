"""
Module 2 for Part 2 Sentence Grammar 2 Builder:
Part 2 Lessons 1 through 4 and Review Test 1-4 (Images 106-116, p. 102-113).
"""

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

def get_part2_lessons_sections():
    sections = []

    # =========================================================================
    # Section 7: Part 2 Lesson 1 (第1課 文の組み立て-1 引用) p. 102-104
    # =========================================================================
    sec7 = {
        "section_number": 7,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>1<ruby>課<rt>か</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>みたて-1 <ruby>引用<rt>いんよう</rt></ruby>",
        "title_en": "Part 2 Lesson 1: Sentence Composition 1 - Quotation",
        "theme": "「〜と」「〜ように」などの引用節を含む文の組み立て",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "引用の「〜と / 〜ように」",
                "pattern_name_en": "Quotative 'to / you ni'",
                "meaning_ja": "発言や思考内容を引用して文を組み立てる。",
                "meaning_en": "Assembling sentences by quoting statements, thoughts, or indirect requests.",
                "connection_forms": ["普通形 + と（言う/思う/聞く等）", "V-辞書形/V-ない形 + ように（言う/頼む等）"],
                "nuance_notes": "間接疑問文（〜かどうか、〜か）や伝聞・指示の引用節の配置順序に注意する。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>授業中<rt>じゅぎょうちゅう</rt></ruby>は<ruby>寝<rt>ね</rt></ruby>るなと<ruby>言<rt>い</rt></ruby>われた。",
                        "english": "I was told by the teacher not to sleep during class."
                    }
                ]
            }
        ],
        "drills": [
            make_star(
                701, "Part2 1課 練習",
                "<ruby>今度<rt>こんど</rt></ruby>の<ruby>旅行<rt>りょこう</rt></ruby>について　＿＿＿　＿＿＿　＿★＿　＿＿＿　お<ruby>返事<rt>へんじ</rt></ruby>をください。",
                ["1　<ruby>計画<rt>けいかく</rt></ruby>で", "2　このような", "3　どうか", "4　いいか"],
                [2, 1, 4, 3], 3, 4,
                "<ruby>今度<rt>こんど</rt></ruby>の<ruby>旅行<rt>りょこう</rt></ruby>についてこのような<ruby>計画<rt>けいかく</rt></ruby>でいいかどうかお<ruby>返事<rt>へんじ</rt></ruby>をください。",
                "Please reply whether this plan for the upcoming trip is okay or not.",
                "「このような計画で」（2→1）、「いいかどうか」（4→3）。全体で「このような計画でいいかどうか」となり、★には 4 が入る。",
                "'このような計画で' (2->1), 'いいかどうか' (4->3). Correct order is 2-1-4-3. Star is 4."
            ),
            make_star(
                702, "Part2 1課 練習",
                "<ruby>危<rt>あぶ</rt></ruby>ないから　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>子<rt>こ</rt></ruby>どもたちに<ruby>注意<rt>ちゅうい</rt></ruby>した。",
                ["1　<ruby>並<rt>なら</rt></ruby>んで", "2　<ruby>横<rt>よこ</rt></ruby>に", "3　ように", "4　<ruby>歩<rt>ある</rt></ruby>かない"],
                [2, 1, 4, 3], 3, 4,
                "<ruby>危<rt>あぶ</rt></ruby>ないから<ruby>横<rt>よこ</rt></ruby>に<ruby>並<rt>なら</rt></ruby>んで<ruby>歩<rt>ある</rt></ruby>かないように<ruby>子<rt>こ</rt></ruby>どもたちに<ruby>注意<rt>ちゅうい</rt></ruby>した。",
                "I warned the children not to walk side by side because it is dangerous.",
                "「横に並んで」（2→1）、「歩かないように」（4→3）。順序は 2→1→4→3。★には 4 が入る。",
                "'横に並んで' (2->1), '歩かないように' (4->3). Order is 2-1-4-3. Star is 4."
            ),
            make_star(
                703, "Part2 1課 練習",
                "どうすれば<ruby>入<rt>はい</rt></ruby>りたい　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>聞<rt>き</rt></ruby>いてみたい。",
                ["1　<ruby>会社<rt>かいしゃ</rt></ruby>に", "2　<ruby>先輩<rt>せんぱい</rt></ruby>に", "3　<ruby>入<rt>はい</rt></ruby>れる", "4　か"],
                [1, 3, 4, 2], 3, 4,
                "どうすれば<ruby>入<rt>はい</rt></ruby>りたい<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>れるか<ruby>先輩<rt>せんぱい</rt></ruby>に<ruby>聞<rt>き</rt></ruby>いてみたい。",
                "I want to ask my senior how I can get into the company I want to join.",
                "「入りたい会社に」（1）「入れるか」（3→4）「先輩に聞いてみたい」（2）。順序は 1→3→4→2。★には 4 が入る。",
                "'入りたい会社に入れるか' (1->3->4) '先輩に' (2). Order is 1-3-4-2. Star is 4."
            ),
            make_star(
                704, "Part2 1課 練習",
                "<ruby>今年<rt>ことし</rt></ruby>こそ　＿＿＿　＿＿＿　＿★＿　＿＿＿　と<ruby>思<rt>おも</rt></ruby>う。",
                ["1　<ruby>行<rt>い</rt></ruby>きたかった", "2　<ruby>行<rt>い</rt></ruby>こう", "3　ヨーロッパに", "4　<ruby>前<rt>まえ</rt></ruby>から"],
                [4, 1, 3, 2], 3, 3,
                "<ruby>今年<rt>ことし</rt></ruby>こそ<ruby>前<rt>まえ</rt></ruby>から<ruby>行<rt>い</rt></ruby>きたかったヨーロッパに<ruby>行<rt>い</rt></ruby>こうと<ruby>思<rt>おも</rt></ruby>う。",
                "This year, I think I will go to Europe, where I have wanted to go for a long time.",
                "「前から行きたかった」（4→1）がヨーロッパを修飾。「ヨーロッパに行こうと思う」（3→2）。順序は 4→1→3→2。★には 3 が入る。",
                "'前から行きたかった' (4->1) modifies 'ヨーロッパに' (3), followed by '行こう' (2). Order is 4-1-3-2. Star is 3."
            ),
            make_star(
                705, "Part2 1課 練習",
                "リンさんは、<ruby>自分<rt>じぶん</rt></ruby>がアルバイトで　＿＿＿　＿＿＿　＿★＿　＿＿＿　と<ruby>言<rt>い</rt></ruby>った。",
                ["1　<ruby>食<rt>た</rt></ruby>べに", "2　<ruby>働<rt>はたら</rt></ruby>いている", "3　<ruby>来<rt>き</rt></ruby>てほしい", "4　<ruby>店<rt>みせ</rt></ruby>に"],
                [2, 4, 1, 3], 3, 1,
                "リンさんは、<ruby>自分<rt>じぶん</rt></ruby>がアルバイトで<ruby>働<rt>はたら</rt></ruby>いている<ruby>店<rt>みせ</rt></ruby>に<ruby>食<rt>た</rt></ruby>べに<ruby>来<rt>き</rt></ruby>てほしいと<ruby>言<rt>い</rt></ruby>った。",
                "Lin said she wants us to come eat at the shop where she works part-time.",
                "「働いている店に」（2→4）、「食べに来てほしい」（1→3）。順序は 2→4→1→3。★には 1 が入る。",
                "'働いている店に' (2->4), '食べに来てほしい' (1->3). Order is 2-4-1-3. Star is 1."
            ),
            make_star(
                706, "Part2 1課 練習",
                "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>授業中<rt>じゅぎょうちゅう</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　どうしても<ruby>寝<rt>ね</rt></ruby>てしまう。",
                ["1　と", "2　<ruby>言<rt>い</rt></ruby>われても", "3　<ruby>寝<rt>ね</rt></ruby>るな", "4　つまらないと"],
                [3, 1, 2, 4], 3, 2,
                "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>授業中<rt>じゅぎょうちゅう</rt></ruby>は<ruby>寝<rt>ね</rt></ruby>るなと<ruby>言<rt>い</rt></ruby>われても、つまらないとどうしても<ruby>寝<rt>ね</rt></ruby>てしまう。",
                "Even if the teacher tells me not to sleep during class, if it's boring I end up sleeping anyway.",
                "「寝るなと言われても」（3→1→2）、「つまらないと」（4）。順序は 3→1→2→4。★には 2 が入る。",
                "'寝るなと言われても' (3->1->2), 'つまらないと' (4). Order is 3-1-2-4. Star is 2."
            ),
            make_star(
                707, "Part2 1課 練習",
                "<ruby>山田<rt>やまだ</rt></ruby>さんに　＿＿＿　＿＿＿　＿★＿　＿＿＿　と<ruby>聞<rt>き</rt></ruby>かれた。",
                ["1　ほしいの", "2　どれか", "3　いちばん", "4　は"],
                [3, 1, 4, 2], 3, 4,
                "<ruby>山田<rt>やまだ</rt></ruby>さんにいちばんほしいのはどれかと<ruby>聞<rt>き</rt></ruby>かれた。",
                "Yamada asked me which one I wanted the most.",
                "「いちばんほしいのは」（3→1→4）、「どれかと」（2）。順序は 3→1→4→2。★には 4 が入る。",
                "'いちばんほしいのは' (3->1->4), 'どれか' (2). Order is 3-1-4-2. Star is 4."
            ),
            make_star(
                708, "Part2 1課 練習",
                "どうして　＿＿＿　＿＿＿　＿★＿　＿＿＿　やり<ruby>方<rt>かた</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えていたからだ。",
                ["1　というと", "2　ように", "3　<ruby>言<rt>い</rt></ruby>われたか", "4　やり<ruby>直<rt>なお</rt></ruby>す"],
                [4, 2, 3, 1], 3, 3,
                "どうしてやり<ruby>直<rt>なお</rt></ruby>すように<ruby>言<rt>い</rt></ruby>われたかというと、やり<ruby>方<rt>かた</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えていたからだ。",
                "If you ask why I was told to redo it, it's because I made a mistake in the method.",
                "「やり直すように言われたかというと」（4→2→3→1）。順序は 4→2→3→1。★には 3 が入る。",
                "'やり直すように言われたかというと' (4->2->3->1). Order is 4-2-3-1. Star is 3."
            ),
            make_star(
                709, "Part2 1課 練習",
                "<ruby>店長<rt>てんちょう</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　と<ruby>言<rt>い</rt></ruby>われた。",
                ["1　<ruby>言<rt>い</rt></ruby>え", "2　そう", "3　<ruby>休<rt>やす</rt></ruby>みたい", "4　なら"],
                [3, 4, 2, 1], 3, 2,
                "<ruby>店長<rt>てんちょう</rt></ruby>に<ruby>休<rt>やす</rt></ruby>みたいならそう<ruby>言<rt>い</rt></ruby>えと<ruby>言<rt>い</rt></ruby>われた。",
                "The store manager told me: 'If you want to take time off, just say so.'",
                "「休みたいなら」（3→4）、「そう言えと」（2→1）。順序は 3→4→2→1。★には 2 が入る。",
                "'休みたいならそう言え' (3->4->2->1). Order is 3-4-2-1. Star is 2."
            ),
            make_star(
                710, "Part2 1課 練習",
                "いつごろからこの<ruby>言葉<rt>ことば</rt></ruby>が　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>調<rt>しら</rt></ruby>べてみた。",
                ["1　なった", "2　<ruby>使<rt>つか</rt></ruby>われる", "3　か", "4　ように"],
                [2, 4, 1, 3], 3, 1,
                "いつごろからこの<ruby>言葉<rt>ことば</rt></ruby>が<ruby>使<rt>つか</rt></ruby>われるようになったか<ruby>調<rt>しら</rt></ruby>べてみた。",
                "I looked into when this word came to be used.",
                "「使われるようになったか」（2→4→1→3）。順序は 2→4→1→3。★には 1 が入る。",
                "'使われるようになったか' (2->4->1->3). Order is 2-4-1-3. Star is 1."
            )
        ]
    }
    sections.append(sec7)

    # =========================================================================
    # Section 8: Part 2 Lesson 2 (第2課 文の組み立て-2 名詞の説明) p. 105-106
    # =========================================================================
    sec8 = {
        "section_number": 8,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>2<ruby>課<rt>か</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>みたて-2 <ruby>名詞<rt>めいし</rt></ruby>の<ruby>説明<rt>せつめい</rt></ruby>",
        "title_en": "Part 2 Lesson 2: Sentence Composition 2 - Modifying Nouns",
        "theme": "連体修飾節（名詞修飾）の構造と組み立て",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "名詞修飾の構造",
                "pattern_name_en": "Noun Modification Structure",
                "meaning_ja": "動詞句や複文によって名詞を詳しく説明する構文。",
                "meaning_en": "Structures where relative clauses or complex phrases modify a noun.",
                "connection_forms": ["動詞普通形 / イ形容詞 / ナ形容詞+な / 名詞+の + 名詞"],
                "nuance_notes": "修飾節内の主語は「が」で表されることに注意。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>魚<rt>さかな</rt></ruby>が<ruby>焼<rt>や</rt></ruby>けるいい<ruby>匂<rt>にお</rt></ruby>いがしてきた。",
                        "english": "A nice smell of fish grilling came wafting over."
                    }
                ]
            }
        ],
        "drills": [
            make_star(
                801, "Part2 2課 練習",
                "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>いていたら、どこからか　＿＿＿　＿＿＿　＿★＿　＿＿＿　きた。",
                ["1　<ruby>魚<rt>さかな</rt></ruby>が", "2　いい<ruby>匂<rt>にお</rt></ruby>いが", "3　<ruby>焼<rt>や</rt></ruby>ける", "4　して"],
                [1, 3, 2, 4], 3, 2,
                "<ruby>海岸<rt>かいがん</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>いていたら、どこからか<ruby>魚<rt>さかな</rt></ruby>が<ruby>焼<rt>や</rt></ruby>けるいい<ruby>匂<rt>にお</rt></ruby>いがしてきた。",
                "While walking along the shore, a nice smell of grilled fish came wafting from somewhere.",
                "「魚が焼けるいい匂いがして」（1→3→2→4）。順序は 1→3→2→4。★には 2 が入る。",
                "'魚が焼けるいい匂いがして' (1->3->2->4). Order is 1-3-2-4. Star is 2."
            ),
            make_star(
                802, "Part2 2課 練習",
                "<ruby>読<rt>よ</rt></ruby>む　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>多<rt>おお</rt></ruby>くはない。",
                ["1　<ruby>本<rt>ほん</rt></ruby>は", "2　<ruby>感動<rt>かんどう</rt></ruby>する", "3　たびに", "4　あまり"],
                [3, 2, 1, 4], 3, 1,
                "<ruby>読<rt>よ</rt></ruby>むたびに<ruby>感動<rt>かんどう</rt></ruby>する<ruby>本<rt>ほん</rt></ruby>はあまり<ruby>多<rt>おお</rt></ruby>くはない。",
                "Books that move me every time I read them are not very numerous.",
                "「読むたびに感動する本はあまり」（3→2→1→4）。順序は 3→2→1→4。★には 1 が入る。",
                "'読むたびに感動する本はあまり' (3->2->1->4). Order is 3-2-1-4. Star is 1."
            ),
            make_star(
                803, "Part2 2課 練習",
                "ここに　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>紹介<rt>しょうかい</rt></ruby>されている。",
                ["1　<ruby>若<rt>わか</rt></ruby>い", "2　<ruby>作品<rt>さくひん</rt></ruby>が", "3　よる", "4　デザイナーたちに"],
                [1, 4, 3, 2], 3, 3,
                "ここに<ruby>若<rt>わか</rt></ruby>いデザイナーたちによる<ruby>作品<rt>さくひん</rt></ruby>が<ruby>紹介<rt>しょうかい</rt></ruby>されている。",
                "Works by young designers are introduced here.",
                "「若いデザイナーたちによる作品が」（1→4→3→2）。順序は 1→4→3→2。★には 3 が入る。",
                "'若いデザイナーたちによる作品が' (1->4->3->2). Order is 1-4-3-2. Star is 3."
            ),
            make_star(
                804, "Part2 2課 練習",
                "きのう　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>目<rt>め</rt></ruby>が<ruby>見<rt>み</rt></ruby>えないみたいだ。",
                ["1　<ruby>子<rt>こ</rt></ruby>ねこは", "2　<ruby>生<rt>う</rt></ruby>まれた", "3　まだ", "4　ばかりの"],
                [2, 4, 1, 3], 3, 1,
                "きのう<ruby>生<rt>う</rt></ruby>まれたばかりの<ruby>子<rt>こ</rt></ruby>ねこはまだ<ruby>目<rt>め</rt></ruby>が<ruby>見<rt>み</rt></ruby>えないみたいだ。",
                "The kittens born just yesterday seem unable to see yet.",
                "「生まれたばかりの子ねこはまだ」（2→4→1→3）。順序は 2→4→1→3。★には 1 が入る。",
                "'生まれたばかりの子ねこはまだ' (2->4->1->3). Order is 2-4-1-3. Star is 1."
            ),
            make_star(
                805, "Part2 2課 練習",
                "<ruby>私<rt>わたし</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>残念<rt>ざんねん</rt></ruby>だ。",
                ["1　あの<ruby>人<rt>ひと</rt></ruby>と", "2　<ruby>約束<rt>やくそく</rt></ruby>を", "3　<ruby>守<rt>まも</rt></ruby>れなくて", "4　の"],
                [1, 4, 2, 3], 3, 2,
                "<ruby>私<rt>わたし</rt></ruby>はあの<ruby>人<rt>ひと</rt></ruby>との<ruby>約束<rt>やくそく</rt></ruby>を<ruby>守<rt>まも</rt></ruby>れなくて<ruby>残念<rt>ざんねん</rt></ruby>だ。",
                "I regret that I couldn't keep my promise with that person.",
                "「あの人との約束を守れなくて」（1→4→2→3）。順序は 1→4→2→3。★には 2 が入る。",
                "'あの人との約束を守れなくて' (1->4->2->3). Order is 1-4-2-3. Star is 2."
            ),
            make_star(
                806, "Part2 2課 練習",
                "<ruby>山田<rt>やまだ</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>変<rt>か</rt></ruby>わりません。",
                ["1　<ruby>今<rt>いま</rt></ruby>も", "2　<ruby>気持<rt>きも</rt></ruby>ちは", "3　<ruby>感謝<rt>かんしゃ</rt></ruby>の", "4　<ruby>対<rt>たい</rt></ruby>する"],
                [4, 3, 2, 1], 3, 2,
                "<ruby>山田<rt>やまだ</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>に<ruby>対<rt>たい</rt></ruby>する<ruby>感謝<rt>かんしゃ</rt></ruby>の<ruby>気持<rt>きも</rt></ruby>ちは<ruby>今<rt>いま</rt></ruby>も<ruby>変<rt>か</rt></ruby>わりません。",
                "My feeling of gratitude toward Yamada-sensei remains unchanged even now.",
                "「対する感謝の気持ちは今も」（4→3→2→1）。順序は 4→3→2→1。★には 2 が入る。",
                "'対する感謝の気持ちは今も' (4->3->2->1). Order is 4-3-2-1. Star is 2."
            ),
            make_star(
                807, "Part2 2課 練習",
                "2<ruby>回目<rt>かいめ</rt></ruby>の　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>出<rt>で</rt></ruby>た。",
                ["1　<ruby>結果<rt>けっか</rt></ruby>が", "2　<ruby>実験<rt>じっけん</rt></ruby>では", "3　<ruby>思<rt>おも</rt></ruby>った", "4　とおりの"],
                [2, 3, 4, 1], 3, 4,
                "2<ruby>回目<rt>かいめ</rt></ruby>の<ruby>実験<rt>じっけん</rt></ruby>では<ruby>思<rt>おも</rt></ruby>ったとおりの<ruby>結果<rt>けっか</rt></ruby>が<ruby>出<rt>で</rt></ruby>た。",
                "In the second experiment, the results came out just as expected.",
                "「実験では思ったとおりの結果が」（2→3→4→1）。順序は 2→3→4→1。★には 4 が入る。",
                "'実験では思ったとおりの結果が' (2->3->4->1). Order is 2-3-4-1. Star is 4."
            ),
            make_star(
                808, "Part2 2課 練習",
                "どこで　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>話<rt>はなし</rt></ruby>が<ruby>面白<rt>おもしろ</rt></ruby>かった。",
                ["1　について", "2　<ruby>知<rt>し</rt></ruby>り<ruby>合<rt>あ</rt></ruby>ったか", "3　<ruby>二人<rt>ふたり</rt></ruby>が", "4　の"],
                [3, 2, 1, 4], 3, 1,
                "どこで<ruby>二人<rt>ふたり</rt></ruby>が<ruby>知<rt>し</rt></ruby>り<ruby>合<rt>あ</rt></ruby>ったかについての<ruby>話<rt>はなし</rt></ruby>が<ruby>面白<rt>おもしろ</rt></ruby>かった。",
                "The story about where the two of them met each other was interesting.",
                "「二人が知り合ったかについての」（3→2→1→4）。順序は 3→2→1→4。★には 1 が入る。",
                "'二人が知り合ったかについての' (3->2->1->4). Order is 3-2-1-4. Star is 1."
            ),
            make_star(
                809, "Part2 2課 練習",
                "この<ruby>町<rt>まち</rt></ruby>には、　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>通<rt>とお</rt></ruby>りがある。",
                ["1　<ruby>家々<rt>いえいえ</rt></ruby>が", "2　ままの", "3　<ruby>昔<rt>むかし</rt></ruby>の", "4　<ruby>残<rt>のこ</rt></ruby>っている"],
                [3, 2, 1, 4], 3, 1,
                "この<ruby>町<rt>まち</rt></ruby>には、<ruby>昔<rt>むかし</rt></ruby>のままの<ruby>家々<rt>いえいえ</rt></ruby>が<ruby>残<rt>のこ</rt></ruby>っている<ruby>通<rt>とお</rt></ruby>りがある。",
                "In this town, there is a street where houses preserved as they were in the past still remain.",
                "「昔のままの家々が残っている」（3→2→1→4）。順序は 3→2→1→4。★には 1 が入る。",
                "'昔のままの家々が残っている' (3->2->1->4). Order is 3-2-1-4. Star is 1."
            ),
            make_star(
                810, "Part2 2課 練習",
                "<ruby>今日<rt>きょう</rt></ruby>の<ruby>午前中<rt>ごぜんちゅう</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　まだ<ruby>着<rt>つ</rt></ruby>いていない。",
                ["1　<ruby>荷物<rt>にもつ</rt></ruby>が", "2　はずの", "3　<ruby>友<rt>とも</rt></ruby>だちから", "4　<ruby>届<rt>とど</rt></ruby>く"],
                [3, 4, 2, 1], 3, 2,
                "<ruby>今日<rt>きょう</rt></ruby>の<ruby>午前中<rt>ごぜんちゅう</rt></ruby>に<ruby>友<rt>とも</rt></ruby>だちから<ruby>届<rt>とど</rt></ruby>くはずの<ruby>荷物<rt>にもつ</rt></ruby>がまだ<ruby>着<rt>つ</rt></ruby>いていない。",
                "The package that was supposed to arrive from my friend this morning hasn't arrived yet.",
                "「友だちから届くはずの荷物が」（3→4→2→1）。順序は 3→4→2→1。★には 2 が入る。",
                "'友だちから届くはずの荷物が' (3->4->2->1). Order is 3-4-2-1. Star is 2."
            )
        ]
    }
    sections.append(sec8)

    # =========================================================================
    # Section 9: Part 2 Lesson 3 (第3課 文の組み立て-3 「〜という・〜といった」) p. 107-108
    # =========================================================================
    sec9 = {
        "section_number": 9,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>3<ruby>課<rt>か</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>みたて-3 「〜という・〜といった」",
        "title_en": "Part 2 Lesson 3: Sentence Composition 3 - 'to iu / to itta'",
        "theme": "内容説明・具体例列挙の「という」「といった」構文",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "内容・定義・例示の「〜という / 〜といった」",
                "pattern_name_en": "Appositive and Exemplifying 'to iu / to itta'",
                "meaning_ja": "先行する内容を名詞に同格で結びつけたり、具体例を列挙したりする。",
                "meaning_en": "Links clauses appositively to nouns to explain content, or introduces exemplary lists.",
                "connection_forms": ["文 + という + N", "N1、N2 + といった + N"],
                "nuance_notes": "定義（〜というのは…ということだ）や具体例（〜といった）の構文配置。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>洗濯<rt>せんたく</rt></ruby>、<ruby>掃除<rt>そうじ</rt></ruby>、<ruby>料理<rt>りょうり</rt></ruby>といった<ruby>家庭内<rt>かていない</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>みんなでするべきだ。",
                        "english": "Household chores such as laundry, cleaning, and cooking should be done by the whole family."
                    }
                ]
            }
        ],
        "drills": [
            make_star(
                901, "Part2 3課 練習",
                "<ruby>何<rt>なん</rt></ruby>　＿＿＿　＿＿＿　＿★＿　＿＿＿　から、だれかに<ruby>聞<rt>き</rt></ruby>いてみよう。",
                ["1　<ruby>植物<rt>しょくぶつ</rt></ruby>", "2　という", "3　わからない", "4　か"],
                [2, 1, 4, 3], 3, 4,
                "<ruby>何<rt>なん</rt></ruby>という<ruby>植物<rt>しょくぶつ</rt></ruby>かわからないから、だれかに<ruby>聞<rt>き</rt></ruby>いてみよう。",
                "Since I don't know what kind of plant this is called, let's ask someone.",
                "「何という植物かわからないから」（2→1→4→3）。順序は 2→1→4→3。★には 4 が入る。",
                "'何という植物かわからないから' (2->1->4->3). Order is 2-1-4-3. Star is 4."
            ),
            make_star(
                902, "Part2 3課 練習",
                "<ruby>何<rt>なん</rt></ruby>でも　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>考<rt>かんが</rt></ruby>えには<ruby>私<rt>わたし</rt></ruby>は<ruby>賛成<rt>さんせい</rt></ruby>できない。",
                ["1　いい", "2　ような", "3　という", "4　いちばんが"],
                [4, 1, 3, 2], 3, 3,
                "<ruby>何<rt>なん</rt></ruby>でもいちばんがいいというような<ruby>考<rt>かんが</rt></ruby>えには<ruby>私<rt>わたし</rt></ruby>は<ruby>賛成<rt>さんせい</rt></ruby>できない。",
                "I cannot agree with the idea that being number one in everything is best.",
                "「いちばんがいいというような考え」（4→1→3→2）。順序は 4→1→3→2。★には 3 が入る。",
                "'いちばんがいいというような' (4->1->3->2). Order is 4-1-3-2. Star is 3."
            ),
            make_star(
                903, "Part2 3課 練習",
                "<ruby>調<rt>しら</rt></ruby>べた<ruby>結果<rt>けっか</rt></ruby>、これは<ruby>昔<rt>むかし</rt></ruby>、<ruby>子<rt>こ</rt></ruby>どもの　＿＿＿　＿＿＿　＿★＿　＿＿＿　ことがわかった。",
                ["1　おもちゃだ", "2　<ruby>作<rt>つく</rt></ruby>られた", "3　ために", "4　という"],
                [3, 2, 1, 4], 3, 1,
                "<ruby>調<rt>しら</rt></ruby>べた<ruby>結果<rt>けっか</rt></ruby>、これは<ruby>昔<rt>むかし</rt></ruby>、<ruby>子<rt>こ</rt></ruby>どものために<ruby>作<rt>つく</rt></ruby>られたおもちゃだということがわかった。",
                "As a result of investigation, it was discovered that this was a toy made for children in the past.",
                "「子どものために作られたおもちゃだという」（3→2→1→4）。順序は 3→2→1→4。★には 1 が入る。",
                "'ために作られたおもちゃだという' (3->2->1->4). Order is 3-2-1-4. Star is 1."
            ),
            make_star(
                904, "Part2 3課 練習",
                "<ruby>洗濯<rt>せんたく</rt></ruby>、<ruby>掃除<rt>そうじ</rt></ruby>、<ruby>料理<rt>りょうり</rt></ruby>　＿＿＿　＿＿＿　＿★＿　＿＿＿　みんなでするべきだ。",
                ["1　<ruby>家族<rt>かぞく</rt></ruby>", "2　<ruby>家庭内<rt>かていない</rt></ruby>の", "3　<ruby>仕事<rt>しごと</rt></ruby>は", "4　といった"],
                [4, 2, 3, 1], 3, 3,
                "<ruby>洗濯<rt>せんたく</rt></ruby>、<ruby>掃除<rt>そうじ</rt></ruby>、<ruby>料理<rt>りょうり</rt></ruby>といった<ruby>家庭内<rt>かていない</rt></ruby>の<ruby>仕事<rt>しごと</rt></ruby>は<ruby>家族<rt>かぞく</rt></ruby>みんなでするべきだ。",
                "Domestic chores like laundry, cleaning, and cooking should be done by all family members.",
                "「といった家庭内の仕事は家族」（4→2→3→1）。順序は 4→2→3→1。★には 3 が入る。",
                "'といった家庭内の仕事は家族' (4->2->3->1). Order is 4-2-3-1. Star is 3."
            ),
            make_star(
                905, "Part2 3課 練習",
                "「ださい」という　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>意味<rt>いみ</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>だ。",
                ["1　かっこ<ruby>悪<rt>わる</rt></ruby>い", "2　という", "3　のは", "4　ような"],
                [3, 1, 2, 4], 3, 2,
                "「ださい」というのはかっこ<ruby>悪<rt>わる</rt></ruby>いというような<ruby>意味<rt>いみ</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>だ。",
                "The word 'dasai' means something along the lines of 'uncool'.",
                "「のはかっこ悪いというような」（3→1→2→4）。順序は 3→1→2→4。★には 2 が入る。",
                "'のはかっこ悪いというような' (3->1->2->4). Order is 3-1-2-4. Star is 2."
            ),
            make_star(
                906, "Part2 3課 練習",
                "<ruby>田中<rt>たなか</rt></ruby>さんがいない　＿＿＿　＿＿＿　＿★＿　＿＿＿　が<ruby>見<rt>み</rt></ruby>えましたよ。",
                ["1　リーさん", "2　<ruby>女性<rt>じょせい</rt></ruby>", "3　という", "4　<ruby>間<rt>あいだ</rt></ruby>に"],
                [4, 1, 3, 2], 3, 3,
                "<ruby>田中<rt>たなか</rt></ruby>さんがいない<ruby>間<rt>あいだ</rt></ruby>にリーさんという<ruby>女性<rt>じょせい</rt></ruby>が<ruby>見<rt>み</rt></ruby>えましたよ。",
                "While Tanaka-san was away, a woman named Ms. Li came to visit.",
                "「間にリーさんという女性」（4→1→3→2）。順序は 4→1→3→2。★には 3 が入る。",
                "'間にリーさんという女性' (4->1->3->2). Order is 4-1-3-2. Star is 3."
            ),
            make_star(
                907, "Part2 3課 練習",
                "<ruby>自分<rt>じぶん</rt></ruby>にとって　＿＿＿　＿＿＿　＿★＿　＿＿＿　ことをもう<ruby>一度<rt>いちど</rt></ruby><ruby>考<rt>かんが</rt></ruby>えたい。",
                ["1　<ruby>何<rt>なに</rt></ruby>か", "2　ものは", "3　という", "4　<ruby>大切<rt>たいせつ</rt></ruby>な"],
                [4, 2, 1, 3], 3, 1,
                "<ruby>自分<rt>じぶん</rt></ruby>にとって<ruby>大切<rt>たいせつ</rt></ruby>なものは<ruby>何<rt>なに</rt></ruby>かということをもう<ruby>一度<rt>いちど</rt></ruby><ruby>考<rt>かんが</rt></ruby>えたい。",
                "I want to think once again about what is truly important to me.",
                "「大切なものは何かという」（4→2→1→3）。順序は 4→2→1→3。★には 1 が入る。",
                "'大切なものは何かという' (4->2->1->3). Order is 4-2-1-3. Star is 1."
            ),
            make_star(
                908, "Part2 3課 練習",
                "「<ruby>雨模様<rt>あめもよう</rt></ruby>」　＿＿＿　＿＿＿　＿★＿　＿＿＿　ことだ。",
                ["1　<ruby>様子<rt>ようす</rt></ruby>の", "2　のは", "3　という", "4　<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうな"],
                [3, 2, 4, 1], 3, 4,
                "「<ruby>雨模様<rt>あめもよう</rt></ruby>」というのは<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうな<ruby>様子<rt>ようす</rt></ruby>のことだ。",
                "'Amemoyou' means a state where it looks like it is about to rain.",
                "「というのは雨が降りそうな様子の」（3→2→4→1）。順序は 3→2→4→1。★には 4 が入る。",
                "'というのは雨が降りそうな様子の' (3->2->4->1). Order is 3-2-4-1. Star is 4."
            ),
            make_star(
                909, "Part2 3課 練習",
                "もう<ruby>年末<rt>ねんまつ</rt></ruby>だが、もうすぐ　＿＿＿　＿＿＿　＿★＿　＿＿＿　あまりしない。",
                ["1　<ruby>感<rt>かん</rt></ruby>じが", "2　<ruby>正月<rt>しょうがつ</rt></ruby>が", "3　<ruby>来<rt>く</rt></ruby>る", "4　という"],
                [2, 3, 4, 1], 3, 4,
                "もう<ruby>年末<rt>ねんまつ</rt></ruby>だが、もうすぐ<ruby>正月<rt>しょうがつ</rt></ruby>が<ruby>来<rt>く</rt></ruby>るという<ruby>感<rt>かん</rt></ruby>じがあまりしない。",
                "Even though it's year-end, it hardly feels like New Year is coming soon.",
                "「正月が来るという感じが」（2→3→4→1）。順序は 2→3→4→1。★には 4 が入る。",
                "'正月が来るという感じが' (2->3->4->1). Order is 2-3-4-1. Star is 4."
            ),
            make_star(
                910, "Part2 3課 練習",
                "ゆっくり<ruby>温泉<rt>おんせん</rt></ruby>に<ruby>入<rt>はい</rt></ruby>って、また　＿＿＿　＿＿＿　＿★＿　＿＿＿　なった。",
                ["1　という", "2　がんばろう", "3　<ruby>気持<rt>きも</rt></ruby>ちに", "4　あしたから"],
                [4, 2, 1, 3], 3, 1,
                "ゆっくり<ruby>温泉<rt>おんせん</rt></ruby>に<ruby>入<rt>はい</rt></ruby>って、またあしたからがんばろうという<ruby>気持<rt>きも</rt></ruby>ちになった。",
                "After taking a relaxing hot spring bath, I felt ready to do my best again starting tomorrow.",
                "「あしたからがんばろうという気持ちに」（4→2→1→3）。順序は 4→2→1→3。★には 1 が入る。",
                "'あしたからがんばろうという気持ちに' (4->2->1->3). Order is 4-2-1-3. Star is 1."
            )
        ]
    }
    sections.append(sec9)

    # =========================================================================
    # Section 10: Part 2 Lesson 4 (第4課 文の組み立て-4 決まった形) p. 109-110
    # =========================================================================
    sec10 = {
        "section_number": 10,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby> <ruby>第<rt>だい</rt></ruby>4<ruby>課<rt>か</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>みたて-4 <ruby>決<rt>き</rt></ruby>まった<ruby>形<rt>かたち</rt></ruby>",
        "title_en": "Part 2 Lesson 4: Sentence Composition 4 - Fixed Patterns",
        "theme": "呼応構文や定型文法形式（〜から〜にかけて、〜をはじめ、〜さえ〜ば等）の組み立て",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "文法形式による定型構文",
                "pattern_name_en": "Fixed Grammatical Frame Patterns",
                "meaning_ja": "呼応するペアや決まった助詞・文型が組み合わさって文を作る。",
                "meaning_en": "Sentence constructions that rely on fixed correlative pairs or formulaic grammar patterns.",
                "connection_forms": [
                    "〜から〜にかけて",
                    "〜はもちろん〜も",
                    "〜として",
                    "〜ば〜ほど",
                    "〜さえ〜ば"
                ],
                "nuance_notes": "決まった文型のスロットを意識して順序を決定する。",
                "example_sentences": [
                    {
                        "japanese": "この<ruby>店<rt>みせ</rt></ruby>は<ruby>夕方<rt>ゆうがた</rt></ruby>から<ruby>夜<rt>よる</rt></ruby>にかけて<ruby>会社帰<rt>かいしゃがえ</rt></ruby>りの<ruby>客<rt>きゃく</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。",
                        "english": "This shop has many customers on their way home from work from evening to night."
                    }
                ]
            }
        ],
        "drills": [
            make_star(
                1001, "Part2 4課 練習",
                "この<ruby>店<rt>みせ</rt></ruby>は<ruby>夕方<rt>ゆうがた</rt></ruby>　＿＿＿　＿＿＿　＿★＿　＿＿＿　の<ruby>客<rt>きゃく</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。",
                ["1　<ruby>夜<rt>よる</rt></ruby>", "2　<ruby>会社帰<rt>かいしゃがえ</rt></ruby>り", "3　にかけて", "4　から"],
                [4, 1, 3, 2], 3, 3,
                "この<ruby>店<rt>みせ</rt></ruby>は<ruby>夕方<rt>ゆうがた</rt></ruby>から<ruby>夜<rt>よる</rt></ruby>にかけて<ruby>会社帰<rt>かいしゃがえ</rt></ruby>りの<ruby>客<rt>きゃく</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。",
                "This shop has many customers coming from work from evening to night.",
                "「〜から夜にかけて会社帰りの」（4→1→3→2）。順序は 4→1→3→2。★には 3 が入る。",
                "'から夜にかけて会社帰りの' (4->1->3->2). Order is 4-1-3-2. Star is 3."
            ),
            make_star(
                1002, "Part2 4課 練習",
                "<ruby>京都<rt>きょうと</rt></ruby>には、　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>観光客<rt>かんこうきゃく</rt></ruby>が<ruby>訪<rt>おとず</rt></ruby>れる。",
                ["1　<ruby>週末<rt>しゅうまつ</rt></ruby>は", "2　<ruby>多<rt>おお</rt></ruby>くの", "3　もちろん", "4　<ruby>平日<rt>へいじつ</rt></ruby>にも"],
                [1, 3, 4, 2], 3, 4,
                "<ruby>京都<rt>きょうと</rt></ruby>には、<ruby>週末<rt>しゅうまつ</rt></ruby>はもちろん<ruby>平日<rt>へいじつ</rt></ruby>にも<ruby>多<rt>おお</rt></ruby>くの<ruby>観光客<rt>かんこうきゃく</rt></ruby>が<ruby>訪<rt>おとず</rt></ruby>れる。",
                "To Kyoto, many tourists visit on weekdays as well, not to mention on weekends.",
                "「週末はもちろん平日にも多くの」（1→3→4→2）。順序は 1→3→4→2。★には 4 が入る。",
                "'週末はもちろん平日にも多くの' (1->3->4->2). Order is 1-3-4-2. Star is 4."
            ),
            make_star(
                1003, "Part2 4課 練習",
                "<ruby>私<rt>わたし</rt></ruby>はこの　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>初<rt>はじ</rt></ruby>めからがんばるつもりです。",
                ["1　<ruby>出発点<rt>しゅっぱつてん</rt></ruby>", "2　<ruby>失敗<rt>しっぱい</rt></ruby>を", "3　もう<ruby>一度<rt>いちど</rt></ruby>", "4　として"],
                [2, 1, 4, 3], 3, 4,
                "<ruby>私<rt>わたし</rt></ruby>はこの<ruby>失敗<rt>しっぱい</rt></ruby>を<ruby>出発点<rt>しゅっぱつてん</rt></ruby>としてもう<ruby>一度<rt>いちど</rt></ruby><ruby>初<rt>はじ</rt></ruby>めからがんばるつもりです。",
                "I intend to take this failure as a starting point and work hard once more from the beginning.",
                "「失敗を出発点としてもう一度」（2→1→4→3）。順序は 2→1→4→3。★には 4 が入る。",
                "'失敗を出発点としてもう一度' (2->1->4->3). Order is 2-1-4-3. Star is 4."
            ),
            make_star(
                1004, "Part2 4課 練習",
                "<ruby>野球<rt>やきゅう</rt></ruby>はするのも　＿＿＿　＿＿＿　＿★＿　＿＿＿　ですね。",
                ["1　スポーツ", "2　<ruby>楽<rt>たの</rt></ruby>しい", "3　<ruby>楽<rt>たの</rt></ruby>しければ", "4　<ruby>見<rt>み</rt></ruby>るのも"],
                [3, 4, 2, 1], 3, 2,
                "<ruby>野球<rt>やきゅう</rt></ruby>はするのも<ruby>楽<rt>たの</rt></ruby>しければ<ruby>見<rt>み</rt></ruby>るのも<ruby>楽<rt>たの</rt></ruby>しいスポーツですね。",
                "Baseball is a sport that is fun both to play and to watch.",
                "「楽しければ見るのも楽しいスポーツ」（3→4→2→1）。順序は 3→4→2→1。★には 2 が入る。",
                "'楽しければ見るのも楽しいスポーツ' (3->4->2->1). Order is 3-4-2-1. Star is 2."
            ),
            make_star(
                1005, "Part2 4課 練習",
                "ここから　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>姿<rt>すがた</rt></ruby>を<ruby>見<rt>み</rt></ruby>たことがない。",
                ["1　<ruby>富士山<rt>ふじさん</rt></ruby>", "2　きれいな", "3　<ruby>見<rt>み</rt></ruby>える", "4　ほど"],
                [3, 1, 4, 2], 3, 4,
                "ここから<ruby>見<rt>み</rt></ruby>える<ruby>富士山<rt>ふじさん</rt></ruby>ほどきれいな<ruby>姿<rt>すがた</rt></ruby>を<ruby>見<rt>み</rt></ruby>たことがない。",
                "I have never seen a sight as beautiful as Mt. Fuji seen from here.",
                "「見える富士山ほどきれいな」（3→1→4→2）。順序は 3→1→4→2。★には 4 が入る。",
                "'見える富士山ほどきれいな' (3->1->4->2). Order is 3-1-4-2. Star is 4."
            ),
            make_star(
                1006, "Part2 4課 練習",
                "<ruby>絵<rt>え</rt></ruby>を　＿＿＿　＿＿＿　＿★＿　＿＿＿　いれば、どこでも<ruby>何時間<rt>なんじかん</rt></ruby>でも<ruby>楽<rt>たの</rt></ruby>しめる。",
                ["1　さえ", "2　<ruby>紙<rt>かみ</rt></ruby>とペン", "3　<ruby>持<rt>も</rt></ruby>って", "4　かくことは"],
                [4, 2, 1, 3], 3, 1,
                "<ruby>絵<rt>え</rt></ruby>をかくことは<ruby>紙<rt>かみ</rt></ruby>とペンさえ<ruby>持<rt>も</rt></ruby>っていれば、どこでも<ruby>何時間<rt>なんじかん</rt></ruby>でも<ruby>楽<rt>たの</rt></ruby>しめる。",
                "As for drawing pictures, as long as you have paper and a pen, you can enjoy it anywhere for any number of hours.",
                "「かくことは紙とペンさえ持っていれば」（4→2→1→3）。順序は 4→2→1→3。★には 1 が入る。",
                "'かくことは紙とペンさえ持っていれば' (4->2->1->3). Order is 4-2-1-3. Star is 1."
            ),
            make_star(
                1007, "Part2 4課 練習",
                "<ruby>無理<rt>むり</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　なってしまう。",
                ["1　<ruby>眠<rt>ねむ</rt></ruby>れなく", "2　<ruby>眠<rt>ねむ</rt></ruby>ろうと", "3　するほど", "4　すれば"],
                [2, 4, 3, 1], 3, 3,
                "<ruby>無理<rt>むり</rt></ruby>に<ruby>眠<rt>ねむ</rt></ruby>ろうとすればするほど<ruby>眠<rt>ねむ</rt></ruby>れなくなってしまう。",
                "The more you try hard to force yourself to sleep, the more sleepless you become.",
                "「眠ろうとすればするほど眠れなく」（2→4→3→1）。順序は 2→4→3→1。★には 3 が入る。",
                "'眠ろうとすればするほど眠れなく' (2->4->3->1). Order is 2-4-3-1. Star is 3."
            ),
            make_star(
                1008, "Part2 4課 練習",
                "<ruby>週<rt>しゅう</rt></ruby>3<ruby>回以上<rt>かいいじょう</rt></ruby>　＿＿＿　＿＿＿　＿★＿　＿＿＿　アルバイトの<ruby>人<rt>ひと</rt></ruby>を<ruby>募集<rt>ぼしゅう</rt></ruby>した。",
                ["1　<ruby>条件<rt>じょうけん</rt></ruby>", "2　<ruby>働<rt>はたら</rt></ruby>ける", "3　ことを", "4　として"],
                [2, 3, 1, 4], 3, 1,
                "<ruby>週<rt>しゅう</rt></ruby>3<ruby>回以上<rt>かいいじょう</rt></ruby><ruby>働<rt>はたら</rt></ruby>けることを<ruby>条件<rt>じょうけん</rt></ruby>としてアルバイトの<ruby>人<rt>ひと</rt></ruby>を<ruby>募集<rt>ぼしゅう</rt></ruby>した。",
                "We recruited part-time workers under the condition of being able to work at least 3 times a week.",
                "「働けることを条件として」（2→3→1→4）。順序は 2→3→1→4。★には 1 が入る。",
                "'働けることを条件として' (2->3->1->4). Order is 2-3-1-4. Star is 1."
            ),
            make_star(
                1009, "Part2 4課 練習",
                "この<ruby>会<rt>かい</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>活動<rt>かつどう</rt></ruby>をしている。",
                ["1　<ruby>中心<rt>ちゅうしん</rt></ruby>に", "2　<ruby>木村<rt>きむら</rt></ruby>さんを", "3　<ruby>会長<rt>かいちょう</rt></ruby>の", "4　いろいろな"],
                [3, 2, 1, 4], 3, 1,
                "この<ruby>会<rt>かい</rt></ruby>は<ruby>会長<rt>かいちょう</rt></ruby>の<ruby>木村<rt>きむら</rt></ruby>さんを<ruby>中心<rt>ちゅうしん</rt></ruby>にいろいろな<ruby>活動<rt>かつどう</rt></ruby>をしている。",
                "This association carries out various activities centered on its chairperson, Mr. Kimura.",
                "「会長の木村さんを中心にいろいろな」（3→2→1→4）。順序は 3→2→1→4。★には 1 が入る。",
                "'会長の木村さんを中心にいろいろな' (3->2->1->4). Order is 3-2-1-4. Star is 1."
            ),
            make_star(
                1010, "Part2 4課 練習",
                "<ruby>携帯電話<rt>けいたいでんわ</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　が、じゃまになることも<ruby>多<rt>おお</rt></ruby>い。",
                ["1　<ruby>便利<rt>べんり</rt></ruby>な", "2　<ruby>便利<rt>べんり</rt></ruby>だ", "3　ことは", "4　あれば"],
                [4, 1, 3, 2], 3, 3,
                "<ruby>携帯電話<rt>けいたいでんわ</rt></ruby>はあれば<ruby>便利<rt>べんり</rt></ruby>なことは<ruby>便利<rt>べんり</rt></ruby>だが、じゃまになることも<ruby>多<rt>おお</rt></ruby>い。",
                "Mobile phones are certainly convenient if you have one, but they often get in the way too.",
                "「あれば便利なことは便利だが」（4→1→3→2）。順序は 4→1→3→2。★には 3 が入る。",
                "'あれば便利なことは便利だが' (4->1->3->2). Order is 4-1-3-2. Star is 3."
            )
        ]
    }
    sections.append(sec10)

    # =========================================================================
    # Section 11: Part 2 Review Test (まとめ問題 1課〜4課) p. 111-113
    # =========================================================================
    sec11 = {
        "section_number": 11,
        "title": "<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby>まとめ <ruby>問題<rt>もんだい</rt></ruby> (1<ruby>課<rt>か</rt></ruby>〜4<ruby>課<rt>か</rt></ruby>)",
        "title_en": "Part 2 Review Test (Lessons 1-4)",
        "theme": "第2部文の組み立て（星印並べ替え問題）総合演習",
        "patterns": [],
        "drills": [
            make_star(
                1101, "Part2 まとめ問題",
                "<ruby>初<rt>はじ</rt></ruby>めて<ruby>会<rt>あ</rt></ruby>った　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>美<rt>うつく</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>だった。",
                ["1　とおりの", "2　<ruby>聞<rt>き</rt></ruby>いていた", "3　<ruby>母<rt>はは</rt></ruby>から", "4　その<ruby>人<rt>ひと</rt></ruby>は"],
                [4, 3, 2, 1], 3, 2,
                "<ruby>初<rt>はじ</rt></ruby>めて<ruby>会<rt>あ</rt></ruby>ったその<ruby>人<rt>ひと</rt></ruby>は<ruby>母<rt>はは</rt></ruby>から<ruby>聞<rt>き</rt></ruby>いていたとおりの<ruby>美<rt>うつく</rt></ruby>しい<ruby>人<rt>ひと</rt></ruby>だった。",
                "That person whom I met for the first time was just as beautiful as I had heard from my mother.",
                "「その人は母から聞いていたとおりの」（4→3→2→1）。★には 2 が入る。",
                "'その人は母から聞いていたとおりの' (4->3->2->1). Star is 2."
            ),
            make_star(
                1102, "Part2 まとめ問題",
                "<ruby>林<rt>はやし</rt></ruby>さんの　＿＿＿　＿＿＿　＿★＿　＿＿＿　はとても<ruby>役<rt>やく</rt></ruby>に<ruby>立<rt>た</rt></ruby>った。",
                ["1　<ruby>経験者<rt>けいけんしゃ</rt></ruby>", "2　<ruby>意見<rt>いけん</rt></ruby>", "3　の", "4　として"],
                [1, 4, 3, 2], 3, 3,
                "<ruby>林<rt>はやし</rt></ruby>さんの<ruby>経験者<rt>けいけんしゃ</rt></ruby>としての<ruby>意見<rt>いけん</rt></ruby>はとても<ruby>役<rt>やく</rt></ruby>に<ruby>立<rt>た</rt></ruby>った。",
                "Hayashi-san's opinion as someone with experience was very helpful.",
                "「経験者としての意見」（1→4→3→2）。★には 3 が入る。",
                "'経験者としての意見' (1->4->3->2). Star is 3."
            ),
            make_star(
                1103, "Part2 まとめ問題",
                "A「<ruby>先週<rt>せんしゅう</rt></ruby><ruby>送<rt>おく</rt></ruby>ったメール、<ruby>返事<rt>へんじ</rt></ruby>をもらっていないけど、<ruby>読<rt>よ</rt></ruby>んでくれましたか。」 B「<ruby>実<rt>じつ</rt></ruby>は<ruby>先週<rt>せんしゅう</rt></ruby>から　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>時間<rt>じかん</rt></ruby>がなかったんです。ごめんなさい。」",
                ["1　<ruby>返信<rt>へんしん</rt></ruby>する", "2　<ruby>今週<rt>こんしゅう</rt></ruby>に", "3　とても<ruby>忙<rt>いそが</rt></ruby>しくて", "4　かけて"],
                [2, 4, 3, 1], 3, 3,
                "B「<ruby>実<rt>じつ</rt></ruby>は<ruby>先週<rt>せんしゅう</rt></ruby>から<ruby>今週<rt>こんしゅう</rt></ruby>にかけてとても<ruby>忙<rt>いそが</rt></ruby>しくて<ruby>返信<rt>へんしん</rt></ruby>する<ruby>時間<rt>じかん</rt></ruby>がなかったんです。ごめんなさい。」",
                "Actually, from last week through this week I was so busy that I didn't have time to reply. I'm sorry.",
                "「今週にかけてとても忙しくて返信する」（2→4→3→1）。★には 3 が入る。",
                "'今週にかけてとても忙しくて返信する' (2->4->3->1). Star is 3."
            ),
            make_star(
                1104, "Part2 まとめ問題",
                "<ruby>今回<rt>こんかい</rt></ruby>は　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>書<rt>か</rt></ruby>くつもりだ。",
                ["1　テーマと", "2　<ruby>人口問題<rt>じんこうもんだい</rt></ruby>を", "3　レポートを", "4　した"],
                [2, 1, 4, 3], 3, 4,
                "<ruby>今回<rt>こんかい</rt></ruby>は<ruby>人口問題<rt>じんこうもんだい</rt></ruby>をテーマとしたレポートを<ruby>書<rt>か</rt></ruby>くつもりだ。",
                "This time, I intend to write a report with population issues as its theme.",
                "「人口問題をテーマとしたレポートを」（2→1→4→3）。★には 4 が入る。",
                "'人口問題をテーマとしたレポートを' (2->1->4->3). Star is 4."
            ),
            make_star(
                1105, "Part2 まとめ問題",
                "この<ruby>町<rt>まち</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>不満<rt>ふまん</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きくなっている。",
                ["1　<ruby>住民<rt>じゅうみん</rt></ruby>からの", "2　に<ruby>対<rt>たい</rt></ruby>する", "3　<ruby>工場<rt>こうじょう</rt></ruby>を<ruby>作<rt>つく</rt></ruby>る", "4　こと"],
                [3, 4, 2, 1], 3, 2,
                "この<ruby>町<rt>まち</rt></ruby>に<ruby>工場<rt>こうじょう</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ることに対する<ruby>住民<rt>じゅうみん</rt></ruby>からの<ruby>不満<rt>ふまん</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きくなっている。",
                "Dissatisfaction from residents against building a factory in this town is growing.",
                "「工場を作ることに対する住民からの」（3→4→2→1）。★には 2 が入る。",
                "'工場を作ることに対する住民からの' (3->4->2->1). Star is 2."
            ),
            make_star(
                1106, "Part2 まとめ問題",
                "<ruby>私<rt>わたし</rt></ruby>には　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>悩<rt>なや</rt></ruby>みがある。",
                ["1　<ruby>上手<rt>じょうず</rt></ruby>に", "2　という", "3　<ruby>人<rt>ひと</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で", "4　<ruby>話<rt>はな</rt></ruby>せない"],
                [3, 1, 4, 2], 3, 4,
                "<ruby>私<rt>わたし</rt></ruby>には<ruby>人<rt>ひと</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>で<ruby>上手<rt>じょうず</rt></ruby>に<ruby>話<rt>はな</rt></ruby>せないという<ruby>悩<rt>なや</rt></ruby>みがある。",
                "I have the trouble of not being able to speak well in front of other people.",
                "「人の前で上手に話せないという」（3→1→4→2）。★には 4 が入る。",
                "'人の前で上手に話せないという' (3->1->4->2). Star is 4."
            ),
            make_star(
                1107, "Part2 まとめ問題",
                "<ruby>私<rt>わたし</rt></ruby>は<ruby>今日<rt>きょう</rt></ruby>　＿＿＿　＿＿＿　＿★＿　＿＿＿　したことはない。",
                ["1　<ruby>楽<rt>たの</rt></ruby>しい", "2　<ruby>経験<rt>けいけん</rt></ruby>を", "3　ほど", "4　これまで"],
                [3, 1, 2, 4], 3, 2,
                "<ruby>私<rt>わたし</rt></ruby>は<ruby>今日<rt>きょう</rt></ruby>ほど<ruby>楽<rt>たの</rt></ruby>しい<ruby>経験<rt>けいけん</rt></ruby>をこれまでしたことはない。",
                "I have never before had an experience as enjoyable as today.",
                "「今日ほど楽しい経験をこれまで」（3→1→2→4）。★には 2 が入る。",
                "'今日ほど楽しい経験をこれまで' (3->1->2->4). Star is 2."
            ),
            make_star(
                1108, "Part2 まとめ問題",
                "これらの<ruby>写真<rt>しゃしん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>には、<ruby>価値<rt>かち</rt></ruby>の　＿＿＿　＿＿＿　＿★＿　＿＿＿　ものもある。",
                ["1　つまらない", "2　ある", "3　あれば", "4　ものも"],
                [2, 4, 3, 1], 3, 3,
                "これらの<ruby>写真<rt>しゃしん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>には、<ruby>価値<rt>かち</rt></ruby>のあるものもあればつまらないものもある。",
                "Among these photos, there are valuable ones, and there are also worthless ones.",
                "「あるものもあればつまらない」（2→4→3→1）。★には 3 が入る。",
                "'あるものもあればつまらない' (2->4->3->1). Star is 3."
            ),
            make_star(
                1109, "Part2 まとめ問題",
                "A「どうしたの？さっきから<ruby>何<rt>なに</rt></ruby>を<ruby>探<rt>さが</rt></ruby>しているの？」 B「<ruby>朝<rt>あさ</rt></ruby>、かばんに<ruby>入<rt>い</rt></ruby>れた　＿＿＿　＿＿＿　＿★＿　＿＿＿　ないんだ。」",
                ["1　<ruby>財布<rt>さいふ</rt></ruby>", "2　はず", "3　が", "4　の"],
                [2, 4, 1, 3], 3, 1,
                "B「<ruby>朝<rt>あさ</rt></ruby>、かばんに<ruby>入<rt>い</rt></ruby>れたはずの<ruby>財布<rt>さいふ</rt></ruby>がないんだ。」",
                "The wallet that should have been put into my bag this morning isn't there.",
                "「はずの財布が」（2→4→1→3）。★には 1 が入る。",
                "'はずの財布が' (2->4->1->3). Star is 1."
            ),
            make_star(
                1110, "Part2 まとめ問題",
                "どこからか　＿＿＿　＿＿＿　＿★＿　＿＿＿　ようですが……。",
                ["1　<ruby>声<rt>こえ</rt></ruby>が", "2　<ruby>赤<rt>あか</rt></ruby>ちゃんが", "3　する", "4　<ruby>泣<rt>な</rt></ruby>いている"],
                [2, 4, 1, 3], 3, 1,
                "どこからか<ruby>赤<rt>あか</rt></ruby>ちゃんが<ruby>泣<rt>な</rt></ruby>いている<ruby>声<rt>こえ</rt></ruby>がするようですが……。",
                "It seems that the cry of a baby crying can be heard from somewhere, but...",
                "「赤ちゃんが泣いている声がする」（2→4→1→3）。★には 1 が入る。",
                "'赤ちゃんが泣いている声がする' (2->4->1->3). Star is 1."
            ),
            make_star(
                1111, "Part2 まとめ問題",
                "<ruby>先生<rt>せんせい</rt></ruby>に、　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>言<rt>い</rt></ruby>われた。",
                ["1　わからない", "2　ように", "3　<ruby>質問<rt>しつもん</rt></ruby>する", "4　ときは"],
                [1, 4, 3, 2], 3, 3,
                "<ruby>先生<rt>せんせい</rt></ruby>に、わからないときは<ruby>質問<rt>しつもん</rt></ruby>するように<ruby>言<rt>い</rt></ruby>われた。",
                "I was told by the teacher to ask questions whenever I don't understand.",
                "「わからないときは質問するように」（1→4→3→2）。★には 3 が入る。",
                "'わからないときは質問するように' (1->4->3->2). Star is 3."
            ),
            make_star(
                1112, "Part2 まとめ問題",
                "A「<ruby>今度<rt>こんど</rt></ruby>うちでパーティーをするんですが、<ruby>簡単<rt>かんたん</rt></ruby>な<ruby>料理<rt>りょうり</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えてくれませんか。」 B「この<ruby>料理<rt>りょうり</rt></ruby>はどうですか。ここに　＿＿＿　＿＿＿　＿★＿　＿＿＿　だれでもすぐに<ruby>作<rt>つく</rt></ruby>れるはずですよ。」",
                ["1　あれば", "2　<ruby>書<rt>か</rt></ruby>いてある", "3　さえ", "4　<ruby>材料<rt>ざいりょう</rt></ruby>"],
                [2, 4, 3, 1], 3, 3,
                "B「この<ruby>料理<rt>りょうり</rt></ruby>はどうですか。ここに<ruby>書<rt>か</rt></ruby>いてある<ruby>材料<rt>ざいりょう</rt></ruby>さえあればだれでもすぐに<ruby>作<rt>つく</rt></ruby>れるはずですよ。」",
                "How about this dish? As long as you have the ingredients written here, anyone should be able to make it right away.",
                "「書いてある材料さえあれば」（2→4→3→1）。★には 3 が入る。",
                "'書いてある材料さえあれば' (2->4->3->1). Star is 3."
            ),
            make_star(
                1113, "Part2 まとめ問題",
                "ごみが<ruby>増<rt>ふ</rt></ruby>え<ruby>続<rt>つづ</rt></ruby>けている　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>考<rt>かんが</rt></ruby>えていかなければならない。",
                ["1　<ruby>問題<rt>もんだい</rt></ruby>", "2　ことを", "3　として", "4　<ruby>自分<rt>じぶん</rt></ruby>たちの"],
                [2, 4, 1, 3], 3, 1,
                "ごみが<ruby>増<rt>ふ</rt></ruby>え<ruby>続<rt>つづ</rt></ruby>けていることを<ruby>自分<rt>じぶん</rt></ruby>たちの<ruby>問題<rt>もんだい</rt></ruby>として<ruby>考<rt>かんが</rt></ruby>えていかなければならない。",
                "We must think of the continually increasing trash as our own problem.",
                "「ことを自分たちの問題として」（2→4→1→3）。★には 1 が入る。",
                "'ことを自分たちの問題として' (2->4->1->3). Star is 1."
            ),
            make_star(
                1114, "Part2 まとめ問題",
                "<ruby>私<rt>わたし</rt></ruby>はハンバーガーや<ruby>焼<rt>や</rt></ruby>き<ruby>肉<rt>にく</rt></ruby>と　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>好<rt>す</rt></ruby>きだ。",
                ["1　カロリーが", "2　<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>が", "3　いった", "4　<ruby>高<rt>たか</rt></ruby>い"],
                [3, 1, 4, 2], 3, 4,
                "<ruby>私<rt>わたし</rt></ruby>はハンバーガーや<ruby>焼<rt>や</rt></ruby>き<ruby>肉<rt>にく</rt></ruby>といったカロリーが<ruby>高<rt>たか</rt></ruby>い<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>が<ruby>好<rt>す</rt></ruby>きだ。",
                "I like high-calorie foods such as hamburgers and yakiniku.",
                "「いったカロリーが高い食べ物が」（3→1→4→2）。★には 4 が入る。",
                "'いったカロリーが高い食べ物が' (3->1->4->2). Star is 4."
            ),
            make_star(
                1115, "Part2 まとめ問題",
                "なぜ<ruby>私<rt>わたし</rt></ruby>が<ruby>係<rt>かかり</rt></ruby>を　＿＿＿　＿＿＿　＿★＿　＿＿＿　ほかにいなかったからだ。",
                ["1　いうと", "2　やることに", "3　やりたい<ruby>人<rt>ひと</rt></ruby>が", "4　なったかと"],
                [2, 4, 1, 3], 3, 1,
                "なぜ<ruby>私<rt>わたし</rt></ruby>が<ruby>係<rt>かかり</rt></ruby>をやるようになったかというとやりたい<ruby>人<rt>ひと</rt></ruby>がほかにいなかったからだ。",
                "If you ask why I came to take charge of this duty, it is because there was no one else who wanted to do it.",
                "「やるようになったかというとやりたい人が」（2→4→1→3）。★には 1 が入る。",
                "'やるようになったかというとやりたい人が' (2->4->1->3). Star is 1."
            ),
            make_star(
                1116, "Part2 まとめ問題",
                "【<ruby>電話<rt>でんわ</rt></ruby>で】<ruby>兄<rt>あに</rt></ruby>「お<ruby>母<rt>かあ</rt></ruby>さん、<ruby>何<rt>なん</rt></ruby>と<ruby>言<rt>い</rt></ruby>っていた？」 <ruby>妹<rt>いもうと</rt></ruby>「お<ruby>正月<rt>しょうがつ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に　＿＿＿　＿＿＿　＿★＿　＿＿＿　ほしいって。」",
                ["1　くるか", "2　<ruby>知<rt>し</rt></ruby>らせて", "3　<ruby>帰<rt>かえ</rt></ruby>って", "4　どうか"],
                [3, 1, 4, 2], 3, 4,
                "<ruby>妹<rt>いもうと</rt></ruby>「お<ruby>正月<rt>しょうがつ</rt></ruby>に<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってくるかどうか<ruby>知<rt>し</rt></ruby>らせてほしいって。」",
                "Little sister: 'Mom says she wants you to let her know whether you will be coming home for New Year.'",
                "「帰ってくるかどうか知らせて」（3→1→4→2）。★には 4 が入る。",
                "'帰ってくるかどうか知らせて' (3->1->4->2). Star is 4."
            ),
            make_star(
                1117, "Part2 まとめ問題",
                "<ruby>親<rt>おや</rt></ruby>にとって　＿＿＿　＿＿＿　＿★＿　＿＿＿　ことはない。",
                ["1　<ruby>病気<rt>びょうき</rt></ruby>", "2　<ruby>心配<rt>しんぱい</rt></ruby>な", "3　<ruby>子<rt>こ</rt></ruby>どもの", "4　ぐらい"],
                [3, 1, 4, 2], 3, 4,
                "<ruby>親<rt>おや</rt></ruby>にとって<ruby>子<rt>こ</rt></ruby>どもの<ruby>病気<rt>びょうき</rt></ruby>ぐらい<ruby>心配<rt>しんぱい</rt></ruby>なことはない。",
                "For parents, nothing is as worrisome as a child's illness.",
                "「子どもの病気ぐらい心配な」（3→1→4→2）。★には 4 が入る。",
                "'子どもの病気ぐらい心配な' (3->1->4->2). Star is 4."
            ),
            make_star(
                1118, "Part2 まとめ問題",
                "できるだけ<ruby>規則正<rt>きそくただ</rt></ruby>しい<ruby>生活<rt>せいかつ</rt></ruby>を　＿＿＿　＿＿＿　＿★＿　＿＿＿　と<ruby>思<rt>おも</rt></ruby>う。",
                ["1　ように", "2　したほうがいい", "3　する", "4　だろう"],
                [3, 1, 2, 4], 3, 2,
                "できるだけ<ruby>規則正<rt>きそくただ</rt></ruby>しい<ruby>生活<rt>せいかつ</rt></ruby>をするようにしたほうがいいだろうと<ruby>思<rt>おも</rt></ruby>う。",
                "I think it would probably be best to try to lead as orderly and regular a life as possible.",
                "「するようにしたほうがいいだろう」（3→1→2→4）。★には 2 が入る。",
                "'するようにしたほうがいいだろう' (3->1->2->4). Star is 2."
            )
        ]
    }
    sections.append(sec11)

    return sections
