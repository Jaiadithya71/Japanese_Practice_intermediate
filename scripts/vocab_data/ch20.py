# -*- coding: utf-8 -*-
"""
Chapter 20: 数と量 (Numbers and Quantities)
Pages: 86-89
"""

ch20_data = {
    "metadata": {
        "chapter": 20,
        "part": 1,
        "topic_ja": "数と量",
        "topic_en": "Numbers and Quantities",
        "pages": [86, 87, 88, 89]
    },
    "sections": [
        {
            "section_id": 1,
            "title_ja": "数と量(1)",
            "title_en": "Numbers and Quantities 1",
            "warming_up": {
                "question_ja": "どんなものを測ったり、数えたりしますか。"
            },
            "words": [
                {
                    "term_ja": "数",
                    "reading": "かず",
                    "ruby_html": "<ruby>数<rt>かず</rt></ruby>",
                    "meaning_en": "number, count",
                    "example_ja": "人数を数える",
                    "example_ruby": "<ruby>人数<rt>にんずう</rt></ruby>を<ruby>数<rt>かぞ</rt></ruby>える"
                },
                {
                    "term_ja": "量",
                    "reading": "りょう",
                    "ruby_html": "<ruby>量<rt>りょう</rt></ruby>",
                    "meaning_en": "quantity, volume, amount",
                    "example_ja": "食事の量を減らす",
                    "example_ruby": "<ruby>食事<rt>しょくじ</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>を<ruby>減<rt>へ</rt></ruby>らす"
                },
                {
                    "term_ja": "増やす",
                    "reading": "ふやす",
                    "ruby_html": "<ruby>増<rt>ふ</rt></ruby>やす",
                    "meaning_en": "to increase, multiply (transitive)",
                    "example_ja": "貯金を増やす",
                    "example_ruby": "<ruby>貯金<rt>ちょきん</rt></ruby>を<ruby>増<rt>ふ</rt></ruby>やす"
                },
                {
                    "term_ja": "増す",
                    "reading": "ます",
                    "ruby_html": "<ruby>増<rt>ま</rt></ruby>す",
                    "meaning_en": "to increase, heighten, grow",
                    "example_ja": "興味が増す",
                    "example_ruby": "<ruby>興味<rt>きょうみ</rt></ruby>が<ruby>増<rt>ま</rt></ruby>す"
                },
                {
                    "term_ja": "減らす",
                    "reading": "へらす",
                    "ruby_html": "<ruby>減<rt>へ</rt></ruby>らす",
                    "meaning_en": "to reduce, decrease, curtail (transitive)",
                    "example_ja": "体重を減らす",
                    "example_ruby": "<ruby>体重<rt>たいじゅう</rt></ruby>を<ruby>減<rt>へ</rt></ruby>らす"
                },
                {
                    "term_ja": "増える",
                    "reading": "ふえる",
                    "ruby_html": "<ruby>増<rt>ふ</rt></ruby>える",
                    "meaning_en": "to increase, multiply (intransitive)",
                    "example_ja": "体重が増える",
                    "example_ruby": "<ruby>体重<rt>たいじゅう</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>える"
                },
                {
                    "term_ja": "減る",
                    "reading": "へる",
                    "ruby_html": "<ruby>減<rt>へ</rt></ruby>る",
                    "meaning_en": "to decrease, diminish (intransitive)",
                    "example_ja": "人口が減る",
                    "example_ruby": "<ruby>人口<rt>じんこう</rt></ruby>が<ruby>減<rt>へ</rt></ruby>る"
                },
                {
                    "term_ja": "倍",
                    "reading": "ばい",
                    "ruby_html": "<ruby>倍<rt>ばい</rt></ruby>",
                    "meaning_en": "times, -fold, double",
                    "example_ja": "2倍に増える",
                    "example_ruby": "2<ruby>倍<rt>ばい</rt></ruby>に<ruby>増<rt>ふ</rt></ruby>える"
                },
                {
                    "term_ja": "余る",
                    "reading": "あまる",
                    "ruby_html": "<ruby>余<rt>あま</rt></ruby>る",
                    "meaning_en": "to be left over, remain",
                    "example_ja": "料理が余る",
                    "example_ruby": "<ruby>料理<rt>りょうり</rt></ruby>が<ruby>余<rt>あま</rt></ruby>る"
                },
                {
                    "term_ja": "不足する",
                    "reading": "ふそくする",
                    "ruby_html": "<ruby>不足<rt>ふそく</rt></ruby>する",
                    "meaning_en": "to be insufficient, lack",
                    "example_ja": "運動が不足する",
                    "example_ruby": "<ruby>運動<rt>うんどう</rt></ruby>が<ruby>不足<rt>ふそく</rt></ruby>する"
                },
                {
                    "term_ja": "余裕",
                    "reading": "よゆう",
                    "ruby_html": "<ruby>余裕<rt>よゆう</rt></ruby>",
                    "meaning_en": "leeway, margin, room (time, money)",
                    "example_ja": "時間に余裕がある",
                    "example_ruby": "<ruby>時間<rt>じかん</rt></ruby>に<ruby>余裕<rt>よゆう</rt></ruby>がある"
                },
                {
                    "term_ja": "人数",
                    "reading": "にんずう",
                    "ruby_html": "<ruby>人数<rt>にんずう</rt></ruby>",
                    "meaning_en": "number of people",
                    "example_ja": "参加者の人数",
                    "example_ruby": "<ruby>参加者<rt>さんかしゃ</rt></ruby>の<ruby>人数<rt>にんずう</rt></ruby>"
                },
                {
                    "term_ja": "個数",
                    "reading": "こすう",
                    "ruby_html": "<ruby>個数<rt>こすう</rt></ruby>",
                    "meaning_en": "number of items, count of articles",
                    "example_ja": "リンゴの個数",
                    "example_ruby": "リンゴの<ruby>個数<rt>こすう</rt></ruby>"
                },
                {
                    "term_ja": "回数",
                    "reading": "かいすう",
                    "ruby_html": "<ruby>回数<rt>かいすう</rt></ruby>",
                    "meaning_en": "number of times, frequency",
                    "example_ja": "練習の回数を増やす",
                    "example_ruby": "<ruby>練習<rt>れんしゅう</rt></ruby>の<ruby>回数<rt>かいすう</rt></ruby>を<ruby>増<rt>ふ</rt></ruby>やす"
                },
                {
                    "term_ja": "台数",
                    "reading": "だいすう",
                    "ruby_html": "<ruby>台数<rt>だいすう</rt></ruby>",
                    "meaning_en": "number of vehicles, machines",
                    "example_ja": "車の台数",
                    "example_ruby": "<ruby>車<rt>くるま</rt></ruby>の<ruby>台数<rt>だいすう</rt></ruby>"
                },
                {
                    "term_ja": "数える",
                    "reading": "かぞえる",
                    "ruby_html": "<ruby>数<rt>かぞ</rt></ruby>える",
                    "meaning_en": "to count",
                    "example_ja": "お金を数える",
                    "example_ruby": "お<ruby>金<rt>かね</rt></ruby>を<ruby>数<rt>かぞ</rt></ruby>える"
                },
                {
                    "term_ja": "測る",
                    "reading": "はかる",
                    "ruby_html": "<ruby>測<rt>はか</rt></ruby>る",
                    "meaning_en": "to measure (length, distance, time)",
                    "example_ja": "長さを測る",
                    "example_ruby": "<ruby>長<rt>なが</rt></ruby>さを<ruby>測<rt>はか</rt></ruby>る"
                },
                {
                    "term_ja": "距離",
                    "reading": "きょり",
                    "ruby_html": "<ruby>距離<rt>きょり</rt></ruby>",
                    "meaning_en": "distance, interval",
                    "example_ja": "駅までの距離",
                    "example_ruby": "<ruby>駅<rt>えき</rt></ruby>までの<ruby>距離<rt>きょり</rt></ruby>"
                },
                {
                    "term_ja": "面積",
                    "reading": "めんせき",
                    "ruby_html": "<ruby>面積<rt>めんせき</rt></ruby>",
                    "meaning_en": "area, surface area",
                    "example_ja": "部屋の面積",
                    "example_ruby": "<ruby>部屋<rt>へや</rt></ruby>の<ruby>面積<rt>めんせき</rt></ruby>"
                },
                {
                    "term_ja": "時間",
                    "reading": "じかん",
                    "ruby_html": "<ruby>時間<rt>じかん</rt></ruby>",
                    "meaning_en": "time, hours, duration",
                    "example_ja": "かかる時間を測る",
                    "example_ruby": "かかる<ruby>時間<rt>じかん</rt></ruby>を<ruby>測<rt>はか</rt></ruby>る"
                },
                {
                    "term_ja": "重さ",
                    "reading": "おもさ",
                    "ruby_html": "<ruby>重<rt>おも</rt></ruby>さ",
                    "meaning_en": "weight, heaviness",
                    "example_ja": "荷物の重さ",
                    "example_ruby": "<ruby>荷物<rt>にもつ</rt></ruby>の<ruby>重<rt>おも</rt></ruby>さ"
                },
                {
                    "term_ja": "量る",
                    "reading": "はかる",
                    "ruby_html": "<ruby>量<rt>はか</rt></ruby>る",
                    "meaning_en": "to weigh, measure quantity/volume",
                    "example_ja": "体重を量る",
                    "example_ruby": "<ruby>体重<rt>たいじゅう</rt></ruby>を<ruby>量<rt>はか</rt></ruby>る"
                },
                {
                    "term_ja": "記録",
                    "reading": "きろく",
                    "ruby_html": "<ruby>記録<rt>きろく</rt></ruby>",
                    "meaning_en": "record, minutes, documentation",
                    "example_ja": "新記録を出す",
                    "example_ruby": "<ruby>新記録<rt>しんきろく</rt></ruby>を<ruby>出<rt>だ</rt></ruby>す"
                },
                {
                    "term_ja": "取る",
                    "reading": "とる",
                    "ruby_html": "<ruby>取<rt>と</rt></ruby>る",
                    "meaning_en": "to take (notes/record)",
                    "example_ja": "記録を取る",
                    "example_ruby": "<ruby>記録<rt>きろく</rt></ruby>を<ruby>取<rt>と</rt></ruby>る"
                }
            ],
            "yattemiyou": [
                {
                    "id": 1,
                    "question_ja": "時間に（　余裕　）を持って出かけよう。",
                    "answer": "余裕",
                    "explanation": "時間的にゆとりがあることは「余裕」です。"
                },
                {
                    "id": 2,
                    "question_ja": "ダイエットのために、甘いものを（　減らす　）。",
                    "answer": "減らす",
                    "explanation": "量を少なくする行為は「減らす」です。"
                },
                {
                    "id": 3,
                    "question_ja": "最近、運動不足で体力が（　減る　）。",
                    "answer": "減る",
                    "explanation": "体力などが落ちて少なくなることは「減る」です。"
                },
                {
                    "id": 4,
                    "question_ja": "買いすぎて、パンが（　余る　）。",
                    "answer": "余る",
                    "explanation": "使いきれずに残ることは「余る」です。"
                },
                {
                    "id": 5,
                    "question_ja": "売り上げが去年の2（　倍　）になった。",
                    "answer": "倍",
                    "explanation": "掛け算の比率は「倍」です。"
                },
                {
                    "id": 6,
                    "question_ja": "体重計で体重を（　量る　）。",
                    "answer": "量る",
                    "explanation": "重さを測定することは「量る」です。"
                }
            ]
        },
        {
            "section_id": 2,
            "title_ja": "数と量(2)",
            "title_en": "Numbers and Quantities 2",
            "warming_up": {
                "question_ja": "どんな料理を作るのが得意ですか。材料の量はどうやって決めますか。"
            },
            "words": [
                {
                    "term_ja": "大量",
                    "reading": "たいりょう",
                    "ruby_html": "<ruby>大量<rt>たいりょう</rt></ruby>",
                    "meaning_en": "large quantity, mass volume",
                    "example_ja": "大量に購入する",
                    "example_ruby": "<ruby>大量<rt>たいりょう</rt></ruby>に<ruby>購入<rt>こうにゅう</rt></ruby>する"
                },
                {
                    "term_ja": "少量",
                    "reading": "しょうりょう",
                    "ruby_html": "<ruby>少量<rt>しょうりょう</rt></ruby>",
                    "meaning_en": "small amount, small quantity",
                    "example_ja": "少量の水",
                    "example_ruby": "<ruby>少量<rt>しょうりょう</rt></ruby>の<ruby>水<rt>みず</rt></ruby>"
                },
                {
                    "term_ja": "多数",
                    "reading": "たすう",
                    "ruby_html": "<ruby>多数<rt>たすう</rt></ruby>",
                    "meaning_en": "large number, majority",
                    "example_ja": "多数の参加者",
                    "example_ruby": "<ruby>多数<rt>たすう</rt></ruby>の<ruby>参加者<rt>さんかしゃ</rt></ruby>"
                },
                {
                    "term_ja": "少数",
                    "reading": "しょうすう",
                    "ruby_html": "<ruby>少数<rt>しょうすう</rt></ruby>",
                    "meaning_en": "small number, minority",
                    "example_ja": "少数の意見",
                    "example_ruby": "<ruby>少数<rt>しょうすう</rt></ruby>の<ruby>意見<rt>いけん</rt></ruby>"
                },
                {
                    "term_ja": "マイナス",
                    "reading": "マイナス",
                    "ruby_html": "マイナス",
                    "meaning_en": "minus, negative, below zero",
                    "example_ja": "気温がマイナスになる",
                    "example_ruby": "<ruby>気温<rt>きおん</rt></ruby>がマイナスになる"
                },
                {
                    "term_ja": "プラス",
                    "reading": "プラス",
                    "ruby_html": "プラス",
                    "meaning_en": "plus, positive, addition",
                    "example_ja": "プラスに働く",
                    "example_ruby": "プラスに<ruby>働<rt>はたら</rt></ruby>く"
                },
                {
                    "term_ja": "レベル",
                    "reading": "レベル",
                    "ruby_html": "レベル",
                    "meaning_en": "level, standard",
                    "example_ja": "技術のレベル",
                    "example_ruby": "<ruby>技術<rt>ぎじゅつ</rt></ruby>のレベル"
                },
                {
                    "term_ja": "上がる",
                    "reading": "あがる",
                    "ruby_html": "<ruby>上<rt>あ</rt></ruby>がる",
                    "meaning_en": "to rise, go up (level/price/fever)",
                    "example_ja": "レベルが上がる",
                    "example_ruby": "レベルが<ruby>上<rt>あ</rt></ruby>がる"
                },
                {
                    "term_ja": "最大",
                    "reading": "さいだい",
                    "ruby_html": "<ruby>最大<rt>さいだい</rt></ruby>",
                    "meaning_en": "greatest, maximum, largest",
                    "example_ja": "最大の効果",
                    "example_ruby": "<ruby>最大<rt>さいだい</rt></ruby>の<ruby>効果<rt>こうか</rt></ruby>"
                },
                {
                    "term_ja": "最小",
                    "reading": "さいしょう",
                    "ruby_html": "<ruby>最小<rt>さいしょう</rt></ruby>",
                    "meaning_en": "smallest, minimum",
                    "example_ja": "被害を最小にする",
                    "example_ruby": "<ruby>被害<rt>ひがい</rt></ruby>を<ruby>最小<rt>さいしょう</rt></ruby>にする"
                },
                {
                    "term_ja": "最高",
                    "reading": "さいこう",
                    "ruby_html": "<ruby>最高<rt>さいこう</rt></ruby>",
                    "meaning_en": "highest, supreme, maximum",
                    "example_ja": "最高気温",
                    "example_ruby": "<ruby>最高気温<rt>さいこうきおん</rt></ruby>"
                },
                {
                    "term_ja": "最低",
                    "reading": "さいてい",
                    "ruby_html": "<ruby>最低<rt>さいてい</rt></ruby>",
                    "meaning_en": "lowest, minimum, worst",
                    "example_ja": "最低限の条件",
                    "example_ruby": "<ruby>最低限<rt>さいていげん</rt></ruby>の<ruby>条件<rt>じょうけん</rt></ruby>"
                },
                {
                    "term_ja": "平均",
                    "reading": "へいきん",
                    "ruby_html": "<ruby>平均<rt>へいきん</rt></ruby>",
                    "meaning_en": "average, mean",
                    "example_ja": "平均点を計算する",
                    "example_ruby": "<ruby>平均点<rt>へいきんてん</rt></ruby>を<ruby>計算<rt>けいさん</rt></ruby>する"
                },
                {
                    "term_ja": "たっぷり",
                    "reading": "たっぷり",
                    "ruby_html": "たっぷり",
                    "meaning_en": "plenty, full, ample",
                    "example_ja": "野菜をたっぷり入れる",
                    "example_ruby": "<ruby>野菜<rt>やさい</rt></ruby>をたっぷり<ruby>入<rt>い</rt></ruby>れる"
                },
                {
                    "term_ja": "少々",
                    "reading": "しょうしょう",
                    "ruby_html": "<ruby>少々<rt>しょうしょう</rt></ruby>",
                    "meaning_en": "just a little, a small pinch",
                    "example_ja": "塩を少々加える",
                    "example_ruby": "<ruby>塩<rt>しお</rt></ruby>を<ruby>少々<rt>しょうしょう</rt></ruby><ruby>加<rt>くわ</rt></ruby>える"
                },
                {
                    "term_ja": "加える",
                    "reading": "くわえる",
                    "ruby_html": "<ruby>加<rt>くわ</rt></ruby>える",
                    "meaning_en": "to add, append, include",
                    "example_ja": "具材を加える",
                    "example_ruby": "<ruby>具材<rt>ぐざい</rt></ruby>を<ruby>加<rt>くわ</rt></ruby>える"
                },
                {
                    "term_ja": "すべて",
                    "reading": "すべて",
                    "ruby_html": "すべて",
                    "meaning_en": "all, entirely, everything",
                    "example_ja": "すべての問題",
                    "example_ruby": "すべての<ruby>問題<rt>もんだい</rt></ruby>"
                },
                {
                    "term_ja": "全員",
                    "reading": "ぜんいん",
                    "ruby_html": "<ruby>全員<rt>ぜんいん</rt></ruby>",
                    "meaning_en": "all members, everyone",
                    "example_ja": "全員が出席する",
                    "example_ruby": "<ruby>全員<rt>ぜんいん</rt></ruby>が<ruby>出席<rt>しゅっせき</rt></ruby>する"
                },
                {
                    "term_ja": "合計",
                    "reading": "ごうけい",
                    "ruby_html": "<ruby>合計<rt>ごうけい</rt></ruby>",
                    "meaning_en": "total amount, sum total",
                    "example_ja": "合計を計算する",
                    "example_ruby": "<ruby>合計<rt>ごうけい</rt></ruby>を<ruby>計算<rt>けいさん</rt></ruby>する"
                },
                {
                    "term_ja": "出す",
                    "reading": "だす",
                    "ruby_html": "<ruby>出<rt>だ</rt></ruby>す",
                    "meaning_en": "to produce, calculate, output",
                    "example_ja": "合計を出す",
                    "example_ruby": "<ruby>合計<rt>ごうけい</rt></ruby>を<ruby>出<rt>だ</rt></ruby>す"
                },
                {
                    "term_ja": "計算",
                    "reading": "けいさん",
                    "ruby_html": "<ruby>計算<rt>けいさん</rt></ruby>",
                    "meaning_en": "calculation, reckoning",
                    "example_ja": "計算が速い",
                    "example_ruby": "<ruby>計算<rt>けいさん</rt></ruby>が<ruby>速<rt>はや</rt></ruby>い"
                },
                {
                    "term_ja": "間違える",
                    "reading": "まちがえる",
                    "ruby_html": "<ruby>間違<rt>まちが</rt></ruby>える",
                    "meaning_en": "to mistake, make an error in",
                    "example_ja": "道を間違える",
                    "example_ruby": "<ruby>道<rt>みち</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>える"
                }
            ],
            "yattemiyou": [
                {
                    "id": 1,
                    "question_ja": "試験で（　最低　）でも60点は取りたい。",
                    "answer": "最低",
                    "explanation": "最小限の下限を表す言葉は「最低（でも）」です。"
                },
                {
                    "id": 2,
                    "question_ja": "服の（　サイズ　）が合わない。",
                    "answer": "サイズ",
                    "explanation": "衣服や靴の大きさ・寸法は「サイズ」です。"
                },
                {
                    "id": 3,
                    "question_ja": "この会場には、（　最大　）で500人入ることができる。",
                    "answer": "最大",
                    "explanation": "上限・最も多い数値を表すのは「最大」です。"
                },
                {
                    "id": 4,
                    "question_ja": "買い物をした（　合計　）は3,000円だった。",
                    "answer": "合計",
                    "explanation": "合わせた総額は「合計」です。"
                },
                {
                    "id": 5,
                    "question_ja": "スープに塩を少し（　加えて　）味を調える。",
                    "answer": "加えて",
                    "explanation": "調味料などを足し入れることは「加える」です。"
                },
                {
                    "id": 6,
                    "question_ja": "電卓を使って、数字を（　計算　）する。",
                    "answer": "計算",
                    "explanation": "数値を算出することは「計算する」です。"
                }
            ]
        }
    ],
    "exercises": [
        {
            "exercise_id": 1,
            "title_ja": "正しいほうを選びなさい。",
            "items": [
                {
                    "id": 1,
                    "question_ja": "箱の中のリンゴを（a 測った / b 数えた）。",
                    "options": ["a 測った", "b 数えた"],
                    "answer": "b",
                    "explanation": "個数を数える行為は「数えた」です。"
                },
                {
                    "id": 2,
                    "question_ja": "注文する商品の（a 人数 / b 個数）を確認した。",
                    "options": ["a 人数", "b 個数"],
                    "answer": "b",
                    "explanation": "商品や物品の数は「個数」です。"
                },
                {
                    "id": 3,
                    "question_ja": "薬は（a 少量 / b 少数）でも効果がある。",
                    "options": ["a 少量", "b 少数"],
                    "answer": "a",
                    "explanation": "分量が少ないことは「少量」です。"
                },
                {
                    "id": 4,
                    "question_ja": "被害を（a 最小 / b 最低）にとどめる。",
                    "options": ["a 最小", "b 最低"],
                    "answer": "a",
                    "explanation": "被害や損失を最も小さく抑えることは「最小にとどめる」と言います。"
                },
                {
                    "id": 5,
                    "question_ja": "勉強してテストの点数が（a 増えた / b 上がった）。",
                    "options": ["a 増えた", "b 上がった"],
                    "answer": "b",
                    "explanation": "点数やレベルが高くなることは「上がる」です。"
                }
            ]
        },
        {
            "exercise_id": 2,
            "title_ja": "世界の米の生産量グラフを見て、文の内容が正しければ○、違っていれば×を書きなさい。",
            "items": [
                {
                    "id": 1,
                    "question_ja": "インドの米の生産量は、中国より多い。",
                    "options": ["○", "×"],
                    "answer": "×",
                    "explanation": "世界1位は中国であり、インドより多いです。"
                },
                {
                    "id": 2,
                    "question_ja": "インドネシアの米の生産量は、中国の半分以上だ。",
                    "options": ["○", "×"],
                    "answer": "×",
                    "explanation": "インドネシアの生産量は中国の半分に満たない数値です。"
                },
                {
                    "id": 3,
                    "question_ja": "上位3か国（中国、インド、インドネシア）で世界の米の生産量の半分以上を占める。",
                    "options": ["○", "×"],
                    "answer": "○",
                    "explanation": "上位3か国の合計は全世界生産量の過半数を占めています。"
                },
                {
                    "id": 4,
                    "question_ja": "日本の米の生産量は、世界5位以内に入っている。",
                    "options": ["○", "×"],
                    "answer": "×",
                    "explanation": "日本の順位はトップ5に入っていません。"
                },
                {
                    "id": 5,
                    "question_ja": "アメリカの米の生産量は、日本の倍以上だ。",
                    "options": ["○", "×"],
                    "answer": "×",
                    "explanation": "グラフデータ上、倍以上ではありません。"
                }
            ]
        },
        {
            "exercise_id": 3,
            "title_ja": "（　）に言葉を入れなさい。",
            "items": [
                {
                    "id": 1,
                    "question_ja": "日本の国土の（　面積　）は約38万平方キロメートルだ。",
                    "answer": "面積",
                    "explanation": "土地の広さは「面積」です。"
                },
                {
                    "id": 2,
                    "question_ja": "睡眠時間が（　不足している　）と、集中力が落ちる。",
                    "answer": "不足している",
                    "explanation": "足りていない状態は「不足している」です。"
                },
                {
                    "id": 3,
                    "question_ja": "売り上げを（　増やし　）て、利益を出したい。",
                    "answer": "増やし",
                    "explanation": "多くすることは他動詞「増やす」です。"
                },
                {
                    "id": 4,
                    "question_ja": "今日の気温は氷点下で、（　マイナス　）3度だ。",
                    "answer": "マイナス",
                    "explanation": "零下（氷点下）は「マイナス」です。"
                },
                {
                    "id": 5,
                    "question_ja": "クラスの（　全員　）が合格した。",
                    "answer": "全員",
                    "explanation": "メンバー全員を表す言葉は「全員」です。"
                }
            ]
        },
        {
            "exercise_id": 4,
            "title_ja": "言葉の組み合わせを選びなさい。",
            "items": [
                {
                    "id": 1,
                    "question_ja": "1. 野菜を（ a 大量 / b たっぷり / c プラス ）食べる",
                    "options": ["a 大量", "b たっぷり", "c プラス"],
                    "answer": "b",
                    "explanation": "「たっぷりと食べる」"
                },
                {
                    "id": 2,
                    "question_ja": "1. ゴミを（ a 大量 / b たっぷり / c プラス ）に出す",
                    "options": ["a 大量", "b たっぷり", "c プラス"],
                    "answer": "a",
                    "explanation": "「大量に出す」"
                },
                {
                    "id": 3,
                    "question_ja": "1. 経験が（ a 大量 / b たっぷり / c プラス ）になる",
                    "options": ["a 大量", "b たっぷり", "c プラス"],
                    "answer": "c",
                    "explanation": "「プラスになる」"
                },
                {
                    "id": 4,
                    "question_ja": "2. （ a 記録 / b 計算 / c 平均 ）点を出す",
                    "options": ["a 記録", "b 計算", "c 平均"],
                    "answer": "c",
                    "explanation": "「平均点を出す」"
                },
                {
                    "id": 5,
                    "question_ja": "2. お釣りを（ a 記録 / b 計算 / c 平均 ）する",
                    "options": ["a 記録", "b 計算", "c 平均"],
                    "answer": "b",
                    "explanation": "「お釣りを計算する」"
                },
                {
                    "id": 6,
                    "question_ja": "2. ノートに（ a 記録 / b 計算 / c 平均 ）を取る",
                    "options": ["a 記録", "b 計算", "c 平均"],
                    "answer": "a",
                    "explanation": "「記録を取る」"
                }
            ]
        },
        {
            "exercise_id": 5,
            "title_ja": "カレーの作り方の文章の（　）に適切な言葉を入れなさい。",
            "items": [
                {
                    "id": 1,
                    "question_ja": "具材を切って鍋に入れ、塩コショウを（①少々）振って炒める。",
                    "answer": "少々",
                    "explanation": "ほんの少しの分量は「少々」。"
                },
                {
                    "id": 2,
                    "question_ja": "肉は一口（②サイズ）に切る。",
                    "answer": "サイズ",
                    "explanation": "大きさの寸法「一口サイズ」。"
                },
                {
                    "id": 3,
                    "question_ja": "水を（③加えて）煮込む。",
                    "answer": "加えて",
                    "explanation": "水を足し入れる「加える」。"
                },
                {
                    "id": 4,
                    "question_ja": "火を（④減らす）／弱める。",
                    "answer": "減らす",
                    "explanation": "火力や分量を抑える「減らす」。"
                },
                {
                    "id": 5,
                    "question_ja": "食べる（⑤人数）に合わせて、",
                    "answer": "人数",
                    "explanation": "人の頭数「人数」。"
                },
                {
                    "id": 6,
                    "question_ja": "カレールーを（⑥増やす）。",
                    "answer": "増やす",
                    "explanation": "分量を多くする「増やす」。"
                },
                {
                    "id": 7,
                    "question_ja": "隠し味にチョコを入れるとコクが（⑦プラス）される。",
                    "answer": "プラス",
                    "explanation": "付加価値や味が増す「プラス」。"
                },
                {
                    "id": 8,
                    "question_ja": "もしカレーが（⑧余った）ら、次の日はうどんにする。",
                    "answer": "余った",
                    "explanation": "残ってしまう「余る」。"
                }
            ]
        }
    ]
}
