import json
import os
import sys

# Paths
reading_dir = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\reading"
passages_file = os.path.join(reading_dir, "passages.json")
out_file = os.path.join(reading_dir, "part1_foundation.json")

with open(passages_file, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

existing_lessons = existing_data["lessons"]
print(f"Loaded {len(existing_lessons)} existing lessons.")

# Define Lesson 7 (Pages 26, 27)
lesson_07 = {
    "id": "dokkai-n3-l07",
    "pages": [26, 27],
    "skillNumber": 7,
    "skillCode": "reading_speed_7",
    "problemNumber": 11,
    "title_ja": "指示語を意識する",
    "title_en": "Paying Attention to Demonstrative Terms",
    "title_zh": "注意指示词",
    "passageTitle_ja": "コーヒーと活性酸素",
    "passageTitle_en": "Coffee and Active Oxygen",
    "readingStrategy": {
        "rule_ja": "文章の中の指示語 ⇒「これ・それ・あれ／この・その・あの／…」すぐ前の文の中に書かれていることを指すことが多いが、後ろにあるものを指すこともある。その場合は「こ（これ・この〜など）」が使われることが多い。",
        "rule_en": "Demonstrative terms in a text (これ・それ・あれ / この・その・あの / ...) most frequently refer to what was stated in the immediately preceding sentence, but they can also refer to something that follows. When referring to following content, the 'こ' series (これ, この〜, etc.) is commonly used.",
        "rule_zh": "文章中的指示词 ⇒「这・那／这个・那个／…」多数情况下指代紧邻的前文中写到的内容，但有时也会指代后文的内容。这种情况下多使用「こ」系列（これ、この〜等）。",
        "keyPoints": [
            {
                "point_ja": "Ⅰ. 直前の内容を指す指示語",
                "point_en": "I. Demonstratives pointing to preceding content",
                "example_ja": "朝一杯のコーヒー。 ↑ 私は「これ」がないと目が覚めない。",
                "example_en": "A cup of coffee in the morning. ↑ Without 'this', I cannot wake up."
            },
            {
                "point_ja": "Ⅱ. 後ろの内容を指す指示語（こ系列）",
                "point_en": "II. Demonstratives pointing forward to following content (Ko-series)",
                "example_ja": "その仕組みは、「こう」である。 ↓ 太陽の光にあたると、人間の体内で「活性酸素」と呼ばれる物質ができる…。",
                "example_en": "The mechanism is 'as follows': ↓ When exposed to sunlight, a substance called 'active oxygen' is produced inside the human body..."
            }
        ]
    },
    "preReading": {
        "question_ja": "「朝一杯のコーヒー。私はこれがないと目が覚めない。」の「これ」は何をさしますか。",
        "question_en": "In the sentence 'A cup of coffee in the morning. Without this (これ), I cannot wake up', what does 'これ' refer to?",
        "answer_ja": "朝一杯のコーヒー",
        "answer_en": "A cup of coffee in the morning",
        "note_ja": "答えはこのページの下にあります。（答え：朝一杯のコーヒー）",
        "note_en": "The answer is at the bottom of the page. (Answer: A cup of coffee in the morning)"
    },
    "passage": {
        "sentences": [
            {
                "id": 1,
                "text_ja": "コーヒーを多く飲む人ほど、肌のしみができにくいという研究結果がある。",
                "ruby_html": "コーヒーを<ruby>多<rt>おお</rt></ruby>く<ruby>飲<rt>の</rt></ruby>む<ruby>人<rt>ひと</rt></ruby>ほど、<ruby>肌<rt>はだ</rt></ruby>のしみ<sup>(注1)</sup>ができにくいという<ruby>研究結果<rt>けんきゅうけっか</rt></ruby>がある。",
                "text_en": "Research results show that the more coffee people drink, the less likely they are to develop skin blemishes."
            },
            {
                "id": 2,
                "text_ja": "なぜコーヒーにそのような効果があるのだろうか。",
                "ruby_html": "なぜコーヒーに<span class=\"target-pointer\">そのような</span><ruby>効果<rt>こうか</rt></ruby>があるのだろうか。",
                "text_en": "Why does coffee have such an effect?"
            },
            {
                "id": 3,
                "text_ja": "その仕組みは、こうである。",
                "ruby_html": "その<ruby>仕組<rt>しく</rt></ruby>みは、<span class=\"target-pointer\">こう</span>である。",
                "text_en": "The mechanism is as follows:"
            },
            {
                "id": 4,
                "text_ja": "太陽の光にあたると、人間の体内で「活性酸素」と呼ばれる物質ができる。",
                "ruby_html": "<ruby>太陽<rt>たいよう</rt></ruby>の<ruby>光<rt>ひかり</rt></ruby>にあたると、<ruby>人間<rt>にんげん</rt></ruby>の<ruby>体内<rt>たいない</rt></ruby>で「<ruby>活性酸素<rt>かっせいさんそ</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>ばれる<ruby>物質<rt>ぶっしつ</rt></ruby>ができる。",
                "text_en": "When exposed to sunlight, a substance called 'active oxygen' is produced inside the human body."
            },
            {
                "id": 5,
                "text_ja": "これは、しみの原因となる物質「メラニン」を増やしてしまう。",
                "ruby_html": "<span class=\"target-pointer\">これ</span>は、しみの<ruby>原因<rt>げんいん</rt></ruby>となる<ruby>物質<rt>ぶっしつ</rt></ruby>「メラニン」を<ruby>増<rt>ふ</rt></ruby>やしてしまう。",
                "text_en": "This ends up increasing 'melanin', the substance that causes blemishes."
            },
            {
                "id": 6,
                "text_ja": "しかし、コーヒーにたくさん含まれる「ポリフェノール」という物質は活性酸素の働きを小さくしてくれるという。",
                "ruby_html": "しかし、コーヒーにたくさん<ruby>含<rt>ふく</rt></ruby>まれる「ポリフェノール」という<ruby>物質<rt>ぶっしつ</rt></ruby>は<ruby>活性酸素<rt>かっせいさんそ</rt></ruby>の<ruby>働<rt>はたら</rt></ruby>きを<ruby>小<rt>ちい</rt></ruby>さくしてくれるという。",
                "text_en": "However, it is said that a substance called 'polyphenol', which is abundantly contained in coffee, diminishes the action of active oxygen."
            },
            {
                "id": 7,
                "text_ja": "それで、コーヒーを飲む人はしみができにくいというわけだ。",
                "ruby_html": "それで、コーヒーを<ruby>飲<rt>の</rt></ruby>む<ruby>人<rt>ひと</rt></ruby>はしみができにくいというわけだ。",
                "text_en": "That is why people who drink coffee do not easily develop skin blemishes."
            },
            {
                "id": 8,
                "text_ja": "ポリフェノールをたくさん含むコーヒーは、美容にいい飲み物だと言えそうだ。",
                "ruby_html": "ポリフェノールをたくさん<ruby>含<rt>ふく</rt></ruby>むコーヒーは、<ruby>美容<rt>びよう</rt></ruby>にいい<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>だと<ruby>言<rt>い</rt></ruby>えそうだ。",
                "text_en": "It could be said that coffee, containing abundant polyphenols, is a drink that is good for beauty and skin health."
            }
        ]
    },
    "footnotes": [
        {
            "index": 1,
            "term_ja": "しみ",
            "reading": "しみ",
            "definition_ja": "顔や手などにできる茶色い点",
            "definition_en": "Skin blemishes / spots: small brown marks that form on faces or hands."
        }
    ],
    "vocabulary": [
        { "term": "肌", "reading": "はだ", "meaning": "skin", "type": "noun" },
        { "term": "研究結果", "reading": "けんきゅうけっか", "meaning": "research results, study findings", "type": "noun" },
        { "term": "効果", "reading": "こうか", "meaning": "effect, efficacy", "type": "noun" },
        { "term": "仕組み", "reading": "しくみ", "meaning": "mechanism, workings, structure", "type": "noun" },
        { "term": "活性酸素", "reading": "かっせいさんそ", "meaning": "active oxygen, reactive oxygen species", "type": "noun" },
        { "term": "物質", "reading": "ぶっしつ", "meaning": "substance, material", "type": "noun" },
        { "term": "原因", "reading": "げんいん", "meaning": "cause, origin", "type": "noun" },
        { "term": "増やす", "reading": "ふやす", "meaning": "to increase, multiply", "type": "transitive verb" },
        { "term": "含まれる", "reading": "ふくまれる", "meaning": "to be contained, included", "type": "passive verb" },
        { "term": "働き", "reading": "はたらき", "meaning": "function, action, operation", "type": "noun" },
        { "term": "美容", "reading": "びよう", "meaning": "beauty, cosmetics, skin aesthetics", "type": "noun" }
    ],
    "comprehensionQuestions": [
        {
            "questionId": "q-11-1",
            "questionNumber": 1,
            "questionText_ja": "この文章によると、活性酸素とはどんな物質か。",
            "questionText_en": "According to this passage, what kind of substance is active oxygen?",
            "options": [
                { "id": 1, "text_ja": "しみをできにくくする物質", "text_en": "A substance that prevents blemishes from forming" },
                { "id": 2, "text_ja": "ポリフェノールを増やす物質", "text_en": "A substance that increases polyphenols" },
                { "id": 3, "text_ja": "メラニンを増やす物質", "text_en": "A substance that increases melanin" },
                { "id": 4, "text_ja": "コーヒーの中に多く含まれる物質", "text_en": "A substance contained in large amounts in coffee" }
            ],
            "correctAnswer": 3,
            "explanation_ja": "第2段落に「太陽の光にあたると、人間の体内で『活性酸素』と呼ばれる物質ができる。これは、しみの原因となる物質『メラニン』を増やしてしまう。」と書かれています。指示語「これ」は活性酸素を指しており、メラニンを増やす物質であることが説明されています。したがって正解は 3 です。（選択肢1はポリフェノール、選択肢2は本文に記述がなく、選択肢4はポリフェノールの説明です。）",
            "explanation_en": "Paragraph 2 states: 'When exposed to sunlight, a substance called active oxygen is produced inside the human body. This (これ) increases melanin, which causes blemishes.' The demonstrative 'これ' refers back to 'active oxygen', confirming that it increases melanin. Therefore, Option 3 is correct. (Option 1 describes polyphenols; Option 2 is unmentioned; Option 4 describes polyphenols in coffee.)",
            "techniqueFocus": "Demonstrative tracking: Identify that 'これ' refers to '活性酸素' in the preceding sentence, and connect it directly to the predicate 'メラニンを増やしてしまう'."
        }
    ],
    "drills": [
        {
            "drillId": "drill-27-1",
            "title_ja": "練習：指示語が何を指すか書きなさい",
            "title_en": "Exercise: Identify What the Demonstratives Refer To",
            "instruction_ja": "下の [ ] の指示語が何を指すか書きなさい。",
            "instruction_en": "Identify what each demonstrative in brackets [ ] refers to.",
            "items": [
                {
                    "itemId": 1,
                    "demonstrative": "そのような",
                    "fullSentence_ja": "コーヒーを多く飲む人ほど、肌のしみができにくいという研究結果がある。なぜコーヒーに [そのような] 効果があるのだろうか。",
                    "fullSentence_ruby": "コーヒーを<ruby>多<rt>おお</rt></ruby>く<ruby>飲<rt>の</rt></ruby>む<ruby>人<rt>ひと</rt></ruby>ほど、<ruby>肌<rt>はだ</rt></ruby>のしみができにくいという<ruby>研究結果<rt>けんきゅうけっか</rt></ruby>がある。なぜコーヒーに [そのような] <ruby>効果<rt>こうか</rt></ruby>があるのだろうか。",
                    "fullSentence_en": "Research results show that the more coffee people drink, the less likely they are to develop skin blemishes. Why does coffee have such an effect?",
                    "targetReferent_ja": "肌のしみができにくい（という）",
                    "completedSentence_ja": "なぜコーヒーに [肌のしみができにくい（という）] 効果があるのだろうか。",
                    "completedSentence_en": "Why does coffee have the effect of [making skin blemishes less prone to form]?",
                    "direction": "backward",
                    "explanation_en": "'そのような' points back to the result stated right beforehand: '肌のしみができにくい'."
                },
                {
                    "itemId": 2,
                    "demonstrative": "これ",
                    "fullSentence_ja": "トマトにはリコピンという物質が含まれているが、[これ] はガンの予防に効果があると言われている。",
                    "fullSentence_ruby": "トマトにはリコピンという<ruby>物質<rt>ぶっしつ</rt></ruby>が<ruby>含<rt>ふく</rt></ruby>まれているが、[これ] はガンの<ruby>予防<rt>よぼう</rt></ruby>に<ruby>効果<rt>こうか</rt></ruby>があると言われている。",
                    "fullSentence_en": "Tomatoes contain a substance called lycopene, and this is said to be effective in cancer prevention.",
                    "targetReferent_ja": "リコピン",
                    "completedSentence_ja": "[リコピン] は ガンの予防に効果があると言われている。",
                    "completedSentence_en": "[Lycopene] is said to be effective in cancer prevention.",
                    "direction": "backward",
                    "explanation_en": "'これ' refers back to 'リコピン' mentioned in the first half of the sentence."
                },
                {
                    "itemId": 3,
                    "demonstrative": "こう",
                    "fullSentence_ja": "初めて宇宙から地球を見て、彼は [こう] 言った。「地球は青かった。」",
                    "fullSentence_ruby": "<ruby>初<rt>はじ</rt></ruby>めて<ruby>宇宙<rt>うちゅう</rt></ruby>から<ruby>地球<rt>ちきゅう</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>彼<rt>かれ</rt></ruby>は [こう] <ruby>言<rt>い</rt></ruby>った。「<ruby>地球<rt>ちきゅう</rt></ruby>は<ruby>青<rt>あお</rt></ruby>かった。」",
                    "fullSentence_en": "Looking at Earth from outer space for the first time, he said like this: 'The Earth was blue.'",
                    "targetReferent_ja": "「地球は青かった。」（と）",
                    "completedSentence_ja": "初めて宇宙から地球を見て、彼は [「地球は青かった。」と] 言った。",
                    "completedSentence_en": "Looking at Earth from outer space for the first time, he said ['The Earth was blue'].",
                    "direction": "forward",
                    "explanation_en": "'こう' is a forward-pointing demonstrative pointing directly to the quoted statement that immediately follows: '地球は青かった'."
                }
            ]
        }
    ]
}

# Define Lesson 8 (Pages 28, 29)
lesson_08 = {
    "id": "dokkai-n3-l08",
    "pages": [28, 29],
    "skillNumber": 8,
    "skillCode": "reading_speed_8",
    "problemNumber": 12,
    "title_ja": "文章の構造を理解する",
    "title_en": "Understanding Text Structure",
    "title_zh": "理解文章结构",
    "passageTitle_ja": "冷房と体調管理",
    "passageTitle_en": "Air Conditioning and Health Management",
    "readingStrategy": {
        "rule_ja": "それぞれの段落には役割がある。それぞれの段落で一番言いたいことを見つけ、段落の役割を考えよう。段落の役割を理解すると、段落同士の関係がわかり、その文章の構造が理解できる。",
        "rule_en": "Each paragraph has its own function. Find the primary point the writer is trying to convey in each paragraph, and consider the paragraph's specific role. Understanding paragraph roles illuminates the relationships between paragraphs and clarifies the overall structure of the text.",
        "rule_zh": "每个段落都有其作用。找到各段最想表达的意思，思考段落的作用吧。理解了段落所起的作用之后就会搞清楚段落之间的关系，从而理解文章的结构。",
        "keyPoints": [
            {
                "point_ja": "段落の4つの典型的な役割",
                "point_en": "Four typical paragraph roles",
                "roles": [
                    { "name_ja": "話題の提出", "name_en": "Topic proposal", "name_zh": "提出话题" },
                    { "name_ja": "Aへの反対", "name_en": "Counter-argument to A", "name_zh": "对A的反对/转折" },
                    { "name_ja": "追加情報 / 具体例", "name_en": "Additional information / Specific example", "name_zh": "补充信息 / 具体例子" },
                    { "name_ja": "まとめ", "name_en": "Summary / Conclusion", "name_zh": "总结" }
                ]
            }
        ]
    },
    "preReading": {
        "question_ja": "「第1段落が『冷房は素晴らしい技術だ』という内容で始まる文章があります。その次の段落が『しかし』で始まっていたら、その文章全体の内容はどんなものだと考えられますか。\nA 冷房のよい点だけを述べる。\nB 冷房のよくない点も述べる。」",
        "question_en": "There is an article whose first paragraph begins with 'Air conditioning is a wonderful technology.' If the next paragraph starts with 'However' (しかし), what do you expect the overall content of the text to be?\nA: Discusses only the positive points of air conditioning.\nB: Also discusses the negative points of air conditioning.",
        "answer": "B",
        "explanation_ja": "「しかし」は逆接の接続詞なので、前の段落で述べたよい点とは反対の「よくない点」も取り上げられます。（答え：B）",
        "explanation_en": "Because 'しかし' (however) is a contrastive conjunction, the text will introduce negative aspects in contrast to the merits discussed earlier. (Answer: B)"
    },
    "passage": {
        "sentences": [
            {
                "id": 1,
                "paragraph": "A",
                "text_ja": "冷房という技術は本当に素晴らしく、私たちは暑い夏に冷房のおかげでいろいろ助けられている。",
                "ruby_html": "<ruby>冷房<rt>れいぼう</rt></ruby>という<ruby>技術<rt>ぎじゅつ</rt></ruby>は<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>素晴<rt>すば</rt></ruby>らしく、<ruby>私<rt>わたし</rt></ruby>たちは<ruby>暑<rt>あつ</rt></ruby>い<ruby>夏<rt>なつ</rt></ruby>に<ruby>冷房<rt>れいぼう</rt></ruby>のおかげでいろいろ<ruby>助<rt>たす</rt></ruby>けられている。",
                "text_en": "The technology known as air conditioning is truly wonderful, and we are helped in many ways thanks to air conditioning during hot summers."
            },
            {
                "id": 2,
                "paragraph": "A",
                "text_ja": "例えば、勉強でも仕事でも、暑い中、汗をかきながらやるよりも、涼しいところでやったほうがずっと快適だ。",
                "ruby_html": "<ruby>例<rt>たと</rt></ruby>えば、<ruby>勉強<rt>べんきょう</rt></ruby>でも<ruby>仕事<rt>しごと</rt></ruby>でも、<ruby>暑<rt>あつ</rt></ruby>い<ruby>中<rt>なか</rt></ruby>、<ruby>汗<rt>あせ</rt></ruby>をかきながらやるよりも、<ruby>涼<rt>すず</rt></ruby>しいところでやったほうがずっと<ruby>快適<rt>かいてき</rt></ruby>だ。",
                "text_en": "For instance, whether studying or working, doing it in a cool place is far more comfortable than sweating in the heat."
            },
            {
                "id": 3,
                "paragraph": "B",
                "text_ja": "しかし、よいことばかりではない。",
                "ruby_html": "<strong>しかし</strong>、よいことばかりではない。",
                "text_en": "However, it is not all good things."
            },
            {
                "id": 4,
                "paragraph": "B",
                "text_ja": "実は、人の体温を調節する神経は5℃以上の急な変化を繰り返すことに弱いそうだ。",
                "ruby_html": "<ruby>実<rt>じつ</rt></ruby>は、<ruby>人<rt>ひと</rt></ruby>の<ruby>体温<rt>たいおん</rt></ruby>を<ruby>調節<rt>ちょうせつ</rt></ruby>する<ruby>神経<rt>しんけい</rt></ruby>は5℃<ruby>以上<rt>いじょう</rt></ruby>の<ruby>急<rt>きゅう</rt></ruby>な<ruby>変化<rt>へんか</rt></ruby>を<ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>すことに<ruby>弱<rt>よわ</rt></ruby>いそうだ。",
                "text_en": "In fact, it is said that the nerves regulating human body temperature are vulnerable to repeated abrupt changes of 5°C or more."
            },
            {
                "id": 5,
                "paragraph": "B",
                "text_ja": "夏の室外と室内の温度差は10℃以上になることもよくあり、そこを出たり入ったりしているうちに、この体温を調節する神経がうまく働かなくなることがあるのだ。",
                "ruby_html": "<ruby>夏<rt>なつ</rt></ruby>の<ruby>室外<rt>しつがい</rt></ruby>と<ruby>室内<rt>しつない</rt></ruby>の<ruby>温度差<rt>おんどさ</rt></ruby>は10℃<ruby>以上<rt>いじょう</rt></ruby>になることもよくあり、そこを<ruby>出<rt>で</rt></ruby>たり<ruby>入<rt>はい</rt></ruby>ったりしているうちに、この<ruby>体温<rt>たいおん</rt></ruby>を<ruby>調節<rt>ちょうせつ</rt></ruby>する<ruby>神経<rt>しんけい</rt></ruby>がうまく<ruby>働<rt>はたら</rt></ruby>かなくなることがあるのだ。",
                "text_en": "In summer, the temperature difference between indoors and outdoors often reaches 10°C or more, and as one goes in and out, these temperature-regulating nerves can malfunction."
            },
            {
                "id": 6,
                "paragraph": "B",
                "text_ja": "その結果、疲れやすい、頭が痛いなど、さまざまな症状があらわれる。",
                "ruby_html": "その<ruby>結果<rt>けっか</rt></ruby>、<ruby>疲<rt>つか</rt></ruby>れやすい、<ruby>頭<rt>あたま</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いなど、さまざまな<ruby>症状<rt>しょうじょう</rt></ruby>があらわれる。",
                "text_en": "As a result, various symptoms appear, such as tiring easily and suffering from headaches."
            },
            {
                "id": 7,
                "paragraph": "C",
                "text_ja": "そうなると、さらに悪いことが起きる。",
                "ruby_html": "そうなると、さらに<ruby>悪<rt>わる</rt></ruby>いことが<ruby>起<rt>お</rt></ruby>きる。",
                "text_en": "When that occurs, even worse things happen."
            },
            {
                "id": 8,
                "paragraph": "C",
                "text_ja": "どこへ行っても冷房があるために、どんどん具合が悪くなったり、夏が終わるまで治らないということもあるのだ。",
                "ruby_html": "どこへ<ruby>行<rt>い</rt></ruby>っても<ruby>冷房<rt>れいぼう</rt></ruby>があるために、どんどん<ruby>具合<rt>ぐあい</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>くなったり、<ruby>夏<rt>なつ</rt></ruby>が<ruby>終<rt>お</rt></ruby>わるまで<ruby>治<rt>なお</rt></ruby>らないということもあるのだ。",
                "text_en": "Because there is air conditioning wherever one goes, one's condition can deteriorate steadily, and sometimes does not recover until summer is over."
            },
            {
                "id": 9,
                "paragraph": "C",
                "text_ja": "それでは仕事や勉強どころか、遊びも楽しめないだろう。",
                "ruby_html": "それでは<ruby>仕事<rt>しごと</rt></ruby>や<ruby>勉強<rt>べんきょう</rt></ruby>どころか、<ruby>遊<rt>あそ</rt></ruby>びも<ruby>楽<rt>たの</rt></ruby>しめないだろう。",
                "text_en": "Under those circumstances, far from working or studying, one cannot even enjoy recreation."
            },
            {
                "id": 10,
                "paragraph": "D",
                "text_ja": "このように、冷房は暑い夏を快適に過ごすための優れた技術ではあるが、思わぬ体調不良の原因にもなりうる。",
                "ruby_html": "<span class=\"discourse-marker\">このように</span>、<ruby>冷房<rt>れいぼう</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>い<ruby>夏<rt>なつ</rt></ruby>を<ruby>快適<rt>かいてき</rt></ruby>に<ruby>過<rt>す</rt></ruby>ごすための<ruby>優<rt>すぐ</rt></ruby>れた<ruby>技術<rt>ぎじゅつ</rt></ruby>ではあるが、<ruby>思<rt>おも</rt></ruby>わぬ<ruby>体調不良<rt>たいちょうふりょう</rt></ruby>の<ruby>原因<rt>げんいん</rt></ruby>にもなりうる。",
                "text_en": "In this way, while air conditioning is an excellent technology for spending hot summers comfortably, it can also become a cause of unexpected illness."
            },
            {
                "id": 11,
                "paragraph": "D",
                "text_ja": "冷房の技術はありがたいものだが、大事なことは、その技術を上手に使うということだろう。",
                "ruby_html": "<ruby>冷房<rt>れいぼう</rt></ruby>の<ruby>技術<rt>ぎじゅつ</rt></ruby>はありがたいものだが、<span class=\"target-question\"><strong><ruby>大事<rt>だいじ</rt></ruby>なことは、その<ruby>技術<rt>ぎじゅつ</rt></ruby>を<ruby>上手<rt>じょうず</rt></ruby>に<ruby>使<rt>つか</rt></ruby>うということだろう</strong></span>。",
                "text_en": "Although air conditioning technology is something to appreciate, the crucial thing is to use that technology skillfully."
            }
        ]
    },
    "vocabulary": [
        { "term": "冷房", "reading": "れいぼう", "meaning": "air conditioning, cooling", "type": "noun" },
        { "term": "快適", "reading": "かいてき", "meaning": "comfortable, agreeable", "type": "na-adjective" },
        { "term": "体温", "reading": "たいおん", "meaning": "body temperature", "type": "noun" },
        { "term": "調節する", "reading": "ちょうせつする", "meaning": "to regulate, adjust", "type": "noun/suru-verb" },
        { "term": "神経", "reading": "しんけい", "meaning": "nerves, nervous system", "type": "noun" },
        { "term": "室外", "reading": "しつがい", "meaning": "outdoors, outside room", "type": "noun" },
        { "term": "室内", "reading": "しつない", "meaning": "indoors, inside room", "type": "noun" },
        { "term": "温度差", "reading": "おんどさ", "meaning": "temperature difference", "type": "noun" },
        { "term": "症状", "reading": "しょうじょう", "meaning": "symptoms, condition", "type": "noun" },
        { "term": "具合", "reading": "ぐあい", "meaning": "health condition, state", "type": "noun" },
        { "term": "治る", "reading": "なおる", "meaning": "to heal, get better, recover", "type": "intransitive verb" },
        { "term": "体調不良", "reading": "たいちょうふりょう", "meaning": "poor physical health, ailment", "type": "noun" },
        { "term": "思わぬ", "reading": "おもわぬ", "meaning": "unexpected, unforeseen", "type": "pre-noun adjectival" },
        { "term": "どころか", "reading": "どころか", "meaning": "far from, let alone", "type": "particle" }
    ],
    "comprehensionQuestions": [
        {
            "questionId": "q-12-1",
            "questionNumber": 1,
            "questionText_ja": "この文章で一番言いたいことは何か。",
            "questionText_en": "What is the author's primary argument in this text?",
            "options": [
                { "id": 1, "text_ja": "冷房は素晴らしい技術なのでどんどん使用するべきだ。", "text_en": "Air conditioning is a wonderful technology, so it should be used extensively." },
                { "id": 2, "text_ja": "室外と室内の温度差が10℃以上あると、快適でほっとする。", "text_en": "When the temperature difference between inside and outside is 10°C or more, it is comfortable and relieving." },
                { "id": 3, "text_ja": "冷房で体をこわしてしまうこともあるので、うまく使う必要がある。", "text_en": "Because air conditioning can also harm health, it is necessary to use it skillfully." },
                { "id": 4, "text_ja": "冷房を使うと体温を調節することができなくなるので、使わないほうがいい。", "text_en": "Because air conditioning prevents body temperature regulation, it is better not to use it at all." }
            ],
            "correctAnswer": 3,
            "explanation_ja": "最後の段落Dで筆者は「冷房は暑い夏を快適に過ごすための優れた技術ではあるが、思わぬ体調不良の原因にもなりうる。冷房の技術はありがたいものだが、大事なことは、その技術を上手に使うということだろう。」と述べています。冷房のメリットと健康被害のリスクの両面を挙げたうえで「上手に使う必要がある」と結論づけているため、正解は 3 です。（選択肢1はデメリットを無視しており、選択肢2は10℃以上の温度差が体調不良を招く本文と矛盾し、選択肢4は冷房の全面否定となり筆者の主張と異なります。）",
            "explanation_en": "In the concluding paragraph D, the author summarizes: 'While air conditioning is an outstanding technology for spending hot summers comfortably, it can also cause unexpected poor health... What is vital is using that technology skillfully.' This directly corresponds to Option 3. Option 1 ignores negative consequences, Option 2 misconstrues temperature difference, and Option 4 erroneously advises not using AC at all.",
            "techniqueFocus": "Discourse structure analysis: Paragraph D begins with 'このように' (In this way), presenting the concluding synthesis that AC must be used skillfully."
        }
    ],
    "drills": [
        {
            "drillId": "drill-29-1",
            "title_ja": "練習1：段落の要点把握",
            "title_en": "Exercise 1: Identifying the Main Point of Each Paragraph",
            "instruction_ja": "左の文章のA、B、C、Dの段落でそれぞれ一番言いたいことは何か、a、bから選びなさい。",
            "instruction_en": "For each paragraph A, B, C, and D, choose the statement (a or b) that best expresses what the author wants to convey most.",
            "items": [
                {
                    "paragraph": "A",
                    "options": [
                        { "key": "a", "text_ja": "冷房の技術はいいものだ。", "text_en": "Air-conditioning technology is a good thing." },
                        { "key": "b", "text_ja": "冷房がないと勉強も仕事もできない。", "text_en": "Without air conditioning, one cannot study or work." }
                    ],
                    "correctKey": "a",
                    "explanation_en": "Paragraph A states: '冷房という技術は本当に素晴らしく...' (Air conditioning is truly wonderful)."
                },
                {
                    "paragraph": "B",
                    "options": [
                        { "key": "a", "text_ja": "冷房が原因のよくないことはほとんどない。", "text_en": "Bad things caused by air conditioning hardly ever occur." },
                        { "key": "b", "text_ja": "冷房が原因でよくないことが起きることもある。", "text_en": "Bad things caused by air conditioning can also happen." }
                    ],
                    "correctKey": "b",
                    "explanation_en": "Paragraph B states: 'しかし、よいことばかりではない...' (However, it is not all good things)."
                },
                {
                    "paragraph": "C",
                    "options": [
                        { "key": "a", "text_ja": "冷房で体をこわすとさらにそれが深刻化して長引くこともある。", "text_en": "When harmed by air conditioning, it can worsen and become prolonged." },
                        { "key": "b", "text_ja": "冷房で体調を悪くしないように気をつけなければならない。", "text_en": "One must be careful not to fall ill from air conditioning." }
                    ],
                    "correctKey": "a",
                    "explanation_en": "Paragraph C states: 'そうなると、さらに悪いことが起きる...夏が終わるまで治らないということもあるのだ' (Worse things happen; symptoms can linger until summer ends)."
                },
                {
                    "paragraph": "D",
                    "options": [
                        { "key": "a", "text_ja": "冷房は体をこわす原因にもなる技術なので使わないほうがいい。", "text_en": "Since air conditioning causes illness, it's better not to use it." },
                        { "key": "b", "text_ja": "冷房で体をこわしたりしないように、うまく使うことが大切だ。", "text_en": "It is important to use air conditioning skillfully so as not to harm one's health." }
                    ],
                    "correctKey": "b",
                    "explanation_en": "Paragraph D states: '大事なことは、その技術を上手に使うということだろう' (The vital point is using the technology skillfully)."
                }
            ]
        },
        {
            "drillId": "drill-29-2",
            "title_ja": "練習2：段落の役割と文章構造",
            "title_en": "Exercise 2: Paragraph Roles and Text Structure",
            "instruction_ja": "この文章の段落A、B、C、Dの役割を考え、下のa〜dから選びなさい。",
            "instruction_en": "Consider the roles of paragraphs A, B, C, and D, and choose the correct structural flow from a to d.",
            "options": [
                {
                    "key": "a",
                    "text_ja": "（話題の提出）→（Aへの反対）→（Bの具体例）→（まとめ）",
                    "text_en": "(Topic Proposal) -> (Counter to A) -> (Specific Example of B) -> (Summary)"
                },
                {
                    "key": "b",
                    "text_ja": "（話題の提出）→（Aへの反対）→（Bとは別の内容）→（まとめ）",
                    "text_en": "(Topic Proposal) -> (Counter to A) -> (Content Distinct from B) -> (Summary)"
                },
                {
                    "key": "c",
                    "text_ja": "（話題の提出）→（Aへの賛成）→（Bへの追加情報）→（まとめ）",
                    "text_en": "(Topic Proposal) -> (Agreement with A) -> (Additional Information to B) -> (Summary)"
                },
                {
                    "key": "d",
                    "text_ja": "（話題の提出）→（Aへの反対）→（Bへの追加情報）→（まとめ）",
                    "text_en": "(Topic Proposal) -> (Counter to A) -> (Additional Information to B) -> (Summary)"
                }
            ],
            "correctKey": "d",
            "explanation_en": "Paragraph A introduces the topic of AC merits (話題の提出). Paragraph B counters with the negative impact on temperature-regulating nerves (Aへの反対). Paragraph C provides additional information on how this deterioration escalates and lingers (Bへの追加情報). Paragraph D wraps up the conclusion that AC should be used skillfully (まとめ). Therefore, sequence 'd' is correct."
        }
    ]
}

# Define Lesson 9 (Pages 30, 31)
lesson_09 = {
    "id": "dokkai-n3-l09",
    "pages": [30, 31],
    "skillNumber": 9,
    "skillCode": "reading_speed_9",
    "problemNumber": 13,
    "title_ja": "筆者の気持ちを理解する",
    "title_en": "Understanding the Author's Mood and Stance",
    "title_zh": "理解作者的心情",
    "passageTitle_ja": "レストランでの食事",
    "passageTitle_en": "Dining at the Restaurant",
    "readingStrategy": {
        "rule_ja": "筆者の気持ちが表れる言葉に注意しよう。筆者のよい評価（＋）や悪い評価（−）を表す言葉や表現を覚えよう。",
        "rule_en": "Pay close attention to words that reveal the writer's feelings. Learn the vocabulary and grammatical expressions used to express positive evaluations (+) and negative evaluations (-).",
        "rule_zh": "留意表达作者心情的词语。记住表达作者正面评价（＋）和负面评价（−）的词语及表达方式。",
        "keyPoints": [
            {
                "point_ja": "よい評価（＋）の言葉や表現",
                "point_en": "Words and expressions used for positive (+) judgments",
                "point_zh": "表达正面评价(+)的词语及表达方式",
                "examples": [
                    "落ち着いている",
                    "よく食べる",
                    "Aさんが来てくれた。・（私は）Aさんに来てもらった。",
                    "Aさんが歌を聞かせてくれた。・（私は）Aさんの歌を聞かせてもらった。"
                ]
            },
            {
                "point_ja": "悪い評価（−）の言葉や表現",
                "point_en": "Words and expressions used for negative (-) judgments",
                "point_zh": "表达负面评价(-)的词语及表达方式",
                "examples": [
                    "落ち着かない",
                    "食べすぎる",
                    "Aさんに来られた。",
                    "Aさんに歌を聞かせられた／聞かされた。"
                ]
            }
        ]
    },
    "preReading": {
        "question_ja": "「筆者がいいパーティーだったと思っているのはどちらですか。\nA そのパーティーはにぎやかだった。\nB そのパーティーはうるさかった。」",
        "question_en": "Which of the following indicates that the writer thought it was a good party?\nA: The party was lively (にぎやかだった).\nB: The party was noisy/annoying (うるさかった).",
        "answer": "A",
        "explanation_ja": "「にぎやか」は楽しく活気があるというプラス（＋）の評価、「うるさい」は騒がしくて不快というマイナス（−）の評価を表します。（答え：A）",
        "explanation_en": "'にぎやか' conveys positive vitality (+), whereas 'うるさい' conveys annoying noise (-). (Answer: A)"
    },
    "passage": {
        "sentences": [
            {
                "id": 1,
                "text_ja": "うちのそばに小さいレストランができたので、さっそく行ってみた。",
                "ruby_html": "うちのそばに<ruby>小<rt>ちい</rt></ruby>さいレストランができたので、さっそく<ruby>行<rt>い</rt></ruby>ってみた。",
                "text_en": "A small restaurant opened near my place, so I went to check it out right away."
            },
            {
                "id": 2,
                "text_ja": "外には小さく店の名前が書いてあるだけ。",
                "ruby_html": "<ruby>外<rt>そと</rt></ruby>には<ruby>小<rt>ちい</rt></ruby>さく<ruby>店<rt>みせ</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>が<ruby>書<rt>か</rt></ruby>いてあるだけ。",
                "text_en": "Outside, only the name of the shop was written in small letters."
            },
            {
                "id": 3,
                "text_ja": "派手なかざりは一つもなく、落ち着いた雰囲気だ。",
                "ruby_html": "<ruby>派手<rt>はで</rt></ruby>なかざりは<ruby>一<rt>ひと</rt></ruby>つもなく、<span class=\"eval-pos\"><strong><ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いた<ruby>雰囲気<rt>ふんいき</rt></ruby></strong></span>だ。",
                "text_en": "There were no flashy decorations at all, giving it a calm and relaxed atmosphere."
            },
            {
                "id": 4,
                "text_ja": "入ってみると3つほどテーブルがあり、汚れ一つない真っ白なテーブルクロスがかけられていた。",
                "ruby_html": "<ruby>入<rt>はい</rt></ruby>ってみると3つほどテーブルがあり、<span class=\"eval-pos\"><strong><ruby>汚<rt>よご</rt></ruby>れ<ruby>一<rt>ひと</rt></ruby>つない<ruby>真<rt>ま</rt></ruby>っ<ruby>白<rt>しろ</rt></ruby>なテーブルクロス</strong></span>がかけられていた。",
                "text_en": "When I stepped inside, there were about three tables, draped with spotless, pristine white tablecloths."
            },
            {
                "id": 5,
                "text_ja": "私は窓のそばの席に座り、メニューを開いた。",
                "ruby_html": "<ruby>私<rt>わたし</rt></ruby>は<ruby>窓<rt>まど</rt></ruby>のそばの<ruby>席<rt>せき</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>り、メニューを<ruby>開<rt>ひら</rt></ruby>いた。",
                "text_en": "I sat down at a seat by the window and opened the menu."
            },
            {
                "id": 6,
                "text_ja": "どれもとてもおいしそうで、期待がふくらんだ。",
                "ruby_html": "どれもとてもおいしそうで、<span class=\"eval-pos\"><strong><ruby>期待<rt>きたい</rt></ruby>がふくらんだ</strong></span>。",
                "text_en": "Everything looked so delicious, and my anticipation swelled."
            },
            {
                "id": 7,
                "text_ja": "その時、10人ほどの集団が入ってきて、レストランは満員になった。",
                "ruby_html": "その<ruby>時<rt>とき</rt></ruby>、10<ruby>人<rt>にん</rt></ruby>ほどの<ruby>集団<rt>しゅうだん</rt></ruby>が<ruby>入<rt>はい</rt></ruby>ってきて、レストランは<ruby>満員<rt>まんいん</rt></ruby>になった。",
                "text_en": "At that moment, a group of about ten people entered, filling the restaurant to capacity."
            },
            {
                "id": 8,
                "text_ja": "彼らはこの店によく来るらしく、メニューも見ないでどんどん注文をし始めた。",
                "ruby_html": "<ruby>彼<rt>かれ</rt></ruby>らはこの<ruby>店<rt>みせ</rt></ruby>によく<ruby>来<rt>く</rt></ruby>るらしく、メニューも<ruby>見<rt>み</rt></ruby>ないでどんどん<ruby>注文<rt>ちゅうもん</rt></ruby>をし<ruby>始<rt>はじ</rt></ruby>めた。",
                "text_en": "They seemed to be regulars; without even looking at the menu, they started placing orders rapidly."
            },
            {
                "id": 9,
                "text_ja": "私は自分の注文が後になってしまうと少し心配になりながら、一番人気があるというAセットを注文した。",
                "ruby_html": "<ruby>私<rt>わたし</rt></ruby>は<ruby>自分<rt>じぶん</rt></ruby>の<ruby>注文<rt>ちゅうもん</rt></ruby>が<ruby>後<rt>あと</rt></ruby>になってしまうと<ruby>少<rt>すこ</rt></ruby>し<ruby>心配<rt>しんぱい</rt></ruby>になりながら、<ruby>一番人気<rt>いちばんにんき</rt></ruby>があるというAセットを<ruby>注文<rt>ちゅうもん</rt></ruby>した。",
                "text_en": "Worrying a little that my order would be delayed, I ordered Set A, which was said to be the most popular."
            },
            {
                "id": 10,
                "text_ja": "私の方が先に店に入ったのに、やはり私の料理は彼らの料理の後に運ばれてきた。",
                "ruby_html": "<ruby>私<rt>わたし</rt></ruby>の<ruby>方<rt>ほう</rt></ruby>が<ruby>先<rt>さき</rt></ruby>に<ruby>店<rt>みせ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ったのに、やはり<ruby>私<rt>わたし</rt></ruby>の<ruby>料理<rt>りょうり</rt></ruby>は<ruby>彼<rt>かれ</rt></ruby>らの<ruby>料理<rt>りょうり</rt></ruby>の<ruby>後<rt>あと</rt></ruby>に<ruby>運<rt>はこ</rt></ruby>ばれてきた。",
                "text_en": "Even though I had entered the restaurant first, my food was served after theirs as expected."
            },
            {
                "id": 11,
                "text_ja": "彼らに先に注文されたからだ。",
                "ruby_html": "<ruby>彼<rt>かれ</rt></ruby>らに<span class=\"eval-neg\"><strong><ruby>先<rt>さき</rt></ruby>に<ruby>注文<rt>ちゅうもん</rt></ruby>された</strong></span>からだ。",
                "text_en": "That was because they had ordered before me."
            },
            {
                "id": 12,
                "text_ja": "その上、料理を待っている間ずっと、彼らがおいしそうに料理を食べながら、大声で話をするのを聞かされた。",
                "ruby_html": "その<ruby>上<rt>うえ</rt></ruby>、<ruby>料理<rt>りょうり</rt></ruby>を<ruby>待<rt>ま</rt></ruby>っている<ruby>間<rt>あいだ</rt></ruby>ずっと、<ruby>彼<rt>かれ</rt></ruby>らがおいしそうに<ruby>料理<rt>りょうり</rt></ruby>を<ruby>食<rt>た</rt></ruby>べながら、<span class=\"eval-neg\"><strong><ruby>大声<rt>おおごえ</rt></ruby>で<ruby>話<rt>はなし</rt></ruby>をするのを<ruby>聞<rt>き</rt></ruby>かされた</strong></span>。",
                "text_en": "On top of that, the entire time I was waiting for my food, I was forced to listen to them talking loudly while enjoying their meals."
            },
            {
                "id": 13,
                "text_ja": "料理が来たときにはもう疲れてしまい、味はどうでもよくなってしまった。",
                "ruby_html": "<ruby>料理<rt>りょうり</rt></ruby>が<ruby>来<rt>き</rt></ruby>たときにはもう<span class=\"eval-neg\"><strong><ruby>疲<rt>つか</rt></ruby>れてしまい、<ruby>味<rt>あじ</rt></ruby>はどうでもよくなってしまった</strong></span>。",
                "text_en": "By the time the food arrived, I was completely exhausted, and I didn't care about the taste anymore."
            }
        ]
    },
    "vocabulary": [
        { "term": "派手", "reading": "はで", "meaning": "showy, flashy, gaudy", "type": "na-adjective" },
        { "term": "かざり", "reading": "かざり", "meaning": "decoration, ornament", "type": "noun" },
        { "term": "落ち着く", "reading": "おちつく", "meaning": "to calm down, settle down", "type": "intransitive verb" },
        { "term": "雰囲気", "reading": "ふんいき", "meaning": "atmosphere, ambiance, mood", "type": "noun" },
        { "term": "汚れ", "reading": "よごれ", "meaning": "dirt, stain, spot", "type": "noun" },
        { "term": "真っ白", "reading": "まっしろ", "meaning": "pure white, snow white", "type": "na-adjective/noun" },
        { "term": "期待", "reading": "きたい", "meaning": "expectation, anticipation", "type": "noun/suru-verb" },
        { "term": "集団", "reading": "しゅうだん", "meaning": "group, crowd", "type": "noun" },
        { "term": "満員", "reading": "まんいん", "meaning": "full of people, full house", "type": "noun" },
        { "term": "運ぶ", "reading": "はこぶ", "meaning": "to carry, convey, serve", "type": "transitive verb" },
        { "term": "大声", "reading": "おおごえ", "meaning": "loud voice", "type": "noun" },
        { "term": "聞かされる", "reading": "きかされる", "meaning": "to be forced to listen to (causative-passive)", "type": "verb" },
        { "term": "どうでもいい", "reading": "どうでもいい", "meaning": "doesn't matter, indifferent", "type": "phrase" }
    ],
    "comprehensionQuestions": [
        {
            "questionId": "q-13-1",
            "questionNumber": 1,
            "questionText_ja": "この文章を書いた人の気持ちを説明しているのはどれか。",
            "questionText_en": "Which of the following explains the feelings of the person who wrote this text?",
            "options": [
                { "id": 1, "text_ja": "レストランはきれいだし、料理がおいしかったので満足している。", "text_en": "Satisfied because the restaurant was clean and the food was delicious." },
                { "id": 2, "text_ja": "集団のせいでなかなか料理を食べられなかったので、楽しめなかった。", "text_en": "Could not enjoy it because the group delayed the meal and ruined the experience." },
                { "id": 3, "text_ja": "レストランはかざりがなくてよくなかったが、集団の話は楽しめた。", "text_en": "The restaurant was not good because it lacked decoration, but enjoyed the group's conversation." },
                { "id": 4, "text_ja": "集団と話をしながら料理を食べたので、料理の味はどうでもよかった。", "text_en": "Because they ate while talking with the group, the flavor didn't matter." }
            ],
            "correctAnswer": 2,
            "explanation_ja": "筆者は最初、落ち着いた雰囲気の店に期待していましたが、後から入ってきた集団に先に注文され、大声で話すのを聞かされながら長く待たされたため、料理が届いたときには「もう疲れてしまい、味はどうでもよくなってしまった」と述べています。集団のせいで食事を楽しめなかった心情を表しているため、正解は 2 です。（選択肢1は満足しておらず、選択肢3は店の雰囲気を好意的に捉えており集団の話は不快でした。選択肢4は筆者は集団と会話していません。）",
            "explanation_en": "Although the author initially had high expectations in the calm restaurant, a later-arriving group ordered first, causing a long wait while loudly talking. When the food finally arrived, the author was exhausted and no longer cared about the taste. Thus Option 2 is correct. Options 1, 3, and 4 contradict the narrative details.",
            "techniqueFocus": "Tracking psychological changes: Follow the shift from positive expectation ('期待がふくらんだ') to negative experience caused by suffering passive ('先に注文された') and causative-passive ('聞かされた')."
        }
    ],
    "drills": [
        {
            "drillId": "drill-31-1",
            "title_ja": "練習：プラス評価（＋）とマイナス評価（−）",
            "title_en": "Exercise: Distinguishing Positive (+) and Negative (-) Judgments",
            "instruction_ja": "下線の部分を筆者はよいことだと思っている（＋）か、悪いことだと思っている（−）か。○をつけなさい。",
            "instruction_en": "Does the writer regard the underlined phrase as positive (+) or negative (-)? Circle (+) or (-).",
            "items": [
                {
                    "itemId": 1,
                    "text_ja": "落ち着いた雰囲気",
                    "text_en": "A calm atmosphere",
                    "evaluation": "+",
                    "explanation_en": "'落ち着いた' is a positive description of pleasant tranquility (+)."
                },
                {
                    "itemId": 2,
                    "text_ja": "汚れ一つない真っ白なテーブルクロス",
                    "text_en": "A spotless pure white tablecloth",
                    "evaluation": "+",
                    "explanation_en": "'汚れ一つない真っ白な' portrays pristine cleanliness (+)."
                },
                {
                    "itemId": 3,
                    "text_ja": "彼らに先に注文された",
                    "text_en": "Having them order ahead of me",
                    "evaluation": "-",
                    "explanation_en": "Adversative passive ('〜された') indicates suffering inconvenience/annoyance (-)."
                },
                {
                    "itemId": 4,
                    "text_ja": "大声で話をするのを聞かされた。",
                    "text_en": "Forced to listen to them talking in loud voices.",
                    "evaluation": "-",
                    "explanation_en": "Causative-passive ('聞かされた') indicates being forced to endure loud chatter (-)."
                },
                {
                    "itemId": 5,
                    "text_ja": "あの人はさっぱりした性格だ。",
                    "text_en": "That person has a frank, refreshing, and agreeable personality.",
                    "evaluation": "+",
                    "explanation_en": "'さっぱりした性格' is a positive compliment denoting an open-hearted, pleasant temperament (+)."
                },
                {
                    "itemId": 6,
                    "text_ja": "あの人はしつこい性格だ。",
                    "text_en": "That person has a persistent, nagging, obstinate personality.",
                    "evaluation": "-",
                    "explanation_en": "'しつこい' carries a negative nuance of being pestering or annoying (-)."
                },
                {
                    "itemId": 7,
                    "text_ja": "携帯電話を学校へ持ってきてしまった。",
                    "text_en": "Inadvertently brought the mobile phone to school (regrettably).",
                    "evaluation": "-",
                    "explanation_en": "'〜てしまった' expresses regret over an unintended or improper action (-)."
                },
                {
                    "itemId": 8,
                    "text_ja": "自然に恵まれた環境",
                    "text_en": "An environment blessed with rich nature",
                    "evaluation": "+",
                    "explanation_en": "'恵まれた' indicates being blessed or endowed with advantages (+)."
                }
            ]
        }
    ]
}

# Define Lesson 10 / Part 2 Preparatory Work (Pages 35, 36, 37)
lesson_part2_prep = {
    "id": "dokkai-n3-part2-prep",
    "pages": [35, 36, 37],
    "section": "第2部 学習の前に (Part 2: Preparatory Work)",
    "title_ja": "第2部 学習の前に",
    "title_en": "Part 2: Preparatory Work",
    "title_zh": "第2部分 学前准备",
    "overview_ja": "第2部では、日本語能力試験でよく取り上げられる、さまざまなタイプの文章を読みます。これらの文章の特徴やよく使われる文型などの紹介があります。どんなところに注意したほうがよいか、確認しましょう。",
    "overview_en": "In Part 2, you encounter various types of text which occur frequently in the JLPT. This section includes the characteristics of these types of text and frequently used sentence patterns. Be sure to check which points you need to take note of.",
    "overview_zh": "在第2部分，阅读日语能力考试中经常出现的各种类型文章。介绍这些文章的特点以及经常使用的句型。核查一下应该留意哪些地方吧。",
    "textTypes": [
        { "number": 1, "type_ja": "メール（プライベート）", "type_en": "E-mail (private)", "type_zh": "邮件（私人）" },
        { "number": 2, "type_ja": "手紙", "type_en": "Letters", "type_zh": "书信" },
        { "number": 3, "type_ja": "メモ", "type_en": "Memos", "type_zh": "提示便条" },
        { "number": 4, "type_ja": "指示文", "type_en": "Instruction texts", "type_zh": "操作说明" },
        { "number": 5, "type_ja": "意見文", "type_en": "Expressions of opinion", "type_zh": "观点阐释文" },
        { "number": 6, "type_ja": "説明文", "type_en": "Explanatory texts", "type_zh": "解释说明文" },
        { "number": 7, "type_ja": "エッセイ", "type_en": "Essays", "type_zh": "散文随笔" }
    ],
    "exerciseSequence": [
        {
            "step": 1,
            "heading_ja": "読む前に",
            "heading_en": "Preparation before reading",
            "heading_zh": "阅读前",
            "description_ja": "文章についての簡単な質問。答えは各ページの下にあります。",
            "description_en": "Simple questions about the text. The answers are at the bottom of each page.",
            "description_zh": "关于文章的简单提问。答案在各页下方。"
        },
        {
            "step": 2,
            "heading_ja": "問題",
            "heading_en": "Questions",
            "heading_zh": "试题",
            "description_ja": "短文から長文まであります。問いは一つ〜三つです。（実際の試験問題より問いの数が少ないものもあります。）",
            "description_en": "These comprise short, mid-length and long sentences. There are between one and three questions. (This is sometimes fewer than the number of questions that occur in the actual examination.)",
            "description_zh": "从短篇文章到长篇文章，包含各种类型文章。提问有1-3个。（有的题比实际考试中的设问数量少。）"
        },
        {
            "step": 3,
            "heading_ja": "語句・表現",
            "heading_en": "Phrases and expressions",
            "heading_zh": "词汇表",
            "description_ja": "本文にある言葉で、よく使われるもの。できるだけ覚えましょう。",
            "description_en": "These are terms that occur in the main text and are frequently used. Do your best to memorize as many as possible.",
            "description_zh": "收录正文中出现的词汇，都是常用词。尽量记住吧。"
        },
        {
            "step": 4,
            "heading_ja": "解説",
            "heading_en": "Commentary",
            "heading_zh": "解说",
            "description_ja": "それぞれの文章の形式についての簡単な説明",
            "description_en": "Simple explanations of each type of text.",
            "description_zh": "关于各种文章格式的简单解释说明。"
        },
        {
            "step": 5,
            "heading_ja": "試験問題では次のように考えよう",
            "heading_en": "Approach the examination questions in the following way",
            "heading_zh": "应试提示",
            "description_ja": "それぞれの形式の文章を読むときの注意点。本文ではどう考えればよいかの具体的な説明。",
            "description_en": "Points to bear in mind when reading texts in each of the different formats. Detailed explanations of the optimal approach to the main texts.",
            "description_zh": "介绍阅读各种类型文章时要注意的地方。具体解释说明在本题中应该如何思考。"
        }
    ],
    "passage": {
        "sentences": [
            {
                "id": 1,
                "text_ja": "第2部では、日本語能力試験でよく取り上げられる、さまざまなタイプの文章を読みます。",
                "ruby_html": "<ruby>第2部<rt>だいにぶ</rt></ruby>では、<ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby>でよく<ruby>取<rt>と</rt></ruby>り<ruby>上<rt>あ</rt></ruby>げられる、さまざまなタイプの<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。",
                "text_en": "In Part 2, you encounter various types of text which occur frequently in the JLPT."
            },
            {
                "id": 2,
                "text_ja": "これらの文章の特徴やよく使われる文型などの紹介があります。どんなところに注意したほうがよいか、確認しましょう。",
                "ruby_html": "これらの<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>特徴<rt>とくちょう</rt></ruby>やよく<ruby>使<rt>つか</rt></ruby>われる<ruby>文型<rt>ぶんけい</rt></ruby>などの<ruby>紹介<rt>しょうかい</rt></ruby>があります。どんなところに<ruby>注意<rt>ちゅうい</rt></ruby>したほうがよいか、<ruby>確認<rt>かくにん</rt></ruby>しましょう。",
                "text_en": "This section includes the characteristics of these types of text and frequently used sentence patterns. Be sure to check which points you need to take note of."
            },
            {
                "id": 3,
                "text_ja": "それぞれの練習は以下のような順番になっています。",
                "ruby_html": "それぞれの<ruby>練習<rt>れんしゅう</rt></ruby>は<ruby>以下<rt>いか</rt></ruby>のような<ruby>順番<rt>じゅんばん</rt></ruby>になっています。",
                "text_en": "The sequence of the exercises follows below."
            },
            {
                "id": 4,
                "text_ja": "読む前に：文章についての簡単な質問。答えは各ページの下にあります。",
                "ruby_html": "<ruby>読<rt>よ</rt></ruby>む<ruby>前<rt>まえ</rt></ruby>に：<ruby>文章<rt>ぶんしょう</rt></ruby>についての<ruby>簡単<rt>かんたん</rt></ruby>な<ruby>質問<rt>しつもん</rt></ruby>。<ruby>答<rt>こた</rt></ruby>えは<ruby>各<rt>かく</rt></ruby>ページの下にあります。",
                "text_en": "Preparation before reading: Simple questions about the text. The answers are at the bottom of each page."
            },
            {
                "id": 5,
                "text_ja": "問題：短文から長文まであります。問いは一つ〜三つです。（実際の試験問題より問いの数が少ないものもあります。）",
                "ruby_html": "<ruby>問題<rt>もんだい</rt></ruby>：<ruby>短文<rt>たんぶん</rt></ruby>から<ruby>長文<rt>ちょうぶん</rt></ruby>まであります。<ruby>問<rt>と</rt></ruby>いは<ruby>一<rt>ひと</rt></ruby>つ〜<ruby>三<rt>みっ</rt></ruby>つです。（<ruby>実際<rt>じっさい</rt></ruby>の<ruby>試験問題<rt>しけんもんだい</rt></ruby>より<ruby>問<rt>と</rt></ruby>いの<ruby>数<rt>かず</rt></ruby>が<ruby>少<rt>すく</rt></ruby>ないものもあります。）",
                "text_en": "Questions: These comprise short, mid-length and long sentences. There are between one and three questions. (This is sometimes fewer than the number of questions that occur in the actual examination.)"
            },
            {
                "id": 6,
                "text_ja": "語句・表現：本文にある言葉で、よく使われるもの。できるだけ覚えましょう。",
                "ruby_html": "<ruby>語句<rt>ごく</rt></ruby>・<ruby>表現<rt>ひょうげん</rt></ruby>：<ruby>本文<rt>ほんぶん</rt></ruby>にある<ruby>言葉<rt>ことば</rt></ruby>で、よく<ruby>使<rt>つか</rt></ruby>われるもの。できるだけ<ruby>覚<rt>おぼ</rt></ruby>えましょう。",
                "text_en": "Phrases and expressions: These are terms that occur in the main text and are frequently used. Do your best to memorize as many as possible."
            },
            {
                "id": 7,
                "text_ja": "解説：それぞれの文章の形式についての簡単な説明。",
                "ruby_html": "<ruby>解説<rt>かいせつ</rt></ruby>：それぞれの<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>形式<rt>けいしき</rt></ruby>についての<ruby>簡単<rt>かんたん</rt></ruby>な<ruby>説明<rt>せつめい</rt></ruby>。",
                "text_en": "Commentary: Simple explanations of each type of text."
            },
            {
                "id": 8,
                "text_ja": "試験問題では次のように考えよう：それぞれの形式の文章を読むときの注意点。本文ではどう考えればよいかの具体的な説明。",
                "ruby_html": "<ruby>試験問題<rt>しけんもんだい</rt></ruby>では<ruby>次<rt>つぎ</rt></ruby>のように<ruby>考<rt>かんが</rt></ruby>えよう：それぞれの<ruby>形式<rt>けいしき</rt></ruby>の<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>読<rt>よ</rt></ruby>むときの<ruby>注意点<rt>ちゅういてん</rt></ruby>。<ruby>本文<rt>ほんぶん</rt></ruby>ではどう<ruby>考<rt>かんが</rt></ruby>えればよいかの<ruby>具体的<rt>ぐたいてき</rt></ruby>な<ruby>説明<rt>せつめい</rt></ruby>。",
                "text_en": "Approach the examination questions in the following way: Points to bear in mind when reading texts in each of the different formats. Detailed explanations of the optimal approach to the main texts."
            }
        ]
    },
    "vocabulary": [
        { "term": "取り上げる", "reading": "とりあげる", "meaning": "to take up, feature, adopt", "type": "transitive verb" },
        { "term": "特徴", "reading": "とくちょう", "meaning": "characteristic, distinctive feature", "type": "noun" },
        { "term": "文型", "reading": "ぶんけい", "meaning": "sentence pattern", "type": "noun" },
        { "term": "紹介", "reading": "しょうかい", "meaning": "introduction, presentation", "type": "noun/suru-verb" },
        { "term": "順番", "reading": "じゅんばん", "meaning": "order, sequence", "type": "noun" },
        { "term": "短文", "reading": "たんぶん", "meaning": "short text / short sentence", "type": "noun" },
        { "term": "長文", "reading": "ちょうぶん", "meaning": "long text / long passage", "type": "noun" },
        { "term": "語句", "reading": "ごく", "meaning": "words and phrases", "type": "noun" },
        { "term": "形式", "reading": "けいしき", "meaning": "form, format, style", "type": "noun" },
        { "term": "注意点", "reading": "ちゅういてん", "meaning": "points to note / precautions", "type": "noun" }
    ],
    "comprehensionQuestions": [],
    "drills": []
}

combined_lessons = existing_lessons + [lesson_07, lesson_08, lesson_09, lesson_part2_prep]

output_data = {
    "metadata": {
        "bookTitle": "新完全マスター JLPT N3 読解",
        "bookTitleRomaji": "Shin Kanzen Master JLPT N3 Dokkai",
        "englishTitle": "New Complete Master JLPT N3 Reading Comprehension",
        "level": "JLPT N3 (Intermediate)",
        "section": "第1部 基礎力をつけよう (Part 1: Building Foundational Skills) & 第2部 学習の前に (Part 2: Preparatory Work)",
        "chapter": "2. 読むスピードを上げよう (Increasing Reading Speed) & 第2部導入 (Part 2 Orientation)",
        "totalPagesCovered": "19-37",
        "totalLessons": len(combined_lessons),
        "version": "1.1.0",
        "lastUpdated": "2026-10-11"
    },
    "lessons": combined_lessons
}

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(combined_lessons)} lessons to {out_file}.")
