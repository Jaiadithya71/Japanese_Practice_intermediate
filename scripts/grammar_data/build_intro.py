"""
Builder script for nihongo-intermediate/data/grammar/intro_and_guide.json
Transcribes Images 000-018:
- Cover & Publication metadata
- はじめに (Preface)
- 目次 (Table of Contents summary)
- 本書の使い方 (Book Structure & How to Use)
- 本書で使う記号 (Notation & Grammatical Connection Symbols)
- 問題紹介 (Exam Format & Sample Questions with full explanations)
"""

import json
from pathlib import Path

intro_data = {
    "metadata": {
        "book_title": "<ruby>新完全<rt>しんかんぜん</rt></ruby>マスター<ruby>文法<rt>ぶんぽう</rt></ruby> <ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby> N3",
        "book_title_romaji": "Shin Kanzen Master Bunpou JLPT N3",
        "english_title": "New Complete Master JLPT N3 Grammar",
        "authors": [
            "<ruby>友松<rt>ともまつ</rt></ruby><ruby>悦子<rt>えつこ</rt></ruby>",
            "<ruby>福島<rt>ふくしま</rt></ruby><ruby>佐知<rt>さち</rt></ruby>",
            "<ruby>中村<rt>なかむら</rt></ruby><ruby>則子<rt>のりこ</rt></ruby>"
        ],
        "publisher": "スリーエーネットワーク (3A Corporation)",
        "target_level": "JLPT N3",
        "pages_covered": "Cover - p.14 (Images 000-018)"
    },
    "preface": {
        "title": "<ruby>初<rt>はじ</rt></ruby>めに",
        "title_en": "Preface",
        "paragraphs": [
            {
                "japanese": "この『<ruby>新完全<rt>しんかんぜん</rt></ruby>マスター<ruby>文法<rt>ぶんぽう</rt></ruby> <ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby> N3』は、<ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby>N3に<ruby>合格<rt>ごうかく</rt></ruby>するための<ruby>実力<rt>じつりょく</rt></ruby>をつけることを<ruby>目指<rt>めざ</rt></ruby>す<ruby>学習書<rt>がくしゅうしょ</rt></ruby>です。",
                "english": "This book, 'Shin Kanzen Master JLPT N3 Grammar,' is a study textbook designed to build the necessary proficiency to pass the JLPT N3."
            },
            {
                "japanese": "<ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby>のN3では、<ruby>基礎的<rt>きそてき</rt></ruby>な<ruby>文法<rt>ぶんぽう</rt></ruby>から<ruby>中級<rt>ちゅうきゅう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>への<ruby>橋渡<rt>はしわた</rt></ruby>しとなる<ruby>重要<rt>じゅうよう</rt></ruby>な<ruby>文法項目<rt>ぶんぽうこうもく</rt></ruby>が<ruby>出題<rt>しゅつだい</rt></ruby>されます。これらをしっかりと<ruby>身<rt>み</rt></ruby>につけることは、<ruby>試験<rt>しけん</rt></ruby>の<ruby>合格<rt>ごうかく</rt></ruby>だけでなく、その<ruby>後<rt>ご</rt></ruby>のより<ruby>高度<rt>こうど</rt></ruby>な<ruby>日本語学習<rt>にほんごがくしゅう</rt></ruby>にとっても<ruby>不可欠<rt>ふかけつ</rt></ruby>です。",
                "english": "In JLPT N3, essential grammar items that serve as a bridge from elementary grammar to intermediate grammar are tested. Mastering these is crucial not only for passing the test, but also for future advanced Japanese studies."
            },
            {
                "japanese": "<ruby>本書<rt>ほんしょ</rt></ruby>は、「<ruby>問題紹介<rt>もんだいしょうかい</rt></ruby>」「<ruby>実力養成編<rt>じつりょくようせいへん</rt></ruby>」「<ruby>模擬試験<rt>もぎしけん</rt></ruby>」の3つの<ruby>部分<rt>ぶぶん</rt></ruby>で<ruby>構成<rt>こうせい</rt></ruby>されています。<ruby>実力養成編<rt>じつりょくようせいへん</rt></ruby>では、<ruby>文法項目<rt>ぶんぽうこうもく</rt></ruby>を<ruby>意味<rt>いみ</rt></ruby>や<ruby>機能<rt>きのう</rt></ruby>ごとにグループ<ruby>分<rt>わ</rt></ruby>けし、<ruby>形<rt>かたち</rt></ruby>の<ruby>接続<rt>せつぞく</rt></ruby>や<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>の<ruby>注意点<rt>ちゅういてん</rt></ruby>をわかりやすく<ruby>整理<rt>せいり</rt></ruby>しています。",
                "english": "This book consists of three main parts: 'Question Introduction,' 'Skill Building (Core Lessons),' and 'Mock Examination.' In the Skill Building section, grammar points are grouped by meaning and function, clearly organizing form connections and usage nuances."
            },
            {
                "japanese": "<ruby>多<rt>おお</rt></ruby>くの<ruby>練習問題<rt>れんしゅうもんだい</rt></ruby>を<ruby>解<rt>と</rt></ruby>くことで、<ruby>文法<rt>ぶんぽう</rt></ruby>の<ruby>知識<rt>ちしき</rt></ruby>を<ruby>確実<rt>かくじつ</rt></ruby>にし、<ruby>実際<rt>じっさい</rt></ruby>の<ruby>場面<rt>ばめん</rt></ruby>で<ruby>使<rt>つか</rt></ruby>える<ruby>力<rt>ちから</rt></ruby>を<ruby>養<rt>やしな</rt></ruby>うことができます。<ruby>学習者<rt>がくしゅうしゃ</rt></ruby>の<ruby>皆<rt>みな</rt></ruby>さんが<ruby>目標<rt>もくひょう</rt></ruby>を<ruby>達成<rt>たっせい</rt></ruby>されることを<ruby>心<rt>こころ</rt></ruby>から<ruby>願<rt>ねが</rt></ruby>っています。",
                "english": "By solving numerous practice questions, learners can solidify their grammatical knowledge and cultivate the ability to use it naturally in real-life situations. We sincerely hope that all learners achieve their goals."
            }
        ]
    },
    "book_guide": {
        "title": "<ruby>本書<rt>ほんしょ</rt></ruby>の<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>",
        "title_en": "How to Use This Book",
        "structure": [
            {
                "section": "<ruby>問題紹介<rt>もんだいしょうかい</rt></ruby>",
                "section_en": "Introduction to Question Types",
                "description": "<ruby>日本語能力試験<rt>にほんごのうりょくしけん</rt></ruby>N3の「<ruby>文法<rt>ぶんぽう</rt></ruby>」でどのような<ruby>形式<rt>けいしき</rt></ruby>の<ruby>問題<rt>もんだい</rt></ruby>が<ruby>出題<rt>しゅつだい</rt></ruby>されるかを<ruby>確認<rt>かくにん</rt></ruby>します。<ruby>問題<rt>もんだい</rt></ruby>1（<ruby>文法形式<rt>ぶんぽうけいしき</rt></ruby>の<ruby>判断<rt>はんだん</rt></ruby>）、<ruby>問題<rt>もんだい</rt></ruby>2（<ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>みたて）、<ruby>問題<rt>もんだい</rt></ruby>3（<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>）のそれぞれの<ruby>解<rt>と</rt></ruby>き<ruby>方<rt>かた</rt></ruby>のコツを<ruby>学<rt>まな</rt></ruby>びます。",
                "description_en": "Explains the question formats appearing on the JLPT N3 Grammar section: Question 1 (Grammatical Form Selection), Question 2 (Sentence Composition), and Question 3 (Text Grammar)."
            },
            {
                "section": "<ruby>実力養成編<rt>じつりょくようせいへん</rt></ruby>",
                "section_en": "Skill Building Section",
                "parts": [
                    {
                        "part_name": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>1",
                        "part_en": "Part 1: Sentence Grammar 1",
                        "description": "<ruby>意味<rt>いみ</rt></ruby>・<ruby>機能<rt>きのう</rt></ruby>ごとに<ruby>整理<rt>せいり</rt></ruby>された<ruby>文法項目<rt>ぶんぽうこうもく</rt></ruby>を<ruby>学習<rt>がくしゅう</rt></ruby>します。<ruby>形<rt>かたち</rt></ruby>の<ruby>接続<rt>せつぞく</rt></ruby>、<ruby>意味<rt>いみ</rt></ruby>、<ruby>例文<rt>れいぶん</rt></ruby>、<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>の<ruby>注意<rt>ちゅうい</rt></ruby>を<ruby>確認<rt>かくにん</rt></ruby>した<ruby>後<rt>あと</rt></ruby>、<ruby>練習問題<rt>れんしゅうもんだい</rt></ruby>で<ruby>定着<rt>ていちゃく</rt></ruby>を<ruby>図<rt>はか</rt></ruby>ります。"
                    },
                    {
                        "part_name": "<ruby>第<rt>だい</rt></ruby>2<ruby>部<rt>ぶ</rt></ruby> <ruby>文<rt>ぶん</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>2",
                        "part_en": "Part 2: Sentence Grammar 2",
                        "description": "<ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>みたて（<ruby>並<rt>なら</rt></ruby>べ<ruby>替<rt>か</rt></ruby>え<ruby>問題<rt>もんだい</rt></ruby>）に<ruby>焦点<rt>しょうてん</rt></ruby>を<ruby>当<rt>あ</rt></ruby>て、<ruby>修飾関係<rt>しゅうしょくかんけい</rt></ruby>や<ruby>文<rt>ぶん</rt></ruby>の<ruby>構造<rt>こうぞう</rt></ruby>を<ruby>正<rt>ただ</rt></ruby>しく<ruby>把握<rt>はあく</rt></ruby>する<ruby>力<rt>ちから</rt></ruby>を<ruby>養<rt>やしな</rt></ruby>います。"
                    },
                    {
                        "part_name": "<ruby>第<rt>だい</rt></ruby>3<ruby>部<rt>ぶ</rt></ruby> <ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>",
                        "part_en": "Part 3: Text Grammar",
                        "description": "<ruby>一<rt>ひと</rt></ruby>つのまとまった<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>中<rt>なか</rt></ruby>で、<ruby>文脈<rt>ぶんみゃく</rt></ruby>に<ruby>合<rt>あ</rt></ruby>った<ruby>適切<rt>てきせつ</rt></ruby>な<ruby>表現<rt>ひょうげん</rt></ruby>、<ruby>接続詞<rt>せつぞくし</rt></ruby>、<ruby>指示詞<rt>しじし</rt></ruby>などを<ruby>選<rt>えら</rt></ruby>ぶ<ruby>力<rt>ちから</rt></ruby>を<ruby>鍛<rt>きた</rt></ruby>えます。"
                    }
                ]
            },
            {
                "section": "<ruby>模擬試験<rt>もぎしけん</rt></ruby>",
                "section_en": "Mock Examination",
                "description": "<ruby>実際<rt>じっさい</rt></ruby>の<ruby>試験<rt>しけん</rt></ruby>と<ruby>同<rt>おな</rt></ruby>じ<ruby>形式<rt>けいしき</rt></ruby>・<ruby>問題数<rt>もんだいすう</rt></ruby>のテストで、これまでの<ruby>学習<rt>がくしゅう</rt></ruby>の<ruby>成果<rt>せいか</rt></ruby>を<ruby>測定<rt>そくてい</rt></ruby>します。",
                "description_en": "A full-length mock test matching the exact JLPT N3 Grammar format and question volume to evaluate learner mastery."
            }
        ]
    },
    "symbols_guide": {
        "title": "<ruby>本書<rt>ほんしょ</rt></ruby>で<ruby>使<rt>つか</rt></ruby>う<ruby>記号<rt>きごう</rt></ruby>",
        "title_en": "Symbols Used in This Book",
        "symbols": [
            {
                "symbol": "V",
                "name_ja": "<ruby>動詞<rt>どうし</rt></ruby>",
                "name_en": "Verb",
                "description": "V-辞書形（辞書形）、V-ない形、V-た形、V-ます（ます形語幹）、V-て形など",
                "description_en": "Verb forms: dictionary form, -nai form, -ta form, verb stem (masu stem), -te form, etc."
            },
            {
                "symbol": "A",
                "name_ja": "い<ruby>形容詞<rt>けいようし</rt></ruby>",
                "name_en": "i-Adjective",
                "description": "A-い（普通形）、A-くない、A-かった、A-く（副詞形）など",
                "description_en": "i-Adjectives: plain dictionary form, negative -kunai, past -katta, adverbial -ku, etc."
            },
            {
                "symbol": "Na",
                "name_ja": "な<ruby>形容詞<rt>けいようし</rt></ruby>",
                "name_en": "na-Adjective",
                "description": "Na-な、Na-である、Na-に（副詞形）、Na語幹など",
                "description_en": "na-Adjectives: with な, である, adverbial に, or pure stem."
            },
            {
                "symbol": "N",
                "name_ja": "<ruby>名詞<rt>めいし</rt></ruby>",
                "name_en": "Noun",
                "description": "N-の、N-である、Nそのものなど",
                "description_en": "Nouns: followed by の, である, or noun alone."
            },
            {
                "symbol": "普通形",
                "name_ja": "<ruby>普通形<rt>ふつうけい</rt></ruby>",
                "name_en": "Plain / Informal Form",
                "description": "V・A・Na・Nの普通形（丁寧形「です・ます」ではない形）。ただし、NaとNの現在肯定では「だ」が「な」や「である」に変わる場合がある。",
                "description_en": "Plain form of verbs, i-adj, na-adj, and nouns (non-polite). For Na and N present affirmative, 'だ' often shifts to 'な' or 'である'."
            },
            {
                "symbol": "★",
                "name_ja": "<ruby>重要<rt>じゅうよう</rt></ruby>マーク",
                "name_en": "Important Point",
                "description": "特に試験に出やすいポイントや注意すべき規則",
                "description_en": "Key test points or crucial grammatical rules."
            },
            {
                "symbol": "×",
                "name_ja": "<ruby>誤用<rt>ごよう</rt></ruby>・<ruby>非文<rt>ひぶん</rt></ruby>マーク",
                "name_en": "Incorrect / Ungrammatical Form",
                "description": "文法的に不自然または誤りである例",
                "description_en": "Marks an unnatural or grammatically incorrect expression."
            }
        ]
    },
    "problem_introduction": {
        "title": "<ruby>問題紹介<rt>もんだいしょうかい</rt></ruby>",
        "title_en": "Introduction of Test Question Types",
        "questions": [
            {
                "section": "<ruby>問題<rt>もんだい</rt></ruby>1",
                "section_en": "Question Type 1: Sentence Grammar 1 (Selecting Grammatical Form)",
                "description": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の（　　）に<ruby>入<rt>い</rt></ruby>れるのに<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                "description_en": "Select the best option from 1, 2, 3, or 4 to fill the parenthesis in each sentence.",
                "example_item": {
                    "question_number": 1,
                    "prompt": "<ruby>風邪<rt>かぜ</rt></ruby>をひいて<ruby>熱<rt>ねつ</rt></ruby>がある（　　）、<ruby>無理<rt>むり</rt></ruby>をして<ruby>学校<rt>がっこう</rt></ruby>に<ruby>行<rt>い</rt></ruby>った。",
                    "options": [
                        "1　<ruby>だけに<rt>だけに</rt></ruby>",
                        "2　<ruby>くせに<rt>くせに</rt></ruby>",
                        "3　<ruby>わりに<rt>わりに</rt></ruby>",
                        "4　<ruby>ように<rt>ように</rt></ruby>"
                    ],
                    "correct_answer": 2,
                    "explanation_ja": "「〜くせに」は、「〜のに（不満や非難、意外の気持ちを表す）」という意味で、主語が同じ場合に用いられます。「熱があるのに、無理をして行った」という逆接・不満のニュアンスに最も適しています。",
                    "explanation_en": "'~くせに' means 'despite / even though', carrying a nuance of complaint, reproach, or contradiction. Here it expresses going to school despite having a fever."
                }
            },
            {
                "section": "<ruby>問題<rt>もんだい</rt></ruby>2",
                "section_en": "Question Type 2: Sentence Grammar 2 (Sentence Composition / Star Arrangement)",
                "description": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の　★　に<ruby>入<rt>い</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                "description_en": "Select the best option from 1, 2, 3, or 4 to place in the star position (★).",
                "example_item": {
                    "question_number": 2,
                    "prompt": "<ruby>田中<rt>たなか</rt></ruby>さんは　＿＿＿　＿＿＿　＿★＿　＿＿＿　<ruby>帰<rt>かえ</rt></ruby>ってしまった。",
                    "options": [
                        "1　<ruby>挨拶<rt>あいさつ</rt></ruby>も",
                        "2　なしに",
                        "3　<ruby>何<rt>なに</rt></ruby>も",
                        "4　<ruby>言<rt>い</rt></ruby>わずに"
                    ],
                    "correct_order": [3, 4, 1, 2],
                    "star_position": 3,
                    "correct_answer": 1,
                    "full_sentence": "<ruby>田中<rt>たなか</rt></ruby>さんは<ruby>何<rt>なに</rt></ruby>も<ruby>言<rt>い</rt></ruby>わずに<ruby>挨拶<rt>あいさつ</rt></ruby>もなしに<ruby>帰<rt>かえ</rt></ruby>ってしまった。",
                    "full_sentence_en": "Tanaka went home without saying anything and without even saying goodbye.",
                    "explanation_ja": "文の組み立ての手順：\n1. 「〜なしに」の前に来る名詞を探すと「挨拶もなしに」（1→2）。\n2. 前半の修飾節は「何も言わずに」（3→4）。\n3. 全体をつなげると「何も言わずに挨拶もなしに帰ってしまった」となり、順序は 3 → 4 → 1 → 2。3番目の★に入るのは 1「挨拶も」。",
                    "explanation_en": "Sentence assembly steps:\n1. '〜なしに' connects to a noun: '挨拶もなしに' (1 -> 2).\n2. Preceding adverbial clause: '何も言わずに' (3 -> 4).\n3. Complete sentence: '何も言わずに (3) 挨拶も (★=1) なしに (2) 帰ってしまった'. Thus 3rd spot is option 1."
                }
            },
            {
                "section": "<ruby>問題<rt>もんだい</rt></ruby>3",
                "section_en": "Question Type 3: Text Grammar (Cloze Test)",
                "description": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで、<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>全体<rt>ぜんたい</rt></ruby>の<ruby>内容<rt>ないよう</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>えて、［　　］に<ruby>入<rt>い</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものを1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                "description_en": "Read the passage below and select the best option from 1, 2, 3, or 4 to fill each blank [ ], considering the overall context.",
                "passage": {
                    "text": "<ruby>私<rt>わたし</rt></ruby>は<ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>近所<rt>きんじょ</rt></ruby>の<ruby>公園<rt>こうえん</rt></ruby>を<ruby>散歩<rt>さんぽ</rt></ruby>することにしている。<ruby>散歩<rt>さんぽ</rt></ruby>を［ 1 ］、<ruby>体<rt>からだ</rt></ruby>の<ruby>調子<rt>ちょうし</rt></ruby>がよくなり、<ruby>仕事<rt>しごと</rt></ruby>にも<ruby>集中<rt>しゅうちゅう</rt></ruby>できるようになった。<ruby>朝<rt>あさ</rt></ruby>の<ruby>新鮮<rt>しんせん</rt></ruby>な<ruby>空気<rt>くうき</rt></ruby>を<ruby>吸<rt>す</rt></ruby>うことは、<ruby>健康<rt>けんこう</rt></ruby>にとてもよい［ 2 ］。",
                    "text_en": "I make it a rule to walk in the nearby park every morning. Since I started walking, my physical condition has improved and I can concentrate on my work better. Breathing fresh morning air is truly great for health."
                },
                "items": [
                    {
                        "item_number": 1,
                        "options": [
                            "1　<ruby>始<rt>はじ</rt></ruby>めてから",
                            "2　<ruby>始<rt>はじ</rt></ruby>めたら",
                            "3　<ruby>始<rt>はじ</rt></ruby>めるなら",
                            "4　<ruby>始<rt>はじ</rt></ruby>めたので"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "「〜てから」は「ある行為をして以来、ずっとその状態が続いている」ことを表します。散歩を始めて以来、体調が良くなったという文脈に適しています。",
                        "explanation_en": "'~てから' denotes 'ever since doing X', indicating that since starting walks, condition has improved."
                    },
                    {
                        "item_number": 2,
                        "options": [
                            "1　に<ruby>違<rt>ちが</rt></ruby>いない",
                            "2　わけがない",
                            "3　はずがない",
                            "4　かもしれない"
                        ],
                        "correct_answer": 1,
                        "explanation_ja": "「〜に違いない」は話し手の強い確信を表します。健康に良いと強く確信している結びとして最も自然です。",
                        "explanation_en": "'~に違いない' expresses strong conviction ('must be / definitely is')."
                    }
                ]
            }
        ]
    }
}

target_file = Path("nihongo-intermediate/data/grammar/intro_and_guide.json")
target_file.parent.mkdir(parents=True, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(intro_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_file}")
