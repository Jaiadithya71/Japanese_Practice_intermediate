import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/kanji"))


def make_item(ex_id, idx, kanji, target_word, reading, q_ja, q_en, sentence, ruby_html, options, answer, explanation):
    return {
        "id": f"{ex_id}_{idx}",
        "item_id": idx,
        "kanji": kanji,
        "target_word": target_word,
        "reading": reading,
        "question_ja": q_ja,
        "question_en": q_en,
        "sentence": sentence,
        "ruby_html": ruby_html,
        "options": options,
        "answer": str(answer),
        "explanation": explanation
    }


def build_part3_exercises():
    lessons = [
        # =====================================================================
        # LESSON 11: 第11回 教育・文化・生活(2) (pp. 46-47)
        # =====================================================================
        {
            "lesson": 11,
            "title_ja": "第11回 教育・文化・生活 (2)",
            "title_en": "Lesson 11: Education, Culture & Daily Life (2)",
            "page_range": "46-47",
            "exercises": [
                {
                    "id": "k_ex_11_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。(ひがし病院のお知らせ)",
                    "title_en": "1. Choose the correct reading for the underlined kanji (East Hospital Notice).",
                    "items": [
                        make_item(
                            "k_ex_11_1", 1, "保", "保険", "ほけん",
                            "●健康 <u>保険</u> がない方は相談してください。",
                            "Please consult us if you do not have health insurance.",
                            "健康保険がない方は相談してください。",
                            "<ruby>健康<rt>けんこう</rt></ruby><ruby>保険<rt>ほけん</rt></ruby>がない<ruby>方<rt>かた</rt></ruby>は<ruby>相談<rt>そうだん</rt></ruby>してください。",
                            ["1 ほけん", "2 ほうけん", "3 ほっけん", "4 ぼけん"],
                            1,
                            "保険（ほけん）＝ insurance (保: ほ, 険: けん). 健康保険（けんこうほけん）means health insurance."
                        ),
                        make_item(
                            "k_ex_11_1", 2, "支", "お支払い", "おしはらい",
                            "● <u>お支払い</u> はカードでもできます。",
                            "Payment can also be made by card.",
                            "お支払いはカードでもできます。",
                            "お<ruby>支払<rt>しはら</rt></ruby>いはカードでもできます。",
                            ["1 おしはらい", "2 おしわらい", "3 おしぱらい", "4 おじはらい"],
                            1,
                            "お支払い（おしはらい）＝ payment (polite form of 支払い from 支払う: しはらう)."
                        ),
                        make_item(
                            "k_ex_11_1", 3, "退", "退院", "たいいん",
                            "● <u>退院</u> の手続きの方は5番窓口です。",
                            "Those completing hospital discharge procedures, please go to counter 5.",
                            "退院の手続きの方は5番窓口です。",
                            "<ruby>退院<rt>たいいん</rt></ruby>の<ruby>手続<rt>てつづ</rt></ruby>きの<ruby>方<rt>かた</rt></ruby>は5<ruby>番窓口<rt>ばんまどぐち</rt></ruby>です。",
                            ["1 たいいん", "2 だいいん", "3 しりぞいん", "4 にゅういん"],
                            1,
                            "退院（たいいん）＝ leaving/being discharged from the hospital (opposite of 入院: にゅういん)."
                        ),
                        make_item(
                            "k_ex_11_1", 4, "局", "薬局", "やっきょく",
                            "⬅ <u>薬局</u>（病院の案内表示）",
                            "⬅ Pharmacy (Hospital sign)",
                            "薬局",
                            "<ruby>薬局<rt>やっきょく</rt></ruby>",
                            ["1 やっきょく", "2 やくきょく", "3 くすりきょく", "4 やっきょう"],
                            1,
                            "薬局（やっきょく）＝ pharmacy / drugstore. Note the geminate consonant っ before きょく."
                        ),
                        make_item(
                            "k_ex_11_1", 5, "非", "非常口", "ひじょうぐち",
                            "<u>非常口</u> ➡（病院の案内表示）",
                            "Emergency Exit ➡ (Hospital sign)",
                            "非常口",
                            "<ruby>非常口<rt>ひじょうぐち</rt></ruby>",
                            ["1 ひじょうぐち", "2 ひじょうくち", "3 びじょうぐち", "4 ひしょうぐち"],
                            1,
                            "非常口（ひじょうぐち）＝ emergency exit (非常: ひじょう + 口: ぐち with rendaku)."
                        )
                    ]
                },
                {
                    "id": "k_ex_11_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct reading or kanji.",
                    "items": [
                        make_item(
                            "k_ex_11_2", 1, "早", "早退", "そうたい",
                            "①頭が痛かったので、学校を<u>早退</u>した。",
                            "Because I had a headache, I left school early.",
                            "頭が痛かったので、学校を早退した。",
                            "<ruby>頭<rt>あたま</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>かったので、<ruby>学校<rt>がっこう</rt></ruby>を<ruby>早退<rt>そうたい</rt></ruby>した。",
                            ["1 はやたい", "2 そくたい", "3 そうたい", "4 ちょうたい"],
                            3,
                            "早退（そうたい）＝ leaving early (from school or work). 早 takes the on-reading そう here."
                        ),
                        make_item(
                            "k_ex_11_2", 2, "財", "財産", "ざいさん",
                            "②父の<u>ざいさん</u>を兄弟で分けた。",
                            "The brothers divided their father's property/assets.",
                            "父の財産を兄弟で分けた。",
                            "<ruby>父<rt>ちち</rt></ruby>の<ruby>財産<rt>ざいさん</rt></ruby>を<ruby>兄弟<rt>きょうだい</rt></ruby>で<ruby>分<rt>わ</rt></ruby>けた。",
                            ["1 財産", "2 材産", "3 剤産", "4 税産"],
                            1,
                            "財産（ざいさん）＝ property, fortune, assets. Uses 財 (wealth/fortune), not 材 (material/timber)."
                        ),
                        make_item(
                            "k_ex_11_2", 3, "収", "収入", "しゅうにゅう",
                            "③ <u>a. しゅうにゅう</u>がいくらか、けいさんした。",
                            "I calculated how much my income was.",
                            "収入がいくらか、計算した。",
                            "<ruby>収入<rt>しゅうにゅう</rt></ruby>がいくらか、<ruby>計算<rt>けいさん</rt></ruby>した。",
                            ["1 収入", "2 収人", "3 取入", "4 集入"],
                            1,
                            "収入（しゅうにゅう）＝ income, receipts (収: collect/obtain + 入: enter)."
                        ),
                        make_item(
                            "k_ex_11_2", 4, "算", "計算", "けいさん",
                            "③ しゅうにゅうがいくらか、<u>b. けいさん</u>した。",
                            "I calculated how much my income was.",
                            "収入がいくらか、計算した。",
                            "<ruby>収入<rt>しゅうにゅう</rt></ruby>がいくらか、<ruby>計算<rt>けいさん</rt></ruby>した。",
                            ["1 計覧", "2 計算", "3 記算", "4 計賛"],
                            2,
                            "計算（けいさん）＝ calculation, reckoning (計: measure/plan + 算: calculate)."
                        ),
                        make_item(
                            "k_ex_11_2", 5, "宅", "お宅", "おたく",
                            "④日曜日は、<u>おたく</u>にいらっしゃいますか。",
                            "Will you be at home on Sunday?",
                            "日曜日は、お宅にいらっしゃいますか。",
                            "<ruby>日曜日<rt>にちようび</rt></ruby>は、お<ruby>宅<rt>たく</rt></ruby>にいらっしゃいますか。",
                            ["1 お宅", "2 お家", "3 お宇", "4 お完"],
                            1,
                            "お宅（おたく）＝ someone's home/house (polite), written with 宅."
                        )
                    ]
                },
                {
                    "id": "k_ex_11_3",
                    "type": "sentence_fill",
                    "title_ja": "3. [ 予、球、支、給 ] の中から漢字を選んで、文を完成しましょう。読み方も書きましょう。",
                    "title_en": "3. Choose a kanji from [ 予, 球, 支, 給 ] to complete the sentence and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_11_3", 1, "球", "地球", "ちきゅう",
                            "①月は、地<u>［　］</u>の周りを約30日で回っている。",
                            "The moon orbits around the Earth in about 30 days.",
                            "月は、地球の周りを約30日で回っている。",
                            "<ruby>月<rt>つき</rt></ruby>は、<ruby>地球<rt>ちきゅう</rt></ruby>の<ruby>周<rt>まわ</rt></ruby>りを<ruby>約<rt>やく</rt></ruby>30<ruby>日<rt>にち</rt></ruby>で<ruby>回<rt>まわ</rt></ruby>っている。",
                            ["1 球（ちきゅう）", "2 予（ちよ）", "3 支（ちし）", "4 給（ちきゅう）"],
                            1,
                            "地球（ちきゅう）＝ the Earth, the globe (地: earth/ground + 球: sphere)."
                        ),
                        make_item(
                            "k_ex_11_3", 2, "支", "支出", "ししゅつ",
                            "②先月は引っ越しにお金を使ったので、いつもより<u>［　］</u>出が多かった。",
                            "Because I spent money on moving last month, my expenses were higher than usual.",
                            "先月は引っ越しにお金を使ったので、いつもより支出が多かった。",
                            "<ruby>先月<rt>せんげつ</rt></ruby>は<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しにお<ruby>金<rt>かね</rt></ruby>を<ruby>使<rt>つか</rt></ruby>ったので、いつもより<ruby>支出<rt>ししゅつ</rt></ruby>が<ruby>多<rt>おお</rt></ruby>かった。",
                            ["1 支（ししゅつ）", "2 予（よしゅつ）", "3 給（きゅうしゅつ）", "4 球（きゅうしゅつ）"],
                            1,
                            "支出（ししゅつ）＝ expenditure, expenses (opposite of 収入: しゅうにゅう)."
                        ),
                        make_item(
                            "k_ex_11_3", 3, "給", "給食", "きゅうしょく",
                            "③今日の学校の<u>［　］</u>食は、私が大好きなメニューだった。",
                            "Today's school lunch was a menu I love.",
                            "今日の学校の給食は、私が大好きなメニューだった。",
                            "<ruby>今日<rt>きょう</rt></ruby>の<ruby>学校<rt>がっこう</rt></ruby>の<ruby>給食<rt>きゅうしょく</rt></ruby>は、<ruby>私<rt>わたし</rt></ruby>が<ruby>大好<rt>だいす</rt></ruby>きなメニューだった。",
                            ["1 給（きゅうしょく）", "2 支（ししょく）", "3 予（よしょく）", "4 球（きゅうしょく）"],
                            1,
                            "給食（きゅうしょく）＝ school lunch / meal service (給: supply/provide + 食: meal)."
                        ),
                        make_item(
                            "k_ex_11_3", 4, "予", "予算", "よさん",
                            "④海外旅行にどのくらいお金がかかるか調べて、<u>［　］</u>算を立てた。",
                            "I researched how much an overseas trip would cost and drew up a budget.",
                            "海外旅行にどのくらいお金がかかるか調べて、予算を立てた。",
                            "<ruby>海外旅行<rt>かいがいりょこう</rt></ruby>にどのくらいお<ruby>金<rt>かね</rt></ruby>がかかるか<ruby>調<rt>しら</rt></ruby>べて、<ruby>予算<rt>よさん</rt></ruby>を<ruby>立<rt>た</rt></ruby>てた。",
                            ["1 予（よさん）", "2 支（しさん）", "3 給（きゅうさん）", "4 球（きゅうさん）"],
                            1,
                            "予算（よさん）＝ budget, estimate (予: beforehand + 算: calculation)."
                        )
                    ]
                },
                {
                    "id": "k_ex_11_4",
                    "type": "reading_writing",
                    "title_ja": "4. 下線の部分の漢字には読み方を、平仮名には漢字を書きましょう。(♪ マナの部屋 ♬)",
                    "title_en": "4. Give the reading for underlined kanji and kanji for underlined hiragana (Mana's Blog).",
                    "items": [
                        make_item(
                            "k_ex_11_4", 1, "活", "生活", "せいかつ",
                            "初めての一人の <u>a. せいかつ</u> で、やっていけるかなあ。",
                            "It's my first time living alone; I wonder if I can manage.",
                            "初めての一人の生活で、やっていけるかなあ。",
                            "<ruby>初<rt>はじ</rt></ruby>めての<ruby>一人<rt>ひとり</rt></ruby>の<ruby>生活<rt>せいかつ</rt></ruby>で、やっていけるかなあ。",
                            ["1 生活", "2 生括", "3 性活", "4 正活"],
                            1,
                            "生活（せいかつ）＝ daily life, living (生: life + 活: lively/active)."
                        ),
                        make_item(
                            "k_ex_11_4", 2, "階", "2階", "にかい",
                            "部屋は、マンションの <u>b. 2かい</u> です。",
                            "My room is on the 2nd floor of the apartment building.",
                            "部屋は、マンションの2階です。",
                            "<ruby>部屋<rt>へや</rt></ruby>は、マンションの2<ruby>階<rt>かい</rt></ruby>です。",
                            ["1 2階", "2 2回", "3 2界", "4 2開"],
                            1,
                            "2階（にかい）＝ 2nd floor / story of a building (階: floor/stairs)."
                        ),
                        make_item(
                            "k_ex_11_4", 3, "絵", "絵", "え",
                            "午前中は部屋の掃除をして、友達がくれた <u>c. え</u> を飾ったり、カーテンを替えたりしました。",
                            "In the morning I cleaned my room, hung up a picture my friend gave me, and changed the curtains.",
                            "午前中は部屋の掃除をして、友達がくれた絵を飾ったり、カーテンを替えたりしました。",
                            "<ruby>午前中<rt>ごぜんちゅう</rt></ruby>は<ruby>部屋<rt>へや</rt></ruby>の<ruby>掃除<rt>そうじ</rt></ruby>をして、<ruby>友達<rt>ともだち</rt></ruby>がくれた<ruby>絵<rt>え</rt></ruby>を<ruby>飾<rt>かざ</rt></ruby>ったり、カーテンを<ruby>替<rt>か</rt></ruby>えたりしました。",
                            ["1 絵", "2 会", "3 重", "4 線"],
                            1,
                            "絵（え）＝ picture, painting, drawing."
                        ),
                        make_item(
                            "k_ex_11_4", 4, "類", "書類", "しょるい",
                            "午後は市役所へ <u>d. 書類</u> を出しに行きました。",
                            "In the afternoon I went to city hall to submit documents.",
                            "午後は市役所へ書類を出しに行きました。",
                            "<ruby>午後<rt>ごご</rt></ruby>は<ruby>市役所<rt>しやくしょ</rt></ruby>へ<ruby>書類<rt>しょるい</rt></ruby>を<ruby>出<rt>だ</rt></ruby>しに<ruby>行<rt>い</rt></ruby>きました。",
                            ["1 しょるい", "2 しょうるい", "3 かきるい", "4 しょらい"],
                            1,
                            "書類（しょるい）＝ documents, papers (書: write/document + 類: kind/category)."
                        ),
                        make_item(
                            "k_ex_11_4", 5, "器", "食器", "しょっき",
                            "そのあと、ちょっとお店に寄って、新しい <u>e. 食器</u> を買って…。",
                            "After that, I stopped by a shop and bought new tableware...",
                            "そのあと、ちょっとお店に寄って、新しい食器を買って…。",
                            "そのあと、ちょっとお<ruby>店<rt>みせ</rt></ruby>に<ruby>寄<rt>よ</rt></ruby>って、<ruby>新<rt>あたら</rt></ruby>しい<ruby>食器<rt>しょっき</rt></ruby>を<ruby>買<rt>か</rt></ruby>って…。",
                            ["1 しょっき", "2 しょくき", "3 たべき", "4 じき"],
                            1,
                            "食器（しょっき）＝ tableware, dishes (食: eat + 器: vessel/utensil)."
                        ),
                        make_item(
                            "k_ex_11_4", 6, "修", "修理", "しゅうり",
                            "シャワーがちょっとおかしいので、<u>f. 修理</u> を頼まなくちゃ。",
                            "The shower is acting a bit strange, so I have to ask for repairs.",
                            "シャワーがちょっとおかしいので、修理を頼まなくちゃ。",
                            "シャワーがちょっとおかしいので、<ruby>修理<rt>しゅうり</rt></ruby>を<ruby>頼<rt>たの</rt></ruby>まなくちゃ。",
                            ["1 しゅうり", "2 しゅり", "3 じゅうり", "4 なおし"],
                            1,
                            "修理（しゅうり）＝ repair, mending (修: fix/discipline + 理: arrange/reason)."
                        ),
                        make_item(
                            "k_ex_11_4", 7, "活", "活動", "かつどう",
                            "しばらく休んでいた音楽 <u>g. かつどう</u> もまた始めるつもりです。",
                            "I also plan to resume my music activities that I had taken a break from.",
                            "しばらく休んでいた音楽活動もまた始めるつもりです。",
                            "しばらく<ruby>休<rt>やす</rt></ruby>んでいた<ruby>音楽活動<rt>おんがくかつどう</rt></ruby>もまた<ruby>始<rt>はじ</rt></ruby>めるつもりです。",
                            ["1 活動", "2 括動", "3 話動", "4 活働"],
                            1,
                            "活動（かつどう）＝ activity, action (活: active + 動: move)."
                        )
                    ]
                }
            ]
        },

        # =====================================================================
        # LESSON 12: 第12回 教育・文化・生活(3) (pp. 48-50)
        # =====================================================================
        {
            "lesson": 12,
            "title_ja": "第12回 教育・文化・生活 (3)",
            "title_en": "Lesson 12: Education, Culture & Daily Life (3)",
            "page_range": "48-50",
            "exercises": [
                {
                    "id": "k_ex_12_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。(ともや君とさつきさんの結婚パーティー)",
                    "title_en": "1. Choose the correct reading for the underlined kanji (Tomoya & Satsuki's Wedding Party).",
                    "items": [
                        make_item(
                            "k_ex_12_1", 1, "式", "式", "しき",
                            "（<u>a. 式</u> が終わったら、すぐに準備を開始します）",
                            "(As soon as the ceremony ends, we will start preparations.)",
                            "式が終わったら、すぐに準備を開始します。",
                            "<ruby>式<rt>しき</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったら、すぐに<ruby>準備<rt>じゅんび</rt></ruby>を<ruby>開始<rt>かいし</rt></ruby>します。",
                            ["1 しき", "2 じき", "3 しぎ", "4 せき"],
                            1,
                            "式（しき）＝ ceremony, rite, formula (e.g., 結婚式: wedding ceremony)."
                        ),
                        make_item(
                            "k_ex_12_1", 2, "準", "準備", "じゅんび",
                            "（式が終わったら、すぐに <u>b. 準備</u> を開始します）",
                            "(As soon as the ceremony ends, we will start preparations.)",
                            "式が終わったら、すぐに準備を開始します。",
                            "<ruby>式<rt>しき</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったら、すぐに<ruby>準備<rt>じゅんび</rt></ruby>を<ruby>開始<rt>かいし</rt></ruby>します。",
                            ["1 じゅんび", "2 しゅんび", "3 じゅうび", "4 じゅんぴ"],
                            1,
                            "準備（じゅんび）＝ preparation, arrangements (準: prepare/standard + 備: provide/equip)."
                        ),
                        make_item(
                            "k_ex_12_1", 3, "司", "司会", "しかい",
                            "<u>c. 司会</u>（古田）",
                            "Master of Ceremonies / Host (Furuta)",
                            "司会（古田）",
                            "<ruby>司会<rt>しかい</rt></ruby>（<ruby>古田<rt>ふるた</rt></ruby>）",
                            ["1 しかい", "2 じかい", "3 しっかい", "4 つかさかい"],
                            1,
                            "司会（しかい）＝ chairmanship, presiding, MC / host (司: officiate/rule + 会: meeting)."
                        ),
                        make_item(
                            "k_ex_12_1", 4, "紹", "紹介", "しょうかい",
                            "二人の <u>d. 紹介</u>",
                            "Introduction of the couple",
                            "二人の紹介",
                            "<ruby>二人<rt>ふたり</rt></ruby>の<ruby>紹介<rt>しょうかい</rt></ruby>",
                            ["1 しょうかい", "2 しょかい", "3 じょうかい", "4 しょうがい"],
                            1,
                            "紹介（しょうかい）＝ introduction, presentation (紹: introduce + 介: mediate)."
                        ),
                        make_item(
                            "k_ex_12_1", 5, "身", "出身", "しゅっしん",
                            "<u>e. 出身</u> 高校の友人代表（山中、森）",
                            "Representatives of friends from their alma mater high school (Yamanaka, Mori)",
                            "出身高校の友人代表",
                            "<ruby>出身高校<rt>しゅっしんこうこう</rt></ruby>の<ruby>友人代表<rt>ゆうじんだいひょう</rt></ruby>",
                            ["1 しゅっしん", "2 しゅしん", "3 でみ", "4 しゅつしん"],
                            1,
                            "出身（しゅっしん）＝ one's hometown, alma mater, or origin (出: come out + 身: body/status)."
                        ),
                        make_item(
                            "k_ex_12_1", 6, "念", "記念", "きねん",
                            "17時：<u>f. 記念</u> 写真",
                            "17:00: Commemorative photo",
                            "17時：記念写真",
                            "17<ruby>時<rt>じ</rt></ruby>：<ruby>記念写真<rt>きねんしゃしん</rt></ruby>",
                            ["1 きねん", "2 ぎねん", "3 きんねん", "4 けねん"],
                            1,
                            "記念（きねん）＝ commemoration, remembrance (記: record + 念: thought/mind)."
                        )
                    ]
                },
                {
                    "id": "k_ex_12_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct reading or kanji.",
                    "items": [
                        make_item(
                            "k_ex_12_2", 1, "婦", "主婦", "しゅふ",
                            "①今は、かなり多くの<u>主婦</u>が仕事を持っている。",
                            "Nowadays, quite a lot of housewives have jobs.",
                            "今は、かなり多くの主婦が仕事を持っている。",
                            "<ruby>今<rt>いま</rt></ruby>は、かなり<ruby>多<rt>おお</rt></ruby>くの<ruby>主婦<rt>しゅふ</rt></ruby>が<ruby>仕事<rt>しごと</rt></ruby>を<ruby>持<rt>も</rt></ruby>っている。",
                            ["1 しゅうふ", "2 しゅふ", "3 しぇふ", "4 しゅっぷ"],
                            2,
                            "主婦（しゅふ）＝ housewife, homemaker (short vowel しゅ, unlike 夫婦 ふうふ)."
                        ),
                        make_item(
                            "k_ex_12_2", 2, "未", "未来", "みらい",
                            "②<u>みらい</u>は自分の力で変えられる。",
                            "The future can be changed by your own power.",
                            "未来は自分の力で変えられる。",
                            "<ruby>未来<rt>みらい</rt></ruby>は<ruby>自分<rt>じぶん</rt></ruby>の<ruby>力<rt>ちから</rt></ruby>で<ruby>変<rt>か</rt></ruby>えられる。",
                            ["1 未来", "2 末来", "3 朱来", "4 味来"],
                            1,
                            "未来（みらい）＝ future (yet to come). Written with 未 (top horizontal stroke shorter than second), not 末."
                        ),
                        make_item(
                            "k_ex_12_2", 3, "王", "国王", "こくおう",
                            "③来月、A国の<u>こくおう</u>が来日する。",
                            "Next month, the King of Country A will visit Japan.",
                            "来月、A国の国王が来日する。",
                            "<ruby>来月<rt>らいげつ</rt></ruby>、A<ruby>国<rt>こく</rt></ruby>の<ruby>国王<rt>こくおう</rt></ruby>が<ruby>来日<rt>らいにち</rt></ruby>する。",
                            ["1 国帝", "2 国玉", "3 国王", "4 国主"],
                            3,
                            "国王（こくおう）＝ king, monarch (国: country + 王: king)."
                        ),
                        make_item(
                            "k_ex_12_2", 4, "老", "老人", "ろうじん",
                            "④外国語を学ぶ<u>ろうじん</u>が増えているという。",
                            "It is said that the number of elderly people learning foreign languages is increasing.",
                            "外国語を学ぶ老人が増えているという。",
                            "<ruby>外国語<rt>がいこくご</rt></ruby>を<ruby>学<rt>まな</rt></ruby>ぶ<ruby>老人<rt>ろうじん</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えているという。",
                            ["1 老人", "2 考人", "3 孝人", "4 者人"],
                            1,
                            "老人（ろうじん）＝ elderly person, senior citizen (老: old age + 人: person)."
                        ),
                        make_item(
                            "k_ex_12_2", 5, "師", "医師", "いし",
                            "⑤息子は病院で<u>いし</u>として働いている。",
                            "My son works as a doctor at a hospital.",
                            "息子は病院で医師として働いている。",
                            "<ruby>息子<rt>むすこ</rt></ruby>は<ruby>病院<rt>びょういん</rt></ruby>で<ruby>医師<rt>いし</rt></ruby>として<ruby>働<rt>はたら</rt></ruby>いている。",
                            ["1 医氏", "2 医師", "3 医追", "4 医帥"],
                            2,
                            "医師（いし）＝ medical doctor, physician (医: medicine + 師: master/specialist)."
                        )
                    ]
                },
                {
                    "id": "k_ex_12_3",
                    "type": "word_pairing",
                    "title_ja": "3. □には同じ漢字が入ります。[ 達、原、失、身 ] から漢字を選んで書きましょう。下線の部分の読み方も書きましょう。",
                    "title_en": "3. Fill in each pair of blanks with the same kanji from [ 達, 原, 失, 身 ] and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_12_3", 1, "達", "速達", "そくたつ",
                            "①a 手紙が早く着くように、<u>速［　］</u>で出した。",
                            "I sent the letter by express mail so that it would arrive quickly.",
                            "手紙が早く着くように、速達で出した。",
                            "<ruby>手紙<rt>てがみ</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>着<rt>つ</rt></ruby>くように、<ruby>速達<rt>そくたつ</rt></ruby>で<ruby>出<rt>だ</rt></ruby>した。",
                            ["1 達（そくたつ）", "2 原（そくげん）", "3 失（そくしつ）", "4 身（そくしん）"],
                            1,
                            "速達（そくたつ）＝ express mail, special delivery (速: fast + 達: reach/deliver)."
                        ),
                        make_item(
                            "k_ex_12_3", 2, "達", "発達", "はったつ",
                            "①b 子供の言葉は、1歳から3歳ごろまでに急に <u>発［　］</u>する。",
                            "A child's language develops rapidly between ages 1 and 3.",
                            "子供の言葉は、1歳から3歳ごろまでに急に発達する。",
                            "<ruby>子供<rt>こども</rt></ruby>の<ruby>言葉<rt>ことば</rt></ruby>は、1<ruby>歳<rt>さい</rt></ruby>から3<ruby>歳<rt>さい</rt></ruby>ごろまでに<ruby>急<rt>きゅう</rt></ruby>に<ruby>発達<rt>はったつ</rt></ruby>する。",
                            ["1 達（はったつ）", "2 原（はつげん）", "3 失（はっしつ）", "4 身（はっしん）"],
                            1,
                            "発達（はったつ）＝ development, growth (発: develop/emit + 達: attain)."
                        ),
                        make_item(
                            "k_ex_12_3", 3, "身", "出身", "しゅっしん",
                            "②a 私は北海道の <u>出［　］</u>ですが、寒さに弱いです。",
                            "I am from Hokkaido, but I am sensitive to the cold.",
                            "私は北海道の出身ですが、寒さに弱いです。",
                            "<ruby>私<rt>わたし</rt></ruby>は<ruby>北海道<rt>ほっかいどう</rt></ruby>の<ruby>出身<rt>しゅっしん</rt></ruby>ですが、<ruby>寒<rt>さむ</rt></ruby>さに<ruby>弱<rt>よわ</rt></ruby>いです。",
                            ["1 身（しゅっしん）", "2 達（しゅったつ）", "3 原（しゅつげん）", "4 失（しゅっしつ）"],
                            1,
                            "出身（しゅっしん）＝ being from (a place/school)."
                        ),
                        make_item(
                            "k_ex_12_3", 4, "身", "身長", "しんちょう",
                            "②b 彼は <u>［　］長</u>が180cmで、足も長い。",
                            "He is 180 cm tall and has long legs.",
                            "彼は身長が180cmで、足も長い。",
                            "<ruby>彼<rt>かれ</rt></ruby>は<ruby>身長<rt>しんちょう</rt></ruby>が180cmで、<ruby>足<rt>あし</rt></ruby>も<ruby>長<rt>なが</rt></ruby>い。",
                            ["1 身（しんちょう）", "2 達（たっちょう）", "3 原（げんちょう）", "4 失（しっちょう）"],
                            1,
                            "身長（しんちょう）＝ stature, body height (身: body + 長: length)."
                        ),
                        make_item(
                            "k_ex_12_3", 5, "失", "失敗", "しっぱい",
                            "③a 1回ぐらい <u>［　］敗</u>しても、よく反省して次に頑張ればいい。",
                            "Even if you fail once or so, you just need to reflect well and try hard next time.",
                            "1回ぐらい失敗しても、よく反省して次に頑張ればいい。",
                            "1<ruby>回<rt>かい</rt></ruby>ぐらい<ruby>失敗<rt>しっぱい</rt></ruby>しても、よく<ruby>反省<rt>はんせい</rt></ruby>して<ruby>次<rt>つぎ</rt></ruby>に<ruby>頑張<rt>がんば</rt></ruby>ればいい。",
                            ["1 失（しっぱい）", "2 達（たっぱい）", "3 原（げんぱい）", "4 身（しんぱい）"],
                            1,
                            "失敗（しっぱい）＝ failure, mistake (失: lose/miss + 敗: defeat)."
                        ),
                        make_item(
                            "k_ex_12_3", 6, "失", "失業", "しつぎょう",
                            "③b <u>［　］業</u>する人が増えて、社会問題になっている。",
                            "The number of people losing their jobs is increasing, becoming a social problem.",
                            "失業する人が増えて、社会問題になっている。",
                            "<ruby>失業<rt>しつぎょう</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えて、<ruby>社会問題<rt>しゃかいもんだい</rt></ruby>になっている。",
                            ["1 失（しつぎょう）", "2 達（たつぎょう）", "3 原（げんぎょう）", "4 身（しんぎょう）"],
                            1,
                            "失業（しつぎょう）＝ unemployment, losing one's job (失: lose + 業: work/business)."
                        ),
                        make_item(
                            "k_ex_12_3", 7, "因", "原因", "げんいん",
                            "④a 事故の <u>［　］因</u>を調査した。",
                            "We investigated the cause of the accident.",
                            "事故の原因を調査した。",
                            "<ruby>事故<rt>じこ</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>を<ruby>調査<rt>ちょうさ</rt></ruby>した。",
                            ["1 原（げんいん）", "2 失（しついん）", "3 達（たついん）", "4 身（しんいん）"],
                            1,
                            "原因（げんいん）＝ cause, origin, source (原: origin + 因: cause)."
                        ),
                        make_item(
                            "k_ex_12_3", 8, "因", "原料", "げんりょう",
                            "④b 石油はプラスチック製品の <u>［　］料</u>になる。",
                            "Petroleum serves as the raw material for plastic products.",
                            "石油はプラスチック製品の原料になる。",
                            "<ruby>石油<rt>せきゆ</rt></ruby>はプラスチック<ruby>製品<rt>せいひん</rt></ruby>の<ruby>原料<rt>げんりょう</rt></ruby>になる。",
                            ["1 原（げんりょう）", "2 達（たつりょう）", "3 失（しつりょう）", "4 身（しんりょう）"],
                            1,
                            "原料（げんりょう）＝ raw material, ingredient (原: original/raw + 料: material)."
                        )
                    ]
                },
                {
                    "id": "k_ex_12_4",
                    "type": "reading_writing",
                    "title_ja": "4. 下線の部分の漢字には読み方を、平仮名には漢字を書きましょう。(さつきとともやのメール)",
                    "title_en": "4. Give the reading for underlined kanji and kanji for underlined hiragana (Satsuki & Tomoya's Emails).",
                    "items": [
                        make_item(
                            "k_ex_12_4", 1, "婦", "産婦人科", "さんふじんか",
                            "いい知らせ(*^_^*) 午前中、<u>a. 産婦人科</u> に行ってきた。",
                            "Good news! In the morning, I went to the obstetrics and gynecology clinic.",
                            "いい知らせ(*^_^*) 午前中、産婦人科に行ってきた。",
                            "いい<ruby>知<rt>し</rt></ruby>らせ(*^_^*) <ruby>午前中<rt>ごぜんちゅう</rt></ruby>、<ruby>産婦人科<rt>さんふじんか</rt></ruby>に<ruby>行<rt>い</rt></ruby>ってきた。",
                            ["1 さんふじんか", "2 さんぶじんか", "3 さんふしんか", "4 うみふじんか"],
                            1,
                            "産婦人科（さんふじんか）＝ obstetrics and gynecology department/clinic (産: birth + 婦人: woman + 科: department)."
                        ),
                        make_item(
                            "k_ex_12_4", 2, "普", "普通", "ふつう",
                            "でも、どうして言ってくれなかったの？ <u>b. 普通</u>、言うだろ？",
                            "Wait, why didn't you tell me? Normally, you'd tell me, right?",
                            "でも、どうして言ってくれなかったの？ 普通、言うだろ？",
                            "でも、どうして<ruby>言<rt>い</rt></ruby>ってくれなかったの？ <ruby>普通<rt>ふつう</rt></ruby>、<ruby>言<rt>い</rt></ruby>うだろ？",
                            ["1 ふつう", "2 ふうつう", "3 ぶつう", "4 ふっつう"],
                            1,
                            "普通（ふつう）＝ normal, ordinary, usually (普: universal/wide + 通: pass/common)."
                        ),
                        make_item(
                            "k_ex_12_4", 3, "紹", "紹介", "しょうかい",
                            "病院は、かなちゃんが <u>c. しょうかい</u> してくれたところ。",
                            "The hospital is the place Kana-chan introduced to me.",
                            "病院は、かなちゃんが紹介してくれたところ。",
                            "<ruby>病院<rt>びょういん</rt></ruby>は、かなちゃんが<ruby>紹介<rt>しょうかい</rt></ruby>してくれたところ。",
                            ["1 紹介", "2 招介", "3 昭介", "4 照介"],
                            1,
                            "紹介（しょうかい）＝ introduction, referral."
                        ),
                        make_item(
                            "k_ex_12_4", 4, "礼", "お礼", "おれい",
                            "そうか。僕からも彼女に <u>d. おれい</u> を言わなくちゃ。",
                            "I see. I'll have to thank her too.",
                            "そうか。僕からも彼女にお礼を言わなくちゃ。",
                            "そうか。<ruby>僕<rt>ぼく</rt></ruby>からも<ruby>彼女<rt>かのじょ</rt></ruby>にお<ruby>礼<rt>れい</rt></ruby>を<ruby>言<rt>い</rt></ruby>わなくちゃ。",
                            ["1 お礼", "2 お例", "3 お札", "4 お祝"],
                            1,
                            "お礼（おれい）＝ thanks, gratitude, manners (礼: thanks/etiquette)."
                        ),
                        make_item(
                            "k_ex_12_4", 5, "未", "未来", "みらい",
                            "そうだ、僕たちの <u>e. 未来</u> の家族のために、今日はお祝いしよう！",
                            "That's right, let's celebrate today for our future family!",
                            "そうだ、僕たちの未来の家族のために、今日はお祝いしよう！",
                            "そうだ、<ruby>僕<rt>ぼく</rt></ruby>たちの<ruby>未来<rt>みらい</rt></ruby>の<ruby>家族<rt>かぞく</rt></ruby>のために、<ruby>今日<rt>きょう</rt></ruby>はお<ruby>祝<rt>いわ</rt></ruby>いしよう！",
                            ["1 みらい", "2 まらい", "3 みくる", "4 びらい"],
                            1,
                            "未来（みらい）＝ the future."
                        ),
                        make_item(
                            "k_ex_12_4", 6, "約", "約束", "やくそく",
                            "ありがとう♡ <u>f. やくそく</u> ね。",
                            "Thank you! It's a promise!",
                            "ありがとう♡ 約束ね。",
                            "ありがとう♡ <ruby>約束<rt>やくそく</rt></ruby>ね。",
                            ["1 約束", "2 約足", "3 薬束", "4 役束"],
                            1,
                            "約束（やくそく）＝ promise, appointment (約: promise + 束: bundle/bind)."
                        )
                    ]
                }
            ]
        },

        # =====================================================================
        # LESSON 13: 第13回 教育・文化・生活(4) (pp. 51-52)
        # =====================================================================
        {
            "lesson": 13,
            "title_ja": "第13回 教育・文化・生活 (4)",
            "title_en": "Lesson 13: Education, Culture & Daily Life (4)",
            "page_range": "51-52",
            "exercises": [
                {
                    "id": "k_ex_13_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。(夏の講座のお知らせ 市中央センター)",
                    "title_en": "1. Choose the correct reading for the underlined kanji (Summer Course Notice).",
                    "items": [
                        make_item(
                            "k_ex_13_1", 1, "歴", "歴史", "れきし",
                            "8月3日 地域の <u>a. 歴史</u> と文化を考える",
                            "Aug 3: Thinking about local history and culture",
                            "地域の歴史と文化を考える",
                            "<ruby>地域<rt>ちいき</rt></ruby>の<ruby>歴史<rt>れきし</rt></ruby>と<ruby>文化<rt>ぶんか</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>える",
                            ["1 れきし", "2 れっきし", "3 りゃくし", "4 ろうし"],
                            1,
                            "歴史（れきし）＝ history (歴: pass through time + 史: history/chronicle)."
                        ),
                        make_item(
                            "k_ex_13_1", 2, "化", "文化", "ぶんか",
                            "8月3日 地域の歴史と <u>b. 文化</u> を考える",
                            "Aug 3: Thinking about local history and culture",
                            "地域の歴史と文化を考える",
                            "<ruby>地域<rt>ちいき</rt></ruby>の<ruby>歴史<rt>れきし</rt></ruby>と<ruby>文化<rt>ぶんか</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>える",
                            ["1 ぶんか", "2 ぶんが", "3 もんか", "4 ぶっか"],
                            1,
                            "文化（ぶんか）＝ culture (文: literature/civility + 化: change/influence)."
                        ),
                        make_item(
                            "k_ex_13_1", 3, "存", "保存", "ほぞん",
                            "8月5日 食品の <u>c. 保存</u> の方法",
                            "Aug 5: Methods of food preservation",
                            "食品の保存の方法",
                            "<ruby>食品<rt>しょくひん</rt></ruby>の<ruby>保存<rt>ほぞん</rt></ruby>の<ruby>方法<rt>ほうほう</rt></ruby>",
                            ["1 ほぞん", "2 ほそん", "3 ぼうぞん", "4 ほっぞん"],
                            1,
                            "保存（ほぞん）＝ preservation, conservation, saving (file). 存 is read ぞん here."
                        ),
                        make_item(
                            "k_ex_13_1", 4, "化", "化学", "かがく",
                            "8月1日 ペットボトルで <u>d. 化学</u> の実験！",
                            "Aug 1: Chemistry experiments with plastic bottles!",
                            "ペットボトルで化学の実験！",
                            "ペットボトルで<ruby>化学<rt>かがく</rt></ruby>の<ruby>実験<rt>じっけん</rt></ruby>！",
                            ["1 かがく", "2 ばけがく", "3 けがく", "4 かっがく"],
                            1,
                            "化学（かがく）＝ chemistry (化: transform + 学: study)."
                        ),
                        make_item(
                            "k_ex_13_1", 5, "疑", "疑問", "ぎもん",
                            "身近な <u>e. 疑問</u> を調べよう",
                            "Let's investigate everyday questions/doubts",
                            "身近な疑問を調べよう",
                            "<ruby>身近<rt>みぢか</rt></ruby>な<ruby>疑問<rt>ぎもん</rt></ruby>を<ruby>調<rt>しら</rt></ruby>べよう",
                            ["1 ぎもん", "2 きもん", "3 ぎぶん", "4 うたがもん"],
                            1,
                            "疑問（ぎもん）＝ question, doubt (疑: doubt + 問: question)."
                        ),
                        make_item(
                            "k_ex_13_1", 6, "読", "読書", "どくしょ",
                            "8月10日 <u>f. 読書</u> の感想を書こう",
                            "Aug 10: Let's write our impressions of reading books",
                            "読書の感想を書こう",
                            "<ruby>読書<rt>どくしょ</rt></ruby>の<ruby>感想<rt>かんそう</rt></ruby>を<ruby>書<rt>か</rt></ruby>こう",
                            ["1 どくしょ", "2 とくしょ", "3 よみしょ", "4 どくしょう"],
                            1,
                            "読書（どくしょ）＝ reading books (読: read + 書: book)."
                        ),
                        make_item(
                            "k_ex_13_1", 7, "想", "感想", "かんそう",
                            "8月10日 読書の <u>g. 感想</u> を書こう",
                            "Aug 10: Let's write our impressions of reading books",
                            "読書の感想を書こう",
                            "<ruby>読書<rt>どくしょ</rt></ruby>の<ruby>感想<rt>かんそう</rt></ruby>を<ruby>書<rt>か</rt></ruby>こう",
                            ["1 かんそう", "2 かんぞう", "3 がんそう", "4 かんしょう"],
                            1,
                            "感想（かんそう）＝ impressions, thoughts, feelings (感: feel + 想: thought)."
                        )
                    ]
                },
                {
                    "id": "k_ex_13_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct reading or kanji.",
                    "items": [
                        make_item(
                            "k_ex_13_2", 1, "対", "対", "たい",
                            "①試合は5<u>対</u>3で勝った。",
                            "We won the match 5 to 3.",
                            "試合は5対3で勝った。",
                            "<ruby>試合<rt>しあい</rt></ruby>は5<ruby>対<rt>たい</rt></ruby>3で<ruby>勝<rt>か</rt></ruby>った。",
                            ["1 つい", "2 たい", "3 と", "4 だい"],
                            2,
                            "対（たい）＝ versus / to (in scores like 5対3: ごたいさん)."
                        ),
                        make_item(
                            "k_ex_13_2", 2, "存", "ご存じ", "ごぞんじ",
                            "②田中先生を<u>ご存じ</u>ですか。",
                            "Do you know Professor Tanaka?",
                            "田中先生をご存じですか。",
                            "<ruby>田中先生<rt>たなかせんせい</rt></ruby>をご<ruby>存<rt>ぞん</rt></ruby>じですか。",
                            ["1 ごそんじ", "2 ごぞんじ", "3 ごそうじ", "4 ござんじ"],
                            2,
                            "ご存じ（ごぞんじ）＝ knowing (honorific of 知っている)."
                        ),
                        make_item(
                            "k_ex_13_2", 3, "愛", "愛情", "あいじょう",
                            "③子供の成長には、<u>あいじょう</u>が必要です。",
                            "Love and affection are necessary for a child's growth.",
                            "子供の成長には、愛情が必要です。",
                            "<ruby>子供<rt>こども</rt></ruby>の<ruby>成長<rt>せいちょう</rt></ruby>には、<ruby>愛情<rt>あいじょう</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>です。",
                            ["1 愛情", "2 愛清", "3 愛晴", "4 憂情"],
                            1,
                            "愛情（あいじょう）＝ love, affection (愛: love + 情: emotion/feeling)."
                        ),
                        make_item(
                            "k_ex_13_2", 4, "想", "予想", "よそう",
                            "④その<u>よそう</u>は全く外れてしまった。",
                            "That prediction was completely off the mark.",
                            "その予想は全く外れてしまった。",
                            "その<ruby>予想<rt>よそう</rt></ruby>は<ruby>全<rt>まった</rt></ruby>く<ruby>外<rt>はず</rt></ruby>れてしまった。",
                            ["1 予箱", "2 予想", "3 予霜", "4 予相"],
                            2,
                            "予想（よそう）＝ expectation, prediction, forecast (予: beforehand + 想: conceive/think)."
                        ),
                        make_item(
                            "k_ex_13_2", 5, "才", "才能", "さいのう",
                            "⑤彼女にはピアノの<u>さいのう</u>がある。",
                            "She has a talent for the piano.",
                            "彼女にはピアノの才能がある。",
                            "<ruby>彼女<rt>かのじょ</rt></ruby>にはピアノの<ruby>才能<rt>さいのう</rt></ruby>がある。",
                            ["1 才能", "2 丈能", "3 寸能", "4 財能"],
                            1,
                            "才能（さいのう）＝ talent, ability (才: talent/genius + 能: ability)."
                        )
                    ]
                },
                {
                    "id": "k_ex_13_3",
                    "type": "sentence_fill",
                    "title_ja": "3. [ 検、不、満、可、反 ] の中から漢字を選んで、文を完成しましょう。読み方も書きましょう。",
                    "title_en": "3. Choose a kanji from [ 検, 不, 満, 可, 反 ] to complete the sentence and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_13_3", 1, "満", "満足", "まんぞく",
                            "①今の生活に<u>［　］</u>足しています。",
                            "I am satisfied with my current life.",
                            "今の生活に満足しています。",
                            "<ruby>今<rt>いま</rt></ruby>の<ruby>生活<rt>せいかつ</rt></ruby>に<ruby>満足<rt>まんぞく</rt></ruby>しています。",
                            ["1 満（まんぞく）", "2 不（ふそく）", "3 可（かぞく）", "4 反（はんぞく）"],
                            1,
                            "満足（まんぞく）＝ satisfaction (満: full + 足: sufficient)."
                        ),
                        make_item(
                            "k_ex_13_3", 2, "検", "検査", "けんさ",
                            "②目が疲れて本が読めないので、病院で<u>［　］</u>査してもらった。",
                            "Because my eyes were tired and I couldn't read books, I had them examined at the hospital.",
                            "目が疲れて本が読めないので、病院で検査してもらった。",
                            "<ruby>目<rt>め</rt></ruby>が<ruby>疲<rt>つか</rt></ruby>れて<ruby>本<rt>ほん</rt></ruby>が<ruby>読<rt>よ</rt></ruby>めないので、<ruby>病院<rt>びょういん</rt></ruby>で<ruby>検査<rt>けんさ</rt></ruby>してもらった。",
                            ["1 検（けんさ）", "2 反（はんさ）", "3 可（かさ）", "4 満（まんさ）"],
                            1,
                            "検査（けんさ）＝ inspection, medical examination, test (検: examine + 査: investigate)."
                        ),
                        make_item(
                            "k_ex_13_3", 3, "省", "反省", "はんせい",
                            "③私たちは、練習が足りなかったことを<u>［　］</u>省した。",
                            "We reflected on the fact that we hadn't practiced enough.",
                            "私たちは、練習が足りなかったことを反省した。",
                            "<ruby>私<rt>わたし</rt></ruby>たちは、<ruby>練習<rt>れんしゅう</rt></ruby>が<ruby>足<rt>た</rt></ruby>りなかったことを<ruby>反省<rt>はんせい</rt></ruby>した。",
                            ["1 反（はんせい）", "2 検（けんせい）", "3 不（ふせい）", "4 満（まんせい）"],
                            1,
                            "反省（はんせい）＝ reflection, reconsideration, regret (反: turn back + 省: examine oneself)."
                        ),
                        make_item(
                            "k_ex_13_3", 4, "足", "不足", "ふそく",
                            "④忙しくて、睡眠時間が<u>［　］</u>足している。",
                            "I'm so busy that I'm lacking sleep time.",
                            "忙しくて、睡眠時間が不足している。",
                            "<ruby>忙<rt>いそが</rt></ruby>しくて、<ruby>睡眠時間<rt>すいみんじかん</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>している。",
                            ["1 不（ふそく）", "2 満（まんぞく）", "3 反（はんそく）", "4 可（かそく）"],
                            1,
                            "不足（ふそく）＝ insufficiency, shortage, lack (不: not + 足: enough)."
                        ),
                        make_item(
                            "k_ex_13_3", 5, "可", "可能", "かのう",
                            "⑤買ってから1週間以内なら、お取り替えが<u>［　］</u>能です。",
                            "Within one week of purchase, exchange is possible.",
                            "買ってから1週間以内なら、お取り替えが可能です。",
                            "<ruby>買<rt>か</rt></ruby>ってから1<ruby>週間以内<rt>しゅうかんいない</rt></ruby>なら、お<ruby>取<rt>と</rt></ruby>り<ruby>替<rt>か</rt></ruby>えが<ruby>可能<rt>かのう</rt></ruby>です。",
                            ["1 可（かのう）", "2 不（ふのう）", "3 検（けんのう）", "4 反（はんのう）"],
                            1,
                            "可能（かのう）＝ possible, feasible (可: possible/permit + 能: ability)."
                        )
                    ]
                },
                {
                    "id": "k_ex_13_4",
                    "type": "reading_recall",
                    "title_ja": "4. 下線の部分の読み方を書きましょう。(「結婚と家庭」についてのアンケート)",
                    "title_en": "4. Choose the correct reading for the underlined kanji (Survey on Marriage and Family).",
                    "items": [
                        make_item(
                            "k_ex_13_4", 1, "才", "20〜29才", "さい",
                            "年齢：20〜29<u>a. 才</u>",
                            "Age: 20–29 years old",
                            "年齢：20〜29才",
                            "<ruby>年齢<rt>ねんれい</rt></ruby>：20〜29<ruby>才<rt>さい</rt></ruby>",
                            ["1 さい", "2 ざい", "3 とし", "4 だい"],
                            1,
                            "才（さい）＝ years old (commonly used as a simpler alternative to 歳)."
                        ),
                        make_item(
                            "k_ex_13_4", 2, "愛", "愛", "あい",
                            "①「<u>b. 愛</u> があれば、お金はなくてもいい」という意見に賛成ですか。",
                            "Do you agree with the opinion that 'as long as you have love, you don't need money'?",
                            "「愛があれば、お金はなくてもいい」という意見に賛成ですか。",
                            "「<ruby>愛<rt>あい</rt></ruby>があれば、お<ruby>金<rt>かね</rt></ruby>はなくてもいい」という<ruby>意見<rt>いけん</rt></ruby>に<ruby>賛成<rt>さんせい</rt></ruby>ですか。",
                            ["1 あい", "2 こい", "3 じょう", "4 めぐみ"],
                            1,
                            "愛（あい）＝ love."
                        ),
                        make_item(
                            "k_ex_13_4", 3, "歴", "学歴", "がくれき",
                            "②結婚相手の <u>c. 学歴</u> について、どう思いますか。",
                            "What do you think about a marriage partner's educational background?",
                            "結婚相手の学歴について、どう思いますか。",
                            "<ruby>結婚相手<rt>けっこんあいて</rt></ruby>の<ruby>学歴<rt>がくれき</rt></ruby>について、どう<ruby>思<rt>おも</rt></ruby>いますか。",
                            ["1 がくれき", "2 がっくり", "3 がくれきし", "4 まなびれき"],
                            1,
                            "学歴（がくれき）＝ academic/educational background (学: study + 歴: personal history)."
                        ),
                        make_item(
                            "k_ex_13_4", 4, "反", "反対", "はんたい",
                            "③親が <u>d. 反対</u> したら、好きな人でも別れますか。",
                            "If your parents opposed it, would you break up even with someone you love?",
                            "親が反対したら、好きな人でも別れますか。",
                            "<ruby>親<rt>おや</rt></ruby>が<ruby>反対<rt>はんたい</rt></ruby>したら、<ruby>好<rt>す</rt></ruby>きな<ruby>人<rt>ひと</rt></ruby>でも<ruby>別<rt>わか</rt></ruby>れますか。",
                            ["1 はんたい", "2 ばんたい", "3 はんだい", "4 へんたい"],
                            1,
                            "反対（はんたい）＝ opposition, objection, opposite (反: against + 対: oppose)."
                        ),
                        make_item(
                            "k_ex_13_4", 5, "責", "責任", "せきにん",
                            "④子供の教育は、父親と母親のどちらの <u>e. 責任</u> のほうが大きいと思いますか。",
                            "Whose responsibility do you think is greater for a child's education, the father's or the mother's?",
                            "子供の教育は、父親と母親のどちらの責任のほうが大きいと思いますか。",
                            "<ruby>子供<rt>こども</rt></ruby>の<ruby>教育<rt>きょういく</rt></ruby>は、<ruby>父親<rt>ちちおや</rt></ruby>と<ruby>母親<rt>ははおや</rt></ruby>のどちらの<ruby>責任<rt>せきにん</rt></ruby>のほうが<ruby>大<rt>おお</rt></ruby>きいと<ruby>思<rt>おも</rt></ruby>いますか。",
                            ["1 せきにん", "2 ぜきにん", "3 せいにん", "4 しゃくにん"],
                            1,
                            "責任（せきにん）＝ responsibility, duty (責: blame/duty + 任: entrust/duty)."
                        ),
                        make_item(
                            "k_ex_13_4", 6, "想", "理想", "りそう",
                            "⑤あなたの <u>f. 理想</u> の家庭は、どんな家庭ですか。",
                            "What kind of family is your ideal family?",
                            "あなたの理想の家庭は、どんな家庭ですか。",
                            "あなたの<ruby>理想<rt>りそう</rt></ruby>の<ruby>家庭<rt>かてい</rt></ruby>は、どんな<ruby>家庭<rt>かてい</rt></ruby>ですか。",
                            ["1 りそう", "2 りぞう", "3 りっそう", "4 りしょう"],
                            1,
                            "理想（りそう）＝ ideal (理: principle/reason + 想: thought/conception)."
                        )
                    ]
                }
            ]
        },

        # =====================================================================
        # LESSON 14: 第14回 教育・文化・生活(5) (pp. 53-55)
        # =====================================================================
        {
            "lesson": 14,
            "title_ja": "第14回 教育・文化・生活 (5)",
            "title_en": "Lesson 14: Education, Culture & Daily Life (5)",
            "page_range": "53-55",
            "exercises": [
                {
                    "id": "k_ex_14_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。(みほちゃんの会話)",
                    "title_en": "1. Choose the correct reading for the underlined kanji (Miho's Conversation).",
                    "items": [
                        make_item(
                            "k_ex_14_1", 1, "夫", "夫婦", "ふうふ",
                            "うん、来月でね。でも、まだ <u>a. 夫婦</u> という感じがしないわ。",
                            "Yeah, next month. But it still doesn't feel like we're a married couple.",
                            "でも、まだ夫婦という感じがしないわ。",
                            "でも、まだ<ruby>夫婦<rt>ふうふ</rt></ruby>という<ruby>感<rt>かん</rt></ruby>じがしないわ。",
                            ["1 ふうふ", "2 ふふ", "3 おっとふ", "4 ぶうふ"],
                            1,
                            "夫婦（ふうふ）＝ married couple, husband and wife (note the long vowel ふう)."
                        ),
                        make_item(
                            "k_ex_14_1", 2, "夫", "夫", "おっと",
                            "<u>b. 夫</u> じゃなくて恋人って感じかな。",
                            "It feels more like he's my boyfriend rather than my husband.",
                            "夫じゃなくて恋人って感じかな。",
                            "<ruby>夫<rt>おっと</rt></ruby>じゃなくて<ruby>恋人<rt>こいびと</rt></ruby>って<ruby>感<rt>かん</rt></ruby>じかな。",
                            ["1 おっと", "2 ふう", "3 おと", "4 しゅじん"],
                            1,
                            "夫（おっと）＝ husband (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_1", 3, "勤", "勤めて", "つとめて",
                            "まあね。でも、<u>c. 勤めて</u> いる会社が近いから、朝はゆっくり出勤できるし…",
                            "Well, yes. But since the company I work for is close by, I can take my time going to work in the morning...",
                            "でも、勤めている会社が近いから、朝はゆっくり出勤できるし…",
                            "でも、<ruby>勤<rt>つと</rt></ruby>めている<ruby>会社<rt>かいしゃ</rt></ruby>が<ruby>近<rt>ちか</rt></ruby>いから、<ruby>朝<rt>あさ</rt></ruby>はゆっくり<ruby>出勤<rt>しゅっきん</rt></ruby>できるし…",
                            ["1 つとめて", "2 きめて", "3 はじめて", "4 あつめて"],
                            1,
                            "勤める（つとめる）＝ to work for, to be employed at."
                        ),
                        make_item(
                            "k_ex_14_1", 4, "勤", "出勤", "しゅっきん",
                            "…朝はゆっくり <u>d. 出勤</u> できるし、彼もよくやってくれるから。",
                            "...I can go to work at a relaxed pace in the morning, and he also helps out a lot.",
                            "朝はゆっくり出勤できるし、彼もよくやってくれるから。",
                            "<ruby>朝<rt>あさ</rt></ruby>はゆっくり<ruby>出勤<rt>しゅっきん</rt></ruby>できるし、<ruby>彼<rt>かれ</rt></ruby>もよくやってくれるから。",
                            ["1 しゅっきん", "2 しゅつきん", "3 でづとめ", "4 しゅうきん"],
                            1,
                            "出勤（しゅっきん）＝ going to work, attendance at work."
                        ),
                        make_item(
                            "k_ex_14_1", 5, "連", "連休", "れんきゅう",
                            "今度の <u>e. 連休</u> は、両方の両親を連れて温泉に行くの。",
                            "On the upcoming consecutive holidays, we're taking both sets of parents to a hot spring.",
                            "今度の連休は、両方の両親を連れて温泉に行くの。",
                            "<ruby>今度<rt>こんど</rt></ruby>の<ruby>連休<rt>れんきゅう</rt></ruby>は、<ruby>両方<rt>りょうほう</rt></ruby>の<ruby>両親<rt>りょうしん</rt></ruby>を<ruby>連<rt>つ</rt></ruby>れて<ruby>温泉<rt>おんせん</rt></ruby>に<ruby>行<rt>い</rt></ruby>くの。",
                            ["1 れんきゅう", "2 れんきゅ", "3 つれやすみ", "4 れんぎゅう"],
                            1,
                            "連休（れんきゅう）＝ consecutive holidays (連: consecutive/link + 休: holiday)."
                        ),
                        make_item(
                            "k_ex_14_1", 6, "連", "連れて", "つれて",
                            "今度の連休は、両方の両親を <u>f. 連れて</u> 温泉に行くの。",
                            "On the upcoming consecutive holidays, we're taking both sets of parents to a hot spring.",
                            "今度の連休は、両方の両親を連れて温泉に行くの。",
                            "<ruby>今度<rt>こんど</rt></ruby>の<ruby>連休<rt>れんきゅう</rt></ruby>は、<ruby>両方<rt>りょうほう</rt></ruby>の<ruby>両親<rt>りょうしん</rt></ruby>を<ruby>連<rt>つ</rt></ruby>れて<ruby>温泉<rt>おんせん</rt></ruby>に<ruby>行<rt>い</rt></ruby>くの。",
                            ["1 つれて", "2 れんれて", "3 つられて", "4 はなれて"],
                            1,
                            "連れる（つれる）＝ to take/bring someone along."
                        )
                    ]
                },
                {
                    "id": "k_ex_14_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct reading.",
                    "items": [
                        make_item(
                            "k_ex_14_2", 1, "香", "香水", "こうすい",
                            "①この <u>a. 香水</u> の香りが好きです。",
                            "I like the fragrance of this perfume.",
                            "この香水の香りが好きです。",
                            "この<ruby>香水<rt>こうすい</rt></ruby>の<ruby>香<rt>かお</rt></ruby>りが<ruby>好<rt>す</rt></ruby>きです。",
                            ["1 こうずい", "2 こうすい", "3 かおりみず", "4 きょうすい"],
                            2,
                            "香水（こうすい）＝ perfume (香: fragrance + 水: water)."
                        ),
                        make_item(
                            "k_ex_14_2", 2, "香", "香り", "かおり",
                            "①この香水の <u>b. 香り</u> が好きです。",
                            "I like the fragrance of this perfume.",
                            "この香水の香りが好きです。",
                            "この<ruby>香水<rt>こうすい</rt></ruby>の<ruby>香<rt>かお</rt></ruby>りが<ruby>好<rt>す</rt></ruby>きです。",
                            ["1 かおり", "2 におり", "3 こうり", "4 かかり"],
                            1,
                            "香り（かおり）＝ fragrance, aroma, pleasant scent."
                        ),
                        make_item(
                            "k_ex_14_2", 3, "忘", "忘年会", "ぼうねんかい",
                            "②来週の<u>忘年会</u>には出席されますか。",
                            "Will you attend next week's year-end party?",
                            "来週の忘年会には出席されますか。",
                            "<ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>忘年会<rt>ぼうねんかい</rt></ruby>には<ruby>出席<rt>しゅっせき</rt></ruby>されますか。",
                            ["1 ぼねんかい", "2 ぼうねんかい", "3 わすねんかい", "4 もうねんかい"],
                            2,
                            "忘年会（ぼうねんかい）＝ year-end party (lit. 'forget-the-year gathering')."
                        ),
                        make_item(
                            "k_ex_14_2", 4, "血", "出血", "しゅっけつ",
                            "③<u>出血</u>がひどいので、救急車を呼んだ。",
                            "Because the bleeding was severe, I called an ambulance.",
                            "出血がひどいので、救急車を呼んだ。",
                            "<ruby>出血<rt>しゅっけつ</rt></ruby>がひどいので、<ruby>救急車<rt>きゅうきゅうしゃ</rt></ruby>を<ruby>呼<rt>よ</rt></ruby>んだ。",
                            ["1 しゅうけつ", "2 しゅっけつ", "3 しゅげつ", "4 でち"],
                            2,
                            "出血（しゅっけつ）＝ bleeding, hemorrhage (出: come out + 血: blood)."
                        )
                    ]
                },
                {
                    "id": "k_ex_14_3",
                    "type": "word_pairing",
                    "title_ja": "3. □には同じ漢字が入ります。[ 夢、庭、幸、君 ] から漢字を選んで書きましょう。下線の部分の読み方も書きましょう。",
                    "title_en": "3. Fill in each pair of blanks with the same kanji from [ 夢, 庭, 幸, 君 ] and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_14_3", 1, "庭", "家庭", "かてい",
                            "①a 父は、仕事も <u>家［　］</u>も大切にする人だった。",
                            "My father was a person who valued both work and family.",
                            "父は、仕事も家庭も大切にする人だった。",
                            "<ruby>父<rt>ちち</rt></ruby>は、<ruby>仕事<rt>しごと</rt></ruby>も<ruby>家庭<rt>かてい</rt></ruby>も<ruby>大切<rt>たいせつ</rt></ruby>にする<ruby>人<rt>ひと</rt></ruby>だった。",
                            ["1 庭（かてい）", "2 幸（かこう）", "3 夢（かむ）", "4 君（かくん）"],
                            1,
                            "家庭（かてい）＝ home, family, household (家: house + 庭: yard/court)."
                        ),
                        make_item(
                            "k_ex_14_3", 2, "庭", "庭", "にわ",
                            "①b 今度引っ越した家は、<u>［　］</u>があるので、いろいろな花を育てたい。",
                            "Since the house we just moved into has a garden, I want to grow various flowers.",
                            "今度引っ越した家は、庭があるので、いろいろな花を育てたい。",
                            "<ruby>今度<rt>こんど</rt></ruby><ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>した<ruby>家<rt>いえ</rt></ruby>は、<ruby>庭<rt>にわ</rt></ruby>があるので、いろいろな<ruby>花<rt>はな</rt></ruby>を<ruby>育<rt>そだ</rt></ruby>てたい。",
                            ["1 庭（にわ）", "2 幸（しあわせ）", "3 夢（ゆめ）", "4 君（きみ）"],
                            1,
                            "庭（にわ）＝ garden, yard (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_3", 3, "君", "田中君", "たなかくん",
                            "②a 会議で、社長から、「<u>田中［　］</u>、君はどう思う？」と意見を聞かれた。",
                            "At the meeting, the president asked for my opinion: 'Tanaka-kun, what do you think?'",
                            "会議で、社長から、「田中君、君はどう思う？」と意見を聞かれた。",
                            "<ruby>会議<rt>かいぎ</rt></ruby>で、<ruby>社長<rt>しゃちょう</rt></ruby>から、「<ruby>田中君<rt>たなかくん</rt></ruby>、<ruby>君<rt>きみ</rt></ruby>はどう<ruby>思<rt>おも</rt></ruby>う？」と<ruby>意見<rt>いけん</rt></ruby>を<ruby>聞<rt>き</rt></ruby>かれた。",
                            ["1 君（たなかくん）", "2 幸（たなかこう）", "3 庭（たなかてい）", "4 夢（たなかむ）"],
                            1,
                            "〜君（くん）＝ Mr. / master (familiar suffix used after a name)."
                        ),
                        make_item(
                            "k_ex_14_3", 4, "君", "君", "きみ",
                            "②b 会議で、社長から、「田中君、<u>［　］</u>はどう思う？」と意見を聞かれた。",
                            "At the meeting, the president asked for my opinion: 'Tanaka-kun, what do you think?'",
                            "会議で、社長から、「田中君、君はどう思う？」と意見を聞かれた。",
                            "<ruby>会議<rt>かいぎ</rt></ruby>で、<ruby>社長<rt>しゃちょう</rt></ruby>から、「<ruby>田中君<rt>たなかくん</rt></ruby>、<ruby>君<rt>きみ</rt></ruby>はどう<ruby>思<rt>おも</rt></ruby>う？」と<ruby>意見<rt>いけん</rt></ruby>を<ruby>聞<rt>き</rt></ruby>かれた。",
                            ["1 君（きみ）", "2 夢（ゆめ）", "3 庭（にわ）", "4 幸（さち）"],
                            1,
                            "君（きみ）＝ you (informal/familiar pronoun)."
                        ),
                        make_item(
                            "k_ex_14_3", 5, "夢", "夢中", "むちゅう",
                            "③a 息子は新しいゲームに <u>［　］中</u>になっている。",
                            "My son is absorbed in his new game.",
                            "息子は新しいゲームに夢中になっている。",
                            "<ruby>息子<rt>むすこ</rt></ruby>は<ruby>新<rt>あたら</rt></ruby>しいゲームに<ruby>夢中<rt>むちゅう</rt></ruby>になっている。",
                            ["1 夢（むちゅう）", "2 幸（こうちゅう）", "3 庭（ていちゅう）", "4 君（くんちゅう）"],
                            1,
                            "夢中（むちゅう）＝ absorbed in, crazy about, entranced (夢: dream + 中: middle)."
                        ),
                        make_item(
                            "k_ex_14_3", 6, "夢", "夢", "ゆめ",
                            "③b 自分の会社を作ることは、子供の頃からの <u>［　］</u>だった。",
                            "Starting my own company had been my dream since childhood.",
                            "自分の会社を作ることは、子供の頃からの夢だった。",
                            "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>会社<rt>かいしゃ</rt></ruby>を<ruby>作<rt>つく</rt></ruby>ることは、<ruby>子供<rt>こども</rt></ruby>の<ruby>頃<rt>ころ</rt></ruby>からの<ruby>夢<rt>ゆめ</rt></ruby>だった。",
                            ["1 夢（ゆめ）", "2 幸（しあわせ）", "3 庭（にわ）", "4 君（きみ）"],
                            1,
                            "夢（ゆめ）＝ dream (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_3", 7, "幸", "幸せ", "しあわせ",
                            "④a 好きな人と結婚できて <u>［　］せ</u>だ。",
                            "I am happy to have married the person I love.",
                            "好きな人と結婚できて幸せだ。",
                            "<ruby>好<rt>す</rt></ruby>きな<ruby>人<rt>ひと</rt></ruby>と<ruby>結婚<rt>けっこん</rt></ruby>できて<ruby>幸<rt>しあわ</rt></ruby>せだ。",
                            ["1 幸（しあわせ）", "2 夢（ゆめせ）", "3 庭（にわせ）", "4 君（きみせ）"],
                            1,
                            "幸せ（しあわせ）＝ happiness, good fortune (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_3", 8, "幸", "幸福", "こうふく",
                            "④b みんなが <u>［　］福</u>に生活できる社会に、早くなってほしい。",
                            "I hope we soon become a society where everyone can live happily.",
                            "みんなが幸福に生活できる社会に、早くなってほしい。",
                            "みんなが<ruby>幸福<rt>こうふく</rt></ruby>に<ruby>生活<rt>せいかつ</rt></ruby>できる<ruby>社会<rt>しゃかい</rt></ruby>に、<ruby>早<rt>はや</rt></ruby>くなってほしい。",
                            ["1 幸（こうふく）", "2 夢（むふく）", "3 庭（ていふく）", "4 君（くんふく）"],
                            1,
                            "幸福（こうふく）＝ happiness, blessedness, welfare (幸: happiness + 福: fortune)."
                        )
                    ]
                },
                {
                    "id": "k_ex_14_4",
                    "type": "radical_assembly",
                    "title_ja": "4. [ 妾、辶、心、关 ] の中から漢字の部分を選んで、漢字を完成しましょう。読み方も書きましょう。",
                    "title_en": "4. Choose a component from [ 妾, 辶, 心, 关 ] to complete the kanji and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_14_4", 1, "関", "関心", "かんしん",
                            "①今度の選挙の結果に、国民は強い <u>[ 門＋？ ]心</u> を持っている。",
                            "Citizens have a strong interest in the results of the upcoming election.",
                            "今度の選挙の結果に、国民は強い関心を持っている。",
                            "<ruby>今度<rt>こんど</rt></ruby>の<ruby>選挙<rt>せんきょ</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>に、<ruby>国民<rt>こくみん</rt></ruby>は<ruby>強<rt>つよ</rt></ruby>い<ruby>関心<rt>かんしん</rt></ruby>を<ruby>持<rt>も</rt></ruby>っている。",
                            ["1 門＋关＝関心（かんしん）", "2 門＋心＝悶心（もんしん）", "3 門＋妾＝関接（かんせつ）", "4 門＋辶＝連心（れんしん）"],
                            1,
                            "門 + 关 = 関. 関心（かんしん）＝ interest, concern."
                        ),
                        make_item(
                            "k_ex_14_4", 2, "接", "面接", "めんせつ",
                            "②次の <u>面[ 扌＋？ ]</u> に合格すれば、就職が決まる。",
                            "If I pass the next interview, I will get the job.",
                            "次の面接に合格すれば、就職が決まる。",
                            "<ruby>次<rt>つぎ</rt></ruby>の<ruby>面接<rt>めんせつ</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>すれば、<ruby>就職<rt>しゅうしょく</rt></ruby>が<ruby>決<rt>き</rt></ruby>まる。",
                            ["1 扌＋妾＝面接（めんせつ）", "2 扌＋关＝面関（めんかん）", "3 扌＋心＝面忘（めんぼう）", "4 扌＋辶＝面連（めんれん）"],
                            1,
                            "扌 (hand radical) + 妾 = 接. 面接（めんせつ）＝ interview."
                        ),
                        make_item(
                            "k_ex_14_4", 3, "連", "連れて", "つれて",
                            "③行き方が分からなかったので、木村さんに <u>[ ？＋車 ]れて</u> いってもらった。",
                            "Because I didn't know how to get there, I had Kimura-san take me along.",
                            "行き方が分からなかったので、木村さんに連れていってもらった。",
                            "<ruby>行<rt>い</rt></ruby>き<ruby>方<rt>かた</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からなかったので、<ruby>木村<rt>きむら</rt></ruby>さんに<ruby>連<rt>つ</rt></ruby>れていってもらった。",
                            ["1 辶＋車＝連れて（つれて）", "2 心＋車＝忘て（わすれて）", "3 关＋車＝関て（かかわって）", "4 妾＋車＝接て（つげて）"],
                            1,
                            "辶 (movement radical) + 車 = 連. 連れて（つれて）＝ taking someone along."
                        ),
                        make_item(
                            "k_ex_14_4", 4, "忘", "忘れて", "わすれて",
                            "④結婚記念日を <u>[ 亡＋？ ]れて</u>、妻に怒られてしまった。",
                            "I forgot our wedding anniversary and my wife got angry at me.",
                            "結婚記念日を忘れて、妻に怒られてしまった。",
                            "<ruby>結婚記念日<rt>けっこんきねんび</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れて、<ruby>妻<rt>つま</rt></ruby>に<ruby>怒<rt>おこ</rt></ruby>られてしまった。",
                            ["1 亡＋心＝忘れて（わすれて）", "2 亡＋辶＝連て（つれて）", "3 亡＋关＝関て（かんして）", "4 亡＋妾＝接て（せして）"],
                            1,
                            "亡 + 心 (heart radical) = 忘. 忘れる（わすれる）＝ to forget."
                        )
                    ]
                },
                {
                    "id": "k_ex_14_5",
                    "type": "reading_writing",
                    "title_ja": "5. 下線の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
                    "title_en": "5. Give the reading for underlined kanji and kanji for underlined hiragana.",
                    "items": [
                        make_item(
                            "k_ex_14_5", 1, "他", "他", "ほか",
                            "① <u>a. 他</u> に質問がある場合は、係の者にお聞きください。",
                            "If you have any other questions, please ask the person in charge.",
                            "他に質問がある場合は、係の者にお聞きください。",
                            "<ruby>他<rt>ほか</rt></ruby>に<ruby>質問<rt>しつもん</rt></ruby>がある<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>係<rt>かかり</rt></ruby>の<ruby>者<rt>もの</rt></ruby>にお<ruby>聞<rt>き</rt></ruby>きください。",
                            ["1 ほか", "2 た", "3 ちが", "4 よそ"],
                            1,
                            "他に（ほかに）＝ besides, in addition, other (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_5", 2, "係", "係", "かかり",
                            "① 他に質問がある場合は、<u>b. 係</u> の者にお聞きください。",
                            "If you have any other questions, please ask the person in charge.",
                            "他に質問がある場合は、係の者にお聞きください。",
                            "<ruby>他<rt>ほか</rt></ruby>に<ruby>質問<rt>しつもん</rt></ruby>がある<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>係<rt>かかり</rt></ruby>の<ruby>者<rt>もの</rt></ruby>にお<ruby>聞<rt>き</rt></ruby>きください。",
                            ["1 かかり", "2 けい", "3 かかわり", "4 つなぎ"],
                            1,
                            "係（かかり）＝ person in charge, attendant, duty."
                        ),
                        make_item(
                            "k_ex_14_5", 3, "他", "他人", "たにん",
                            "② <u>a. 他人</u> から注意される前に、自分でやり方を見直したほうがいい。",
                            "You should review your own way of doing things before being warned by others.",
                            "他人から注意される前に、自分でやり方を見直したほうがいい。",
                            "<ruby>他人<rt>たにん</rt></ruby>から<ruby>注意<rt>ちゅうい</rt></ruby>される<ruby>前<rt>まえ</rt></ruby>に、<ruby>自分<rt>じぶん</rt></ruby>でやり<ruby>方<rt>かた</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>したほうがいい。",
                            ["1 たにん", "2 ほかにん", "3 たじん", "4 ほかひと"],
                            1,
                            "他人（たにん）＝ other people, strangers, outsiders (on-reading た)."
                        ),
                        make_item(
                            "k_ex_14_5", 4, "直", "見直した", "みなおした",
                            "② 他人から注意される前に、自分でやり方を <u>b. 見直した</u> ほうがいい。",
                            "You should review your own way of doing things before being warned by others.",
                            "他人から注意される前に、自分でやり方を見直したほうがいい。",
                            "<ruby>他人<rt>たにん</rt></ruby>から<ruby>注意<rt>ちゅうい</rt></ruby>される<ruby>前<rt>まえ</rt></ruby>に、<ruby>自分<rt>じぶん</rt></ruby>でやり<ruby>方<rt>かた</rt></ruby>を<ruby>見直<rt>みなお</rt></ruby>したほうがいい。",
                            ["1 みなおした", "2 みちょくした", "3 みじかした", "4 みただした"],
                            1,
                            "見直す（みなおす）＝ to look at again, to review, to reconsider."
                        ),
                        make_item(
                            "k_ex_14_5", 5, "歯", "歯", "は",
                            "③ <u>a. 歯</u> が痛くて、ちも出ていたので、朝すぐに近所の歯科に行った。",
                            "Because my tooth hurt and was bleeding, I went straight to the neighborhood dentist in the morning.",
                            "歯が痛くて、血も出ていたので、朝すぐに近所の歯科に行った。",
                            "<ruby>歯<rt>は</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>くて、<ruby>血<rt>ち</rt></ruby>も<ruby>出<rt>で</rt></ruby>ていたので、<ruby>朝<rt>あさ</rt></ruby>すぐに<ruby>近所<rt>きんじょ</rt></ruby>の<ruby>歯科<rt>しか</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                            ["1 は", "2 し", "3 はぐき", "4 きば"],
                            1,
                            "歯（は）＝ tooth, teeth (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_5", 6, "血", "血", "ち",
                            "③ 歯が痛くて、<u>b. ち</u> も出ていたので、朝すぐに近所の歯科に行った。",
                            "Because my tooth hurt and was bleeding, I went straight to the neighborhood dentist in the morning.",
                            "歯が痛くて、血も出ていたので、朝すぐに近所の歯科に行った。",
                            "<ruby>歯<rt>は</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>くて、<ruby>血<rt>ち</rt></ruby>も<ruby>出<rt>で</rt></ruby>ていたので、<ruby>朝<rt>あさ</rt></ruby>すぐに<ruby>近所<rt>きんじょ</rt></ruby>の<ruby>歯科<rt>しか</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                            ["1 血", "2 皿", "3 汗", "4 涙"],
                            1,
                            "血（ち）＝ blood (kun-reading)."
                        ),
                        make_item(
                            "k_ex_14_5", 7, "歯", "歯科", "しか",
                            "③ 歯が痛くて、ちも出ていたので、朝すぐに近所の <u>c. 歯科</u> に行った。",
                            "Because my tooth hurt and was bleeding, I went straight to the neighborhood dentist in the morning.",
                            "歯が痛くて、血も出ていたので、朝すぐに近所の歯科に行った。",
                            "<ruby>歯<rt>は</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>くて、<ruby>血<rt>ち</rt></ruby>も<ruby>出<rt>で</rt></ruby>ていたので、<ruby>朝<rt>あさ</rt></ruby>すぐに<ruby>近所<rt>きんじょ</rt></ruby>の<ruby>歯科<rt>しか</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                            ["1 しか", "2 はか", "3 しいか", "4 じか"],
                            1,
                            "歯科（しか）＝ dentistry, dental clinic (歯: tooth, on-reading し + 科: department)."
                        ),
                        make_item(
                            "k_ex_14_5", 8, "直", "直線", "ちょくせん",
                            "④ここから富士山まで、<u>直線</u>の距離で約200キロだ。",
                            "From here to Mt. Fuji, it is about 200 km in a straight-line distance.",
                            "ここから富士山まで、直線の距離で約200キロだ。",
                            "ここから<ruby>富士山<rt>ふじさん</rt></ruby>まで、<ruby>直線<rt>ちょくせん</rt></ruby>の<ruby>距離<rt>きょり</rt></ruby>で<ruby>約<rt>やく</rt></ruby>200キロだ。",
                            ["1 ちょくせん", "2 じきせん", "3 なおせん", "4 ちょうせん"],
                            1,
                            "直線（ちょくせん）＝ straight line (直: straight + 線: line)."
                        )
                    ]
                },
                {
                    "id": "k_ex_14_6",
                    "type": "reading_recall",
                    "title_ja": "6. 下線の部分の読み方を書きましょう。(通勤時間と幸福についての調査)",
                    "title_en": "6. Choose the correct reading for the underlined kanji (Survey on Commuting Time and Happiness).",
                    "items": [
                        make_item(
                            "k_ex_14_6", 1, "勤", "通勤", "つうきん",
                            "アメリカで <u>a. 通勤</u> 時間と幸福だと感じる程度の関係について、調査が行われた。",
                            "In the US, a survey was conducted on the relationship between commuting time and the degree of feeling happy.",
                            "アメリカで通勤時間と幸福だと感じる程度の関係について、調査が行われた。",
                            "アメリカで<ruby>通勤時間<rt>つうきんじかん</rt></ruby>と<ruby>幸福<rt>こうふく</rt></ruby>だと<ruby>感<rt>かん</rt></ruby>じる<ruby>程度<rt>ていど</rt></ruby>の<ruby>関係<rt>かんけい</rt></ruby>について、<ruby>調査<rt>ちょうさ</rt></ruby>が<ruby>行<rt>おこな</rt></ruby>われた。",
                            ["1 つうきん", "2 つうぎん", "3 ときん", "4 かよいきん"],
                            1,
                            "通勤（つうきん）＝ commuting to work (通: commute + 勤: work)."
                        ),
                        make_item(
                            "k_ex_14_6", 2, "福", "幸福", "こうふく",
                            "アメリカで通勤時間と <u>b. 幸福</u> だと感じる程度の関係について、調査が行われた。",
                            "In the US, a survey was conducted on the relationship between commuting time and the degree of feeling happy.",
                            "アメリカで通勤時間と幸福だと感じる程度の関係について、調査が行われた。",
                            "アメリカで<ruby>通勤時間<rt>つうきんじかん</rt></ruby>と<ruby>幸福<rt>こうふく</rt></ruby>だと<ruby>感<rt>かん</rt></ruby>じる<ruby>程度<rt>ていど</rt></ruby>の<ruby>関係<rt>かんけい</rt></ruby>について、<ruby>調査<rt>ちょうさ</rt></ruby>が<ruby>行<rt>おこな</rt></ruby>われた。",
                            ["1 こうふく", "2 しあわふく", "3 さちふく", "4 こうぶく"],
                            1,
                            "幸福（こうふく）＝ happiness, well-being."
                        ),
                        make_item(
                            "k_ex_14_6", 3, "関", "関係", "かんけい",
                            "アメリカで通勤時間と幸福だと感じる程度の <u>c. 関係</u> について、調査が行われた。",
                            "In the US, a survey was conducted on the relationship between commuting time and the degree of feeling happy.",
                            "アメリカで通勤時間と幸福だと感じる程度の関係について、調査が行われた。",
                            "アメリカで<ruby>通勤時間<rt>つうきんじかん</rt></ruby>と<ruby>幸福<rt>こうふく</rt></ruby>だと<ruby>感<rt>かん</rt></ruby>じる<ruby>程度<rt>ていど</rt></ruby>の<ruby>関係<rt>かんけい</rt></ruby>について、<ruby>調査<rt>ちょうさ</rt></ruby>が<ruby>行<rt>おこな</rt></ruby>われた。",
                            ["1 かんけい", "2 かんがい", "3 かんかかり", "4 れんけい"],
                            1,
                            "関係（かんけい）＝ relationship, connection (関: connection + 係: relation)."
                        ),
                        make_item(
                            "k_ex_14_6", 4, "庭", "家庭", "かてい",
                            "通勤時間が長いと、<u>d. 家庭</u> での夫婦の会話も少なくなるだろう。",
                            "When commuting time is long, conversations between husband and wife at home also likely decrease.",
                            "通勤時間が長いと、家庭での夫婦の会話も少なくなるだろう。",
                            "<ruby>通勤時間<rt>つうきんじかん</rt></ruby>が<ruby>長<rt>なが</rt></ruby>いと、<ruby>家庭<rt>かてい</rt></ruby>での<ruby>夫婦<rt>ふうふ</rt></ruby>の<ruby>会話<rt>かいわ</rt></ruby>も<ruby>少<rt>すく</rt></ruby>なくなるだろう。",
                            ["1 かてい", "2 かにわ", "3 いえてい", "4 かじょう"],
                            1,
                            "家庭（かてい）＝ home, household, family."
                        ),
                        make_item(
                            "k_ex_14_6", 5, "夫", "夫婦", "ふうふ",
                            "通勤時間が長いと、家庭での <u>e. 夫婦</u> の会話も少なくなるだろう。",
                            "When commuting time is long, conversations between husband and wife at home also likely decrease.",
                            "通勤時間が長いと、家庭での夫婦の会話も少なくなるだろう。",
                            "<ruby>通勤時間<rt>つうきんじかん</rt></ruby>が<ruby>長<rt>なが</rt></ruby>いと、<ruby>家庭<rt>かてい</rt></ruby>での<ruby>夫婦<rt>ふうふ</rt></ruby>の<ruby>会話<rt>かいわ</rt></ruby>も<ruby>少<rt>すく</rt></ruby>なくなるだろう。",
                            ["1 ふうふ", "2 ふふ", "3 おっとふ", "4 ぶうふ"],
                            1,
                            "夫婦（ふうふ）＝ husband and wife, married couple."
                        ),
                        make_item(
                            "k_ex_14_6", 6, "幸", "幸せ", "しあわせ",
                            "また、一日の行動の中でも、朝の通勤を <u>f. 幸せ</u> だと感じる人はほとんどいなかったという。",
                            "Also, among daily activities, almost no one felt that the morning commute was a happy time.",
                            "また、一日の行動の中でも、朝の通勤を幸せだと感じる人はほとんどいなかったという。",
                            "また、<ruby>一日<rt>いちにち</rt></ruby>の<ruby>行動<rt>こうどう</rt></ruby>の<ruby>中<rt>なか</rt></ruby>でも、<ruby>朝<rt>あさ</rt></ruby>の<ruby>通勤<rt>つうきん</rt></ruby>を<ruby>幸<rt>しあわ</rt></ruby>せだと<ruby>感<rt>かん</rt></ruby>じる<ruby>人<rt>ひと</rt></ruby>はほとんどいなかったという。",
                            ["1 しあわせ", "2 こうせ", "3 さちせ", "4 さいわせ"],
                            1,
                            "幸せ（しあわせ）＝ happy, happiness."
                        ),
                        make_item(
                            "k_ex_14_6", 7, "勤", "勤める", "つとめる",
                            "近い職場に <u>g. 勤める</u> ことは、通勤時間が長い人にとっては夢かもしれない。",
                            "Working at a nearby workplace might be a dream for people with long commutes.",
                            "近い職場に勤めることは、通勤時間が長い人にとっては夢かもしれない。",
                            "<ruby>近<rt>ちか</rt></ruby>い<ruby>職場<rt>しょくば</rt></ruby>に<ruby>勤<rt>つと</rt></ruby>めることは、<ruby>通勤時間<rt>つうきんじかん</rt></ruby>が<ruby>長<rt>なが</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>にとっては<ruby>夢<rt>ゆめ</rt></ruby>かもしれない。",
                            ["1 つとめる", "2 きめる", "3 やめる", "4 すすめる"],
                            1,
                            "勤める（つとめる）＝ to work at, to be employed at."
                        ),
                        make_item(
                            "k_ex_14_6", 8, "夢", "夢", "ゆめ",
                            "近い職場に勤めることは、通勤時間が長い人にとっては <u>h. 夢</u> かもしれない。",
                            "Working at a nearby workplace might be a dream for people with long commutes.",
                            "近い職場に勤めることは、通勤時間が長い人にとっては夢かもしれない。",
                            "<ruby>近<rt>ちか</rt></ruby>い<ruby>職場<rt>しょくば</rt></ruby>に<ruby>勤<rt>つと</rt></ruby>めることは、<ruby>通勤時間<rt>つうきんじかん</rt></ruby>が<ruby>長<rt>なが</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>にとっては<ruby>夢<rt>ゆめ</rt></ruby>かもしれない。",
                            ["1 ゆめ", "2 む", "3 のぞみ", "4 まぼろし"],
                            1,
                            "夢（ゆめ）＝ dream."
                        )
                    ]
                }
            ]
        },

        # =====================================================================
        # SUMMARY TEST 3 (まとめ問題(4) in book, pp. 56-57)
        # =====================================================================
        {
            "lesson": "summary_3",
            "title_ja": "まとめ問題 (4) (第11回〜第14回)",
            "title_en": "Review Test (Lessons 11-14)",
            "page_range": "56-57",
            "exercises": [
                {
                    "id": "k_ex_sum3_1",
                    "type": "multiple_choice_reading",
                    "title_ja": "1. 下線の言葉の読み方として最もよいものを、1・2・3・4から一つ選びましょう。",
                    "title_en": "1. Choose the best reading for the underlined words from 1, 2, 3, or 4.",
                    "items": [
                        make_item(
                            "k_ex_sum3_1", 1, "国", "国立", "こくりつ",
                            "①<u>国立</u>の大学に入りたい。",
                            "I want to enter a national university.",
                            "国立の大学に入りたい。",
                            "<ruby>国立<rt>こくりつ</rt></ruby>の<ruby>大学<rt>だいがく</rt></ruby>に<ruby>入<rt>はい</rt></ruby>りたい。",
                            ["1 こくたち", "2 こくりつ", "3 くにりつ", "4 くにたつ"],
                            2,
                            "国立（こくりつ）＝ national (established by the state)."
                        ),
                        make_item(
                            "k_ex_sum3_1", 2, "勤", "通勤", "つうきん",
                            "②夫は毎日電車で<u>通勤</u>している。",
                            "My husband commutes to work by train every day.",
                            "夫は毎日電車で通勤している。",
                            "<ruby>夫<rt>おっと</rt></ruby>は<ruby>毎日電車<rt>まいにちでんしゃ</rt></ruby>で<ruby>通勤<rt>つうきん</rt></ruby>している。",
                            ["1 とおぎん", "2 つうぎん", "3 とおきん", "4 つうきん"],
                            4,
                            "通勤（つうきん）＝ commuting to work."
                        ),
                        make_item(
                            "k_ex_sum3_1", 3, "礼", "失礼", "しつれい",
                            "③会っても挨拶もしない。彼は本当に<u>失礼</u>な人だ。",
                            "He doesn't even greet me when we meet. He is truly a rude person.",
                            "会っても挨拶もしない。彼は本当に失礼な人だ。",
                            "<ruby>会<rt>あ</rt></ruby>っても<ruby>挨拶<rt>あいさつ</rt></ruby>もしない。<ruby>彼<rt>かれ</rt></ruby>は<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>失礼<rt>しつれい</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>だ。",
                            ["1 しっれん", "2 しっれい", "3 しつれえ", "4 しつれい"],
                            4,
                            "失礼（しつれい）＝ rude, impolite, discourtesy (失: lose/lack + 礼: courtesy)."
                        ),
                        make_item(
                            "k_ex_sum3_1", 4, "満", "満員", "まんいん",
                            "④この電車は、いつも<u>満員</u>だ。",
                            "This train is always packed/full of passengers.",
                            "この電車は、いつも満員だ。",
                            "この<ruby>電車<rt>でんしゃ</rt></ruby>は、いつも<ruby>満員<rt>まんいん</rt></ruby>だ。",
                            ["1 まいん", "2 まんいん", "3 まんにん", "4 まんい"],
                            2,
                            "満員（まんいん）＝ full capacity, crowded (満: full + 員: member/people)."
                        ),
                        make_item(
                            "k_ex_sum3_1", 5, "幸", "不幸", "ふこう",
                            "⑤今まで<u>不幸</u>な人生だったが、今はとても幸せだ。",
                            "Until now I had an unhappy life, but now I am very happy.",
                            "今まで不幸な人生だったが、今はとても幸せだ。",
                            "<ruby>今<rt>いま</rt></ruby>まで<ruby>不幸<rt>ふこう</rt></ruby>な<ruby>人生<rt>じんせい</rt></ruby>だったが、<ruby>今<rt>いま</rt></ruby>はとても<ruby>幸<rt>しあわ</rt></ruby>せだ。",
                            ["1 ふっこう", "2 ふうこ", "3 ふうごう", "4 ふこう"],
                            4,
                            "不幸（ふこう）＝ unhappiness, misfortune (不: un- + 幸: happiness, on-reading こう)."
                        )
                    ]
                },
                {
                    "id": "k_ex_sum3_2",
                    "type": "multiple_choice_kanji",
                    "title_ja": "2. 下線の言葉を漢字で書くとき、最もよいものを、1・2・3・4から一つ選びましょう。",
                    "title_en": "2. Choose the best kanji for the underlined words from 1, 2, 3, or 4.",
                    "items": [
                        make_item(
                            "k_ex_sum3_2", 1, "席", "席", "せき",
                            "①電車でお年寄りに<u>せき</u>を譲った。",
                            "I gave up my seat to an elderly person on the train.",
                            "電車でお年寄りに席を譲った。",
                            "<ruby>電車<rt>でんしゃ</rt></ruby>でお<ruby>年寄<rt>としよ</rt></ruby>りに<ruby>席<rt>せき</rt></ruby>を<ruby>譲<rt>ゆず</rt></ruby>った。",
                            ["1 席", "2 度", "3 店", "4 庶"],
                            1,
                            "席（せき）＝ seat."
                        ),
                        make_item(
                            "k_ex_sum3_2", 2, "給", "給料", "きゅうりょう",
                            "②この会社は休みも多いし、<u>きゅうりょう</u>も高い。",
                            "This company has many holidays, and the salary is also high.",
                            "この会社は休みも多いし、給料も高い。",
                            "この<ruby>会社<rt>かいしゃ</rt></ruby>は<ruby>休<rt>やす</rt></ruby>みも<ruby>多<rt>おお</rt></ruby>いし、<ruby>給料<rt>きゅうりょう</rt></ruby>も<ruby>高<rt>たか</rt></ruby>い。",
                            ["1 紛料", "2 給料", "3 給科", "4 紹科"],
                            2,
                            "給料（きゅうりょう）＝ salary, wages (給: provide + 料: fee/pay)."
                        ),
                        make_item(
                            "k_ex_sum3_2", 3, "予", "予報", "よほう",
                            "③天気<u>よほう</u>によると、明日は晴れるそうだ。",
                            "According to the weather forecast, it will be sunny tomorrow.",
                            "天気予報によると、明日は晴れるそうだ。",
                            "<ruby>天気予報<rt>てんきよほう</rt></ruby>によると、<ruby>明日<rt>あした</rt></ruby>は<ruby>晴<rt>は</rt></ruby>れるそうだ。",
                            ["1 矛報", "2 予報", "3 予服", "4 矛服"],
                            2,
                            "予報（よほう）＝ forecast, prediction (予: beforehand + 報: report)."
                        ),
                        make_item(
                            "k_ex_sum3_2", 4, "他", "他", "ほか",
                            "④その<u>ほか</u>に質問はありませんか。",
                            "Are there any other questions besides that?",
                            "その他に質問はありませんか。",
                            "その<ruby>他<rt>ほか</rt></ruby>に<ruby>質問<rt>しつもん</rt></ruby>はありませんか。",
                            ["1 弛", "2 地", "3 池", "4 他"],
                            4,
                            "他（ほか）＝ other, besides (イ person radical + 也)."
                        ),
                        make_item(
                            "k_ex_sum3_2", 5, "修", "研修", "けんしゅう",
                            "⑤新しく会社に入った社員は、全員<u>けんしゅう</u>を受けなければならない。",
                            "All employees who newly joined the company must undergo training.",
                            "新しく会社に入った社員は、全員研修を受けなければならない。",
                            "<ruby>新<rt>あたら</rt></ruby>しく<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>った<ruby>社員<rt>しゃいん</rt></ruby>は、<ruby>全員研修<rt>ぜんいんけんしゅう</rt></ruby>を<ruby>受<rt>う</rt></ruby>けなければならない。",
                            ["1 検修", "2 研條", "3 研修", "4 検條"],
                            3,
                            "研修（けんしゅう）＝ training, study seminar (研: polish/study + 修: master/cultivate)."
                        )
                    ]
                },
                {
                    "id": "k_ex_sum3_3",
                    "type": "reading_recall",
                    "title_ja": "3. 下線の部分の読み方を書きましょう。",
                    "title_en": "3. Choose the correct reading for the underlined kanji.",
                    "items": [
                        make_item(
                            "k_ex_sum3_3", 1, "直", "直して", "なおして",
                            "①a 間違えた漢字を先生に <u>a. 直して</u> もらった。",
                            "I had the teacher correct the kanji I got wrong.",
                            "間違えた漢字を先生に直してもらった。",
                            "<ruby>間違<rt>まちが</rt></ruby>えた<ruby>漢字<rt>かんじ</rt></ruby>を<ruby>先生<rt>せんせい</rt></ruby>に<ruby>直<rt>なお</rt></ruby>してもらった。",
                            ["1 なおして", "2 ちょくして", "3 じきして", "4 ただして"],
                            1,
                            "直す（なおす）＝ to correct, to fix."
                        ),
                        make_item(
                            "k_ex_sum3_3", 2, "直", "直接", "ちょくせつ",
                            "①b この書類は、<u>b. 直接</u> 窓口まで持ってきてください。",
                            "Please bring this document directly to the counter.",
                            "この書類は、直接窓口まで持ってきてください。",
                            "この<ruby>書類<rt>しょるい</rt></ruby>は、<ruby>直接窓口<rt>ちょくせつまどぐち</rt></ruby>まで<ruby>持<rt>も</rt></ruby>ってきてください。",
                            ["1 ちょくせつ", "2 じきせつ", "3 なおせつ", "4 ちょっせつ"],
                            1,
                            "直接（ちょくせつ）＝ directly, in person (直: direct + 接: contact)."
                        ),
                        make_item(
                            "k_ex_sum3_3", 3, "失", "失業", "しつぎょう",
                            "②c <u>c. 失業</u> した人の数は、今年のほうが去年より少なくなっている。",
                            "The number of unemployed people is smaller this year than last year.",
                            "失業した人の数は、今年のほうが去年より少なくなっている。",
                            "<ruby>失業<rt>しつぎょう</rt></ruby>した<ruby>人<rt>ひと</rt></ruby>の<ruby>数<rt>かず</rt></ruby>は、<ruby>今年<rt>ことし</rt></ruby>のほうが<ruby>去年<rt>きょねん</rt></ruby>より<ruby>少<rt>すく</rt></ruby>なくなっている。",
                            ["1 しつぎょう", "2 しっぎょう", "3 うしぎょう", "4 しつごう"],
                            1,
                            "失業（しつぎょう）＝ unemployment."
                        ),
                        make_item(
                            "k_ex_sum3_3", 4, "失", "失敗", "しっぱい",
                            "②d 過去の <u>d. 失敗</u> から学ぶことが大切だ。",
                            "It is important to learn from past failures.",
                            "過去の失敗から学ぶことが大切だ。",
                            "<ruby>過去<rt>かこ</rt></ruby>の<ruby>失敗<rt>しっぱい</rt></ruby>から<ruby>学<rt>まな</rt></ruby>ぶことが<ruby>大切<rt>たいせつ</rt></ruby>だ。",
                            ["1 しっぱい", "2 しつぱい", "3 しつはい", "4 しっばい"],
                            1,
                            "失敗（しっぱい）＝ failure, mistake."
                        ),
                        make_item(
                            "k_ex_sum3_3", 5, "法", "文法", "ぶんぽう",
                            "③e 私は <u>e. 文法</u> と漢字が苦手だ。",
                            "I am weak at grammar and kanji.",
                            "私は文法と漢字が苦手だ。",
                            "<ruby>私<rt>わたし</rt></ruby>は<ruby>文法<rt>ぶんぽう</rt></ruby>と<ruby>漢字<rt>かんじ</rt></ruby>が<ruby>苦手<rt>にがて</rt></ruby>だ。",
                            ["1 ぶんぽう", "2 ぶんほう", "3 もんぽう", "4 ぶんぼう"],
                            1,
                            "文法（ぶんぽう）＝ grammar (法 changes from ほう to ぽう after ん)."
                        ),
                        make_item(
                            "k_ex_sum3_3", 6, "法", "方法", "ほうほう",
                            "③f もっと簡単にできる <u>f. 方法</u> を考えた。",
                            "I thought of an easier method to do it.",
                            "もっと簡単にできる方法を考えた。",
                            "もっと<ruby>簡単<rt>かんたん</rt></ruby>にできる<ruby>方法<rt>ほうほう</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>えた。",
                            ["1 ほうほう", "2 ほうぽう", "3 かたほう", "4 ぼうほう"],
                            1,
                            "方法（ほうほう）＝ method, way, manner."
                        ),
                        make_item(
                            "k_ex_sum3_3", 7, "足", "不足", "ふそく",
                            "④g この地域では医師が <u>g. 不足</u> している。",
                            "Doctors are in short supply in this region.",
                            "この地域では医師が不足している。",
                            "この<ruby>地域<rt>ちいき</rt></ruby>では<ruby>医師<rt>いし</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>している。",
                            ["1 ふそく", "2 ふぞく", "3 ぶそく", "4 ふたり"],
                            1,
                            "不足（ふそく）＝ shortage, insufficiency (no rendaku on そく)."
                        ),
                        make_item(
                            "k_ex_sum3_3", 8, "満", "満足", "まんぞく",
                            "④h 彼は今の生活に <u>h. 満足</u> している。",
                            "He is satisfied with his current life.",
                            "彼は今の生活に満足している。",
                            "<ruby>彼<rt>かれ</rt></ruby>は<ruby>今<rt>いま</rt></ruby>の<ruby>生活<rt>せいかつ</rt></ruby>に<ruby>満足<rt>まんぞく</rt></ruby>している。",
                            ["1 まんぞく", "2 まんそく", "3 まぞく", "4 ばんぞく"],
                            1,
                            "満足（まんぞく）＝ satisfaction (rendaku ぞく after ん)."
                        ),
                        make_item(
                            "k_ex_sum3_3", 9, "算", "計算", "けいさん",
                            "⑤i 子供のとき、<u>i. 計算</u> が嫌いで、特に引き算が苦手だった。",
                            "When I was a child, I hated calculation, and was especially bad at subtraction.",
                            "子供のとき、計算が嫌いで、特に引き算が苦手だった。",
                            "<ruby>子供<rt>こども</rt></ruby>のとき、<ruby>計算<rt>けいさん</rt></ruby>が<ruby>嫌<rt>きら</rt></ruby>いで、<ruby>特<rt>とく</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>き<ruby>算<rt>ざん</rt></ruby>が<ruby>苦手<rt>にがて</rt></ruby>だった。",
                            ["1 けいさん", "2 けいざん", "3 かぞさん", "4 けっさん"],
                            1,
                            "計算（けいさん）＝ calculation, arithmetic."
                        ),
                        make_item(
                            "k_ex_sum3_3", 10, "算", "引き算", "ひきざん",
                            "⑤j 子供のとき、計算が嫌いで、特に <u>j. 引き算</u> が苦手だった。",
                            "When I was a child, I hated calculation, and was especially bad at subtraction.",
                            "子供のとき、計算が嫌いで、特に引き算が苦手だった。",
                            "<ruby>子供<rt>こども</rt></ruby>のとき、<ruby>計算<rt>けいさん</rt></ruby>が<ruby>嫌<rt>きら</rt></ruby>いで、<ruby>特<rt>とく</rt></ruby>に<ruby>引<rt>ひ</rt></ruby>き<ruby>算<rt>ざん</rt></ruby>が<ruby>苦手<rt>にがて</rt></ruby>だった。",
                            ["1 ひきざん", "2 ひきさん", "3 いんざん", "4 ひっざん"],
                            1,
                            "引き算（ひきざん）＝ subtraction (算 voices to ざん in arithmetic operation names like 足し算, 引き算, 掛け算, 割り算)."
                        )
                    ]
                },
                {
                    "id": "k_ex_sum3_4",
                    "type": "reading_writing",
                    "title_ja": "4. 下線の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
                    "title_en": "4. Give the reading for underlined kanji and kanji for underlined hiragana.",
                    "items": [
                        make_item(
                            "k_ex_sum3_4", 1, "短", "短所", "たんしょ",
                            "①a 彼の <u>a. 短所</u> は、よく忘れ物をするところだ。",
                            "His shortcoming is that he often forgets things.",
                            "彼の短所は、よく忘れ物をするところだ。",
                            "<ruby>彼<rt>かれ</rt></ruby>の<ruby>短所<rt>たんしょ</rt></ruby>は、よく<ruby>忘<rt>わす</rt></ruby>れ<ruby>物<rt>もの</rt></ruby>をするところだ。",
                            ["1 たんしょ", "2 たんじょ", "3 みじかしょ", "4 だんしょ"],
                            1,
                            "短所（たんしょ）＝ shortcoming, weak point, flaw (opposite of 長所: ちょうしょ)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 2, "忘", "忘れ物", "わすれもの",
                            "①b 彼の短所は、よく <u>b. 忘れ物</u> をするところだ。",
                            "His shortcoming is that he often forgets things.",
                            "彼の短所は、よく忘れ物をするところだ。",
                            "<ruby>彼<rt>かれ</rt></ruby>の<ruby>短所<rt>たんしょ</rt></ruby>は、よく<ruby>忘<rt>わす</rt></ruby>れ<ruby>物<rt>もの</rt></ruby>をするところだ。",
                            ["1 わすれもの", "2 ぼうれもの", "3 わすれぶつ", "4 おくれもの"],
                            1,
                            "忘れ物（わすれもの）＝ lost/forgotten article, something left behind."
                        ),
                        make_item(
                            "k_ex_sum3_4", 3, "非", "非常に", "ひじょうに",
                            "②c この問題の解決は、<u>c. 非常に</u> 難しい。",
                            "Solving this problem is extremely difficult.",
                            "この問題の解決は、非常に難しい。",
                            "この<ruby>問題<rt>もんだい</rt></ruby>の<ruby>解決<rt>かいけつ</rt></ruby>は、<ruby>非常<rt>ひじょう</rt></ruby>に<ruby>難<rt>むずか</rt></ruby>しい。",
                            ["1 ひじょうに", "2 びじょうに", "3 ひっじょうに", "4 ふじょうに"],
                            1,
                            "非常に（ひじょうに）＝ very, extremely, exceedingly."
                        ),
                        make_item(
                            "k_ex_sum3_4", 4, "局", "結局", "けっきょく",
                            "③d 妹は嫌がっていたが、<u>d. 結局</u> はいしゃに行った。",
                            "My younger sister was reluctant, but in the end she went to the dentist.",
                            "妹は嫌がっていたが、結局歯医者に行った。",
                            "<ruby>妹<rt>いもうと</rt></ruby>は<ruby>嫌<rt>いや</rt></ruby>がっていたが、<ruby>結局<rt>けっきょく</rt></ruby><ruby>歯医者<rt>はいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                            ["1 けっきょく", "2 けつきょく", "3 けっきょう", "4 むすきょく"],
                            1,
                            "結局（けっきょく）＝ after all, in the end, eventually."
                        ),
                        make_item(
                            "k_ex_sum3_4", 5, "歯", "歯医者", "はいしゃ",
                            "③e 妹は嫌がっていたが、結局 <u>e. はいしゃ</u> に行った。",
                            "My younger sister was reluctant, but in the end she went to the dentist.",
                            "妹は嫌がっていたが、結局歯医者に行った。",
                            "<ruby>妹<rt>いもうと</rt></ruby>は<ruby>嫌<rt>いや</rt></ruby>がっていたが、<ruby>結局<rt>けっきょく</rt></ruby><ruby>歯医者<rt>はいしゃ</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                            ["1 歯医者", "2 歯科者", "3 羽医者", "4 齢医者"],
                            1,
                            "歯医者（はいしゃ）＝ dentist (歯: tooth + 医者: doctor)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 6, "段", "階段", "かいだん",
                            "④f <u>f. 階段</u> のでんきゅうが切れてしまって、とても暗い。",
                            "The lightbulb on the stairs burned out, so it is very dark.",
                            "階段の電球が切れてしまって、とても暗い。",
                            "<ruby>階段<rt>かいだん</rt></ruby>の<ruby>電球<rt>でんきゅう</rt></ruby>が<ruby>切<rt>き</rt></ruby>れてしまって、とても<ruby>暗<rt>くら</rt></ruby>い。",
                            ["1 かいだん", "2 がいだん", "3 かいたん", "4 かいだんじ"],
                            1,
                            "階段（かいだん）＝ stairs, stairway (階: story/step + 段: step)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 7, "球", "電球", "でんきゅう",
                            "④g 階段の <u>g. でんきゅう</u> が切れてしまって、とても暗い。",
                            "The lightbulb on the stairs burned out, so it is very dark.",
                            "階段の電球が切れてしまって、とても暗い。",
                            "<ruby>階段<rt>かいだん</rt></ruby>の<ruby>電球<rt>でんきゅう</rt></ruby>が<ruby>切<rt>き</rt></ruby>れてしまって、とても<ruby>暗<rt>くら</rt></ruby>い。",
                            ["1 電球", "2 電求", "3 電救", "4 電休"],
                            1,
                            "電球（でんきゅう）＝ lightbulb (電: electric + 球: globe/bulb)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 8, "約", "約", "やく",
                            "⑤h この学校には、<u>h. やく</u> 50人の教師がいる。",
                            "There are about 50 teachers at this school.",
                            "この学校には、約50人の教師がいる。",
                            "この<ruby>学校<rt>がっこう</rt></ruby>には、<ruby>約<rt>やく</rt></ruby>50<ruby>人<rt>にん</rt></ruby>の<ruby>教師<rt>きょうし</rt></ruby>がいる。",
                            ["1 約", "2 役", "3 薬", "4 訳"],
                            1,
                            "約（やく）＝ approximately, about."
                        ),
                        make_item(
                            "k_ex_sum3_4", 9, "師", "教師", "きょうし",
                            "⑤i この学校には、やく50人の <u>i. 教師</u> がいる。",
                            "There are about 50 teachers at this school.",
                            "この学校には、約50人の教師がいる。",
                            "この<ruby>学校<rt>がっこう</rt></ruby>には、<ruby>約<rt>やく</rt></ruby>50<ruby>人<rt>にん</rt></ruby>の<ruby>教師<rt>きょうし</rt></ruby>がいる。",
                            ["1 きょうし", "2 きょし", "3 きょうじ", "4 おしえし"],
                            1,
                            "教師（きょうし）＝ teacher, instructor (教: teach + 師: master/teacher)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 10, "具", "絵の具", "えのぐ",
                            "⑥j 子供たちは、<u>j. 絵の具</u> で絵を描いたり、がっきを弾いたりしていた。",
                            "The children were painting pictures with paints and playing musical instruments.",
                            "子供たちは、絵の具で絵を描いたり、楽器を弾いたりしていた。",
                            "<ruby>子供<rt>こども</rt></ruby>たちは、<ruby>絵<rt>え</rt></ruby>の<ruby>具<rt>ぐ</rt></ruby>で<ruby>絵<rt>え</rt></ruby>を<ruby>描<rt>か</rt></ruby>いたり、<ruby>楽器<rt>がっき</rt></ruby>を<ruby>弾<rt>ひ</rt></ruby>いたりしていた。",
                            ["1 えのぐ", "2 えのく", "3 かいぐ", "4 えのぐう"],
                            1,
                            "絵の具（えのぐ）＝ paints, coloring materials (絵: picture + の + 具: tool/material)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 11, "器", "楽器", "がっき",
                            "⑥k 子供たちは、絵の具で絵を描いたり、<u>k. がっき</u> を弾いたりしていた。",
                            "The children were painting pictures with paints and playing musical instruments.",
                            "子供たちは、絵の具で絵を描いたり、楽器を弾いたりしていた。",
                            "<ruby>子供<rt>こども</rt></ruby>たちは、<ruby>絵<rt>え</rt></ruby>の<ruby>具<rt>ぐ</rt></ruby>で<ruby>絵<rt>え</rt></ruby>を<ruby>描<rt>か</rt></ruby>いたり、<ruby>楽器<rt>がっき</rt></ruby>を<ruby>弾<rt>ひ</rt></ruby>いたりしていた。",
                            ["1 楽器", "2 楽機", "3 楽期", "4 楽気"],
                            1,
                            "楽器（がっき）＝ musical instrument (楽: music + 器: instrument/vessel)."
                        ),
                        make_item(
                            "k_ex_sum3_4", 12, "線", "点線", "てんせん",
                            "⑦l <u>l. てんせん</u> のとおりに紙を切ってください。",
                            "Please cut the paper along the dotted line.",
                            "点線のとおりに紙を切ってください。",
                            "<ruby>点線<rt>てんせん</rt></ruby>のとおりに<ruby>紙<rt>かみ</rt></ruby>を<ruby>切<rt>き</rt></ruby>ってください。",
                            ["1 点線", "2 天線", "3 店線", "4 転線"],
                            1,
                            "点線（てんせん）＝ dotted line, perforated line (点: dot/point + 線: line)."
                        )
                    ]
                }
            ]
        },

        # =====================================================================
        # LESSON 15: 第15回 交通・旅行(1) (pp. 58-59)
        # =====================================================================
        {
            "lesson": 15,
            "title_ja": "第15回 交通・旅行 (1)",
            "title_en": "Lesson 15: Traffic & Travel (1)",
            "page_range": "58-59",
            "exercises": [
                {
                    "id": "k_ex_15_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。(北山鉄道のお知らせ)",
                    "title_en": "1. Choose the correct reading for the underlined kanji (Kitayama Railway Notice).",
                    "items": [
                        make_item(
                            "k_ex_15_1", 1, "路", "線路", "せんろ",
                            "ただいま、南山線は、<u>a. 線路</u> で起きた事故のため、動いておりません。",
                            "Currently, the Minamiyama Line is not operating due to an accident that occurred on the tracks.",
                            "ただいま、南山線は、線路で起きた事故のため、動いておりません。",
                            "ただいま、<ruby>南山線<rt>みなみやません</rt></ruby>は、<ruby>線路<rt>せんろ</rt></ruby>で<ruby>起<rt>お</rt></ruby>きた<ruby>事故<rt>じこ</rt></ruby>のため、<ruby>動<rt>うご</rt></ruby>いておりません。",
                            ["1 せんろ", "2 せんろう", "3 ぜんろ", "4 せんみち"],
                            1,
                            "線路（せんろ）＝ railway track, line (線: line + 路: road/track)."
                        ),
                        make_item(
                            "k_ex_15_1", 2, "故", "事故", "じこ",
                            "ただいま、南山線は、線路で起きた <u>b. 事故</u> のため、動いておりません。",
                            "Currently, the Minamiyama Line is not operating due to an accident that occurred on the tracks.",
                            "ただいま、南山線は、線路で起きた事故のため、動いておりません。",
                            "ただいま、<ruby>南山線<rt>みなみやません</rt></ruby>は、<ruby>線路<rt>せんろ</rt></ruby>で<ruby>起<rt>お</rt></ruby>きた<ruby>事故<rt>じこ</rt></ruby>のため、<ruby>動<rt>うご</rt></ruby>いておりません。",
                            ["1 じこ", "2 しこ", "3 じこう", "4 ことゆえ"],
                            1,
                            "事故（じこ）＝ accident, incident (事: matter + 故: reason/mishap)."
                        ),
                        make_item(
                            "k_ex_15_1", 3, "鉄", "地下鉄", "ちかてつ",
                            "<u>c. 地下鉄</u> を利用されるお客様には、中央の改札口で証明書を差し上げております。",
                            "For passengers using the subway, we are issuing delay certificates at the central ticket gate.",
                            "地下鉄を利用されるお客様には、中央の改札口で証明書を差し上げております。",
                            "<ruby>地下鉄<rt>ちかてつ</rt></ruby>を<ruby>利用<rt>りよう</rt></ruby>されるお<ruby>客様<rt>きゃくさま</rt></ruby>には、<ruby>中央<rt>ちゅうおう</rt></ruby>の<ruby>改札口<rt>かいさつぐち</rt></ruby>で<ruby>証明書<rt>しょうめいしょ</rt></ruby>を<ruby>差<rt>さ</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げております。",
                            ["1 ちかてつ", "2 じかてつ", "3 ちがてつ", "4 ちかてっ"],
                            1,
                            "地下鉄（ちかてつ）＝ subway, underground railway (地下: underground + 鉄: iron/rail)."
                        ),
                        make_item(
                            "k_ex_15_1", 4, "客", "お客様", "おきゃくさま",
                            "地下鉄を利用される <u>d. お客様</u> には、中央の改札口で証明書を差し上げております。",
                            "For passengers using the subway, we are issuing delay certificates at the central ticket gate.",
                            "地下鉄を利用されるお客様には、中央の改札口で証明書を差し上げております。",
                            "<ruby>地下鉄<rt>ちかてつ</rt></ruby>を<ruby>利用<rt>りよう</rt></ruby>されるお<ruby>客様<rt>きゃくさま</rt></ruby>には、<ruby>中央<rt>ちゅうおう</rt></ruby>の<ruby>改札口<rt>かいさつぐち</rt></ruby>で<ruby>証明書<rt>しょうめいしょ</rt></ruby>を<ruby>差<rt>さ</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げております。",
                            ["1 おきゃくさま", "2 おかくさま", "3 おきゃくざま", "4 おきやくさま"],
                            1,
                            "お客様（おきゃくさま）＝ customer, guest, passenger (polite)."
                        ),
                        make_item(
                            "k_ex_15_1", 5, "央", "中央", "ちゅうおう",
                            "地下鉄を利用されるお客様には、<u>e. 中央</u> の改札口で証明書を差し上げております。",
                            "For passengers using the subway, we are issuing delay certificates at the central ticket gate.",
                            "地下鉄を利用されるお客様には、中央の改札口で証明書を差し上げております。",
                            "<ruby>地下鉄<rt>ちかてつ</rt></ruby>を<ruby>利用<rt>りよう</rt></ruby>されるお<ruby>客様<rt>きゃくさま</rt></ruby>には、<ruby>中央<rt>ちゅうおう</rt></ruby>の<ruby>改札口<rt>かいさつぐち</rt></ruby>で<ruby>証明書<rt>しょうめいしょ</rt></ruby>を<ruby>差<rt>さ</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げております。",
                            ["1 ちゅうおう", "2 ちゅうお", "3 なかおう", "4 ちゅうよう"],
                            1,
                            "中央（ちゅうおう）＝ center, middle (中: middle + 央: center)."
                        ),
                        make_item(
                            "k_ex_15_1", 6, "明", "証明書", "しょうめいしょ",
                            "地下鉄を利用されるお客様には、中央の改札口で <u>f. 証明書</u> を差し上げております。",
                            "For passengers using the subway, we are issuing delay certificates at the central ticket gate.",
                            "地下鉄を利用されるお客様には、中央の改札口で証明書を差し上げております。",
                            "<ruby>地下鉄<rt>ちかてつ</rt></ruby>を<ruby>利用<rt>りよう</rt></ruby>されるお<ruby>客様<rt>きゃくさま</rt></ruby>には、<ruby>中央<rt>ちゅうおう</rt></ruby>の<ruby>改札口<rt>かいさつぐち</rt></ruby>で<ruby>証明書<rt>しょうめいしょ</rt></ruby>を<ruby>差<rt>さ</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げております。",
                            ["1 しょうめいしょ", "2 しょめいしょ", "3 しょうみょうしょ", "4 せいめいしょ"],
                            1,
                            "証明書（しょうめいしょ）＝ certificate (証明: proof/certification + 書: document)."
                        ),
                        make_item(
                            "k_ex_15_1", 7, "鉄", "鉄道", "てつどう",
                            "北山 <u>g. 鉄道</u>",
                            "Kitayama Railway",
                            "北山鉄道",
                            "<ruby>北山鉄道<rt>きたやまてつどう</rt></ruby>",
                            ["1 てつどう", "2 てっどう", "3 てつみち", "4 でつどう"],
                            1,
                            "鉄道（てつどう）＝ railway, railroad (鉄: iron + 道: road/way)."
                        )
                    ]
                },
                {
                    "id": "k_ex_15_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct reading.",
                    "items": [
                        make_item(
                            "k_ex_15_2", 1, "遠", "遠足", "えんそく",
                            "①子供の頃、<u>遠足</u>が楽しみだった。",
                            "When I was a child, I looked forward to school excursions.",
                            "子供の頃、遠足が楽しみだった。",
                            "<ruby>子供<rt>こども</rt></ruby>の<ruby>頃<rt>ころ</rt></ruby>、<ruby>遠足<rt>えんそく</rt></ruby>が<ruby>楽<rt>たの</rt></ruby>しみだった。",
                            ["1 とおあし", "2 えんそく", "3 えんあし", "4 おんそく"],
                            2,
                            "遠足（えんそく）＝ excursion, field trip, outing (遠: far + 足: foot/trip)."
                        ),
                        make_item(
                            "k_ex_15_2", 2, "航", "航空機", "こうくうき",
                            "②<u>航空機</u>の写真を壁に張った。",
                            "I put up a photo of an aircraft on the wall.",
                            "航空機の写真を壁に張った。",
                            "<ruby>航空機<rt>こうくうき</rt></ruby>の<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>壁<rt>かべ</rt></ruby>に<ruby>張<rt>は</rt></ruby>った。",
                            ["1 こくうき", "2 こうくうき", "3 こうくき", "4 こうき"],
                            2,
                            "航空機（こうくうき）＝ aircraft, airplane (航: navigate + 空: sky + 機: machine). Both こう and くう are long vowels."
                        ),
                        make_item(
                            "k_ex_15_2", 3, "観", "観光", "かんこう",
                            "③大型バスで市内を<u>観光</u>した。",
                            "We went sightseeing around the city on a large bus.",
                            "大型バスで市内を観光した。",
                            "<ruby>大型<rt>おおがた</rt></ruby>バスで<ruby>市内<rt>しない</rt></ruby>を<ruby>観光<rt>かんこう</rt></ruby>した。",
                            ["1 かんこう", "2 かんごう", "3 かんこ", "4 みひかり"],
                            1,
                            "観光（かんこう）＝ sightseeing, tourism (観: view/observe + 光: light/scenery)."
                        ),
                        make_item(
                            "k_ex_15_2", 4, "路", "道路", "どうろ",
                            "④<u>道路</u>を横断するときは、車に注意してください。",
                            "When crossing the road, please watch out for cars.",
                            "道路を横断するときは、車に注意してください。",
                            "<ruby>道路<rt>どうろ</rt></ruby>を<ruby>横断<rt>おうだん</rt></ruby>するときは、<ruby>車<rt>くるま</rt></ruby>に<ruby>注意<rt>ちゅうい</rt></ruby>してください。",
                            ["1 どうろ", "2 とうろ", "3 とうろう", "4 みちろ"],
                            1,
                            "道路（どうろ）＝ road, highway, street (道: road + 路: road)."
                        )
                    ]
                },
                {
                    "id": "k_ex_15_3",
                    "type": "sentence_fill",
                    "title_ja": "3. [ 億、個、倍、枚、秒 ] の中から漢字を選んで、文を完成しましょう。読み方も書きましょう。",
                    "title_en": "3. Choose a kanji counter from [ 億, 個, 倍, 枚, 秒 ] to complete the sentence and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_15_3", 1, "億", "31億", "さんじゅういちおく",
                            "①東京の地下鉄を利用する人は、1年間で約31<u>［　］</u>人だそうだ。",
                            "It is said that about 3.1 billion people use the Tokyo subway in a single year.",
                            "東京の地下鉄を利用する人は、1年間で約31億人だそうだ。",
                            "<ruby>東京<rt>とうきょう</rt></ruby>の<ruby>地下鉄<rt>ちかてつ</rt></ruby>を<ruby>利用<rt>りよう</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>は、1<ruby>年間<rt>ねんかん</rt></ruby>で<ruby>約<rt>やく</rt></ruby>31<ruby>億人<rt>おくにん</rt></ruby>だそうだ。",
                            ["1 億（おく）", "2 倍（ばい）", "3 枚（まい）", "4 個（こ）"],
                            1,
                            "億（おく）＝ hundred million (31億 = 3.1 billion)."
                        ),
                        make_item(
                            "k_ex_15_3", 2, "枚", "2枚", "にまい",
                            "②友達と京都に行くので、切符を2<u>［　］</u>買った。",
                            "Since I am going to Kyoto with a friend, I bought two tickets.",
                            "友達と京都に行くので、切符を2枚買った。",
                            "<ruby>友達<rt>ともだち</rt></ruby>と<ruby>京都<rt>きょうと</rt></ruby>に<ruby>行<rt>い</rt></ruby>くので、<ruby>切符<rt>きっぷ</rt></ruby>を2<ruby>枚買<rt>まいか</rt></ruby>った。",
                            ["1 枚（にまい）", "2 個（にこ）", "3 倍（にばい）", "4 秒（にびょう）"],
                            1,
                            "枚（まい）＝ counter for flat, thin objects such as tickets, paper, plates, or shirts."
                        ),
                        make_item(
                            "k_ex_15_3", 3, "個", "何個", "なんこ",
                            "③飛行機の中には、荷物を何<u>［　］</u>持って入れますか。",
                            "How many pieces of baggage can you bring onto the airplane?",
                            "飛行機の中には、荷物を何個持って入れますか。",
                            "<ruby>飛行機<rt>ひこうき</rt></ruby>の<ruby>中<rt>なか</rt></ruby>には、<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>何個持<rt>なんこも</rt></ruby>って<ruby>入<rt>はい</rt></ruby>れますか。",
                            ["1 個（なんこ）", "2 枚（なんまい）", "3 倍（なんばい）", "4 億（なんおく）"],
                            1,
                            "個（こ）＝ counter for small, three-dimensional objects or pieces of baggage (何個: なんこ)."
                        ),
                        make_item(
                            "k_ex_15_3", 4, "秒", "38秒", "さんじゅうはちびょう",
                            "④その年は、交通事故が38<u>［　］</u>に1回起きていた。",
                            "In that year, a traffic accident was occurring once every 38 seconds.",
                            "その年は、交通事故が38秒に1回起きていた。",
                            "その<ruby>年<rt>とし</rt></ruby>は、<ruby>交通事故<rt>こうつうじこ</rt></ruby>が38<ruby>秒<rt>びょう</rt></ruby>に1<ruby>回起<rt>かいお</rt></ruby>きていた。",
                            ["1 秒（びょう）", "2 倍（ばい）", "3 個（こ）", "4 枚（まい）"],
                            1,
                            "秒（びょう）＝ second (unit of time)."
                        ),
                        make_item(
                            "k_ex_15_3", 5, "倍", "4倍", "よんばい",
                            "⑤タクシーは速いですが、お金が電車の4<u>［　］</u>も高くかかりますよ。",
                            "A taxi is fast, but it costs four times as much money as the train.",
                            "タクシーは速いですが、お金が電車の4倍も高くかかりますよ。",
                            "タクシーは<ruby>速<rt>はや</rt></ruby>いですが、お<ruby>金<rt>かね</rt></ruby>が<ruby>電車<rt>でんしゃ</rt></ruby>の4<ruby>倍<rt>ばい</rt></ruby>も<ruby>高<rt>たか</rt></ruby>くかかりますよ。",
                            ["1 倍（よんばい）", "2 億（よんおく）", "3 枚（よんまい）", "4 秒（よんびょう）"],
                            1,
                            "倍（ばい）＝ times, -fold (4倍: よんばい = four times)."
                        )
                    ]
                },
                {
                    "id": "k_ex_15_4",
                    "type": "word_pairing",
                    "title_ja": "4. □には同じ漢字が入ります。[ 送、末、明 ] から漢字を選んで書きましょう。下線の部分の読み方も書きましょう。",
                    "title_en": "4. Fill in each pair of blanks with the same kanji from [ 送, 末, 明 ] and identify the reading.",
                    "items": [
                        make_item(
                            "k_ex_15_4", 1, "放", "放送", "ほうそう",
                            "①a 電車の事故のニュースをテレビで <u>放［　］</u>していた。",
                            "They were broadcasting news of the train accident on TV.",
                            "電車の事故のニュースをテレビで放送していた。",
                            "<ruby>電車<rt>でんしゃ</rt></ruby>の<ruby>事故<rt>じこ</rt></ruby>のニュースをテレビで<ruby>放送<rt>ほうそう</rt></ruby>していた。",
                            ["1 送（ほうそう）", "2 明（ほうめい）", "3 末（ほうまつ）", "4 鉄（ほうてつ）"],
                            1,
                            "放送（ほうそう）＝ broadcast, broadcasting (放: release/emit + 送: send)."
                        ),
                        make_item(
                            "k_ex_15_4", 2, "送", "送料", "そうりょう",
                            "①b 5000円以上の商品の配達は、<u>［　］料</u>がかかりません。",
                            "For delivery of products over 5,000 yen, there is no shipping charge.",
                            "5000円以上の商品の配達は、送料がかかりません。",
                            "5000<ruby>円以上<rt>えんいじょう</rt></ruby>の<ruby>商品<rt>しょうひん</rt></ruby>の<ruby>配達<rt>はいたつ</rt></ruby>は、<ruby>送料<rt>そうりょう</rt></ruby>がかかりません。",
                            ["1 送（そうりょう）", "2 明（めいりょう）", "3 末（まつりょう）", "4 客（きゃくりょう）"],
                            1,
                            "送料（そうりょう）＝ shipping fee, postage, carriage (送: send + 料: fee)."
                        ),
                        make_item(
                            "k_ex_15_4", 3, "明", "発明", "はつめい",
                            "②a 電話はベルによって <u>発［　］</u>された。",
                            "The telephone was invented by Bell.",
                            "電話はベルによって発明された。",
                            "<ruby>電話<rt>でんわ</rt></ruby>はベルによって<ruby>発明<rt>はつめい</rt></ruby>された。",
                            ["1 明（はつめい）", "2 送（はっそう）", "3 末（はつまつ）", "4 鉄（はつてつ）"],
                            1,
                            "発明（はつめい）＝ invention (発: originate/produce + 明: make clear)."
                        ),
                        make_item(
                            "k_ex_15_4", 4, "明", "説明", "せつめい",
                            "②b 雪のため新幹線が遅れているという <u>説［　］</u>があった。",
                            "There was an explanation/announcement that the Shinkansen was delayed due to snow.",
                            "雪のため新幹線が遅れているという説明があった。",
                            "<ruby>雪<rt>ゆき</rt></ruby>のため<ruby>新幹線<rt>しんかんせん</rt></ruby>が<ruby>遅<rt>おく</rt></ruby>れているという<ruby>説明<rt>せつめい</rt></ruby>があった。",
                            ["1 明（せつめい）", "2 送（せっそう）", "3 末（せつまつ）", "4 客（せっきゃく）"],
                            1,
                            "説明（せつめい）＝ explanation (説: explain + 明: clear)."
                        ),
                        make_item(
                            "k_ex_15_4", 5, "末", "週末", "しゅうまつ",
                            "③a <u>週［　］</u>は山に行って、月曜に帰って来るつもりだ。",
                            "I plan to go to the mountains for the weekend and come back on Monday.",
                            "週末は山に行って、月曜に帰って来るつもりだ。",
                            "<ruby>週末<rt>しゅうまつ</rt></ruby>は<ruby>山<rt>やま</rt></ruby>に<ruby>行<rt>い</rt></ruby>って、<ruby>月曜<rt>げつよう</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>って<ruby>来<rt>く</rt></ruby>るつもりだ。",
                            ["1 末（しゅうまつ）", "2 送（しゅうそう）", "3 明（しゅうめい）", "4 秒（しゅうびょう）"],
                            1,
                            "週末（しゅうまつ）＝ weekend (週: week + 末: end)."
                        ),
                        make_item(
                            "k_ex_15_4", 6, "末", "月末", "げつまつ",
                            "③b 新しい駅が <u>月［　］</u>に完成する予定だ。",
                            "The new station is scheduled to be completed at the end of the month.",
                            "新しい駅が月末に完成する予定だ。",
                            "<ruby>新<rt>あたら</rt></ruby>しい<ruby>駅<rt>えき</rt></ruby>が<ruby>月末<rt>げつまつ</rt></ruby>に<ruby>完成<rt>かんせい</rt></ruby>する<ruby>予定<rt>よてい</rt></ruby>だ。",
                            ["1 末（げつまつ）", "2 送（げっそう）", "3 明（げつめい）", "4 倍（げつばい）"],
                            1,
                            "月末（げつまつ）＝ end of the month (月: month + 末: end)."
                        )
                    ]
                },
                {
                    "id": "k_ex_15_5",
                    "type": "reading_writing",
                    "title_ja": "5. 下線の部分の漢字には読み方を、平仮名には漢字を書きましょう。(日本の交通と輸送)",
                    "title_en": "5. Give the reading for underlined kanji and kanji for underlined hiragana (Transportation in Japan).",
                    "items": [
                        make_item(
                            "k_ex_15_5", 1, "鉄", "鉄道", "てつどう",
                            "1960年頃まで、日本では、人や物を運ぶのは、主に <u>a. てつどう</u> だった。",
                            "Until around 1960 in Japan, transporting people and goods was mainly by railway.",
                            "1960年頃まで、日本では、人や物を運ぶのは、主に鉄道だった。",
                            "1960<ruby>年頃<rt>ねんごろ</rt></ruby>まで、<ruby>日本<rt>にほん</rt></ruby>では、<ruby>人<rt>ひと</rt></ruby>や<ruby>物<rt>もの</rt></ruby>を<ruby>運<rt>はこ</rt></ruby>ぶのは、<ruby>主<rt>おも</rt></ruby>に<ruby>鉄道<rt>てつどう</rt></ruby>だった。",
                            ["1 鉄道", "2 鉄路", "3 秩道", "4 失道"],
                            1,
                            "鉄道（てつどう）＝ railway, railroad."
                        ),
                        make_item(
                            "k_ex_15_5", 2, "観", "観光", "かんこう",
                            "1970年頃からは、<u>b. かんこう</u> の目的で旅行する人や、個人や女性の旅行客が増えたが…",
                            "From around 1970, people traveling for sightseeing and individual or female travelers increased...",
                            "1970年頃からは、観光の目的で旅行する人や、個人や女性の旅行客が増えたが…",
                            "1970<ruby>年頃<rt>ねんごろ</rt></ruby>からは、<ruby>観光<rt>かんこう</rt></ruby>の<ruby>目的<rt>もくてき</rt></ruby>で<ruby>旅行<rt>りょこう</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>や、<ruby>個人<rt>こじん</rt></ruby>や<ruby>女性<rt>じょせい</rt></ruby>の<ruby>旅行客<rt>りょこうきゃく</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えたが…",
                            ["1 観光", "2 勧光", "3 歓光", "4 感光"],
                            1,
                            "観光（かんこう）＝ sightseeing, tourism."
                        ),
                        make_item(
                            "k_ex_15_5", 3, "個", "個人", "こじん",
                            "1970年頃からは、かんこうの目的で旅行する人や、<u>c. 個人</u> や女性の旅行客が増えたが…",
                            "From around 1970, people traveling for sightseeing and individual or female travelers increased...",
                            "1970年頃からは、観光の目的で旅行する人や、個人や女性の旅行客が増えたが…",
                            "1970<ruby>年頃<rt>ねんごろ</rt></ruby>からは、<ruby>観光<rt>かんこう</rt></ruby>の<ruby>目的<rt>もくてき</rt></ruby>で<ruby>旅行<rt>りょこう</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>や、<ruby>個人<rt>こじん</rt></ruby>や<ruby>女性<rt>じょせい</rt></ruby>の<ruby>旅行客<rt>りょこうきゃく</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えたが…",
                            ["1 こじん", "2 こにん", "3 かじん", "4 こうじん"],
                            1,
                            "個人（こじん）＝ individual, personal, private person."
                        ),
                        make_item(
                            "k_ex_15_5", 4, "客", "旅行客", "りょこうきゃく",
                            "1970年頃からは、かんこうの目的で旅行する人や、個人や女性の <u>d. 旅行客</u> が増えたが…",
                            "From around 1970, people traveling for sightseeing and individual or female travelers increased...",
                            "1970年頃からは、観光の目的で旅行する人や、個人や女性の旅行客が増えたが…",
                            "1970<ruby>年頃<rt>ねんごろ</rt></ruby>からは、<ruby>観光<rt>かんこう</rt></ruby>の<ruby>目的<rt>もくてき</rt></ruby>で<ruby>旅行<rt>りょこう</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>や、<ruby>個人<rt>こじん</rt></ruby>や<ruby>女性<rt>じょせい</rt></ruby>の<ruby>旅行客<rt>りょこうきゃく</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えたが…",
                            ["1 りょこうきゃく", "2 りょこうかく", "3 りょうこうきゃく", "4 りょこきゃく"],
                            1,
                            "旅行客（りょこうきゃく）＝ traveler, tourist (旅行: travel + 客: guest/passenger)."
                        ),
                        make_item(
                            "k_ex_15_5", 5, "速", "高速道路", "こうそくどうろ",
                            "しかし、だんだんと物を運ぶのにトラックが利用されるようになって、<u>e. こうそくどうろ</u> が全国に作られた。",
                            "However, trucks gradually came to be used for transporting goods, and expressways were built nationwide.",
                            "しかし、だんだんと物を運ぶのにトラックが利用されるようになって、高速道路が全国に作られた。",
                            "しかし、だんだんと<ruby>物<rt>もの</rt></ruby>を<ruby>運<rt>はこ</rt></ruby>ぶのにトラックが<ruby>利用<rt>りよう</rt></ruby>されるようになって、<ruby>高速道路<rt>こうそくどうろ</rt></ruby>が<ruby>全国<rt>ぜんこく</rt></ruby>に<ruby>作<rt>つく</rt></ruby>られた。",
                            ["1 高速道路", "2 高束道路", "3 広速道路", "4 高足道路"],
                            1,
                            "高速道路（こうそくどうろ）＝ expressway, highway, freeway (高速: high speed + 道路: road)."
                        ),
                        make_item(
                            "k_ex_15_5", 6, "航", "航空機", "こうくうき",
                            "現在は、<u>f. こうくうき</u> も使われるようになって、スーパーなどには、外国からの野菜や果物がたくさん並んでいる。",
                            "Nowadays, aircraft have also come to be used, and supermarkets are lined with many vegetables and fruits from foreign countries.",
                            "現在は、航空機も使われるようになって、スーパーなどには、外国からの野菜や果物がたくさん並んでいる。",
                            "<ruby>現在<rt>げんざい</rt></ruby>は、<ruby>航空機<rt>こうくうき</rt></ruby>も<ruby>使<rt>つか</rt></ruby>われるようになって、スーパーなどには、<ruby>外国<rt>がいこく</rt></ruby>からの<ruby>野菜<rt>やさい</rt></ruby>や<ruby>果物<rt>くだもの</rt></ruby>がたくさん<ruby>並<rt>なら</rt></ruby>んでいる。",
                            ["1 航空機", "2 航空気", "3 行空機", "4 港空機"],
                            1,
                            "航空機（こうくうき）＝ aircraft, airplane."
                        )
                    ]
                }
            ]
        }
    ]

    output = {
        "metadata": {
            "book": "Shin Kanzen Master Kanji N3",
            "part": 3,
            "lessons": "11-15 + Summary Test 3 (まとめ問題4)",
            "pages": "46-59",
            "description": "Exhaustive verbatim exercise bank for Lessons 11 to 15 and Summary Review 3"
        },
        "lessons": lessons
    }

    out_path = os.path.join(BASE_DIR, "exercises_part3.json")
    os.makedirs(BASE_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    total_ex = sum(len(l["exercises"]) for l in lessons)
    total_items = sum(len(e["items"]) for l in lessons for e in l["exercises"])
    print(f"Wrote {out_path}: {len(lessons)} lesson blocks, {total_ex} exercises, {total_items} items.")


if __name__ == "__main__":
    build_part3_exercises()
