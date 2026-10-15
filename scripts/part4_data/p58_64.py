# -*- coding: utf-8 -*-
"""
Part 4 Information Retrieval (情報検索): Problems 58 to 64
Pages 132 - 145
"""

lessons = [
    {
        "id": "dokkai-n3-p4-58",
        "pages": [132, 133],
        "problemNumber": 58,
        "genre": "請求書",
        "genre_en": "Bill / Invoice",
        "genre_zh": "账单",
        "title_ja": "問題58 請求書（NAT携帯電話料金請求書）",
        "title_en": "Problem 58: Bill (NAT Mobile Phone Bill)",
        "title_zh": "问题58 账单（NAT手机话费账单）",
        "preReading": {
            "question_ja": "毎月の公共料金や携帯代の請求書はどうやって支払っていますか。",
            "question_en": "How do you pay your monthly utility and mobile phone bills?",
            "question_zh": "你通常如何缴纳每月的公共事业费和手机话费账单？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "Read the following text and answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "NAT携帯電話料金請求書 東京都○○市××町3-5-2 カン ヘミ様",
                    "ruby_html": "NAT<ruby>携帯電話料金請求書<rt>けいたいでんわりょうきんせいきゅうしょ</rt></ruby> <ruby>東京都<rt>とうきょうと</rt></ruby>○○<ruby>市<rt>し</rt></ruby>××<ruby>町<rt>ちょう</rt></ruby>3-5-2 カン ヘミ<ruby>様<rt>さま</rt></ruby>",
                    "text_en": "NAT Mobile Phone Bill - To: Ms./Mr. Kang Hemi, 3-5-2 xx-cho, oo-city, Tokyo"
                },
                {
                    "id": 2,
                    "text_ja": "ご利用期間：2014年5月1日〜5月31日、ご請求額：7,800円、お支払い期限：2014年6月30日(月)。",
                    "ruby_html": "ご<ruby>利用期間<rt>りようきかん</rt></ruby>：2014<ruby>年<rt>ねん</rt></ruby>5<ruby>月<rt>がつ</rt></ruby>1<ruby>日<rt>にち</rt></ruby>〜5<ruby>月<rt>がつ</rt></ruby>31<ruby>日<rt>にち</rt></ruby>、ご<ruby>請求額<rt>せいきゅうがく</rt></ruby>：7,800<ruby>円<rt>えん</rt></ruby>、お<ruby>支払<rt>しはら</rt></ruby>い<ruby>期限<rt>きげん</rt></ruby>：2014<ruby>年<rt>ねん</rt></ruby>6<ruby>月<rt>がつ</rt></ruby>30<ruby>日<rt>にち</rt></ruby>(<ruby>月<rt>げつ</rt></ruby>)。",
                    "text_en": "Billing period: May 1, 2014 - May 31; Invoiced amount: 7,800 yen; Payment due date: Monday, June 30, 2014."
                },
                {
                    "id": 3,
                    "text_ja": "お問い合わせ先：NAT 0800-222-3333 月〜日(年中無休) 9:00-20:00、発行日：2014年6月3日。",
                    "ruby_html": "お<ruby>問<rt>と</rt></ruby>い<ruby>合<rt>あ</rt></ruby>わせ<ruby>先<rt>さき</rt></ruby>：NAT 0800-222-3333 <ruby>月<rt>げつ</rt></ruby>〜<ruby>日<rt>にち</rt></ruby>(<ruby>年中無休<rt>ねんじゅうむきゅう</rt></ruby>) 9:00-20:00、<ruby>発行日<rt>はっこうび</rt></ruby>：2014<ruby>年<rt>ねん</rt></ruby>6<ruby>月<rt>がつ</rt></ruby>3<ruby>日<rt>にち</rt></ruby>。",
                    "text_en": "Contact inquiry: NAT 0800-222-3333 Mon-Sun (Open year-round) 9:00-20:00; Issue date: June 3, 2014."
                },
                {
                    "id": 4,
                    "text_ja": "お支払い方法のご案内：●現金でのお支払いの場合 「振込用紙」を切り取り、お近くのコンビニまたは銀行・郵便局でお支払いください。",
                    "ruby_html": "お<ruby>支払<rt>しはら</rt></ruby>い<ruby>方法<rt>ほうほう</rt></ruby>のご<ruby>案内<rt>あんない</rt></ruby>：●<ruby>現金<rt>げんきん</rt></ruby>でのお<ruby>支払<rt>しはら</rt></ruby>いの<ruby>場合<rt>ばあい</rt></ruby> 「<ruby>振込用紙<rt>ふりこみようし</rt></ruby>」を<ruby>切<rt>き</rt></ruby>り<ruby>取<rt>と</rt></ruby>り、お<ruby>近<rt>ちか</rt></ruby>くのコンビニまたは<ruby>銀行<rt>ぎんこう</rt></ruby>・<ruby>郵便局<rt>ゆうびんきょく</rt></ruby>でお<ruby>支払<rt>しはら</rt></ruby>いください。",
                    "text_en": "Payment methods guide: - Paying in cash: Detach the transfer payment slip and pay at a nearby convenience store, bank, or post office."
                },
                {
                    "id": 5,
                    "text_ja": "●クレジットカードでのお支払いの場合 NATのウェブサイトからお支払いください。",
                    "ruby_html": "●クレジットカードでのお<ruby>支払<rt>しはら</rt></ruby>いの<ruby>場合<rt>ばあい</rt></ruby> NATのウェブサイトからお<ruby>支払<rt>しはら</rt></ruby>いください。",
                    "text_en": "- Paying by credit card: Please pay via the NAT official website."
                },
                {
                    "id": 6,
                    "text_ja": "●銀行口座の振替手続きをすると、毎月26日に自動的にお振替になります。",
                    "ruby_html": "●<ruby>銀行口座<rt>ぎんこうこうざ</rt></ruby>の<ruby>振替<rt>ふりかえ</rt></ruby><ruby>手続<rt>てつづ</rt></ruby>きをすると、<ruby>毎月<rt>まいつき</rt></ruby>26<ruby>日<rt>にち</rt></ruby>に<ruby>自動的<rt>じどうてき</rt></ruby>にお<ruby>振替<rt>ふりかえ</rt></ruby>になります。",
                    "text_en": "- Automatic bank account transfer: Once transfer procedures are set up, deductions occur automatically on the 26th of each month."
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "切り取る",
                "meaning_ja": "切ってその部分を取る",
                "meaning_en": "to cut off, detach a coupon or slip"
            },
            {
                "label": "注2",
                "term": "振替",
                "meaning_ja": "口座から自動的にお金が支払われること",
                "meaning_en": "automatic account transfer/debit"
            }
        ],
        "vocabulary": [
            {
                "term": "携帯電話",
                "reading": "けいたいでんわ",
                "meaning": "cellphone, mobile phone / 手机",
                "type": "noun"
            },
            {
                "term": "請求額",
                "reading": "せいきゅうがく",
                "meaning": "invoiced amount / 支付金额",
                "type": "noun"
            },
            {
                "term": "支払い期限",
                "reading": "しはらいきげん",
                "meaning": "payment deadline / 支付截止日",
                "type": "noun"
            },
            {
                "term": "問い合わせ先",
                "reading": "といあわせさき",
                "meaning": "inquiries contact / 问讯处",
                "type": "noun"
            },
            {
                "term": "年中無休",
                "reading": "ねんじゅうむきゅう",
                "meaning": "open all year round / 全年不休",
                "type": "noun"
            },
            {
                "term": "発行",
                "reading": "はっこう",
                "meaning": "to issue / 发行",
                "type": "noun"
            },
            {
                "term": "現金",
                "reading": "げんきん",
                "meaning": "cash / 现金",
                "type": "noun"
            },
            {
                "term": "振込用紙",
                "reading": "ふりこみようし",
                "meaning": "transfer payment slip / 汇款单",
                "type": "noun"
            },
            {
                "term": "ウェブサイト",
                "reading": "うぇぶさいと",
                "meaning": "website / 网站",
                "type": "noun"
            },
            {
                "term": "銀行口座",
                "reading": "ぎんこうこうざ",
                "meaning": "bank account / 银行账号",
                "type": "noun"
            },
            {
                "term": "自動的に",
                "reading": "じどうてきに",
                "meaning": "automatically / 自动地",
                "type": "adverb"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-58-1",
                "questionNumber": 1,
                "questionText_ja": "カンさんは何足をしなければならないか。（カンさんは銀行の口座を作ったが、郵便局の口座はない。まだクレジットカードも持っていない。）",
                "questionText_en": "What must Kang do? (Kang has opened a bank account, but does not have a post office account, nor does he possess a credit card yet.)",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "NATに電話をする。",
                        "text_en": "Call NAT."
                    },
                    {
                        "id": 2,
                        "text_ja": "郵便局に行って、口座を作る。",
                        "text_en": "Go to the post office and open an account."
                    },
                    {
                        "id": 3,
                        "text_ja": "コンビニに行って、クレジットカードで払う。",
                        "text_en": "Go to the convenience store and pay by credit card."
                    },
                    {
                        "id": 4,
                        "text_ja": "銀行かコンビニに行って、現金で払う。",
                        "text_en": "Go to a bank or convenience store and pay with cash."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "カンさんはクレジットカードを持っておらず、銀行口座の振替手続きもまだ済んでいません。そのため選べる方法は「現金でのお支払い」のみです。現金で支払う場合は「『振込用紙』を切り取り、お近くのコンビニまたは銀行・郵便局でお支払いください」とあるため、銀行かコンビニに行って現金で支払う必要があります。したがって 4 が正解です。",
                "explanation_en": "Kang has no credit card, and has not completed the automatic account transfer registration. Thus, his only available option is cash payment. The cash payment instructions state: 'detach the payment slip and pay at a nearby convenience store, bank, or post office.' Therefore, Option 4 ('Go to a bank or convenience store and pay with cash') is correct."
            },
            {
                "questionId": "q-58-2",
                "questionNumber": 2,
                "questionText_ja": "支払いはいつまでにしなければならないか。",
                "questionText_en": "By when must the payment be made?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "5月31日",
                        "text_en": "May 31"
                    },
                    {
                        "id": 2,
                        "text_ja": "6月3日",
                        "text_en": "June 3"
                    },
                    {
                        "id": 3,
                        "text_ja": "6月26日",
                        "text_en": "June 26"
                    },
                    {
                        "id": 4,
                        "text_ja": "6月30日",
                        "text_en": "June 30"
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "請求書の「お支払い期限」の欄に「2014年6月30日(月)」と明記されています。したがって 4 が正解です。（5月31日は利用期間の末日、6月3日は発行日、毎月26日は口座振替日です。）",
                "explanation_en": "The 'Payment due date' (お支払い期限) column explicitly specifies 'June 30, 2014 (Mon)'. Therefore, Option 4 is correct. (May 31 is billing period end, June 3 is issue date, and 26th is monthly auto-debit date.)"
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆請求書（NAT携帯電話料金請求書）",
            "text_ja": "請求書では、「利用期間」「発行日」「支払期限」「自動振替日」など複数の日付が登場します。質問が求めているのが「期日（デッドライン）」なのか「手段（支払い方法）」なのかを峻別し、人物の保有状況（クレカ有無、口座振替有無）に合わせて最適な選択肢を選びましょう。",
            "text_en": "In utility invoices, multiple dates appear (billing period, issue date, payment deadline, auto-debit date). Distinguish clearly between deadline vs payment channel, and match the character's available means (no credit card, no auto-debit set up).",
            "structureLayout": [
                {
                    "component": "基本請求情報",
                    "detail": "請求額7,800円、支払期限：2014年6月30日",
                    "en": "Invoice info: 7,800 yen, payment due June 30, 2014."
                },
                {
                    "component": "支払方法の区分",
                    "detail": "現金（コンビニ・銀行・郵便局）、クレカ（Web）、口座振替（26日引落）",
                    "en": "Payment channels: Cash (combini/bank/post), Credit card (Web), Auto-debit (26th)."
                },
                {
                    "component": "人物の現状",
                    "detail": "クレカなし、口座振替未設定→現金支払いを選択",
                    "en": "Character condition: No credit card, no auto-debit setup -> Choose cash."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "日付の混同に注意！「発行日」「振替日」「支払い期限」の区別を正確につけましょう。",
            "point_en": "Beware date confusions! Clearly distinguish issue date, monthly transfer date, and final payment deadline."
        }
    },
    {
        "id": "dokkai-n3-p4-59",
        "pages": [134, 135],
        "problemNumber": 59,
        "genre": "保証書",
        "genre_en": "Warranty Certificate",
        "genre_zh": "保修卡",
        "title_ja": "問題59 保証書（テニスラケット保証書）",
        "title_en": "Problem 59: Warranty Certificate (Tennis Racket Warranty)",
        "title_zh": "问题59 保修单（网球拍保修单）",
        "preReading": {
            "question_ja": "電化製品やスポーツ用品を買ったとき、保証書の期間や条件を確認しますか。",
            "question_en": "Do you check the warranty period and coverage conditions when purchasing electronics or sports goods?",
            "question_zh": "购买家电或体育用品时，你会查看保修期和保修条款吗？"
        },
        "passageInstructions": {
            "instruction_ja": "右のページの文章は保証書である。下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The text on the right page is a warranty certificate. Answer the questions below. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "メイさんはテニスのラケットを買いにお店に行った。買った時、お店の人から、ラケットと一緒に右の保証書をもらった。",
                    "ruby_html": "メイさんはテニスのラケットを<ruby>買<rt>か</rt></ruby>いにお<ruby>店<rt>みせ</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。<ruby>買<rt>か</rt></ruby>った<ruby>時<rt>とき</rt></ruby>、お<ruby>店<rt>みせ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>から、ラケットと<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>右<rt>みぎ</rt></ruby>の<ruby>保証書<rt>ほしょうしょ</rt></ruby>をもらった。",
                    "text_en": "May went to a shop to buy a tennis racket. When she bought it, the clerk gave her this warranty certificate along with the racket."
                },
                {
                    "id": 2,
                    "text_ja": "【保証書】ご購入日：2014年5月1日、メーカー：プレンセス、ラケット名：ショット35、カラー：青。",
                    "ruby_html": "【<ruby>保証書<rt>ほしょうしょ</rt></ruby>】ご<ruby>購入日<rt>こうにゅうび</rt></ruby>：2014<ruby>年<rt>ねん</rt></ruby>5<ruby>月<rt>がつ</rt></ruby>1<ruby>日<rt>にち</rt></ruby>、メーカー：プレンセス、ラケット<ruby>名<rt>めい</rt></ruby>：ショット35、カラー：<ruby>青<rt>あお</rt></ruby>。",
                    "text_en": "[Warranty] Purchase date: May 1, 2014; Manufacturer: Princess; Racket name: Shot 35; Color: Blue."
                },
                {
                    "id": 3,
                    "text_ja": "1. 普通の使用状態において破損などがあった場合は、お買い上げ日から下に書いてある期限（保証期間）の間、無料で修理または交換します。",
                    "ruby_html": "1. <ruby>普通<rt>ふつう</rt></ruby>の<ruby>使用状態<rt>しようじょうたい</rt></ruby>において<ruby>破損<rt>はそん</rt></ruby>などがあった<ruby>場合<rt>ばあい</rt></ruby>は、お<ruby>買<rt>か</rt></ruby>い<ruby>上<rt>あ</rt></ruby>げ<ruby>日<rt>ひ</rt></ruby>から<ruby>下<rt>した</rt></ruby>に<ruby>書<rt>か</rt></ruby>いてある<ruby>期限<rt>きげん</rt></ruby>（<ruby>保証期間<rt>ほしょうきかん</rt></ruby>）の<ruby>間<rt>あいだ</rt></ruby>、<ruby>無料<rt>むりょう</rt></ruby>で<ruby>修理<rt>しゅうり</rt></ruby>または<ruby>交換<rt>こうかん</rt></ruby>します。",
                    "text_en": "1. In case of damage occurring under normal conditions of use, free repair or replacement will be provided during the warranty period starting from the date of purchase."
                },
                {
                    "id": 4,
                    "text_ja": "・ピンポンラケット：お買い上げの日から6か月。ただし子ども用は1年間。・バドミントンラケット：お買い上げの日から3か月、ただし子ども用は半年。・テニスラケット：お買い上げの日から9か月。＊日本国内でお買い上げのお客様に限ります。",
                    "ruby_html": "・ピンポンラケット：お<ruby>買<rt>か</rt></ruby>い<ruby>上<rt>あ</rt></ruby>げの<ruby>日<rt>ひ</rt></ruby>から6か<ruby>月<rt>げつ</rt></ruby>。ただし<ruby>子<rt>こ</rt></ruby>ども<ruby>用<rt>よう</rt></ruby>は1<ruby>年間<rt>ねんかん</rt></ruby>。・バドミントンラケット：お<ruby>買<rt>か</rt></ruby>い<ruby>上<rt>あ</rt></ruby>げの<ruby>日<rt>ひ</rt></ruby>から3か<ruby>月<rt>げつ</rt></ruby>、ただし<ruby>子<rt>こ</rt></ruby>ども<ruby>用<rt>よう</rt></ruby>は<ruby>半年<rt>はんとし</rt></ruby>。・テニスラケット：お<ruby>買<rt>か</rt></ruby>い<ruby>上<rt>あ</rt></ruby>げの<ruby>日<rt>ひ</rt></ruby>から9か<ruby>月<rt>げつ</rt></ruby>。＊<ruby>日本国内<rt>にほんこくない</rt></ruby>でお<ruby>買<rt>か</rt></ruby>い<ruby>上<rt>あ</rt></ruby>げのお<ruby>客様<rt>きゃくさま</rt></ruby>に<ruby>限<rt>かぎ</rt></ruby>ります。",
                    "text_en": "- Table tennis racket: 6 months from purchase (1 year for children's model); - Badminton racket: 3 months from purchase (half a year for children's model); - Tennis racket: 9 months from purchase. * Limited to customers who purchased within Japan."
                },
                {
                    "id": 5,
                    "text_ja": "2. 次の場合は保証期間中でも修理または交換ができません。・火災、地震、水害などによる破損。・次のような使用方法による破損。（ラケットの上に重い物をのせる。ラケットを投げたり物をたたいたりする。ボールや羽根を打つこと以外のために使用するなど）・次のような状態で置いておいたことによる破損。（日光の当たるところや、湿気の多いところに長時間置くなど）",
                    "ruby_html": "2. <ruby>次<rt>つぎ</rt></ruby>の<ruby>場合<rt>ばあい</rt></ruby>は<ruby>保証期間中<rt>ほしょうきかんちゅう</rt></ruby>でも<ruby>修理<rt>しゅうり</rt></ruby>または<ruby>交換<rt>こうかん</rt></ruby>ができません。・<ruby>火災<rt>かさい</rt></ruby>、<ruby>地震<rt>じしん</rt></ruby>、<ruby>水害<rt>すいがい</rt></ruby>などによる<ruby>破損<rt>はそん</rt></ruby>。・<ruby>次<rt>つぎ</rt></ruby>のような<ruby>使用方法<rt>しようほうほう</rt></ruby>による<ruby>破損<rt>はそん</rt></ruby>。（ラケットの<ruby>上<rt>うえ</rt></ruby>に<ruby>重<rt>おも</rt></ruby>い<ruby>物<rt>もの</rt></ruby>をのせる。ラケットを<ruby>投<rt>な</rt></ruby>げたり<ruby>物<rt>もの</rt></ruby>をたたいたりする。ボールや<ruby>羽根<rt>はね</rt></ruby>を<ruby>打<rt>う</rt></ruby>つこと<ruby>以外<rt>いがい</rt></ruby>のために<ruby>使用<rt>しよう</rt></ruby>するなど）・<ruby>次<rt>つぎ</rt></ruby>のような<ruby>状態<rt>じょうたい</rt></ruby>で<ruby>置<rt>お</rt></ruby>いておいたことによる<ruby>破損<rt>はそん</rt></ruby>。（<ruby>日光<rt>にっこう</rt></ruby>の<ruby>当<rt>あ</rt></ruby>たるところや、<ruby>湿気<rt>しっけ</rt></ruby>の<ruby>多<rt>おお</rt></ruby>いところに<ruby>長時間置<rt>ちょうじかんお</rt></ruby>くなど）",
                    "text_en": "2. Under the following circumstances, repair or replacement is not available even within the warranty period: Damage from fire, earthquake, or flood; improper usage (placing heavy objects on racket, throwing or hitting non-ball items, using for purposes other than hitting balls/shuttlecocks); improper storage (leaving under direct sunlight or high humidity for long periods)."
                },
                {
                    "id": 6,
                    "text_ja": "3. 保証書をなくした場合は、修理または交換できないことがあります。ラケットショップ ふじ 東京都○○市××町1-2-3 Tel: 03-8888-7777",
                    "ruby_html": "3. <ruby>保証書<rt>ほしょうしょ</rt></ruby>をなくした<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>修理<rt>しゅうり</rt></ruby>または<ruby>交換<rt>こうかん</rt></ruby>できないことがあります。ラケットショップ ふじ <ruby>東京都<rt>とうきょうと</rt></ruby>○○<ruby>市<rt>し</rt></ruby>××<ruby>町<rt>ちょう</rt></ruby>1-2-3 Tel: 03-8888-7777",
                    "text_en": "3. If the warranty card is lost, repair or replacement may not be provided. Racket Shop Fuji, 1-2-3 xx-cho, oo-city, Tokyo Tel: 03-8888-7777."
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "保証書",
                "meaning_ja": "買った品物に問題があったら、修理したり、新しいものにとりかえると書いてある紙",
                "meaning_en": "warranty certificate / guarantee paper"
            },
            {
                "label": "注2",
                "term": "ご購入",
                "meaning_ja": "買うこと",
                "meaning_en": "purchase (polite)"
            },
            {
                "label": "注3",
                "term": "破損",
                "meaning_ja": "こわれたり傷ついたりすること",
                "meaning_en": "breakage, damage"
            },
            {
                "label": "注4",
                "term": "水害",
                "meaning_ja": "洪水や高波によって被害を受けること",
                "meaning_en": "flood / water damage"
            }
        ],
        "vocabulary": [
            {
                "term": "メーカー",
                "reading": "めーかー",
                "meaning": "maker, manufacturer / 生产厂商",
                "type": "noun"
            },
            {
                "term": "お買い上げ日",
                "reading": "おかいあげび",
                "meaning": "date of purchase / 购买日",
                "type": "noun"
            },
            {
                "term": "無料",
                "reading": "むりょう",
                "meaning": "free of charge / 免费",
                "type": "noun"
            },
            {
                "term": "修理する",
                "reading": "しゅうりする",
                "meaning": "to repair / 修理",
                "type": "verb"
            },
            {
                "term": "交換する",
                "reading": "こうかんする",
                "meaning": "to exchange, replace / 交换、更换",
                "type": "verb"
            },
            {
                "term": "限る",
                "reading": "かぎる",
                "meaning": "to limit, restrict / 仅限于",
                "type": "verb"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-59-1",
                "questionNumber": 1,
                "questionText_ja": "メイさんのラケットの保証期間はいつまでか。",
                "questionText_en": "Until when is the warranty period for May's racket?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "2014年7月31日",
                        "text_en": "July 31, 2014"
                    },
                    {
                        "id": 2,
                        "text_ja": "2014年10月30日",
                        "text_en": "October 30, 2014"
                    },
                    {
                        "id": 3,
                        "text_ja": "2015年1月31日",
                        "text_en": "January 31, 2015"
                    },
                    {
                        "id": 4,
                        "text_ja": "2015年5月31日",
                        "text_en": "May 31, 2015"
                    }
                ],
                "correctAnswer": 3,
                "explanation_ja": "メイさんが購入したのは「テニスラケット」です。購入日は「2014年5月1日」です。テニスラケットの保証期間は「お買い上げの日から9か月」と書かれています。2014年5月1日から9か月後は、2015年1月31日となります。したがって 3 が正解です。",
                "explanation_en": "May purchased a tennis racket (テニスラケット) on May 1, 2014. The warranty duration for tennis rackets is '9 months from date of purchase'. Adding 9 months to May 1, 2014 gives January 31, 2015. Therefore, Option 3 is correct."
            },
            {
                "questionId": "q-59-2",
                "questionNumber": 2,
                "questionText_ja": "保証期間中に以下のことをしたら、ラケットがこわれた。保証してもらえるのはどれか。",
                "questionText_en": "During the warranty period, the racket broke under one of the following circumstances. Which one will be covered under warranty?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "シャワールームに2日間置いてしまった。",
                        "text_en": "Left it in the shower room for 2 days."
                    },
                    {
                        "id": 2,
                        "text_ja": "テニスコートに忘れたら、その後大雨が降って、ぬれてしまった。",
                        "text_en": "Forgot it on the tennis court, and it got soaked in heavy rain."
                    },
                    {
                        "id": 3,
                        "text_ja": "友達がラケットの上に座ってしまった。",
                        "text_en": "A friend sat on top of the racket."
                    },
                    {
                        "id": 4,
                        "text_ja": "暑い中8時間ボールを打ち続けた。",
                        "text_en": "Kept hitting tennis balls for 8 hours in hot weather."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "第2項に保証対象外となる事例が挙げられています。\n1: 「湿気の多いところに長時間置く」に該当するため対象外。\n2: 雨による水濡れ放置は対象外。\n3: 「ラケットの上に重い物をのせる」に該当するため対象外。\n4: ボールを打つことはラケットの本来の使用目的（「普通の使用状態」）であり、長時間打ったとしても目的外使用には該当しません。したがって保証の対象となります。正解は 4 です。",
                "explanation_en": "Clause 2 lists exclusion cases.\nOption 1: Covered under 'leaving in high humidity for long periods' (not covered).\nOption 2: Negligent exposure to flood/rain (not covered).\nOption 3: Equivalent to 'placing heavy weight on racket' (not covered).\nOption 4: Hitting balls is the normal intended usage ('普通の使用状態') of a tennis racket, and is not prohibited by the exclusion rules. Therefore, Option 4 is covered."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆保証書（テニスラケット保証書）",
            "text_ja": "保証書では品目（テニス、卓球、バドミントン）ごとの保証月数の違い、および「通常使用による故障（無償保証）」と「不適切使用・保管ミス・天災による免責（有償または不可）」の境界を正確に読み解くことが要点です。",
            "text_en": "In warranty agreements, differentiate between product types (tennis vs. ping-pong vs. badminton) to calculate expiration dates, and distinguish covered normal use ('普通の使用状態') from exclusions (misuse, improper storage, force majeure).",
            "structureLayout": [
                {
                    "component": "製品・購入日",
                    "detail": "テニスラケット、2014年5月1日購入、保証期間9か月",
                    "en": "Product: Tennis racket, bought May 1, 2014; warranty 9 months."
                },
                {
                    "component": "期限計算",
                    "detail": "2014年5月1日＋9か月＝2015年1月31日",
                    "en": "Deadline calculation: May 1, 2014 + 9 mo = Jan 31, 2015."
                },
                {
                    "component": "免責条項",
                    "detail": "湿気放置、重い物を載せる、ボール打球以外は免責",
                    "en": "Exclusions: High humidity storage, heavy load, improper use."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "品目ごとの保証期間の違い（ピンポン6か月、バドミントン3か月、テニス9か月）を正しく参照しましょう。",
            "point_en": "Check the exact row corresponding to the sport (ping-pong 6 mo, badminton 3 mo, tennis 9 mo)."
        }
    },
    {
        "id": "dokkai-n3-p4-60",
        "pages": [136, 137],
        "problemNumber": 60,
        "genre": "映画館HP",
        "genre_en": "Cinema Schedule",
        "genre_zh": "电影院时刻表",
        "title_ja": "問題60 映画館HP（シネマスケジュール案内）",
        "title_en": "Problem 60: Cinema Website (Movie Screening Schedule)",
        "title_zh": "问题60 电影院网页（影院放映时刻表）",
        "preReading": {
            "question_ja": "映画館で映画を見るとき、上映時間や映画の内容をどのように確認しますか。",
            "question_en": "When watching a movie at a cinema, how do you verify showtimes and synopses?",
            "question_zh": "去电影院看电影时，你通常如何确认上映时间和剧情简介？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章は、映画館のホームページである。右のページの質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The following text is from a cinema website. Answer the questions on the right. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "A≪上映時間≫ シネマ1（50席）：10:15〜12:25 大きな食卓、14:00〜16:10 大きな食卓、17:15〜19:25 大きな食卓。",
                    "ruby_html": "A≪<ruby>上映時間<rt>じょうえいじかん</rt></ruby>≫ シネマ1（50<ruby>席<rt>せき</rt></ruby>）：10:15〜12:25 <ruby>大<rt>おお</rt></ruby>きな<ruby>食卓<rt>しょくたく</rt></ruby>、14:00〜16:10 <ruby>大<rt>おお</rt></ruby>きな<ruby>食卓<rt>しょくたく</rt></ruby>、17:15〜19:25 <ruby>大<rt>おお</rt></ruby>きな<ruby>食卓<rt>しょくたく</rt></ruby>。",
                    "text_en": "A: Screening Times - Screen 1 (50 seats): 10:15-12:25 'A Big Dining Table'; 14:00-16:10 'A Big Dining Table'; 17:15-19:25 'A Big Dining Table'."
                },
                {
                    "id": 2,
                    "text_ja": "シネマ2（150席）：11:45〜13:30 猫と一郎、15:15〜17:00 猫と一郎、19:15〜21:35 オハナ♡。",
                    "ruby_html": "シネマ2（150<ruby>席<rt>せき</rt></ruby>）：11:45〜13:30 <ruby>猫<rt>ねこ</rt></ruby>と<ruby>一郎<rt>いちろう</rt></ruby>、15:15〜17:00 <ruby>猫<rt>ねこ</rt></ruby>と<ruby>一郎<rt>いちろう</rt></ruby>、19:15〜21:35 オハナ♡。",
                    "text_en": "Screen 2 (150 seats): 11:45-13:30 'Cat and Ichiro'; 15:15-17:00 'Cat and Ichiro'; 19:15-21:35 'Ohana (Heart)'."
                },
                {
                    "id": 3,
                    "text_ja": "シネマ3（300席）：11:15〜14:15 風の忍者、14:30〜17:30 風の忍者。",
                    "ruby_html": "シネマ3（300<ruby>席<rt>せき</rt></ruby>）：11:15〜14:15 <ruby>風<rt>かぜ</rt></ruby>の<ruby>忍者<rt>にんじゃ</rt></ruby>、14:30〜17:30 <ruby>風<rt>かぜ</rt></ruby>の<ruby>忍者<rt>にんじゃ</rt></ruby>。",
                    "text_en": "Screen 3 (300 seats): 11:15-14:15 'Wind Ninja'; 14:30-17:30 'Wind Ninja'."
                },
                {
                    "id": 4,
                    "text_ja": "B≪映画紹介≫ ＊「大きな食卓」……15人家族の日常生活。笑いと涙の3年間を追った記録映画。",
                    "ruby_html": "B≪<ruby>映画紹介<rt>えいがしょうかい</rt></ruby>≫ ＊「<ruby>大<rt>おお</rt></ruby>きな<ruby>食卓<rt>しょくたく</rt></ruby>」……15<ruby>人家族<rt>にんかぞく</rt></ruby>の<ruby>日常生活<rt>にちじょうせいかつ</rt></ruby>。<ruby>笑<rt>わら</rt></ruby>いと<ruby>涙<rt>なみだ</rt></ruby>の3<ruby>年間<rt>ねんかん</rt></ruby>を<ruby>追<rt>お</rt></ruby>った<ruby>記録映画<rt>きろくえいが</rt></ruby>。",
                    "text_en": "B: Movie Synopses - * 'A Big Dining Table': Daily life of a 15-person family; documentary chronicling 3 years of tears and laughter."
                },
                {
                    "id": 5,
                    "text_ja": "＊「猫と一郎」……一郎は7歳の少年。メガネをかけると猫と会話ができる！？",
                    "ruby_html": "＊「<ruby>猫<rt>ねこ</rt></ruby>と<ruby>一郎<rt>いちろう</rt></ruby>」……<ruby>一郎<rt>いちろう</rt></ruby>は7<ruby>歳<rt>さい</rt></ruby>の<ruby>少年<rt>しょうねん</rt></ruby>。メガネをかけると<ruby>猫<rt>ねこ</rt></ruby>と<ruby>会話<rt>かいわ</rt></ruby>ができる！？",
                    "text_en": "* 'Cat and Ichiro': Ichiro is a 7-year-old boy. When he puts on glasses, he can talk with cats?!"
                },
                {
                    "id": 6,
                    "text_ja": "＊「風の忍者」……風のように移動する忍者ハンゾー。人気マンガを映画化。",
                    "ruby_html": "＊「<ruby>風<rt>かぜ</rt></ruby>の<ruby>忍者<rt>にんじゃ</rt></ruby>」……<ruby>風<rt>かぜ</rt></ruby>のように<ruby>移動<rt>いどう</rt></ruby>する<ruby>忍者<rt>にんじゃ</rt></ruby>ハンゾー。<ruby>人気<rt>にんき</rt></ruby>マンガを<ruby>映画化<rt>えいがか</rt></ruby>。",
                    "text_en": "* 'Wind Ninja': Hanzo, a ninja who moves like the wind; movie adaptation of a hit manga."
                },
                {
                    "id": 7,
                    "text_ja": "＊「オハナ♡」……ダンスチームの5人が世界のトップを目指す中で、いつしか家族のような関係に。オハナとはハワイの言葉で「家族」の意味。",
                    "ruby_html": "＊「オハナ♡」……ダンスチームの5<ruby>人<rt>にん</rt></ruby>が<ruby>世界<rt>せかい</rt></ruby>のトップを<ruby>目指<rt>めざ</rt></ruby>す<ruby>中<rt>なか</rt></ruby>で、いつしか<ruby>家族<rt>かぞく</rt></ruby>のような<ruby>関係<rt>かんけい</rt></ruby>に。オハナとはハワイの<ruby>言葉<rt>ことば</rt></ruby>で「<ruby>家族<rt>かぞく</rt></ruby>」の<ruby>意味<rt>いみ</rt></ruby>。",
                    "text_en": "* 'Ohana (Heart)': Five dance team members aim for the world's top and become like family. Ohana is Hawaiian for 'family'."
                }
            ]
        },
        "footnotes": [],
        "vocabulary": [
            {
                "term": "ホームページ",
                "reading": "ほーむぺーじ",
                "meaning": "website, web page / 网页",
                "type": "noun"
            },
            {
                "term": "〜席",
                "reading": "〜せき",
                "meaning": "seating for ~ / 〜座位",
                "type": "suffix"
            },
            {
                "term": "追う",
                "reading": "おう",
                "meaning": "to follow, chronicle / 追踪、按照顺序记录",
                "type": "verb"
            },
            {
                "term": "記録",
                "reading": "きろく",
                "meaning": "[film] chronicle, documentary / 记录",
                "type": "noun"
            },
            {
                "term": "目指す",
                "reading": "めざす",
                "meaning": "to aim for / 以为目标",
                "type": "verb"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-60-1",
                "questionNumber": 1,
                "questionText_ja": "グエンさんは動物が出てくる映画が見たい。午前中はアルバイトがあるが、午後は時間がある。何時から始まる映画が見られるか。",
                "questionText_en": "Nguyen wants to see a movie featuring animals. He has a part-time job in the morning, but is free in the afternoon. What time does the movie he can watch start?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "12:25",
                        "text_en": "12:25"
                    },
                    {
                        "id": 2,
                        "text_ja": "14:00",
                        "text_en": "14:00"
                    },
                    {
                        "id": 3,
                        "text_ja": "14:30",
                        "text_en": "14:30"
                    },
                    {
                        "id": 4,
                        "text_ja": "15:15",
                        "text_en": "15:15"
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "「動物が出てくる映画」は映画紹介から「猫と一郎」（猫と会話ができる）であることが分かります。グエンさんは午後に見るため、午後開始の回を探します。「猫と一郎」の上映回は 11:45〜13:30（開始は午前）と 15:15〜17:00（午後開始）です。したがって午後に見られる映画の開始時刻は「15:15」です。正解は 4 です。",
                "explanation_en": "From the movie synopsis, the film featuring animals is 'Cat and Ichiro' (猫と一郎). Nguyen is free in the afternoon (午後). Showings for 'Cat and Ichiro' are 11:45-13:30 (starts in morning) and 15:15-17:00 (starts in afternoon). Thus, the afternoon showing begins at 15:15. Therefore, Option 4 is correct."
            },
            {
                "questionId": "q-60-2",
                "questionNumber": 2,
                "questionText_ja": "タンさんは、午後時間ができたので映画を見ることにした。映画館にいられる時間は午後3時から午後6時までの3時間だけである。今日タンさんが、初めから終わりまで見ることができる映画は次のうちどれか。",
                "questionText_en": "Tan decided to watch a movie since he had free time in the afternoon. The time he can stay at the theater is only the 3 hours between 3:00 PM and 6:00 PM. Which movie can Tan watch today from beginning to end?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "大きな食卓",
                        "text_en": "A Big Dining Table"
                    },
                    {
                        "id": 2,
                        "text_ja": "猫と一郎",
                        "text_en": "Cat and Ichiro"
                    },
                    {
                        "id": 3,
                        "text_ja": "風の忍者",
                        "text_en": "Wind Ninja"
                    },
                    {
                        "id": 4,
                        "text_ja": "オハナ♡",
                        "text_en": "Ohana (Heart)"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "タンさんが映画館にいられるのは「15:00〜18:00」です。「初めから終わりまで見る」には、開始が15:00以降かつ終了が18:00以前である必要があります。\n・大きな食卓：14:00〜16:10（15時前開始）、17:15〜19:25（18時以降終了）。不可。\n・猫と一郎：15:15〜17:00。開始が15:00以降で終了が18:00前なので完全に収まります！\n・風の忍者：14:30〜17:30（15時前開始）。不可。\n・オハナ♡：19:15〜21:35。不可。\nしたがって 2 が正解です。",
                "explanation_en": "Tan can be at the cinema from 15:00 to 18:00. Watching from start to finish requires start >= 15:00 and end <= 18:00.\n- 'A Big Dining Table': 14:00-16:10 (starts before 15:00), 17:15-19:25 (ends after 18:00).\n- 'Cat and Ichiro': 15:15-17:00 (starts 15:15, ends 17:00; fits completely!).\n- 'Wind Ninja': 14:30-17:30 (starts before 15:00).\n- 'Ohana': 19:15-21:35 (after 18:00).\nTherefore, Option 2 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆映画館HP（シネマスケジュール案内）",
            "text_ja": "タイムテーブル読解では、あらすじ（映画紹介）から条件に合う作品名を特定するステップと、利用可能時間帯（開始時刻≧滞在開始、終了時刻≦滞在終了）に完全に収まるスロットを照合するステップを連動させて解きます。",
            "text_en": "Timetable reading links synopsis matching (identifying the film title from themes) with interval verification (ensuring start >= arrival time and end <= departure time).",
            "structureLayout": [
                {
                    "component": "映画内容照合",
                    "detail": "動物＝「猫と一郎」",
                    "en": "Content match: Animals = 'Cat and Ichiro'."
                },
                {
                    "component": "時間帯照合",
                    "detail": "15:00〜18:00に完全に収まる＝「猫と一郎」（15:15〜17:00）",
                    "en": "Time match: Entirely within 15:00-18:00 = 'Cat and Ichiro' (15:15-17:00)."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "途中入場や途中退出は不可（「初めから終わりまで」）なので、開始・終了の両方が時間枠内に収まるか必ず確認しましょう。",
            "point_en": "Verify both start and end times fall strictly within the stay window since partial viewing is prohibited."
        }
    },
    {
        "id": "dokkai-n3-p4-61",
        "pages": [138, 139],
        "problemNumber": 61,
        "genre": "メール",
        "genre_en": "Email Notification",
        "genre_zh": "电子邮件",
        "title_ja": "問題61 メール（会社説明会予約完了メール）",
        "title_en": "Problem 61: Email (Company Briefing Session Confirmation)",
        "title_zh": "问题61 电子邮件（说明会预约完成通知邮件）",
        "preReading": {
            "question_ja": "就職活動や面接の案内メールで、どのような注意事項が書かれていますか。",
            "question_en": "What precautions and instructions are typically written in job hunt or briefing confirmation emails?",
            "question_zh": "在求职或面试的确认邮件中，通常会写明哪些注意事项？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章と右のページのメールを見て、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "Read the following text and the email on the right page, and answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "ウェンさんはある会社に就職したいと思い、その会社の会社説明会にホームページから申し込みをした。その後、右のページのような添付ファイルがついた確認のメールが届いた。",
                    "ruby_html": "ウェンさんはある<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>就職<rt>しゅうしょく</rt></ruby>したいと<ruby>思<rt>おも</rt></ruby>い、その<ruby>会社<rt>かいしゃ</rt></ruby>の<ruby>会社説明会<rt>かいしゃせつめいかい</rt></ruby>にホームページから<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>みをした。その<ruby>後<rt>ご</rt></ruby>、<ruby>右<rt>みぎ</rt></ruby>のページのような<ruby>添付<rt>てんぷ</rt></ruby>ファイルがついた<ruby>確認<rt>かくにん</rt></ruby>のメールが<ruby>届<rt>とど</rt></ruby>いた。",
                    "text_en": "Wen wanted to work at a certain company and registered for their informational briefing on the website. Afterwards, a confirmation email arrived with an attachment."
                },
                {
                    "id": 2,
                    "text_ja": "(株)△△社 会社説明会 予約完了メール 【開催日時】20xx年12月1日 13:00〜14:30 ウェン・モーリー様",
                    "ruby_html": "(<ruby>株<rt>かぶ</rt></ruby>)△△<ruby>社<rt>しゃ</rt></ruby> <ruby>会社説明会<rt>かいしゃせつめいかい</rt></ruby> <ruby>予約完了<rt>よやくかんりょう</rt></ruby>メール 【<ruby>開催日時<rt>かいさいにちじ</rt></ruby>】20xx<ruby>年<rt>ねん</rt></ruby>12<ruby>月<rt>がつ</rt></ruby>1<ruby>日<rt>にち</rt></ruby> 13:00〜14:30 ウェン・モーリー<ruby>様<rt>さま</rt></ruby>",
                    "text_en": "Delta Co., Ltd. Company Briefing Reservation Confirmation - Date & Time: December 1, 20XX, 13:00-14:30 - To: Wen Morley"
                },
                {
                    "id": 3,
                    "text_ja": "株式会社△△社、採用担当です。このたびは、説明会にお申し込みいただきありがとうございました。日時や持ち物をもう一度ご確認いただき、ご参加くださいますよう、お願いいたします。",
                    "ruby_html": "<ruby>株式会社<rt>かぶしきがいしゃ</rt></ruby>△△<ruby>社<rt>しゃ</rt></ruby>、<ruby>採用担当<rt>さいようたんとう</rt></ruby>です。このたびは、<ruby>説明会<rt>せつめいかい</rt></ruby>にお<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>みいただきありがとうございました。<ruby>日時<rt>にちじ</rt></ruby>や<ruby>持<rt>も</rt></ruby>ち<ruby>物<rt>もの</rt></ruby>をもう<ruby>一度<rt>いちど</rt></ruby>ご<ruby>確認<rt>かくにん</rt></ruby>いただき、ご<ruby>参加<rt>さんか</rt></ruby>くださいますよう、お<ruby>願<rt>ねが</rt></ruby>いいたします。",
                    "text_en": "Recruitment Department, Delta Co., Ltd. Thank you very much for applying to our informational briefing. Please confirm the date, time, and required items again before attending."
                },
                {
                    "id": 4,
                    "text_ja": "「会社説明会」 ●持ち物：筆記用具、履歴書（写真をはってください。）、この予約完了メールをプリントアウトしたもの。 ●服装：スーツ。",
                    "ruby_html": "「<ruby>会社説明会<rt>かいしゃせつめいかい</rt></ruby>」 ●<ruby>持<rt>も</rt></ruby>ち<ruby>物<rt>もの</rt></ruby>：<ruby>筆記用具<rt>ひっきようぐ</rt></ruby>、<ruby>履歴書<rt>りれきしょ</rt></ruby>（<ruby>写真<rt>しゃしん</rt></ruby>をはってください。）、この<ruby>予約完了<rt>よやくかんりょう</rt></ruby>メールをプリントアウトしたもの。 ●<ruby>服装<rt>ふくそう</rt></ruby>：スーツ。",
                    "text_en": "Company Briefing - Items to bring: Writing utensils, résumé (please affix photo), printout of this reservation email. - Attire: Suit."
                },
                {
                    "id": 5,
                    "text_ja": "●会場：△△社本社 〒111-2222 東京都○○市□□2-3-4 (株)△△社第一ビル ●交通機関：JR中央線・総武線、東京メトロ東西線「○×駅」徒歩10分。",
                    "ruby_html": "●<ruby>会場<rt>かいじょう</rt></ruby>：△△<ruby>社本社<rt>しゃほんしゃ</rt></ruby> 〒111-2222 <ruby>東京都<rt>とうきょうと</rt></ruby>○○<ruby>市<rt>し</rt></ruby>□□2-3-4 (<ruby>株<rt>かぶ</rt></ruby>)△△<ruby>社第一<rt>しゃだいいち</rt></ruby>ビル ●<ruby>交通機関<rt>こうつうきかん</rt></ruby>：JR<ruby>中央線<rt>ちゅうおうせん</rt></ruby>・<ruby>総武線<rt>そうぶせん</rt></ruby>、<ruby>東京<rt>とうきょう</rt></ruby>メトロ<ruby>東西線<rt>とうざいせん</rt></ruby>「○×<ruby>駅<rt>えき</rt></ruby>」<ruby>徒歩<rt>とほ</rt></ruby>10<ruby>分<rt>ふん</rt></ruby>。",
                    "text_en": "Venue: Delta Co. Headquarters, Building 1, 2-3-4 square-square, oo-city, Tokyo; Transport: JR Chuo/Sobu Line or Tokyo Metro Tozai Line, 10 min walk from 'ox Station'."
                },
                {
                    "id": 6,
                    "text_ja": "●受付場所：ビル1階の(株)△△社本社受付 ●受付開始時間：開始時間の10分前〜 ＊早くご来社いただいてもご案内ができません。また、開始時刻を過ぎてからの参加はできません。",
                    "ruby_html": "●<ruby>受付場所<rt>うけつけばしょ</rt></ruby>：ビル1<ruby>階<rt>かい</rt></ruby>の(<ruby>株<rt>かぶ</rt></ruby>)△△<ruby>社本社受付<rt>しゃほんしゃうけつけ</rt></ruby> ●<ruby>受付開始時間<rt>うけつけかいしじかん</rt></ruby>：<ruby>開始時間<rt>かいしじかん</rt></ruby>の10<ruby>分前<rt>ふんまえ</rt></ruby>〜 ＊<ruby>早<rt>はや</rt></ruby>くご<ruby>来社<rt>らいしゃ</rt></ruby>いただいてもご<ruby>案内<rt>あんない</rt></ruby>ができません。また、<ruby>開始時刻<rt>かいしじこく</rt></ruby>を<ruby>過<rt>す</rt></ruby>ぎてからの<ruby>参加<rt>さんか</rt></ruby>はできません。",
                    "text_en": "Reception desk: 1st floor HQ reception; Reception opens: 10 minutes prior to starting time. * Even if you arrive early, we cannot accommodate you. Furthermore, entry after starting time is not permitted."
                },
                {
                    "id": 7,
                    "text_ja": "＜注意事項＞ ＊当日は時間厳守でお願いいたします。 ＊前日までに参加日の変更がある場合は、当社ホームページの採用案内ページからキャンセルの手続きをして、あらためて申し込みをしてください。 ＊当日の遅刻や欠席は直接当社にご連絡ください。(採用担当: 03-4567-8901)",
                    "ruby_html": "＜<ruby>注意事項<rt>ちゅういじこう</rt></ruby>＞ ＊<ruby>当日<rt>とうじつ</rt></ruby>は<ruby>時間厳守<rt>じかんげんしゅ</rt></ruby>でお<ruby>願<rt>ねが</rt></ruby>いいたします。 ＊<ruby>前日<rt>ぜんじつ</rt></ruby>までに<ruby>参加日<rt>さんかび</rt></ruby>の<ruby>変更<rt>へんこう</rt></ruby>がある<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>当社<rt>とうしゃ</rt></ruby>ホームページの<ruby>採用案内<rt>さいようあんない</rt></ruby>ページからキャンセルの<ruby>手続<rt>てつづ</rt></ruby>きをして、あらためて<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>みをしてください。 ＊<ruby>当日<rt>とうじつ</rt></ruby>の<ruby>遅刻<rt>ちこく</rt></ruby>や<ruby>欠席<rt>けっせき</rt></ruby>は<ruby>直接当社<rt>ちょくせつとうしゃ</rt></ruby>にご<ruby>連絡<rt>れんらく</rt></ruby>ください。(<ruby>採用担当<rt>さいようたんとう</rt></ruby>: 03-4567-8901)",
                    "text_en": "Important Notices: * Please strictly observe punctuality. * To reschedule by the day before, please cancel via our recruitment webpage and re-apply. * In case of same-day tardiness or absence, please contact us directly by phone (Recruitment Team: 03-4567-8901)."
                }
            ]
        },
        "footnotes": [],
        "vocabulary": [
            {
                "term": "添付ファイル",
                "reading": "てんぷふぁいる",
                "meaning": "attached document, attachment / 附件",
                "type": "noun"
            },
            {
                "term": "株式会社",
                "reading": "かぶしきがいしゃ",
                "meaning": "joint-stock company, Co., Ltd. / 股份公司",
                "type": "noun"
            },
            {
                "term": "採用",
                "reading": "さいよう",
                "meaning": "hiring, recruitment / 录用",
                "type": "noun"
            },
            {
                "term": "筆記用具",
                "reading": "ひっきようぐ",
                "meaning": "writing instruments / 文具",
                "type": "noun"
            },
            {
                "term": "履歴書",
                "reading": "りれきしょ",
                "meaning": "résumé, CV / 简历",
                "type": "noun"
            },
            {
                "term": "プリントアウト",
                "reading": "ぷりんとおうと",
                "meaning": "printout / 打印",
                "type": "noun"
            },
            {
                "term": "徒歩",
                "reading": "とほ",
                "meaning": "on foot, walking / 徒步",
                "type": "noun"
            },
            {
                "term": "来社する",
                "reading": "らいしゃする",
                "meaning": "to visit the company / 来公司",
                "type": "verb"
            },
            {
                "term": "時間厳守",
                "reading": "じかんげんしゅ",
                "meaning": "strict punctuality / 严格遵守时间",
                "type": "noun"
            },
            {
                "term": "当社",
                "reading": "とうしゃ",
                "meaning": "our company / 我公司",
                "type": "noun"
            },
            {
                "term": "キャンセル",
                "reading": "きゃんせる",
                "meaning": "cancellation / 取消",
                "type": "noun"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-61-1",
                "questionNumber": 1,
                "questionText_ja": "説明会に行く際、○×駅に何時に着くのが一番よいか。",
                "questionText_en": "When attending the briefing, what time is best to arrive at ox Station?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "12時35分",
                        "text_en": "12:35"
                    },
                    {
                        "id": 2,
                        "text_ja": "12時50分",
                        "text_en": "12:50"
                    },
                    {
                        "id": 3,
                        "text_ja": "13時ちょうど",
                        "text_en": "Exactly 13:00"
                    },
                    {
                        "id": 4,
                        "text_ja": "14時半",
                        "text_en": "14:30"
                    }
                ],
                "correctAnswer": 1,
                "explanation_ja": "説明会の開始時刻は13:00です。駅から会社までは徒歩10分かかり、受付開始は「開始時間の10分前（12:50）〜」です。また「開始時刻を過ぎてからの参加はできません」とあります。12:50に駅に着いた場合、徒歩10分で到着は13:00となり、少しでも遅れると参加できなくなります。12:35に駅に着けば、12:45頃に会社に着き、12:50の受付開始と同時に余裕をもって受付を済ませることができます。したがって 1 が正解です。",
                "explanation_en": "The briefing begins at 13:00. It takes 10 minutes on foot from the station, and reception opens 10 minutes prior (12:50). Late arrivals after 13:00 are not permitted. Arriving at the station at 12:50 would put arrival at the building right at 13:00 with zero margin for error. Arriving at the station at 12:35 allows arrival around 12:45-12:50, entering punctually right when reception opens. Therefore, Option 1 is correct."
            },
            {
                "questionId": "q-61-2",
                "questionNumber": 2,
                "questionText_ja": "ウェンさんは説明会の日に具合が悪くなり開始の時間に行けなくなった。どうすればよいか。",
                "questionText_en": "Wen felt unwell on the day of the briefing and became unable to make it by starting time. What should she do?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "連絡はせず、参加もしない。",
                        "text_en": "Do not contact them and do not attend."
                    },
                    {
                        "id": 2,
                        "text_ja": "会社のホームページの採用案内ページからキャンセルをする。",
                        "text_en": "Cancel via the recruitment page on the company website."
                    },
                    {
                        "id": 3,
                        "text_ja": "連絡はせず、遅れて参加する。",
                        "text_en": "Do not contact them and join late."
                    },
                    {
                        "id": 4,
                        "text_ja": "会社の採用担当者に電話をする。",
                        "text_en": "Call the company's recruitment coordinator."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "注意事項に「前日までに参加日の変更がある場合は、当社ホームページの採用案内ページからキャンセルの手続きをして…」「当日の遅刻や欠席は直接当社にご連絡ください。(採用担当: 03-4567-8901)」と明確に区別されています。今回は「説明会の日に（＝当日）」の欠席・遅刻であるため、電話で直接採用担当者に連絡しなければなりません。したがって 4 が正解です。",
                "explanation_en": "The instructions distinguish between: 'rescheduling by the previous day' (cancel online via webpage) and 'same-day tardiness/absence' ('contact us directly by phone at 03-4567-8901'). Since this occurred on the day of the briefing (当日), calling the recruitment coordinator directly is required. Therefore, Option 4 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆メール（会社説明会予約完了メール）",
            "text_ja": "ビジネス案内メールでは、「事前対応（前日まで・Web）」と「緊急対応（当日・電話）」の手続きの分岐を峻別することが頻出テーマです。また所要時間（駅からの徒歩時間＋受付開始時間）の逆算問題も重要です。",
            "text_en": "Business confirmation emails often test bifurcated procedures: advance online actions (by previous day) vs. urgent telephone actions (same-day). Back-calculating departure times including walking buffers is another key task.",
            "structureLayout": [
                {
                    "component": "時間逆算",
                    "detail": "13:00開始、12:50受付、徒歩10分→12:35駅到着が最適",
                    "en": "Time back-calculation: 13:00 start, 12:50 reception, 10 min walk -> 12:35 at station."
                },
                {
                    "component": "変更・欠席対応",
                    "detail": "前日まで＝HPでキャンセル、当日＝電話で連絡",
                    "en": "Reschedule rule: By prior day = Web cancel; Same day = Call recruitment."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "「前日まで」と「当日」で連絡手段が異なる点に注目しましょう。",
            "point_en": "Note the critical distinction between 'by previous day' (Web) and 'on the day' (Phone)."
        }
    },
    {
        "id": "dokkai-n3-p4-62",
        "pages": [140, 141],
        "problemNumber": 62,
        "genre": "メール",
        "genre_en": "Email Newsletter",
        "genre_zh": "电子邮件杂志",
        "title_ja": "問題62 メール（留学生の生活応援メルマガ）",
        "title_en": "Problem 62: Email (International Students Newsletter)",
        "title_zh": "问题62 电子杂志（留学生生活支援电子杂志）",
        "preReading": {
            "question_ja": "メールマガジンで読みたい記事やイベント情報はどのように探しますか。",
            "question_en": "How do you find interesting articles or event information in email newsletters?",
            "question_zh": "在电子杂志中，你通常如何查找感兴趣的文章或活动信息？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章はメールマガジンである。文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "The following text is an email newsletter. Read it and answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "★留学生の生活応援メールマガジン★ ★20XX年1月号★ 新年あけましておめでとうございます！",
                    "ruby_html": "★<ruby>留学生<rt>りゅうがくせい</rt></ruby>の<ruby>生活応援<rt>せいかつおうえん</rt></ruby>メールマガジン★ ★20XX<ruby>年<rt>ねん</rt></ruby>1<ruby>月号<rt>がつごう</rt></ruby>★ <ruby>新年<rt>しんねん</rt></ruby>あけましておめでとうございます！",
                    "text_en": "★ International Student Life Support Newsletter ★ ★ January Issue, 20XX ★ Happy New Year!"
                },
                {
                    "id": 2,
                    "text_ja": "日本のお正月はいかがですか？ 留学生の生活応援メルマガは、今年もみなさんの役に立つ情報をどんどん紹介しますので、どうぞよろしくお願いいたします！",
                    "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>のお<ruby>正月<rt>しょうがつ</rt></ruby>はいかがですか？ <ruby>留学生<rt>りゅうがくせい</rt></ruby>の<ruby>生活応援<rt>せいかつおうえん</rt></ruby>メルマガは、<ruby>今年<rt>ことし</rt></ruby>もみなさんの<ruby>役<rt>やく</rt></ruby>に<ruby>立<rt>た</rt></ruby>つ<ruby>情報<rt>じょうほう</rt></ruby>をどんどん<ruby>紹介<rt>しょうかい</rt></ruby>しますので、どうぞよろしくお<ruby>願<rt>ねが</rt></ruby>いいたします！",
                    "text_en": "How are you enjoying the New Year in Japan? The International Student Support Newsletter will continue sharing lots of useful tips this year, so stay tuned!"
                },
                {
                    "id": 3,
                    "text_ja": "目次 1. ニュース………新年会・不用品交換 2. 特集……………「みんなの節約方法」",
                    "ruby_html": "<ruby>目次<rt>もくじ</rt></ruby> 1. ニュース………<ruby>新年会<rt>しんねんかい</rt></ruby>・<ruby>不用品交換<rt>ふようひんこうかん</rt></ruby> 2. <ruby>特集<rt>とくしゅう</rt></ruby>……………「みんなの<ruby>節約方法<rt>せつやくほうほう</rt></ruby>」",
                    "text_en": "Contents: 1. News: New Year party, Unwanted goods exchange; 2. Special Feature: 'Everyone's Money-Saving Tips'."
                },
                {
                    "id": 4,
                    "text_ja": "◆1. ニュース 新年会 餅つき、おせち料理など、日本のお正月を楽しみましょう。日時：1月15日(土) 13:00〜17:00 場所：○○市民会館集会室 参加申し込みはこちら ①http://ryugakuoen.or.jp/shinnen.htm",
                    "ruby_html": "◆1. ニュース <ruby>新年会<rt>しんねんかい</rt></ruby> <ruby>餅<rt>もち</rt></ruby>つき、おせち<ruby>料理<rt>りょうり</rt></ruby>など、<ruby>日本<rt>にほん</rt></ruby>のお<ruby>正月<rt>しょうがつ</rt></ruby>を<ruby>楽<rt>たの</rt></ruby>しみましょう。<ruby>日時<rt>にちじ</rt></ruby>：1<ruby>月<rt>がつ</rt></ruby>15<ruby>日<rt>にち</rt></ruby>(<ruby>土<rt>ど</rt></ruby>) 13:00〜17:00 <ruby>場所<rt>ばしょ</rt></ruby>：○○<ruby>市民会館集会室<rt>しみんかいかんしゅうかいしつ</rt></ruby> <ruby>参加申<rt>さんかもう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>みはこちら ①http://ryugakuoen.or.jp/shinnen.htm",
                    "text_en": "1. News - New Year Party: Enjoy traditional Japanese New Year with mochi pounding and osechi food. Date: Sat, Jan 15, 13:00-17:00 at City Hall Room. Register here: (1) http://ryugakuoen.or.jp/shinnen.htm"
                },
                {
                    "id": 5,
                    "text_ja": "不用品交換 家具、電気製品など、欲しいものやいらないものを書いておくと、だれかと交換できるかもしれません。交換ページはこちら http://ryugakuoen.or.jp/koukan.htm",
                    "ruby_html": "<ruby>不用品交換<rt>ふようひんこうかん</rt></ruby> <ruby>家具<rt>かぐ</rt></ruby>、<ruby>電気製品<rt>でんきせいひん</rt></ruby>など、<ruby>欲<rt>ほ</rt></ruby>しいものやいらないものを<ruby>書<rt>か</rt></ruby>いておくと、だれかと<ruby>交換<rt>こうかん</rt></ruby>できるかもしれません。<ruby>交換<rt>こうかん</rt></ruby>ページはこちら http://ryugakuoen.or.jp/koukan.htm",
                    "text_en": "Unwanted items exchange: Post items you need or want to give away, such as furniture and electrical appliances! Exchange page: http://ryugakuoen.or.jp/koukan.htm"
                },
                {
                    "id": 6,
                    "text_ja": "◆2. 特集「みんなの節約方法」 電気代を30%カットする方法、安いお店の情報など、上手に節約しながら日本での生活を楽しむ留学生のアイディアがたくさん！ぜひ参考にしてください！ 特集ページはこちら http://ryugakuoen.or.jp/tokushu.htm",
                    "ruby_html": "◆2. <ruby>特集<rt>とくしゅう</rt></ruby>「みんなの<ruby>節約方法<rt>せつやくほうほう</rt></ruby>」 <ruby>電気代<rt>でんきだい</rt></ruby>を30%カットする<ruby>方法<rt>ほうほう</rt></ruby>、<ruby>安<rt>やす</rt></ruby>いお<ruby>店<rt>みせ</rt></ruby>の<ruby>情報<rt>じょうほう</rt></ruby>など、<ruby>上手<rt>じょうず</rt></ruby>に<ruby>節約<rt>せつやく</rt></ruby>しながら<ruby>日本<rt>にほん</rt></ruby>での<ruby>生活<rt>せいかつ</rt></ruby>を<ruby>楽<rt>たの</rt></ruby>しむ<ruby>留学生<rt>りゅうがくせい</rt></ruby>のアイディアがたくさん！ぜひ<ruby>参考<rt>さんこう</rt></ruby>にしてください！ <ruby>特集<rt>とくしゅう</rt></ruby>ページはこちら http://ryugakuoen.or.jp/tokushu.htm",
                    "text_en": "2. Special Feature 'Everyone's Money-Saving Tips': Full of ideas from students who save money while enjoying life, such as cutting electricity bills by 30% and finding cheap shops! Special feature: http://ryugakuoen.or.jp/tokushu.htm"
                },
                {
                    "id": 7,
                    "text_ja": "◆バックナンバーはこちら http://ryugakuoen.or.jp/menu-mmag.htm ◆このメルマガは配信専用です。このアドレスに返信はできません。 ご意見、お問い合わせはこちら ②http://ryugakuoen.or.jp/ad/mail.htm ◆配信停止はこちら ③http://ryugakuoen.or.jp/mmag.resign.htm",
                    "ruby_html": "◆バックナンバーはこちら http://ryugakuoen.or.jp/menu-mmag.htm ◆このメルマガは<ruby>配信専用<rt>はいしんせんよう</rt></ruby>です。このアドレスに<ruby>返信<rt>へんしん</rt></ruby>はできません。 ご<ruby>意見<rt>いけん</rt></ruby>、お<ruby>問<rt>と</rt></ruby>い<ruby>合<rt>あ</rt></ruby>わせはこちら ②http://ryugakuoen.or.jp/ad/mail.htm ◆<ruby>配信停止<rt>はいしんていし</rt></ruby>はこちら ③http://ryugakuoen.or.jp/mmag.resign.htm",
                    "text_en": "Back issues: http://ryugakuoen.or.jp/menu-mmag.htm; * This newsletter is send-only; you cannot reply directly. Feedback/Inquiries: (2) http://ryugakuoen.or.jp/ad/mail.htm; Unsubscribe: (3) http://ryugakuoen.or.jp/mmag.resign.htm"
                },
                {
                    "id": 8,
                    "text_ja": "発行人：NPO留学生の生活応援グループ 編集人：メルマガ委員会 e-mail: ④xxx@ryuugakuoen.or.jp",
                    "ruby_html": "<ruby>発行人<rt>はっこうにん</rt></ruby>：NPO<ruby>留学生<rt>りゅうがくせい</rt></ruby>の<ruby>生活応援<rt>せいかつおうえん</rt></ruby>グループ <ruby>編集人<rt>へんしゅうにん</rt></ruby>：メルマガ<ruby>委員会<rt>いいんかい</rt></ruby> e-mail: ④xxx@ryuugakuoen.or.jp",
                    "text_en": "Publisher: NPO International Student Life Support Group; Editor: Newsletter Committee; e-mail: (4) xxx@ryuugakuoen.or.jp"
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "メールマガジン",
                "meaning_ja": "メールで送られてくる情報",
                "meaning_en": "e-mail magazine, digital newsletter"
            }
        ],
        "vocabulary": [
            {
                "term": "不用品",
                "reading": "ふようひん",
                "meaning": "unneeded, unwanted article / 不使用的东西",
                "type": "noun"
            },
            {
                "term": "特集",
                "reading": "とくしゅう",
                "meaning": "special feature / 专题",
                "type": "noun"
            },
            {
                "term": "節約",
                "reading": "せつやく",
                "meaning": "saving, economizing / 节约",
                "type": "noun"
            },
            {
                "term": "餅つき",
                "reading": "もちつき",
                "meaning": "pounding rice into mochi / 捣年糕",
                "type": "noun"
            },
            {
                "term": "おせち料理",
                "reading": "おせちりょうり",
                "meaning": "traditional New Year's dishes / 年节饭",
                "type": "noun"
            },
            {
                "term": "カットする",
                "reading": "かっとする",
                "meaning": "to cut, reduce / 削减",
                "type": "verb"
            },
            {
                "term": "配信",
                "reading": "はいしん",
                "meaning": "send out, transmit / 发送",
                "type": "noun"
            },
            {
                "term": "〜専用",
                "reading": "〜せんよう",
                "meaning": "exclusively for ~ / 〜专用",
                "type": "suffix"
            },
            {
                "term": "返信",
                "reading": "へんしん",
                "meaning": "reply / 回信",
                "type": "noun"
            },
            {
                "term": "クリックする",
                "reading": "くりっくする",
                "meaning": "to click / 点击",
                "type": "verb"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-62-1",
                "questionNumber": 1,
                "questionText_ja": "新年会に参加したい場合、どうすればよいと書いてあるか。",
                "questionText_en": "What is written that one should do if one wants to participate in the New Year party?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "連絡はしないで、直接1月15日に○○市民会館集会室へ行く。",
                        "text_en": "Go directly to the City Hall meeting room on January 15 without contacting them."
                    },
                    {
                        "id": 2,
                        "text_ja": "①のURLをクリックして手続きをする。",
                        "text_en": "Click URL (1) and complete the procedure."
                    },
                    {
                        "id": 3,
                        "text_ja": "②のURLをクリックして手続きをする。",
                        "text_en": "Click URL (2) and complete the procedure."
                    },
                    {
                        "id": 4,
                        "text_ja": "④のメールアドレスにメールを送る。",
                        "text_en": "Send an email to address (4)."
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "「新年会」の案内の直下に「参加申し込みはこちら ①http://ryugakuoen.or.jp/shinnen.htm」と指定されています。したがって、①のURLをクリックして手続きをする 2 が正解です。",
                "explanation_en": "Directly beneath the New Year Party announcement, it specifies: 'Sign up here: (1) http://ryugakuoen.or.jp/shinnen.htm'. Therefore, Option 2 ('Click URL (1) and complete the procedure') is correct."
            },
            {
                "questionId": "q-62-2",
                "questionNumber": 2,
                "questionText_ja": "このメールマガジンをもう受け取りたくない。どうすればよいと書いてあるか。",
                "questionText_en": "You no longer want to receive this newsletter. What does it say you should do?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "このメールマガジンに返信をして伝える。",
                        "text_en": "Inform them by replying to this email newsletter."
                    },
                    {
                        "id": 2,
                        "text_ja": "②のURLをクリックして手続きをする。",
                        "text_en": "Click URL (2) and complete the procedure."
                    },
                    {
                        "id": 3,
                        "text_ja": "③のURLをクリックして手続きをする。",
                        "text_en": "Click URL (3) and complete the procedure."
                    },
                    {
                        "id": 4,
                        "text_ja": "④のメールアドレスにメールを送る。",
                        "text_en": "Send an email to email address (4)."
                    }
                ],
                "correctAnswer": 3,
                "explanation_ja": "末尾のフッター部分に「◆このメルマガは配信専用です。このアドレスに返信はできません」「◆配信停止はこちら ③http://ryugakuoen.or.jp/mmag.resign.htm」と明記されています。配信停止（購読解除）をするには③のURLにアクセスする必要があります。したがって 3 が正解です。",
                "explanation_en": "In the footer, it clearly states: 'This newsletter is send-only; you cannot reply directly' and 'Unsubscribe here: (3) http://ryugakuoen.or.jp/mmag.resign.htm'. To stop receiving it, you must click URL (3). Therefore, Option 3 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆メール（留学生の生活応援メルマガ）",
            "text_ja": "メールマガジンの問題では、本文中の各種URLリンク（申込用、問い合わせ用、配信停止用）の役割を正しく識別することが核心です。「配信専用アドレス」には返信できないというルールも頻出の確認ポイントです。",
            "text_en": "In newsletter questions, match each URL link with its specific destination (event registration, general inquiries, unsubscription). Remember that send-only (配信専用) addresses do not accept direct replies.",
            "structureLayout": [
                {
                    "component": "① 参加申込",
                    "detail": "新年会参加リンク（shinnen.htm）",
                    "en": "(1) Event registration: New Year Party link."
                },
                {
                    "component": "② 問合せ窓口",
                    "detail": "意見・問い合わせ用リンク（mail.htm）",
                    "en": "(2) Inquiries: Feedback & question form."
                },
                {
                    "component": "③ 配信停止",
                    "detail": "購読解除用リンク（resign.htm）",
                    "en": "(3) Unsubscribe: Resign link."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "URLの末尾（shinnen, mail, resign）の単語からもリンクの役割を推測できます。",
            "point_en": "Keywords at the end of URLs (shinnen, mail, resign) help confirm each link's exact purpose."
        }
    },
    {
        "id": "dokkai-n3-p4-63",
        "pages": [142, 143],
        "problemNumber": 63,
        "genre": "メール",
        "genre_en": "Customer Service Email",
        "genre_zh": "客服邮件",
        "title_ja": "問題63 メール（不良品返品・返金メール）",
        "title_en": "Problem 63: Email (Product Return & Refund Response)",
        "title_zh": "问题63 电子邮件（残次品退货与退款回复邮件）",
        "preReading": {
            "question_ja": "ネットショッピングで買った商品が壊れていたとき、どのように対応しますか。",
            "question_en": "How do you respond when a product purchased online arrives broken or defective?",
            "question_zh": "网购的商品如果有破损或瑕疵，你通常会如何处理？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "Read the following text and answer the questions. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "インターネットで買った商品が不良品だったので、チンさんが返品の希望をメールで連絡したら、以下のような返事が来た。",
                    "ruby_html": "インターネットで<ruby>買<rt>か</rt></ruby>った<ruby>商品<rt>しょうひん</rt></ruby>が<ruby>不良品<rt>ふりょうひん</rt></ruby>だったので、チンさんが<ruby>返品<rt>へんぴん</rt></ruby>の<ruby>希望<rt>きぼう</rt></ruby>をメールで<ruby>連絡<rt>れんらく</rt></ruby>したら、<ruby>以下<rt>いか</rt></ruby>のような<ruby>返事<rt>へんじ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。",
                    "text_en": "Because an item purchased online was defective, Chin emailed requesting a return, and received the following response."
                },
                {
                    "id": 2,
                    "text_ja": "チン・スーチー様 いつも○×ショップをご利用いただきまして、ありがとうございます。担当の木村と申します。",
                    "ruby_html": "チン・スーチー<ruby>様<rt>さま</rt></ruby> いつも○×ショップをご<ruby>利用<rt>りよう</rt></ruby>いただきまして、ありがとうございます。<ruby>担当<rt>たんとう</rt></ruby>の<ruby>木村<rt>きむら</rt></ruby>と<ruby>申<rt>もう</rt></ruby>します。",
                    "text_en": "Dear Chin Suchi: Thank you for shopping with OX Shop. My name is Kimura, customer service representative."
                },
                {
                    "id": 3,
                    "text_ja": "このたびは、先日ご購入いただきました商品【ABC電気ポット】に不備がございましたこと、大変申し訳ありませんでした。",
                    "ruby_html": "このたびは、<ruby>先日<rt>せんじつ</rt></ruby>ご<ruby>購入<rt>こうにゅう</rt></ruby>いただきました<ruby>商品<rt>しょうひん</rt></ruby>【ABC<ruby>電気<rt>でんき</rt></ruby>ポット】に<ruby>不備<rt>ふび</rt></ruby>がございましたこと、<ruby>大変<rt>たいへん</rt></ruby><ruby>申<rt>もう</rt></ruby>し<ruby>訳<rt>わけ</rt></ruby>ありませんでした。",
                    "text_en": "We sincerely apologize that the product you recently purchased, [ABC Electric Pot], had a defect."
                },
                {
                    "id": 4,
                    "text_ja": "大変ご面倒ではございますが、商品【ABC電気ポット】を、商品着払いにて、ご返送くださいますようお願いいたします。",
                    "ruby_html": "<ruby>大変<rt>たいへん</rt></ruby>ご<ruby>面倒<rt>めんどう</rt></ruby>ではございますが、<ruby>商品<rt>しょうひん</rt></ruby>【ABC<ruby>電気<rt>でんき</rt></ruby>ポット】を、<ruby>商品着払<rt>しょうひんちゃくばら</rt></ruby>いにて、ご<ruby>返送<rt>へんそう</rt></ruby>くださいますようお<ruby>願<rt>ねが</rt></ruby>いいたします。",
                    "text_en": "We are very sorry for the inconvenience, but please return the [ABC Electric Pot] to us via cash on delivery (receiver pays postage)."
                },
                {
                    "id": 5,
                    "text_ja": "●ご返送先住所 〒123-4567 東京都○○区○○町1-2-3 株式会社 ○×ショップ Tel: 03-1234-5678",
                    "ruby_html": "●ご<ruby>返送先住所<rt>へんそうさきじゅうしょ</rt></ruby> 〒123-4567 <ruby>東京都<rt>とうきょうと</rt></ruby>○○<ruby>区<rt>く</rt></ruby>○○<ruby>町<rt>ちょう</rt></ruby>1-2-3 <ruby>株式会社<rt>かぶしきがいしゃ</rt></ruby> ○×ショップ Tel: 03-1234-5678",
                    "text_en": "Return address: 1-2-3 oo-cho, oo-ku, Tokyo 123-4567, OX Shop Co., Ltd. Tel: 03-1234-5678"
                },
                {
                    "id": 6,
                    "text_ja": "商品が到着しましたら、ご返金の対応をさせていただきます。",
                    "ruby_html": "<ruby>商品<rt>しょうひん</rt></ruby>が<ruby>到着<rt>とうちゃく</rt></ruby>しましたら、ご<ruby>返金<rt>へんきん</rt></ruby>の<ruby>対応<rt>たいおう</rt></ruby>をさせていただきます。",
                    "text_en": "Once the item arrives, we will process your refund."
                },
                {
                    "id": 7,
                    "text_ja": "つきましては、お客様のお振込先口座を教えていただけますでしょうか。下の項目にご入力の上、このメールにご返信いただきますようお願いいたします。",
                    "ruby_html": "つきましては、お<ruby>客様<rt>きゃくさま</rt></ruby>のお<ruby>振込先口座<rt>ふりこみさきこうざ</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えていただけますでしょうか。<ruby>下<rt>した</rt></ruby>の<ruby>項目<rt>こうもく</rt></ruby>にご<ruby>入力<rt>にゅうりょく</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>、このメールにご<ruby>返信<rt>へんしん</rt></ruby>いただきますようお<ruby>願<rt>ねが</rt></ruby>いいたします。",
                    "text_en": "Accordingly, could you please provide your bank transfer account information? Please fill in the fields below and reply to this email."
                },
                {
                    "id": 8,
                    "text_ja": "●銀行名： ●支店名： ●口座番号： ●ご名義人様：",
                    "ruby_html": "●<ruby>銀行名<rt>ぎんこうめい</rt></ruby>： ●<ruby>支店名<rt>してんめい</rt></ruby>： ●<ruby>口座番号<rt>こうざばんごう</rt></ruby>： ●ご<ruby>名義人様<rt>めいぎにんさま</rt></ruby>：",
                    "text_en": "- Bank name: - Branch name: - Account number: - Account holder name:"
                },
                {
                    "id": 9,
                    "text_ja": "このたびはお客様にご迷惑をおかけしてしまい、大変申し訳ありませんでした。またのご利用を心よりお待ちしております。",
                    "ruby_html": "このたびはお<ruby>客様<rt>きゃくさま</rt></ruby>にご<ruby>迷惑<rt>めいわく</rt></ruby>をおかけしてしまい、<ruby>大変<rt>たいへん</rt></ruby><ruby>申<rt>もう</rt></ruby>し<ruby>訳<rt>わけ</rt></ruby>ありませんでした。またのご<ruby>利用<rt>りよう</rt></ruby>を<ruby>心<rt>こころ</rt></ruby>よりお<ruby>待<rt>ま</rt></ruby>ちしております。",
                    "text_en": "We truly apologize for causing you such inconvenience, and look forward to serving you again in the future."
                }
            ]
        },
        "footnotes": [
            {
                "label": "注1",
                "term": "返品",
                "meaning_ja": "買った品物を返すこと",
                "meaning_en": "returning purchased goods"
            },
            {
                "label": "注2",
                "term": "不備",
                "meaning_ja": "よくない、不完全なこと",
                "meaning_en": "defect, imperfection"
            },
            {
                "label": "注3",
                "term": "着払い",
                "meaning_ja": "配達の料金を、荷物などを受け取った方が払うこと",
                "meaning_en": "freight collect, receiver pays shipping fee"
            },
            {
                "label": "注4",
                "term": "返金",
                "meaning_ja": "お金を返すこと",
                "meaning_en": "refund, return of money"
            }
        ],
        "vocabulary": [
            {
                "term": "不良品",
                "reading": "ふりょうひん",
                "meaning": "defective item / 残次品",
                "type": "noun"
            },
            {
                "term": "担当",
                "reading": "たんとう",
                "meaning": "being in charge, representative / 负责人",
                "type": "noun"
            },
            {
                "term": "面倒な",
                "reading": "めんどうな",
                "meaning": "bothersome / 麻烦的",
                "type": "na-adjective"
            },
            {
                "term": "返送する",
                "reading": "へんそうする",
                "meaning": "to send back, return / 寄回",
                "type": "verb"
            },
            {
                "term": "到着する",
                "reading": "とうちゃくする",
                "meaning": "to arrive, get to / 到达",
                "type": "verb"
            },
            {
                "term": "対応をする",
                "reading": "たいおうをする",
                "meaning": "to handle, process / 处理",
                "type": "phrase"
            },
            {
                "term": "つきましては",
                "reading": "つきましては",
                "meaning": "in this connection, therefore / 因此",
                "type": "conjunction"
            },
            {
                "term": "振込先口座",
                "reading": "ふりこみさきこうざ",
                "meaning": "bank account for refund / 汇款账户",
                "type": "noun"
            },
            {
                "term": "項目",
                "reading": "こうもく",
                "meaning": "item, field / 项目",
                "type": "noun"
            },
            {
                "term": "返信する",
                "reading": "へんしんする",
                "meaning": "to reply / 回信",
                "type": "verb"
            },
            {
                "term": "名義",
                "reading": "めいぎ",
                "meaning": "name, account holder / 用户名",
                "type": "noun"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-63-1",
                "questionNumber": 1,
                "questionText_ja": "買った商品をどうしてほしいと言っているか。",
                "questionText_en": "What does the shop say they want done with the purchased product?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "そのまま直して使う。",
                        "text_en": "Repair it as is and use it."
                    },
                    {
                        "id": 2,
                        "text_ja": "使わないで捨てる。",
                        "text_en": "Throw it away without using it."
                    },
                    {
                        "id": 3,
                        "text_ja": "○×ショップに送り、払った送料をメールで連絡する。",
                        "text_en": "Send it to OX Shop and report the postage paid by email."
                    },
                    {
                        "id": 4,
                        "text_ja": "着払いで、○×ショップに送る。",
                        "text_en": "Send it to OX Shop via cash on delivery (freight collect)."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "本文に「商品【ABC電気ポット】を、商品着払いにて、ご返送くださいますようお願いいたします」と明確に書かれています。「着払い」とは受取人（ショップ側）が送料を負担して送る方法のことです。したがって 4 が正解です。",
                "explanation_en": "The email clearly asks: 'please return the [ABC Electric Pot] via cash on delivery (着払い).' 'Cash on delivery' means the receiver (the shop) pays shipping charges. Therefore, Option 4 is correct."
            },
            {
                "questionId": "q-63-2",
                "questionNumber": 2,
                "questionText_ja": "お金はどのように戻ってくるか。",
                "questionText_en": "How will the money be refunded?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "商品を送り返さなくても、銀行の口座情報を教えると急にお金が振り込まれる。",
                        "text_en": "Money will be transferred immediately upon giving bank details without sending back the item."
                    },
                    {
                        "id": 2,
                        "text_ja": "商品を送ったことをメールすると、お金が振り込まれる。",
                        "text_en": "Money will be transferred when you email that you sent the product."
                    },
                    {
                        "id": 3,
                        "text_ja": "商品が○×ショップに届いたら、お金が郵便で送られてくる。",
                        "text_en": "Money will be mailed by post when the product arrives at OX Shop."
                    },
                    {
                        "id": 4,
                        "text_ja": "商品が○×ショップに届いたら、伝えておいた口座にお金が振り込まれる。",
                        "text_en": "When the product arrives at OX Shop, money will be transferred to the provided bank account."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "本文に「商品が到着しましたら、ご返金の対応をさせていただきます」「お客様のお振込先口座を教えていただけますでしょうか」とあります。つまり、メールで事前に伝えておいた口座に、返品商品がショップに到着した後に振込が行われます。したがって 4 が正解です。",
                "explanation_en": "The email states: 'Once the item arrives, we will process your refund' and 'could you please provide your bank transfer account information?'. Thus, once the returned goods arrive at the shop, the refund is deposited into the designated account. Therefore, Option 4 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆メール（不良品返品・返金メール）",
            "text_ja": "カスタマーサービスの返信メールでは、「送料負担の区分（着払い＝受取人払い／元払い＝送り主払い）」と「返金のトリガー条件（商品到着後に指定口座へ振込）」の流れを正確に把握することが重要です。",
            "text_en": "In customer service refund emails, understand key commercial terms like '着払い' (receiver-paid postage) vs. '元払い' (sender-paid postage), and trace the refund sequence: customer ships item + replies with account info -> item arrives -> funds transferred.",
            "structureLayout": [
                {
                    "component": "返品手順",
                    "detail": "電気ポットを着払い（ショップ送料負担）で返送",
                    "en": "Return step: Ship electric pot collect on delivery."
                },
                {
                    "component": "返金手順",
                    "detail": "口座情報を返信メールで連絡→商品到着後に振込",
                    "en": "Refund step: Reply with bank info -> refund transferred upon arrival."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "「着払い」（荷物を受け取る側が送料を払う）の意味を必ず覚えておきましょう。",
            "point_en": "Remember that '着払い' (chakubarai) means the recipient pays the shipping charges."
        }
    },
    {
        "id": "dokkai-n3-p4-64",
        "pages": [144, 145],
        "problemNumber": 64,
        "genre": "グラフ",
        "genre_en": "Chart / Graph Analysis",
        "genre_zh": "图表分析",
        "title_ja": "問題64 グラフ（好きな動物調査グラフ）",
        "title_en": "Problem 64: Graph (Favorite Animals Survey Graph)",
        "title_zh": "问题64 图表（最喜爱的动物调查图表）",
        "preReading": {
            "question_ja": "棒グラフや折れ線グラフを見るとき、年代による変化をどう比べますか。",
            "question_en": "When looking at bar or line charts, how do you compare chronological changes over different eras?",
            "question_zh": "查看柱状图或折线图时，你通常如何比较不同年份的变化？"
        },
        "passageInstructions": {
            "instruction_ja": "つぎの文章と右のページのグラフを見て、下の質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
            "instruction_en": "Look at the following text and the graph on the right page, and answer the questions below. Choose the best answer from 1, 2, 3, 4."
        },
        "passage": {
            "sentences": [
                {
                    "id": 1,
                    "text_ja": "右のグラフは、好きな動物について日本人3,600人を対象に行った調査の結果である。1983年と2007年の調査結果のうち、上位1位から8位までを示している。",
                    "ruby_html": "<ruby>右<rt>みぎ</rt></ruby>のグラフは、<ruby>好<rt>す</rt></ruby>きな<ruby>動物<rt>どうぶつ</rt></ruby>について<ruby>日本人<rt>にほんじん</rt></ruby>3,600<ruby>人<rt>にん</rt></ruby>を<ruby>対象<rt>たいしょう</rt></ruby>に<ruby>行<rt>おこな</rt></ruby>った<ruby>調査<rt>ちょうさ</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>である。1983<ruby>年<rt>ねん</rt></ruby>と2007<ruby>年<rt>ねん</rt></ruby>の<ruby>調査結果<rt>ちょうさけっか</rt></ruby>のうち、<ruby>上位<rt>じょうい</rt></ruby>1<ruby>位<rt>い</rt></ruby>から8<ruby>位<rt>い</rt></ruby>までを<ruby>示<rt>しめ</rt></ruby>している。",
                    "text_en": "The graph on the right shows the results of a survey conducted among 3,600 Japanese people regarding their favorite animals. It displays the top 1st through 8th ranked animals in the 1983 and 2007 surveys."
                },
                {
                    "id": 2,
                    "text_ja": "【好きな動物 複数回答結果】（NHK放送文化研究所「日本人の好きなもの」より引用）",
                    "ruby_html": "【<ruby>好<rt>す</rt></ruby>きな<ruby>動物<rt>どうぶつ</rt></ruby> <ruby>複数回答結果<rt>ふくすうかいとうけっか</rt></ruby>】（NHK<ruby>放送文化研究所<rt>ほうそうぶんかけんきゅうじょ</rt></ruby>「<ruby>日本人<rt>にほんじん</rt></ruby>の<ruby>好<rt>す</rt></ruby>きなもの」より<ruby>引用<rt>いんよう</rt></ruby>）",
                    "text_en": "[Favorite Animals - Multiple Responses Allowed] (Source: NHK Broadcasting Culture Research Institute, 'What Japanese People Like')"
                },
                {
                    "id": 3,
                    "text_ja": "犬：1983年約62%、2007年約65%。猫：1983年約39%、2007年約36%。イルカ：1983年約29%、2007年約31%。",
                    "ruby_html": "<ruby>犬<rt>いぬ</rt></ruby>：1983<ruby>年約<rt>ねんやく</rt></ruby>62%、2007<ruby>年約<rt>ねんやく</rt></ruby>65%。<ruby>猫<rt>ねこ</rt></ruby>：1983<ruby>年約<rt>ねんやく</rt></ruby>39%、2007<ruby>年約<rt>ねんやく</rt></ruby>36%。イルカ：1983<ruby>年約<rt>ねんやく</rt></ruby>29%、2007<ruby>年約<rt>ねんやく</rt></ruby>31%。",
                    "text_en": "Dog: 1983 approx 62%, 2007 approx 65%. Cat: 1983 approx 39%, 2007 approx 36%. Dolphin: 1983 approx 29%, 2007 approx 31%."
                },
                {
                    "id": 4,
                    "text_ja": "馬：1983年約39%、2007年約28%。うさぎ：1983年約50%、2007年約27%。パンダ：1983年約58%、2007年約29%。コアラ：1983年約51%、2007年約26%。リス：1983年約50%、2007年約26%。",
                    "ruby_html": "<ruby>馬<rt>うま</rt></ruby>：1983<ruby>年約<rt>ねんやく</rt></ruby>39%、2007<ruby>年約<rt>ねんやく</rt></ruby>28%。うさぎ：1983<ruby>年約<rt>ねんやく</rt></ruby>50%、2007<ruby>年約<rt>ねんやく</rt></ruby>27%。パンダ：1983<ruby>年約<rt>ねんやく</rt></ruby>58%、2007<ruby>年約<rt>ねんやく</rt></ruby>29%。コアラ：1983<ruby>年約<rt>ねんやく</rt></ruby>51%、2007<ruby>年約<rt>ねんやく</rt></ruby>26%。リス：1983<ruby>年約<rt>ねんやく</rt></ruby>50%、2007<ruby>年約<rt>ねんやく</rt></ruby>26%。",
                    "text_en": "Horse: 1983 ~39%, 2007 ~28%. Rabbit: 1983 ~50%, 2007 ~27%. Panda: 1983 ~58%, 2007 ~29%. Koala: 1983 ~51%, 2007 ~26%. Squirrel: 1983 ~50%, 2007 ~26%."
                }
            ]
        },
        "footnotes": [],
        "vocabulary": [
            {
                "term": "全国",
                "reading": "ぜんこく",
                "meaning": "whole country, nationwide / 全国",
                "type": "noun"
            },
            {
                "term": "対象",
                "reading": "たいしょう",
                "meaning": "[as] subjects, target audience / 对象",
                "type": "noun"
            },
            {
                "term": "調査",
                "reading": "ちょうさ",
                "meaning": "investigation, survey / 调查",
                "type": "noun"
            },
            {
                "term": "結果",
                "reading": "けっか",
                "meaning": "result, outcome / 结果",
                "type": "noun"
            },
            {
                "term": "上位",
                "reading": "じょうい",
                "meaning": "the top ~, the leading ~ / 排位靠前",
                "type": "noun"
            },
            {
                "term": "示す",
                "reading": "しめす",
                "meaning": "to indicate, show / 显示",
                "type": "verb"
            },
            {
                "term": "差",
                "reading": "さ",
                "meaning": "difference, gap / 差异",
                "type": "noun"
            },
            {
                "term": "複数回答",
                "reading": "ふくすうかいとう",
                "meaning": "multiple responses allowed / 多项选择题",
                "type": "noun"
            }
        ],
        "comprehensionQuestions": [
            {
                "questionId": "q-64-1",
                "questionNumber": 1,
                "questionText_ja": "1983年と2007年で一番大きな差があらわれた動物はどれか。",
                "questionText_en": "Which animal showed the largest difference between 1983 and 2007?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "犬",
                        "text_en": "Dog"
                    },
                    {
                        "id": 2,
                        "text_ja": "パンダ",
                        "text_en": "Panda"
                    },
                    {
                        "id": 3,
                        "text_ja": "馬",
                        "text_en": "Horse"
                    },
                    {
                        "id": 4,
                        "text_ja": "うさぎ",
                        "text_en": "Rabbit"
                    }
                ],
                "correctAnswer": 2,
                "explanation_ja": "グラフの2本の棒の高さの差を比較します。\n・犬：62%と65%で差は約3%\n・パンダ：58%から29%へと約29%の減少（選択肢の中で最大の差）\n・馬：39%から28%へと約11%の差\n・うさぎ：50%から27%へと約23%の差\nしたがって、最も大きな差があらわれた動物は「パンダ」です。正解は 2 です。",
                "explanation_en": "Compare the height differences between the two bars for each animal:\n- Dog: 62% vs 65%, diff is ~3%\n- Panda: 58% down to 29%, diff is ~29% (largest difference among options)\n- Horse: 39% down to 28%, diff is ~11%\n- Rabbit: 50% down to 27%, diff is ~23%\nTherefore, the animal exhibiting the biggest difference is the panda. Option 2 is correct."
            },
            {
                "questionId": "q-64-2",
                "questionNumber": 2,
                "questionText_ja": "グラフについて正しく述べているのはどれか。",
                "questionText_en": "Which statement correctly describes the graph?",
                "options": [
                    {
                        "id": 1,
                        "text_ja": "ねこは1983年と2007年で大きな差がある。",
                        "text_en": "Cats show a large difference between 1983 and 2007."
                    },
                    {
                        "id": 2,
                        "text_ja": "うさぎは2007年の調査では3位である。",
                        "text_en": "Rabbits ranked 3rd in the 2007 survey."
                    },
                    {
                        "id": 3,
                        "text_ja": "パンダは1983年の調査では1位である。",
                        "text_en": "Pandas ranked 1st in the 1983 survey."
                    },
                    {
                        "id": 4,
                        "text_ja": "コアラは2007年の調査では1983年より減少している。",
                        "text_en": "Koalas decreased in the 2007 survey compared to 1983."
                    }
                ],
                "correctAnswer": 4,
                "explanation_ja": "各選択肢を検討します。\n1: ねこは39%と36%で差はわずか3%であり、「大きな差がある」は不適切です。\n2: 2007年の3位はイルカ（約31%）です。うさぎ（約27%）は6位前後です。\n3: 1983年の1位は犬（約62%）です。パンダ（約58%）は2位です。\n4: コアラは1983年の約51%から2007年の約26%へと大きく減少しています。記述は完全に正しいです。\nしたがって 4 が正解です。",
                "explanation_en": "Evaluating each option:\nOption 1: Cats only changed from 39% to 36% (~3% diff), not a large difference.\nOption 2: In 2007, 3rd was the dolphin (~31%). Rabbits (~27%) ranked around 6th.\nOption 3: In 1983, 1st was the dog (~62%), with panda in 2nd (~58%).\nOption 4: Koalas dropped substantially from ~51% in 1983 to ~26% in 2007, meaning they clearly decreased (減少している). This statement is completely accurate. Therefore, Option 4 is correct."
            }
        ],
        "commentary": {
            "title_ja": "解説 ◆グラフ（好きな動物調査グラフ）",
            "text_ja": "グラフ・図表読解では、①凡例（どの色の棒がどの年代か）、②縦軸の単位（％）、③横軸の項目と順位、④差分（増加・減少・変化量）を素早く視覚的に照合します。「1位」「差が最大」「減少している」といったキーワードをグラフから正確に拾いましょう。",
            "text_en": "Graph and chart questions require four verification steps: (1) Legend (which bar represents which survey year), (2) Y-axis scale (percentage), (3) Category rankings on X-axis, and (4) Direction/magnitude of change (increase, decrease, delta). Focus on keywords like '1st place', 'maximum difference', and 'decrease'.",
            "structureLayout": [
                {
                    "component": "凡例と軸",
                    "detail": "黒棒＝1983年、灰色棒＝2007年。縦軸＝％（0〜70）",
                    "en": "Legend: Dark = 1983, Grey = 2007. Y-axis: % (0 to 70)."
                },
                {
                    "component": "変化量比較",
                    "detail": "パンダが58%→29%と最大の落ち込み（差が一番大きい）",
                    "en": "Delta check: Panda dropped by ~29%, the largest gap."
                },
                {
                    "component": "増減の判定",
                    "detail": "コアラは51%→26%と明確に減少している",
                    "en": "Trend check: Koala decreased from ~51% to ~26%."
                }
            ]
        },
        "testAdvice": {
            "point_ja": "1位は常に「犬」（62%／65%）です。「パンダが1位」などの引っかけに惑わされないように！",
            "point_en": "Dogs are consistently #1 in both years (~62% and ~65%); don't be tricked by claims of other animals ranking first."
        }
    }
]
