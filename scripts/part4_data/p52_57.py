# -*- coding: utf-8 -*-
"""
Part 4 Information Retrieval (情報検索): Problems 52 to 57
Pages 120 - 131
"""

lessons = [
    {
        "id": "dokkai-n3-p4-52",
        "pages": [120, 121],
        "problemNumber": 52,
        "genre": "広告",
        "genre_en": "Advertisement",
        "genre_zh": "广告",
        "title_ja": "問題52 広告（Sマート 割引セール）",
        "title_en": "Problem 52: Advertisement (S-Mart Discount Sale)",
        "title_zh": "问题52 广告（S超市 折扣特卖）",
        "preReading": {
            "question_ja": "スーパーやコンビニの割引券を使ったことがありますか。",
            "question_en": "Have you ever used discount coupons at supermarkets or convenience stores?",
            "question_zh": "你在超市或便利店用过打折券吗？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "Read the following text and answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "Sマート（24hオープン）は近くて便利！",
                    "ruby_html": "Sマート（24hオープン）は<ruby>近<rt>ちか</rt></ruby>くて<ruby>便利<rt>べんり</rt></ruby>！",
                    "text_en": "S-Mart (open 24 hours) is close and convenient!"
                },
                {
                    "id": 2,
                    "text_ja": "6月のお得な割引セール！ 18時〜24時だけ！",
                    "ruby_html": "6<ruby>月<rt>がつ</rt></ruby>のお<ruby>得<rt>とく</rt></ruby>な<ruby>割引<rt>わりびき</rt></ruby>セール！ 18<ruby>時<rt>じ</rt></ruby>〜24<ruby>時<rt>じ</rt></ruby>だけ！",
                    "text_en": "Bargain discount sale in June! From 18:00 to 24:00 only!"
                },
                {
                    "id": 3,
                    "text_ja": "セール期間：2014年6月2日(月)〜6月28日(土)",
                    "ruby_html": "セール<ruby>期間<rt>きかん</rt></ruby>：2014<ruby>年<rt>ねん</rt></ruby>6<ruby>月<rt>がつ</rt></ruby>2<ruby>日<rt>にち</rt></ruby>(<ruby>月<rt>げつ</rt></ruby>)〜6<ruby>月<rt>がつ</rt></ruby>28<ruby>日<rt>にち</rt></ruby>(<ruby>土<rt>ど</rt></ruby>)",
                    "text_en": "Sale period: Monday, June 2, 2014 to Saturday, June 28."
                },
                {
                    "id": 4,
                    "text_ja": "＊下の割引券は切って、かならず商品と一緒にレジにお出しください！",
                    "ruby_html": "＊<ruby>下<rt>した</rt></ruby>の<ruby>割引券<rt>わりびきけん</rt></ruby>は<ruby>切<rt>き</rt></ruby>って、かならず<ruby>商品<rt>しょうひん</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>にレジにお<ruby>出<rt>だ</rt></ruby>しください！",
                    "text_en": "* Please cut out the coupons below and be sure to present them at the register along with the products!"
                },
                {
                    "id": 5,
                    "text_ja": "＊この広告はお一人様1枚限りとさせていただきます。",
                    "ruby_html": "＊この<ruby>広告<rt>こうこく</rt></ruby>はお<ruby>一人様<rt>ひとりさま</rt></ruby>1<ruby>枚<rt>まい</rt></ruby><ruby>限<rt>かぎ</rt></ruby>りとさせていただきます。",
                    "text_en": "* Limit one coupon flyer per customer."
                },
                {
                    "id": 6,
                    "text_ja": "＊割引券1枚につき商品1個が割引となります。",
                    "ruby_html": "＊<ruby>割引券<rt>わりびきけん</rt></ruby>1<ruby>枚<rt>まい</rt></ruby>につき<ruby>商品<rt>しょうひん</rt></ruby>1<ruby>個<rt>こ</rt></ruby>が<ruby>割引<rt>わりびき</rt></ruby>となります。",
                    "text_en": "* One coupon applies a discount to one single item."
                },
                {
                    "id": 7,
                    "text_ja": "＊お店によっては、商品がない場合もあります。",
                    "ruby_html": "＊お<ruby>店<rt>みせ</rt></ruby>によっては、<ruby>商品<rt>しょうひん</rt></ruby>がない<ruby>場合<rt>ばあい</rt></ruby>もあります。",
                    "text_en": "* Depending on the store, some items may not be in stock."
                },
                {
                    "id": 8,
                    "text_ja": "＊割引券が利用できるのは、18時〜24時です。",
                    "ruby_html": "＊<ruby>割引券<rt>わりびきけん</rt></ruby>が<ruby>利用<rt>りよう</rt></ruby>できるのは、18<ruby>時<rt>じ</rt></ruby>〜24<ruby>時<rt>じ</rt></ruby>です。",
                    "text_en": "* Coupons can only be used between 18:00 and 24:00."
                },
                {
                    "id": 9,
                    "text_ja": "【割引券一覧】2日(月)〜14日(土)：チョコレート（書かれた価格より30円引き）、ドーナッツ（書かれた価格より20円引き）。",
                    "ruby_html": "【<ruby>割引券<rt>わりびきけん</rt></ruby><ruby>一覧<rt>いちらん</rt></ruby>】2<ruby>日<rt>にち</rt></ruby>(<ruby>月<rt>げつ</rt></ruby>)〜14<ruby>日<rt>にち</rt></ruby>(<ruby>土<rt>ど</rt></ruby>)：チョコレート（<ruby>書<rt>か</rt></ruby>かれた<ruby>価格<rt>かかく</rt></ruby>より30<ruby>円引<rt>えんび</rt></ruby>き）、ドーナッツ（<ruby>書<rt>か</rt></ruby>かれた<ruby>価格<rt>かかく</rt></ruby>より20<ruby>円引<rt>えんび</rt></ruby>き）。",
                    "text_en": "[Coupon List] June 2 (Mon) - 14 (Sat): Chocolate (30 yen off marked price), Doughnuts (20 yen off marked price)."
                },
                {
                    "id": 10,
                    "text_ja": "15日(日)〜28日(土)：アイスクリーム（書かれた価格より20円引き）、ホットコーヒー（書かれた価格より30円引き）。",
                    "ruby_html": "15<ruby>日<rt>にち</rt></ruby>(<ruby>日<rt>にち</rt></ruby>)〜28<ruby>日<rt>にち</rt></ruby>(<ruby>土<rt>ど</rt></ruby>)：アイスクリーム（<ruby>書<rt>か</rt></ruby>かれた<ruby>価格<rt>かかく</rt></ruby>より20<ruby>円引<rt>えんび</rt></ruby>き）、ホットコーヒー（<ruby>書<rt>か</rt></ruby>かれた<ruby>価格<rt>かかく</rt></ruby>より30<ruby>円引<rt>えんび</rt></ruby>き）。",
                    "text_en": "June 15 (Sun) - 28 (Sat): Ice cream (20 yen off marked price), Hot coffee (30 yen off marked price)."
                }
            ]
        },
        "footnotes": [],
        "vocabulary": [
            {
                "term": "お得な",
                "reading": "おとくな",
                "meaning": "a good bargain / 合算的",
                "type": "na-adjective"
            },
            {
                "term": "セール期間",
                "reading": "せーるきかん",
                "meaning": "period of a sale / 折扣优惠期间",
                "type": "noun"
            },
            {
                "term": "割引券",
                "reading": "わりびきけん",
                "meaning": "discount coupon / 打折券",
                "type": "noun"
            },
            {
                "term": "〜限り",
                "reading": "〜かぎり",
                "meaning": "restricted to ~, limited to ~ / 只限用〜",
                "type": "suffix"
            },
            {
                "term": "商品",
                "reading": "しょうひん",
                "meaning": "product, merchandise / 商品",
                "type": "noun"
            },
            {
                "term": "価格",
                "reading": "かかく",
                "meaning": "price / 价格",
                "type": "noun"
            },
            {
                "term": "〜円引き",
                "reading": "〜えんびき",
                "meaning": "discount of ~ yen / 便宜〜日元",
                "type": "phrase"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-52-1",
                "questionNumber": 1,
                "questionText_ja": "アリさんは6月18日午後10時頃、この広告を1枚持ってコンビニに行った。アイスクリームを2個買った。アイスクリームは100円と書いてあった。いくら払ったか。",
                "questionText_en": "Around 10:00 PM on June 18, Ali went to the convenience store with one copy of this advertisement. He bought two ice creams. The price tag on the ice cream was 100 yen. How much did he pay?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "200円",
                        "text_en": "200 yen"
                    },
                    {
                        "id": 2,
                        "text_ja": "180円",
                        "text_en": "180 yen"
                    },
                    {
                        "id": 3,
                        "text_ja": "160円",
                        "text_en": "160 yen"
                    },
                    {
                        "id": 4,
                        "text_ja": "140円",
                        "text_en": "140 yen"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "6月18日はアイスクリームの割引期間（15日〜28日）内であり、午後10時（22時）は割引券が使える時間（18時〜24時）です。ただし、広告には「割引券1枚につき商品1個が割引となります」「お一人様1枚限り」と書かれているため、2個のうち割引（20円引き）されるのは1個だけです。したがって、(100 - 20) + 100 = 180円 となり、正解は 2 です。",
                "explanation_en": "June 18 falls within the ice cream discount window (June 15–28), and 10:00 PM (22:00) is within the eligible hours (18:00–24:00). However, the rules specify that only one coupon is allowed per customer and one coupon applies to only one item. Thus, only one ice cream receives the 20-yen discount (100 - 20 = 80 yen), and the second is charged at the regular 100 yen. Total: 80 + 100 = 180 yen. Therefore, Option 2 is correct."
            },
            {
                "questionId": "q-52-2",
                "questionNumber": 2,
                "questionText_ja": "ドーナッツを安く買いたい。この広告を持って、いつ買いに行けばよいか。",
                "questionText_en": "You want to buy doughnuts at a discount. When should you take this advertisement and go shopping?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "6月10日 午前10時ごろ",
                        "text_en": "Around 10:00 AM on June 10"
                    },
                    {
                        "id": 2,
                        "text_ja": "6月12日 午後10時ごろ",
                        "text_en": "Around 10:00 PM on June 12"
                    },
                    {
                        "id": 3,
                        "text_ja": "6月16日 午前8時ごろ",
                        "text_en": "Around 8:00 AM on June 16"
                    },
                    {
                        "id": 4,
                        "text_ja": "6月20日 午後8時ごろ",
                        "text_en": "Around 8:00 PM on June 20"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "ドーナッツの割引期間は「2日(月)〜14日(土)」です。また、割引券が利用できる時間帯は「18時〜24時」に限られています。選択肢2「6月12日 午後10時ごろ」は期間内（2日〜14日の間）かつ時間内（22時は18時〜24時の間）であるため条件を完全に満たしています。したがって 2 が正解です。",
                "explanation_en": "The discount period for doughnuts is June 2 (Mon) to June 14 (Sat), and the valid coupon usage hours are 18:00 to 24:00. Option 2 ('Around 10:00 PM on June 12') falls within the June 2–14 period and within the 18:00–24:00 time frame (22:00). Therefore, Option 2 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆情報検索（Sマート 割引セール）",
            "text_ja": "情報検索問題の基本は、質問文の条件（日付・時間・対象商品・数量）を明確にし、広告の条件枠（対象期間、利用可能時間、使用制限事項）と照らし合わせることです。特に「1枚につき1個」「お一人様1枚限り」などの注記（米印・アスタリスク）を見落とさないようにしましょう。",
            "text_en": "The key to information retrieval tasks is identifying the question's criteria (date, time, item, quantity) and checking against limitations (valid periods, hours, coupon restrictions like '1 per person' and '1 discount per coupon'). Always inspect asterisked notes carefully.",
            "structureLayout": [
                {
                    "component": "基本情報",
                    "detail": "セール期間：6月2日〜28日、利用可能時間：18時〜24時",
                    "en": "Basic info: Sale period June 2–28, usable 18:00–24:00."
                },
                {
                    "component": "利用制限",
                    "detail": "1人1枚限り、1枚につき1個割引",
                    "en": "Restrictions: Limit 1 coupon per customer, 1 item discounted per coupon."
                },
                {
                    "component": "商品別期間",
                    "detail": "チョコ・ドーナツ（2日〜14日）、アイス・コーヒー（15日〜28日）",
                    "en": "Item dates: Chocolate & Donuts (2nd–14th), Ice cream & Coffee (15th–28th)."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "数量と制限に注意！2個買っても割引券が1枚なら、引かれるのは1個分のみです。",
            "point_en": "Watch quantity vs. restrictions! Buying two items with one coupon means only one item gets discounted."
        }
    },
    {
        "id": "dokkai-n3-p4-53",
        "pages": [122, 123],
        "problemNumber": 53,
        "genre": "求人広告",
        "genre_en": "Job Recruitment Ad",
        "genre_zh": "招聘广告",
        "title_ja": "問題53 求人広告（すしの吉野 求人募集）",
        "title_en": "Problem 53: Job Recruitment Ad (Sushi Yoshino Staff Wanted)",
        "title_zh": "问题53 招聘广告（吉野寿司 招募兼职）",
        "preReading": {
            "question_ja": "日本でアルバイトを探すとき、どんな条件を重視しますか。",
            "question_en": "What conditions do you focus on when looking for a part-time job in Japan?",
            "question_zh": "在日本找兼职时，你最看重哪些条件？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章は求人募集広告である。右の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The following text is a job recruitment advertisement. Answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "一緒にすし屋で働きませんか！ アルバイト大募集！",
                    "ruby_html": "<ruby>一緒<rt>いっしょ</rt></ruby>にすし<ruby>屋<rt>や</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>きませんか！ アルバイト<ruby>大募集<rt>だいぼしゅう</rt></ruby>！",
                    "text_en": "Won't you work with us at a sushi restaurant? Hiring part-time staff now!"
                },
                {
                    "id": 2,
                    "text_ja": "職種：調理の手伝い",
                    "ruby_html": "<ruby>職種<rt>しょくしゅ</rt></ruby>：<ruby>調理<rt>ちょうり</rt></ruby>の<ruby>手伝<rt>てつだ</rt></ruby>い",
                    "text_en": "Job type: Cooking assistant / kitchen help."
                },
                {
                    "id": 3,
                    "text_ja": "勤務時間・給与：①8:00-15:00 時給900円、②15:00-24:00 時給1,000円（時給は経験を考慮）。",
                    "ruby_html": "<ruby>勤務時間<rt>きんむじかん</rt></ruby>・<ruby>給与<rt>きゅうよ</rt></ruby>：①8:00-15:00 <ruby>時給<rt>じきゅう</rt></ruby>900<ruby>円<rt>えん</rt></ruby>、②15:00-24:00 <ruby>時給<rt>じきゅう</rt></ruby>1,000<ruby>円<rt>えん</rt></ruby>（<ruby>時給<rt>じきゅう</rt></ruby>は<ruby>経験<rt>けいけん</rt></ruby>を<ruby>考慮<rt>こうりょ</rt></ruby>）。",
                    "text_en": "Working hours & wages: (1) 8:00–15:00: 900 yen/hour; (2) 15:00–24:00: 1,000 yen/hour (experience taken into consideration)."
                },
                {
                    "id": 4,
                    "text_ja": "＊週2日、1日5時間以上働ける方。",
                    "ruby_html": "＊<ruby>週<rt>しゅう</rt></ruby>2<ruby>日<rt>にち</rt></ruby>、1<ruby>日<rt>にち</rt></ruby>5<ruby>時間以上<rt>じかんいじょう</rt></ruby><ruby>働<rt>はたら</rt></ruby>ける<ruby>方<rt>かた</rt></ruby>。",
                    "text_en": "* Those who can work at least 2 days a week and at least 5 hours a day."
                },
                {
                    "id": 5,
                    "text_ja": "＊曜日、時間は相談に応じます。",
                    "ruby_html": "＊<ruby>曜日<rt>ようび</rt></ruby>、<ruby>時間<rt>じかん</rt></ruby>は<ruby>相談<rt>そうだん</rt></ruby>に<ruby>応<rt>おう</rt></ruby>じます。",
                    "text_en": "* Days and hours negotiable upon consultation."
                },
                {
                    "id": 6,
                    "text_ja": "＊経験のない方もOK！",
                    "ruby_html": "＊<ruby>経験<rt>けいけん</rt></ruby>のない<ruby>方<rt>かた</rt></ruby>もOK！",
                    "text_en": "* People with no experience are welcome!"
                },
                {
                    "id": 7,
                    "text_ja": "＊主婦・学生の方歓迎。（高校生は不可）",
                    "ruby_html": "＊<ruby>主婦<rt>しゅふ</rt></ruby>・<ruby>学生<rt>がくせい</rt></ruby>の<ruby>方歓迎<rt>かたかんげい</rt></ruby>。（<ruby>高校生<rt>こうこうせい</rt></ruby>は<ruby>不可<rt>ふか</rt></ruby>）",
                    "text_en": "* Homemakers and students welcome. (High school students not accepted)"
                },
                {
                    "id": 8,
                    "text_ja": "少しでも興味ある方はお電話ください！",
                    "ruby_html": "<ruby>少<rt>すこ</rt></ruby>しでも<ruby>興味<rt>きょうみ</rt></ruby>ある<ruby>方<rt>かた</rt></ruby>はお<ruby>電話<rt>でんわ</rt></ruby>ください！",
                    "text_en": "If you are interested at all, please give us a call!"
                },
                {
                    "id": 9,
                    "text_ja": "応募方法：お電話の上、履歴書（写真付）を持って面接にお越しください。",
                    "ruby_html": "<ruby>応募方法<rt>おうぼほうほう</rt></ruby>：お<ruby>電話<rt>でんわ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>、<ruby>履歴書<rt>りれきしょ</rt></ruby>（<ruby>写真付<rt>しゃしんつき</rt></ruby>）を<ruby>持<rt>も</rt></ruby>って<ruby>面接<rt>めんせつ</rt></ruby>にお<ruby>越<rt>こ</rt></ruby>しください。",
                    "text_en": "Application procedure: Please call first, then come for an interview bringing a resume with photo attached."
                },
                {
                    "id": 10,
                    "text_ja": "勤務地・連絡先：A市山田町 2-2-1 すしの吉野（山田店） TEL: 1111-3333",
                    "ruby_html": "<ruby>勤務地<rt>きんむち</rt></ruby>・<ruby>連絡先<rt>れんらくさき</rt></ruby>：A<ruby>市<rt>し</rt></ruby><ruby>山田町<rt>やまだちょう</rt></ruby> 2-2-1 すしの<ruby>吉野<rt>よしの</rt></ruby>（<ruby>山田店<rt>やまだてん</rt></ruby>） TEL: 1111-3333",
                    "text_en": "Work location & contact: 2-2-1 Yamada-cho, City A; Sushi Yoshino (Yamada Branch) TEL: 1111-3333."
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "職種",
                "meaning_ja": "職業の種類",
                "meaning_en": "job category / type of occupation"
            },
            {
                "label": "注2",
                "term": "考慮",
                "meaning_ja": "よく考えること",
                "meaning_en": "taking into consideration, careful thought"
            }
        ],
        "vocabulary": [
            {
                "term": "募集",
                "reading": "ぼしゅう",
                "meaning": "recruitment / 招募",
                "type": "noun"
            },
            {
                "term": "勤務",
                "reading": "きんむ",
                "meaning": "service, duty, work / 工作",
                "type": "noun"
            },
            {
                "term": "給与",
                "reading": "きゅうよ",
                "meaning": "salary, pay / 薪水",
                "type": "noun"
            },
            {
                "term": "時給",
                "reading": "じきゅう",
                "meaning": "hourly wage / 时薪",
                "type": "noun"
            },
            {
                "term": "歓迎",
                "reading": "かんげい",
                "meaning": "[be] welcome / 欢迎",
                "type": "noun"
            },
            {
                "term": "応募",
                "reading": "おうぼ",
                "meaning": "application, applying / 应聘",
                "type": "noun"
            },
            {
                "term": "履歴書",
                "reading": "りれきしょ",
                "meaning": "résumé, CV / 简历",
                "type": "noun"
            },
            {
                "term": "面接",
                "reading": "めんせつ",
                "meaning": "interview / 面试",
                "type": "noun"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-53-1",
                "questionNumber": 1,
                "questionText_ja": "ホンさんは、火・木・金曜日に夕方5時から夜10時まで働くことになった。1週間で給料がいくらもらえるか。",
                "questionText_en": "Hong ended up working on Tuesdays, Thursdays, and Fridays from 5:00 PM to 10:00 PM. How much wage will he receive in one week?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "9,000円",
                        "text_en": "9,000 yen"
                    },
                    {
                        "id": 2,
                        "text_ja": "9,500円",
                        "text_en": "9,500 yen"
                    },
                    {
                        "id": 3,
                        "text_ja": "13,500円",
                        "text_en": "13,500 yen"
                    },
                    {
                        "id": 4,
                        "text_ja": "15,000円",
                        "text_en": "15,000 yen"
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "夕方5時（17:00）から夜10時（22:00）までは1日あたり5時間です。この時間帯は「②15:00-24:00 時給1,000円」に該当します。1日あたり 5時間 × 1,000円 ＝ 5,000円 となります。火・木・金の週3日勤務するため、1週間で 5,000円 × 3日 ＝ 15,000円 となります。したがって 4 が正解です。",
                "explanation_en": "From 5:00 PM (17:00) to 10:00 PM (22:00) is 5 hours per day. This falls under shift (2) 15:00–24:00 where hourly wage is 1,000 yen. Daily pay is 5 hours * 1,000 yen = 5,000 yen. Working 3 days a week (Tue, Thu, Fri), weekly pay is 5,000 yen * 3 = 15,000 yen. Therefore, Option 4 is correct."
            },
            {
                "questionId": "q-53-2",
                "questionNumber": 2,
                "questionText_ja": "このすし屋で働ける人はだれか。",
                "questionText_en": "Who can work at this sushi restaurant?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "経験がある主婦。月曜日と火曜日に9時から12時まで働ける。",
                        "text_en": "An experienced homemaker who can work Mondays and Tuesdays from 9:00 to 12:00."
                    },
                    {
                        "id": 2,
                        "text_ja": "経験がない大学生。水曜日に午後6時から午後11時まで働ける。",
                        "text_en": "A college student without experience who can work Wednesdays from 6:00 PM to 11:00 PM."
                    },
                    {
                        "id": 3,
                        "text_ja": "経験がある高校生。火曜日と木曜日に午後3時から午後9時まで働ける。",
                        "text_en": "An experienced high school student who can work Tuesdays and Thursdays from 3:00 PM to 9:00 PM."
                    },
                    {
                        "id": 4,
                        "text_ja": "経験がない大学生。水曜日と土曜日に午後5時から夜10時まで働ける。",
                        "text_en": "A college student without experience who can work Wednesdays and Saturdays from 5:00 PM to 10:00 PM."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "応募条件は「週2日、1日5時間以上働ける方」「経験のない方もOK」「主婦・学生の方歓迎（高校生は不可）」です。\n1: 9時から12時は3時間で、「1日5時間以上」を満たしません。\n2: 水曜日のみ（週1日）で、「週2日以上」を満たしません。\n3: 高校生は「高校生は不可」により働けません。\n4: 週2日（水・土）、1日5時間（17:00〜22:00）、大学生で未経験OKの条件をすべて満たしています。したがって 4 が正解です。",
                "explanation_en": "The requirements are: 'at least 2 days a week, at least 5 hours a day', 'no experience necessary', and 'homemakers and students welcome (high school students not permitted)'.\nOption 1: 9:00 to 12:00 is only 3 hours (< 5 hours).\nOption 2: Wednesdays only is just 1 day (< 2 days).\nOption 3: High school students are disqualified.\nOption 4: 2 days a week (Wed/Sat), 5 hours a day (17:00–22:00), student, no experience needed—meets all criteria! Therefore, Option 4 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆求人広告（すしの吉野 求人募集）",
            "text_ja": "求人広告では、勤務条件（日数・時間帯・時給）の掛け算計算問題と、応募資格（対象者・除外対象・経験不問など）のフィルタリング問題が頻出します。カッコ書きの「高校生は不可」のような除外条件に特に注意しましょう。",
            "text_en": "In job advertisement problems, calculation of weekly wages based on shifts and hourly rates is common, alongside qualification verification (minimum hours/days, prohibited applicants like high schoolers). Look out for exclusions in parentheses.",
            "structureLayout": [
                {
                    "component": "勤務シフト",
                    "detail": "①8:00-15:00（時給900円）、②15:00-24:00（時給1,000円）",
                    "en": "Shifts: (1) 8:00–15:00 (900 yen/hr), (2) 15:00–24:00 (1,000 yen/hr)."
                },
                {
                    "component": "応募要件",
                    "detail": "週2日・1日5時間以上、未経験可、高校生不可",
                    "en": "Requirements: >=2 days/wk, >=5 hrs/day, unexperienced OK, no high schoolers."
                },
                {
                    "component": "応募手順",
                    "detail": "電話のうえ、写真付き履歴書持参で面接",
                    "en": "Procedure: Call in advance, attend interview with photo résumé."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "シフトごとの時給の違いと、1日の実働時間を正しく計算しましょう。",
            "point_en": "Make sure to match the exact shift hour rate to the actual daily hours worked."
        }
    },
    {
        "id": "dokkai-n3-p4-54",
        "pages": [124, 125],
        "problemNumber": 54,
        "genre": "広告",
        "genre_en": "Real Estate Listing",
        "genre_zh": "租房广告",
        "title_ja": "問題54 広告（アパート「マイハウスネット」）",
        "title_en": "Problem 54: Real Estate Listing (Apartment 'My House Net')",
        "title_zh": "问题54 租房广告（公寓“My House Net”）",
        "preReading": {
            "question_ja": "アパートを借りるとき、家賃以外にどんな費用がかかるか知っていますか。",
            "question_en": "Do you know what expenses are required besides monthly rent when renting an apartment?",
            "question_zh": "租公寓时，除了房租之外还需要哪些费用，你知道吗？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "Read the following text and answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "アパート情報サイト「マイハウスネット」（20XX年3月現在）",
                    "ruby_html": "アパート<ruby>情報<rt>じょうほう</rt></ruby>サイト「マイハウスネット」（20XX<ruby>年<rt>ねん</rt></ruby>3<ruby>月現在<rt>がつげんざい</rt></ruby>）",
                    "text_en": "Apartment Information Website 'My House Net' (As of March 20XX)"
                },
                {
                    "id": 2,
                    "text_ja": "中山田駅 徒歩3分、アパート 築10年、家賃 30,000円、敷金／礼金 1か月／1か月、ワンルーム 19.84m²。",
                    "ruby_html": "<ruby>中山田駅<rt>なかやまだえき</rt></ruby> <ruby>徒歩<rt>とほ</rt></ruby>3<ruby>分<rt>ふん</rt></ruby>、アパート <ruby>築<rt>ちく</rt></ruby>10<ruby>年<rt>ねん</rt></ruby>、<ruby>家賃<rt>やちん</rt></ruby> 30,000<ruby>円<rt>えん</rt></ruby>、<ruby>敷金<rt>しききん</rt></ruby>／<ruby>礼金<rt>れいきん</rt></ruby> 1か<ruby>月<rt>げつ</rt></ruby>／1か<ruby>月<rt>げつ</rt></ruby>、ワンルーム 19.84m²。",
                    "text_en": "Nakayamada Station 3 min walk; Apartment 10 years old; Rent 30,000 yen; Security deposit / Key money: 1 month / 1 month; Studio 19.84 m²."
                },
                {
                    "id": 3,
                    "text_ja": "・南向き ・5階建ての2階 ・スーパーまで400m",
                    "ruby_html": "・<ruby>南向<rt>みなみむ</rt></ruby>き ・5<ruby>階建<rt>かいだ</rt></ruby>ての2<ruby>階<rt>かい</rt></ruby> ・スーパーまで400m",
                    "text_en": "- South-facing - 2nd floor of a 5-story building - 400m to supermarket"
                },
                {
                    "id": 4,
                    "text_ja": "・手数料無料！ 契約時には家賃1か月分と敷金・礼金各1か月分だけでOK！",
                    "ruby_html": "・<ruby>手数料無料<rt>てすうりょうむりょう</rt></ruby>！ <ruby>契約時<rt>けいやくじ</rt></ruby>には<ruby>家賃<rt>やちん</rt></ruby>1か<ruby>月分<rt>げつぶん</rt></ruby>と<ruby>敷金<rt>しききん</rt></ruby>・<ruby>礼金<rt>れいきん</rt></ruby><ruby>各<rt>かく</rt></ruby>1か<ruby>月分<rt>げつぶん</rt></ruby>だけでOK！",
                    "text_en": "- No brokerage commission! At contract signing, only 1 month's rent plus 1 month each of security deposit and key money is required!"
                },
                {
                    "id": 5,
                    "text_ja": "・ペットは相談可！",
                    "ruby_html": "・ペットは<ruby>相談可<rt>そうだんか</rt></ruby>！",
                    "text_en": "- Pets allowed upon consultation!"
                },
                {
                    "id": 6,
                    "text_ja": "間取り図：北側に玄関・浴室・トイレ、洋室19.84m²（収納あり）、南側にベランダ。",
                    "ruby_html": "<ruby>間取<rt>まと</rt></ruby>り<ruby>図<rt>ず</rt></ruby>：<ruby>北側<rt>きたがわ</rt></ruby>に<ruby>玄関<rt>げんかん</rt></ruby>・<ruby>浴室<rt>よくしつ</rt></ruby>・トイレ、<ruby>洋室<rt>ようしつ</rt></ruby>19.84m²（<ruby>収納<rt>しゅうのう</rt></ruby>あり）、<ruby>南側<rt>みなみがわ</rt></ruby>にベランダ。",
                    "text_en": "Floor layout: North side has front entrance, bath, and toilet; Western-style room 19.84 m² (with closet); South side has veranda."
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "敷金",
                "meaning_ja": "アパートを契約するときに、保証金として大家さんに預けるお金",
                "meaning_en": "security deposit deposited with landlord when contracting an apartment"
            },
            {
                "label": "注2",
                "term": "礼金",
                "meaning_ja": "アパートを契約するときに、お礼として大家さんに支払うお金",
                "meaning_en": "gratuity fee (key money) paid to landlord upon contracting"
            }
        ],
        "vocabulary": [
            {
                "term": "徒歩",
                "reading": "とほ",
                "meaning": "on foot, walking / 徒步",
                "type": "noun"
            },
            {
                "term": "築",
                "reading": "ちく",
                "meaning": "built in [year], building age / 建造（年数）",
                "type": "noun"
            },
            {
                "term": "家賃",
                "reading": "やちん",
                "meaning": "[apartment] rent / 房租",
                "type": "noun"
            },
            {
                "term": "ワンルーム",
                "reading": "わんるーむ",
                "meaning": "single-room studio apartment / 单间公寓",
                "type": "noun"
            },
            {
                "term": "〜向き",
                "reading": "〜むき",
                "meaning": "facing ~ / 朝向〜",
                "type": "suffix"
            },
            {
                "term": "契約",
                "reading": "けいやく",
                "meaning": "contract, lease / 合同",
                "type": "noun"
            },
            {
                "term": "玄関",
                "reading": "げんかん",
                "meaning": "front entrance, doorway / 房门、玄关",
                "type": "noun"
            },
            {
                "term": "浴室",
                "reading": "よくしつ",
                "meaning": "washroom, bathroom / 浴室",
                "type": "noun"
            },
            {
                "term": "収納",
                "reading": "しゅうのう",
                "meaning": "storage area, closet / 储物间、收纳",
                "type": "noun"
            },
            {
                "term": "ベランダ",
                "reading": "べらんだ",
                "meaning": "veranda, balcony / 阳台",
                "type": "noun"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-54-1",
                "questionNumber": 1,
                "questionText_ja": "契約するときにいくら必要か。",
                "questionText_en": "How much money is required upon signing the contract?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "3万円",
                        "text_en": "30,000 yen"
                    },
                    {
                        "id": 2,
                        "text_ja": "3万5千円",
                        "text_en": "35,000 yen"
                    },
                    {
                        "id": 3,
                        "text_ja": "9万円",
                        "text_en": "90,000 yen"
                    },
                    {
                        "id": 4,
                        "text_ja": "9万5千円",
                        "text_en": "95,000 yen"
                    }
                ],
                "correctAnswer": 3,
                "explanation_ja": "広告に「手数料無料！ 契約時には家賃1か月分と敷金・礼金各1か月分だけでOK！」と書かれています。家賃は30,000円、敷金は1か月分（30,000円）、礼金も1か月分（30,000円）です。手数料は無料なので、合計は 30,000 ＋ 30,000 ＋ 30,000 ＝ 90,000円（9万円）となります。したがって 3 が正解です。",
                "explanation_en": "The listing states: 'No fees! At contract signing, only 1 month of rent and 1 month each of security deposit and key money are needed!' Rent is 30,000 yen, security deposit is 1 month (30,000 yen), and key money is 1 month (30,000 yen). With no brokerage fee, the total is 30,000 + 30,000 + 30,000 = 90,000 yen (9万円). Therefore, Option 3 is correct."
            },
            {
                "questionId": "q-54-2",
                "questionNumber": 2,
                "questionText_ja": "このアパートの説明として本文の内容と合っているものはどれか。",
                "questionText_en": "Which statement correctly matches the content of the text as a description of this apartment?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "部屋は5階にある。",
                        "text_en": "The room is on the 5th floor."
                    },
                    {
                        "id": 2,
                        "text_ja": "ベランダは南側にある。",
                        "text_en": "The veranda is on the south side."
                    },
                    {
                        "id": 3,
                        "text_ja": "犬を飼うことはできない。",
                        "text_en": "You cannot keep a dog."
                    },
                    {
                        "id": 4,
                        "text_ja": "部屋にお風呂がない。",
                        "text_en": "There is no bathtub/bath in the apartment."
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "間取り図の方位マーク（矢印が北）と部屋の南向きという記述から、ベランダは南側に位置しています。したがって 2 が正解です。\n1: 「5階建ての2階」なので、部屋は2階です。\n3: 「ペットは相談可」とあるため、飼うことができないわけではありません。\n4: 間取り図に「浴室」が明記されています。",
                "explanation_en": "Based on the north arrow in the floor plan and the note '南向き' (south-facing), the veranda is situated on the south side. Therefore, Option 2 is correct.\nOption 1: It is on the 2nd floor of a 5-story building.\nOption 3: 'Pets negotiable' means keeping a pet may be permitted.\nOption 4: The floor plan clearly includes a bathroom (浴室)."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆広告（アパート「マイハウスネット」）",
            "text_ja": "不動産広告の問題では、初期費用（家賃＋敷金＋礼金＋仲介手数料等）の内訳合算と、間取り図の方角（方位記号N）・設備表示を照合する読解力が試されます。",
            "text_en": "Real estate listing questions test your ability to tally move-in initial costs (rent, deposit, key money, agency fees) and interpret floor plan orientation (North marker) and amenities.",
            "structureLayout": [
                {
                    "component": "物件概要",
                    "detail": "中山田駅徒歩3分、築10年、家賃3万円、5階建ての2階",
                    "en": "Property: 3 min walk to station, 10 yrs old, rent 30k yen, 2nd floor of 5."
                },
                {
                    "component": "初期費用",
                    "detail": "家賃1か月分＋敷金1か月分＋礼金1か月分（手数料無料）＝9万円",
                    "en": "Initial cost: 1 mo rent + 1 mo deposit + 1 mo key money (no commission) = 90k yen."
                },
                {
                    "component": "間取り・条件",
                    "detail": "ワンルーム19.84m²、南向きベランダ、浴室あり、ペット相談可",
                    "en": "Layout: 19.84m² studio, south veranda, bath included, pets negotiable."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "間取り図の方位記号（Nの矢印）を確認し、部屋の開口部（ベランダや窓）がどの方角を向いているか把握しましょう。",
            "point_en": "Check the orientation compass (arrow pointing North) to determine which cardinal direction windows and verandas face."
        }
    },
    {
        "id": "dokkai-n3-p4-55",
        "pages": [126, 127],
        "problemNumber": 55,
        "genre": "パンフレット",
        "genre_en": "Pamphlet",
        "genre_zh": "传单",
        "title_ja": "問題55 パンフレット（文化カフェ講座案内）",
        "title_en": "Problem 55: Pamphlet (Culture Cafe Course Guide)",
        "title_zh": "问题55 宣传册（文化咖啡馆讲座指南）",
        "preReading": {
            "question_ja": "地域の文化センターやサークルの講座に参加したことがありますか。",
            "question_en": "Have you ever taken part in community center or club culture courses?",
            "question_zh": "你参加过社区文化中心或社团的课程吗？"
        },
        "passageInstructions": {
            "instruction_ja": "右のページの文章は文化講座の案内パンフレットである。これを読んで下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The text on the right page is an information pamphlet for culture courses. Read it and answer the questions below. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "「文化カフェ」http://bunkacafe.com お茶を飲みながらいろいろな国の文化について語り合いませんか？",
                    "ruby_html": "「<ruby>文化<rt>ぶんか</rt></ruby>カフェ」http://bunkacafe.com お<ruby>茶<rt>ちゃ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>みながらいろいろな<ruby>国<rt>くに</rt></ruby>の<ruby>文化<rt>ぶんか</rt></ruby>について<ruby>語<rt>かた</rt></ruby>り<ruby>合<rt>あ</rt></ruby>いませんか？",
                    "text_en": "'Culture Cafe' http://bunkacafe.com Won't you talk about various world cultures while having tea?"
                },
                {
                    "id": 2,
                    "text_ja": "★語学クラス★ ①「日本語」毎週月曜 15:00-16:30 ②「アラビア語」毎週水曜 19:00-20:30 ③「中国語」第4週の日曜日 14:00-15:30",
                    "ruby_html": "★<ruby>語学<rt>ごがく</rt></ruby>クラス★ ①「<ruby>日本語<rt>にほんご</rt></ruby>」<ruby>毎週<rt>まいしゅう</rt></ruby><ruby>月曜<rt>げつよう</rt></ruby> 15:00-16:30 ②「アラビア<ruby>語<rt>ご</rt></ruby>」<ruby>毎週<rt>まいしゅう</rt></ruby><ruby>水曜<rt>すいよう</rt></ruby> 19:00-20:30 ③「<ruby>中国語<rt>ちゅうごくご</rt></ruby>」<ruby>第<rt>だい</rt></ruby>4<ruby>週<rt>しゅう</rt></ruby>の<ruby>日曜日<rt>にちようび</rt></ruby> 14:00-15:30",
                    "text_en": "Language classes: (1) Japanese: Mondays 15:00-16:30; (2) Arabic: Wednesdays 19:00-20:30; (3) Chinese: 4th Sunday 14:00-15:30."
                },
                {
                    "id": 3,
                    "text_ja": "★日本文化クラス★ ④「お茶クラス」…第4日曜日 15:00〜17:00 茶道を習ったり、和菓子を食べたり、お茶に関係することについて学びます。",
                    "ruby_html": "★<ruby>日本文化<rt>にほんぶんか</rt></ruby>クラス★ ④「お<ruby>茶<rt>ちゃ</rt></ruby>クラス」…<ruby>第<rt>だい</rt></ruby>4<ruby>日曜日<rt>にちようび</rt></ruby> 15:00〜17:00 <ruby>茶道<rt>さどう</rt></ruby>を<ruby>習<rt>なら</rt></ruby>ったり、<ruby>和菓子<rt>わがし</rt></ruby>を<ruby>食<rt>た</rt></ruby>べたり、お<ruby>茶<rt>ちゃ</rt></ruby>に<ruby>関係<rt>かんけい</rt></ruby>することについて<ruby>学<rt>まな</rt></ruby>びます。",
                    "text_en": "Japanese culture classes: (4) Tea ceremony class: 4th Sunday 15:00-17:00 (learn tea ceremony, eat Japanese sweets, and study tea-related culture)."
                },
                {
                    "id": 4,
                    "text_ja": "⑤「京都クラス」…月1回程度 京都のお寺や料理、京都についての情報を交換する。",
                    "ruby_html": "⑤「<ruby>京都<rt>きょうと</rt></ruby>クラス」…<ruby>月<rt>つき</rt></ruby>1<ruby>回程度<rt>かいていど</rt></ruby> <ruby>京都<rt>きょうと</rt></ruby>のお<ruby>寺<rt>てら</rt></ruby>や<ruby>料理<rt>りょうり</rt></ruby>、<ruby>京都<rt>きょうと</rt></ruby>についての<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>交換<rt>こうかん</rt></ruby>する。",
                    "text_en": "(5) Kyoto class: About once a month (exchange information about Kyoto's temples, cuisine, and culture)."
                },
                {
                    "id": 5,
                    "text_ja": "⑥「日本ポップカルチャークラス」…月1回程度 日本のアニメやJ-ポップなどいろいろな日本文化について学びおしゃべりする",
                    "ruby_html": "⑥「<ruby>日本<rt>にほん</rt></ruby>ポップカルチャークラス」…<ruby>月<rt>つき</rt></ruby>1<ruby>回程度<rt>かいていど</rt></ruby> <ruby>日本<rt>にほん</rt></ruby>のアニメやJ-ポップなどいろいろな<ruby>日本文化<rt>にほんぶんか</rt></ruby>について<ruby>学<rt>まな</rt></ruby>びおしゃべりする",
                    "text_en": "(6) Japanese pop culture class: About once a month (chat and learn about Japanese pop culture like anime and J-pop)."
                },
                {
                    "id": 6,
                    "text_ja": "★イベント★ ⑦「世界の料理教室」…年数回 …いろいろな国の料理を一緒に作って食べます♪",
                    "ruby_html": "★イベント★ ⑦「<ruby>世界<rt>せかい</rt></ruby>の<ruby>料理教室<rt>りょうりきょうしつ</rt></ruby>」…<ruby>年数回<rt>ねんすうかい</rt></ruby> …いろいろな<ruby>国<rt>くに</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>を<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>作<rt>つく</rt></ruby>って<ruby>食<rt>た</rt></ruby>べます♪",
                    "text_en": "Events: (7) World cooking class: Several times a year (cook and eat food from various countries together)."
                },
                {
                    "id": 7,
                    "text_ja": "☆料金（「文化カフェ」の会員は500円割引） 語学クラス 1回 2,000円、日本文化クラス 1回 1,500円",
                    "ruby_html": "☆<ruby>料金<rt>りょうきん</rt></ruby>（「<ruby>文化<rt>ぶんか</rt></ruby>カフェ」の<ruby>会員<rt>かいいん</rt></ruby>は500<ruby>円割引<rt>えんわりびき</rt></ruby>） <ruby>語学<rt>ごがく</rt></ruby>クラス 1<ruby>回<rt>かい</rt></ruby> 2,000<ruby>円<rt>えん</rt></ruby>、<ruby>日本文化<rt>にほんぶんか</rt></ruby>クラス 1<ruby>回<rt>かい</rt></ruby> 1,500<ruby>円<rt>えん</rt></ruby>",
                    "text_en": "Fee (Culture Cafe members get a 500 yen discount): Language classes: 2,000 yen/session; Japanese culture classes: 1,500 yen/session."
                },
                {
                    "id": 8,
                    "text_ja": "☆定員8名（先着順） ☆申し込み 3日前までにネットで予約 →info@bunkacafe.com ☆場所 みなと市民会館（みなと駅徒歩4分）",
                    "ruby_html": "☆<ruby>定員<rt>ていいん</rt></ruby>8<ruby>名<rt>めい</rt></ruby>（<ruby>先着順<rt>せんちゃくじゅん</rt></ruby>） ☆<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>み 3<ruby>日前<rt>にちまえ</rt></ruby>までにネットで<ruby>予約<rt>よやく</rt></ruby> →info@bunkacafe.com ☆<ruby>場所<rt>ばしょ</rt></ruby> みなと<ruby>市民会館<rt>しみんかいかん</rt></ruby>（みなと<ruby>駅徒歩<rt>えきとほ</rt></ruby>4<ruby>分<rt>ふん</rt></ruby>）",
                    "text_en": "Capacity: 8 participants (first-come basis); Registration: Reserve online at least 3 days in advance (info@bunkacafe.com); Venue: Minato Community Center (4 min walk from Minato Station)."
                }
            ]
        },
        "footnotes": [],
        "vocabulary": [
            {
                "term": "語学",
                "reading": "ごがく",
                "meaning": "study of languages / 外语（学习）",
                "type": "noun"
            },
            {
                "term": "情報",
                "reading": "じょうほう",
                "meaning": "information / 信息",
                "type": "noun"
            },
            {
                "term": "交換する",
                "reading": "こうかんする",
                "meaning": "to exchange / 交换",
                "type": "verb"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-55-1",
                "questionNumber": 1,
                "questionText_ja": "右の文章の中の「⑤京都クラス」のクラスに、「文化カフェ」の会員が参加する場合、1回の料金はいくらか。",
                "questionText_en": "When a member of 'Culture Cafe' attends '(5) Kyoto Class' in the text, how much is the fee per session?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "500円",
                        "text_en": "500 yen"
                    },
                    {
                        "id": 2,
                        "text_ja": "1,000円",
                        "text_en": "1,000 yen"
                    },
                    {
                        "id": 3,
                        "text_ja": "1,500円",
                        "text_en": "1,500 yen"
                    },
                    {
                        "id": 4,
                        "text_ja": "2,000円",
                        "text_en": "2,000 yen"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "「⑤京都クラス」は「日本文化クラス」に属します。日本文化クラスの通常料金は「1回 1,500円」です。「文化カフェ」の会員は「500円割引」となるため、1,500円 － 500円 ＝ 1,000円 となります。したがって 2 が正解です。",
                "explanation_en": "'(5) Kyoto Class' belongs to the 'Japanese Culture Classes' category. The regular fee for Japanese culture classes is 1,500 yen per session. Since Culture Cafe members receive a 500-yen discount, the fee is 1,500 - 500 = 1,000 yen. Therefore, Option 2 is correct."
            },
            {
                "questionId": "q-55-2",
                "questionNumber": 2,
                "questionText_ja": "リーさんは4月9日(水)のアラビア語クラスに参加したい。何をすればよいか。",
                "questionText_en": "Lee wants to attend the Arabic class on Wednesday, April 9. What should he do?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "4月6日までに、電話して予約する。",
                        "text_en": "Call to make a reservation by April 6."
                    },
                    {
                        "id": 2,
                        "text_ja": "4月6日までに、ネットで予約する。",
                        "text_en": "Reserve online by April 6."
                    },
                    {
                        "id": 3,
                        "text_ja": "4月8日までに、みなと市民会館に行って予約する。",
                        "text_en": "Go to Minato Community Center to reserve by April 8."
                    },
                    {
                        "id": 4,
                        "text_ja": "4月9日に、教室に行って申し込む。",
                        "text_en": "Go to the classroom on April 9 to apply."
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "申し込み規定には「3日前までにネットで予約（→info@bunkacafe.com）」と明記されています。4月9日の3日前は4月6日です。予約手段は「ネットで予約」なので、選択肢2「4月6日までに、ネットで予約する」が正解です。",
                "explanation_en": "The registration guidelines state: 'Reserve online at least 3 days in advance (info@bunkacafe.com)'. Three days prior to April 9 is April 6, and the registration channel is via the internet. Therefore, Option 2 ('Reserve online by April 6') is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆パンフレット（文化カフェ講座案内）",
            "text_ja": "案内パンフレットの読解では、対象講座がどのカテゴリ（語学か日本文化か）に分類されるかを特定した上で、会員割引条件を適用します。また、締切計算（〜日前）と受付方法（ネットか電話か窓口か）の組み合わせを正確に見極めましょう。",
            "text_en": "When reading course guide pamphlets, locate the class under the correct category (Language vs. Japanese Culture) before applying member discounts. Furthermore, match deadline calculation ('3 days before') with the correct booking channel (online vs. phone).",
            "structureLayout": [
                {
                    "component": "講座分類",
                    "detail": "語学クラス（1回2,000円）／日本文化クラス（1回1,500円）",
                    "en": "Categories: Language classes (2,000 yen) / Japanese Culture (1,500 yen)."
                },
                {
                    "component": "会員特典",
                    "detail": "文化カフェ会員は各クラス500円割引",
                    "en": "Member perk: 500 yen discount for members."
                },
                {
                    "component": "予約条件",
                    "detail": "3日前までにメール/ネット予約、定員8名先着順",
                    "en": "Booking: Online reserve >=3 days ahead, 8 people first-come basis."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "「3日前までに」の日付計算と「ネット予約」という指定手段をセットで確認しましょう。",
            "point_en": "Calculate '3 days prior' correctly and verify the mandated booking method (online)."
        }
    },
    {
        "id": "dokkai-n3-p4-56",
        "pages": [128, 129],
        "problemNumber": 56,
        "genre": "パンフレット",
        "genre_en": "Pamphlet",
        "genre_zh": "宣传册",
        "title_ja": "問題56 パンフレット（ひがし町 レストラン案内）",
        "title_en": "Problem 56: Pamphlet (Higashimachi Restaurant Guide)",
        "title_zh": "问题56 宣传册（东町 餐厅指南）",
        "preReading": {
            "question_ja": "外食するとき、予算や営業時間、定休日はどのように調べますか。",
            "question_en": "How do you check budget, business hours, and regular holidays when dining out?",
            "question_zh": "外出就餐时，你通常如何查看预算、营业时间和休息日？"
        },
        "passageInstructions": {
            "instruction_ja": "右のページはレストランの案内である。これを読んで、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The right page is a restaurant guide. Read it and answer the questions below. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "ひがし町 レストラン案内",
                    "ruby_html": "ひがし<ruby>町<rt>ちょう</rt></ruby> レストラン<ruby>案内<rt>あんない</rt></ruby>",
                    "text_en": "Higashimachi Restaurant Guide"
                },
                {
                    "id": 2,
                    "text_ja": "①オリーブの風：南ヨーロッパのさまざまな国の料理が楽しめる。パーティーにもよい。[昼]800〜1,500円 [夜]2,000〜5,000円。時間：11:00〜14:00 18:00〜24:00。休み：木。",
                    "ruby_html": "①オリーブの<ruby>風<rt>かぜ</rt></ruby>：<ruby>南<rt>みなみ</rt></ruby>ヨーロッパのさまざまな<ruby>国<rt>くに</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>が<ruby>楽<rt>たの</rt></ruby>しめる。<ruby>パーティー<rt></rt></ruby>にもよい。[<ruby>昼<rt>ひる</rt></ruby>]800〜1,500<ruby>円<rt>えん</rt></ruby> [<ruby>夜<rt>よる</rt></ruby>]2,000〜5,000<ruby>円<rt>えん</rt></ruby>。<ruby>時間<rt>じかん</rt></ruby>：11:00〜14:00 18:00〜24:00。<ruby>休<rt>やす</rt></ruby>み：<ruby>木<rt>もく</rt></ruby>。",
                    "text_en": "(1) Olive Breeze: Enjoy dishes from various Southern European countries. Great for parties. [Lunch] 800-1,500 yen [Dinner] 2,000-5,000 yen. Hours: 11:00-14:00, 18:00-24:00. Closed: Thursday."
                },
                {
                    "id": 3,
                    "text_ja": "②山海：新鮮な魚と野菜を使った日本のふるさとの味。さしみが最高。[昼]950〜1,500円 [夜]3,500〜8,000円。時間：11:30〜14:30 18:00〜22:00。休み：火。",
                    "ruby_html": "②<ruby>山海<rt>さんかい</rt></ruby>：<ruby>新鮮<rt>しんせん</rt></ruby>な<ruby>魚<rt>さかな</rt></ruby>と<ruby>野菜<rt>やさい</rt></ruby>を<ruby>使<rt>つか</rt></ruby>った<ruby>日本<rt>にほん</rt></ruby>のふるさとの<ruby>味<rt>あじ</rt></ruby>。さしみが<ruby>最高<rt>さいこう</rt></ruby>。[<ruby>昼<rt>ひる</rt></ruby>]950〜1,500<ruby>円<rt>えん</rt></ruby> [<ruby>夜<rt>よる</rt></ruby>]3,500〜8,000<ruby>円<rt>えん</rt></ruby>。<ruby>時間<rt>じかん</rt></ruby>：11:30〜14:30 18:00〜22:00。<ruby>休<rt>やす</rt></ruby>み：<ruby>火<rt>か</rt></ruby>。",
                    "text_en": "(2) Sankai: Traditional Japanese hometown flavors using fresh fish and vegetables. Sashimi is top-notch! [Lunch] 950-1,500 yen [Dinner] 3,500-8,000 yen. Hours: 11:30-14:30, 18:00-22:00. Closed: Tuesday."
                },
                {
                    "id": 4,
                    "text_ja": "③よねやま：てんぷら、すしなど日本料理のメニューが豊富。個室あり。[昼]1,000〜2,300円 [夜]3,800〜8,800円。時間：12:00〜14:00 17:30〜21:30。年中無休。",
                    "ruby_html": "③よねやま：てんぷら、すしなど<ruby>日本料理<rt>にほんりょうり</rt></ruby>のメニューが<ruby>豊富<rt>ほうふ</rt></ruby>。<ruby>個室<rt>こしつ</rt></ruby>あり。[<ruby>昼<rt>ひる</rt></ruby>]1,000〜2,300<ruby>円<rt>えん</rt></ruby> [<ruby>夜<rt>よる</rt></ruby>]3,800〜8,800<ruby>円<rt>えん</rt></ruby>。<ruby>時間<rt>じかん</rt></ruby>：12:00〜14:00 17:30〜21:30。<ruby>年中無休<rt>ねんじゅうむきゅう</rt></ruby>。",
                    "text_en": "(3) Yoneyama: Abundant Japanese menu including tempura and sushi. Private dining rooms available. [Lunch] 1,000-2,300 yen [Dinner] 3,800-8,800 yen. Hours: 12:00-14:00, 17:30-21:30. Open year-round."
                },
                {
                    "id": 5,
                    "text_ja": "④李安：カニ料理が有名な中華料理店。食べ放題メニューもあり。[昼]1,000〜1,800円 [夜]2,500〜12,000円。時間：11:00〜14:00 17:00〜23:00。休み：火。個室あり。",
                    "ruby_html": "④<ruby>李安<rt>りあん</rt></ruby>：カニ<ruby>料理<rt>りょうり</rt></ruby>が<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>中華料理店<rt>ちゅうかりょうりてん</rt></ruby>。<ruby>食<rt>た</rt></ruby>べ<ruby>放題<rt>ほうだい</rt></ruby>メニューもあり。[<ruby>昼<rt>ひる</rt></ruby>]1,000〜1,800<ruby>円<rt>えん</rt></ruby> [<ruby>夜<rt>よる</rt></ruby>]2,500〜12,000<ruby>円<rt>えん</rt></ruby>。<ruby>時間<rt>じかん</rt></ruby>：11:00〜14:00 17:00〜23:00。<ruby>休<rt>やす</rt></ruby>み：<ruby>火<rt>か</rt></ruby>。<ruby>個室<rt>こしつ</rt></ruby>あり。",
                    "text_en": "(4) Li An: Chinese restaurant famous for crab dishes. All-you-can-eat options available. [Lunch] 1,000-1,800 yen [Dinner] 2,500-12,000 yen. Hours: 11:00-14:00, 17:00-23:00. Closed: Tuesday. Private dining rooms available."
                }
            ]
        },
        "footnotes": [],
        "vocabulary": [
            {
                "term": "ふるさと",
                "reading": "ふるさと",
                "meaning": "hometown, native place / 故乡",
                "type": "noun"
            },
            {
                "term": "さしみ",
                "reading": "さしみ",
                "meaning": "raw fish, sashimi / 生鱼片",
                "type": "noun"
            },
            {
                "term": "豊富",
                "reading": "ほうふ",
                "meaning": "very varied, rich, abundant / 丰富",
                "type": "na-adjective"
            },
            {
                "term": "個室",
                "reading": "こしつ",
                "meaning": "single private room / 包间",
                "type": "noun"
            },
            {
                "term": "食べ放題",
                "reading": "たべほうだい",
                "meaning": "all-you-can-eat meal / 自助餐",
                "type": "noun"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-56-1",
                "questionNumber": 1,
                "questionText_ja": "チョウさんは、友達と夕食が食べられる店を探している。予算は3,000円以内で、時間は来週の火曜日の19時からである。どの店がよいか。",
                "questionText_en": "Cho is looking for a restaurant to eat dinner with friends. The budget is within 3,000 yen, and the time is next Tuesday starting at 19:00. Which restaurant is best?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "①",
                        "text_en": "(1) Olive Breeze"
                    },
                    {
                        "id": 2,
                        "text_ja": "②",
                        "text_en": "(2) Sankai"
                    },
                    {
                        "id": 3,
                        "text_ja": "③",
                        "text_en": "(3) Yoneyama"
                    },
                    {
                        "id": 4,
                        "text_ja": "④",
                        "text_en": "(4) Li An"
                    }
                ],
                "correctAnswer": 1,
                "explanation_ja": "条件は「火曜日の19時（夜）」「予算3,000円以内」です。\n①オリーブの風：木曜定休（火曜は営業）、夜18:00〜24:00（19時OK）、夜の予算2,000〜5,000円（3,000円以内で可能）。条件を満たします。\n②山海：火曜日が定休日です。\n③よねやま：夜の予算が3,800〜8,800円で、3,000円を超えています。\n④李安：火曜日が定休日です。\nしたがって、すべての条件を満たす店は ① です。",
                "explanation_en": "The conditions are: 'Tuesday at 19:00 (dinner)' and 'budget within 3,000 yen'.\n(1) Olive Breeze: Closed Thursday (open Tuesday), evening hours 18:00-24:00 (open at 19:00), dinner budget starts at 2,000 yen (fits <= 3,000 yen). Matches!\n(2) Sankai: Closed on Tuesdays.\n(3) Yoneyama: Dinner starts at 3,800 yen (exceeds 3,000 yen budget).\n(4) Li An: Closed on Tuesdays.\nTherefore, the only suitable restaurant is Option 1."
            },
            {
                "questionId": "q-56-2",
                "questionNumber": 2,
                "questionText_ja": "サムさんは、木曜日の昼のできるだけ早い時間に友達と和食が食べたい。何時から食べることができるか。",
                "questionText_en": "Sam wants to eat Japanese food with a friend on Thursday as early as possible for lunch. From what time can they eat?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "11時",
                        "text_en": "11:00"
                    },
                    {
                        "id": 2,
                        "text_ja": "11時30分",
                        "text_en": "11:30"
                    },
                    {
                        "id": 3,
                        "text_ja": "12時",
                        "text_en": "12:00"
                    },
                    {
                        "id": 4,
                        "text_ja": "12時30分",
                        "text_en": "12:30"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "木曜日の昼に和食（日本料理）が食べられる店を探します。\n和食を扱うのは ②山海（日本のふるさとの味、さしみ）と ③よねやま（日本料理）です。\n②山海：木曜営業（火曜定休）、昼の営業時間は 11:30〜14:30。\n③よねやま：年中無休、昼の営業時間は 12:00〜14:00。\nできるだけ早い時間は、11時30分です。したがって 2 が正解です。",
                "explanation_en": "We need Japanese food (和食) for lunch on Thursday at the earliest possible time.\nRestaurants serving Japanese cuisine are:\n(2) Sankai (traditional Japanese flavors, sashimi): Open on Thursday (closed Tuesday); lunch hours begin at 11:30.\n(3) Yoneyama (Japanese cuisine): Open Thursday; lunch hours begin at 12:00.\nThe earliest time is 11:30 (at Sankai). Therefore, Option 2 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆パンフレット（ひがし町 レストラン案内）",
            "text_ja": "複数の飲食店比較テーブルでは、曜日（定休日チェック）、時間帯（昼夜の営業時間区分）、料理ジャンル（和食・洋食・中華）、予算の4軸を素早く消去法で絞り込みます。",
            "text_en": "In comparative restaurant guides, filter candidates systematically using a four-axis elimination process: day of the week (holidays), time frame (lunch vs dinner hours), cuisine genre (Japanese, European, Chinese), and price range.",
            "structureLayout": [
                {
                    "component": "①オリーブの風",
                    "detail": "南欧料理、昼800〜1,500円、夜2,000〜5,000円、木曜休",
                    "en": "Olive Breeze: S. European, lunch 800-1.5k, dinner 2k-5k, closed Thu."
                },
                {
                    "component": "②山海",
                    "detail": "和食（さしみ）、昼950〜1,500円（11:30〜）、火曜休",
                    "en": "Sankai: Japanese, lunch 950-1.5k (from 11:30), closed Tue."
                },
                {
                    "component": "③よねやま",
                    "detail": "日本料理、昼1,000〜2,300円（12:00〜）、年中無休",
                    "en": "Yoneyama: Japanese, lunch 1k-2.3k (from 12:00), open year-round."
                },
                {
                    "component": "④李安",
                    "detail": "中華料理、火曜休",
                    "en": "Li An: Chinese, closed Tue."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "定休日を最初にチェックすると候補を劇的に減らすことができます。",
            "point_en": "Filtering by closing day first dramatically eliminates non-viable options quickly."
        }
    },
    {
        "id": "dokkai-n3-p4-57",
        "pages": [130, 131],
        "problemNumber": 57,
        "genre": "メニュー",
        "genre_en": "Delivery Menu",
        "genre_zh": "外卖菜单",
        "title_ja": "問題57 メニュー（レストランさくら 宅配メニュー）",
        "title_en": "Problem 57: Delivery Menu (Restaurant Sakura Delivery Menu)",
        "title_zh": "问题57 菜单（樱花餐厅 外卖菜单）",
        "preReading": {
            "question_ja": "デリバリーやお弁当の宅配を頼むとき、配達料や受付時間に注意したことがありますか。",
            "question_en": "Have you ever paid attention to delivery fees and order cutoff times when ordering food delivery?",
            "question_zh": "点外卖或便当送餐时，你注意过配送费和接单时间吗？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章は宅配用のメニューである。右の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The following text is a delivery menu. Answer the questions on the right. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "レストラン さくら 宅配メニュー 年中無休",
                    "ruby_html": "レストラン さくら <ruby>宅配<rt>たくはい</rt></ruby>メニュー <ruby>年中無休<rt>ねんじゅうむきゅう</rt></ruby>",
                    "text_en": "Restaurant Sakura Delivery Menu - Open 365 days a year"
                },
                {
                    "id": 2,
                    "text_ja": "日替わり弁当（全て600円、みそ汁付）：月：ハンバーグ弁当、火：とんかつ弁当、水：からあげ弁当、木：コロッケ弁当、金：焼肉弁当。",
                    "ruby_html": "<ruby>日替<rt>ひが</rt></ruby>わり<ruby>弁当<rt>べんとう</rt></ruby>（<ruby>全<rt>すべ</rt></ruby>て600<ruby>円<rt>えん</rt></ruby>、みそ<ruby>汁付<rt>しるつ</rt></ruby>き）：<ruby>月<rt>げつ</rt></ruby>：ハンバーグ<ruby>弁当<rt>べんとう</rt></ruby>、<ruby>火<rt>か</rt></ruby>：とんかつ<ruby>弁当<rt>べんとう</rt></ruby>、<ruby>水<rt>すい</rt></ruby>：からあげ<ruby>弁当<rt>べんとう</rt></ruby>、<ruby>木<rt>もく</rt></ruby>：コロッケ<ruby>弁当<rt>べんとう</rt></ruby>、<ruby>金<rt>きん</rt></ruby>：<ruby>焼肉弁当<rt>やきにくべんとう</rt></ruby>。",
                    "text_en": "Daily special bento (all 600 yen, includes miso soup): Mon: Hamburg bento; Tue: Tonkatsu bento; Wed: Fried chicken bento; Thu: Croquette bento; Fri: Yakiniku bento."
                },
                {
                    "id": 3,
                    "text_ja": "ごはん：カレーライス 550円、オムライス 600円、親子丼 720円、かつ丼 800円。",
                    "ruby_html": "ごはん：カレーライス 550<ruby>円<rt>えん</rt></ruby>、オムライス 600<ruby>円<rt>えん</rt></ruby>、<ruby>親子丼<rt>おやこどん</rt></ruby> 720<ruby>円<rt>えん</rt></ruby>、かつ<ruby>丼<rt>どん</rt></ruby> 800<ruby>円<rt>えん</rt></ruby>。",
                    "text_en": "Rice meals: Curry and rice 550 yen; Omelet rice 600 yen; Oyako-don 720 yen; Katsu-don 800 yen."
                },
                {
                    "id": 4,
                    "text_ja": "サラダ：コーンサラダ 200円、ポテトサラダ 230円。",
                    "ruby_html": "サラダ：コーンサラダ 200<ruby>円<rt>えん</rt></ruby>、ポテトサラダ 230<ruby>円<rt>えん</rt></ruby>。",
                    "text_en": "Salads: Corn salad 200 yen; Potato salad 230 yen."
                },
                {
                    "id": 5,
                    "text_ja": "飲み物：コーラ 150円、オレンジジュース 150円、緑茶 120円。★お食事と一緒のご注文の場合、お飲み物は100円！",
                    "ruby_html": "<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>：コーラ 150<ruby>円<rt>えん</rt></ruby>、オレンジジュース 150<ruby>円<rt>えん</rt></ruby>、<ruby>緑茶<rt>りょくちゃ</rt></ruby> 120<ruby>円<rt>えん</rt></ruby>。★お<ruby>食事<rt>しょくじ</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>のご<ruby>注文<rt>ちゅうもん</rt></ruby>の<ruby>場合<rt>ばあい</rt></ruby>、お<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>は100<ruby>円<rt>えん</rt></ruby>！",
                    "text_en": "Drinks: Cola 150 yen; Orange juice 150 yen; Green tea 120 yen. ★When ordered together with a meal, drinks are 100 yen!"
                },
                {
                    "id": 6,
                    "text_ja": "TEL: 5555-8888 受付時間：9:00〜20:30（土日祝は19:30で終了）。",
                    "ruby_html": "TEL: 5555-8888 <ruby>受付時間<rt>うけつけじかん</rt></ruby>：9:00〜20:30（<ruby>土日祝<rt>どにちしゅく</rt></ruby>は19:30で<ruby>終了<rt>しゅうりょう</rt></ruby>）。",
                    "text_en": "TEL: 5555-8888 Order reception: 9:00-20:30 (ends at 19:30 on weekends and holidays)."
                },
                {
                    "id": 7,
                    "text_ja": "配達時間：10:30〜21:00 (14:00〜17:00を除く) 土日祝は20:00で終了。",
                    "ruby_html": "<ruby>配達時間<rt>はいたつじかん</rt></ruby>：10:30〜21:00 (14:00〜17:00を<ruby>除<rt>のぞ</rt></ruby>く) <ruby>土日祝<rt>どにちしゅく</rt></ruby>は20:00で<ruby>終了<rt>しゅうりょう</rt></ruby>。",
                    "text_en": "Delivery hours: 10:30-21:00 (excluding 14:00-17:00); ends at 20:00 on weekends and holidays."
                },
                {
                    "id": 8,
                    "text_ja": "＊お食事お一つでも注文できます！ 1,000円未満のご注文は、1回のお届けにつき、200円いただきます。",
                    "ruby_html": "＊お<ruby>食事<rt>しょくじ</rt></ruby>お<ruby>一<rt>ひと</rt></ruby>つでも<ruby>注文<rt>ちゅうもん</rt></ruby>できます！ 1,000<ruby>円未満<rt>えんみまん</rt></ruby>のご<ruby>注文<rt>ちゅうもん</rt></ruby>は、1<ruby>回<rt>かい</rt></ruby>のお<ruby>届<rt>とど</rt></ruby>けにつき、200<ruby>円<rt>えん</rt></ruby>いただきます。",
                    "text_en": "* You can order even just a single meal! For orders under 1,000 yen, a 200 yen delivery charge applies per delivery."
                },
                {
                    "id": 9,
                    "text_ja": "＊10個以上の注文は前の日までにご注文ください。 ＊インターネットでも注文できます。 http://www.aaa.ccc",
                    "ruby_html": "＊10<ruby>個以上<rt>こいじょう</rt></ruby>の<ruby>注文<rt>ちゅうもん</rt></ruby>は<ruby>前<rt>まえ</rt></ruby>の<ruby>日<rt>ひ</rt></ruby>までにご<ruby>注文<rt>ちゅうもん</rt></ruby>ください。 ＊インターネットでも<ruby>注文<rt>ちゅうもん</rt></ruby>できます。 http://www.aaa.ccc",
                    "text_en": "* Orders of 10 items or more must be placed by the day before. * Online ordering is also available at http://www.aaa.ccc."
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "宅配",
                "meaning_ja": "商品を家に配達すること",
                "meaning_en": "home delivery of goods"
            }
        ],
        "vocabulary": [
            {
                "term": "年中無休",
                "reading": "ねんじゅうむきゅう",
                "meaning": "[open] all-year-round / 全年不休",
                "type": "noun"
            },
            {
                "term": "日替わり",
                "reading": "ひがわり",
                "meaning": "daily special / 每日推荐",
                "type": "noun"
            },
            {
                "term": "〜付",
                "reading": "〜つき",
                "meaning": "with, accompanied by ~ / 附送〜",
                "type": "suffix"
            },
            {
                "term": "注文",
                "reading": "ちゅうもん",
                "meaning": "order / 订购",
                "type": "noun"
            },
            {
                "term": "受付",
                "reading": "うけつけ",
                "meaning": "order reception / 受理",
                "type": "noun"
            },
            {
                "term": "配達",
                "reading": "はいたつ",
                "meaning": "delivery / 配送",
                "type": "noun"
            },
            {
                "term": "〜未満",
                "reading": "〜みまん",
                "meaning": "less than ~ / 不到〜",
                "type": "suffix"
            },
            {
                "term": "〜以上",
                "reading": "〜いじょう",
                "meaning": "~ and above, or more / 等于或超过〜",
                "type": "suffix"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-57-1",
                "questionNumber": 1,
                "questionText_ja": "シンさんはカレーライスとコーラを宅配で注文した。全部でいくら払わなければならないか。",
                "questionText_en": "Shin ordered curry rice and cola for delivery. How much does he have to pay in total?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "550円＋100円＝650円",
                        "text_en": "550 yen + 100 yen = 650 yen"
                    },
                    {
                        "id": 2,
                        "text_ja": "550円＋150円＝700円",
                        "text_en": "550 yen + 150 yen = 700 yen"
                    },
                    {
                        "id": 3,
                        "text_ja": "550円＋100円＋200円＝850円",
                        "text_en": "550 yen + 100 yen + 200 yen = 850 yen"
                    },
                    {
                        "id": 4,
                        "text_ja": "550円＋150円＋200円＝900円",
                        "text_en": "550 yen + 150 yen + 200 yen = 900 yen"
                    }
                ],
                "correctAnswer": 3,
                "explanation_ja": "カレーライスの価格は550円です。食事と一緒に飲み物を注文すると100円になるため、コーラは100円です。料理の合計は 550円 ＋ 100円 ＝ 650円 となります。これは「1,000円未満のご注文」に該当するため、配達料として別途200円がかかります。合計は 550円 ＋ 100円 ＋ 200円 ＝ 850円 です。したがって 3 が正解です。",
                "explanation_en": "Curry rice costs 550 yen. When ordered together with a meal, drinks cost 100 yen, so cola is 100 yen. Food total is 550 + 100 = 650 yen. Because 650 yen is under 1,000 yen ('1,000円未満'), a 200-yen delivery fee is added. Total payment is 550 + 100 + 200 = 850 yen. Therefore, Option 3 is correct."
            },
            {
                "questionId": "q-57-2",
                "questionNumber": 2,
                "questionText_ja": "ホルへさんは4月13日(日)の昼12時半にお弁当が20個必要である。いつ注文すればよいか。",
                "questionText_en": "Jorge needs 20 bentos at 12:30 PM on Sunday, April 13. When should he place the order?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "4月11日(金)の午後9時ごろ",
                        "text_en": "Around 9:00 PM on Friday, April 11"
                    },
                    {
                        "id": 2,
                        "text_ja": "4月12日(土)の午後6時ごろ",
                        "text_en": "Around 6:00 PM on Saturday, April 12"
                    },
                    {
                        "id": 3,
                        "text_ja": "4月12日(土)の午後8時ごろ",
                        "text_en": "Around 8:00 PM on Saturday, April 12"
                    },
                    {
                        "id": 4,
                        "text_ja": "4月13日(日)の午前9時ごろ",
                        "text_en": "Around 9:00 AM on Sunday, April 13"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "20個の注文は「10個以上の注文は前の日までにご注文ください」に該当するため、4月13日の前日である4月12日(土)までに注文する必要があります。また、受付時間は平日は20:30までですが、「土日祝は19:30で終了」となっています。\n1: 金曜の午後9時は平日の受付時間（20:30まで）を過ぎています。\n2: 4月12日(土)の午後6時は、前日かつ土曜受付時間（19:30まで）内なので注文可能です。\n3: 4月12日(土)の午後8時は、土曜の受付時間（19:30まで）を過ぎています。\n4: 当日の注文は10個以上ルールに違反します。\nしたがって 2 が正解です。",
                "explanation_en": "An order of 20 bentos triggers the rule 'Orders of 10 items or more must be placed by the day before', requiring order placement by Saturday, April 12. In addition, reception hours on weekends and holidays end at 19:30 (土日祝は19:30で終了).\nOption 1: Friday 21:00 is past the weekday 20:30 cutoff.\nOption 2: Saturday 18:00 is before the Saturday 19:30 cutoff on the day before. Valid!\nOption 3: Saturday 20:00 is past the Saturday 19:30 cutoff.\nOption 4: Sunday same-day ordering violates the day-before rule for >=10 items.\nTherefore, Option 2 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆メニュー（レストランさくら 宅配メニュー）",
            "text_ja": "宅配メニューでは、セット割引（セットドリンク100円）＋追加配達料（1,000円未満は＋200円）の二重条件計算、および大量注文時（10個以上は前日締切）と曜日別営業時間（土日祝は19:30受付終了）の複合条件判定がポイントです。",
            "text_en": "In delivery menus, look for stacked pricing rules (meal combo drink discount + minimum delivery surcharge) and compound reservation conditions (large orders >=10 by the prior day combined with weekend earlier cutoff times).",
            "structureLayout": [
                {
                    "component": "価格・割引",
                    "detail": "食事と一緒ならドリンク100円、1,000円未満は送料200円",
                    "en": "Pricing: Combo drinks 100 yen, delivery fee 200 yen for orders <1,000 yen."
                },
                {
                    "component": "受付時間",
                    "detail": "平日9:00〜20:30、土日祝は19:30終了",
                    "en": "Order reception: Weekdays until 20:30, weekends/holidays until 19:30."
                },
                {
                    "component": "大量注文規定",
                    "detail": "10個以上は前日までに注文必須",
                    "en": "Large orders: 10 items or more require booking by previous day."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "曜日によって受付終了時間が異なる点（平日は20:30、土日祝は19:30）を絶対に見落とさないこと！",
            "point_en": "Never overlook divergent cutoff times by day of the week (20:30 on weekdays vs 19:30 on weekends/holidays)!"
        }
    }
]
