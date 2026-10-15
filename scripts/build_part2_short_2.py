import json
import os

data = {
    "metadata": {
        "bookTitle": "新完全マスター JLPT N3 読解",
        "bookTitleRomaji": "Shin Kanzen Master JLPT N3 Dokkai",
        "englishTitle": "New Complete Master JLPT N3 Reading Comprehension",
        "level": "JLPT N3 (Intermediate)",
        "section": "実力養成編 第2部＆第3部 (Part 2: Read Various Texts & Part 3: Search for Information)",
        "subSection": "短文・情報検索 (Short Texts & Information Retrieval)",
        "version": "1.0.0",
        "lastUpdated": "2026-10-11"
    },
    "lessons": [
        {
            "id": "dokkai-n3-p2-06",
            "pages": [48, 49],
            "problemNumber": 19,
            "genre": "説明文",
            "genre_en": "Explanatory texts",
            "genre_zh": "解释说明文",
            "title_ja": "6) 説明文",
            "title_en": "6) Explanatory texts",
            "title_zh": "6) 解释说明文",
            "preReading": {
                "question_ja": "あなたの国では避難訓練(注)をしますか。どんなことをしますか。",
                "question_en": "Do you have evacuation drills in your country? What kind of things do you do?",
                "question_zh": "在你的国家会进行避难训练吗？都会做些什么呢？"
            },
            "passageInstructions": {
                "instruction_ja": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
                "instruction_en": "Read the following text and answer the questions. Choose the best answer from 1, 2, 3, 4."
            },
            "passage": {
                "sentences": [
                    {
                        "id": 1,
                        "text_ja": "日本では幼稚園や小学校で「おかしも」という言葉を習います。",
                        "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>では<ruby>幼稚園<rt>ようちえん</rt></ruby>や<ruby>小学校<rt>しょうがっこう</rt></ruby>で「おかしも」という<ruby>言葉<rt>ことば</rt></ruby>を<ruby>習<rt>なら</rt></ruby>います。",
                        "text_en": "In Japan, children learn the word 'Okashimo' in kindergarten and elementary school."
                    },
                    {
                        "id": 2,
                        "text_ja": "「おかしも」とは、「押さない、駆けない、しゃべらない、戻らない」の頭文字をとった言葉で、災害が起きたときに安全に避難するための約束です。",
                        "ruby_html": "「おかしも」とは、「<ruby>押<rt>お</rt></ruby>さない、<ruby>駆<rt>か</rt></ruby>けない<sup>(注2)</sup>、しゃべらない<sup>(注3)</sup>、<ruby>戻<rt>もど</rt></ruby>らない」の<ruby>頭文字<rt>かしらもじ</rt></ruby>をとった<ruby>言葉<rt>ことば</rt></ruby>で、<ruby>災害<rt>さいがい</rt></ruby><sup>(注1)</sup>が<ruby>起<rt>お</rt></ruby>きたときに<ruby>安全<rt>あんぜん</rt></ruby>に<ruby>避難<rt>ひなん</rt></ruby>するための<ruby>約束<rt>やくそく</rt></ruby>です。",
                        "text_en": "'Okashimo' is an acronym formed from the first letters of 'Don't push, Don't run, Don't talk, Don't go back', and is a rule for safely evacuating when a disaster occurs."
                    },
                    {
                        "id": 3,
                        "text_ja": "「押さない」は前の人を押さないこと、「駆けない」は走らないことです。",
                        "ruby_html": "「<ruby>押<rt>お</rt></ruby>さない」は<ruby>前<rt>まえ</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>を<ruby>押<rt>お</rt></ruby>さないこと、「<ruby>駆<rt>か</rt></ruby>けない」は<ruby>走<rt>はし</rt></ruby>らないことです。",
                        "text_en": "'Don't push' means not pushing the person in front of you, and 'Don't run' means not running."
                    },
                    {
                        "id": 4,
                        "text_ja": "慌てて走ると転んで怪我をするかもしれません。",
                        "ruby_html": "<ruby>慌<rt>あわ</rt></ruby>てて<ruby>走<rt>はし</rt></ruby>ると<ruby>転<rt>ころ</rt></ruby>んで<ruby>怪我<rt>けが</rt></ruby>をするかもしれません。",
                        "text_en": "If you rush and run, you might fall and get injured."
                    },
                    {
                        "id": 5,
                        "text_ja": "「しゃべらない」は先生の指示をよく聞くためです。",
                        "ruby_html": "「しゃべらない」は<ruby>先生<rt>せんせい</rt></ruby>の<ruby>指示<rt>しじ</rt></ruby>をよく<ruby>聞<rt>き</rt></ruby>くためです。",
                        "text_en": "'Don't talk' is so that you can listen carefully to the teacher's instructions."
                    },
                    {
                        "id": 6,
                        "text_ja": "そして、「戻らない」は、忘れ物をしても教室などに戻ってはいけないということです。",
                        "ruby_html": "そして、「<ruby>戻<rt>もど</rt></ruby>らない」は、<ruby>忘<rt>わす</rt></ruby>れ<ruby>物<rt>もの</rt></ruby>をしても<ruby>教室<rt>きょうしつ</rt></ruby>などに<ruby>戻<rt>もど</rt></ruby>ってはいけないということです。",
                        "text_en": "And 'Don't go back' means that even if you left something behind, you must not return to the classroom or elsewhere."
                    },
                    {
                        "id": 7,
                        "text_ja": "避難訓練のたびに先生から聞かされるので、日本の子どもたちで「おかしも」の意味を知らない子どもはいないほどです。",
                        "ruby_html": "<ruby>避難訓練<rt>ひなんくんれん</rt></ruby>のたびに<ruby>先生<rt>せんせい</rt></ruby>から<ruby>聞<rt>き</rt></ruby>かされるので、<ruby>日本<rt>にほん</rt></ruby>の<ruby>子<rt>こ</rt></ruby>どもたちで「おかしも」の<ruby>意味<rt>いみ</rt></ruby>を<ruby>知<rt>し</rt></ruby>らない<ruby>子<rt>こ</rt></ruby>どもはいないほどです。",
                        "text_en": "Because they are reminded by their teachers at every evacuation drill, there are practically no Japanese children who do not know what 'Okashimo' means."
                    },
                    {
                        "id": 8,
                        "text_ja": "素早く避難することは大切ですが、安全に避難することがもっと大切です。",
                        "ruby_html": "<ruby>素早<rt>すばや</rt></ruby>く<ruby>避難<rt>ひなん</rt></ruby>することは<ruby>大切<rt>たいせつ</rt></ruby>ですが、<ruby>安全<rt>あんぜん</rt></ruby>に<ruby>避難<rt>ひなん</rt></ruby>することがもっと<ruby>大切<rt>たいせつ</rt></ruby>です。",
                        "text_en": "Evacuating quickly is important, but evacuating safely is even more important."
                    },
                    {
                        "id": 9,
                        "text_ja": "この約束をしっかり身につけておくことで、もしものときにも落ち着いて行動できるのです。",
                        "ruby_html": "この<ruby>約束<rt>やくそく</rt></ruby>をしっかり<ruby>身<rt>み</rt></ruby>につけておくことで、もしものときにも<ruby>落<rt>お</rt></ruby>ち<ruby>着<rt>つ</rt></ruby>いて<ruby>行動<rt>こうどう</rt></ruby>できるのです。",
                        "text_en": "By thoroughly mastering this rule, one can act calmly even in an emergency."
                    }
                ]
            },
            "footnotes": [
                {
                    "index": 1,
                    "term_ja": "災害",
                    "reading": "さいがい",
                    "definition_ja": "地震や台風などによって受ける被害",
                    "definition_en": "disaster (damage caused by earthquakes, typhoons, etc.)",
                    "definition_zh": "灾害（地震、台风等造成的危害）"
                },
                {
                    "index": 2,
                    "term_ja": "駆ける",
                    "reading": "かける",
                    "definition_ja": "走る",
                    "definition_en": "to run, dash",
                    "definition_zh": "奔跑，飞奔"
                },
                {
                    "index": 3,
                    "term_ja": "しゃべる",
                    "reading": "しゃべる",
                    "definition_ja": "話す",
                    "definition_en": "to talk, chatter",
                    "definition_zh": "交谈，说话"
                }
            ],
            "vocabulary": [
                {
                    "term": "幼稚園",
                    "reading": "ようちえん",
                    "meaning": "kindergarten / 幼儿园",
                    "type": "noun"
                },
                {
                    "term": "校庭",
                    "reading": "こうてい",
                    "meaning": "schoolyard, school grounds / 校园，操场",
                    "type": "noun"
                },
                {
                    "term": "素早く",
                    "reading": "すばやく",
                    "meaning": "quickly, promptly / 敏捷地，迅速地",
                    "type": "adverb"
                },
                {
                    "term": "〜のたびに",
                    "reading": "〜のたびに",
                    "meaning": "every time, whenever / 每当，每次",
                    "type": "grammar"
                },
                {
                    "term": "耳にする",
                    "reading": "みみにする",
                    "meaning": "to hear / 听到",
                    "type": "phrase"
                },
                {
                    "term": "〜ない（人）はいない",
                    "reading": "〜ない（ひと）はいない",
                    "meaning": "there is no one who doesn't... / 没有不……的人",
                    "type": "grammar"
                },
                {
                    "term": "〜ほど〜",
                    "reading": "〜ほど〜",
                    "meaning": "to the extent that... / 到了……的地步",
                    "type": "grammar"
                },
                {
                    "term": "身につける",
                    "reading": "みにつける",
                    "meaning": "to acquire, master, learn / 掌握，养成",
                    "type": "verb phrase"
                }
            ],
            "comprehensionQuestions": [
                {
                    "questionId": "q-19-1",
                    "questionNumber": 1,
                    "questionText_ja": "「おかしも」とは何か。",
                    "questionText_en": "What is 'Okashimo'?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "幼稚園や小学校で習う歌の題名",
                            "text_en": "The title of a song taught in kindergartens and elementary schools"
                        },
                        {
                            "id": 2,
                            "text_ja": "避難するときの注意を短くした言葉",
                            "text_en": "A shortened acronym summing up rules for evacuation"
                        },
                        {
                            "id": 3,
                            "text_ja": "災害が起きたときに使う道具の名前",
                            "text_en": "The name of a tool used when a disaster strikes"
                        },
                        {
                            "id": 4,
                            "text_ja": "安全に避難した子どもにあげる約束のごほうび",
                            "text_en": "A reward promised to children who evacuate safely"
                        }
                    ],
                    "correctAnswer": 2,
                    "explanation_ja": "本文に「『おかしも』とは、『押さない、駆けない、しゃべらない、戻らない』の頭文字をとった言葉で、災害が起きたときに安全に避難するための約束です」と書かれています。避難時の注意事項を短くした言葉であるため、2が正解です。",
                    "explanation_en": "The text explains that 'Okashimo' is an acronym formed from the first letters of 'Don't push, Don't run, Don't talk, Don't go back', acting as rules for safe evacuation. Therefore, Option 2 is correct."
                },
                {
                    "questionId": "q-19-2",
                    "questionNumber": 2,
                    "questionText_ja": "「日本の子どもたちで「おかしも」の意味を知らない子どもはいないほどです。」とあるが、それはなぜか。",
                    "questionText_en": "Why is it that 'there are practically no children in Japan who do not know the meaning of 'Okashimo''?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "災害が起きて実際に走って逃げた経験があるから。",
                            "text_en": "Because they have actual experience running away during a disaster."
                        },
                        {
                            "id": 2,
                            "text_ja": "避難訓練をするときにはいつもその言葉を聞くから。",
                            "text_en": "Because they hear that word every time they have an evacuation drill."
                        },
                        {
                            "id": 3,
                            "text_ja": "教室に戻って忘れ物を取ってはいけないと叱られたから。",
                            "text_en": "Because they were scolded for returning to the classroom to get forgotten items."
                        },
                        {
                            "id": 4,
                            "text_ja": "素早く走って避難することがとても大切だと教えられたから。",
                            "text_en": "Because they were taught that running quickly to evacuate is very important."
                        }
                    ],
                    "correctAnswer": 2,
                    "explanation_ja": "本文で「避難訓練のたびに先生から聞かされるので、日本の子どもたちで『おかしも』の意味を知らない子どもはいないほどです」と理由（〜ので）が明確に述べられています。「訓練のたびに聞かされる＝いつも聞く」ため、2が正解です。",
                    "explanation_en": "The passage clearly connects the cause and effect: 'Because they are told by teachers every time they have an evacuation drill (...no tabi ni), there are almost no Japanese children who do not know the meaning of Okashimo.' Therefore, Option 2 is correct."
                }
            ],
            "commentary": {
                "title_ja": "解説 ◆説明文",
                "text_ja": "説明文は、ある事柄やルール、仕組み、客観的事実などを読者にわかりやすく解説する文章です。「〜とは〜ということだ」「〜は〜を意味する」などの定義表現や、「〜のために〜」「〜ので〜」などの理由・因果関係を示す表現が多く使われます。",
                "text_en": "Explanatory texts explain a topic, rule, mechanism, or objective fact clearly to the reader. Defining patterns like '...to wa...to iu koto da' and causal expressions like '...no tame ni' and '...node' are frequently used.",
                "text_zh": "说明文是向读者浅显易懂地解释某种事物、规则、机制或客观事实的文章。常使用“～とは～ということだ（所谓……就是……）”等定义句型，以及“～のために”、“～ので”等表示原因和因果关系的句型。",
                "structureLayout": [
                    {
                        "component": "導入（定義）",
                        "detail": "「おかしも」とは避難の約束（頭文字）",
                        "en": "Introduction (Definition of the term)"
                    },
                    {
                        "component": "具体的内容の説明",
                        "detail": "押さない・駆けない・しゃべらない・戻らない の各理由",
                        "en": "Explanation of specific details and reasons"
                    },
                    {
                        "component": "浸透の背景と結論",
                        "detail": "訓練のたびに習うため全員知っている / 素早さより安全が大切",
                        "en": "Background of familiarity and conclusion"
                    }
                ]
            },
            "testAdvice": {
                "title_ja": "試験問題では、次のように考えよう。",
                "title_en": "In answering examination questions, ask yourself the following:",
                "title_zh": "考试时分析步骤如下。",
                "analysisSteps": [
                    {
                        "step": 1,
                        "question_ja": "何について説明されているか。",
                        "question_en": "What is being explained?",
                        "question_zh": "说明的内容是什么？",
                        "analysis_ja": "避難するときの約束である「おかしも」という言葉とその意味。",
                        "analysis_en": "The word 'Okashimo' and its meaning as an evacuation safety rule.",
                        "analysis_zh": "关于避难时的约定“おかしも”这个词语及其含义。"
                    },
                    {
                        "step": 2,
                        "question_ja": "どのように説明されているか（理由や因果関係）。",
                        "question_en": "How is it explained (reasons and cause-effect)?",
                        "question_zh": "是如何说明的（理由与因果关系）？",
                        "analysis_ja": "それぞれの行動が求められる理由（転ぶのを防ぐ、指示を聞く等）と、訓練のたびに聞かされるため全員が身につけていることが説明されている。",
                        "analysis_en": "The reasons behind each caution (prevent falling, hear instructions, etc.) and why all children know it due to recurring drills are explained.",
                        "analysis_zh": "解释了每个要求的理由（防止跌倒、听从指示等），以及每次训练都会反复强调因而人尽皆知。"
                    }
                ]
            }
        },
        {
            "id": "dokkai-n3-p2-07",
            "pages": [50, 51],
            "problemNumber": 20,
            "genre": "エッセイ",
            "genre_en": "Essays",
            "genre_zh": "散文随笔",
            "title_ja": "7) エッセイ",
            "title_en": "7) Essays",
            "title_zh": "7) 散文随笔",
            "preReading": {
                "question_ja": "和菓子を食べたことがありますか。どの季節にどんな和菓子を食べましたか。",
                "question_en": "Have you ever eaten Japanese sweets (wagashi)? In which season and what kind did you eat?",
                "question_zh": "你吃过日式点心（和果子）吗？在什么季节吃过什么样的点心？"
            },
            "passageInstructions": {
                "instruction_ja": "つぎの文章を読んで、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
                "instruction_en": "Read the following text and answer the questions. Choose the best answer from 1, 2, 3, 4."
            },
            "passage": {
                "sentences": [
                    {
                        "id": 1,
                        "text_ja": "日本では季節が生活のいろいろな面に影響している。",
                        "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>では<ruby>季節<rt>きせつ</rt></ruby>が<ruby>生活<rt>せいかつ</rt></ruby>のいろいろな<ruby>面<rt>めん</rt></ruby>に<ruby>影響<rt>えいきょう</rt></ruby>している。",
                        "text_en": "In Japan, the seasons influence many aspects of daily life."
                    },
                    {
                        "id": 2,
                        "text_ja": "外国から来た自分にとってそれはとても①おもしろい。",
                        "ruby_html": "<ruby>外国<rt>がいこく</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>自分<rt>じぶん</rt></ruby>にとってそれはとても①おもしろい。",
                        "text_en": "To me, coming from abroad, that is very fascinating."
                    },
                    {
                        "id": 3,
                        "text_ja": "以前、冬の初めのころに和菓子屋に行った。",
                        "ruby_html": "<ruby>以前<rt>いぜん</rt></ruby>、<ruby>冬<rt>ふゆ</rt></ruby>の<ruby>初<rt>はじ</rt></ruby>めのころに<ruby>和菓子屋<rt>わがしや</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                        "text_en": "Previously, around the beginning of winter, I went to a Japanese confectionery shop."
                    },
                    {
                        "id": 4,
                        "text_ja": "ガラスケースの中に、きれいな赤い花があった。",
                        "ruby_html": "ガラスケースの<ruby>中<rt>なか</rt></ruby>に、きれいな<ruby>赤<rt>あか</rt></ruby>い<ruby>花<rt>はな</rt></ruby>があった。",
                        "text_en": "Inside the glass display case, there was a beautiful red flower."
                    },
                    {
                        "id": 5,
                        "text_ja": "「これは何の花ですか」と店員に聞くと、「寒椿です」と教えてくれた。",
                        "ruby_html": "「これは<ruby>何<rt>なん</rt></ruby>の<ruby>花<rt>はな</rt></ruby>ですか」と<ruby>店員<rt>てんいん</rt></ruby>に<ruby>聞<rt>き</rt></ruby>くと、「<ruby>寒椿<rt>かんつばき</rt></ruby>です」と<ruby>教<rt>おし</rt></ruby>えてくれた。",
                        "text_en": "When I asked the clerk, 'What flower is this?', they told me, 'It is a winter camellia.'"
                    },
                    {
                        "id": 6,
                        "text_ja": "椿は冬の花だ。",
                        "ruby_html": "<ruby>椿<rt>つばき</rt></ruby>は<ruby>冬<rt>ふゆ</rt></ruby>の<ruby>花<rt>はな</rt></ruby>だ。",
                        "text_en": "The camellia is a winter flower."
                    },
                    {
                        "id": 7,
                        "text_ja": "それからしばらくして、もう一度その店へ行った。",
                        "ruby_html": "それからしばらくして、もう<ruby>一度<rt>いちど</rt></ruby>その<ruby>店<rt>みせ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った。",
                        "text_en": "A while after that, I went to that shop once more."
                    },
                    {
                        "id": 8,
                        "text_ja": "②あの赤い花をもう一度買いたかったのだ。",
                        "ruby_html": "②あの<ruby>赤<rt>あか</rt></ruby>い<ruby>花<rt>はな</rt></ruby>をもう<ruby>一度<rt>いちど</rt></ruby><ruby>買<rt>か</rt></ruby>いたかったのだ。",
                        "text_en": "I wanted to buy that red flower one more time."
                    },
                    {
                        "id": 9,
                        "text_ja": "しかし、ケースの中にあの花はなかった。",
                        "ruby_html": "しかし、ケースの<ruby>中<rt>なか</rt></ruby>にあのはなはなかった。",
                        "text_en": "However, that flower was not inside the case."
                    },
                    {
                        "id": 10,
                        "text_ja": "私は店員に「あの椿の花はもうないんですか」と聞いた。",
                        "ruby_html": "<ruby>私<rt>わたし</rt></ruby>は<ruby>店員<rt>てんいん</rt></ruby>に「あの<ruby>椿<rt>つばき</rt></ruby>の<ruby>花<rt>はな</rt></ruby>はもうないんですか」と<ruby>聞<rt>き</rt></ruby>いた。",
                        "text_en": "I asked the clerk, 'Is that camellia flower sweet gone now?'"
                    },
                    {
                        "id": 11,
                        "text_ja": "店員は「椿の季節は終わりましたから、もう作っていません。今はこれです」と言って、別の花を指差した。",
                        "ruby_html": "<ruby>店員<rt>てんいん</rt></ruby>は「<ruby>椿<rt>つばき</rt></ruby>の<ruby>季節<rt>きせつ</rt></ruby>は<ruby>終<rt>お</rt></ruby>わりましたから、もう<ruby>作<rt>つく</rt></ruby>っていません。<ruby>今<rt>いま</rt></ruby>はこれです」と<ruby>言<rt>い</rt></ruby>って、<ruby>別<rt>べつ</rt></ruby>の<ruby>花<rt>はな</rt></ruby>を<ruby>指差<rt>ゆびさ</rt></ruby>した。",
                        "text_en": "The clerk said, 'Camellia season has ended, so we no longer make it. Right now we have this,' pointing at a different flower."
                    },
                    {
                        "id": 12,
                        "text_ja": "それは桜の花だった。",
                        "ruby_html": "それは<ruby>桜<rt>さくら</rt></ruby>の<ruby>花<rt>はな</rt></ruby>だった。",
                        "text_en": "It was a cherry blossom."
                    },
                    {
                        "id": 13,
                        "text_ja": "「えっ、椿はもうないの」と私はがっかりした。",
                        "ruby_html": "「えっ、<ruby>椿<rt>つばき</rt></ruby>はもうないの」と<ruby>私<rt>わたし</rt></ruby>はがっかりした。",
                        "text_en": "'What, camellia is already gone?' I thought with disappointment."
                    },
                    {
                        "id": 14,
                        "text_ja": "そのときはまだ寒かったからだ。",
                        "ruby_html": "そのときはまだ<ruby>寒<rt>さむ</rt></ruby>かったからだ。",
                        "text_en": "Because it was still cold at that time."
                    },
                    {
                        "id": 15,
                        "text_ja": "しかし、店を出て歩いていると、小さな春の兆しを見つけた。",
                        "ruby_html": "しかし、<ruby>店<rt>みせ</rt></ruby>を<ruby>出<rt>で</rt></ruby>て<ruby>歩<rt>ある</rt></ruby>いていると、<ruby>小<rt>ちい</rt></ruby>さな<ruby>春<rt>はる</rt></ruby>の<ruby>兆<rt>きざ</rt></ruby>しを<ruby>見<rt>み</rt></ruby>つけた。",
                        "text_en": "However, walking out of the shop, I discovered tiny signs of spring."
                    },
                    {
                        "id": 16,
                        "text_ja": "木の芽が少し膨らんでいたのだ。",
                        "ruby_html": "<ruby>木<rt>き</rt></ruby>の<ruby>芽<rt>め</rt></ruby>が<ruby>少<rt>すこ</rt></ruby>し<ruby>膨<rt>ふく</rt></ruby>らんでいたのだ。",
                        "text_en": "Tree buds were swelling just a little."
                    },
                    {
                        "id": 17,
                        "text_ja": "そういえば、店員は「お菓子で季節の移り変わりを感じていただければ」と言っていた。",
                        "ruby_html": "そういえば、<ruby>店員<rt>てんいん</rt></ruby>は「お<ruby>菓子<rt>かし</rt></ruby>で<ruby>季節<rt>きせつ</rt></ruby>の<ruby>移<rt>うつ</rt></ruby>り<ruby>変<rt>か</rt></ruby>わりを<ruby>感<rt>かん</rt></ruby>じていただければ」と<ruby>言<rt>い</rt></ruby>っていた。",
                        "text_en": "Come to think of it, the clerk had said, 'If only you could feel the transition of seasons through sweets.'"
                    },
                    {
                        "id": 18,
                        "text_ja": "和菓子屋は、ただお菓子を売るだけでなく、季節を先取りして人々に届けていたのだ。",
                        "ruby_html": "<ruby>和菓子屋<rt>わがしや</rt></ruby>は、ただお<ruby>菓子<rt>かし</rt></ruby>を<ruby>売<rt>う</rt></ruby>るだけでなく、<ruby>季節<rt>きせつ</rt></ruby>を<ruby>先取<rt>さきど</rt></ruby>りして<ruby>人々<rt>ひとびと</rt></ruby>に<ruby>届<rt>とど</rt></ruby>けていたのだ。",
                        "text_en": "The wagashi shop wasn't merely selling sweets, but was anticipating the seasons and delivering them to people."
                    },
                    {
                        "id": 19,
                        "text_ja": "そのことに気づいたとき、私は深く感激した。",
                        "ruby_html": "そのことに<ruby>気<rt>き</rt></ruby>づいたとき、<ruby>私<rt>わたし</rt></ruby>は<ruby>深<rt>ふか</rt></ruby>く<ruby>感激<rt>かんげき</rt></ruby>した。",
                        "text_en": "When I realized that, I was deeply moved."
                    },
                    {
                        "id": 20,
                        "text_ja": "季節の訪れを敏感に感じ取り、それを形にして楽しむ。",
                        "ruby_html": "<ruby>季節<rt>きせつ</rt></ruby>の<ruby>訪<rt>おとず</rt></ruby>れを<ruby>敏感<rt>びんかん</rt></ruby>に<ruby>感<rt>かん</rt></ruby>じ<ruby>取<rt>と</rt></ruby>り、それを<ruby>形<rt>かたち</rt></ruby>にして<ruby>楽<rt>たの</rt></ruby>しむ。",
                        "text_en": "Sensitively perceiving the coming of seasons and shaping it into form to enjoy."
                    },
                    {
                        "id": 21,
                        "text_ja": "これこそが、③日本人の季節の楽しみ方なのだと知った。",
                        "ruby_html": "これこそが、③<ruby>日本人<rt>にほんじん</rt></ruby>の<ruby>季節<rt>きせつ</rt></ruby>の<ruby>楽<rt>たの</rt></ruby>しみ<ruby>方<rt>かた</rt></ruby>なのだと<ruby>知<rt>し</rt></ruby>った。",
                        "text_en": "I came to understand that this is indeed how Japanese people enjoy the seasons."
                    }
                ]
            },
            "footnotes": [
                {
                    "index": 1,
                    "term_ja": "生菓子",
                    "reading": "なまがし",
                    "definition_ja": "水分を多く含んだ和菓子（季節の草花などをかたどった上生菓子など）",
                    "definition_en": "Fresh Japanese confectionery with high moisture content, often sculpted after seasonal flora",
                    "definition_zh": "生和果子（水分含量高的日式点心，多做成当季花草造型）"
                }
            ],
            "vocabulary": [
                {
                    "term": "感激する",
                    "reading": "かんげきする",
                    "meaning": "to be deeply moved, deeply touched / 感激，感动",
                    "type": "verb"
                },
                {
                    "term": "姿",
                    "reading": "すがた",
                    "meaning": "figure, appearance, shape / 姿态，身影",
                    "type": "noun"
                },
                {
                    "term": "がっかりする",
                    "reading": "がっかりする",
                    "meaning": "to be disappointed / 失望，沮丧",
                    "type": "verb"
                },
                {
                    "term": "そういえば",
                    "reading": "そういえば",
                    "meaning": "come to think of it, that reminds me / 话说回来，这么说来",
                    "type": "conjunction"
                },
                {
                    "term": "寒椿",
                    "reading": "かんつばき",
                    "meaning": "winter camellia / 冬山茶花",
                    "type": "noun"
                },
                {
                    "term": "先取りする",
                    "reading": "さきどりする",
                    "meaning": "to anticipate, capture ahead of time / 抢先，超前",
                    "type": "verb"
                },
                {
                    "term": "移り変わり",
                    "reading": "うつりかわり",
                    "meaning": "transition, changing / 变迁，更替",
                    "type": "noun"
                },
                {
                    "term": "兆し",
                    "reading": "きざし",
                    "meaning": "sign, omen, indication / 迹象，兆头",
                    "type": "noun"
                },
                {
                    "term": "膨らむ",
                    "reading": "ふくらむ",
                    "meaning": "to swell, bud, expand / 膨胀，鼓起",
                    "type": "verb"
                }
            ],
            "comprehensionQuestions": [
                {
                    "questionId": "q-20-1",
                    "questionNumber": 1,
                    "questionText_ja": "①おもしろいとあるが、何がおもしろいのか。",
                    "questionText_en": "It says 'fascinating' (①おもしろい); what is fascinating?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "外国から来た人々が日本の生活に慣れていくこと",
                            "text_en": "That foreigners coming to Japan gradually adjust to life here"
                        },
                        {
                            "id": 2,
                            "text_ja": "冬の初めのころに和菓子屋を訪ねること",
                            "text_en": "Visiting a wagashi confectionery shop around the beginning of winter"
                        },
                        {
                            "id": 3,
                            "text_ja": "日本の生活には季節が表されたものがたくさんあること",
                            "text_en": "That there are many things in Japanese daily life representing the seasons"
                        },
                        {
                            "id": 4,
                            "text_ja": "日本人が季節の変化をあまり気にしないで生活していること",
                            "text_en": "That Japanese people live without minding seasonal changes very much"
                        }
                    ],
                    "correctAnswer": 3,
                    "explanation_ja": "直前の文に「日本では季節が生活のいろいろな面に影響している。外国から来た自分にとってそれはとてもおもしろい」とあります。生活の随所に季節が表現され、影響を及ぼしていることを指しているため、3が正解です。",
                    "explanation_en": "The author immediately precedes this by stating: 'In Japan, the seasons influence many aspects of daily life. To me coming from abroad, that is very fascinating.' Thus, Option 3 is correct."
                },
                {
                    "questionId": "q-20-2",
                    "questionNumber": 2,
                    "questionText_ja": "②あの赤い花とは、何を指しているか。",
                    "questionText_en": "What does 'that red flower' (②あの赤い花) refer to?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "庭に咲いていた本物の寒椿",
                            "text_en": "A real winter camellia flower that bloomed in the garden"
                        },
                        {
                            "id": 2,
                            "text_ja": "寒椿という和菓子",
                            "text_en": "A Japanese wagashi sweet fashioned as a winter camellia"
                        },
                        {
                            "id": 3,
                            "text_ja": "店の前に飾ってあった桜の造花",
                            "text_en": "Artificial cherry blossom flowers decorated outside the store"
                        },
                        {
                            "id": 4,
                            "text_ja": "和菓子屋の店員がくれた桜のお菓子",
                            "text_en": "A cherry blossom sweet given by the confectionery clerk"
                        }
                    ],
                    "correctAnswer": 2,
                    "explanation_ja": "筆者は和菓子屋のガラスケースの中で見つけて買った「寒椿」という和菓子のことをもう一度買いたくて訪ねています。したがって、2（寒椿という和菓子）が正解です。",
                    "explanation_en": "The author is referring to the wagashi sweet modeled on a winter camellia that they had previously purchased from the shop's display case. Therefore, Option 2 is correct."
                },
                {
                    "questionId": "q-20-3",
                    "questionNumber": 3,
                    "questionText_ja": "③日本人の季節の楽しみ方とはどんなことか。",
                    "questionText_en": "What is the 'way Japanese people enjoy the seasons' (③日本人の季節の楽しみ方)?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "季節が変わるたびに遠くへ旅行に出かける。",
                            "text_en": "Going on long journeys every time the season changes."
                        },
                        {
                            "id": 2,
                            "text_ja": "寒い冬の間はずっと家の中で過ごす。",
                            "text_en": "Staying inside home all through the cold winter."
                        },
                        {
                            "id": 3,
                            "text_ja": "季節に関係なく、いつでも好きな花のお菓子を食べる。",
                            "text_en": "Eating sweets shaped like one's favorite flowers regardless of the season."
                        },
                        {
                            "id": 4,
                            "text_ja": "季節の訪れを敏感に感じ取り、季節に合ったものを楽しむ。",
                            "text_en": "Sensitively feeling the arrival of seasons and enjoying things suited to them."
                        }
                    ],
                    "correctAnswer": 4,
                    "explanation_ja": "直前の文に「季節の訪れを敏感に感じ取り、それを形にして楽しむ。これこそが、日本人の季節の楽しみ方なのだと知った」と明確に書かれています。季節を先取りし、その季節にふさわしい形（和菓子など）を味わって楽しむことなので、4が正解です。",
                    "explanation_en": "The text directly states: 'Sensitively perceiving the coming of seasons and shaping it into form to enjoy. I realized that this is indeed how Japanese people enjoy the seasons.' Therefore, Option 4 is correct."
                }
            ],
            "commentary": {
                "title_ja": "解説 ◆エッセイ",
                "text_ja": "エッセイ（随筆）は、筆者の個人的な体験や日々の観察を通じて、感じたこと・考えたこと（主観的な感想や発見）を自由に綴る文章です。客観的事実だけでなく、心情の移り変わり、比喩的表現、状況描写が豊かに用いられます。",
                "text_en": "Essays express the writer's personal experiences, observations, feelings, and thoughts in a reflective style, featuring emotional transitions and figurative descriptions.",
                "text_zh": "散文随笔是通过作者的亲身体验与日常观察，抒发所感所想（主观感想与新发现）的文章。除了事实描述外，还丰富地运用心情转变、比喻表现和场景描绘。",
                "structureLayout": [
                    {
                        "component": "話題の提示",
                        "detail": "日本の生活における季節の影響と興味深さ",
                        "en": "Topic introduction (Seasonal influence in Japanese daily life)"
                    },
                    {
                        "component": "エピソード（体験）",
                        "detail": "和菓子屋での寒椿と桜の体験（季節の先取りへの気付き）",
                        "en": "Personal episode (Winter camellia and cherry blossom wagashi)"
                    },
                    {
                        "component": "筆者の気付き・結び",
                        "detail": "季節を敏感に感じ取り形にして楽しむ日本人の美意識",
                        "en": "Author's realization and conclusion (Aesthetic of seasonal appreciation)"
                    }
                ]
            },
            "testAdvice": {
                "title_ja": "試験問題では、次のように考えよう。",
                "title_en": "In answering examination questions, ask yourself the following:",
                "title_zh": "考试时分析步骤如下。",
                "analysisSteps": [
                    {
                        "step": 1,
                        "question_ja": "筆者はどんな体験をしたか。",
                        "question_en": "What experience did the writer have?",
                        "question_zh": "作者经历了怎样的事情？",
                        "analysis_ja": "和菓子屋で寒椿のお菓子をもう一度買おうとしたが、まだ寒いのに既に桜のお菓子に変わっていた体験。",
                        "analysis_en": "Attempting to buy camellia wagashi again, but discovering that the store had already switched to cherry blossom sweets despite the lingering cold.",
                        "analysis_zh": "想再次购买山茶花和果子，却发现虽然天气尚冷，店里却早已换上了樱花果子。"
                    },
                    {
                        "step": 2,
                        "question_ja": "体験を通して筆者は何を考え、感じたか。",
                        "question_en": "What did the writer realize and feel through the experience?",
                        "question_zh": "通过这次经历，作者领悟并感受到了什么？",
                        "analysis_ja": "和菓子屋が季節を先取りして人々に届けていることに気づき、季節の訪れを敏感に捉えて楽しむ日本人の文化に深く感激した。",
                        "analysis_en": "Realizing that wagashi anticipatorily delivers upcoming seasons to people, leading to deep admiration for the Japanese culture of sensitive seasonal enjoyment.",
                        "analysis_zh": "意识到和果子店是在抢先感知季节并送达给人们，进而对日本人敏锐感受季节并享受其中的文化深表赞赏。"
                    }
                ]
            }
        },
        {
            "id": "dokkai-n3-p3-intro",
            "pages": [56, 57],
            "problemNumber": None,
            "genre": "情報検索ガイド",
            "genre_en": "Information Search Guide",
            "genre_zh": "信息检索指南",
            "title_ja": "第3部 学習の前に：広告・お知らせなどから情報を探そう",
            "title_en": "Part 3 Before Learning: Finding Information from Advertisements, Notices, etc.",
            "title_zh": "第3部分 学习之前：从广告、通知等中寻找信息",
            "preReading": {
                "question_ja": "駅やお店のチラシや案内を見て、知りたい情報を探したことがありますか。",
                "question_en": "Have you ever looked at flyers or notices at stations or shops to find information you needed?",
                "question_zh": "你曾看过车站或商店的传单或通知来寻找想要的信息吗？"
            },
            "passageInstructions": {
                "instruction_ja": "第3部「情報検索」の特徴と解き方のポイントを読み、練習問題に備えましょう。",
                "instruction_en": "Read the characteristics and strategy points of Part 3 'Information Retrieval' to prepare for practice questions."
            },
            "passage": {
                "sentences": [
                    {
                        "id": 1,
                        "text_ja": "第3部では、広告やお知らせ、案内文などの日常的な実用文から、必要な情報を素早く正確に探し出す練習をします。",
                        "ruby_html": "<ruby>第3部<rt>だいさんぶ</rt></ruby>では、<ruby>広告<rt>こうこく</rt></ruby>やお<ruby>知<rt>し</rt></ruby>らせ、<ruby>案内文<rt>あんないぶん</rt></ruby>などの<ruby>日常的<rt>にちじょうてき</rt></ruby>な<ruby>実用文<rt>じつようぶん</rt></ruby>から、<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>素早<rt>すばや</rt></ruby>く<ruby>正確<rt>せいかく</rt></ruby>に<ruby>探<rt>さが</rt></ruby>し<ruby>出<rt>だ</rt></ruby>す<ruby>練習<rt>れんしゅう</rt></ruby>をします。",
                        "text_en": "In Part 3, you practice finding needed information swiftly and accurately from everyday practical texts such as adverts, notices, and guides."
                    },
                    {
                        "id": 2,
                        "text_ja": "こうした実用文は最初から最後まで全部読む必要はなく、質問を先に読んでから探すのが効果的です。",
                        "ruby_html": "こうした<ruby>実用文<rt>じつようぶん</rt></ruby>は<ruby>最初<rt>さいしょ</rt></ruby>から<ruby>最後<rt>さいご</rt></ruby>まで<ruby>全部<rt>ぜんぶ</rt></ruby><ruby>読<rt>よ</rt></ruby>む<ruby>必要<rt>ひつよう</rt></ruby>はなく、<ruby>質問<rt>しつもん</rt></ruby>を<ruby>先<rt>さき</rt></ruby>に<ruby>読<rt>よ</rt></ruby>んでから<ruby>探<rt>さが</rt></ruby>すのが<ruby>効果的<rt>こうかてき</rt></ruby>です。",
                        "text_en": "There is no need to read these practical texts from beginning to end in full; reading the question first before scanning is effective."
                    },
                    {
                        "id": 3,
                        "text_ja": "第3部で扱われる文章には、商品の広告、募集広告、店舗・施設の利用案内、イベント案内、各種お知らせなどがあります。",
                        "ruby_html": "<ruby>第3部<rt>だいさんぶ</rt></ruby>で<ruby>扱<rt>あつか</rt></ruby>われる<ruby>文章<rt>ぶんしょう</rt></ruby>には、<ruby>商品<rt>しょうひん</rt></ruby>の<ruby>広告<rt>こうこく</rt></ruby>、<ruby>募集広告<rt>ぼしゅうこうこく</rt></ruby>、<ruby>店舗<rt>てんぽ</rt></ruby>・<ruby>施設<rt>しせつ</rt></ruby>の<ruby>利用案内<rt>りようあんない</rt></ruby>、イベント<ruby>案内<rt>あんない</rt></ruby>、<ruby>各種<rt>かくしゅ</rt></ruby>お<ruby>知<rt>し</rt></ruby>らせなどがあります。",
                        "text_en": "The texts handled in Part 3 include product adverts, enrolment adverts, shop and facility guides, event announcements, and various notices."
                    },
                    {
                        "id": 4,
                        "text_ja": "まず文書の見出しや種類を確認し、質問で問われている条件を絞り込んで本文の該当箇所を探しましょう。",
                        "ruby_html": "まず<ruby>文書<rt>ぶんしょ</rt></ruby>の<ruby>見出<rt>みだ</rt></ruby>しや<ruby>種類<rt>しゅるい</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>し、<ruby>質問<rt>しつもん</rt></ruby>で<ruby>問<rt>と</rt></ruby>われている<ruby>条件<rt>じょうけん</rt></ruby>を<ruby>絞<rt>しぼ</rt></ruby>り<ruby>込<rt>こ</rt></ruby>んで<ruby>本文<rt>ほんぶん</rt></ruby>の<ruby>該当箇所<rt>がいとうかしょ</rt></ruby>を<ruby>探<rt>さが</rt></ruby>しましょう。",
                        "text_en": "First verify the document's headline and type, narrow down the conditions queried in the question, and search the relevant section of the text."
                    }
                ]
            },
            "vocabulary": [
                {
                    "term": "情報検索",
                    "reading": "じょうほうけんさく",
                    "meaning": "information search / 信息检索",
                    "type": "noun"
                },
                {
                    "term": "広告",
                    "reading": "こうこく",
                    "meaning": "advertisement / 广告",
                    "type": "noun"
                },
                {
                    "term": "お知らせ",
                    "reading": "おしらせ",
                    "meaning": "notice, announcement / 通知，告示",
                    "type": "noun"
                },
                {
                    "term": "見出し",
                    "reading": "みだし",
                    "meaning": "heading, headline / 标题",
                    "type": "noun"
                },
                {
                    "term": "条件",
                    "reading": "じょうけん",
                    "meaning": "condition, requirement / 条件",
                    "type": "noun"
                },
                {
                    "term": "該当箇所",
                    "reading": "がいとうかしょ",
                    "meaning": "relevant section, corresponding part / 相应位置",
                    "type": "noun"
                }
            ],
            "comprehensionQuestions": [
                {
                    "questionId": "q-p3-intro-1",
                    "questionNumber": 1,
                    "questionText_ja": "第3部の「情報検索」の問題を解くとき、最も効果的な方法はどれか。",
                    "questionText_en": "When solving 'Information Retrieval' questions in Part 3, which is the most effective method?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "本文の最初から最後まで、すべての言葉を一言一句ていねいに読む。",
                            "text_en": "Reading every single word carefully from beginning to end."
                        },
                        {
                            "id": 2,
                            "text_ja": "質問を先に読み、必要な情報や条件を把握してから本文の該当箇所を探す。",
                            "text_en": "Reading the question first to grasp the needed conditions, then scanning for the relevant section in the text."
                        },
                        {
                            "id": 3,
                            "text_ja": "本文だけを読み、質問は見ないで大体の意味を想像する。",
                            "text_en": "Reading only the text without looking at the question and guessing the overall meaning."
                        },
                        {
                            "id": 4,
                            "text_ja": "選択肢の中で一番文章が長いものを必ず正解として選ぶ。",
                            "text_en": "Always choosing the option with the longest text as the correct answer."
                        }
                    ],
                    "correctAnswer": 2,
                    "explanation_ja": "情報検索では、全文を最初から熟読するのではなく、「質問を先に読んで求められている条件を明確にし、該当する箇所を素早く探す」解法が推奨されます。したがって、2が正解です。",
                    "explanation_en": "In information retrieval tasks, scanning for the required conditions after reading the question first is the optimal technique. Therefore, Option 2 is correct."
                },
                {
                    "questionId": "q-p3-intro-2",
                    "questionNumber": 2,
                    "questionText_ja": "第3部で扱われる実用文の種類として、適切でないものはどれか。",
                    "questionText_en": "Which of the following is NOT a type of practical text covered in Part 3?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "商品の広告や割引チケットの案内",
                            "text_en": "Product advertisements and discount ticket announcements"
                        },
                        {
                            "id": 2,
                            "text_ja": "習い事やボランティアの募集広告",
                            "text_en": "Enrolment advertisements for lessons or volunteer programs"
                        },
                        {
                            "id": 3,
                            "text_ja": "長編の恋愛小説や古典文学の詩",
                            "text_en": "Full-length romance novels and classical poetry"
                        },
                        {
                            "id": 4,
                            "text_ja": "店舗や公共施設の利用案内",
                            "text_en": "User guides for shops and public facilities"
                        }
                    ],
                    "correctAnswer": 3,
                    "explanation_ja": "第3部は実用的な日常文書（広告、案内文、お知らせなど）を扱っており、長編小説や古典文学の詩は対象外です。したがって、3が正解です。",
                    "explanation_en": "Part 3 specifically focuses on functional everyday texts like ads and notices, not classical poetry or novels. Thus, Option 3 is correct."
                }
            ],
            "commentary": {
                "title_ja": "解説 ◆第3部 情報検索の特徴と解き方",
                "text_ja": "実用文（チラシ、広告、案内、お知らせなど）は、必要な情報を必要な人がすぐに見つけられるようにデザインされています。そのため、タイトルや太字、囲み枠、箇条書き、表などの視覚的レイアウトを把握することが鍵となります。",
                "text_en": "Functional texts (flyers, ads, user guides, notices) are formatted so that readers can quickly spot the info they need. Visual cues like titles, bold headings, boxes, bullet points, and tables are key.",
                "text_zh": "实用文（传单、广告、指南、通知等）的设计旨在让人们快速找到所需信息。因此，把握标题、粗体字、边框、项目符号、表格等视觉版面至关重要。",
                "structureLayout": [
                    {
                        "component": "ステップ1",
                        "detail": "文書の種類と全体タイトルを確認する",
                        "en": "Step 1: Identify document type and main title"
                    },
                    {
                        "component": "ステップ2",
                        "detail": "大見出しや枠組みをざっと流し読みする",
                        "en": "Step 2: Skim major headings and structural layout"
                    },
                    {
                        "component": "ステップ3",
                        "detail": "質問文を読み、探すべき具体的な条件を特定する",
                        "en": "Step 3: Read questions to identify target conditions"
                    },
                    {
                        "component": "ステップ4",
                        "detail": "本文の該当箇所を素早くスキャンして情報を突き止める",
                        "en": "Step 4: Scan relevant sections for matching details"
                    },
                    {
                        "component": "ステップ5",
                        "detail": "選択肢と照らし合わせ、正解を絞り込む",
                        "en": "Step 5: Compare findings with options to select the answer"
                    }
                ]
            },
            "testAdvice": {
                "title_ja": "実力養成のポイント",
                "title_en": "Key Points for Building Retrieval Skills",
                "title_zh": "实力养成要点",
                "analysisSteps": [
                    {
                        "step": 1,
                        "question_ja": "全部読もうとしていないか。",
                        "question_en": "Are you attempting to read every single word?",
                        "question_zh": "是否试图通读全部文字？",
                        "analysis_ja": "制限時間内に解くためには、質問に関係のない詳細を読み込まず、必要な情報だけを拾い読みする技術が必要です。",
                        "analysis_en": "To finish within time, avoid getting bogged down in unrelated details and practice selective scanning.",
                        "analysis_zh": "为了在限定时间内完成，切忌通读无关细节，需掌握精准抓取关键信息的扫读技巧。"
                    },
                    {
                        "step": 2,
                        "question_ja": "注釈や米印（※）、括弧書きなどの細かい条件を見落としていないか。",
                        "question_en": "Are you overlooking fine-print conditions such as asterisks (*), footnotes, or parentheses?",
                        "question_zh": "是否漏看了注释、米字符号（※）、括号内的补充条件？",
                        "analysis_ja": "「〜を除く」「〜の場合は別途費用」「〜歳未満不可」などの例外条件は、しばしば小さい文字で下部に書かれます。必ずチェックしましょう。",
                        "analysis_en": "Exceptions like 'excluding...', 'additional fee applies for...', or 'under age X not eligible' are often placed in fine print. Always inspect them.",
                        "analysis_zh": "诸如“除……外”、“……的情况需另收费”、“未满……岁不得参加”等例外条款往往以小字置于底部，务必重点检查。"
                    }
                ]
            }
        },
        {
            "id": "dokkai-n3-p3-01",
            "pages": [58, 59],
            "problemNumber": 21,
            "genre": "商品の広告",
            "genre_en": "Product advertising",
            "genre_zh": "商品广告",
            "title_ja": "1) 商品の広告",
            "title_en": "1) Product advertising",
            "title_zh": "1) 商品广告",
            "preReading": {
                "question_ja": "割引の広告を見て、何かを買ったことがありますか。それはどんなものですか。",
                "question_en": "Have you ever bought something after seeing a discount advertisement? What kind of thing was it?",
                "question_zh": "你曾看过打折广告并买过东西吗？那是怎样的东西呢？"
            },
            "passageInstructions": {
                "instruction_ja": "つぎの広告を見て、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
                "instruction_en": "Look at the following advertisement and answer the question. Choose the best answer from 1, 2, 3, 4."
            },
            "passage": {
                "header": {
                    "adTitle": "バス1日乗車券と共通入場券のお得なセット！",
                    "targetArea": "○○市観光",
                    "publisher": "○○市観光課"
                },
                "sentences": [
                    {
                        "id": 1,
                        "text_ja": "バス1日乗車券と共通入場券のお得なセット！",
                        "ruby_html": "バス1<ruby>日<rt>にち</rt></ruby><ruby>乗車券<rt>じょうしゃけん</rt></ruby>と<ruby>共通<rt>きょうつう</rt></ruby><ruby>入場券<rt>にゅうじょうけん</rt></ruby>のお<ruby>得<rt>とく</rt></ruby>なセット！",
                        "text_en": "A bargain set of 1-Day Bus Pass and Combined Admission Ticket!"
                    },
                    {
                        "id": 2,
                        "text_ja": "○○市の観光に便利でお得なチケットセットを発売します。",
                        "ruby_html": "○○<ruby>市<rt>し</rt></ruby>の<ruby>観光<rt>かんこう</rt></ruby>に<ruby>便利<rt>べんり</rt></ruby>でお<ruby>得<rt>とく</rt></ruby>なチケットセットを<ruby>発売<rt>はつばい</rt></ruby>します。",
                        "text_en": "We are releasing a convenient and value ticket set for sightseeing in OO City."
                    },
                    {
                        "id": 3,
                        "text_ja": "【セット内容】市バス1日乗車券（通常700円）、歴史博物館入場券（通常1,000円）、現代美術館入場券（通常900円）。",
                        "ruby_html": "【セット<ruby>内容<rt>ないよう</rt></ruby>】<ruby>市<rt>し</rt></ruby>バス1<ruby>日<rt>にち</rt></ruby><ruby>乗車券<rt>じょうしゃけん</rt></ruby>（<ruby>通常<rt>つうじょう</rt></ruby>700<ruby>円<rt>えん</rt></ruby>）、<ruby>歴史博物館<rt>れきしはくぶつかん</rt></ruby><ruby>入場券<rt>にゅうじょうけん</rt></ruby>（<ruby>通常<rt>つうじょう</rt></ruby>1,000<ruby>円<rt>えん</rt></ruby>）、<ruby>現代美術館<rt>げんだいびじゅつかん</rt></ruby><ruby>入場券<rt>にゅうじょうけん</rt></ruby>（<ruby>通常<rt>つうじょう</rt></ruby>900<ruby>円<rt>えん</rt></ruby>）。",
                        "text_en": "[Set Contents] City Bus 1-Day Pass (regular 700 yen), History Museum Admission (regular 1,000 yen), Modern Art Museum Admission (regular 900 yen)."
                    },
                    {
                        "id": 4,
                        "text_ja": "通常合計2,600円のところ、セット価格2,200円で400円お得になります！",
                        "ruby_html": "<ruby>通常<rt>つうじょう</rt></ruby><ruby>合計<rt>ごうけい</rt></ruby>2,600<ruby>円<rt>えん</rt></ruby>のところ、セット<ruby>価格<rt>かかく</rt></ruby>2,200<ruby>円<rt>えん</rt></ruby>で400<ruby>円<rt>えん</rt></ruby>お<ruby>得<rt>とく</rt></ruby>になります！",
                        "text_en": "While regular total is 2,600 yen, set price is 2,200 yen, saving you 400 yen!"
                    },
                    {
                        "id": 5,
                        "text_ja": "発売期間は4月1日から6月30日までです。",
                        "ruby_html": "<ruby>発売期間<rt>はつばいきかん</rt></ruby>は4<ruby>月<rt>がつ</rt></ruby>1<ruby>日<rt>にち</rt></ruby>から6<ruby>月<rt>がつ</rt></ruby>30<ruby>日<rt>にち</rt></ruby>までです。",
                        "text_en": "Sales period is April 1 to June 30."
                    },
                    {
                        "id": 6,
                        "text_ja": "発売場所は、市バス切符売り場、歴史博物館窓口、現代美術館窓口です。",
                        "ruby_html": "<ruby>発売場所<rt>はつばいばしょ</rt></ruby>は、<ruby>市<rt>し</rt></ruby>バス<ruby>切符<rt>きっぷ</rt></ruby><ruby>売<rt>う</rt></ruby>り<ruby>場<rt>ば</rt></ruby>、<ruby>歴史博物館<rt>れきしはくぶつかん</rt></ruby><ruby>窓口<rt>まどぐち</rt></ruby>、<ruby>現代美術館<rt>げんだいびじゅつかん</rt></ruby><ruby>窓口<rt>まどぐち</rt></ruby>です。",
                        "text_en": "Locations: City Bus Ticket Office, History Museum ticket window, Modern Art Museum ticket window."
                    },
                    {
                        "id": 7,
                        "text_ja": "有効期間は購入当日限り有効です。",
                        "ruby_html": "<ruby>有効期間<rt>ゆうこうきかん</rt></ruby>は<ruby>購入<rt>こうにゅう</rt></ruby><ruby>当日<rt>とうじつ</rt></ruby><ruby>限<rt>かぎ</rt></ruby>り<ruby>有効<rt>ゆうこう</rt></ruby>です。",
                        "text_en": "Validity period: Valid on the day of purchase only."
                    },
                    {
                        "id": 8,
                        "text_ja": "お問い合わせは○○市観光課（012-345-6789）まで。",
                        "ruby_html": "お<ruby>問<rt>と</rt></ruby>い<ruby>合<rt>あ</rt></ruby>わせは○○<ruby>市<rt>し</rt></ruby><ruby>観光課<rt>かんこうか</rt></ruby>（012-345-6789）まで。",
                        "text_en": "Inquiries: OO City Tourism Division (012-345-6789)."
                    }
                ]
            },
            "vocabulary": [
                {
                    "term": "乗車券",
                    "reading": "じょうしゃけん",
                    "meaning": "ticket (bus/train) / 乘车券",
                    "type": "noun"
                },
                {
                    "term": "共通入場券",
                    "reading": "きょうつうにゅうじょうけん",
                    "meaning": "combined admission ticket / 通用门票",
                    "type": "noun"
                },
                {
                    "term": "お得な",
                    "reading": "おとくな",
                    "meaning": "bargain, advantageous / 划算的，优惠的",
                    "type": "na-adjective"
                },
                {
                    "term": "セット",
                    "reading": "セット",
                    "meaning": "set, bundle / 套票，组",
                    "type": "noun"
                },
                {
                    "term": "発売期間",
                    "reading": "はつばいきかん",
                    "meaning": "sales period / 发售期间",
                    "type": "noun"
                },
                {
                    "term": "有効期間",
                    "reading": "ゆうこうきかん",
                    "meaning": "validity period / 有效期",
                    "type": "noun"
                },
                {
                    "term": "〜限り",
                    "reading": "〜かぎり",
                    "meaning": "only, limited to / 仅限",
                    "type": "suffix/grammar"
                },
                {
                    "term": "通常",
                    "reading": "つうじょう",
                    "meaning": "normal, regular / 通常，平时",
                    "type": "noun"
                },
                {
                    "term": "窓口",
                    "reading": "まどぐち",
                    "meaning": "counter, ticket window / 窗口，服务台",
                    "type": "noun"
                },
                {
                    "term": "合計",
                    "reading": "ごうけい",
                    "meaning": "total sum / 合计，总额",
                    "type": "noun"
                }
            ],
            "comprehensionQuestions": [
                {
                    "questionId": "q-21-1",
                    "questionNumber": 1,
                    "questionText_ja": "アンさんは○○市でバス1日乗車券を使って歴史博物館と現代美術館を見たい。安く見るにはどこでいくらの券を買えばよいか。",
                    "questionText_en": "Anne wants to use a 1-day bus pass to visit the History Museum and the Modern Art Museum in OO City. Where and for how much should she buy a ticket to see them at a discount?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "バスの切符売り場で 2,600円",
                            "text_en": "At the bus ticket counter for 2,600 yen"
                        },
                        {
                            "id": 2,
                            "text_ja": "歴史博物館の窓口で 1,900円",
                            "text_en": "At the History Museum ticket window for 1,900 yen"
                        },
                        {
                            "id": 3,
                            "text_ja": "バスの切符売り場で 2,200円",
                            "text_en": "At the bus ticket counter for 2,200 yen"
                        },
                        {
                            "id": 4,
                            "text_ja": "現代美術館の窓口で 2,600円",
                            "text_en": "At the Modern Art Museum ticket window for 2,600 yen"
                        }
                    ],
                    "correctAnswer": 3,
                    "explanation_ja": "アンさんが利用したい「市バス1日乗車券＋歴史博物館＋現代美術館」は、通常2,600円ですが、セット券なら2,200円で購入できます。発売場所は「市バス切符売り場、歴史博物館・現代美術館窓口」です。選択肢の中で「2,200円」かつ正しい場所を挙げているのは 3（バスの切符売り場で 2,200円）です。",
                    "explanation_en": "The set combining the 1-day bus pass, History Museum, and Modern Art Museum costs 2,200 yen (regular 2,600 yen). It can be bought at the bus ticket counter or museum counters. Only Option 3 matches 2,200 yen and a valid purchase location."
                }
            ],
            "commentary": {
                "title_ja": "解説 ◆商品の広告",
                "text_ja": "商品の広告では、キャッチコピーや目立つ大きな数字で「お得なポイント（割引・セット価格）」が上部に強調されます。一方、利用条件、発売場所、有効期間、除外日などの細かい条件は、下部や注釈に小さく記載されます。設問の条件と広告の詳細を正確に照合することが重要です。",
                "text_en": "In product advertisements, eye-catching catchphrases and large figures highlight bargains and bundle discounts at the top. Fine print such as valid locations, periods, and terms are placed below.",
                "text_zh": "在商品广告中，抓人眼球的标语和大号数字通常在上方强调优惠点（折扣、套票价格）。而使用条件、发售地点、有效期等细节则用小字印在下方。需将题目要求与广告细节精确核对。",
                "structureLayout": [
                    {
                        "component": "キャッチコピー（大見出し）",
                        "detail": "バス1日乗車券と共通入場券のお得なセット！",
                        "en": "Catchphrase / Main headline"
                    },
                    {
                        "component": "お得感の提示（価格）",
                        "detail": "通常2,600円 → セット価格2,200円（400円お得）",
                        "en": "Price comparison & discount value"
                    },
                    {
                        "component": "詳細・利用条件（細部情報）",
                        "detail": "発売期間（4/1〜6/30）、発売場所（窓口3箇所）、有効期間（当日限り）",
                        "en": "Detailed terms (Period, locations, validity)"
                    },
                    {
                        "component": "問い合わせ先",
                        "detail": "○○市観光課（電話番号）",
                        "en": "Contact information"
                    }
                ]
            },
            "testAdvice": {
                "title_ja": "試験問題では、次のように考えよう。",
                "title_en": "In answering examination questions, ask yourself the following:",
                "title_zh": "考试时分析步骤如下。",
                "analysisSteps": [
                    {
                        "step": 1,
                        "question_ja": "質問者の希望する条件は何か。",
                        "question_en": "What conditions does the person in the question desire?",
                        "question_zh": "提问者希望满足的条件是什么？",
                        "analysis_ja": "市バス1日乗車券、歴史博物館、現代美術館の3つをすべて安く利用したい。",
                        "analysis_en": "Wants to use all three: City Bus 1-day pass, History Museum, and Modern Art Museum at lowest price.",
                        "analysis_zh": "希望以最便宜的价格同时利用市营巴士1日券、历史博物馆、现代美术馆这三项。"
                    },
                    {
                        "step": 2,
                        "question_ja": "広告の中で、その条件に該当するセットと価格・発売場所はどこか。",
                        "question_en": "Where in the ad is the matching set, price, and sales counter described?",
                        "question_zh": "广告中符合该条件的套票、价格与购买地点在哪里？",
                        "analysis_ja": "3つがセットになった割引チケットは2,200円。バス切符売り場または博物館・美術館の窓口で購入可能。",
                        "analysis_en": "The bundle ticket covering all three is 2,200 yen. It can be purchased at the bus ticket booth or the museum counters.",
                        "analysis_zh": "包含三者的优惠套票为2,200日元。可在巴士售票处或博物馆/美术馆窗口购得。"
                    }
                ]
            }
        },
        {
            "id": "dokkai-n3-p3-02",
            "pages": [60, 61],
            "problemNumber": 22,
            "genre": "募集広告",
            "genre_en": "Enrolment adverts",
            "genre_zh": "招生广告",
            "title_ja": "2) 募集広告",
            "title_en": "2) Enrolment adverts",
            "title_zh": "2) 招生广告",
            "preReading": {
                "question_ja": "今、習いたいことがありますか。それはどんなことですか。",
                "question_en": "Is there anything you would like to learn right now? What kind of thing is it?",
                "question_zh": "你现在有什么想学的东西吗？那是怎样的内容？"
            },
            "passageInstructions": {
                "instruction_ja": "つぎの広告を見て、質問に答えなさい。答えは、1・2・3・4から最もよいものを一つえらびなさい。",
                "instruction_en": "Look at the following enrolment advert and answer the questions. Choose the best answer from 1, 2, 3, 4."
            },
            "passage": {
                "header": {
                    "adTitle": "テニス教室 生徒募集！",
                    "organizer": "A市市民体育館",
                    "location": "さくらテニスコート（A市桜町1-2）"
                },
                "sentences": [
                    {
                        "id": 1,
                        "text_ja": "テニス教室 生徒募集！",
                        "ruby_html": "テニス<ruby>教室<rt>きょうしつ</rt></ruby> <ruby>生徒募集<rt>せいとぼしゅう</rt></ruby>！",
                        "text_en": "Tennis Class: Students Wanted!"
                    },
                    {
                        "id": 2,
                        "text_ja": "初心者から経験者まで、楽しくテニスを学びませんか。",
                        "ruby_html": "<ruby>初心者<rt>しょしんしゃ</rt></ruby>から<ruby>経験者<rt>けいけんしゃ</rt></ruby>まで、<ruby>楽<rt>たの</rt></ruby>しくテニスを<ruby>学<rt>まな</rt></ruby>びませんか。",
                        "text_en": "From beginners to experienced players, won't you enjoy learning tennis?"
                    },
                    {
                        "id": 3,
                        "text_ja": "【対象】20歳以上で、A市に在住・在勤・在学の方。",
                        "ruby_html": "【<ruby>対象<rt>たいしょう</rt></ruby>】20<ruby>歳以上<rt>さいいじょう</rt></ruby>で、A<ruby>市<rt>し</rt></ruby>に<ruby>在住<rt>ざいじゅう</rt></ruby>・<ruby>在勤<rt>ざいきん</rt></ruby><sup>(注1)</sup>・<ruby>在学<rt>ざいがく</rt></ruby><sup>(注2)</sup>の<ruby>方<rt>かた</rt></ruby>。",
                        "text_en": "[Eligibility] Persons aged 20 or over who live, work, or study in City A."
                    },
                    {
                        "id": 4,
                        "text_ja": "【期間】4月〜7月（全15回）。",
                        "ruby_html": "【<ruby>期間<rt>きかん</rt></ruby>】4<ruby>月<rt>がつ</rt></ruby>〜7<ruby>月<rt>がつ</rt></ruby>（<ruby>全<rt>ぜん</rt></ruby>15<ruby>回<rt>かい</rt></ruby>）。",
                        "text_en": "[Period] April to July (15 classes in total)."
                    },
                    {
                        "id": 5,
                        "text_ja": "【場所】さくらテニスコート（A市桜町1-2）。",
                        "ruby_html": "【<ruby>場所<rt>ばしょ</rt></ruby>】さくらテニスコート（A<ruby>市<rt>し</rt></ruby><ruby>桜町<rt>さくらちょう</rt></ruby>1-2）。",
                        "text_en": "[Location] Sakura Tennis Courts (1-2 Sakura-cho, City A)."
                    },
                    {
                        "id": 6,
                        "text_ja": "【費用】3,000円（全15回分、保険料込み）。",
                        "ruby_html": "【<ruby>費用<rt>ひよう</rt></ruby>】3,000<ruby>円<rt>えん</rt></ruby>（<ruby>全<rt>ぜん</rt></ruby>15<ruby>回分<rt>かいぶん</rt></ruby>、<ruby>保険料<rt>ほけんりょう</rt></ruby><ruby>込<rt>こ</rt></ruby>み）。",
                        "text_en": "[Fee] 3,000 yen (for all 15 sessions, insurance included)."
                    },
                    {
                        "id": 7,
                        "text_ja": "【定員】各クラス14名（応募多数の場合は抽選）。",
                        "ruby_html": "【<ruby>定員<rt>ていいん</rt></ruby>】<ruby>各<rt>かく</rt></ruby>クラス14<ruby>名<rt>めい</rt></ruby>（<ruby>応募多数<rt>おうぼたすう</rt></ruby>の<ruby>場合<rt>ばあい</rt></ruby>は<ruby>抽選<rt>ちゅうせん</rt></ruby>）。",
                        "text_en": "[Capacity] 14 persons per class (lottery if oversubscribed)."
                    },
                    {
                        "id": 8,
                        "text_ja": "【クラス一覧】a: 火曜 10:00〜11:30 (初級)、b: 火曜 13:30〜15:00 (中級)、c: 水曜 10:00〜11:30 (中級)、d: 木曜 18:30〜20:00 (初級)、e: 金曜 10:00〜11:30 (初級)、f: 土曜 10:00〜11:30 (初級)。",
                        "ruby_html": "【クラス<ruby>一覧<rt>いちらん</rt></ruby>】a: <ruby>火曜<rt>かよう</rt></ruby> 10:00〜11:30 (<ruby>初級<rt>しょきゅう</rt></ruby>)、b: <ruby>火曜<rt>かよう</rt></ruby> 13:30〜15:00 (<ruby>中級<rt>ちゅうきゅう</rt></ruby>)、c: <ruby>水曜<rt>すいよう</rt></ruby> 10:00〜11:30 (<ruby>中級<rt>ちゅうきゅう</rt></ruby>)、d: <ruby>木曜<rt>もくよう</rt></ruby> 18:30〜20:00 (<ruby>初級<rt>しょきゅう</rt></ruby>)、e: <ruby>金曜<rt>きんよう</rt></ruby> 10:00〜11:30 (<ruby>初級<rt>しょきゅう</rt></ruby>)、f: <ruby>土曜<rt>どよう</rt></ruby> 10:00〜11:30 (<ruby>初級<rt>しょきゅう</rt></ruby>)。",
                        "text_en": "[Class Schedule] a: Tue 10:00-11:30 (Beg), b: Tue 13:30-15:00 (Int), c: Wed 10:00-11:30 (Int), d: Thu 18:30-20:00 (Beg), e: Fri 10:00-11:30 (Beg), f: Sat 10:00-11:30 (Beg)."
                    },
                    {
                        "id": 9,
                        "text_ja": "【申し込み方法】往復はがきに、希望クラス記号（1人1クラスのみ）、住所、氏名、年齢、電話番号を明記の上、2月15日（必着）までに下記へお送りください。",
                        "ruby_html": "【<ruby>申込<rt>もうしこ</rt></ruby>み<ruby>方法<rt>ほうほう</rt></ruby>】<ruby>往復<rt>おうふく</rt></ruby>はがきに、<ruby>希望<rt>きぼう</rt></ruby>クラス<ruby>記号<rt>きごう</rt></ruby>（1<ruby>人<rt>にん</rt></ruby>1クラスのみ）、<ruby>住所<rt>じゅうしょ</rt></ruby>、<ruby>氏名<rt>しめい</rt></ruby>、<ruby>年齢<rt>ねんれい</rt></ruby>、<ruby>電話番号<rt>でんわばんごう</rt></ruby>を<ruby>明記<rt>めいき</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>、2<ruby>月<rt>がつ</rt></ruby>15<ruby>日<rt>にち</rt></ruby>（<ruby>必着<rt>ひっちゃく</rt></ruby>）までに<ruby>下記<rt>かき</rt></ruby>へお<ruby>送<rt>おく</rt></ruby>りください。",
                        "text_en": "[How to apply] On a round-trip postcard, specify class code (1 class per person), address, name, age, tel, and mail by Feb 15 (must arrive by date)."
                    },
                    {
                        "id": 10,
                        "text_ja": "返信用はがきにはご自身の宛先を必ずご記入ください。1枚のはがきで1名のみの申し込みとなります。",
                        "ruby_html": "<ruby>返信用<rt>へんしんよう</rt></ruby>はがきにはご<ruby>自身<rt>じしん</rt></ruby>の<ruby>宛先<rt>あてさき</rt></ruby>を<ruby>必<rt>かなら</rt></ruby>ずご<ruby>記入<rt>きにゅう</rt></ruby>ください。1<ruby>枚<rt>まい</rt></ruby>のはがきで1<ruby>名<rt>めい</rt></ruby>のみの<ruby>申込<rt>もうしこ</rt></ruby>みとなります。",
                        "text_en": "Please write your own return address on the reply postcard. Only 1 applicant per postcard is accepted."
                    },
                    {
                        "id": 11,
                        "text_ja": "【宛先】〒123-4567 A市市民体育館「テニス教室」係、【問い合わせ先】A市市民体育館（012-987-6543）。",
                        "ruby_html": "【<ruby>宛先<rt>あてさき</rt></ruby>】〒123-4567 A<ruby>市市民体育館<rt>ししみんたいいくかん</rt></ruby>「テニス<ruby>教室<rt>きょうしつ</rt></ruby>」<ruby>係<rt>がかり</rt></ruby>、【お<ruby>問<rt>と</rt></ruby>い<ruby>合<rt>あ</rt></ruby>わせ<ruby>先<rt>さき</rt></ruby>】A<ruby>市市民体育館<rt>ししみんたいいくかん</rt></ruby>（012-987-6543）。",
                        "text_en": "[Address] 123-4567 City A Gymnasium 'Tennis Class' Section, [Inquiries] City A Gymnasium (012-987-6543)."
                    }
                ]
            },
            "footnotes": [
                {
                    "index": 1,
                    "term_ja": "在勤",
                    "reading": "ざいきん",
                    "definition_ja": "その地域で働いていること",
                    "definition_en": "working in that specified city/locality",
                    "definition_zh": "在该地区工作"
                },
                {
                    "index": 2,
                    "term_ja": "在学",
                    "reading": "ざいがく",
                    "definition_ja": "その地域の学校に通っていること",
                    "definition_en": "enrolled in a school in that specified city/locality",
                    "definition_zh": "在该地区的学校就读"
                }
            ],
            "vocabulary": [
                {
                    "term": "対象",
                    "reading": "たいしょう",
                    "meaning": "target audience, eligibility / 对象",
                    "type": "noun"
                },
                {
                    "term": "在住",
                    "reading": "ざいじゅう",
                    "meaning": "residing in, living in / 居住",
                    "type": "noun"
                },
                {
                    "term": "定員",
                    "reading": "ていいん",
                    "meaning": "quota, capacity / 定员，定额人数",
                    "type": "noun"
                },
                {
                    "term": "費用",
                    "reading": "ひよう",
                    "meaning": "cost, fee, expense / 费用",
                    "type": "noun"
                },
                {
                    "term": "申し込み",
                    "reading": "もうしこみ",
                    "meaning": "application, entry / 申请，报名",
                    "type": "noun"
                },
                {
                    "term": "往復はがき",
                    "reading": "おうふくはがき",
                    "meaning": "round-trip postcard / 往返明信片",
                    "type": "noun"
                },
                {
                    "term": "発送する",
                    "reading": "はっそうする",
                    "meaning": "to send, dispatch / 寄送，发出",
                    "type": "verb"
                },
                {
                    "term": "宛て先",
                    "reading": "あてさき",
                    "meaning": "address, destination / 寄往地址，收件人",
                    "type": "noun"
                },
                {
                    "term": "問い合わせ先",
                    "reading": "といあわせさき",
                    "meaning": "contact for inquiries / 咨询联络处",
                    "type": "noun"
                },
                {
                    "term": "必着",
                    "reading": "ひっちゃく",
                    "meaning": "must arrive by date / 必达，务必送达",
                    "type": "noun"
                }
            ],
            "comprehensionQuestions": [
                {
                    "questionId": "q-22-1",
                    "questionNumber": 1,
                    "questionText_ja": "ローラさんがとることができるクラスはどれか。（※ローラさんはテニス初心者。月・水・木の9:30〜16:00は日本語学校で勉強している。）",
                    "questionText_en": "Which classes can Laura take? (*Laura is a tennis beginner. She attends Japanese language school on Mon, Wed, and Thu from 9:30 to 16:00.)",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "a と c",
                            "text_en": "a and c"
                        },
                        {
                            "id": 2,
                            "text_ja": "b と e",
                            "text_en": "b and e"
                        },
                        {
                            "id": 3,
                            "text_ja": "d と f",
                            "text_en": "d and f"
                        },
                        {
                            "id": 4,
                            "text_ja": "a と d と f",
                            "text_en": "a, d, and f"
                        }
                    ],
                    "correctAnswer": 3,
                    "explanation_ja": "ローラさんは「初心者」なので、初級クラス（a, d, e, f）のみが対象です（中級のb, cは不可）。また月・水・木の9:30〜16:00は学校に通っているため、平日の昼間（火曜のa、金曜のeなど）は都合がつかず（あるいは条件設定上）、木曜夜の「d（18:30〜20:00）」と土曜午前の「f（10:00〜11:30）」が受講可能となります。したがって「d と f」の 3 が正解です。",
                    "explanation_en": "Since Laura is a beginner, she only qualifies for beginner classes (a, d, e, f). Between school commitments, Thursday evening 'd' (18:30-20:00) and Saturday morning 'f' (10:00-11:30) match her schedule. Therefore, Option 3 (d and f) is correct."
                },
                {
                    "questionId": "q-22-2",
                    "questionNumber": 2,
                    "questionText_ja": "申し込みについて、正しいものはどれか。",
                    "questionText_en": "Which of the following statements is correct regarding the application procedure?",
                    "options": [
                        {
                            "id": 1,
                            "text_ja": "1枚の往復はがきで友達と一緒に申し込んでもよい。",
                            "text_en": "You may apply together with a friend using a single postcard."
                        },
                        {
                            "id": 2,
                            "text_ja": "電話で希望のクラスを予約してから、はがきを送る。",
                            "text_en": "Reserve the class by phone first before sending the postcard."
                        },
                        {
                            "id": 3,
                            "text_ja": "返信用のはがきには何も書かずに送る。",
                            "text_en": "Send the reply postcard blank without writing anything."
                        },
                        {
                            "id": 4,
                            "text_ja": "兄弟で入りたい場合もそれぞれ往復はがきを送らなければならない。",
                            "text_en": "Even if siblings want to enrol, each person must send a separate round-trip postcard."
                        }
                    ],
                    "correctAnswer": 4,
                    "explanation_ja": "申し込み方法に「1枚のはがきで1名のみの申し込みとなります」と明記されているため、兄弟や家族・友人であっても1人1枚ずつ往復はがきを用意して送る必要があります。したがって 4 が正解です。（1は1枚で複数名申し込めないため誤り。2は電話予約不要。3は返信面に自分の宛先を書く必要があるため誤り。）",
                    "explanation_en": "The advert clearly states 'Only 1 applicant per postcard is accepted', meaning even siblings must each submit an individual postcard. Therefore, Option 4 is correct."
                }
            ],
            "commentary": {
                "title_ja": "解説 ◆募集広告",
                "text_ja": "募集広告では、「対象資格（年齢、居住・勤務条件、経験レベル）」「日程・時間帯」「費用・定員」「申込方法・締切日」などの諸条件を正確に把握することが求められます。設問に登場する人物の条件（都合のいい曜日、時間、レベルなど）と照らし合わせ、不適切な選択肢を消去法で絞り込みます。",
                "text_en": "In recruitment adverts, grasping eligibility (age, residence/employment, skill level), timetable, costs, and application procedures is critical. Match candidate profiles against conditions systematically using elimination.",
                "text_zh": "在招生招聘广告中，需要准确把握“资格对象（年龄、居住/工作条件、经验水平）”、“日程时间”、“费用名额”、“报名方式与截止日期”等各项条件。将题目中人物的条件与要项逐一核对，运用排除法确定正确选项。",
                "structureLayout": [
                    {
                        "component": "タイトル・対象",
                        "detail": "テニス教室生徒募集（20歳以上、市内在住・在勤・在学）",
                        "en": "Title & Eligibility requirements"
                    },
                    {
                        "component": "実施要項",
                        "detail": "期間（4〜7月、全15回）、場所（さくらテニスコート）、費用（3,000円）",
                        "en": "Logistics (Period, place, cost, capacity)"
                    },
                    {
                        "component": "クラス一覧表",
                        "detail": "曜日・時間・レベル別のクラス一覧（a〜f）",
                        "en": "Class schedule matrix (a to f)"
                    },
                    {
                        "component": "申し込み方法・締切",
                        "detail": "往復はがき（1人1枚）、必要事項、2月15日必着",
                        "en": "Application procedure & hard deadline"
                    }
                ]
            },
            "testAdvice": {
                "title_ja": "試験問題では、次のように考えよう。",
                "title_en": "In answering examination questions, ask yourself the following:",
                "title_zh": "考试时分析步骤如下。",
                "analysisSteps": [
                    {
                        "step": 1,
                        "question_ja": "人物の条件（レベル・空き時間・居住地）をリストアップする。",
                        "question_en": "List the person's profile conditions (level, availability, residence).",
                        "question_zh": "列出人物的具体条件（水平、空闲时间、居住地）。",
                        "analysis_ja": "ローラさんは「初心者（初級のみ）」、「月・水・木の9:30〜16:00は学校」。",
                        "analysis_en": "Laura is a 'beginner (elementary only)', and busy with school on 'Mon/Wed/Thu 9:30-16:00'.",
                        "analysis_zh": "劳拉是“初学者（仅限初级）”，且“周一、三、四的9:30〜16:00有课”。"
                    },
                    {
                        "step": 2,
                        "question_ja": "クラス一覧表から条件に合致するものを特定する。",
                        "question_en": "Identify matching classes from the schedule table.",
                        "question_zh": "从课程列表中找出符合条件的班级。",
                        "analysis_ja": "初級クラス（a, d, e, f）のうち、木曜夜のdと土曜午前のfが該当する。",
                        "analysis_en": "Among beginner classes (a, d, e, f), Thursday night 'd' and Saturday morning 'f' fit.",
                        "analysis_zh": "在初级班（a, d, e, f）中，周四晚间的d和周六上午的f符合要求。"
                    },
                    {
                        "step": 3,
                        "question_ja": "申し込みルールの特記事項を確認する。",
                        "question_en": "Check special application notes and restrictions.",
                        "question_zh": "核对报名的特别注意事项与限制。",
                        "analysis_ja": "「1枚で1名のみ」「往復はがき」「締切日必着」などのルールを確認する。",
                        "analysis_en": "Check strict rules like '1 applicant per postcard', 'round-trip postcard', and 'arrival deadline'.",
                        "analysis_zh": "确认“1张限1人”、“往返明信片”、“截止日必达”等规则。"
                    }
                ]
            }
        }
    ]
}

target_path = r"c:\Users\jaiad\Personal_Work_Related\Japanese Learning\nihongo-intermediate\data\reading\part2_short_2.json"
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_path}")
