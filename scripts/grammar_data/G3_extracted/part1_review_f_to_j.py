"""
Module 1 for Part 2 Sentence Grammar 2 Builder:
Review Units F through J and Review Test A-J (Images 086-105, p. 82-101).
"""

def get_part1_review_sections():
    sections = []
    
    # =========================================================================
    # Section 1: Part 1 Review Unit F (「ばかり」のいろいろな使い方) p. 82-83
    # =========================================================================
    sec1 = {
        "section_number": 1,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>まとめ F 「ばかり」のいろいろな<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>",
        "title_en": "Part 1 Review Unit F: Various Usages of 'bakari'",
        "theme": "「ばかり」の<ruby>意味<rt>いみ</rt></ruby>・<ruby>接続<rt>せつぞく</rt></ruby>の<ruby>整理<rt>せいり</rt></ruby>",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "N + ばかり",
                "pattern_name_en": "only / nothing but",
                "meaning_ja": "そればかりあって、ほかのものがない。",
                "meaning_en": "Only that, nothing else.",
                "connection_forms": ["N + ばかり"],
                "nuance_notes": "限定を表す。",
                "example_sentences": [
                    {
                        "japanese": "この<ruby>店<rt>みせ</rt></ruby>には<ruby>高<rt>たか</rt></ruby>い<ruby>品物<rt>しなもの</rt></ruby>ばかり<ruby>並<rt>なら</rt></ruby>んでいる。",
                        "english": "Only expensive goods are displayed in this store."
                    }
                ]
            },
            {
                "pattern_number": 2,
                "pattern_name": "V-て + ばかりいる",
                "pattern_name_en": "do nothing but V / always V-ing",
                "meaning_ja": "いつもその行為をしている（非難の気持ちを含むことが多い）。",
                "meaning_en": "Always doing that action (often carries a critical nuance).",
                "connection_forms": ["V-て + ばかりいる / ばかりいないで"],
                "nuance_notes": "話し手の批判的な気持ちを表すことが多い。",
                "example_sentences": [
                    {
                        "japanese": "さっきから<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>てばかりいるね。",
                        "english": "You've been looking at the clock constantly for a while now."
                    }
                ]
            },
            {
                "pattern_number": 3,
                "pattern_name": "V-た + ばかり",
                "pattern_name_en": "just did V",
                "meaning_ja": "その動作をした直後である。",
                "meaning_en": "Just after doing that action.",
                "connection_forms": ["V-た + ばかり / ばかりの N"],
                "nuance_notes": "主観的に直後だと感じているときに使う。時間が経過していても使える。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>試合<rt>しあい</rt></ruby>は<ruby>始<rt>はじ</rt></ruby>まったばかりですから、これからどうなるかわかりません。",
                        "english": "The game has just started, so we don't know what will happen yet."
                    }
                ]
            },
            {
                "pattern_number": 4,
                "pattern_name": "V-る + ばかりだ",
                "pattern_name_en": "all that remains is to V / keep on V-ing",
                "meaning_ja": "準備が整ってあとは〜するだけだ。または一方に変化が進む。",
                "meaning_en": "Everything is ready, so all that is left is to do V; or a change keeps progressing in one direction.",
                "connection_forms": ["V-辞書形 + ばかりだ"],
                "nuance_notes": "マイナスの方向にどんどん進む場合にもよく使われる。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>書類<rt>しょるい</rt></ruby>はもう<ruby>書<rt>か</rt></ruby>き<ruby>終<rt>お</rt></ruby>わった。<ruby>後<rt>あと</rt></ruby>ははんこを<ruby>押<rt>お</rt></ruby>すばかりだ。",
                        "english": "I've already finished writing the documents. All that is left is to stamp them."
                    }
                ]
            }
        ],
        "drills": [
            # 練習1 (p. 82)
            {
                "question_id": 101,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "どうしたの。さっきから<ruby>時計<rt>とけい</rt></ruby>を（　）ばかりいるね。（<ruby>見<rt>み</rt></ruby>る）",
                "correct_answer": "<ruby>見<rt>み</rt></ruby>て",
                "explanation_ja": "「V-てばかりいる」の形。「見る」のて形は「見て」。",
                "explanation_en": "Connects with the te-form: '見てばかりいる' (doing nothing but looking at)."
            },
            {
                "question_id": 102,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>試合<rt>しあい</rt></ruby>は（　）ばかりですから、これからどうなるかわかりません。（<ruby>始<rt>はじ</rt></ruby>まる）",
                "correct_answer": "<ruby>始<rt>はじ</rt></ruby>まった",
                "explanation_ja": "「V-たばかり」で動作の直後を表す。「始まったばかり」。",
                "explanation_en": "'〜たばかり' indicates an action has just happened: '始まったばかり' (just started)."
            },
            {
                "question_id": 103,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "この<ruby>辺<rt>あた</rt></ruby>りは<ruby>交通<rt>こうつう</rt></ruby>が（　）ばかりでなく、<ruby>環境<rt>かんきょう</rt></ruby>もいい。（<ruby>便利<rt>べんり</rt></ruby>だ）",
                "correct_answer": "<ruby>便利<rt>べんり</rt></ruby>な",
                "explanation_ja": "「Na+なばかりでなく / Na+であるばかりでなく」の形。",
                "explanation_en": "Connects with Na-adjectives as '便利なばかりでなく' (not only convenient)."
            },
            {
                "question_id": 104,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>最近<rt>さいきん</rt></ruby><ruby>頭痛<rt>ずつう</rt></ruby>が（　）ばかりなので、<ruby>医者<rt>いしゃ</rt></ruby>に<ruby>相談<rt>そうだん</rt></ruby>することにした。（ひどくなる）",
                "correct_answer": "ひどくなる",
                "explanation_ja": "「V-るばかりだ」で一方に変化が進むことを表す。「ひどくなるばかりなので」。",
                "explanation_en": "'V-るばかり' expresses continuous worsening: 'ひどくなるばかり' (only gets worse)."
            },
            {
                "question_id": 105,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>雨<rt>あめ</rt></ruby>が（　）ばかりでなく、<ruby>風<rt>かぜ</rt></ruby>も<ruby>強<rt>つよ</rt></ruby>くなった。（<ruby>降<rt>ふ</rt></ruby>り<ruby>始<rt>はじ</rt></ruby>める）",
                "correct_answer": "<ruby>降<rt>ふ</rt></ruby>り<ruby>始<rt>はじ</rt></ruby>めた",
                "explanation_ja": "過去の事実の添加「〜たばかりでなく」。「降り始めたばかりでなく」。",
                "explanation_en": "'〜たばかりでなく': 'not only started raining, but...'."
            },
            {
                "question_id": 106,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>書類<rt>しょるい</rt></ruby>はもう<ruby>書<rt>か</rt></ruby>き<ruby>終<rt>お</rt></ruby>わった。<ruby>後<rt>あと</rt></ruby>ははんこを（　）ばかりだ。（<ruby>押<rt>お</rt></ruby>す）",
                "correct_answer": "<ruby>押<rt>お</rt></ruby>す",
                "explanation_ja": "「V-るばかりだ」で準備完了しあとは〜するだけ。「押すばかりだ」。",
                "explanation_en": "'V-るばかりだ' means all that is left is to do V: '押すばかりだ'."
            },
            {
                "question_id": 107,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "ボランティアには<ruby>初<rt>はじ</rt></ruby>めて<ruby>参加<rt>さんか</rt></ruby>したので、ただ（　）ばかりだった。（<ruby>見<rt>み</rt></ruby>ている）",
                "correct_answer": "<ruby>見<rt>み</rt></ruby>ている",
                "explanation_ja": "「V-ているばかりだった」でその状態に終始したことを表す。",
                "explanation_en": "'見ているばかりだった' (did nothing but just watch)."
            },
            {
                "question_id": 108,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "（　）ばかりのころは<ruby>怖<rt>こわ</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>ったが、<ruby>意外<rt>いがい</rt></ruby>に<ruby>面白<rt>おもしろ</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>だった。（<ruby>会<rt>あ</rt></ruby>う）",
                "correct_answer": "<ruby>会<rt>あ</rt></ruby>った",
                "explanation_ja": "「V-たばかりのころ」で会ってすぐの時期。「会ったばかりのころ」。",
                "explanation_en": "'会ったばかりのころ' (around the time when I had just met him)."
            },
            {
                "question_id": 109,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>先生<rt>せんせい</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>を（　）ばかりでなく、どんどん<ruby>質問<rt>しつもん</rt></ruby>してください。（<ruby>聞<rt>き</rt></ruby>く）",
                "correct_answer": "<ruby>聞<rt>き</rt></ruby>く",
                "explanation_ja": "「V-るばかりでなく」で「聞くだけでなく」。「聞くばかりでなく」。",
                "explanation_en": "'聞くばかりでなく' (not only just listening, but...)."
            },
            {
                "question_id": 110,
                "category": "F 練習1",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>先<rt>さき</rt></ruby>のことを（　）ばかりいないで、<ruby>行動<rt>こうどう</rt></ruby>してみたらどうですか。（<ruby>悩<rt>なや</rt></ruby>む）",
                "correct_answer": "<ruby>悩<rt>なや</rt></ruby>んで",
                "explanation_ja": "「V-てばかりいないで」で「〜ばかりしないで」。「悩んでばかりいないで」。",
                "explanation_en": "'悩んでばかりいないで' (don't just keep worrying)."
            },
            # 練習2 (p. 82-83)
            {
                "question_id": 111,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>はあの<ruby>有名<rt>ゆうめい</rt></ruby>な<ruby>歌手<rt>かしゅ</rt></ruby>に（　）、<ruby>握手<rt>あくしゅ</rt></ruby>もした。",
                "options": ["a　会うばかりで", "b　会ったばかりでなく", "c　会ってばかりいないで"],
                "correct_answer": "b",
                "explanation_ja": "「〜ばかりでなく…も」で添加を表す。「会ったばかりでなく、握手もした」。",
                "explanation_en": "'〜ばかりでなく…も' means 'not only... but also...': met him and shook hands too."
            },
            {
                "question_id": 112,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>店<rt>みせ</rt></ruby>はきのう（　）、まだお<ruby>客<rt>きゃく</rt></ruby>さんが<ruby>少<rt>すく</rt></ruby>ない。",
                "options": ["a　開店ばかりして", "b　開店するばかりで", "c　開店したばかりで"],
                "correct_answer": "c",
                "explanation_ja": "「開店したばかりで」＝開店した直後なので。",
                "explanation_en": "'開店したばかりで' (having just opened yesterday)."
            },
            {
                "question_id": 113,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "あのお<ruby>母<rt>かあ</rt></ruby>さんは<ruby>携帯電話<rt>けいたいでんわ</rt></ruby>を（　）、<ruby>子<rt>こ</rt></ruby>どもと<ruby>話<rt>はなし</rt></ruby>もしない。",
                "options": ["a　見たばかりで", "b　見たばかりでなく", "c　見てばかりいて"],
                "correct_answer": "c",
                "explanation_ja": "「見てばかりいて」＝そればかりずっと見ていて。",
                "explanation_en": "'見てばかりいて' (does nothing but look at her cell phone)."
            },
            {
                "question_id": 114,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>出席者<rt>しゅっせきしゃ</rt></ruby>もそろったので、あとはパーティーが<ruby>始<rt>はじ</rt></ruby>まるのを（　）。",
                "options": ["a　待つばかりだ", "b　待ってばかりいる", "c　待ったばかりだ"],
                "correct_answer": "a",
                "explanation_ja": "準備が整いあとは〜するだけ。「待つばかりだ」。",
                "explanation_en": "'待つばかりだ' (all that's left is to wait for the party to start)."
            },
            {
                "question_id": 115,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>子<rt>こ</rt></ruby>どもが<ruby>生<rt>う</rt></ruby>まれる<ruby>日<rt>ひ</rt></ruby>が<ruby>近<rt>ちか</rt></ruby>づいたが、<ruby>夫<rt>おっと</rt></ruby>のぼくは<ruby>何<rt>なに</rt></ruby>もできない。ただ（　）。",
                "options": ["a　見守るばかりだ", "b　見守ったばかりだ", "c　見守ってばかりいる"],
                "correct_answer": "a",
                "explanation_ja": "できることは〜するだけだ。「見守るばかりだ」。",
                "explanation_en": "'見守るばかりだ' (can only watch over)."
            },
            {
                "question_id": 116,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "（　）が、もう<ruby>忘<rt>わす</rt></ruby>れてしまった。",
                "options": ["a　名前ばかり聞いた", "b　名前を聞くばかりだ", "c　名前を聞いたばかりだ"],
                "correct_answer": "c",
                "explanation_ja": "直前に聞いたばかりなのに。「名前を聞いたばかりだが」。",
                "explanation_en": "'名前を聞いたばかりだが' (even though I just heard the name)."
            },
            {
                "question_id": 117,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>最近<rt>さいきん</rt></ruby><ruby>彼<rt>かれ</rt></ruby>は<ruby>疲<rt>つか</rt></ruby>れているらしく、<ruby>休日<rt>きゅうじつ</rt></ruby>は（　）、<ruby>何<rt>なに</rt></ruby>もしない。",
                "options": ["a　寝るばかりで", "b　寝たばかりで", "c　寝るばかりでなく"],
                "correct_answer": "a",
                "explanation_ja": "「寝るばかりで、何もしない」＝寝てばかりいて何もしない。",
                "explanation_en": "'寝るばかりで' (does nothing but sleep)."
            },
            {
                "question_id": 118,
                "category": "F 練習2",
                "question_type": "multiple_choice",
                "prompt": "たばこをやめてから、（　）。",
                "options": ["a　体重ばかり増える", "b　体重が増えるばかりだ", "c　体重が増えたばかりだ"],
                "correct_answer": "b",
                "explanation_ja": "一方に増え続けている。「体重が増えるばかりだ」。",
                "explanation_en": "'体重が増えるばかりだ' (weight only keeps increasing)."
            },
            # ワンポイントレッスン (p. 83)
            {
                "question_id": 119,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "うちには<ruby>生<rt>う</rt></ruby>まれた（　）の<ruby>子犬<rt>こいぬ</rt></ruby>が3<ruby>匹<rt>びき</rt></ruby>います。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "a",
                "explanation_ja": "「〜たばかりのN」の形で名詞を修飾できる（「〜たところのN」とは言えない）。",
                "explanation_en": "'〜たばかりのN' can modify a noun; 'ところ' cannot."
            },
            {
                "question_id": 120,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>会議<rt>かいぎ</rt></ruby>が<ruby>始<rt>はじ</rt></ruby>まった（　）に<ruby>高橋<rt>たかはし</rt></ruby>さんが<ruby>入<rt>はい</rt></ruby>ってきた。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "b",
                "explanation_ja": "後ろに助詞「に」が接続できるのは「〜たところ」。「始まったところに」。",
                "explanation_en": "Particles like 'に' attach to 'ところ': '始まったところに'."
            },
            {
                "question_id": 121,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "もしもし、<ruby>今<rt>いま</rt></ruby><ruby>新幹線<rt>しんかんせん</rt></ruby>に<ruby>乗<rt>の</rt></ruby>った（　）です。そちらに8<ruby>時<rt>じ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くと<ruby>思<rt>おも</rt></ruby>います。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "b",
                "explanation_ja": "客観的にまさに今その行為をした直後であることを伝える。「乗ったところです」。",
                "explanation_en": "'乗ったところです' denotes the precise objective moment just after boarding."
            },
            {
                "question_id": 122,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "このパソコンはまだ<ruby>買<rt>か</rt></ruby>った（　）なのに、<ruby>調子<rt>ちょうし</rt></ruby>が<ruby>悪<rt>わる</rt></ruby>い。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "a",
                "explanation_ja": "「〜たばかりなのに」＝買って日が浅いのに（主観的な時間感覚）。",
                "explanation_en": "'買ったばかりなのに' expresses subjective recentness ('bought just recently')."
            },
            {
                "question_id": 123,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>彼<rt>かれ</rt></ruby>は1か<ruby>月<rt>げつ</rt></ruby><ruby>前<rt>まえ</rt></ruby>に<ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>た（　）だそうです。でも、<ruby>日本語<rt>にほんご</rt></ruby>が<ruby>上手<rt>じょうず</rt></ruby>ですね。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "a",
                "explanation_ja": "1か月前のように客観的に時間が経っていても、主観的に直後と感じる場合は「ばかり」。",
                "explanation_en": "Even after 1 month, subjective recentness requires 'ばかり'."
            },
            {
                "question_id": 124,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>好<rt>す</rt></ruby>きな<ruby>曲<rt>きょく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>き<ruby>終<rt>お</rt></ruby>わった（　）で、ちょうど<ruby>昼休<rt>ひるやす</rt></ruby>みが<ruby>終<rt>お</rt></ruby>わった。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "b",
                "explanation_ja": "後ろに助詞「で」が接続できるのは「〜たところ」。「聞き終わったところで」。",
                "explanation_en": "Particles like 'で' connect to 'ところ': '聞き終わったところで'."
            },
            {
                "question_id": 125,
                "category": "F ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "この4<ruby>月<rt>がつ</rt></ruby>に<ruby>入社<rt>にゅうしゃ</rt></ruby>した（　）なので、まだ<ruby>会社<rt>かいしゃ</rt></ruby>の<ruby>人間関係<rt>にんげんかんけい</rt></ruby>がよくわからない。",
                "options": ["a　ばかり", "b　ところ"],
                "correct_answer": "a",
                "explanation_ja": "客観的な時間の経過（数か月など）があっても主観的に直後である場合は「ばかり」。",
                "explanation_en": "'入社したばかりなので' reflects subjective feeling of having recently joined."
            }
        ]
    }
    sections.append(sec1)
    
    # =========================================================================
    # Section 2: Part 1 Review Unit G (「する・なる」の整理) p. 84-87
    # =========================================================================
    sec2 = {
        "section_number": 2,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>まとめ G 「する・なる」の<ruby>整理<rt>せいり</rt></ruby>",
        "title_en": "Part 1 Review Unit G: Organization of 'suru' and 'naru'",
        "theme": "「する」と「なる」の<ruby>使<rt>つか</rt></ruby>い<ruby>分<rt>わ</rt></ruby>け",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "〜にする・〜くする vs 〜になる・〜くなる",
                "pattern_name_en": "change a state intentionally vs state changes naturally",
                "meaning_ja": "する：人の意志で状態を変える。なる：自然に・客観的に状態が変わる。",
                "meaning_en": "suru: intentionally change a state. naru: a state changes on its own or objectively.",
                "connection_forms": ["N・Na + にする / になる", "A-く + する / なる"],
                "nuance_notes": "するは人為的、なるは客観的変化。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>私<rt>わたし</rt></ruby>は<ruby>部屋<rt>へや</rt></ruby>をきれいにして、<ruby>部屋<rt>へや</rt></ruby>はきれいになった。",
                        "english": "I cleaned the room, and the room became clean."
                    }
                ]
            },
            {
                "pattern_number": 2,
                "pattern_name": "〜ことにする vs 〜ことになる",
                "pattern_name_en": "decide to do vs it has been decided that",
                "meaning_ja": "〜ことにする：話者自身の決断。〜ことになる：外部・組織等の決定や予定。",
                "meaning_en": "koto ni suru: decision made by speaker. koto ni naru: decision made by an organization or circumstances.",
                "connection_forms": ["V-辞書形 / V-ない形 + ことにする / ことになる"],
                "nuance_notes": "主体の意志の有無による使い分け。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>連休<rt>れんきゅう</rt></ruby>にハワイに<ruby>行<rt>い</rt></ruby>くことにした。",
                        "english": "I decided to go to Hawaii during the long holiday."
                    },
                    {
                        "japanese": "<ruby>来月<rt>らいげつ</rt></ruby>、<ruby>出張<rt>しゅっちょう</rt></ruby>することになった。",
                        "english": "It has been decided that I will go on a business trip next month."
                    }
                ]
            },
            {
                "pattern_number": 3,
                "pattern_name": "〜ようにする vs 〜ようになる / 〜ようになっている",
                "pattern_name_en": "make an effort to / come to be able to / is designed to",
                "meaning_ja": "ようにする：習慣的努力。ようになる：能力や習慣の変化。ようになっている：構造・設計。",
                "meaning_en": "you ni suru: make an effort to. you ni naru: change in ability/habit. you ni natte iru: designed/built to.",
                "connection_forms": ["V-辞書形 / V-ない形 + ようにする / ようになる / ようになっている"],
                "nuance_notes": "ようになっているは機械の機能や仕組みによく使われる。",
                "example_sentences": [
                    {
                        "japanese": "<ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>野菜<rt>やさい</rt></ruby>を<ruby>食<rt>た</rt></ruby>べるようにしている。",
                        "english": "I make an effort to eat vegetables every morning."
                    },
                    {
                        "japanese": "トイレに<ruby>入<rt>はい</rt></ruby>ると、<ruby>電気<rt>でんき</rt></ruby>が<ruby>自動<rt>じどう</rt></ruby>でつくようになっている。",
                        "english": "When you enter the bathroom, the light automatically turns on."
                    }
                ]
            }
        ],
        "drills": [
            # 練習1 (p. 86) - 15 items
            {
                "question_id": 201,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "スープの<ruby>味<rt>あじ</rt></ruby>が<ruby>濃<rt>こ</rt></ruby>かったから、お<ruby>湯<rt>ゆ</rt></ruby>を<ruby>入<rt>い</rt></ruby>れて<ruby>薄<rt>うす</rt></ruby>く（　）。",
                "options": ["a　した", "b　なった"],
                "correct_answer": "a",
                "explanation_ja": "お湯を入れて薄く変化させた人為的行為なので「薄くした」。",
                "explanation_en": "Intentional action causing change: '薄くした' (made it thinner)."
            },
            {
                "question_id": 202,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "りんご（　）、<ruby>木<rt>き</rt></ruby>から<ruby>取<rt>と</rt></ruby>って<ruby>食<rt>た</rt></ruby>べてもいいよ。",
                "options": ["a　を赤くしたら", "b　が赤くなったら"],
                "correct_answer": "b",
                "explanation_ja": "りんごが自然に熟して赤く変化することなので自動詞「が赤くなったら」。",
                "explanation_en": "Natural change: 'が赤くなったら' (when apples turn red)."
            },
            {
                "question_id": 203,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "テレビで<ruby>紹介<rt>しょうかい</rt></ruby>されたので、この<ruby>町<rt>まち</rt></ruby>の<ruby>祭<rt>まつ</rt></ruby>りは（　）。",
                "options": ["a　有名にした", "b　有名になった"],
                "correct_answer": "b",
                "explanation_ja": "結果として祭りが知名度を得た変化なので「有名になった」。",
                "explanation_en": "Resulting state: '有名になった' (became famous)."
            },
            {
                "question_id": 204,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "【<ruby>美容院<rt>びよういん</rt></ruby>で】<ruby>今日<rt>きょう</rt></ruby>は10センチぐらい（　）ください。",
                "options": ["a　短くして", "b　短くなって"],
                "correct_answer": "a",
                "explanation_ja": "相手に切ってもらう依頼なので他動詞的表現「短くしてください」。",
                "explanation_en": "Request for intentional change: '短くして' (please cut it shorter)."
            },
            {
                "question_id": 205,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "A「お<ruby>子<rt>こ</rt></ruby>さんのかぜ、いかがですか。」 B「はい、だいぶよく（　）。」",
                "options": ["a　しました", "b　なりました"],
                "correct_answer": "b",
                "explanation_ja": "病状が自然に快方に向かった結果なので「よくなりました」。",
                "explanation_en": "Natural recovery of illness: 'よくなりました' (has gotten much better)."
            },
            {
                "question_id": 206,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>図書館<rt>としょかん</rt></ruby>では<ruby>古<rt>ふる</rt></ruby>い<ruby>本<rt>ほん</rt></ruby>は<ruby>捨<rt>す</rt></ruby>てられることに（　）。",
                "options": ["a　した", "b　なった"],
                "correct_answer": "b",
                "explanation_ja": "図書館という組織の規則・決定なので「ことになった」。",
                "explanation_en": "Institutional rule: 'ことになった' (it has been decided that...)."
            },
            {
                "question_id": 207,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>はあした<ruby>退院<rt>たいいん</rt></ruby>できることに（　）。",
                "options": ["a　しました", "b　なりました"],
                "correct_answer": "b",
                "explanation_ja": "医師や病院の判断で退院が決まったので「ことになりました」。",
                "explanation_en": "Objective decision by doctors: 'ことになりました' (it was decided that I can be discharged)."
            },
            {
                "question_id": 208,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>体重<rt>たいじゅう</rt></ruby>を<ruby>減<rt>へ</rt></ruby>らしたいから、ご<ruby>飯<rt>はん</rt></ruby>は<ruby>毎食<rt>まいしょく</rt></ruby><ruby>茶<rt>ちゃ</rt></ruby>わん1<ruby>杯<rt>ぱい</rt></ruby>だけに（　）。",
                "options": ["a　しよう", "b　なろう"],
                "correct_answer": "a",
                "explanation_ja": "話者自身の意志による決定なので「〜にしよう」。",
                "explanation_en": "Speaker's volitional decision: '〜にしよう' (let's decide on...)."
            },
            {
                "question_id": 209,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今度<rt>こんど</rt></ruby>の<ruby>冬<rt>ふゆ</rt></ruby>のオリンピックはどこに（　）。",
                "options": ["a　しましたか", "b　なりましたか"],
                "correct_answer": "b",
                "explanation_ja": "IOC等の組織の決定事項を尋ねるので「どこになりましたか」。",
                "explanation_en": "Asking about an institutional/external outcome: 'どこになりましたか'."
            },
            {
                "question_id": 210,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>は<ruby>大事<rt>だいじ</rt></ruby>なことは<ruby>何<rt>なん</rt></ruby>でもメモすることに（　）。",
                "options": ["a　している", "b　なっている"],
                "correct_answer": "a",
                "explanation_ja": "話者個人の習慣・心がけなので「ことにしている」。",
                "explanation_en": "Personal self-imposed routine: 'ことにしている' (I make it a rule to...)."
            },
            {
                "question_id": 211,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>公園<rt>こうえん</rt></ruby>では<ruby>花火<rt>はなび</rt></ruby>をしてはいけないことに（　）そうだ。",
                "options": ["a　している", "b　なっている"],
                "correct_answer": "b",
                "explanation_ja": "公園の公共ルール・規則なので「ことになっている」。",
                "explanation_en": "Public regulation: 'ことになっている' (it is a rule that...)."
            },
            {
                "question_id": 212,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>子<rt>こ</rt></ruby>どもは<ruby>何歳<rt>なんさい</rt></ruby>で<ruby>歩<rt>ある</rt></ruby>けるように（　）。",
                "options": ["a　するんですか", "b　なるんですか"],
                "correct_answer": "b",
                "explanation_ja": "可能動詞に接続して能力の自然な発達変化を尋ねるので「ようになる」。",
                "explanation_en": "Developmental change in ability: 'なるんですか' (come to be able to walk)."
            },
            {
                "question_id": 213,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>はよくかんで<ruby>食<rt>た</rt></ruby>べるように（　）。",
                "options": ["a　しましょう", "b　なりましょう"],
                "correct_answer": "a",
                "explanation_ja": "習慣的な心がけを呼びかける表現なので「〜ようにしましょう」。",
                "explanation_en": "Encouraging a habitual effort: '〜ようにしましょう' (let's try to chew well)."
            },
            {
                "question_id": 214,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "ねこの<ruby>目<rt>め</rt></ruby>は、<ruby>入<rt>はい</rt></ruby>ってくる<ruby>光<rt>ひかり</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>を<ruby>調節<rt>ちょうせつ</rt></ruby>できるように（　）。",
                "options": ["a　している", "b　なっている"],
                "correct_answer": "b",
                "explanation_ja": "身体の仕組み・機能としてそうなっているので「ようになっている」。",
                "explanation_en": "Natural biological mechanism: 'ようになっている' (is designed/structured to)."
            },
            {
                "question_id": 215,
                "category": "G 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>先生<rt>せんせい</rt></ruby>「<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>書類<rt>しょるい</rt></ruby>だから、<ruby>書<rt>か</rt></ruby>き<ruby>間違<rt>まちが</rt></ruby>えないように（　）。」",
                "options": ["a　すること", "b　なること"],
                "correct_answer": "a",
                "explanation_ja": "注意・指示として「〜ようにすること」と述べる。",
                "explanation_en": "Instruction to take care: 'すること' (make sure not to miswrite)."
            },
            # 練習2 (p. 86-87) - 6 items
            {
                "question_id": 216,
                "category": "G 練習2 ①",
                "question_type": "multiple_choice",
                "prompt": "B「引っ越しする（① a ことに b ように）したんです。」",
                "options": ["a　ことに", "b　ように"],
                "correct_answer": "a",
                "explanation_ja": "引っ越しを決意した意志決定なので「ことにした」。",
                "explanation_en": "'ことにした' indicates a personal decision to move."
            },
            {
                "question_id": 217,
                "category": "G 練習2 ②",
                "question_type": "multiple_choice",
                "prompt": "「来月から弟といっしょに住む（② a ことに b ように）なったので……。」",
                "options": ["a　ことに", "b　ように"],
                "correct_answer": "a",
                "explanation_ja": "話し合い等で決まった客観的事情なので「ことになった」。",
                "explanation_en": "'ことになった' indicates an agreed upon arrangement."
            },
            {
                "question_id": 218,
                "category": "G 練習2 ③",
                "question_type": "multiple_choice",
                "prompt": "A「じゃ、寝坊しない（③ a ことに b ように）しなければね。」",
                "options": ["a　ことに", "b　ように"],
                "correct_answer": "b",
                "explanation_ja": "習慣的な努力・注意を促すので「寝坊しないようにしなければ」。",
                "explanation_en": "'ようにしなければ' means one must make an effort not to oversleep."
            },
            {
                "question_id": 219,
                "category": "G 練習2 ④",
                "question_type": "multiple_choice",
                "prompt": "B「ええ。駅からも遠いので、自転車を買う（④ a ことに b ように）しました。」",
                "options": ["a　ことに", "b　ように"],
                "correct_answer": "a",
                "explanation_ja": "自転車を買う決心をしたので「ことにしました」。",
                "explanation_en": "'買うことにしました' means decided to purchase a bicycle."
            },
            {
                "question_id": 220,
                "category": "G 練習2 ⑤",
                "question_type": "multiple_choice",
                "prompt": "B「急なんですが、あしたの朝9時に引っ越しのトラックが来る（⑤ a ことに b ように）なったんです。」",
                "options": ["a　ことに", "b　ように"],
                "correct_answer": "a",
                "explanation_ja": "トラックの到着が業者との間で決定されたので「ことになった」。",
                "explanation_en": "'来ることになった' means it was arranged for the moving truck to arrive."
            },
            {
                "question_id": 221,
                "category": "G 練習2 ⑥",
                "question_type": "multiple_choice",
                "prompt": "B「今から弟と弟の友だちが手伝いに来る（⑥ a ことに b ように）なっていますから。」",
                "options": ["a　ことに", "b　ように"],
                "correct_answer": "a",
                "explanation_ja": "すでに決まっている予定・手はずなので「ことになっている」。",
                "explanation_en": "'来ることになっている' indicates a pre-scheduled arrangement."
            },
            # ワンポイントレッスン (p. 87) - 7 items
            {
                "question_id": 222,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>はなるべく<ruby>肉<rt>にく</rt></ruby>よりも（　）ようにしている。",
                "options": ["a　魚を食べる", "b　魚が食べられる"],
                "correct_answer": "a",
                "explanation_ja": "「〜ようにしている」は主語が話者で意志動詞を使う。「魚を食べる」。",
                "explanation_en": "'〜ようにしている' requires a volitional verb: '魚を食べる'."
            },
            {
                "question_id": 223,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "うちの<ruby>台所<rt>だいどころ</rt></ruby>は、<ruby>長<rt>なが</rt></ruby>い<ruby>時間<rt>じかん</rt></ruby>ガスを<ruby>使<rt>つか</rt></ruby>うと（　）ようになっている。",
                "options": ["a　火を消す", "b　火が消える"],
                "correct_answer": "b",
                "explanation_ja": "「〜ようになっている」は主語が人間ではなく、無意志動詞（自動詞）を使う。「火が消える」。",
                "explanation_en": "'〜ようになっている' describes a machine mechanism using intransitive verbs: '火が消える'."
            },
            {
                "question_id": 224,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "ホテルでは、お<ruby>風呂<rt>ふろ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>っていても（　）ようになっている。",
                "options": ["a　電話をかける", "b　電話がかけられる"],
                "correct_answer": "b",
                "explanation_ja": "機能・設備を表すので可能動詞「電話がかけられる」。",
                "explanation_en": "Potential verb used for facility capability: '電話がかけられる'."
            },
            {
                "question_id": 225,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "このおもちゃは<ruby>面白<rt>おもしろ</rt></ruby>い。<ruby>手<rt>て</rt></ruby>をたたくと（　）ようになっている。",
                "options": ["a　人形を動かす", "b　人形が動く"],
                "correct_answer": "b",
                "explanation_ja": "おもちゃの仕組みなので自動詞「人形が動く」。",
                "explanation_en": "Mechanical reaction: '人形が動く' (the doll moves)."
            },
            {
                "question_id": 226,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>健康<rt>けんこう</rt></ruby>のためになるべく（　）ようにしてください。",
                "options": ["a　体を動かす", "b　体が動く"],
                "correct_answer": "a",
                "explanation_ja": "相手に習慣的な行動を促すので意志動詞「体を動かす」。",
                "explanation_en": "Urging volitional effort: '体を動かす'."
            },
            {
                "question_id": 227,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "このドアは<ruby>内側<rt>うちがわ</rt></ruby>からは<ruby>外<rt>そと</rt></ruby>が<ruby>見<rt>み</rt></ruby>えるが、<ruby>外<rt>そと</rt></ruby>からは（　）ようになっている。",
                "options": ["a　中を見ない", "b　中が見えない"],
                "correct_answer": "b",
                "explanation_ja": "ドアの構造・特性なので可能動詞否定「中が見えない」。",
                "explanation_en": "Structural feature of door: '中が見えない' (inside cannot be seen)."
            },
            {
                "question_id": 228,
                "category": "G ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>新聞<rt>しんぶん</rt></ruby>のテレビ<ruby>番組表<rt>ばんぐみひょう</rt></ruby>を<ruby>見<rt>み</rt></ruby>るとテレビが<ruby>見<rt>み</rt></ruby>たくなるので、<ruby>試験前<rt>しけんまえ</rt></ruby>は（　）ようにしているんです。",
                "options": ["a　見ない", "b　見えない"],
                "correct_answer": "a",
                "explanation_ja": "話者自身の自発的自制（意志）なので「見ないようにしている」。",
                "explanation_en": "Speaker's intentional self-restraint: '見ないようにしている'."
            }
        ]
    }
    sections.append(sec2)
    
    # =========================================================================
    # Section 3: Part 1 Review Unit H (「たら・ば・と・なら」の特別な使い方) p. 88-91
    # =========================================================================
    sec3 = {
        "section_number": 3,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>まとめ H 「たら・ば・と・なら」の<ruby>特別<rt>とくべつ</rt></ruby>な<ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>",
        "title_en": "Part 1 Review Unit H: Special Usages of 'tara / ba / to / nara'",
        "theme": "条件表現の特別な用法（発見・きっかけ・反実仮想など）",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "〜と…た・〜たら…た（発見・きっかけ）",
                "pattern_name_en": "when / upon doing (discovery / unexpected result)",
                "meaning_ja": "ある動作をすることで、予想外の事実に気がついた。",
                "meaning_en": "Upon performing an action, noticed an unexpected situation/fact.",
                "connection_forms": ["V-辞書形 + と …た", "V-たら …た"],
                "nuance_notes": "後件には「…ていた」等の過去形が来て、主語は前件と後件で異なる。",
                "example_sentences": [
                    {
                        "japanese": "プレゼントを<ruby>開<rt>あ</rt></ruby>けると、<ruby>人形<rt>にんぎょう</rt></ruby>が<ruby>入<rt>はい</rt></ruby>っていた。",
                        "english": "When I opened the present, there was a doll inside."
                    }
                ]
            },
            {
                "pattern_number": 2,
                "pattern_name": "〜ば…・〜たら…（反実仮想）",
                "pattern_name_en": "if only / had it been (counterfactual hypothesis)",
                "meaning_ja": "実際とは反対のことを仮定して、後悔や残念な気持ちを表す。",
                "meaning_en": "Hypothesizing opposite to reality to express regret or disappointment.",
                "connection_forms": ["V-ば / V-たら …たのに"],
                "nuance_notes": "実際には起こらなかったことについての反事実。",
                "example_sentences": [
                    {
                        "japanese": "もう少し<ruby>早<rt>はや</rt></ruby>く<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>ていれば、<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>ったのに。",
                        "english": "If I had left home a little earlier, I would have caught the train."
                    }
                ]
            }
        ],
        "drills": [
            # 練習1 (p. 90) - 10 items
            {
                "question_id": 301,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "3<ruby>時<rt>じ</rt></ruby>に<ruby>駅<rt>えき</rt></ruby>で<ruby>待<rt>ま</rt></ruby>ち<ruby>合<rt>あ</rt></ruby>わせした。<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くと、<ruby>彼女<rt>かのじょ</rt></ruby>はもう（　）。",
                "options": ["a　来た", "b　来ていた"],
                "correct_answer": "b",
                "explanation_ja": "すでに到着していた状態を発見したので「来ていた」。",
                "explanation_en": "Discovering an existing state: '来ていた' (she was already there)."
            },
            {
                "question_id": 302,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>引<rt>ひ</rt></ruby>き<ruby>出<rt>だ</rt></ruby>しを<ruby>開<rt>あ</rt></ruby>けると、<ruby>手紙<rt>てがみ</rt></ruby>が（　）。",
                "options": ["a　あった", "b　入った"],
                "correct_answer": "a",
                "explanation_ja": "手紙が存在している状態に気がついたので「あった」。",
                "explanation_en": "State discovered upon opening: 'あった' (there was a letter)."
            },
            {
                "question_id": 303,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "テレビをつけたら、<ruby>昔<rt>むかし</rt></ruby><ruby>見<rt>み</rt></ruby>た<ruby>映画<rt>えいが</rt></ruby>を（　）。",
                "options": ["a　見た", "b　やっていた"],
                "correct_answer": "b",
                "explanation_ja": "放送されていた状態に気づいたので「やっていた」。",
                "explanation_en": "Existing ongoing broadcast: 'やっていた' (was showing)."
            },
            {
                "question_id": 304,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "おもちゃを<ruby>振<rt>ふ</rt></ruby>ってみると、いい<ruby>音<rt>おと</rt></ruby>が（　）。",
                "options": ["a　した", "b　していた"],
                "correct_answer": "a",
                "explanation_ja": "振ったその瞬間に音が鳴ったので「した」。",
                "explanation_en": "Sound occurred upon shaking: 'した' (made a good sound)."
            },
            {
                "question_id": 305,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>少<rt>すこ</rt></ruby>しお<ruby>酒<rt>さけ</rt></ruby>を<ruby>飲<rt>の</rt></ruby>むと、（　）。",
                "options": ["a　踊りたくなった", "b　踊りたかった"],
                "correct_answer": "a",
                "explanation_ja": "飲んだ結果として感情の変化が生じたので「踊りたくなった」。",
                "explanation_en": "Emotional change triggered by drinking: '踊りたくなった'."
            },
            {
                "question_id": 306,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>山道<rt>やまみち</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>いていたら、（　）。",
                "options": ["a　へびが出てきた", "b　へびを捕まえた"],
                "correct_answer": "a",
                "explanation_ja": "思いがけない出来事が起こったので「へびが出てきた」。",
                "explanation_en": "Unexpected occurrence: 'へびが出てきた' (a snake came out)."
            },
            {
                "question_id": 307,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>図書館<rt>としょかん</rt></ruby>に<ruby>行<rt>い</rt></ruby>ったら、（　）。",
                "options": ["a　今日は休みだった", "b　たくさん本を借りた"],
                "correct_answer": "a",
                "explanation_ja": "行って初めて休みである事実に気づいたので「今日は休みだった」。",
                "explanation_en": "Discovered fact: '今日は休みだった' (it was closed today)."
            },
            {
                "question_id": 308,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>時計<rt>とけい</rt></ruby>を<ruby>見<rt>み</rt></ruby>ると、もう12<ruby>時<rt>じ</rt></ruby>を（　）。",
                "options": ["a　過ぎた", "b　過ぎていた"],
                "correct_answer": "b",
                "explanation_ja": "すでに12時を回っていた状態に気づいたので「過ぎていた」。",
                "explanation_en": "Discovered state of time: '過ぎていた' (it was already past 12)."
            },
            {
                "question_id": 309,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>公園<rt>こうえん</rt></ruby>のベンチで<ruby>休<rt>やす</rt></ruby>んでいると、おじいさんが（　）。",
                "options": ["a　近づいてきた", "b　いた"],
                "correct_answer": "a",
                "explanation_ja": "動作の最中に発生した事象なので「近づいてきた」。",
                "explanation_en": "Event occurring during rest: '近づいてきた' (an old man approached)."
            },
            {
                "question_id": 310,
                "category": "H 練習1",
                "question_type": "multiple_choice",
                "prompt": "チャイムが<ruby>鳴<rt>な</rt></ruby>ったので<ruby>玄関<rt>げんかん</rt></ruby>の<ruby>外<rt>そと</rt></ruby>に<ruby>出<rt>で</rt></ruby>ると、<ruby>宅配便<rt>たくはいびん</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>が（　）。",
                "options": ["a　来た", "b　いた"],
                "correct_answer": "b",
                "explanation_ja": "外に出たときにそこに立っていた状態を発見したので「いた」。",
                "explanation_en": "Discovered someone standing there: 'いた' (delivery person was there)."
            },
            # 練習2 (p. 90-91) - 8 items
            {
                "question_id": 311,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>目<rt>め</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>いので、<ruby>鏡<rt>かがみ</rt></ruby>で（　）、<ruby>赤<rt>あか</rt></ruby>かった。",
                "options": ["a　見てみると", "b　見ていると", "c　見ていたら"],
                "correct_answer": "a",
                "explanation_ja": "確認する行為をしてみたら赤かったという発見。「見てみると」。",
                "explanation_en": "'見てみると' (when I tried looking in the mirror, it was red)."
            },
            {
                "question_id": 312,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>店<rt>みせ</rt></ruby>で<ruby>友<rt>とも</rt></ruby>だちを（　）、<ruby>携帯電話<rt>けいたいでんわ</rt></ruby>に「<ruby>今日<rt>きょう</rt></ruby>は<ruby>行<rt>い</rt></ruby>けない」という<ruby>連絡<rt>れんらく</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。",
                "options": ["a　待つと", "b　待っていると", "c　待てば"],
                "correct_answer": "b",
                "explanation_ja": "待っている最中に連絡が入ったので「待っていると」。",
                "explanation_en": "'待っていると' (while waiting, a message arrived)."
            },
            {
                "question_id": 313,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>部長<rt>ぶちょう</rt></ruby>は<ruby>私<rt>わたし</rt></ruby>たちの<ruby>話<rt>はなし</rt></ruby>を（　）、<ruby>大<rt>おお</rt></ruby>きくうなずいた。",
                "options": ["a　聞くと", "b　聞いていたら", "c　聞いていると"],
                "correct_answer": "a",
                "explanation_ja": "聞いた直後にうなずいた動作の連続生起なので「聞くと」。",
                "explanation_en": "Immediate subsequent action: '聞くと'."
            },
            {
                "question_id": 314,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "その<ruby>女性<rt>じょせい</rt></ruby>は<ruby>店<rt>みせ</rt></ruby>に（　）、<ruby>窓<rt>まど</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くの<ruby>席<rt>せき</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>った。",
                "options": ["a　入っていたら", "b　入れば", "c　入ると"],
                "correct_answer": "c",
                "explanation_ja": "店に入ってすぐに席に座った動作の連続。「入ると」。",
                "explanation_en": "Successive action: '入ると' (upon entering the shop, sat down)."
            },
            {
                "question_id": 315,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>弟<rt>おとうと</rt></ruby>は<ruby>朝<rt>あさ</rt></ruby>（　）、<ruby>顔<rt>かお</rt></ruby>も<ruby>洗<rt>あら</rt></ruby>わないでどこかに<ruby>出<rt>で</rt></ruby>かけていった。",
                "options": ["a　起きたら", "b　起きれば", "c　起きると"],
                "correct_answer": "c",
                "explanation_ja": "起きるや否やすぐに出ていった連続動作なので「起きると」。",
                "explanation_en": "Successive action: '起きると' (as soon as he woke up)."
            },
            {
                "question_id": 316,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>変<rt>へん</rt></ruby>な<ruby>音<rt>おと</rt></ruby>がしたので、<ruby>窓<rt>まど</rt></ruby>を（　）<ruby>外<rt>そと</rt></ruby>を<ruby>見<rt>み</rt></ruby>た。",
                "options": ["a　開けたら", "b　開ければ", "c　開けて"],
                "correct_answer": "c",
                "explanation_ja": "同一主語の連続する意図的行為をつなぐのでテ形「開けて」。",
                "explanation_en": "Linking intentional successive actions by same subject: '開けて'."
            },
            {
                "question_id": 317,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>家<rt>いえ</rt></ruby>に（　）、<ruby>友<rt>とも</rt></ruby>だちがドアの<ruby>前<rt>まえ</rt></ruby>で<ruby>待<rt>ま</rt></ruby>っていた。",
                "options": ["a　帰ると", "b　帰るなら", "c　帰って"],
                "correct_answer": "a",
                "explanation_ja": "家に帰ったときに待っていた状態を発見したので「帰ると」。",
                "explanation_en": "Discovery upon returning home: '帰ると'."
            },
            {
                "question_id": 318,
                "category": "H 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今<rt>いま</rt></ruby>は（　）お<ruby>金<rt>かね</rt></ruby>もない。<ruby>旅行<rt>りょこう</rt></ruby>は<ruby>無理<rt>むり</rt></ruby>だ。",
                "options": ["a　忙しければ", "b　ひまもなければ", "c　時間もあれば"],
                "correct_answer": "b",
                "explanation_ja": "「Aも〜ばBも…」の並列否定構文。「ひまもなければお金もない」。",
                "explanation_en": "Parallel negation: 'ひまもなければお金もない' (neither time nor money)."
            },
            # ワンポイントレッスン (p. 91) - 7 items
            {
                "question_id": 319,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>車<rt>くるま</rt></ruby>を（　）、ドライブに<ruby>行<rt>い</rt></ruby>きたい。",
                "options": ["a　貸してもらえると", "b　貸してもらえれば"],
                "correct_answer": "b",
                "explanation_ja": "後件が話者の希望（〜たい）なので「〜と」は不可。「貸してもらえれば」が適切。",
                "explanation_en": "'〜と' cannot be followed by speaker's desire; '〜ば' is required."
            },
            {
                "question_id": 320,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>早<rt>はや</rt></ruby>く<ruby>仕事<rt>しごと</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったら、（　）。",
                "options": ["a　飲みに行けるね", "b　飲みに行きませんか"],
                "correct_answer": "a・b",
                "explanation_ja": "「〜たら」の後件には話者の意向や勧誘などどんな文でも来ることができる（両方正解）。",
                "explanation_en": "Both a and b are correct because '〜たら' can take any sentence form in the main clause."
            },
            {
                "question_id": 321,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>早<rt>はや</rt></ruby>く<ruby>予約<rt>よやく</rt></ruby>すれば、（　）。",
                "options": ["a　いい席を取る", "b　いい席が取れる"],
                "correct_answer": "b",
                "explanation_ja": "「〜ば」の後件には可能等の状態文が来る。「いい席が取れる」。",
                "explanation_en": "State/potential predicate fits after '〜ば': 'いい席が取れる'."
            },
            {
                "question_id": 322,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>部屋<rt>へや</rt></ruby>が<ruby>暑<rt>あつ</rt></ruby>ければ、（　）。",
                "options": ["a　窓を開けてください", "b　窓を開けますよ"],
                "correct_answer": "a・b",
                "explanation_ja": "前件が状態・形容詞（暑ければ）の場合、「〜ば」の後件に依頼や意向が来られる（両方正解）。",
                "explanation_en": "Both a and b are valid when condition predicate is an adjective."
            },
            {
                "question_id": 323,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>時間<rt>じかん</rt></ruby>が（　）、<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>はあきらめるつもりだ。",
                "options": ["a　なければ", "b　なかったら"],
                "correct_answer": "a・b",
                "explanation_ja": "状態の否定（なければ／なかったら）は両方とも仮定条件として自然（両方正解）。",
                "explanation_en": "Both a and b are valid."
            },
            {
                "question_id": 324,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "マフラーを（　）、<ruby>彼<rt>かれ</rt></ruby>にあげようと<ruby>思<rt>おも</rt></ruby>う。",
                "options": ["a　作れば", "b　作ったら"],
                "correct_answer": "b",
                "explanation_ja": "前件が動作動詞で後件が意向（あげようと思う）の場合、「〜たら」を使う。「作ったら」。",
                "explanation_en": "With an action verb and volitional intention, '〜たら' is used."
            },
            {
                "question_id": 325,
                "category": "H ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>店<rt>みせ</rt></ruby>の（　）、<ruby>電話<rt>でんわ</rt></ruby>してみます。",
                "options": ["a　電話番号を調べれば", "b　電話番号がわかれば"],
                "correct_answer": "b",
                "explanation_ja": "「〜ば」の後件に話者の意志動詞が来る場合、前件は状態を表す動詞「わかれば」でなければならない。",
                "explanation_en": "State verb 'わかれば' allows speaker intention in main clause with '〜ば'."
            }
        ]
    }
    sections.append(sec3)
    
    # =========================================================================
    # Section 4: Part 1 Review Unit I (後に決まった表現が来る副詞) p. 92-95
    # =========================================================================
    sec4 = {
        "section_number": 4,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>まとめ I <ruby>後<rt>あと</rt></ruby>に<ruby>決<rt>き</rt></ruby>まった<ruby>表現<rt>ひょうげん</rt></ruby>が<ruby>来<rt>く</rt></ruby>る<ruby>副詞<rt>ふくし</rt></ruby>",
        "title_en": "Part 1 Review Unit I: Adverbs Followed by Fixed Expressions",
        "theme": "呼応副詞（否定・比喩・推量・願望・仮定）の整理",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "呼応副詞（否定・推量・比喩）",
                "pattern_name_en": "Correlative Adverbs (Negation, Supposition, Metaphor)",
                "meaning_ja": "文頭の副詞に応じて文末に決まった形式が来る表現。",
                "meaning_en": "Adverbs paired with specific end-of-sentence structures.",
                "connection_forms": [
                    "決して…ない（強い否定）",
                    "めったに…ない（低頻度）",
                    "まるで…ようだ（比喩）",
                    "おそらく…だろう（推量）",
                    "ぜひ…たい/てください（強い希望・依頼）"
                ],
                "nuance_notes": "副詞の意味と文末形式の整合性が問われる。",
                "example_sentences": [
                    {
                        "japanese": "あの<ruby>人<rt>ひと</rt></ruby>は<ruby>決<rt>けっ</rt></ruby>してうそを言わない。",
                        "english": "That person never tells lies."
                    }
                ]
            }
        ],
        "drills": [
            # 練習1 (p. 94) - 14 items
            {
                "question_id": 401,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "（　）<ruby>外国<rt>がいこく</rt></ruby>で<ruby>病気<rt>びょうき</rt></ruby>になった<ruby>場合<rt>ばあい</rt></ruby>は、どうすればいいでしょうか。",
                "options": ["a　万一", "b　ちょうど", "c　どうか"],
                "correct_answer": "a",
                "explanation_ja": "万一〜場合は（万が一の仮定）。",
                "explanation_en": "'万一' (in the unlikely event of)."
            },
            {
                "question_id": 402,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今日<rt>きょう</rt></ruby>の<ruby>会議<rt>かいぎ</rt></ruby>は（　）<ruby>長<rt>なが</rt></ruby>くかかるだろう。",
                "options": ["a　そう", "b　ぜひ", "c　おそらく"],
                "correct_answer": "c",
                "explanation_ja": "おそらく〜だろう（高い確率の推量）。",
                "explanation_en": "'おそらく…だろう' (probably / likely)."
            },
            {
                "question_id": 403,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今日<rt>きょう</rt></ruby>は（　）<ruby>寒<rt>さむ</rt></ruby>くないので、<ruby>上着<rt>うわぎ</rt></ruby>は<ruby>要<rt>い</rt></ruby>らないと<ruby>思<rt>おも</rt></ruby>う。",
                "options": ["a　ただ", "b　たいして", "c　なんとかして"],
                "correct_answer": "b",
                "explanation_ja": "たいして〜ない（それほど〜ない）。",
                "explanation_en": "'たいして…ない' (not particularly / not very)."
            },
            {
                "question_id": 404,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>富士山<rt>ふじさん</rt></ruby>の<ruby>山頂<rt>さんちょう</rt></ruby>から<ruby>見<rt>み</rt></ruby>る<ruby>日<rt>ひ</rt></ruby>の<ruby>出<rt>で</rt></ruby>は、とても<ruby>美<rt>うつく</rt></ruby>しいそうだ。（　）<ruby>見<rt>み</rt></ruby>てみたい。",
                "options": ["a　ぜひ", "b　決して", "c　どんなに"],
                "correct_answer": "a",
                "explanation_ja": "ぜひ〜てみたい（強い希望）。",
                "explanation_en": "'ぜひ…たい' (by all means want to)."
            },
            {
                "question_id": 405,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "あの<ruby>人<rt>ひと</rt></ruby>は（　）<ruby>王様<rt>おうさま</rt></ruby>のように<ruby>人<rt>ひと</rt></ruby>に<ruby>命令<rt>めいれい</rt></ruby>するから<ruby>困<rt>こま</rt></ruby>る。",
                "options": ["a　たとえ", "b　たいして", "c　まるで"],
                "correct_answer": "c",
                "explanation_ja": "まるで〜のように（比喩）。",
                "explanation_en": "'まるで…のようだ' (just like / as if)."
            },
            {
                "question_id": 406,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>救急車<rt>きゅうきゅうしゃ</rt></ruby>の<ruby>音<rt>おと</rt></ruby>は、（　）<ruby>小<rt>ちい</rt></ruby>さくなっていった。",
                "options": ["a　次第に", "b　おそらく", "c　せっかく"],
                "correct_answer": "a",
                "explanation_ja": "次第に〜（徐々に変化する）。",
                "explanation_en": "'次第に' (gradually)."
            },
            {
                "question_id": 407,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "（　）<ruby>彼<rt>かれ</rt></ruby>は<ruby>約束<rt>やくそく</rt></ruby>の<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えたのかもしれない。",
                "options": ["a　万一", "b　もしも", "c　もしかしたら"],
                "correct_answer": "c",
                "explanation_ja": "もしかしたら〜かもしれない（不確実な推量）。",
                "explanation_en": "'もしかしたら…かもしれない' (possibly / perhaps)."
            },
            {
                "question_id": 408,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "（　）<ruby>笑<rt>わら</rt></ruby>わなくてもいいじゃありませんか。",
                "options": ["a　いくら", "b　そんなに", "c　どんなに"],
                "correct_answer": "b",
                "explanation_ja": "そんなに〜なくても（程度がはなはだしいことへの非難）。",
                "explanation_en": "'そんなに' (so much / to that extent)."
            },
            {
                "question_id": 409,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>は<ruby>彼<rt>かれ</rt></ruby>の<ruby>不正<rt>ふせい</rt></ruby>を（　）<ruby>許<rt>ゆる</rt></ruby>さない。",
                "options": ["a　ぜひ", "b　決して", "c　なんとかして"],
                "correct_answer": "b",
                "explanation_ja": "決して〜ない（強い否定の意志）。",
                "explanation_en": "'決して…ない' (never / under no circumstances)."
            },
            {
                "question_id": 410,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今日<rt>きょう</rt></ruby>は（　）<ruby>品物<rt>しなもの</rt></ruby>を<ruby>見<rt>み</rt></ruby>ていただけ何で、<ruby>何<rt>なに</rt></ruby>も<ruby>買<rt>か</rt></ruby>わなかった。",
                "options": ["a　ただ", "b　いくら", "c　せっかく"],
                "correct_answer": "a",
                "explanation_ja": "ただ〜だけで（限定）。",
                "explanation_en": "'ただ…だけで' (merely / only)."
            },
            {
                "question_id": 411,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "あの<ruby>人<rt>ひと</rt></ruby>はいつもまじめな<ruby>顔<rt>かお</rt></ruby>をして、（　）<ruby>笑<rt>わら</rt></ruby>わない。",
                "options": ["a　ますます", "b　そのうち", "c　めったに"],
                "correct_answer": "c",
                "explanation_ja": "めったに〜ない（頻度がごく稀）。",
                "explanation_en": "'めったに…ない' (rarely / seldom)."
            },
            {
                "question_id": 412,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>はその<ruby>事件<rt>じけん</rt></ruby>とは（　）<ruby>関係<rt>かんけい</rt></ruby>がない。",
                "options": ["a　全く", "b　万一", "c　ちょうど"],
                "correct_answer": "a",
                "explanation_ja": "全く〜ない（完全な否定）。",
                "explanation_en": "'全く…ない' (not at all)."
            },
            {
                "question_id": 413,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "（　）<ruby>怒<rt>おこ</rt></ruby>らないで<ruby>私<rt>わたし</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いてください。",
                "options": ["a　どうか", "b　どうも", "c　どんなに"],
                "correct_answer": "a",
                "explanation_ja": "どうか〜てください（懇願・依頼）。",
                "explanation_en": "'どうか…てください' (please, I beg you)."
            },
            {
                "question_id": 414,
                "category": "I 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたときには、<ruby>電車<rt>でんしゃ</rt></ruby>は（　）<ruby>出<rt>で</rt></ruby>ていた。",
                "options": ["a　今に", "b　すでに", "c　まるで"],
                "correct_answer": "b",
                "explanation_ja": "すでに〜ていた（完了）。",
                "explanation_en": "'すでに' (already)."
            },
            # 練習2 (p. 95) - 13 items
            {
                "question_id": 415,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>財布<rt>さいふ</rt></ruby>が<ruby>見<rt>み</rt></ruby>つからない。もしかするとどこかで（　）。",
                "options": ["a　落としただろう", "b　落としたと思う", "c　落としたかもしれない"],
                "correct_answer": "c",
                "explanation_ja": "もしかすると〜かもしれない。",
                "explanation_en": "'もしかすると…かもしれない'."
            },
            {
                "question_id": 416,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今日<rt>きょう</rt></ruby>の<ruby>午後<rt>ごご</rt></ruby>は<ruby>次第<rt>しだい</rt></ruby>に<ruby>気温<rt>きおん</rt></ruby>が（　）でしょう。",
                "options": ["a　上がる", "b　高い", "c　変わらない"],
                "correct_answer": "a",
                "explanation_ja": "次第に＋変化動詞（上がる）。",
                "explanation_en": "'次第に' goes with change verb '上がる'."
            },
            {
                "question_id": 417,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>転<rt>ころ</rt></ruby>んだ<ruby>子<rt>こ</rt></ruby>どもは<ruby>今<rt>いま</rt></ruby>にも（　）<ruby>顔<rt>かお</rt></ruby>をしていた。",
                "options": ["a　泣いた", "b　泣きそうな", "c　泣くような"],
                "correct_answer": "b",
                "explanation_ja": "今にも〜そうだ（直前の様態）。",
                "explanation_en": "'今にも…そうだ' (about to cry at any moment)."
            },
            {
                "question_id": 418,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>展覧会<rt>てんらんかい</rt></ruby>に<ruby>来<rt>き</rt></ruby>た<ruby>人<rt>ひと</rt></ruby>はすでに1<ruby>万人<rt>まんにん</rt></ruby>を（　）。",
                "options": ["a　超えた", "b　超えるだろう", "c　超えていない"],
                "correct_answer": "a",
                "explanation_ja": "すでに＋完了過去「超えた」。",
                "explanation_en": "'すでに' connects to completed past '超えた'."
            },
            {
                "question_id": 419,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "もしも<ruby>入院<rt>にゅういん</rt></ruby>することに（　）、<ruby>仕事<rt>しごと</rt></ruby>を<ruby>休<rt>やす</rt></ruby>まなければならない。",
                "options": ["a　なって", "b　なったら", "c　なったから"],
                "correct_answer": "b",
                "explanation_ja": "もしも〜たら（仮定条件）。",
                "explanation_en": "'もしも…たら'."
            },
            {
                "question_id": 420,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "せっかくカメラを（　）、みんなで<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ろう。",
                "options": ["a　持ってきて", "b　持ってきたら", "c　持ってきたのだから"],
                "correct_answer": "c",
                "explanation_ja": "せっかく〜のだから（好機を無駄にしない）。",
                "explanation_en": "'せっかく…のだから'."
            },
            {
                "question_id": 421,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "A「この<ruby>映画<rt>えいが</rt></ruby>どうだった？<ruby>面白<rt>おもしろ</rt></ruby>かった？」 B「たいして（　）。」",
                "options": ["a　面白かったよ", "b　面白くなかったよ", "c　つまらなかったよ"],
                "correct_answer": "b",
                "explanation_ja": "たいして〜ない（部分否定）。",
                "explanation_en": "'たいして面白くなかったよ'."
            },
            {
                "question_id": 422,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>今日中<rt>きょうじゅうちゅう</rt></ruby>になんとかしてこの<ruby>仕事<rt>しごと</rt></ruby>を（　）。がんばろう。",
                "options": ["a　終わらせたい", "b　終わらせられない", "c　終わらせるだろう"],
                "correct_answer": "a",
                "explanation_ja": "なんとかして〜たい（強い意欲）。",
                "explanation_en": "'なんとかして…たい'."
            },
            {
                "question_id": 423,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "たとえ（　）<ruby>会社<rt>かいしゃ</rt></ruby>には<ruby>行<rt>い</rt></ruby>かなければならない。",
                "options": ["a　大雪でも", "b　大雪では", "c　大雪なのに"],
                "correct_answer": "a",
                "explanation_ja": "たとえ〜ても（逆接の仮定）。",
                "explanation_en": "'たとえ…ても'."
            },
            {
                "question_id": 424,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "まだ<ruby>試合<rt>しあい</rt></ruby>の<ruby>途中<rt>とちゅう</rt></ruby>なのに、まるでもう（　）みんな<ruby>大喜<rt>おおよろこ</rt></ruby>びしている。",
                "options": ["a　勝ったので", "b　勝ったように", "c　勝ったらしく"],
                "correct_answer": "b",
                "explanation_ja": "まるで〜ように（比喩表現）。",
                "explanation_en": "'まるで…ように'."
            },
            {
                "question_id": 425,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>資料<rt>しりょう</rt></ruby>はそんなに（　）。",
                "options": ["a　役に立つかもしれない", "b　役に立つはずだ", "c　役に立たないだろう"],
                "correct_answer": "c",
                "explanation_ja": "そんなに〜ない（程度の否定否定推量）。",
                "explanation_en": "'そんなに…ないだろう'."
            },
            {
                "question_id": 426,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>日本語<rt>にほんご</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>めてから、<ruby>少<rt>すこ</rt></ruby>しずつ（　）。",
                "options": ["a　話せる", "b　上手になってきた", "c　わからない"],
                "correct_answer": "b",
                "explanation_ja": "少しずつ＋変化の進行（上手になってきた）。",
                "explanation_en": "'少しずつ上手になってきた'."
            },
            {
                "question_id": 427,
                "category": "I 練習2",
                "question_type": "multiple_choice",
                "prompt": "<ruby>国<rt>くに</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ってもどうか（　）。",
                "options": ["a　忘れないでください", "b　手紙を書きたいです", "c　遊びに来ませんか"],
                "correct_answer": "a",
                "explanation_ja": "どうか〜てください（懇願）。",
                "explanation_en": "'どうか…てください'."
            }
        ]
    }
    sections.append(sec4)
    
    # =========================================================================
    # Section 5: Part 1 Review Unit J (動詞や名詞の意味を広げる文法形式) p. 96-99
    # =========================================================================
    sec5 = {
        "section_number": 5,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>まとめ J <ruby>動詞<rt>どうし</rt></ruby>や<ruby>名詞<rt>めいし</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>を<ruby>広<rt>ひろ</rt></ruby>げる<ruby>文法形式<rt>ぶんぽうけいしき</rt></ruby>",
        "title_en": "Part 1 Review Unit J: Grammatical Forms that Expand Verb and Noun Meanings",
        "theme": "接尾辞的表現（〜やすい、〜づらい、〜きれない、〜っぽい、〜らしい等）",
        "patterns": [
            {
                "pattern_number": 1,
                "pattern_name": "動詞連用形・名詞接続の接尾表現",
                "pattern_name_en": "Suffix Expressions Expanding Verb/Noun Meaning",
                "meaning_ja": "動詞や名詞の後ろに付いて、容易・困難・過度・傾向などを表す。",
                "meaning_en": "Attached to verbs or nouns to express ease, difficulty, excess, tendency, etc.",
                "connection_forms": [
                    "V-ます + やすい / にくい / づらい",
                    "V-ます + すぎる / かける / きる / だす / 通す",
                    "N + だらけ / っぽい / らしい / みたいだ"
                ],
                "nuance_notes": "話者の感覚や客観的性質の表現。",
                "example_sentences": [
                    {
                        "japanese": "この<ruby>薬<rt>くすり</rt></ruby>は<ruby>飲<rt>の</rt></ruby>みやすい。",
                        "english": "This medicine is easy to swallow."
                    }
                ]
            }
        ],
        "drills": [
            # 練習1 (p. 98) - 10 items
            {
                "question_id": 501,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "（　）ことでも、<ruby>時<rt>とき</rt></ruby>にははっきり<ruby>言<rt>い</rt></ruby>わなければならないだろう。",
                "options": ["a　言いやすい", "b　言いづらい", "c　言いすぎる"],
                "correct_answer": "b",
                "explanation_ja": "言いにくい・心理的に抵抗があること。「言いづらい」。",
                "explanation_en": "'言いづらい' (difficult to say / awkward to say)."
            },
            {
                "question_id": 502,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>料理<rt>りょうり</rt></ruby>はちょっと（　）、あまりおいしくない。",
                "options": ["a　水らしくて", "b　水がちで", "c　水っぽくて"],
                "correct_answer": "c",
                "explanation_ja": "水分が多くて味が薄いマイナス評価。「水っぽくて」。",
                "explanation_en": "'水っぽくて' (watery)."
            },
            {
                "question_id": 503,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "パソコンを（　）のは、<ruby>目<rt>め</rt></ruby>に<ruby>悪<rt>わる</rt></ruby>いですよ。",
                "options": ["a　使いかける", "b　使い出す", "c　使いすぎる"],
                "correct_answer": "c",
                "explanation_ja": "過度な使用。「使いすぎる」。",
                "explanation_en": "'使いすぎる' (overuse / use too much)."
            },
            {
                "question_id": 504,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>試合<rt>しあい</rt></ruby>では<ruby>実力<rt>じつりょく</rt></ruby>を（　）ほしい。みんながんばれ。",
                "options": ["a　出しすぎて", "b　出しきって", "c　出しかけて"],
                "correct_answer": "b",
                "explanation_ja": "持っている力を最後まで全て出し尽くす。「出しきって」。",
                "explanation_en": "'出しきって' (give it your all / exhaust all ability)."
            },
            {
                "question_id": 505,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>祖父<rt>そふ</rt></ruby>は<ruby>年<rt>とし</rt></ruby>を<ruby>取<rt>と</rt></ruby>って、<ruby>最近<rt>さいきん</rt></ruby>（　）なった。<ruby>今日<rt>きょう</rt></ruby>もかぎの<ruby>場所<rt>ばしょ</rt></ruby>を<ruby>忘<rt>わす</rt></ruby>れた。",
                "options": ["a　忘れかけに", "b　忘れにくく", "c　忘れっぽく"],
                "correct_answer": "c",
                "explanation_ja": "よく忘れる性質。「忘れっぽく」。",
                "explanation_en": "'忘れっぽく' (forgetful)."
            },
            {
                "question_id": 506,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>庭<rt>にわ</rt></ruby>に<ruby>植<rt>う</rt></ruby>えた<ruby>木<rt>き</rt></ruby>が<ruby>大<rt>おお</rt></ruby>きく（　）しまったので、<ruby>少<rt>すこ</rt></ruby>し<ruby>切<rt>き</rt></ruby>ることにした。",
                "options": ["a　なりすぎて", "b　なりやすくなって", "c　なり通して"],
                "correct_answer": "a",
                "explanation_ja": "大きくなりすぎた。「なりすぎて」。",
                "explanation_en": "'なりすぎて' (grown too big)."
            },
            {
                "question_id": 507,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>時間<rt>じかん</rt></ruby>が<ruby>短<rt>みじか</rt></ruby>かったので、<ruby>作文<rt>さくぶん</rt></ruby>を<ruby>最後<rt>さいご</rt></ruby>まで（　）。",
                "options": ["a　書き出せなかった", "b　書ききれなかった", "c　書きかけられなかった"],
                "correct_answer": "b",
                "explanation_ja": "最後まで完了できなかった。「書ききれなかった」。",
                "explanation_en": "'書ききれなかった' (could not finish writing)."
            },
            {
                "question_id": 508,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>信号<rt>しんごう</rt></ruby>が<ruby>青<rt>あお</rt></ruby>に<ruby>変<rt>か</rt></ruby>わって、<ruby>車<rt>くるま</rt></ruby>が（　）。",
                "options": ["a　走り出した", "b　走り通した", "c　走りきった"],
                "correct_answer": "a",
                "explanation_ja": "走り始めた。「走り出した」。",
                "explanation_en": "'走り出した' (started running/driving)."
            },
            {
                "question_id": 509,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "うそを<ruby>一生<rt>いっしょう</rt></ruby>（　）ことはできない。",
                "options": ["a　隠しかける", "b　隠しすぎる", "c　隠し通す"],
                "correct_answer": "c",
                "explanation_ja": "最後まで貫く。「隠し通す」。",
                "explanation_en": "'隠し通す' (keep concealed all the way to the end)."
            },
            {
                "question_id": 510,
                "category": "J 練習1",
                "question_type": "multiple_choice",
                "prompt": "<ruby>少<rt>すこ</rt></ruby>し（　）きた<ruby>数学<rt>すうがく</rt></ruby>が、<ruby>授業<rt>じゅぎょう</rt></ruby>を<ruby>休<rt>やす</rt></ruby>んだせいでまたわからなくなった。",
                "options": ["a　わかりかけて", "b　わかりきって", "c　わかり通して"],
                "correct_answer": "a",
                "explanation_ja": "途中でわかりかけていた。「わかりかけて」。",
                "explanation_en": "'わかりかけて' (had begun to understand)."
            },
            # 練習2 (p. 98-99) - 10 items
            {
                "question_id": 511,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>雪道<rt>ゆきみち</rt></ruby>はすべり（　）から、<ruby>気<rt>き</rt></ruby>をつけて。",
                "correct_answer": "やすい",
                "explanation_ja": "「すべりやすい」＝滑る危険性が高い。",
                "explanation_en": "'すべりやすい' (slippery / easy to slip)."
            },
            {
                "question_id": 512,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>社長<rt>しゃちょう</rt></ruby>なら<ruby>社長<rt>しゃちょう</rt></ruby>（　）<ruby>行動<rt>こうどう</rt></ruby>してほしいです。<ruby>今<rt>いま</rt></ruby>は<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>時期<rt>じき</rt></ruby>なんですから。",
                "correct_answer": "らしく",
                "explanation_ja": "社長にふさわしい行動。「社長らしく」。",
                "explanation_en": "'社長らしく' (act like a proper president)."
            },
            {
                "question_id": 513,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "この<ruby>仕事<rt>しごと</rt></ruby>がまだやり（　）ので、<ruby>終<rt>お</rt></ruby>わったらそちらの<ruby>仕事<rt>しごと</rt></ruby>を<ruby>手伝<rt>てつだ</rt></ruby>います。",
                "correct_answer": "かけな",
                "explanation_ja": "途中の状態。「やりかけなので」。",
                "explanation_en": "'やりかけなので' (since I'm in the middle of doing this)."
            },
            {
                "question_id": 514,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "このひもはすぐ<ruby>切<rt>き</rt></ruby>れてしまいます。もっと<ruby>切<rt>き</rt></ruby>れ（　）のはありませんか。",
                "correct_answer": "にくい",
                "explanation_ja": "簡単には切れないもの。「切れにくいの」。",
                "explanation_en": "'切れにくいの' (one that doesn't break easily)."
            },
            {
                "question_id": 515,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "この<ruby>部屋<rt>へや</rt></ruby>は<ruby>長<rt>なが</rt></ruby>い<ruby>間<rt>あいだ</rt></ruby><ruby>掃除<rt>そうじ</rt></ruby>をしていないので、ごみ（　）。",
                "correct_answer": "だらけだ",
                "explanation_ja": "ごみが一面にある。「ごみだらけだ」。",
                "explanation_en": "'ごみだらけだ' (full of trash)."
            },
            {
                "question_id": 516,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>犬<rt>いぬ</rt></ruby>が<ruby>飼<rt>か</rt></ruby>い<ruby>主<rt>ぬし</rt></ruby>を<ruby>助<rt>たす</rt></ruby>けるというドラマ（　）ことが<ruby>実際<rt>じっさい</rt></ruby>に<ruby>起<rt>お</rt></ruby>こった。",
                "correct_answer": "みたいな",
                "explanation_ja": "ドラマのような事態。「ドラマみたいなこと」。",
                "explanation_en": "'ドラマみたいなこと' (a drama-like event)."
            },
            {
                "question_id": 517,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>京都<rt>きょうと</rt></ruby>に<ruby>行<rt>い</rt></ruby>ったら、<ruby>記念<rt>きねん</rt></ruby>に<ruby>何<rt>なに</rt></ruby>か<ruby>京都<rt>きょうと</rt></ruby>（　）<ruby>物<rt>もの</rt></ruby>を<ruby>買<rt>か</rt></ruby>いたいと<ruby>思<rt>おも</rt></ruby>う。",
                "correct_answer": "らしい",
                "explanation_ja": "京都のイメージにぴったりなもの。「京都らしい物」。",
                "explanation_en": "'京都らしい物' (something typical of Kyoto)."
            },
            {
                "question_id": 518,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>今<rt>いま</rt></ruby>の<ruby>時期<rt>じき</rt></ruby>は<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>が<ruby>腐<rt>くさ</rt></ruby>り（　）ので<ruby>注意<rt>ちゅうい</rt></ruby>しましょう。",
                "correct_answer": "やすい",
                "explanation_ja": "腐る傾向が高い。「腐りやすいので」。",
                "explanation_en": "'腐りやすいので' (spoils easily)."
            },
            {
                "question_id": 519,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "<ruby>飲<rt>の</rt></ruby>み（　）ですよ。<ruby>今日<rt>きょう</rt></ruby>はもうやめたらどうですか。",
                "correct_answer": "すぎ",
                "explanation_ja": "過度な飲酒。「飲みすぎですよ」。",
                "explanation_en": "'飲みすぎですよ' (drinking too much)."
            },
            {
                "question_id": 520,
                "category": "J 練習2",
                "question_type": "fill_in_the_blank",
                "prompt": "この<ruby>飲<rt>の</rt></ruby>み（　）かんジュースはだれののう。",
                "correct_answer": "かけの",
                "explanation_ja": "飲みかけの状態の名詞修飾。「飲みかけの」。",
                "explanation_en": "'飲みかけの' (half-drunk can of juice)."
            },
            # ワンポイントレッスン (p. 99) - 7 items
            {
                "question_id": 521,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "もう<ruby>大人<rt>おとな</rt></ruby>なんだから、そんな<ruby>子<rt>こ</rt></ruby>ども（　）しゃべり<ruby>方<rt>かた</rt></ruby>はやめろ。",
                "options": ["a　らしい", "b　みたいな"],
                "correct_answer": "b",
                "explanation_ja": "大人が子供に似ている（実際は子供ではない）比喩なので「みたいな」。",
                "explanation_en": "Metaphor (not actually a child): '子どもみたいな'."
            },
            {
                "question_id": 522,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>子<rt>こ</rt></ruby>どもにはやはり<ruby>子<rt>こ</rt></ruby>ども（　）<ruby>服<rt>ふく</rt></ruby>が<ruby>似合<rt>にあ</rt></ruby>いますよね。",
                "options": ["a　らしい", "b　みたいな"],
                "correct_answer": "a",
                "explanation_ja": "実際に子供である者にふさわしい典型的な性質なので「らしい」。",
                "explanation_en": "Typical characteristic of actual children: '子どもらしい'."
            },
            {
                "question_id": 523,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "6<ruby>月<rt>がつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ってからまだ<ruby>雨<rt>あめ</rt></ruby>（　）<ruby>雨<rt>あめ</rt></ruby>は<ruby>降<rt>ふ</rt></ruby>っていない。",
                "options": ["a　らしい", "b　みたいな"],
                "correct_answer": "a",
                "explanation_ja": "本格的な雨といえる典型的な雨。「雨らしい雨」。",
                "explanation_en": "'雨らしい雨' (real, proper rain)."
            },
            {
                "question_id": 524,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "あれ、<ruby>雪<rt>ゆき</rt></ruby>（　）<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ってきたよ。",
                "options": ["a　らしい", "b　みたいな"],
                "correct_answer": "b",
                "explanation_ja": "雪のような雨（実際は雨）という比喩・類似なので「雪みたいな」。",
                "explanation_en": "Resemblance metaphor: '雪みたいな雨' (snow-like rain)."
            },
            {
                "question_id": 525,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "まだ5<ruby>月<rt>がつ</rt></ruby>なのに、<ruby>今日<rt>きょう</rt></ruby>は<ruby>夏<rt>なつ</rt></ruby>（　）<ruby>日<rt>ひ</rt></ruby>でしたね。",
                "options": ["a　らしい", "b　のような"],
                "correct_answer": "b",
                "explanation_ja": "5月で夏ではないので「夏のような日」。",
                "explanation_en": "Not actually summer: '夏のような日' (summer-like day)."
            },
            {
                "question_id": 526,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "へえ、これが<ruby>交番<rt>こうばん</rt></ruby>か。<ruby>絵本<rt>えほん</rt></ruby>に<ruby>出<rt>で</rt></ruby>てくるかわいい<ruby>家<rt>いえ</rt></ruby>（　）ね。",
                "options": ["a　らしい", "b　のようだ"],
                "correct_answer": "b",
                "explanation_ja": "実際は交番であって絵本の家ではないので「のようだ」。",
                "explanation_en": "Simile: '絵本に出てくるかわいい家のようだ'."
            },
            {
                "question_id": 527,
                "category": "J ワンポイント",
                "question_type": "multiple_choice",
                "prompt": "<ruby>箱根<rt>はこね</rt></ruby>は<ruby>昔<rt>むかし</rt></ruby>からの<ruby>観光地<rt>かんこうち</rt></ruby>だから、<ruby>観光地<rt>かんこうち</rt></ruby>（　）お<ruby>土産屋<rt>みやげや</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い。",
                "options": ["a　らしい", "b　のような"],
                "correct_answer": "a",
                "explanation_ja": "実際に観光地であり、それにふさわしいので「観光地らしい」。",
                "explanation_en": "Truly a sightseeing area: '観光地らしい'."
            }
        ]
    }
    sections.append(sec5)
    
    # =========================================================================
    # Section 6: まとめ問題 (A〜J) p. 100-101
    # =========================================================================
    sec6 = {
        "section_number": 6,
        "title": "<ruby>第<rt>だい</rt></ruby>1<ruby>部<rt>ぶ</rt></ruby>まとめ <ruby>問題<rt>もんだい</rt></ruby> (A〜J)",
        "title_en": "Part 1 Review Test (Units A-J)",
        "theme": "第1部まとめA〜Jの総合復習テスト",
        "patterns": [],
        "drills": [
            {
                "question_id": 601,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>店<rt>みせ</rt></ruby>には<ruby>高<rt>たか</rt></ruby>い<ruby>品物<rt>しなもの</rt></ruby>（　）<ruby>並<rt>なら</rt></ruby>んでいる。",
                "options": ["1　ぐらい", "2　なんか", "3　しか", "4　ばかり"],
                "correct_answer": 4,
                "explanation_ja": "「高い品物ばかり並んでいる」＝高い品物だけが並んでいる。",
                "explanation_en": "'ばかり' expresses 'only/nothing but': only expensive items are lined up."
            },
            {
                "question_id": 602,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "<ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>がたくさん<ruby>重<rt>かさ</rt></ruby>ねてあって、<ruby>今<rt>いま</rt></ruby>にも（　）。",
                "options": ["1　崩れているようだ", "2　崩れそうだ", "3　崩れてしまった", "4　崩れたら大変だ"],
                "correct_answer": 2,
                "explanation_ja": "「今にも〜そうだ」で直前の切迫した様態。「崩れそうだ」。",
                "explanation_en": "'今にも…そうだ' indicates that an event is about to happen at any second."
            },
            {
                "question_id": 603,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>本<rt>ほん</rt></ruby>は、いつも（　）、ぼろぼろになってしまった。<ruby>新<rt>あたら</rt></ruby>しいのを<ruby>買<rt>か</rt></ruby>おうかな。",
                "options": ["1　持ち歩いていては", "2　持ち歩いていれば", "3　持ち歩いていたら", "4　持ち歩いているなら"],
                "correct_answer": 3,
                "explanation_ja": "「〜ていたら」で動作を続けた結果ボロボロになった発見・経過。「持ち歩いていたら」。",
                "explanation_en": "'〜ていたら' shows a continuing condition leading to a realized outcome."
            },
            {
                "question_id": 604,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "<ruby>質問<rt>しつもん</rt></ruby>の<ruby>答<rt>こた</rt></ruby>えをここに（　）<ruby>場合<rt>ばあい</rt></ruby>は、<ruby>紙<rt>かみ</rt></ruby>の<ruby>裏<rt>うら</rt></ruby>に<ruby>続<rt>つづ</rt></ruby>きを<ruby>書<rt>か</rt></ruby>いてください。",
                "options": ["1　書きかける", "2　書き終わる", "3　書ききれない", "4　書き通せない"],
                "correct_answer": 3,
                "explanation_ja": "すべて書ききることができない場合。「書ききれない場合は」。",
                "explanation_en": "'V-きれない' indicates inability to completely finish: '書ききれない'."
            },
            {
                "question_id": 605,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "<ruby>私<rt>わたし</rt></ruby>はそのとき<ruby>彼<rt>かれ</rt></ruby>が<ruby>言<rt>い</rt></ruby>った<ruby>言葉<rt>ことば</rt></ruby>を<ruby>決<rt>けっ</rt></ruby>して（　）。",
                "options": ["1　覚えていたい", "2　忘れないだろう", "3　思い出した", "4　忘れようと思う"],
                "correct_answer": 2,
                "explanation_ja": "「決して〜ない」の呼応。「忘れないだろう」。",
                "explanation_en": "'決して…ない' (never / definitely not forget)."
            },
            {
                "question_id": 606,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "A「<ruby>将来<rt>しょうらい</rt></ruby>はどんな<ruby>仕事<rt>しごと</rt></ruby>をしたいのですか。」 B「<ruby>私<rt>わたし</rt></ruby>は（　）<ruby>日本<rt>にほん</rt></ruby>に<ruby>関係<rt>かんけい</rt></ruby>がある<ruby>仕事<rt>しごと</rt></ruby>をしたいと<ruby>考<rt>かんが</rt></ruby>えています。」",
                "options": ["1　どうか", "2　まるで", "3　おそらく", "4　ぜひ"],
                "correct_answer": 4,
                "explanation_ja": "「ぜひ〜たい」で強い希望を表す。",
                "explanation_en": "'ぜひ…たい' expresses strong personal desire."
            },
            {
                "question_id": 607,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "すみません。はんこをお<ruby>願<rt>ねが</rt></ruby>いします。<ruby>書留<rt>かきとめ</rt></ruby>ははんこをいただかないとお<ruby>渡<rt>わた</rt></ruby>しできない（　）んです。",
                "options": ["1　ことになっている", "2　ようにしている", "3　ことにする", "4　ようになる"],
                "correct_answer": 1,
                "explanation_ja": "郵便局の規則・決まりなので「ことになっている」。",
                "explanation_en": "Official rule/system: 'ことになっている'."
            },
            {
                "question_id": 608,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "<ruby>林君<rt>はやしくん</rt></ruby>は（　）スポーツもできて、クラスの<ruby>女<rt>おんな</rt></ruby>の<ruby>子<rt>こ</rt></ruby>たちに<ruby>人気<rt>にんき</rt></ruby>がある。",
                "options": ["1　頭がいいと", "2　頭もよければ", "3　頭がよかったら", "4　頭もいいのなら"],
                "correct_answer": 2,
                "explanation_ja": "「Aも〜ばBも…」の並列構文。「頭もよければスポーツもできて」。",
                "explanation_en": "Parallel additive construction: '頭もよければスポーツもできて' (both smart and athletic)."
            },
            {
                "question_id": 609,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "<ruby>自分<rt>じぶん</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>を（　）、ほかの<ruby>人<rt>ひと</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>もよく<ruby>聞<rt>き</rt></ruby>くようにしたほうがいいよ。",
                "options": ["1　するばかりでなく", "2　したばかりでなく", "3　するばかりで", "4　しないばかりで"],
                "correct_answer": 1,
                "explanation_ja": "「〜ばかりでなく…も」で添加を表す。「自分の話をするばかりでなく」。",
                "explanation_en": "'〜ばかりでなく…も' (not only talking about yourself, but also...)."
            },
            {
                "question_id": 610,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "みんなと<ruby>同<rt>おな</rt></ruby>じような<ruby>服<rt>ふく</rt></ruby>ではなくて、<ruby>自分<rt>じぶん</rt></ruby>（　）<ruby>服<rt>ふく</rt></ruby>を<ruby>着<rt>き</rt></ruby>たい。",
                "options": ["1　みたいな", "2　のつもりの", "3　らしい", "4　のような"],
                "correct_answer": 3,
                "explanation_ja": "自分本来の個性・自分にふさわしい服。「自分らしい服」。",
                "explanation_en": "'自分らしい服' (clothes that truly reflect oneself)."
            },
            {
                "question_id": 611,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "この<ruby>石<rt>せっ</rt></ruby>けんを（　）、<ruby>新<rt>あたら</rt></ruby>しいのを<ruby>出<rt>だ</rt></ruby>そう。",
                "options": ["1　使いすぎてから", "2　使いきってから", "3　使いすぎると", "4　使いきると"],
                "correct_answer": 2,
                "explanation_ja": "全部最後まで使ってから。「使いきってから」。",
                "explanation_en": "'V-きってから' (after using up completely)."
            },
            {
                "question_id": 612,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "A「あれ、<ruby>山田<rt>やまだ</rt></ruby>さんは？もう<ruby>帰<rt>かえ</rt></ruby>った？」 B「<ruby>山田<rt>やまだ</rt></ruby>さんならたった<ruby>今<rt>いま</rt></ruby>（　）だから、まだその<ruby>辺<rt>へん</rt></ruby>にいると<ruby>思<rt>おも</rt></ruby>いますよ。」",
                "options": ["1　帰るばかり", "2　帰っているところ", "3　帰ってばかり", "4　帰ったところ"],
                "correct_answer": 4,
                "explanation_ja": "「たった今〜たところ」で直前の客観的動作完了。「帰ったところ」。",
                "explanation_en": "'たった今…たところ' (just left a moment ago)."
            },
            {
                "question_id": 613,
                "category": "まとめ問題 A〜J",
                "question_type": "multiple_choice",
                "prompt": "いつの<ruby>間<rt>ま</rt></ruby>にか<ruby>眠<rt>ねむ</rt></ruby>ってしまって、<ruby>目<rt>め</rt></ruby>が<ruby>覚<rt>さ</rt></ruby>めると、<ruby>外<rt>そと</rt></ruby>はもう（　）。",
                "options": ["1　明るくした", "2　明るくなった", "3　明るくしていた", "4　明るくなっていた"],
                "correct_answer": 4,
                "explanation_ja": "目が覚めた時点ですでに明るい状態になっていたことの発見。「明るくなっていた」。",
                "explanation_en": "'明るくなっていた' denotes discovery of the existing state upon waking up."
            }
        ]
    }
    sections.append(sec6)
    
    return sections
