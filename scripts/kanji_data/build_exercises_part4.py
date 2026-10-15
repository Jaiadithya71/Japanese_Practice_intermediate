# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = {
  "part": 4,
  "lessons_covered": [16, 17, 18, 19, 20],
  "lessons": [
    {
      "lesson_number": 16,
      "title": "第16回 交通・旅行 (2) (Transportation and Travel 2)",
      "page_range": "60-62",
      "exercises": [
        {
          "exercise_id": "k_ex_16_1",
          "number": 1,
          "type": "reading_recall",
          "instruction_ja": "＿＿の部分の読み方を書きましょう。",
          "instruction_en": "Write the reading for the underlined kanji in the travel brochure and dialogue.",
          "context_title": "5日間ツアー案内・旅行会社の会話",
          "items": [
            {
              "id": "k_ex_16_1_a",
              "label": "a",
              "sentence": "a【美しい】<ruby>海<rt>うみ</rt></ruby>と<ruby>島<rt>しま</rt></ruby>があなたを<ruby>待<rt>ま</rt></ruby>っている！",
              "target": "美しい",
              "answer": "うつくしい",
              "reading": "うつくしい",
              "meaning": "beautiful",
              "ruby_html": "<ruby>美<rt>うつく</rt></ruby>しい<ruby>海<rt>うみ</rt></ruby>と<ruby>島<rt>しま</rt></ruby>があなたを<ruby>待<rt>ま</rt></ruby>っている！",
              "translation": "Beautiful seas and islands are waiting for you!",
              "explanation": "美しい（うつくしい）は形容詞の訓読みです（音読みはビ：美術館）。"
            },
            {
              "id": "k_ex_16_1_b",
              "label": "b",
              "sentence": "<ruby>美<rt>うつく</rt></ruby>しい<ruby>海<rt>うみ</rt></ruby>とb【島】があなたを<ruby>待<rt>ま</rt></ruby>っている！",
              "target": "島",
              "answer": "しま",
              "reading": "しま",
              "meaning": "island",
              "ruby_html": "<ruby>美<rt>うつく</rt></ruby>しい<ruby>海<rt>うみ</rt></ruby>と<ruby>島<rt>しま</rt></ruby>があなたを<ruby>待<rt>ま</rt></ruby>っている！",
              "translation": "Beautiful seas and islands are waiting for you!",
              "explanation": "島（しま）は訓読みです（音読みはトウ：半島）。"
            },
            {
              "id": "k_ex_16_1_c",
              "label": "c",
              "sentence": "<ruby>南<rt>みなみ</rt></ruby>の<ruby>海<rt>うみ</rt></ruby>で<ruby>魚<rt>さかな</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>にc【泳ごう】！",
              "target": "泳ごう",
              "answer": "およごう",
              "reading": "およごう",
              "meaning": "let's swim",
              "ruby_html": "<ruby>南<rt>みなみ</rt></ruby>の<ruby>海<rt>うみ</rt></ruby>で<ruby>魚<rt>さかな</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>泳<rt>およ</rt></ruby>ごう！",
              "translation": "Let's swim together with fish in the southern sea!",
              "explanation": "泳ぐ（およぐ）の意向形「泳ごう（およごう）」です。"
            },
            {
              "id": "k_ex_16_1_d",
              "label": "d",
              "sentence": "ご<ruby>希望<rt>きぼう</rt></ruby>の<ruby>方<rt>かた</rt></ruby>はd【美術館】<ruby>見学<rt>けんがく</rt></ruby>、<ruby>登山<rt>とざん</rt></ruby>などもできます。",
              "target": "美術館",
              "answer": "びじゅつかん",
              "reading": "びじゅつかん",
              "meaning": "art museum",
              "ruby_html": "ご<ruby>希望<rt>きぼう</rt></ruby>の<ruby>方<rt>かた</rt></ruby>は<ruby>美術館<rt>びじゅつかん</rt></ruby><ruby>見学<rt>けんがく</rt></ruby>、<ruby>登山<rt>とざん</rt></ruby>などもできます。",
              "translation": "Those who wish can also visit an art museum or go mountain climbing.",
              "explanation": "美術館（びじゅつかん）は音読みの熟語です。"
            },
            {
              "id": "k_ex_16_1_e",
              "label": "e",
              "sentence": "ご<ruby>希望<rt>きぼう</rt></ruby>の<ruby>方<rt>かた</rt></ruby>は<ruby>美術館<rt>びじゅつかん</rt></ruby><ruby>見学<rt>けんがく</rt></ruby>、e【登山】などもできます。",
              "target": "登山",
              "answer": "とざん",
              "reading": "とざん",
              "meaning": "mountain climbing",
              "ruby_html": "ご<ruby>希望<rt>きぼう</rt></ruby>の<ruby>方<rt>かた</rt></ruby>は<ruby>美術館<rt>びじゅつかん</rt></ruby><ruby>見学<rt>けんがく</rt></ruby>、<ruby>登山<rt>とざん</rt></ruby>などもできます。",
              "translation": "Those who wish can also visit an art museum or go mountain climbing.",
              "explanation": "登山（とざん）では「山」が連濁して「ざん」と読みます。"
            },
            {
              "id": "k_ex_16_1_f",
              "label": "f",
              "sentence": "ガイド：f【空港】を10<ruby>時<rt>じ</rt></ruby>に<ruby>出発<rt>しゅっぱつ</rt></ruby>して、<ruby>向<rt>む</rt></ruby>こうの<ruby>空港<rt>くうこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くのは12<ruby>時<rt>じ</rt></ruby>の<ruby>予定<rt>よてい</rt></ruby>です。",
              "target": "空港",
              "answer": "くうこう",
              "reading": "くうこう",
              "meaning": "airport",
              "ruby_html": "ガイド：<ruby>空港<rt>くうこう</rt></ruby>を10<ruby>時<rt>じ</rt></ruby>に<ruby>出発<rt>しゅっぱつ</rt></ruby>して、<ruby>向<rt>む</rt></ruby>こうの<ruby>空港<rt>くうこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くのは12<ruby>時<rt>じ</rt></ruby>の<ruby>予定<rt>よてい</rt></ruby>です。",
              "translation": "Guide: We depart the airport at 10 o'clock and are scheduled to arrive at the airport over there at 12 o'clock.",
              "explanation": "空港（くうこう）は「空の港」という意味の音読み熟語です。"
            },
            {
              "id": "k_ex_16_1_g",
              "label": "g",
              "sentence": "ガイド：<ruby>空港<rt>くうこう</rt></ruby>を10<ruby>時<rt>じ</rt></ruby>に<ruby>出発<rt>しゅっぱつ</rt></ruby>して、g【向こう】の<ruby>空港<rt>くうこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くのは12<ruby>時<rt>じ</rt></ruby>の<ruby>予定<rt>よてい</rt></ruby>です。",
              "target": "向こう",
              "answer": "むこう",
              "reading": "むこう",
              "meaning": "over there / destination side",
              "ruby_html": "ガイド：<ruby>空港<rt>くうこう</rt></ruby>を10<ruby>時<rt>じ</rt></ruby>に<ruby>出発<rt>しゅっぱつ</rt></ruby>して、<ruby>向<rt>む</rt></ruby>こうの<ruby>空港<rt>くうこう</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くのは12<ruby>時<rt>じ</rt></ruby>の<ruby>予定<rt>よてい</rt></ruby>です。",
              "translation": "Guide: We depart the airport at 10 o'clock and are scheduled to arrive at the airport over there at 12 o'clock.",
              "explanation": "向こう（むこう）は離れた場所や目的地側を表します。"
            },
            {
              "id": "k_ex_16_1_h",
              "label": "h",
              "sentence": "そこからh【港】までバスで<ruby>行<rt>い</rt></ruby>って、<ruby>船<rt>ふね</rt></ruby>で<ruby>島<rt>しま</rt></ruby>に<ruby>渡<rt>わた</rt></ruby>ります。",
              "target": "港",
              "answer": "みなと",
              "reading": "みなと",
              "meaning": "harbor / port",
              "ruby_html": "そこから<ruby>港<rt>みなと</rt></ruby>までバスで<ruby>行<rt>い</rt></ruby>って、<ruby>船<rt>ふね</rt></ruby>で<ruby>島<rt>しま</rt></ruby>に<ruby>渡<rt>わた</rt></ruby>ります。",
              "translation": "From there we go to the port by bus and cross over to the island by boat.",
              "explanation": "港（みなと）は訓読みです（音読みはコウ：空港）。"
            },
            {
              "id": "k_ex_16_1_i",
              "label": "i",
              "sentence": "そこから<ruby>港<rt>みなと</rt></ruby>までバスで<ruby>行<rt>い</rt></ruby>って、i【船】で<ruby>島<rt>しま</rt></ruby>に<ruby>渡<rt>わた</rt></ruby>ります。",
              "target": "船",
              "answer": "ふね",
              "reading": "ふね",
              "meaning": "ship / boat",
              "ruby_html": "そこから<ruby>港<rt>みなと</rt></ruby>までバスで<ruby>行<rt>い</rt></ruby>って、<ruby>船<rt>ふね</rt></ruby>で<ruby>島<rt>しま</rt></ruby>に<ruby>渡<rt>わた</rt></ruby>ります。",
              "translation": "From there we go to the port by bus and cross over to the island by boat.",
              "explanation": "船（ふね）は訓読みです（音読みはセン：風船）。"
            },
            {
              "id": "k_ex_16_1_j",
              "label": "j",
              "sentence": "<ruby>途中<rt>とちゅう</rt></ruby>までバスで<ruby>行<rt>い</rt></ruby>って、そこからj【登ります】。",
              "target": "登ります",
              "answer": "のぼります",
              "reading": "のぼります",
              "meaning": "climb",
              "ruby_html": "<ruby>途中<rt>とちゅう</rt></ruby>までバスで<ruby>行<rt>い</rt></ruby>って、そこから<ruby>登<rt>のぼ</rt></ruby>ります。",
              "translation": "You go partway by bus and climb from there.",
              "explanation": "登る（のぼる）は山や高い所へ上がることに使います。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_16_2",
          "number": 2,
          "type": "multiple_choice",
          "instruction_ja": "正しいものを選びましょう。",
          "instruction_en": "Choose the correct reading or kanji.",
          "items": [
            {
              "id": "k_ex_16_2_1",
              "number": 1,
              "question_ja": "<ruby>駅<rt>えき</rt></ruby>の<u>方角</u>から、<ruby>大<rt>おお</rt></ruby>きい<ruby>音<rt>おと</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえる。",
              "target": "方角",
              "options": ["ほうこう", "ほうかく", "ほうがく"],
              "correct_index": 2,
              "answer": "ほうがく",
              "ruby_html": "<ruby>駅<rt>えき</rt></ruby>の<ruby>方角<rt>ほうがく</rt></ruby>から、<ruby>大<rt>おお</rt></ruby>きい<ruby>音<rt>おと</rt></ruby>が<ruby>聞<rt>き</rt></ruby>こえる。",
              "translation": "A loud sound can be heard from the direction of the station.",
              "explanation": "方角（ほうがく）は「角（かく）」が連濁して「がく」になります。"
            },
            {
              "id": "k_ex_16_2_2",
              "number": 2,
              "question_ja": "ただいま、<u>電波</u>が<ruby>届<rt>とど</rt></ruby>かない<ruby>所<rt>ところ</rt></ruby>にいます。",
              "target": "電波",
              "options": ["でんぱ", "でんば", "でんは"],
              "correct_index": 0,
              "answer": "でんぱ",
              "ruby_html": "ただいま、<ruby>電波<rt>でんぱ</rt></ruby>が<ruby>届<rt>とど</rt></ruby>かない<ruby>所<rt>ところ</rt></ruby>にいます。",
              "translation": "Right now I am in a place where radio signals cannot reach.",
              "explanation": "電波（でんぱ）は「波（は）」が半濁音化して「ぱ」になります。"
            },
            {
              "id": "k_ex_16_2_3",
              "number": 3,
              "question_ja": "<ruby>車<rt>くるま</rt></ruby>で<ruby>送<rt>おく</rt></ruby>ってくれるというのを<u>断った</u>。",
              "target": "断った",
              "options": ["こどわった", "ことわった", "こわとった"],
              "correct_index": 1,
              "answer": "ことわった",
              "ruby_html": "<ruby>車<rt>くるま</rt></ruby>で<ruby>送<rt>おく</rt></ruby>ってくれるというのを<ruby>断<rt>ことわ</rt></ruby>った。",
              "translation": "I declined their offer to drive me.",
              "explanation": "断る（ことわる）の過去形は「断った（ことわった）」です。"
            },
            {
              "id": "k_ex_16_2_4",
              "number": 4,
              "question_ja": "<ruby>車<rt>くるま</rt></ruby>で<u>半島</u>のいちばん<ruby>先<rt>さき</rt></ruby>まで<ruby>行<rt>い</rt></ruby>こう。",
              "target": "半島",
              "options": ["はんど", "はんどう", "はんとう"],
              "correct_index": 2,
              "answer": "はんとう",
              "ruby_html": "<ruby>車<rt>くるま</rt></ruby>で<ruby>半島<rt>はんとう</rt></ruby>のいちばん<ruby>先<rt>さき</rt></ruby>まで<ruby>行<rt>い</rt></ruby>こう。",
              "translation": "Let's go by car to the very tip of the peninsula.",
              "explanation": "半島（はんとう）は海に突き出た陸地を表します。"
            },
            {
              "id": "k_ex_16_2_5",
              "number": 5,
              "question_ja": "どうぞ、<u>おすわり</u>ください。",
              "target": "おすわり",
              "options": ["お席り", "お座り", "お着り"],
              "correct_index": 1,
              "answer": "お座り",
              "ruby_html": "どうぞ、お<ruby>座<rt>すわ</rt></ruby>りください。",
              "translation": "Please have a seat.",
              "explanation": "座る（すわる）の連用形「お座り（おすわり）」です。"
            },
            {
              "id": "k_ex_16_2_6",
              "number": 6,
              "question_ja": "<u>れんらく</u>したいことがあるので、<ruby>電話<rt>でんわ</rt></ruby>をください。",
              "target": "れんらく",
              "options": ["連洛", "連酪", "連絡"],
              "correct_index": 2,
              "answer": "連絡",
              "ruby_html": "<ruby>連絡<rt>れんらく</rt></ruby>したいことがあるので、<ruby>電話<rt>でんわ</rt></ruby>をください。",
              "translation": "There is something I want to contact you about, so please call me.",
              "explanation": "連絡（れんらく）の「絡」は糸へん（いとへん）です。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_16_3",
          "number": 3,
          "type": "word_pairing",
          "instruction_ja": "□には同じ漢字が入ります。［向・遊・横・置］から漢字を選んで書きましょう。＿＿の部分の読み方も書きましょう。",
          "instruction_en": "The same kanji goes in each pair of boxes. Choose from [向, 遊, 横, 置] and write the readings.",
          "choices": ["向", "遊", "横", "置"],
          "items": [
            {
              "id": "k_ex_16_3_1",
              "number": 1,
              "shared_kanji": "置",
              "sentence_a": "<ruby>彼女<rt>かのじょ</rt></ruby>は、レストランの<ruby>入<rt>い</rt></ruby>り<ruby>口<rt>ぐち</rt></ruby>からすぐ<ruby>見<rt>み</rt></ruby>える a【位□】に<ruby>座<rt>すわ</rt></ruby>っていた。",
              "sentence_b": "<ruby>座席<rt>ざせき</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>荷物<rt>にもつ</rt></ruby>を b【□かないで】ください。",
              "answer": "置",
              "reading_a": "いち",
              "word_a": "位置",
              "reading_b": "おかないで",
              "word_b": "置かないで",
              "ruby_html": "<ruby>彼女<rt>かのじょ</rt></ruby>は、レストランの<ruby>入<rt>い</rt></ruby>り<ruby>口<rt>ぐち</rt></ruby>からすぐ<ruby>見<rt>み</rt></ruby>える<ruby>位置<rt>いち</rt></ruby>に<ruby>座<rt>すわ</rt></ruby>っていた。 / <ruby>座席<rt>ざせき</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>置<rt>お</rt></ruby>かないでください。",
              "translation": "She was sitting in a position easily visible from the restaurant entrance. / Please do not place baggage under your seat.",
              "explanation": "置：音読み「チ」（位置：いち）、訓読み「お（く）」（置かないで：おかないで）。"
            },
            {
              "id": "k_ex_16_3_2",
              "number": 2,
              "shared_kanji": "横",
              "sentence_a": "<ruby>信号<rt>しんごう</rt></ruby>がない<ruby>道<rt>みち</rt></ruby>を a【□断】するときは、<ruby>注意<rt>ちゅうい</rt></ruby>しよう。",
              "sentence_b": "<ruby>駅<rt>えき</rt></ruby>の b【□】にバスの<ruby>案内所<rt>あんないじょ</rt></ruby>がある。",
              "answer": "横",
              "reading_a": "おうだん",
              "word_a": "横断",
              "reading_b": "よこ",
              "word_b": "横",
              "ruby_html": "<ruby>信号<rt>しんごう</rt></ruby>がない<ruby>道<rt>みち</rt></ruby>を<ruby>横断<rt>おうだん</rt></ruby>するときは、<ruby>注意<rt>ちゅうい</rt></ruby>しよう。 / <ruby>駅<rt>えき</rt></ruby>の<ruby>横<rt>よこ</rt></ruby>にバスの<ruby>案内所<rt>あんないじょ</rt></ruby>がある。",
              "translation": "Let's be careful when crossing a road without a traffic light. / There is a bus information booth beside the station.",
              "explanation": "横：音読み「オウ」（横断：おうだん）、訓読み「よこ」（横：よこ）。"
            },
            {
              "id": "k_ex_16_3_3",
              "number": 3,
              "shared_kanji": "向",
              "sentence_a": "<ruby>間違<rt>まちが</rt></ruby>って、<ruby>行<rt>い</rt></ruby>きたい<ruby>所<rt>ところ</rt></ruby>と<ruby>反対<rt>はんたい</rt></ruby>の a【方□】へ<ruby>行<rt>い</rt></ruby>ってしまった。",
              "sentence_b": "この<ruby>車<rt>くるま</rt></ruby>は<ruby>町<rt>まち</rt></ruby>の<ruby>中央<rt>ちゅうおう</rt></ruby>に b【□かっている】。",
              "answer": "向",
              "reading_a": "ほうこう",
              "word_a": "方向",
              "reading_b": "むかっている",
              "word_b": "向かっている",
              "ruby_html": "<ruby>間違<rt>まちが</rt></ruby>って、<ruby>行<rt>い</rt></ruby>きたい<ruby>所<rt>ところ</rt></ruby>と<ruby>反対<rt>はんたい</rt></ruby>の<ruby>方向<rt>ほうこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ってしまった。 / この<ruby>車<rt>くるま</rt></ruby>は<ruby>町<rt>まち</rt></ruby>の<ruby>中央<rt>ちゅうおう</rt></ruby>に<ruby>向<rt>む</rt></ruby>かっている。",
              "translation": "By mistake, I went in the opposite direction of where I wanted to go. / This car is heading toward the center of town.",
              "explanation": "向：音読み「コウ」（方向：ほうこう）、訓読み「む（かう）」（向かっている：むかっている）。"
            },
            {
              "id": "k_ex_16_3_4",
              "number": 4,
              "shared_kanji": "遊",
              "sentence_a": "<ruby>昨日<rt>きのう</rt></ruby>は a【□園地】に<ruby>行<rt>い</rt></ruby>って<ruby>一日中<rt>いちにちじゅう</rt></ruby> b【□んだ】。",
              "sentence_b": "",
              "answer": "遊",
              "reading_a": "ゆうえんち",
              "word_a": "遊園地",
              "reading_b": "あそんだ",
              "word_b": "遊んだ",
              "ruby_html": "<ruby>昨日<rt>きのう</rt></ruby>は<ruby>遊園地<rt>ゆうえんち</rt></ruby>に<ruby>行<rt>い</rt></ruby>って<ruby>一日中<rt>いちにちじゅう</rt></ruby><ruby>遊<rt>あそ</rt></ruby>んだ。",
              "translation": "Yesterday I went to an amusement park and played all day long.",
              "explanation": "遊：音読み「ユウ」（遊園地：ゆうえんち）、訓読み「あそ（ぶ）」（遊んだ：あそんだ）。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_16_4",
          "number": 4,
          "type": "reading_writing",
          "instruction_ja": "＿＿の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
          "instruction_en": "Write the reading for underlined kanji and write kanji for underlined hiragana.",
          "items": [
            {
              "id": "k_ex_16_4_1a",
              "number": 1,
              "sub": "a",
              "mode": "reading",
              "sentence": "<ruby>赤<rt>あか</rt></ruby>や<ruby>黄色<rt>きいろ</rt></ruby>の a【風船】が、<ruby>空<rt>そら</rt></ruby>に<ruby>飛<rt>と</rt></ruby>んでいった。",
              "target": "風船",
              "answer": "ふうせん",
              "reading": "ふうせん",
              "ruby_html": "<ruby>赤<rt>あか</rt></ruby>や<ruby>黄色<rt>きいろ</rt></ruby>の<ruby>風船<rt>ふうせん</rt></ruby>が、<ruby>空<rt>そら</rt></ruby>に<ruby>飛<rt>と</rt></ruby>んでいった。",
              "translation": "Red and yellow balloons flew up into the sky.",
              "explanation": "風船（ふうせん）は空中に浮かぶゴムのおもちゃです。"
            },
            {
              "id": "k_ex_16_4_1b",
              "number": 1,
              "sub": "b",
              "mode": "reading",
              "sentence": "<ruby>赤<rt>あか</rt></ruby>や<ruby>黄色<rt>きいろ</rt></ruby>の<ruby>風船<rt>ふうせん</rt></ruby>が、<ruby>空<rt>そら</rt></ruby>に b【飛んで】いった。",
              "target": "飛んで",
              "answer": "とんで",
              "reading": "とんで",
              "ruby_html": "<ruby>赤<rt>あか</rt></ruby>や<ruby>黄色<rt>きいろ</rt></ruby>の<ruby>風船<rt>ふうせん</rt></ruby>が、<ruby>空<rt>そら</rt></ruby>に<ruby>飛<rt>と</rt></ruby>んでいった。",
              "translation": "Red and yellow balloons flew up into the sky.",
              "explanation": "飛ぶ（とぶ）のテ形は「飛んで（とんで）」です。"
            },
            {
              "id": "k_ex_16_4_2a",
              "number": 2,
              "sub": "a",
              "mode": "reading",
              "sentence": "a【飛行機】では、<ruby>窓側<rt>まどがわ</rt></ruby>の<ruby>座席<rt>ざせき</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶことにしている。",
              "target": "飛行機",
              "answer": "ひこうき",
              "reading": "ひこうき",
              "ruby_html": "<ruby>飛行機<rt>ひこうき</rt></ruby>では、<ruby>窓側<rt>まどがわ</rt></ruby>の<ruby>座席<rt>ざせき</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶことにしている。",
              "translation": "On airplanes, I make a point of choosing a window seat.",
              "explanation": "飛行機（ひこうき）の「飛」は音読み「ヒ」です。"
            },
            {
              "id": "k_ex_16_4_2b",
              "number": 2,
              "sub": "b",
              "mode": "reading",
              "sentence": "<ruby>飛行機<rt>ひこうき</rt></ruby>では、<ruby>窓側<rt>まどがわ</rt></ruby>の b【座席】を<ruby>選<rt>えら</rt></ruby>ぶことにしている。",
              "target": "座席",
              "answer": "ざせき",
              "reading": "ざせき",
              "ruby_html": "<ruby>飛行機<rt>ひこうき</rt></ruby>では、<ruby>窓側<rt>まどがわ</rt></ruby>の<ruby>座席<rt>ざせき</rt></ruby>を<ruby>選<rt>えら</rt></ruby>ぶことにしている。",
              "translation": "On airplanes, I make a point of choosing a window seat.",
              "explanation": "座席（ざせき）は乗り物や劇場の席のことです。"
            },
            {
              "id": "k_ex_16_4_3",
              "number": 3,
              "mode": "reading",
              "sentence": "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>旅行<rt>りょこう</rt></ruby>のお<ruby>土産<rt>みやげ</rt></ruby>を【差し上げた】。",
              "target": "差し上げた",
              "answer": "さしあげた",
              "reading": "さしあげた",
              "ruby_html": "<ruby>先生<rt>せんせい</rt></ruby>に<ruby>旅行<rt>りょこう</rt></ruby>のお<ruby>土産<rt>みやげ</rt></ruby>を<ruby>差<rt>さ</rt></ruby>し<ruby>上<rt>あ</rt></ruby>げた。",
              "translation": "I gave the teacher a souvenir from my trip.",
              "explanation": "差し上げる（さしあげる）は「あげる」の謙譲語です。"
            },
            {
              "id": "k_ex_16_4_4",
              "number": 4,
              "mode": "reading",
              "sentence": "その【四角い】<ruby>箱<rt>はこ</rt></ruby>に、おもちゃの<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>入<rt>はい</rt></ruby>っている。",
              "target": "四角い",
              "answer": "しかくい",
              "reading": "しかくい",
              "ruby_html": "その<ruby>四角<rt>しかく</rt></ruby>い<ruby>箱<rt>はこ</rt></ruby>に、おもちゃの<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>入<rt>はい</rt></ruby>っている。",
              "translation": "There is a toy train inside that square box.",
              "explanation": "四角い（しかくい）は形容詞として使われます。"
            },
            {
              "id": "k_ex_16_4_5a",
              "number": 5,
              "sub": "a",
              "mode": "reading",
              "sentence": "<ruby>今日<rt>きょう</rt></ruby>は a【波】が<ruby>高<rt>たか</rt></ruby>いので、<ruby>水泳<rt>すいえい</rt></ruby>はできません。",
              "target": "波",
              "answer": "なみ",
              "reading": "なみ",
              "ruby_html": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>波<rt>なみ</rt></ruby>が<ruby>高<rt>たか</rt></ruby>いので、<ruby>水泳<rt>すいえい</rt></ruby>はできません。",
              "translation": "Since the waves are high today, swimming is not allowed.",
              "explanation": "波（なみ）は訓読みです。"
            },
            {
              "id": "k_ex_16_4_5b",
              "number": 5,
              "sub": "b",
              "mode": "kanji_write",
              "sentence": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>波<rt>なみ</rt></ruby>が<ruby>高<rt>たか</rt></ruby>いので、b【すいえい】はできません。",
              "target": "すいえい",
              "answer": "水泳",
              "reading": "すいえい",
              "ruby_html": "<ruby>今日<rt>きょう</rt></ruby>は<ruby>波<rt>なみ</rt></ruby>が<ruby>高<rt>たか</rt></ruby>いので、<ruby>水泳<rt>すいえい</rt></ruby>はできません。",
              "translation": "Since the waves are high today, swimming is not allowed.",
              "explanation": "水泳（すいえい）の「泳」は音読み「エイ」です。"
            },
            {
              "id": "k_ex_16_4_6",
              "number": 6,
              "mode": "kanji_write",
              "sentence": "<ruby>急行電車<rt>きゅうこうでんしゃ</rt></ruby>が<ruby>駅<rt>えき</rt></ruby>を【つうか】した。",
              "target": "つうか",
              "answer": "通過",
              "reading": "つうか",
              "ruby_html": "<ruby>急行電車<rt>きゅうこうでんしゃ</rt></ruby>が<ruby>駅<rt>えき</rt></ruby>を<ruby>通過<rt>つうか</rt></ruby>した。",
              "translation": "The express train passed through the station without stopping.",
              "explanation": "通過（つうか）は止まらずに通り過ぎることです。"
            },
            {
              "id": "k_ex_16_4_7a",
              "number": 7,
              "sub": "a",
              "mode": "kanji_write",
              "sentence": "<ruby>病院<rt>びょういん</rt></ruby>は、<ruby>次<rt>つぎ</rt></ruby>の a【かど】を<ruby>右<rt>みぎ</rt></ruby>に<ruby>曲<rt>ま</rt></ruby>がって<ruby>最初<rt>さいしょ</rt></ruby>の<ruby>交差点<rt>こうさてん</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>ると、すぐです。",
              "target": "かど",
              "answer": "角",
              "reading": "かど",
              "ruby_html": "<ruby>病院<rt>びょういん</rt></ruby>は、<ruby>次<rt>つぎ</rt></ruby>の<ruby>角<rt>かど</rt></ruby>を<ruby>右<rt>みぎ</rt></ruby>に<ruby>曲<rt>ま</rt></ruby>がって<ruby>最初<rt>さいしょ</rt></ruby>の<ruby>交差点<rt>こうさてん</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>ると、すぐです。",
              "translation": "Turn right at the next corner and cross the first intersection, and the hospital is right there.",
              "explanation": "道の曲がり角は「角（かど）」と書きます。"
            },
            {
              "id": "k_ex_16_4_7b",
              "number": 7,
              "sub": "b",
              "mode": "kanji_write",
              "sentence": "<ruby>病院<rt>びょういん</rt></ruby>は、<ruby>次<rt>つぎ</rt></ruby>の<ruby>角<rt>かど</rt></ruby>を<ruby>右<rt>みぎ</rt></ruby>に<ruby>曲<rt>ま</rt></ruby>がって<ruby>最初<rt>さいしょ</rt></ruby>の b【こうさてん】を<ruby>渡<rt>わた</rt></ruby>ると、すぐです。",
              "target": "こうさてん",
              "answer": "交差点",
              "reading": "こうさてん",
              "ruby_html": "<ruby>病院<rt>びょういん</rt></ruby>は、<ruby>次<rt>つぎ</rt></ruby>の<ruby>角<rt>かど</rt></ruby>を<ruby>右<rt>みぎ</rt></ruby>に<ruby>曲<rt>ま</rt></ruby>がって<ruby>最初<rt>さいしょ</rt></ruby>の<ruby>交差点<rt>こうさてん</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>ると、すぐです。",
              "translation": "Turn right at the next corner and cross the first intersection, and the hospital is right there.",
              "explanation": "交差点（こうさてん）の「差（さ）」は交わるという意味で使われます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_16_5",
          "number": 5,
          "type": "passage_completion",
          "instruction_ja": "□の中から漢字を選んで、文を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Choose kanji from the box to complete the tourism passage and write their readings.",
          "items": [
            {
              "id": "k_ex_16_5_a",
              "label": "a",
              "choices": ["島", "方", "登"],
              "sentence": "ぽこぽこ<ruby>山<rt>やま</rt></ruby>は a【半□】の<ruby>先<rt>さき</rt></ruby>にあります。",
              "answer": "島",
              "word": "半島",
              "reading": "はんとう",
              "ruby_html": "ぽこぽこ<ruby>山<rt>やま</rt></ruby>は<ruby>半島<rt>はんとう</rt></ruby>の<ruby>先<rt>さき</rt></ruby>にあります。",
              "translation": "Mt. Pokopoko is located at the tip of the peninsula.",
              "explanation": "半島（はんとう）は海に突き出た陸地です。"
            },
            {
              "id": "k_ex_16_5_b",
              "label": "b",
              "choices": ["島", "方", "登"],
              "sentence": "<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つと、<ruby>東<rt>ひがし</rt></ruby>の b【□角】に<ruby>五<rt>いつ</rt></ruby>つの<ruby>島<rt>しま</rt></ruby>がよく<ruby>見<rt>み</rt></ruby>えます。",
              "answer": "方",
              "word": "方角",
              "reading": "ほうがく",
              "ruby_html": "<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つと、<ruby>東<rt>ひがし</rt></ruby>の<ruby>方角<rt>ほうがく</rt></ruby>に<ruby>五<rt>いつ</rt></ruby>つの<ruby>島<rt>しま</rt></ruby>がよく<ruby>見<rt>み</rt></ruby>えます。",
              "translation": "When you stand on top of the mountain, five islands are clearly visible in the eastern direction.",
              "explanation": "方角（ほうがく）は東西南北などの向きのことです。"
            },
            {
              "id": "k_ex_16_5_c",
              "label": "c",
              "choices": ["島", "方", "登"],
              "sentence": "<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つと、<ruby>東<rt>ひがし</rt></ruby>の<ruby>方角<rt>ほうがく</rt></ruby>に<ruby>五<rt>いつ</rt></ruby>つの c【□】がよく<ruby>見<rt>み</rt></ruby>えます。",
              "answer": "島",
              "word": "島",
              "reading": "しま",
              "ruby_html": "<ruby>山<rt>やま</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>立<rt>た</rt></ruby>つと、<ruby>東<rt>ひがし</rt></ruby>の<ruby>方角<rt>ほうがく</rt></ruby>に<ruby>五<rt>いつ</rt></ruby>つの<ruby>島<rt>しま</rt></ruby>がよく<ruby>見<rt>み</rt></ruby>えます。",
              "translation": "When you stand on top of the mountain, five islands are clearly visible in the eastern direction.",
              "explanation": "島（しま）は訓読みです。"
            },
            {
              "id": "k_ex_16_5_d",
              "label": "d",
              "choices": ["島", "方", "登"],
              "sentence": "ぽこぽこ<ruby>山<rt>やま</rt></ruby>に d【□山】するには、<ruby>南側<rt>みなみがわ</rt></ruby>の<ruby>道<rt>みち</rt></ruby>がお<ruby>薦<rt>すす</rt></ruby>めです。",
              "answer": "登",
              "word": "登山",
              "reading": "とざん",
              "ruby_html": "ぽこぽこ<ruby>山<rt>やま</rt></ruby>に<ruby>登山<rt>とざん</rt></ruby>するには、<ruby>南側<rt>みなみがわ</rt></ruby>の<ruby>道<rt>みち</rt></ruby>がお<ruby>薦<rt>すす</rt></ruby>めです。",
              "translation": "To climb Mt. Pokopoko, the southern trail is recommended.",
              "explanation": "登山（とざん）は山に登ることです。"
            },
            {
              "id": "k_ex_16_5_e",
              "label": "e",
              "choices": ["術", "船", "火", "過"],
              "sentence": "ぽこぽこ<ruby>山<rt>やま</rt></ruby>は<ruby>昔<rt>むかし</rt></ruby>、e【□山】でした。<ruby>近<rt>ちか</rt></ruby>くの<ruby>湖<rt>みずうみ</rt></ruby>は、その<ruby>影響<rt>えいきょう</rt></ruby>でできたものです。",
              "answer": "火",
              "word": "火山",
              "reading": "かざん",
              "ruby_html": "ぽこぽこ<ruby>山<rt>やま</rt></ruby>は<ruby>昔<rt>むかし</rt></ruby>、<ruby>火山<rt>かざん</rt></ruby>でした。<ruby>近<rt>ちか</rt></ruby>くの<ruby>湖<rt>みずうみ</rt></ruby>は、その<ruby>影響<rt>えいきょう</rt></ruby>でできたものです。",
              "translation": "Mt. Pokopoko was a volcano in the past. The nearby lake was formed under its influence.",
              "explanation": "火山（かざん）はマグマなどを噴き出す山です。"
            },
            {
              "id": "k_ex_16_5_f",
              "label": "f",
              "choices": ["術", "船", "火", "過"],
              "sentence": "<ruby>観光用<rt>かんこうよう</rt></ruby>の f【□】で、<ruby>湖<rt>みずうみ</rt></ruby>を<ruby>回<rt>まわ</rt></ruby>ることができます。",
              "answer": "船",
              "word": "船",
              "reading": "ふね",
              "ruby_html": "<ruby>観光用<rt>かんこうよう</rt></ruby>の<ruby>船<rt>ふね</rt></ruby>で、<ruby>湖<rt>みずうみ</rt></ruby>を<ruby>回<rt>まわ</rt></ruby>ることができます。",
              "translation": "You can tour around the lake on a sightseeing boat.",
              "explanation": "船（ふね）は訓読みです。"
            },
            {
              "id": "k_ex_16_5_g",
              "label": "g",
              "choices": ["術", "船", "火", "過"],
              "sentence": "すぐそばには、g【美□館】もあって、ゆっくり<ruby>過<rt>す</rt></ruby>ごせる<ruby>人気<rt>にんき</rt></ruby>の<ruby>観光地<rt>かんこうち</rt></ruby>となっています。",
              "answer": "術",
              "word": "美術館",
              "reading": "びじゅつかん",
              "ruby_html": "すぐそばには、<ruby>美術館<rt>びじゅつかん</rt></ruby>もあって、ゆっくり<ruby>過<rt>す</rt></ruby>ごせる<ruby>人気<rt>にんき</rt></ruby>の<ruby>観光地<rt>かんこうち</rt></ruby>となっています。",
              "translation": "Right nearby there is also an art museum, making it a popular sightseeing spot where you can spend time leisurely.",
              "explanation": "美術館（びじゅつかん）は美術品を展示する建物です。"
            },
            {
              "id": "k_ex_16_5_h",
              "label": "h",
              "choices": ["術", "船", "火", "過"],
              "sentence": "すぐそばには、<ruby>美術館<rt>びじゅつかん</rt></ruby>もあって、ゆっくり h【□ごせる】<ruby>人気<rt>にんき</rt></ruby>の<ruby>観光地<rt>かんこうち</rt></ruby>となっています。",
              "answer": "過",
              "word": "過ごせる",
              "reading": "すごせる",
              "ruby_html": "すぐそばには、<ruby>美術館<rt>びじゅつかん</rt></ruby>もあって、ゆっくり<ruby>過<rt>す</rt></ruby>ごせる<ruby>人気<rt>にんき</rt></ruby>の<ruby>観光地<rt>かんこうち</rt></ruby>となっています。",
              "translation": "Right nearby there is also an art museum, making it a popular sightseeing spot where you can spend time leisurely.",
              "explanation": "過ごす（すごす）の可能形「過ごせる（すごせる）」です。"
            }
          ]
        }
      ]
    },
    {
      "lesson_number": 17,
      "title": "第17回 新しく音読みを覚える漢字：動詞 (New Onyomi Kanji: Verbs)",
      "page_range": "74-76",
      "exercises": [
        {
          "exercise_id": "k_ex_17_1",
          "number": 1,
          "type": "reading_recall",
          "instruction_ja": "＿＿の部分の読み方を書きましょう。",
          "instruction_en": "Write the readings for the underlined words (contrasting kunyomi verbs with onyomi compounds).",
          "items": [
            {
              "id": "k_ex_17_1_1a",
              "number": 1,
              "sub": "a",
              "sentence": "ここに<ruby>自転車<rt>じてんしゃ</rt></ruby>を a【止める】のは、<ruby>禁止<rt>きんし</rt></ruby>です。",
              "target": "止める",
              "answer": "とめる",
              "reading": "とめる",
              "ruby_html": "ここに<ruby>自転車<rt>じてんしゃ</rt></ruby>を<ruby>止<rt>と</rt></ruby>めるのは、<ruby>禁止<rt>きんし</rt></ruby>です。",
              "translation": "Parking bicycles here is prohibited.",
              "explanation": "止める（とめる）は訓読みです。"
            },
            {
              "id": "k_ex_17_1_1b",
              "number": 1,
              "sub": "b",
              "sentence": "ここに<ruby>自転車<rt>じてんしゃ</rt></ruby>を<ruby>止<rt>と</rt></ruby>めるのは、b【禁止】です。",
              "target": "禁止",
              "answer": "きんし",
              "reading": "きんし",
              "ruby_html": "ここに<ruby>自転車<rt>じてんしゃ</rt></ruby>を<ruby>止<rt>と</rt></ruby>めるのは、<ruby>禁止<rt>きんし</rt></ruby>です。",
              "translation": "Parking bicycles here is prohibited.",
              "explanation": "禁止（きんし）の「止」は音読み「シ」です（中止・休止など）。"
            },
            {
              "id": "k_ex_17_1_2a",
              "number": 2,
              "sub": "a",
              "sentence": "<ruby>車<rt>くるま</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ない a【歩道】を<ruby>歩<rt>ある</rt></ruby>きましょう。",
              "target": "歩道",
              "answer": "ほどう",
              "reading": "ほどう",
              "ruby_html": "<ruby>車<rt>くるま</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ない<ruby>歩道<rt>ほどう</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>きましょう。",
              "translation": "Let's walk on the sidewalk where cars don't come.",
              "explanation": "歩道（ほどう）の「歩」は音読み「ホ」です。"
            },
            {
              "id": "k_ex_17_1_2b",
              "number": 2,
              "sub": "b",
              "sentence": "<ruby>車<rt>くるま</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ない<ruby>歩道<rt>ほどう</rt></ruby>を b【歩きましょう】。",
              "target": "歩きましょう",
              "answer": "あるきましょう",
              "reading": "あるきましょう",
              "ruby_html": "<ruby>車<rt>くるま</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ない<ruby>歩道<rt>ほどう</rt></ruby>を<ruby>歩<rt>ある</rt></ruby>きましょう。",
              "translation": "Let's walk on the sidewalk where cars don't come.",
              "explanation": "歩く（あるく）は訓読みです。"
            },
            {
              "id": "k_ex_17_1_3a",
              "number": 3,
              "sub": "a",
              "sentence": "<ruby>早<rt>はや</rt></ruby>く a【洗面所】で<ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>ってきなさい。",
              "target": "洗面所",
              "answer": "せんめんじょ",
              "reading": "せんめんじょ",
              "ruby_html": "<ruby>早<rt>はや</rt></ruby>く<ruby>洗面所<rt>せんめんじょ</rt></ruby>で<ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>ってきなさい。",
              "translation": "Hurry and go wash your hands in the washroom.",
              "explanation": "洗面所（せんめんじょ）の「洗」は音読み「セン」です（洗濯など）。"
            },
            {
              "id": "k_ex_17_1_3b",
              "number": 3,
              "sub": "b",
              "sentence": "<ruby>早<rt>はや</rt></ruby>く<ruby>洗面所<rt>せんめんじょ</rt></ruby>で<ruby>手<rt>て</rt></ruby>を b【洗って】きなさい。",
              "target": "洗って",
              "answer": "あらって",
              "reading": "あらって",
              "ruby_html": "<ruby>早<rt>はや</rt></ruby>く<ruby>洗面所<rt>せんめんじょ</rt></ruby>で<ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>ってきなさい。",
              "translation": "Hurry and go wash your hands in the washroom.",
              "explanation": "洗う（あらう）は訓読みです。"
            },
            {
              "id": "k_ex_17_1_4a",
              "number": 4,
              "sub": "a",
              "sentence": "<ruby>学校<rt>がっこう</rt></ruby>で a【習った】<ruby>漢字<rt>かんじ</rt></ruby>は、<ruby>復習<rt>ふくしゅう</rt></ruby>しておいてください。",
              "target": "習った",
              "answer": "ならった",
              "reading": "ならった",
              "ruby_html": "<ruby>学校<rt>がっこう</rt></ruby>で<ruby>習<rt>なら</rt></ruby>った<ruby>漢字<rt>かんじ</rt></ruby>は、<ruby>復習<rt>ふくしゅう</rt></ruby>しておいてください。",
              "translation": "Please review the kanji you learned at school.",
              "explanation": "習う（ならう）は訓読みです。"
            },
            {
              "id": "k_ex_17_1_4b",
              "number": 4,
              "sub": "b",
              "sentence": "<ruby>学校<rt>がっこう</rt></ruby>で<ruby>習<rt>なら</rt></ruby>った<ruby>漢字<rt>かんじ</rt></ruby>は、b【復習】しておいてください。",
              "target": "復習",
              "answer": "ふくしゅう",
              "reading": "ふくしゅう",
              "ruby_html": "<ruby>学校<rt>がっこう</rt></ruby>で<ruby>習<rt>なら</rt></ruby>った<ruby>漢字<rt>かんじ</rt></ruby>は、<ruby>復習<rt>ふくしゅう</rt></ruby>しておいてください。",
              "translation": "Please review the kanji you learned at school.",
              "explanation": "復習（ふくしゅう）の「習」は音読み「シュウ」です（予習・練習・学習など）。"
            },
            {
              "id": "k_ex_17_1_5a",
              "number": 5,
              "sub": "a",
              "sentence": "カラオケで、<ruby>好<rt>す</rt></ruby>きな a【歌手】の b【歌】を c【歌った】。",
              "target": "歌手",
              "answer": "かしゅ",
              "reading": "かしゅ",
              "ruby_html": "カラオケで、<ruby>好<rt>す</rt></ruby>きな<ruby>歌手<rt>かしゅ</rt></ruby>の<ruby>歌<rt>うた</rt></ruby>を<ruby>歌<rt>うた</rt></ruby>った。",
              "translation": "At karaoke, I sang a song by my favorite singer.",
              "explanation": "歌手（かしゅ）の「歌」は音読み「カ」、訓読みは「うた／うた（う）」です。"
            },
            {
              "id": "k_ex_17_1_5b",
              "number": 5,
              "sub": "c",
              "sentence": "カラオケで、<ruby>好<rt>す</rt></ruby>きな<ruby>歌手<rt>かしゅ</rt></ruby>の<ruby>歌<rt>うた</rt></ruby>を c【歌った】。",
              "target": "歌った",
              "answer": "うたった",
              "reading": "うたった",
              "ruby_html": "カラオケで、<ruby>好<rt>す</rt></ruby>きな<ruby>歌手<rt>かしゅ</rt></ruby>の<ruby>歌<rt>うた</rt></ruby>を<ruby>歌<rt>うた</rt></ruby>った。",
              "translation": "At karaoke, I sang a song by my favorite singer.",
              "explanation": "歌う（うたう）のタ形「歌った（うたった）」です。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_17_2",
          "number": 2,
          "type": "multiple_choice",
          "instruction_ja": "正しいものを選びましょう。",
          "instruction_en": "Choose the correct reading or kanji.",
          "items": [
            {
              "id": "k_ex_17_2_1",
              "number": 1,
              "question_ja": "<ruby>今日<rt>きょう</rt></ruby>、<ruby>人気<rt>にんき</rt></ruby>の<ruby>雑誌<rt>ざっし</rt></ruby>が<u>発売</u>される。",
              "target": "発売",
              "options": ["はんばい", "はっぱい", "はつばい"],
              "correct_index": 2,
              "answer": "はつばい",
              "ruby_html": "<ruby>今日<rt>きょう</rt></ruby>、<ruby>人気<rt>にんき</rt></ruby>の<ruby>雑誌<rt>ざっし</rt></ruby>が<ruby>発売<rt>はつばい</rt></ruby>される。",
              "translation": "Today, a popular magazine goes on sale.",
              "explanation": "発売（はつばい）の「売」は音読み「バイ」です。"
            },
            {
              "id": "k_ex_17_2_2",
              "number": 2,
              "question_ja": "<u>寝室</u>に、<ruby>大<rt>おお</rt></ruby>きなベッドが<ruby>置<rt>お</rt></ruby>いてある。",
              "target": "寝室",
              "options": ["しんしつ", "しうしつ", "しゅうしつ"],
              "correct_index": 0,
              "answer": "しんしつ",
              "ruby_html": "<ruby>寝室<rt>しんしつ</rt></ruby>に、<ruby>大<rt>おお</rt></ruby>きなベッドが<ruby>置<rt>お</rt></ruby>いてある。",
              "translation": "A large bed is placed in the bedroom.",
              "explanation": "寝室（しんしつ）の「寝」は音読み「シン」です。"
            },
            {
              "id": "k_ex_17_2_3",
              "number": 3,
              "question_ja": "<ruby>看護師<rt>かんごし</rt></ruby>になるために、<ruby>病院<rt>びょういん</rt></ruby>で<u>実習</u>をした。",
              "target": "実習",
              "options": ["じっしう", "じっしゅう", "じつしゅう"],
              "correct_index": 1,
              "answer": "じっしゅう",
              "ruby_html": "<ruby>看護師<rt>かんごし</rt></ruby>になるために、<ruby>病院<rt>びょういん</rt></ruby>で<ruby>実習<rt>じっしゅう</rt></ruby>をした。",
              "translation": "In order to become a nurse, I did practical training at a hospital.",
              "explanation": "実習（じっしゅう）は「実（じつ）＋習（しゅう）」が促音化して「じっしゅう」となります。"
            },
            {
              "id": "k_ex_17_2_4",
              "number": 4,
              "question_ja": "ただ<ruby>今<rt>いま</rt></ruby>から、<ruby>第<rt>だい</rt></ruby>33<ruby>回<rt>かい</rt></ruby><ruby>全国大会<rt>ぜんこくたいかい</rt></ruby>を<u>かいかい</u>いたします。",
              "target": "かいかい",
              "options": ["開会", "会開", "閉会"],
              "correct_index": 0,
              "answer": "開会",
              "ruby_html": "ただ<ruby>今<rt>いま</rt></ruby>から、<ruby>第<rt>だい</rt></ruby>33<ruby>回<rt>かい</rt></ruby><ruby>全国大会<rt>ぜんこくたいかい</rt></ruby>を<ruby>開会<rt>かいかい</rt></ruby>いたします。",
              "translation": "We now declare the 33rd National Tournament open.",
              "explanation": "会を開くことは「開会（かいかい）」と書きます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_17_3",
          "number": 3,
          "type": "synonym_completion",
          "instruction_ja": "二つの言葉がだいたい同じ意味になるように、［読・始・集・進］の中の漢字を使って、言葉を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Complete the pairs of words with similar meanings using kanji from [読, 始, 集, 進] and write their readings.",
          "choices": ["読", "始", "集", "進"],
          "items": [
            {
              "id": "k_ex_17_3_1",
              "number": 1,
              "shared_kanji": "集",
              "sentence_a": "グラウンドに a【□まる】",
              "sentence_b": "グラウンドに b【□合】する",
              "answer": "集",
              "reading_a": "あつまる",
              "word_a": "集まる",
              "reading_b": "しゅうごう",
              "word_b": "集合",
              "ruby_html": "グラウンドに<ruby>集<rt>あつ</rt></ruby>まる ＝ グラウンドに<ruby>集合<rt>しゅうごう</rt></ruby>する",
              "translation": "gather at the sports ground = assemble at the sports ground",
              "explanation": "集まる（あつまる）＝集合（しゅうごう）する。音読みは「シュウ」です。"
            },
            {
              "id": "k_ex_17_3_2",
              "number": 2,
              "shared_kanji": "進",
              "sentence_a": "<ruby>技術<rt>ぎじゅつ</rt></ruby>が a【□む】",
              "sentence_b": "<ruby>技術<rt>ぎじゅつ</rt></ruby>が b【□歩】する",
              "answer": "進",
              "reading_a": "すすむ",
              "word_a": "進む",
              "reading_b": "しんぽ",
              "word_b": "進歩",
              "ruby_html": "<ruby>技術<rt>ぎじゅつ</rt></ruby>が<ruby>進<rt>すす</rt></ruby>む ＝ <ruby>技術<rt>ぎじゅつ</rt></ruby>が<ruby>進歩<rt>しんぽ</rt></ruby>する",
              "translation": "technology advances = technology makes progress",
              "explanation": "進む（すすむ）＝進歩（しんぽ）する。音読みは「シン」です。"
            },
            {
              "id": "k_ex_17_3_3",
              "number": 3,
              "shared_kanji": "始",
              "sentence_a": "<ruby>試験<rt>しけん</rt></ruby>を a【□める】",
              "sentence_b": "<ruby>試験<rt>しけん</rt></ruby>を b【開□】する",
              "answer": "始",
              "reading_a": "はじめる",
              "word_a": "始める",
              "reading_b": "かいし",
              "word_b": "開始",
              "ruby_html": "<ruby>試験<rt>しけん</rt></ruby>を<ruby>始<rt>はじ</rt></ruby>める ＝ <ruby>試験<rt>しけん</rt></ruby>を<ruby>開始<rt>かいし</rt></ruby>する",
              "translation": "start the exam = commence the exam",
              "explanation": "始める（はじめる）＝開始（かいし）する。音読みは「シ」です。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_17_4",
          "number": 4,
          "type": "word_pairing",
          "instruction_ja": "□には同じ漢字が入ります。［考・思・売・帰］から漢字を選んで書きましょう。＿＿の部分の読み方も書きましょう。",
          "instruction_en": "Fill in the same kanji in both boxes from [考, 思, 売, 帰] and write the readings.",
          "choices": ["考", "思", "売", "帰"],
          "items": [
            {
              "id": "k_ex_17_4_1",
              "number": 1,
              "shared_kanji": "売",
              "sentence_a": "<ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>駅<rt>えき</rt></ruby>の a【□店】で<ruby>新聞<rt>しんぶん</rt></ruby>を<ruby>買<rt>か</rt></ruby>う。",
              "sentence_b": "この<ruby>店<rt>みせ</rt></ruby>は、<ruby>地方<rt>ちほう</rt></ruby>の<ruby>珍<rt>めずら</rt></ruby>しい<ruby>物<rt>もの</rt></ruby>を b【□って】いる。",
              "answer": "売",
              "reading_a": "ばいてん",
              "word_a": "売店",
              "reading_b": "うって",
              "word_b": "売って",
              "ruby_html": "<ruby>毎朝<rt>まいあさ</rt></ruby>、<ruby>駅<rt>えき</rt></ruby>の<ruby>売店<rt>ばいてん</rt></ruby>で<ruby>新聞<rt>しんぶん</rt></ruby>を<ruby>買<rt>か</rt></ruby>う。 / この<ruby>店<rt>みせ</rt></ruby>は、<ruby>地方<rt>ちほう</rt></ruby>の<ruby>珍<rt>めずら</rt></ruby>しい<ruby>物<rt>もの</rt></ruby>を<ruby>売<rt>う</rt></ruby>っている。",
              "translation": "Every morning I buy a newspaper at the station kiosk. / This shop sells rare regional goods.",
              "explanation": "売：音読み「バイ」（売店：ばいてん）、訓読み「う（る）」（売って：うって）。"
            },
            {
              "id": "k_ex_17_4_2",
              "number": 2,
              "shared_kanji": "帰",
              "sentence_a": "<ruby>残業<rt>ざんぎょう</rt></ruby>しないときは、7<ruby>時<rt>じ</rt></ruby>には a【□宅】している。",
              "sentence_b": "<ruby>国<rt>くに</rt></ruby>に b【□ったら】、まず<ruby>友達<rt>ともだち</rt></ruby>に<ruby>会<rt>あ</rt></ruby>いたい。",
              "answer": "帰",
              "reading_a": "きたく",
              "word_a": "帰宅",
              "reading_b": "かえったら",
              "word_b": "帰ったら",
              "ruby_html": "<ruby>残業<rt>ざんぎょう</rt></ruby>しないときは、7<ruby>時<rt>じ</rt></ruby>には<ruby>帰宅<rt>きたく</rt></ruby>している。 / <ruby>国<rt>くに</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら、まず<ruby>友達<rt>ともだち</rt></ruby>に<ruby>会<rt>あ</rt></ruby>いたい。",
              "translation": "When I don't work overtime, I am home by 7 o'clock. / When I return to my country, I want to meet my friends first.",
              "explanation": "帰：音読み「キ」（帰宅：きたく・帰国：きこく）、訓読み「かえ（る）」（帰ったら：かえったら）。"
            },
            {
              "id": "k_ex_17_4_3",
              "number": 3,
              "shared_kanji": "考",
              "sentence_a": "みんなの<ruby>意見<rt>いけん</rt></ruby>を a【参□】にして、もう<ruby>一度<rt>いちど</rt></ruby>よく b【□えて】みよう。",
              "sentence_b": "",
              "answer": "考",
              "reading_a": "さんこう",
              "word_a": "参考",
              "reading_b": "かんがえて",
              "word_b": "考えて",
              "ruby_html": "みんなの<ruby>意見<rt>いけん</rt></ruby>を<ruby>参考<rt>さんこう</rt></ruby>にして、もう<ruby>一度<rt>いちど</rt></ruby>よく<ruby>考<rt>かんが</rt></ruby>えてみよう。",
              "translation": "Let's use everyone's opinions as a reference and think it over carefully once more.",
              "explanation": "考：音読み「コウ」（参考：さんこう）、訓読み「かんが（える）」（考えて：かんがえて）。"
            },
            {
              "id": "k_ex_17_4_4",
              "number": 4,
              "shared_kanji": "思",
              "sentence_a": "テレビを<ruby>見<rt>み</rt></ruby>て、<ruby>世界<rt>せかい</rt></ruby>には a【不□議】な<ruby>出来事<rt>できごと</rt></ruby>がたくさんあると b【□った】。",
              "sentence_b": "",
              "answer": "思",
              "reading_a": "ふしぎ",
              "word_a": "不思議",
              "reading_b": "おもった",
              "word_b": "思った",
              "ruby_html": "テレビを<ruby>見<rt>み</rt></ruby>て、<ruby>世界<rt>せかい</rt></ruby>には<ruby>不思議<rt>ふしぎ</rt></ruby>な<ruby>出来事<rt>できごと</rt></ruby>がたくさんあると<ruby>思<rt>おも</rt></ruby>った。",
              "translation": "Watching TV, I thought that there are many mysterious events in the world.",
              "explanation": "思：音読み「シ」（不思議：ふしぎ・意思：いし）、訓読み「おも（う）」（思った：おもった）。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_17_5",
          "number": 5,
          "type": "reading_writing",
          "instruction_ja": "＿＿の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
          "instruction_en": "Write the reading for underlined kanji and write kanji for underlined hiragana.",
          "items": [
            {
              "id": "k_ex_17_5_1",
              "number": 1,
              "mode": "reading",
              "sentence": "2012<ruby>年<rt>ねん</rt></ruby>、ロンドンでオリンピックが【開かれた】。",
              "target": "開かれた",
              "answer": "ひらかれた",
              "reading": "ひらかれた",
              "ruby_html": "2012<ruby>年<rt>ねん</rt></ruby>、ロンドンでオリンピックが<ruby>開<rt>ひら</rt></ruby>かれた。",
              "translation": "In 2012, the Olympics were held in London.",
              "explanation": "大会やイベントが開催されるときは「開く（ひらく）」の受身形「開かれる（ひらかれる）」を使います。"
            },
            {
              "id": "k_ex_17_5_2",
              "number": 2,
              "mode": "reading",
              "sentence": "<ruby>子供<rt>こども</rt></ruby>たちは、うれしそうにプレゼントの<ruby>箱<rt>はこ</rt></ruby>を【開けた】。",
              "target": "開けた",
              "answer": "あけた",
              "reading": "あけた",
              "ruby_html": "<ruby>子供<rt>こども</rt></ruby>たちは、うれしそうにプレゼントの<ruby>箱<rt>はこ</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けた。",
              "translation": "The children happily opened the present boxes.",
              "explanation": "箱やドアなどをあけるときは「開ける（あける）」と読みます。"
            },
            {
              "id": "k_ex_17_5_3a",
              "number": 3,
              "sub": "a",
              "mode": "kanji_write",
              "sentence": "<ruby>面接<rt>めんせつ</rt></ruby>で、a【れんしゅう】したとおりに<ruby>話<rt>はな</rt></ruby>せたので、いい<ruby>結果<rt>けっか</rt></ruby>を<ruby>期待<rt>きたい</rt></ruby>している。",
              "target": "れんしゅう",
              "answer": "練習",
              "reading": "れんしゅう",
              "ruby_html": "<ruby>面接<rt>めんせつ</rt></ruby>で、<ruby>練習<rt>れんしゅう</rt></ruby>したとおりに<ruby>話<rt>はな</rt></ruby>せたので、いい<ruby>結果<rt>けっか</rt></ruby>を<ruby>期待<rt>きたい</rt></ruby>している。",
              "translation": "Since I was able to speak just as I practiced in the interview, I am hoping for a good result.",
              "explanation": "練習（れんしゅう）の「習」は音読み「シュウ」です。"
            },
            {
              "id": "k_ex_17_5_3b",
              "number": 3,
              "sub": "b",
              "mode": "reading",
              "sentence": "<ruby>面接<rt>めんせつ</rt></ruby>で、<ruby>練習<rt>れんしゅう</rt></ruby>したとおりに<ruby>話<rt>はな</rt></ruby>せたので、いい<ruby>結果<rt>けっか</rt></ruby>を b【期待】している。",
              "target": "期待",
              "answer": "きたい",
              "reading": "きたい",
              "ruby_html": "<ruby>面接<rt>めんせつ</rt></ruby>で、<ruby>練習<rt>れんしゅう</rt></ruby>したとおりに<ruby>話<rt>はな</rt></ruby>せたので、いい<ruby>結果<rt>けっか</rt></ruby>を<ruby>期待<rt>きたい</rt></ruby>している。",
              "translation": "Since I was able to speak just as I practiced in the interview, I am hoping for a good result.",
              "explanation": "期待（きたい）の「待」は音読み「タイ」です（招待など）。"
            }
          ]
        }
      ]
    },
    {
      "lesson_number": 18,
      "title": "第18回 新しく音読みを覚える漢字：名詞や形容詞 (New Onyomi Kanji: Nouns & Adjectives)",
      "page_range": "77-78",
      "exercises": [
        {
          "exercise_id": "k_ex_18_1",
          "number": 1,
          "type": "reading_recall",
          "instruction_ja": "＿＿の部分の読み方を書きましょう。",
          "instruction_en": "Write the readings for the underlined words.",
          "items": [
            {
              "id": "k_ex_18_1_1a",
              "number": 1,
              "sub": "a",
              "sentence": "a【海外】に<ruby>行<rt>い</rt></ruby>くとき、<ruby>飛行機<rt>ひこうき</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>からきれいな<ruby>海<rt>うみ</rt></ruby>が<ruby>見<rt>み</rt></ruby>えた。",
              "target": "海外",
              "answer": "かいがい",
              "reading": "かいがい",
              "ruby_html": "<ruby>海外<rt>かいがい</rt></ruby>に<ruby>行<rt>い</rt></ruby>くとき、<ruby>飛行機<rt>ひこうき</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>からきれいな<ruby>海<rt>うみ</rt></ruby>が<ruby>見<rt>み</rt></ruby>えた。",
              "translation": "When going overseas, I could see the beautiful sea from the airplane window.",
              "explanation": "海外（かいがい）の「海」は音読み「カイ」です。"
            },
            {
              "id": "k_ex_18_1_1b",
              "number": 1,
              "sub": "b",
              "sentence": "<ruby>海外<rt>かいがい</rt></ruby>に<ruby>行<rt>い</rt></ruby>くとき、<ruby>飛行機<rt>ひこうき</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>からきれいな b【海】が<ruby>見<rt>み</rt></ruby>えた。",
              "target": "海",
              "answer": "うみ",
              "reading": "うみ",
              "ruby_html": "<ruby>海外<rt>かいがい</rt></ruby>に<ruby>行<rt>い</rt></ruby>くとき、<ruby>飛行機<rt>ひこうき</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>からきれいな<ruby>海<rt>うみ</rt></ruby>が<ruby>見<rt>み</rt></ruby>えた。",
              "translation": "When going overseas, I could see the beautiful sea from the airplane window.",
              "explanation": "海（うみ）は訓読みです。"
            },
            {
              "id": "k_ex_18_1_2a",
              "number": 2,
              "sub": "a",
              "sentence": "a【次】のページに b【目次】があります。",
              "target": "次",
              "answer": "つぎ",
              "reading": "つぎ",
              "ruby_html": "<ruby>次<rt>つぎ</rt></ruby>のページに<ruby>目次<rt>もくじ</rt></ruby>があります。",
              "translation": "There is a table of contents on the next page.",
              "explanation": "次（つぎ）は訓読み、目次（もくじ）の「次」は音読み「ジ」です。"
            },
            {
              "id": "k_ex_18_1_2b",
              "number": 2,
              "sub": "b",
              "sentence": "<ruby>次<rt>つぎ</rt></ruby>のページに b【目次】があります。",
              "target": "目次",
              "answer": "もくじ",
              "reading": "もくじ",
              "ruby_html": "<ruby>次<rt>つぎ</rt></ruby>のページに<ruby>目次<rt>もくじ</rt></ruby>があります。",
              "translation": "There is a table of contents on the next page.",
              "explanation": "目次（もくじ）は本の章や項目を並べた一覧です。"
            },
            {
              "id": "k_ex_18_1_3a",
              "number": 3,
              "sub": "a",
              "sentence": "a【父母】から<ruby>来<rt>き</rt></ruby>た<ruby>手紙<rt>てがみ</rt></ruby>によると、b【父】も c【母】も<ruby>元気<rt>げんき</rt></ruby>なようだ。",
              "target": "父母",
              "answer": "ふぼ",
              "reading": "ふぼ",
              "ruby_html": "<ruby>父母<rt>ふぼ</rt></ruby>から<ruby>来<rt>き</rt></ruby>た<ruby>手紙<rt>てがみ</rt></ruby>によると、<ruby>父<rt>ちち</rt></ruby>も<ruby>母<rt>はは</rt></ruby>も<ruby>元気<rt>げんき</rt></ruby>なようだ。",
              "translation": "According to the letter from my parents, both my father and mother seem to be doing well.",
              "explanation": "父母（ふぼ）は音読み（父＝フ、母＝ボ）、単独では父（ちち）・母（はは）と読みます。"
            },
            {
              "id": "k_ex_18_1_4a",
              "number": 4,
              "sub": "a",
              "sentence": "a【朝】<ruby>早<rt>はや</rt></ruby>く b【朝食】を<ruby>食<rt>た</rt></ruby>べたので、おなかがすいてしまった。",
              "target": "朝",
              "answer": "あさ",
              "reading": "あさ",
              "ruby_html": "<ruby>朝<rt>あさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>朝食<rt>ちょうしょく</rt></ruby>を<ruby>食<rt>た</rt></ruby>べたので、おなかがすいてしまった。",
              "translation": "Because I ate breakfast early in the morning, I got hungry.",
              "explanation": "朝（あさ）は訓読みです。"
            },
            {
              "id": "k_ex_18_1_4b",
              "number": 4,
              "sub": "b",
              "sentence": "<ruby>朝<rt>あさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く b【朝食】を<ruby>食<rt>た</rt></ruby>べたので、おなかがすいてしまった。",
              "target": "朝食",
              "answer": "ちょうしょく",
              "reading": "ちょうしょく",
              "ruby_html": "<ruby>朝<rt>あさ</rt></ruby><ruby>早<rt>はや</rt></ruby>く<ruby>朝食<rt>ちょうしょく</rt></ruby>を<ruby>食<rt>た</rt></ruby>べたので、おなかがすいてしまった。",
              "translation": "Because I ate breakfast early in the morning, I got hungry.",
              "explanation": "朝食（ちょうしょく）の「朝」は音読み「チョウ」です。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_18_2",
          "number": 2,
          "type": "multiple_choice",
          "instruction_ja": "正しいものを選びましょう。",
          "instruction_en": "Choose the correct reading or kanji.",
          "items": [
            {
              "id": "k_ex_18_2_1",
              "number": 1,
              "question_ja": "<ruby>留学<rt>りゅうがく</rt></ruby>の<u>目的</u>の<ruby>一<rt>ひと</rt></ruby>つは、いろいろな<ruby>経験<rt>けいけん</rt></ruby>をすることだ。",
              "target": "目的",
              "options": ["もっくてき", "もくてき"],
              "correct_index": 1,
              "answer": "もくてき",
              "ruby_html": "<ruby>留学<rt>りゅうがく</rt></ruby>の<ruby>目的<rt>もくてき</rt></ruby>の<ruby>一<rt>ひと</rt></ruby>つは、いろいろな<ruby>経験<rt>けいけん</rt></ruby>をすることだ。",
              "translation": "One of the purposes of studying abroad is to have various experiences.",
              "explanation": "目的（もくてき）の「目」は音読み「モク」です。"
            },
            {
              "id": "k_ex_18_2_2",
              "number": 2,
              "question_ja": "1<ruby>番<rt>ばん</rt></ruby>と2<ruby>番<rt>ばん</rt></ruby>の<ruby>選手<rt>せんしゅ</rt></ruby>が、ほとんど<u>同時</u>にゴールした。",
              "target": "同時",
              "options": ["どうじ", "どんじ"],
              "correct_index": 0,
              "answer": "どうじ",
              "ruby_html": "1<ruby>番<rt>ばん</rt></ruby>と2<ruby>番<rt>ばん</rt></ruby>の<ruby>選手<rt>せんしゅ</rt></ruby>が、ほとんど<ruby>同時<rt>どうじ</rt></ruby>にゴールした。",
              "translation": "The first and second runners crossed the finish line almost simultaneously.",
              "explanation": "同時（どうじ）の「同」は音読み「ドウ」です。"
            },
            {
              "id": "k_ex_18_2_3",
              "number": 3,
              "question_ja": "<ruby>道<rt>みち</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>るとき、<u>左右</u>をよく<ruby>見<rt>み</rt></ruby>てください。",
              "target": "左右",
              "options": ["さゆ", "さゆう", "さう"],
              "correct_index": 1,
              "answer": "さゆう",
              "ruby_html": "<ruby>道<rt>みち</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>るとき、<ruby>左右<rt>さゆう</rt></ruby>をよく<ruby>見<rt>み</rt></ruby>てください。",
              "translation": "When crossing the street, please look carefully left and right.",
              "explanation": "左右（さゆう）は左（サ）と右（ユウ）の熟語です。"
            },
            {
              "id": "k_ex_18_2_4",
              "number": 4,
              "question_ja": "<ruby>日本<rt>にほん</rt></ruby>の<u>しゅと</u>は<ruby>東京<rt>とうきょう</rt></ruby>だ。",
              "target": "しゅと",
              "options": ["主都", "首都"],
              "correct_index": 1,
              "answer": "首都",
              "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>首都<rt>しゅと</rt></ruby>は<ruby>東京<rt>とうきょう</rt></ruby>だ。",
              "translation": "The capital of Japan is Tokyo.",
              "explanation": "国の中心となる都市は「首都（しゅと）」と書きます。"
            },
            {
              "id": "k_ex_18_2_5",
              "number": 5,
              "question_ja": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>全体<rt>ぜんたい</rt></ruby>の66%が<u>しんりん</u>だ。",
              "target": "しんりん",
              "options": ["新林", "深林", "森林"],
              "correct_index": 2,
              "answer": "森林",
              "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>は<ruby>全体<rt>ぜんたい</rt></ruby>の66%が<ruby>森林<rt>しんりん</rt></ruby>だ。",
              "translation": "Sixty-six percent of all of Japan is forest.",
              "explanation": "森林（しんりん）は「森（しん）」と「林（りん）」の組み合わせです。"
            },
            {
              "id": "k_ex_18_2_6",
              "number": 6,
              "question_ja": "<u>ちゅうしょく</u>はもう<ruby>済<rt>す</rt></ruby>みましたか。",
              "target": "ちゅうしょく",
              "options": ["中食", "昼食", "注食"],
              "correct_index": 1,
              "answer": "昼食",
              "ruby_html": "<ruby>昼食<rt>ちゅうしょく</rt></ruby>はもう<ruby>済<rt>す</rt></ruby>みましたか。",
              "translation": "Have you already had lunch?",
              "explanation": "昼の食事は「昼食（ちゅうしょく）」と書きます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_18_3",
          "number": 3,
          "type": "word_pairing",
          "instruction_ja": "□には同じ漢字が入ります。［目・色・低・紙］から漢字を選んで書きましょう。＿＿の部分の読み方も書きましょう。",
          "instruction_en": "Fill in the same kanji in both boxes from [目, 色, 低, 紙] and write the readings.",
          "choices": ["目", "色", "低", "紙"],
          "items": [
            {
              "id": "k_ex_18_3_1",
              "number": 1,
              "shared_kanji": "紙",
              "sentence_a": "アルバムの a【表□】には、<ruby>厚<rt>あつ</rt></ruby>い b【□】が<ruby>使<rt>つか</rt></ruby>われている。",
              "sentence_b": "",
              "answer": "紙",
              "reading_a": "ひょうし",
              "word_a": "表紙",
              "reading_b": "かみ",
              "word_b": "紙",
              "ruby_html": "アルバムの<ruby>表紙<rt>ひょうし</rt></ruby>には、<ruby>厚<rt>あつ</rt></ruby>い<ruby>紙<rt>かみ</rt></ruby>が<ruby>使<rt>つか</rt></ruby>われている。",
              "translation": "Thick paper is used for the cover of the album.",
              "explanation": "紙：音読み「シ」（表紙：ひょうし・用紙：ようし）、訓読み「かみ」。"
            },
            {
              "id": "k_ex_18_3_2",
              "number": 2,
              "shared_kanji": "低",
              "sentence_a": "<ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>するためには、a【最□】70<ruby>点<rt>てん</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>だ。",
              "sentence_b": "<ruby>今朝<rt>けさ</rt></ruby>は<ruby>気温<rt>きおん</rt></ruby>が b【□かった】ので、<ruby>川<rt>かわ</rt></ruby>の<ruby>水<rt>みず</rt></ruby>が<ruby>凍<rt>こお</rt></ruby>っていた。",
              "answer": "低",
              "reading_a": "さいてい",
              "word_a": "最低",
              "reading_b": "ひくかった",
              "word_b": "低かった",
              "ruby_html": "<ruby>試験<rt>しけん</rt></ruby>に<ruby>合格<rt>ごうかく</rt></ruby>するためには、<ruby>最低<rt>さいてい</rt></ruby>70<ruby>点<rt>てん</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby>だ。 / <ruby>今朝<rt>けさ</rt></ruby>は<ruby>気温<rt>きおん</rt></ruby>が<ruby>低<rt>ひく</rt></ruby>かったので、<ruby>川<rt>かわ</rt></ruby>の<ruby>水<rt>みず</rt></ruby>が<ruby>凍<rt>こお</rt></ruby>っていた。",
              "translation": "A minimum of 70 points is required to pass the exam. / Because the temperature was low this morning, the river water was frozen.",
              "explanation": "低：音読み「テイ」（最低：さいてい・低下：ていか）、訓読み「ひく（い）」。"
            },
            {
              "id": "k_ex_18_3_3",
              "number": 3,
              "shared_kanji": "色",
              "sentence_a": "お<ruby>土産<rt>みやげ</rt></ruby>は、その<ruby>地方<rt>ちほう</rt></ruby>の a【特□】が<ruby>出<rt>で</rt></ruby>ていて<ruby>面白<rt>おもしろ</rt></ruby>い。",
              "sentence_b": "この<ruby>動物<rt>どうぶつ</rt></ruby>は、<ruby>周<rt>まわ</rt></ruby>りに<ruby>合<rt>あ</rt></ruby>わせて<ruby>体<rt>からだ</rt></ruby>の b【□】を<ruby>変<rt>か</rt></ruby>えることができる。",
              "answer": "色",
              "reading_a": "とくしょく",
              "word_a": "特色",
              "reading_b": "いろ",
              "word_b": "色",
              "ruby_html": "お<ruby>土産<rt>みやげ</rt></ruby>は、その<ruby>地方<rt>ちほう</rt></ruby>の<ruby>特色<rt>とくしょく</rt></ruby>が<ruby>出<rt>で</rt></ruby>ていて<ruby>面白<rt>おもしろ</rt></ruby>い。 / この<ruby>動物<rt>どうぶつ</rt></ruby>は、<ruby>周<rt>まわ</rt></ruby>りに<ruby>合<rt>あ</rt></ruby>わせて<ruby>体<rt>からだ</rt></ruby>の<ruby>色<rt>いろ</rt></ruby>を<ruby>変<rt>か</rt></ruby>えることができる。",
              "translation": "Souvenirs are interesting because they bring out the special characteristics of that region. / This animal can change its body color to match its surroundings.",
              "explanation": "色：音読み「ショク」（特色：とくしょく）、訓読み「いろ」。"
            },
            {
              "id": "k_ex_18_3_4",
              "number": 4,
              "shared_kanji": "目",
              "sentence_a": "<ruby>英語<rt>えいご</rt></ruby>と<ruby>数学<rt>すうがく</rt></ruby>は、<ruby>私<rt>わたし</rt></ruby>が<ruby>得意<rt>とくい</rt></ruby>な a【科□】です。",
              "sentence_b": "<ruby>今<rt>いま</rt></ruby>、ガスは<ruby>石油<rt>せきゆ</rt></ruby>に<ruby>替<rt>か</rt></ruby>わるエネルギーとして b【注□】されている。",
              "answer": "目",
              "reading_a": "かもく",
              "word_a": "科目",
              "reading_b": "ちゅうもく",
              "word_b": "注目",
              "ruby_html": "<ruby>英語<rt>えいご</rt></ruby>と<ruby>数学<rt>すうがく</rt></ruby>は、<ruby>私<rt>わたし</rt></ruby>が<ruby>得意<rt>とくい</rt></ruby>な<ruby>科目<rt>かもく</rt></ruby>です。 / <ruby>今<rt>いま</rt></ruby>、ガスは<ruby>石油<rt>せきゆ</rt></ruby>に<ruby>替<rt>か</rt></ruby>わるエネルギーとして<ruby>注目<rt>ちゅうもく</rt></ruby>されている。",
              "translation": "English and mathematics are my strong subjects. / Currently, gas is attracting attention as an alternative energy to oil.",
              "explanation": "目：音読み「モク」（科目：かもく・注目：ちゅうもく・目的：もくてき）。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_18_4",
          "number": 4,
          "type": "reading_writing",
          "instruction_ja": "＿＿の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
          "instruction_en": "Write the reading for underlined kanji and write kanji for underlined hiragana.",
          "items": [
            {
              "id": "k_ex_18_4_1",
              "number": 1,
              "mode": "reading",
              "sentence": "<ruby>長女<rt>ちょうじょ</rt></ruby>はしっかりしているが、【次女】はのんびりしている。",
              "target": "次女",
              "answer": "じじょ",
              "reading": "じじょ",
              "ruby_html": "<ruby>長女<rt>ちょうじょ</rt></ruby>はしっかりしているが、<ruby>次女<rt>じじょ</rt></ruby>はのんびりしている。",
              "translation": "The eldest daughter is reliable, whereas the second daughter is easygoing.",
              "explanation": "次女（じじょ）は二番目の娘のことです。"
            },
            {
              "id": "k_ex_18_4_2",
              "number": 2,
              "mode": "reading",
              "sentence": "ずっと<ruby>勉強<rt>べんきょう</rt></ruby>していたら、【首】が<ruby>痛<rt>いた</rt></ruby>くなった。",
              "target": "首",
              "answer": "くび",
              "reading": "くび",
              "ruby_html": "ずっと<ruby>勉強<rt>べんきょう</rt></ruby>していたら、<ruby>首<rt>くび</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>くなった。",
              "translation": "Because I was studying for a long time, my neck started hurting.",
              "explanation": "首（くび）は訓読みです（音読みはシュ：首都・首相）。"
            },
            {
              "id": "k_ex_18_4_3a",
              "number": 3,
              "sub": "a",
              "mode": "reading",
              "sentence": "「パーティーに<ruby>参加<rt>さんか</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>は20<ruby>人<rt>にん</rt></ruby>です」「a【少ない】ですね。もう b【少し】たくさんの<ruby>人<rt>ひと</rt></ruby>が<ruby>参加<rt>さんか</rt></ruby>してくれるといいですね。」",
              "target": "少ない",
              "answer": "すくない",
              "reading": "すくない",
              "ruby_html": "「パーティーに<ruby>参加<rt>さんか</rt></ruby>する<ruby>人<rt>ひと</rt></ruby>は20<ruby>人<rt>にん</rt></ruby>です」「<ruby>少<rt>すく</rt></ruby>ないですね。もう<ruby>少<rt>すこ</rt></ruby>したくさんの<ruby>人<rt>ひと</rt></ruby>が<ruby>参加<rt>さんか</rt></ruby>してくれるといいですね。」",
              "translation": "'There are 20 people joining the party.' 'That's few, isn't it? It would be nice if a few more people joined.'",
              "explanation": "少ない（すくない）と少し（すこし）は送り仮名で読みを区別します。"
            },
            {
              "id": "k_ex_18_4_4",
              "number": 4,
              "mode": "reading",
              "sentence": "<ruby>親切<rt>しんせつ</rt></ruby>な【青年】が、<ruby>私<rt>わたし</rt></ruby>の<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってくれた。",
              "target": "青年",
              "answer": "せいねん",
              "reading": "せいねん",
              "ruby_html": "<ruby>親切<rt>しんせつ</rt></ruby>な<ruby>青年<rt>せいねん</rt></ruby>が、<ruby>私<rt>わたし</rt></ruby>の<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>持<rt>も</rt></ruby>ってくれた。",
              "translation": "A kind young man carried my luggage for me.",
              "explanation": "青年（せいねん）の「青」は音読み「セイ」です。"
            },
            {
              "id": "k_ex_18_4_5a",
              "number": 5,
              "sub": "a",
              "mode": "kanji_write",
              "sentence": "a【もり】で、b【少年】たちがキャンプをしている。",
              "target": "もり",
              "answer": "森",
              "reading": "もり",
              "ruby_html": "<ruby>森<rt>もり</rt></ruby>で、<ruby>少年<rt>しょうねん</rt></ruby>たちがキャンプをしている。",
              "translation": "Boys are camping in the forest.",
              "explanation": "森（もり）は木がたくさん集まった場所です。"
            },
            {
              "id": "k_ex_18_4_5b",
              "number": 5,
              "sub": "b",
              "mode": "reading",
              "sentence": "<ruby>森<rt>もり</rt></ruby>で、b【少年】たちがキャンプをしている。",
              "target": "少年",
              "answer": "しょうねん",
              "reading": "しょうねん",
              "ruby_html": "<ruby>森<rt>もり</rt></ruby>で、<ruby>少年<rt>しょうねん</rt></ruby>たちがキャンプをしている。",
              "translation": "Boys are camping in the forest.",
              "explanation": "少年（しょうねん）の「少」は音読み「ショウ」です。"
            },
            {
              "id": "k_ex_18_4_6",
              "number": 6,
              "mode": "kanji_write",
              "sentence": "【でんち】を2<ruby>本<rt>ほん</rt></ruby><ruby>買<rt>か</rt></ruby>ってきて。",
              "target": "でんち",
              "answer": "電池",
              "reading": "でんち",
              "ruby_html": "<ruby>電池<rt>でんち</rt></ruby>を2<ruby>本<rt>ほん</rt></ruby><ruby>買<rt>か</rt></ruby>ってきて。",
              "translation": "Please go buy two batteries.",
              "explanation": "電池（でんち）の「池（いけ）」は音読み「チ」です。"
            }
          ]
        }
      ]
    },
    {
      "lesson_number": "summary_6",
      "title": "まとめ問題 (6) (Review Quiz 6: Lessons 17-18)",
      "page_range": "79-80",
      "exercises": [
        {
          "exercise_id": "k_ex_matome6_1",
          "number": 1,
          "type": "multiple_choice",
          "instruction_ja": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びましょう。",
          "instruction_en": "Choose the best reading for the underlined word from 1, 2, 3, or 4.",
          "items": [
            {
              "id": "k_ex_matome6_1_1",
              "number": 1,
              "question_ja": "<ruby>田舎<rt>いなか</rt></ruby>から<ruby>都市<rt>とし</rt></ruby>に<ruby>移<rt>うつ</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えて、<ruby>都市<rt>とし</rt></ruby>に<ruby>人口<rt>じんこう</rt></ruby>が<u>集中</u>した。",
              "target": "集中",
              "options": ["しゅうちゅう", "しゅっちゅう", "しゅうじゅう", "しゅじゅう"],
              "correct_index": 0,
              "answer": "しゅうちゅう",
              "ruby_html": "<ruby>田舎<rt>いなか</rt></ruby>から<ruby>都市<rt>とし</rt></ruby>に<ruby>移<rt>うつ</rt></ruby>る<ruby>人<rt>ひと</rt></ruby>が<ruby>増<rt>ふ</rt></ruby>えて、<ruby>都市<rt>とし</rt></ruby>に<ruby>人口<rt>じんこう</rt></ruby>が<ruby>集中<rt>しゅうちゅう</rt></ruby>した。",
              "translation": "More people moved from the countryside to cities, concentrating the population in cities.",
              "explanation": "集中（しゅうちゅう）は一つの場所に集まることです。"
            },
            {
              "id": "k_ex_matome6_1_2",
              "number": 2,
              "question_ja": "<ruby>少<rt>すこ</rt></ruby>しずつだが、<ruby>問題<rt>もんだい</rt></ruby>の<ruby>解決<rt>かいけつ</rt></ruby>に<ruby>向<rt>む</rt></ruby>かって<u>前進</u>している。",
              "target": "前進",
              "options": ["ぜんしん", "せんしん", "ぜんじん", "せんじん"],
              "correct_index": 0,
              "answer": "ぜんしん",
              "ruby_html": "<ruby>少<rt>すこ</rt></ruby>しずつだが、<ruby>問題<rt>もんだい</rt></ruby>の<ruby>解決<rt>かいけつ</rt></ruby>に<ruby>向<rt>む</rt></ruby>かって<ruby>前進<rt>ぜんしん</rt></ruby>している。",
              "translation": "Little by little, we are moving forward toward resolving the problem.",
              "explanation": "前進（ぜんしん）は前へ進むことです。"
            },
            {
              "id": "k_ex_matome6_1_3",
              "number": 3,
              "question_ja": "<ruby>山<rt>やま</rt></ruby>では、<ruby>急<rt>きゅう</rt></ruby>に<ruby>気温<rt>きおん</rt></ruby>が<u>低下</u>することがあるので、<ruby>注意<rt>ちゅうい</rt></ruby>しなければならない。",
              "target": "低下",
              "options": ["てんが", "ていが", "てんげ", "ていか"],
              "correct_index": 3,
              "answer": "ていか",
              "ruby_html": "<ruby>山<rt>やま</rt></ruby>では、<ruby>急<rt>きゅう</rt></ruby>に<ruby>気温<rt>きおん</rt></ruby>が<ruby>低下<rt>ていか</rt></ruby>することがあるので、<ruby>注意<rt>ちゅうい</rt></ruby>しなければならない。",
              "translation": "In the mountains, the temperature can drop suddenly, so one must be careful.",
              "explanation": "低下（ていか）は気温や能力などが低くなることです。"
            },
            {
              "id": "k_ex_matome6_1_4",
              "number": 4,
              "question_ja": "<ruby>彼<rt>かれ</rt></ruby>が<ruby>次<rt>つぎ</rt></ruby>にどんな<ruby>映画<rt>えいが</rt></ruby>を<ruby>作<rt>つく</rt></ruby>るか、<ruby>世界中<rt>せかいじゅう</rt></ruby>が<u>注目</u>している。",
              "target": "注目",
              "options": ["ちゅうぼく", "ちゅうもく", "ちゅまぐ", "ちゅうもぐ"],
              "correct_index": 1,
              "answer": "ちゅうもく",
              "ruby_html": "<ruby>彼<rt>かれ</rt></ruby>が<ruby>次<rt>つぎ</rt></ruby>にどんな<ruby>映画<rt>えいが</rt></ruby>を<ruby>作<rt>つく</rt></ruby>るか、<ruby>世界中<rt>せかいじゅう</rt></ruby>が<ruby>注目<rt>ちゅうもく</rt></ruby>している。",
              "translation": "The whole world is watching closely to see what kind of movie he will make next.",
              "explanation": "注目（ちゅうもく）は関心を持って見守ることです。"
            },
            {
              "id": "k_ex_matome6_1_5",
              "number": 5,
              "question_ja": "スーパーで<ruby>卵<rt>たまご</rt></ruby>の<u>特売</u>をしていた。",
              "target": "特売",
              "options": ["とっくまい", "とぐまい", "とくばい", "とぐばい"],
              "correct_index": 2,
              "answer": "とくばい",
              "ruby_html": "スーパーで<ruby>卵<rt>たまご</rt></ruby>の<ruby>特売<rt>とくばい</rt></ruby>をしていた。",
              "translation": "They were having a special sale on eggs at the supermarket.",
              "explanation": "特売（とくばい）は特別に安く売ることです。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome6_2",
          "number": 2,
          "type": "multiple_choice",
          "instruction_ja": "＿＿の言葉を漢字で書くとき、最もよいものを、1・2・3・4から一つ選びましょう。",
          "instruction_en": "Choose the best kanji representation for the underlined word from 1, 2, 3, or 4.",
          "items": [
            {
              "id": "k_ex_matome6_2_1",
              "number": 1,
              "question_ja": "<ruby>明日<rt>あした</rt></ruby>の<ruby>授業<rt>じゅぎょう</rt></ruby>の<u>よしゅう</u>をしておこう。",
              "target": "よしゅう",
              "options": ["自習", "余習", "用習", "予習"],
              "correct_index": 3,
              "answer": "予習",
              "ruby_html": "<ruby>明日<rt>あした</rt></ruby>の<ruby>授業<rt>じゅぎょう</rt></ruby>の<ruby>予習<rt>よしゅう</rt></ruby>をしておこう。",
              "translation": "Let's prepare in advance for tomorrow's class.",
              "explanation": "授業の前にあらかじめ勉強しておくことは「予習（よしゅう）」です。"
            },
            {
              "id": "k_ex_matome6_2_2",
              "number": 2,
              "question_ja": "<ruby>花火大会<rt>はなびたいかい</rt></ruby>は、<ruby>雨<rt>あめ</rt></ruby>のときは<u>ちゅうし</u>です。",
              "target": "ちゅうし",
              "options": ["注止", "主止", "中止", "休止"],
              "correct_index": 2,
              "answer": "中止",
              "ruby_html": "<ruby>花火大会<rt>はなびたいかい</rt></ruby>は、<ruby>雨<rt>あめ</rt></ruby>のときは<ruby>中止<rt>ちゅうし</rt></ruby>です。",
              "translation": "The fireworks festival will be canceled in case of rain.",
              "explanation": "予定していたことをやめることは「中止（ちゅうし）」です。"
            },
            {
              "id": "k_ex_matome6_2_3",
              "number": 3,
              "question_ja": "<ruby>田中<rt>たなか</rt></ruby>さんは、<u>かいがい</u>で<ruby>生活<rt>せいかつ</rt></ruby>した<ruby>経験<rt>けいけん</rt></ruby>がありますか。",
              "target": "かいがい",
              "options": ["海外", "界外", "海上", "外海"],
              "correct_index": 0,
              "answer": "海外",
              "ruby_html": "<ruby>田中<rt>たなか</rt></ruby>さんは、<ruby>海外<rt>かいがい</rt></ruby>で<ruby>生活<rt>せいかつ</rt></ruby>した<ruby>経験<rt>けいけん</rt></ruby>がありますか。",
              "translation": "Mr. Tanaka, do you have experience living overseas?",
              "explanation": "外国のことは「海外（かいがい）」と書きます。"
            },
            {
              "id": "k_ex_matome6_2_4",
              "number": 4,
              "question_ja": "<ruby>髪<rt>かみ</rt></ruby>が<ruby>長<rt>なが</rt></ruby>い<u>しょうじょ</u>が<ruby>木<rt>き</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>立<rt>た</rt></ruby>っていた。",
              "target": "しょうじょ",
              "options": ["小女", "少女", "子女", "生女"],
              "correct_index": 1,
              "answer": "少女",
              "ruby_html": "<ruby>髪<rt>かみ</rt></ruby>が<ruby>長<rt>なが</rt></ruby>い<ruby>少女<rt>しょうじょ</rt></ruby>が<ruby>木<rt>き</rt></ruby>の<ruby>下<rt>した</rt></ruby>に<ruby>立<rt>た</rt></ruby>っていた。",
              "translation": "A girl with long hair was standing under the tree.",
              "explanation": "女の子どもは「少女（しょうじょ）」と書きます。"
            },
            {
              "id": "k_ex_matome6_2_5",
              "number": 5,
              "question_ja": "キムさん、<u>きこく</u>しても<ruby>日本<rt>にほん</rt></ruby>のことを<ruby>忘<rt>わす</rt></ruby>れないでくださいね。",
              "target": "きこく",
              "options": ["飛国", "来国", "帰国", "行国"],
              "correct_index": 2,
              "answer": "帰国",
              "ruby_html": "キムさん、<ruby>帰国<rt>きこく</rt></ruby>しても<ruby>日本<rt>にほん</rt></ruby>のことを<ruby>忘<rt>わす</rt></ruby>れないでくださいね。",
              "translation": "Kim-san, even after you return to your country, please don't forget about Japan.",
              "explanation": "自分の国へ帰ることは「帰国（きこく）」と書きます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome6_3",
          "number": 3,
          "type": "sentence_completion",
          "instruction_ja": "［集・禁・用・歩・開］から漢字を選んで、文を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Choose a kanji from [集, 禁, 用, 歩, 開] to complete each sentence and write the reading of the compound.",
          "choices": ["集", "禁", "用", "歩", "開"],
          "items": [
            {
              "id": "k_ex_matome6_3_1",
              "number": 1,
              "sentence": "<ruby>雨<rt>あめ</rt></ruby>のために、テニスの<ruby>試合<rt>しあい</rt></ruby>【□始】が30<ruby>分<rt>ぷん</rt></ruby><ruby>遅<rt>おく</rt></ruby>れた。",
              "answer": "開",
              "word": "開始",
              "reading": "かいし",
              "ruby_html": "<ruby>雨<rt>あめ</rt></ruby>のために、テニスの<ruby>試合<rt>しあい</rt></ruby><ruby>開始<rt>かいし</rt></ruby>が30<ruby>分<rt>ぷん</rt></ruby><ruby>遅<rt>おく</rt></ruby>れた。",
              "translation": "Because of rain, the start of the tennis match was delayed by 30 minutes.",
              "explanation": "開始（かいし）＝物事が始まること。"
            },
            {
              "id": "k_ex_matome6_3_2",
              "number": 2,
              "sentence": "あしたは<ruby>遠足<rt>えんそく</rt></ruby>です。【□合】<ruby>時間<rt>じかん</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れないようにしてください。",
              "answer": "集",
              "word": "集合",
              "reading": "しゅうごう",
              "ruby_html": "あしたは<ruby>遠足<rt>えんそく</rt></ruby>です。<ruby>集合<rt>しゅうごう</rt></ruby><ruby>時間<rt>じかん</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れないようにしてください。",
              "translation": "Tomorrow is the excursion. Please make sure not to be late for the assembly time.",
              "explanation": "集合（しゅうごう）＝決まった場所に集まること。"
            },
            {
              "id": "k_ex_matome6_3_3",
              "number": 3,
              "sentence": "<ruby>参加<rt>さんか</rt></ruby>を<ruby>希望<rt>きぼう</rt></ruby>する<ruby>方<rt>かた</rt></ruby>は、この<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>み【□紙】に<ruby>書<rt>か</rt></ruby>いてください。",
              "answer": "用",
              "word": "用紙",
              "reading": "ようし",
              "ruby_html": "<ruby>参加<rt>さんか</rt></ruby>を<ruby>希望<rt>きぼう</rt></ruby>する<ruby>方<rt>かた</rt></ruby>は、この<ruby>申<rt>もう</rt></ruby>し<ruby>込<rt>こ</rt></ruby>み<ruby>用紙<rt>ようし</rt></ruby>に<ruby>書<rt>か</rt></ruby>いてください。",
              "translation": "Those who wish to participate, please fill out this application form.",
              "explanation": "用紙（ようし）＝特定の目的のために使う紙。"
            },
            {
              "id": "k_ex_matome6_3_4",
              "number": 4,
              "sentence": "<ruby>道<rt>みち</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>るときは、<ruby>横断<rt>おうだん</rt></ruby>【□道】を<ruby>渡<rt>わた</rt></ruby>りましょう。",
              "answer": "歩",
              "word": "歩道",
              "reading": "ほどう",
              "ruby_html": "<ruby>道<rt>みち</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>るときは、<ruby>横断歩道<rt>おうだんほどう</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>りましょう。",
              "translation": "When crossing the street, let's cross at the pedestrian crosswalk.",
              "explanation": "横断歩道（おうだんほどう）は歩行者が道路を渡るための場所です。"
            },
            {
              "id": "k_ex_matome6_3_5",
              "number": 5,
              "sentence": "この<ruby>薬<rt>くすり</rt></ruby>は、<ruby>副作用<rt>ふくさよう</rt></ruby>があることが<ruby>分<rt>わ</rt></ruby>かって、<ruby>使用<rt>しよう</rt></ruby>【□止】になりました。",
              "answer": "禁",
              "word": "禁止",
              "reading": "きんし",
              "ruby_html": "この<ruby>薬<rt>くすり</rt></ruby>は、<ruby>副作用<rt>ふくさよう</rt></ruby>があることが<ruby>分<rt>わ</rt></ruby>かって、<ruby>使用禁止<rt>しようきんし</rt></ruby>になりました。",
              "translation": "This medicine was found to have side effects, so its use was banned.",
              "explanation": "禁止（きんし）＝してはいけないと止めること。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome6_4",
          "number": 4,
          "type": "onyomi_grouping",
          "instruction_ja": "音読みが同じ漢字を選んで□に書きましょう。カッコには音読みを書きましょう。",
          "instruction_en": "Select kanji with the same onyomi from the pool and write their shared onyomi reading.",
          "choices_pool": ["習", "洗", "始", "進", "寝", "思", "止", "職", "参", "紙", "色", "森"],
          "items": [
            {
              "id": "k_ex_matome6_4_1",
              "number": 1,
              "prompt": "音読みが「シ」の漢字（4つ）",
              "answers": ["始", "思", "止", "紙"],
              "reading": "シ",
              "explanation": "「始（開始）」「思（意思）」「止（中止）」「紙（用紙）」の音読みはすべて「シ」です（習＝シュウ、洗＝セン、参＝サン）。"
            },
            {
              "id": "k_ex_matome6_4_2",
              "number": 2,
              "prompt": "音読みが「シン」の漢字（3つ）",
              "answers": ["進", "寝", "森"],
              "reading": "シン",
              "explanation": "「進（進行）」「寝（寝室）」「森（森林）」の音読みはすべて「シン」です。"
            },
            {
              "id": "k_ex_matome6_4_3",
              "number": 3,
              "prompt": "音読みが「ショク」の漢字（2つ）",
              "answers": ["職", "色"],
              "reading": "ショク",
              "explanation": "「職（職業・就職）」「色（特色・顔色）」の音読みは「ショク」です。"
            }
          ]
        }
      ]
    },
    {
      "lesson_number": 19,
      "title": "第19回 音読みと訓読みを覚える新しい漢字：動詞 (New Onyomi & Kunyomi Kanji: Verbs)",
      "page_range": "81-83",
      "exercises": [
        {
          "exercise_id": "k_ex_19_1",
          "number": 1,
          "type": "reading_recall",
          "instruction_ja": "＿＿の部分の読み方を書きましょう。",
          "instruction_en": "Write the readings for the underlined words.",
          "items": [
            {
              "id": "k_ex_19_1_1a",
              "number": 1,
              "sub": "a",
              "sentence": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>と<ruby>水<rt>みず</rt></ruby>の a【量】を<ruby>正確<rt>せいかく</rt></ruby>に b【量って】ください。",
              "target": "量",
              "answer": "りょう",
              "reading": "りょう",
              "ruby_html": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>と<ruby>水<rt>みず</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>を<ruby>正確<rt>せいかく</rt></ruby>に<ruby>量<rt>はか</rt></ruby>ってください。",
              "translation": "Please measure the amount of flour and water accurately.",
              "explanation": "量（りょう）は音読みの名詞、量る（はかる）は訓読みの動詞です。"
            },
            {
              "id": "k_ex_19_1_1b",
              "number": 1,
              "sub": "b",
              "sentence": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>と<ruby>水<rt>みず</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>を<ruby>正確<rt>せいかく</rt></ruby>に b【量って】ください。",
              "target": "量って",
              "answer": "はかって",
              "reading": "はかって",
              "ruby_html": "<ruby>小麦粉<rt>こむぎこ</rt></ruby>と<ruby>水<rt>みず</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>を<ruby>正確<rt>せいかく</rt></ruby>に<ruby>量<rt>はか</rt></ruby>ってください。",
              "translation": "Please measure the amount of flour and water accurately.",
              "explanation": "重さや分量を調べることは「量る（はかる）」と書きます。"
            },
            {
              "id": "k_ex_19_1_2a",
              "number": 2,
              "sub": "a",
              "sentence": "まだ<ruby>仕事<rt>しごと</rt></ruby>が a【残って】いるから、b【残業】しなければならない。",
              "target": "残って",
              "answer": "のこって",
              "reading": "のこって",
              "ruby_html": "まだ<ruby>仕事<rt>しごと</rt></ruby>が<ruby>残<rt>のこ</rt></ruby>っているから、<ruby>残業<rt>ざんぎょう</rt></ruby>しなければならない。",
              "translation": "Since there is still work remaining, I have to work overtime.",
              "explanation": "残る（のこる）は訓読み、残業（ざんぎょう）は音読み「ザン」です。"
            },
            {
              "id": "k_ex_19_1_2b",
              "number": 2,
              "sub": "b",
              "sentence": "まだ<ruby>仕事<rt>しごと</rt></ruby>が<ruby>残<rt>のこ</rt></ruby>っているから、b【残業】しなければならない。",
              "target": "残業",
              "answer": "ざんぎょう",
              "reading": "ざんぎょう",
              "ruby_html": "まだ<ruby>仕事<rt>しごと</rt></ruby>が<ruby>残<rt>のこ</rt></ruby>っているから、<ruby>残業<rt>ざんぎょう</rt></ruby>しなければならない。",
              "translation": "Since there is still work remaining, I have to work overtime.",
              "explanation": "残業（ざんぎょう）は決まった時間を過ぎて残って仕事をすることです。"
            },
            {
              "id": "k_ex_19_1_3a",
              "number": 3,
              "sub": "a",
              "sentence": "<ruby>日本<rt>にほん</rt></ruby>の a【習慣】には b【慣れました】が、まだときどき<ruby>分<rt>わ</rt></ruby>からないことがあります。",
              "target": "習慣",
              "answer": "しゅうかん",
              "reading": "しゅうかん",
              "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>習慣<rt>しゅうかん</rt></ruby>には<ruby>慣<rt>な</rt></ruby>れましたが、まだときどき<ruby>分<rt>わ</rt></ruby>からないことがあります。",
              "translation": "I have gotten used to Japanese customs, but there are still things I occasionally don't understand.",
              "explanation": "習慣（しゅうかん）の「慣」は音読み「カン」、訓読みは「な（れる）」です。"
            },
            {
              "id": "k_ex_19_1_3b",
              "number": 3,
              "sub": "b",
              "sentence": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>習慣<rt>しゅうかん</rt></ruby>には b【慣れました】が、まだときどき<ruby>分<rt>わ</rt></ruby>からないことがあります。",
              "target": "慣れました",
              "answer": "なれました",
              "reading": "なれました",
              "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>の<ruby>習慣<rt>しゅうかん</rt></ruby>には<ruby>慣<rt>な</rt></ruby>れましたが、まだときどき<ruby>分<rt>わ</rt></ruby>からないことがあります。",
              "translation": "I have gotten used to Japanese customs, but there are still things I occasionally don't understand.",
              "explanation": "慣れる（なれる）は訓読みです。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_19_2",
          "number": 2,
          "type": "synonym_completion",
          "instruction_ja": "二つの言葉がだいたい同じ意味になるように、［防・移・調・変］の中の漢字を使って、言葉を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Complete the pairs of words with similar meanings using kanji from [防, 移, 調, 変] and write their readings.",
          "choices": ["防", "移", "調", "変"],
          "items": [
            {
              "id": "k_ex_19_2_1",
              "number": 1,
              "shared_kanji": "移",
              "sentence_a": "<ruby>隣<rt>となり</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>に a【□る】",
              "sentence_b": "<ruby>隣<rt>となり</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>に b【□動】する",
              "answer": "移",
              "reading_a": "うつる",
              "word_a": "移る",
              "reading_b": "いどう",
              "word_b": "移動",
              "ruby_html": "<ruby>隣<rt>となり</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>移<rt>うつ</rt></ruby>る ＝ <ruby>隣<rt>となり</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>移動<rt>いどう</rt></ruby>する",
              "translation": "move to the next classroom = relocate to the next classroom",
              "explanation": "移る（うつる）＝移動（いどう）する。音読みは「イ」です。"
            },
            {
              "id": "k_ex_19_2_2",
              "number": 2,
              "shared_kanji": "調",
              "sentence_a": "<ruby>商品<rt>しょうひん</rt></ruby>の<ruby>値段<rt>ねだん</rt></ruby>を a【□べる】",
              "sentence_b": "<ruby>商品<rt>しょうひん</rt></ruby>の<ruby>値段<rt>ねだん</rt></ruby>を b【□査】する",
              "answer": "調",
              "reading_a": "しらべる",
              "word_a": "調べる",
              "reading_b": "ちょうさ",
              "word_b": "調査",
              "ruby_html": "<ruby>商品<rt>しょうひん</rt></ruby>の<ruby>値段<rt>ねだん</rt></ruby>を<ruby>調<rt>しら</rt></ruby>べる ＝ <ruby>商品<rt>しょうひん</rt></ruby>の<ruby>値段<rt>ねだん</rt></ruby>を<ruby>調査<rt>ちょうさ</rt></ruby>する",
              "translation": "check product prices =調査/survey product prices",
              "explanation": "調べる（しらべる）＝調査（ちょうさ）する。音読みは「チョウ」です。"
            },
            {
              "id": "k_ex_19_2_3",
              "number": 3,
              "shared_kanji": "変",
              "sentence_a": "<ruby>町<rt>まち</rt></ruby>の<ruby>様子<rt>ようす</rt></ruby>が a【□わる】",
              "sentence_b": "<ruby>町<rt>まち</rt></ruby>の<ruby>様子<rt>ようす</rt></ruby>が b【□化】する",
              "answer": "変",
              "reading_a": "かわる",
              "word_a": "変わる",
              "reading_b": "へんか",
              "word_b": "変化",
              "ruby_html": "<ruby>町<rt>まち</rt></ruby>の<ruby>様子<rt>ようす</rt></ruby>が<ruby>変<rt>か</rt></ruby>わる ＝ <ruby>町<rt>まち</rt></ruby>の<ruby>様子<rt>ようす</rt></ruby>が<ruby>変化<rt>へんか</rt></ruby>する",
              "translation": "the town's appearance changes = the town's appearance undergoes change",
              "explanation": "変わる（かわる）＝変化（へんか）する。音読みは「ヘン」です。"
            },
            {
              "id": "k_ex_19_2_4",
              "number": 4,
              "shared_kanji": "防",
              "sentence_a": "<ruby>犯罪<rt>はんざい</rt></ruby>を a【□ぐ】",
              "sentence_b": "<ruby>犯罪<rt>はんざい</rt></ruby>を b【□止】する",
              "answer": "防",
              "reading_a": "ふせぐ",
              "word_a": "防ぐ",
              "reading_b": "ぼうし",
              "word_b": "防止",
              "ruby_html": "<ruby>犯罪<rt>はんざい</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐ ＝ <ruby>犯罪<rt>はんざい</rt></ruby>を<ruby>防止<rt>ぼうし</rt></ruby>する",
              "translation": "prevent crime = stop/prevent crime",
              "explanation": "防ぐ（ふせぐ）＝防止（ぼうし）する。音読みは「ボウ」（予防・防止）です。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_19_3",
          "number": 3,
          "type": "multiple_choice",
          "instruction_ja": "正しいものを選びましょう。",
          "instruction_en": "Choose the correct reading or kanji.",
          "items": [
            {
              "id": "k_ex_19_3_1",
              "number": 1,
              "question_ja": "<ruby>手続<rt>てつづ</rt></ruby>きには、<u>預金</u>の<ruby>通帳<rt>つうちょう</rt></ruby>のコピーが<ruby>必要<rt>ひつよう</rt></ruby>です。",
              "target": "預金",
              "options": ["よきん", "ようきん"],
              "correct_index": 0,
              "answer": "よきん",
              "ruby_html": "<ruby>手続<rt>てつづ</rt></ruby>きには、<ruby>預金<rt>よきん</rt></ruby>の<ruby>通帳<rt>つうちょう</rt></ruby>のコピーが<ruby>必要<rt>ひつよう</rt></ruby>です。",
              "translation": "A copy of your bankbook is required for the procedure.",
              "explanation": "預金（よきん）の「預」は短音の「よ」です。"
            },
            {
              "id": "k_ex_19_3_2",
              "number": 2,
              "question_ja": "<ruby>寒<rt>さむ</rt></ruby>くて、<ruby>体<rt>からだ</rt></ruby>が<u>震えます</u>。",
              "target": "震えます",
              "options": ["くるえます", "ふるえます"],
              "correct_index": 1,
              "answer": "ふるえます",
              "ruby_html": "<ruby>寒<rt>さむ</rt></ruby>くて、<ruby>体<rt>からだ</rt></ruby>が<ruby>震<rt>ふる</rt></ruby>えます。",
              "translation": "It's so cold that my body is shivering.",
              "explanation": "震える（ふるえる）は訓読みです。"
            },
            {
              "id": "k_ex_19_3_3",
              "number": 3,
              "question_ja": "<ruby>昨日<rt>きのう</rt></ruby>の<u>地震</u>は、ちょっと<ruby>大<rt>おお</rt></ruby>きかったですね。",
              "target": "地震",
              "options": ["じちん", "じしん", "ちしん"],
              "correct_index": 1,
              "answer": "じしん",
              "ruby_html": "<ruby>昨日<rt>きのう</rt></ruby>の<ruby>地震<rt>じしん</rt></ruby>は、ちょっと<ruby>大<rt>おお</rt></ruby>きかったですね。",
              "translation": "Yesterday's earthquake was quite big, wasn't it?",
              "explanation": "地震（じしん）の「震」は音読み「シン」です。"
            },
            {
              "id": "k_ex_19_3_4",
              "number": 4,
              "question_ja": "<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しで、<u>大量</u>のごみが<ruby>出<rt>で</rt></ruby>た。",
              "target": "大量",
              "options": ["たいりょ", "だいりょう", "たいりょう"],
              "correct_index": 2,
              "answer": "たいりょう",
              "ruby_html": "<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>しで、<ruby>大量<rt>たいりょう</rt></ruby>のごみが<ruby>出<rt>で</rt></ruby>た。",
              "translation": "A large amount of trash came out from moving house.",
              "explanation": "大量（たいりょう）は量が多いことです。"
            },
            {
              "id": "k_ex_19_3_5",
              "number": 5,
              "question_ja": "<ruby>一生懸命<rt>いっしょうけんめい</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>したおかげで、<ruby>試験<rt>しけん</rt></ruby>に<u>うかった</u>。",
              "target": "うかった",
              "options": ["受かった", "覚かった", "妥かった"],
              "correct_index": 0,
              "answer": "受かった",
              "ruby_html": "<ruby>一生懸命<rt>いっしょうけんめい</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>したおかげで、<ruby>試験<rt>しけん</rt></ruby>に<ruby>受<rt>う</rt></ruby>かった。",
              "translation": "Thanks to studying with all my might, I passed the exam.",
              "explanation": "試験に合格することは「受かる（うかる）」と書きます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_19_4",
          "number": 4,
          "type": "radical_completion",
          "instruction_ja": "漢字の部分を入れて、漢字を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Add the missing component to complete the kanji and write the reading of the underlined word.",
          "items": [
            {
              "id": "k_ex_19_4_1",
              "number": 1,
              "radical_given": "氵（さんずい）",
              "sentence": "<ruby>去年<rt>きょねん</rt></ruby>は<ruby>赤<rt>あか</rt></ruby>だったが、<ruby>今年<rt>ことし</rt></ruby>は<ruby>白<rt>しろ</rt></ruby>が【流行】の<ruby>色<rt>いろ</rt></ruby>だそうだ。",
              "target": "流行",
              "answer": "流",
              "reading": "りゅうこう",
              "ruby_html": "<ruby>去年<rt>きょねん</rt></ruby>は<ruby>赤<rt>あか</rt></ruby>だったが、<ruby>今年<rt>ことし</rt></ruby>は<ruby>白<rt>しろ</rt></ruby>が<ruby>流行<rt>りゅうこう</rt></ruby>の<ruby>色<rt>いろ</rt></ruby>だそうだ。",
              "translation": "Last year it was red, but this year white is said to be the trendy color.",
              "explanation": "氵＋充＝流。流行（りゅうこう）は世の中で広くはやることです。"
            },
            {
              "id": "k_ex_19_4_2",
              "number": 2,
              "radical_given": "木（きへん）",
              "sentence": "この<ruby>庭<rt>にわ</rt></ruby>には、<ruby>珍<rt>めずら</rt></ruby>しい【植物】がたくさんある。",
              "target": "植物",
              "answer": "植",
              "reading": "しょくぶつ",
              "ruby_html": "この<ruby>庭<rt>にわ</rt></ruby>には、<ruby>珍<rt>めずら</rt></ruby>しい<ruby>植物<rt>しょくぶつ</rt></ruby>がたくさんある。",
              "translation": "There are many rare plants in this garden.",
              "explanation": "木＋直＝植。植物（しょくぶつ）の「植」は音読み「ショク」です。"
            },
            {
              "id": "k_ex_19_4_3",
              "number": 3,
              "radical_given": "言（ごんべん）",
              "sentence": "<ruby>市長<rt>しちょう</rt></ruby>が<ruby>午後<rt>ごご</rt></ruby>、この<ruby>病院<rt>びょういん</rt></ruby>を【訪問】することになっている。",
              "target": "訪問",
              "answer": "訪",
              "reading": "ほうもん",
              "ruby_html": "<ruby>市長<rt>しちょう</rt></ruby>が<ruby>午後<rt>ごご</rt></ruby>、この<ruby>病院<rt>びょういん</rt></ruby>を<ruby>訪問<rt>ほうもん</rt></ruby>することになっている。",
              "translation": "The mayor is scheduled to visit this hospital in the afternoon.",
              "explanation": "言＋方＝訪。訪問（ほうもん）は人を訪ねることです。"
            },
            {
              "id": "k_ex_19_4_4",
              "number": 4,
              "radical_given": "爫（つめかんむり）",
              "sentence": "<ruby>弟<rt>おとうと</rt></ruby>はみどり<ruby>大学<rt>だいがく</rt></ruby>を【受験】して、<ruby>合格<rt>ごうかく</rt></ruby>した。",
              "target": "受験",
              "answer": "受",
              "reading": "じゅけん",
              "ruby_html": "<ruby>弟<rt>おとうと</rt></ruby>はみどり<ruby>大学<rt>だいがく</rt></ruby>を<ruby>受験<rt>じゅけん</rt></ruby>して、<ruby>合格<rt>ごうかく</rt></ruby>した。",
              "translation": "My younger brother took the entrance examination for Midori University and passed.",
              "explanation": "受験（じゅけん）は試験を受けることです。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_19_5",
          "number": 5,
          "type": "word_pairing",
          "instruction_ja": "□には同じ漢字が入ります。［違・配・育・曲］から漢字を選んで書きましょう。＿＿の部分の読み方も書きましょう。",
          "instruction_en": "Fill in the same kanji in each group of boxes from [違, 配, 育, 曲] and write the readings.",
          "choices": ["違", "配", "育", "曲"],
          "items": [
            {
              "id": "k_ex_19_5_1",
              "number": 1,
              "shared_kanji": "配",
              "sentence_a": "<ruby>試験問題<rt>しけんもんだい</rt></ruby>を a【□ります】から、<ruby>名前<rt>なまえ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてください。",
              "sentence_b": "<ruby>昼間<rt>ひるま</rt></ruby>は<ruby>留守<rt>るす</rt></ruby>なので、<ruby>書留<rt>かきとめ</rt></ruby>の b【□達】は<ruby>夜<rt>よる</rt></ruby>にお<ruby>願<rt>ねが</rt></ruby>いします。",
              "answer": "配",
              "reading_a": "くばります",
              "word_a": "配ります",
              "reading_b": "はいたつ",
              "word_b": "配達",
              "ruby_html": "<ruby>試験問題<rt>しけんもんだい</rt></ruby>を<ruby>配<rt>くば</rt></ruby>りますから、<ruby>名前<rt>なまえ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてください。 / <ruby>昼間<rt>ひるま</rt></ruby>は<ruby>留守<rt>るす</rt></ruby>なので、<ruby>書留<rt>かきとめ</rt></ruby>の<ruby>配達<rt>はいたつ</rt></ruby>は<ruby>夜<rt>よる</rt></ruby>にお<ruby>願<rt>ねが</rt></ruby>いします。",
              "translation": "I will hand out the exam papers, so please write your name. / Since I am out during the day, please deliver the registered mail at night.",
              "explanation": "配：訓読み「くば（る）」、音読み「ハイ」（配達：はいたつ・心配：しんぱい）。"
            },
            {
              "id": "k_ex_19_5_2",
              "number": 2,
              "shared_kanji": "曲",
              "sentence_a": "<ruby>地震<rt>じしん</rt></ruby>で<ruby>柱<rt>はしら</rt></ruby>が a【□がって】しまった。",
              "sentence_b": "この<ruby>美<rt>うつく</rt></ruby>しい b【□】は、<ruby>誰<rt>だれ</rt></ruby>が c【作□】したのですか。",
              "answer": "曲",
              "reading_a": "まがって",
              "word_a": "曲がって",
              "reading_b": "きょく",
              "word_b": "曲",
              "reading_c": "さっきょく",
              "word_c": "作曲",
              "ruby_html": "<ruby>地震<rt>じしん</rt></ruby>で<ruby>柱<rt>はしら</rt></ruby>が<ruby>曲<rt>ま</rt></ruby>がってしまった。 / この<ruby>美<rt>うつく</rt></ruby>しい<ruby>曲<rt>きょく</rt></ruby>は、<ruby>誰<rt>だれ</rt></ruby>が<ruby>作曲<rt>さっきょく</rt></ruby>したのですか。",
              "translation": "The pillar was bent by the earthquake. / Who composed this beautiful piece of music?",
              "explanation": "曲：訓読み「ま（がる）」、音読み「キョク」（曲：きょく・作曲：さっきょく・曲線：きょくせん）。"
            },
            {
              "id": "k_ex_19_5_3",
              "number": 3,
              "shared_kanji": "違",
              "sentence_a": "<ruby>私<rt>わたし</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>えは、あなたのとはちょっと a【□います】。",
              "sentence_b": "スピード b【□反】で、<ruby>警察<rt>けいさつ</rt></ruby>に<ruby>捕<rt>つか</rt></ruby>まった。",
              "answer": "違",
              "reading_a": "ちがいます",
              "word_a": "違います",
              "reading_b": "いはん",
              "word_b": "違反",
              "ruby_html": "<ruby>私<rt>わたし</rt></ruby>の<ruby>考<rt>かんが</rt></ruby>えは、あなたのとはちょっと<ruby>違<rt>ちが</rt></ruby>います。 / スピード<ruby>違反<rt>いはん</rt></ruby>で、<ruby>警察<rt>けいさつ</rt></ruby>に<ruby>捕<rt>つか</rt></ruby>まった。",
              "translation": "My opinion is slightly different from yours. / I was caught by the police for a speeding violation.",
              "explanation": "違：訓読み「ちが（う）」、音読み「イ」（違反：いはん）。"
            },
            {
              "id": "k_ex_19_5_4",
              "number": 4,
              "shared_kanji": "育",
              "sentence_a": "<ruby>父<rt>ちち</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>死<rt>し</rt></ruby>んだので、<ruby>私<rt>わたし</rt></ruby>は<ruby>母<rt>はは</rt></ruby>に a【□てられた】。",
              "sentence_b": "<ruby>雨<rt>あめ</rt></ruby>だったので、b【体□館】で<ruby>運動<rt>うんどう</rt></ruby>した。",
              "answer": "育",
              "reading_a": "そだてられた",
              "word_a": "育てられた",
              "reading_b": "たいいくかん",
              "word_b": "体育館",
              "ruby_html": "<ruby>父<rt>ちち</rt></ruby>が<ruby>早<rt>はや</rt></ruby>く<ruby>死<rt>し</rt></ruby>んだので、<ruby>私<rt>わたし</rt></ruby>は<ruby>母<rt>はは</rt></ruby>に<ruby>育<rt>そだ</rt></ruby>てられた。 / <ruby>雨<rt>あめ</rt></ruby>だったので、<ruby>体育館<rt>たいいくかん</rt></ruby>で<ruby>運動<rt>うんどう</rt></ruby>した。",
              "translation": "Since my father died young, I was raised by my mother. / Since it was raining, I exercised in the gymnasium.",
              "explanation": "育：訓読み「そだ（てる）」、音読み「イク」（体育館：たいいくかん・教育：きょういく）。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_19_6",
          "number": 6,
          "type": "reading_writing",
          "instruction_ja": "＿＿の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
          "instruction_en": "Write the reading for underlined kanji and write kanji for underlined hiragana.",
          "items": [
            {
              "id": "k_ex_19_6_1",
              "number": 1,
              "mode": "reading",
              "sentence": "<ruby>会場<rt>かいじょう</rt></ruby>の【受付】で、<ruby>名前<rt>なまえ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてください。",
              "target": "受付",
              "answer": "うけつけ",
              "reading": "うけつけ",
              "ruby_html": "<ruby>会場<rt>かいじょう</rt></ruby>の<ruby>受付<rt>うけつけ</rt></ruby>で、<ruby>名前<rt>なまえ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてください。",
              "translation": "Please write your name at the reception desk of the venue.",
              "explanation": "受付（うけつけ）は訓読み同士の複合名詞です。"
            },
            {
              "id": "k_ex_19_6_2",
              "number": 2,
              "mode": "reading",
              "sentence": "<ruby>学生時代<rt>がくせいじだい</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>を【訪ねた】。",
              "target": "訪ねた",
              "answer": "たずねた",
              "reading": "たずねた",
              "ruby_html": "<ruby>学生時代<rt>がくせいじだい</rt></ruby>の<ruby>先生<rt>せんせい</rt></ruby>の<ruby>家<rt>いえ</rt></ruby>を<ruby>訪<rt>たず</rt></ruby>ねた。",
              "translation": "I visited the home of my teacher from my student days.",
              "explanation": "人を訪問するときは「訪ねる（たずねる）」と書きます。"
            },
            {
              "id": "k_ex_19_6_3",
              "number": 3,
              "mode": "reading",
              "sentence": "<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったので、<ruby>今日<rt>きょう</rt></ruby>は<ruby>川<rt>かわ</rt></ruby>の<ruby>水<rt>みず</rt></ruby>がとても<ruby>速<rt>はや</rt></ruby>く【流れて】いる。",
              "target": "流れて",
              "answer": "ながれて",
              "reading": "ながれて",
              "ruby_html": "<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったので、<ruby>今日<rt>きょう</rt></ruby>は<ruby>川<rt>かわ</rt></ruby>の<ruby>水<rt>みず</rt></ruby>がとても<ruby>速<rt>はや</rt></ruby>く<ruby>流<rt>なが</rt></ruby>れている。",
              "translation": "Because it rained, the river water is flowing very fast today.",
              "explanation": "流れる（ながれる）は訓読みです。"
            },
            {
              "id": "k_ex_19_6_4",
              "number": 4,
              "mode": "reading",
              "sentence": "<ruby>飛行機<rt>ひこうき</rt></ruby>に<ruby>乗<rt>の</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に、<ruby>荷物<rt>にもつ</rt></ruby>を【預けた】。",
              "target": "預けた",
              "answer": "あずけた",
              "reading": "あずけた",
              "ruby_html": "<ruby>飛行機<rt>ひこうき</rt></ruby>に<ruby>乗<rt>の</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に、<ruby>荷物<rt>にもつ</rt></ruby>を<ruby>預<rt>あず</rt></ruby>けた。",
              "translation": "Before boarding the airplane, I checked my luggage.",
              "explanation": "預ける（あずける）は保管を頼むことです。"
            },
            {
              "id": "k_ex_19_6_5",
              "number": 5,
              "mode": "kanji_write",
              "sentence": "いろいろな<ruby>種類<rt>しゅるい</rt></ruby>の【ちょうみりょう】をそろえた。",
              "target": "ちょうみりょう",
              "answer": "調味料",
              "reading": "ちょうみりょう",
              "ruby_html": "いろいろな<ruby>種類<rt>しゅるい</rt></ruby>の<ruby>調味料<rt>ちょうみりょう</rt></ruby>をそろえた。",
              "translation": "I gathered various kinds of seasonings.",
              "explanation": "調味料（ちょうみりょう）は味を調える（ととのえる）ための材料です。"
            },
            {
              "id": "k_ex_19_6_6",
              "number": 6,
              "mode": "kanji_write",
              "sentence": "<ruby>庭<rt>にわ</rt></ruby>に【うえた】<ruby>木<rt>き</rt></ruby>に、<ruby>毎日<rt>まいにち</rt></ruby><ruby>小鳥<rt>ことり</rt></ruby>がやって<ruby>来<rt>く</rt></ruby>る。",
              "target": "うえた",
              "answer": "植えた",
              "reading": "うえた",
              "ruby_html": "<ruby>庭<rt>にわ</rt></ruby>に<ruby>植<rt>う</rt></ruby>えた<ruby>木<rt>き</rt></ruby>に、<ruby>毎日<rt>まいにち</rt></ruby><ruby>小鳥<rt>ことり</rt></ruby>がやって<ruby>来<rt>く</rt></ruby>る。",
              "translation": "Small birds come every day to the tree I planted in the garden.",
              "explanation": "草や木を土にうえることは「植える（うえる）」と書きます。"
            }
          ]
        }
      ]
    },
    {
      "lesson_number": 20,
      "title": "第20回 音読みと訓読みを覚える新しい漢字：名詞や形容詞 (New Onyomi & Kunyomi Kanji: Nouns & Adjectives)",
      "page_range": "84-85",
      "exercises": [
        {
          "exercise_id": "k_ex_20_1",
          "number": 1,
          "type": "reading_recall",
          "instruction_ja": "＿＿の部分の読み方を書きましょう。",
          "instruction_en": "Write the readings for the underlined words.",
          "items": [
            {
              "id": "k_ex_20_1_1a",
              "number": 1,
              "sub": "a",
              "sentence": "<ruby>体<rt>からだ</rt></ruby>が a【熱い】。b【熱】があるかもしれない。",
              "target": "熱い",
              "answer": "あつい",
              "reading": "あつい",
              "ruby_html": "<ruby>体<rt>からだ</rt></ruby>が<ruby>熱<rt>あつ</rt></ruby>い。<ruby>熱<rt>ねつ</rt></ruby>があるかもしれない。",
              "translation": "My body feels hot. I might have a fever.",
              "explanation": "熱い（あつい）は形容詞、熱（ねつ）は音読みの名詞です。"
            },
            {
              "id": "k_ex_20_1_1b",
              "number": 1,
              "sub": "b",
              "sentence": "<ruby>体<rt>からだ</rt></ruby>が<ruby>熱<rt>あつ</rt></ruby>い。b【熱】があるかもしれない。",
              "target": "熱",
              "answer": "ねつ",
              "reading": "ねつ",
              "ruby_html": "<ruby>体<rt>からだ</rt></ruby>が<ruby>熱<rt>あつ</rt></ruby>い。<ruby>熱<rt>ねつ</rt></ruby>があるかもしれない。",
              "translation": "My body feels hot. I might have a fever.",
              "explanation": "熱（ねつ）は体温が高くなることや温度・エネルギーを表します。"
            },
            {
              "id": "k_ex_20_1_2a",
              "number": 2,
              "sub": "a",
              "sentence": "<ruby>本当<rt>ほんとう</rt></ruby>に a【確実な】<ruby>情報<rt>じょうほう</rt></ruby>かどうか b【確かめます】。",
              "target": "確実な",
              "answer": "かくじつな",
              "reading": "かくじつな",
              "ruby_html": "<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>確実<rt>かくじつ</rt></ruby>な<ruby>情報<rt>じょうほう</rt></ruby>かどうか<ruby>確<rt>たし</rt></ruby>かめます。",
              "translation": "I will verify whether the information is truly reliable.",
              "explanation": "確実（かくじつ）の「確」は音読み「カク」、確かめる（たしかめる）は訓読みです。"
            },
            {
              "id": "k_ex_20_1_2b",
              "number": 2,
              "sub": "b",
              "sentence": "<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>確実<rt>かくじつ</rt></ruby>な<ruby>情報<rt>じょうほう</rt></ruby>かどうか b【確かめます】。",
              "target": "確かめます",
              "answer": "たしかめます",
              "reading": "たしかめます",
              "ruby_html": "<ruby>本当<rt>ほんとう</rt></ruby>に<ruby>確実<rt>かくじつ</rt></ruby>な<ruby>情報<rt>じょうほう</rt></ruby>かどうか<ruby>確<rt>たし</rt></ruby>かめます。",
              "translation": "I will verify whether the information is truly reliable.",
              "explanation": "確かめる（たしかめる）は本当かどうか調べることです。"
            },
            {
              "id": "k_ex_20_1_3a",
              "number": 3,
              "sub": "a",
              "sentence": "<ruby>日本<rt>にほん</rt></ruby>で<ruby>作<rt>つく</rt></ruby>られた<ruby>漢字<rt>かんじ</rt></ruby>には、a【例えば】どんな b【例】がありますか。",
              "target": "例えば",
              "answer": "たとえば",
              "reading": "たとえば",
              "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>で<ruby>作<rt>つく</rt></ruby>られた<ruby>漢字<rt>かんじ</rt></ruby>には、<ruby>例<rt>たと</rt></ruby>えばどんな<ruby>例<rt>れい</rt></ruby>がありますか。",
              "translation": "What kinds of examples are there, for instance, of kanji created in Japan?",
              "explanation": "例えば（たとえば）は訓読み、例（れい・例外など）は音読み「レイ」です。"
            },
            {
              "id": "k_ex_20_1_3b",
              "number": 3,
              "sub": "b",
              "sentence": "<ruby>日本<rt>にほん</rt></ruby>で<ruby>作<rt>つく</rt></ruby>られた<ruby>漢字<rt>かんじ</rt></ruby>には、<ruby>例<rt>たと</rt></ruby>えばどんな b【例】がありますか。",
              "target": "例",
              "answer": "れい",
              "reading": "れい",
              "ruby_html": "<ruby>日本<rt>にほん</rt></ruby>で<ruby>作<rt>つく</rt></ruby>られた<ruby>漢字<rt>かんじ</rt></ruby>には、<ruby>例<rt>たと</rt></ruby>えばどんな<ruby>例<rt>れい</rt></ruby>がありますか。",
              "translation": "What kinds of examples are there, for instance, of kanji created in Japan?",
              "explanation": "例（れい）は具体例のことです。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_20_2",
          "number": 2,
          "type": "multiple_choice",
          "instruction_ja": "正しいものを選びましょう。",
          "instruction_en": "Choose the correct reading or kanji.",
          "items": [
            {
              "id": "k_ex_20_2_1",
              "number": 1,
              "question_ja": "<ruby>日本語<rt>にほんご</rt></ruby>はまだ<u>初級</u>のレベルです。",
              "target": "初級",
              "options": ["しょうきゅう", "しょきゅ", "しょきゅう"],
              "correct_index": 2,
              "answer": "しょきゅう",
              "ruby_html": "<ruby>日本語<rt>にほんご</rt></ruby>はまだ<ruby>初級<rt>しょきゅう</rt></ruby>のレベルです。",
              "translation": "My Japanese is still at the beginner level.",
              "explanation": "初級（しょきゅう）の「初」は短音の「しょ」です。"
            },
            {
              "id": "k_ex_20_2_2",
              "number": 2,
              "question_ja": "<ruby>夏休<rt>なつやす</rt></ruby>みに<u>深夜</u>のアルバイトをした。",
              "target": "深夜",
              "options": ["しんや", "しんよる"],
              "correct_index": 0,
              "answer": "しんや",
              "ruby_html": "<ruby>夏休<rt>なつやす</rt></ruby>みに<ruby>深夜<rt>しんや</rt></ruby>のアルバイトをした。",
              "translation": "During summer vacation, I worked a late-night part-time job.",
              "explanation": "深夜（しんや）の「深」は音読み「シン」です。"
            },
            {
              "id": "k_ex_20_2_3",
              "number": 3,
              "question_ja": "<ruby>毎晩<rt>まいばん</rt></ruby><ruby>遅<rt>おそ</rt></ruby>くまで<u>熱心</u>に<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>をしている。",
              "target": "熱心",
              "options": ["ねっしん", "ねしん", "ねつしん"],
              "correct_index": 0,
              "answer": "ねっしん",
              "ruby_html": "<ruby>毎晩<rt>まいばん</rt></ruby><ruby>遅<rt>おそ</rt></ruby>くまで<ruby>熱心<rt>ねっしん</rt></ruby>に<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>勉強<rt>べんきょう</rt></ruby>をしている。",
              "translation": "Every night until late, they study kanji earnestly.",
              "explanation": "熱心（ねっしん）は「熱（ねつ）＋心（しん）」が促音化して「ねっしん」となります。"
            },
            {
              "id": "k_ex_20_2_4",
              "number": 4,
              "question_ja": "<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>読<rt>よ</rt></ruby>み<ruby>方<rt>かた</rt></ruby>を<u>正確</u>に<ruby>覚<rt>おぼ</rt></ruby>えましょう。",
              "target": "正確",
              "options": ["しょうかく", "せいかく", "せいがく"],
              "correct_index": 1,
              "answer": "せいかく",
              "ruby_html": "<ruby>漢字<rt>かんじ</rt></ruby>の<ruby>読<rt>よ</rt></ruby>み<ruby>方<rt>かた</rt></ruby>を<ruby>正確<rt>せいかく</rt></ruby>に<ruby>覚<rt>おぼ</rt></ruby>えましょう。",
              "translation": "Let's memorize the readings of kanji accurately.",
              "explanation": "正確（せいかく）は正しく確実なことです。"
            },
            {
              "id": "k_ex_20_2_5",
              "number": 5,
              "question_ja": "<ruby>店<rt>みせ</rt></ruby>は、<ruby>駅<rt>えき</rt></ruby>の<ruby>南口<rt>みなみぐち</rt></ruby>を<ruby>出<rt>で</rt></ruby>て<u>歩道橋</u>を<ruby>渡<rt>わた</rt></ruby>ったところにある。",
              "target": "歩道橋",
              "options": ["ほどうきょう", "ほどうきょ", "はどうきょう"],
              "correct_index": 0,
              "answer": "ほどうきょう",
              "ruby_html": "<ruby>店<rt>みせ</rt></ruby>は、<ruby>駅<rt>えき</rt></ruby>の<ruby>南口<rt>みなみぐち</rt></ruby>を<ruby>出<rt>で</rt></ruby>て<ruby>歩道橋<rt>ほどうきょう</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>ったところにある。",
              "translation": "The shop is right after exiting the south exit of the station and crossing the pedestrian overpass.",
              "explanation": "歩道橋（ほどうきょう）の「橋」は音読み「キョウ」です。"
            },
            {
              "id": "k_ex_20_2_6",
              "number": 6,
              "question_ja": "<ruby>地域<rt>ちいき</rt></ruby>の<ruby>住民<rt>じゅうみん</rt></ruby>の<u>ようきゅう</u>をまとめて、<ruby>県<rt>けん</rt></ruby>に<ruby>提出<rt>ていしゅつ</rt></ruby>した。",
              "target": "ようきゅう",
              "options": ["要急", "要求", "用求"],
              "correct_index": 1,
              "answer": "要求",
              "ruby_html": "<ruby>地域<rt>ちいき</rt></ruby>の<ruby>住民<rt>じゅうみん</rt></ruby>の<ruby>要求<rt>ようきゅう</rt></ruby>をまとめて、<ruby>県<rt>けん</rt></ruby>に<ruby>提出<rt>ていしゅつ</rt></ruby>した。",
              "translation": "We compiled the demands of local residents and submitted them to the prefecture.",
              "explanation": "必要として求めることは「要求（ようきゅう）」と書きます。"
            },
            {
              "id": "k_ex_20_2_7",
              "number": 7,
              "question_ja": "この<ruby>規則<rt>きそく</rt></ruby>に<u>れいがい</u>はありません。",
              "target": "れいがい",
              "options": ["例外", "列外", "冽外"],
              "correct_index": 0,
              "answer": "例外",
              "ruby_html": "この<ruby>規則<rt>きそく</rt></ruby>に<ruby>例外<rt>れいがい</rt></ruby>はありません。",
              "translation": "There are no exceptions to this rule.",
              "explanation": "規則や普通の例から外れることは「例外（れいがい）」と書きます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_20_3",
          "number": 3,
          "type": "synonym_completion",
          "instruction_ja": "二つの言葉がだいたい同じ意味になるように、［初・要・必・痛］の中の漢字を使って、言葉を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Complete the pairs of expressions with similar meanings using kanji from [初, 要, 必, 痛] and write their readings.",
          "choices": ["初", "要", "必", "痛"],
          "items": [
            {
              "id": "k_ex_20_3_1",
              "number": 1,
              "shared_kanji": "初",
              "sentence_a": "<ruby>誰<rt>だれ</rt></ruby>でも a【□め】は<ruby>緊張<rt>きんちょう</rt></ruby>する。",
              "sentence_b": "<ruby>誰<rt>だれ</rt></ruby>でも b【最□】は<ruby>緊張<rt>きんちょう</rt></ruby>する。",
              "answer": "初",
              "reading_a": "はじめ",
              "word_a": "初め",
              "reading_b": "さいしょ",
              "word_b": "最初",
              "ruby_html": "<ruby>誰<rt>だれ</rt></ruby>でも<ruby>初<rt>はじ</rt></ruby>めは<ruby>緊張<rt>きんちょう</rt></ruby>する。 ＝ <ruby>誰<rt>だれ</rt></ruby>でも<ruby>最初<rt>さいしょ</rt></ruby>は<ruby>緊張<rt>きんちょう</rt></ruby>する。",
              "translation": "Everyone is nervous at the beginning. = Everyone is nervous at first.",
              "explanation": "初め（はじめ）＝最初（さいしょ）。音読みは「ショ」です。"
            },
            {
              "id": "k_ex_20_3_2",
              "number": 2,
              "shared_kanji": "痛",
              "sentence_a": "<ruby>朝<rt>あさ</rt></ruby>から a【頭が□い】。",
              "sentence_b": "<ruby>朝<rt>あさ</rt></ruby>から b【頭□がする】。",
              "answer": "痛",
              "reading_a": "あたまがいたい",
              "word_a": "頭が痛い",
              "reading_b": "ずつうがする",
              "word_b": "頭痛がする",
              "ruby_html": "<ruby>朝<rt>あさ</rt></ruby>から<ruby>頭<rt>あたま</rt></ruby>が<ruby>痛<rt>いた</rt></ruby>い。 ＝ <ruby>朝<rt>あさ</rt></ruby>から<ruby>頭痛<rt>ずつう</rt></ruby>がする。",
              "translation": "My head hurts since morning. = I have a headache since morning.",
              "explanation": "頭が痛い（あたまがいたい）＝頭痛（ずつう）がする。音読みは「ツウ」です。"
            },
            {
              "id": "k_ex_20_3_3",
              "number": 3,
              "shared_kanji": "必",
              "sentence_a": "<ruby>海外旅行<rt>かいがいりょこう</rt></ruby>はパスポートが a【かならず□る】。",
              "sentence_b": "<ruby>海外旅行<rt>かいがいりょこう</rt></ruby>はパスポートが b【必要だ】。",
              "answer": "要",
              "reading_a": "かならずいる",
              "word_a": "必ず要る",
              "reading_b": "ひつようだ",
              "word_b": "必要だ",
              "ruby_html": "<ruby>海外旅行<rt>かいがいりょこう</rt></ruby>はパスポートが<ruby>必<rt>かなら</rt></ruby>ず<ruby>要<rt>い</rt></ruby>る。 ＝ <ruby>海外旅行<rt>かいがいりょこう</rt></ruby>はパスポートが<ruby>必要<rt>ひつよう</rt></ruby>だ。",
              "translation": "For overseas travel, a passport is definitely needed. = For overseas travel, a passport is necessary.",
              "explanation": "必ず（かならず）＋要る（いる）＝必要（ひつよう）だ。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_20_4",
          "number": 4,
          "type": "radical_completion",
          "instruction_ja": "漢字の部分を入れて、漢字を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Add the missing part to complete the kanji and write the reading.",
          "items": [
            {
              "id": "k_ex_20_4_1",
              "number": 1,
              "radical_given": "禾（のぎへん）",
              "sentence": "この<ruby>魚屋<rt>さかなや</rt></ruby>さんでは、いろいろな【種類】の<ruby>魚<rt>さかな</rt></ruby>を<ruby>売<rt>う</rt></ruby>っている。",
              "target": "種類",
              "answer": "種",
              "reading": "しゅるい",
              "ruby_html": "この<ruby>魚屋<rt>さかなや</rt></ruby>さんでは、いろいろな<ruby>種類<rt>しゅるい</rt></ruby>の<ruby>魚<rt>さかな</rt></ruby>を<ruby>売<rt>う</rt></ruby>っている。",
              "translation": "This fish shop sells various kinds of fish.",
              "explanation": "禾＋重＝種。種類（しゅるい）の「種」は音読み「シュ」です。"
            },
            {
              "id": "k_ex_20_4_2",
              "number": 2,
              "radical_given": "氵（さんずい）",
              "sentence": "この<ruby>海<rt>うみ</rt></ruby>は、<ruby>急<rt>きゅう</rt></ruby>に【深く】なって<ruby>危険<rt>きけん</rt></ruby>ですから、<ruby>泳<rt>およ</rt></ruby>いではいけません。",
              "target": "深く",
              "answer": "深",
              "reading": "ふかく",
              "ruby_html": "この<ruby>海<rt>うみ</rt></ruby>は、<ruby>急<rt>きゅう</rt></ruby>に<ruby>深<rt>ふか</rt></ruby>くなって<ruby>危険<rt>きけん</rt></ruby>ですから、<ruby>泳<rt>およ</rt></ruby>いではいけません。",
              "translation": "Because this sea suddenly gets deep and is dangerous, you must not swim here.",
              "explanation": "深い（ふかい）は訓読みです。"
            },
            {
              "id": "k_ex_20_4_3",
              "number": 3,
              "radical_given": "木（きへん）",
              "sentence": "<ruby>昔<rt>むかし</rt></ruby>は、この<ruby>川<rt>かわ</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>るのが<ruby>大変<rt>たいへん</rt></ruby>だったので、【橋】ができてみんな<ruby>喜<rt>よろこ</rt></ruby>んだ。",
              "target": "橋",
              "answer": "橋",
              "reading": "はし",
              "ruby_html": "<ruby>昔<rt>むかし</rt></ruby>は、この<ruby>川<rt>かわ</rt></ruby>を<ruby>渡<rt>わた</rt></ruby>るのが<ruby>大変<rt>たいへん</rt></ruby>だったので、<ruby>橋<rt>はし</rt></ruby>ができてみんな<ruby>喜<rt>よろこ</rt></ruby>んだ。",
              "translation": "In the past, crossing this river was difficult, so everyone was delighted when the bridge was built.",
              "explanation": "橋（はし）は訓読みです（音読みはキョウ：歩道橋）。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_20_5",
          "number": 5,
          "type": "reading_writing",
          "instruction_ja": "＿＿の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
          "instruction_en": "Write the reading for underlined kanji and write kanji for underlined hiragana.",
          "items": [
            {
              "id": "k_ex_20_5_1",
              "number": 1,
              "mode": "reading",
              "sentence": "<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだら、やっと【平熱】に<ruby>下<rt>さ</rt></ruby>がった。",
              "target": "平熱",
              "answer": "へいねつ",
              "reading": "へいねつ",
              "ruby_html": "<ruby>薬<rt>くすり</rt></ruby>を<ruby>飲<rt>の</rt></ruby>んだら、やっと<ruby>平熱<rt>へいねつ</rt></ruby>に<ruby>下<rt>さ</rt></ruby>がった。",
              "translation": "After I took the medicine, my temperature finally went down to normal.",
              "explanation": "平熱（へいねつ）は普段の正常な体温のことです。"
            },
            {
              "id": "k_ex_20_5_2",
              "number": 2,
              "mode": "reading",
              "sentence": "ご<ruby>注文<rt>ちゅうもん</rt></ruby>の<ruby>品<rt>しな</rt></ruby>は、<ruby>明日<rt>あす</rt></ruby>【確かに】お<ruby>届<rt>とど</rt></ruby>けします。",
              "target": "確かに",
              "answer": "たしかに",
              "reading": "たしかに",
              "ruby_html": "ご<ruby>注文<rt>ちゅうもん</rt></ruby>の<ruby>品<rt>しな</rt></ruby>は、<ruby>明日<rt>あす</rt></ruby><ruby>確<rt>たし</rt></ruby>かにお<ruby>届<rt>とど</rt></ruby>けします。",
              "translation": "We will certainly deliver your ordered item tomorrow.",
              "explanation": "確かに（たしかに）は間違いなく・確実にという意味です。"
            },
            {
              "id": "k_ex_20_5_3",
              "number": 3,
              "mode": "reading",
              "sentence": "<ruby>花<rt>はな</rt></ruby>の【種】を<ruby>買<rt>か</rt></ruby>った。",
              "target": "種",
              "answer": "たね",
              "reading": "たね",
              "ruby_html": "<ruby>花<rt>はな</rt></ruby>の<ruby>種<rt>たね</rt></ruby>を<ruby>買<rt>か</rt></ruby>った。",
              "translation": "I bought flower seeds.",
              "explanation": "種（たね）は訓読みです。"
            },
            {
              "id": "k_ex_20_5_4",
              "number": 4,
              "mode": "reading",
              "sentence": "この<ruby>漢字<rt>かんじ</rt></ruby>は【正しい】ですか。",
              "target": "正しい",
              "answer": "ただしい",
              "reading": "ただしい",
              "ruby_html": "この<ruby>漢字<rt>かんじ</rt></ruby>は<ruby>正<rt>ただ</rt></ruby>しいですか。",
              "translation": "Is this kanji correct?",
              "explanation": "正しい（ただしい）は訓読みです（音読みはセイ・ショウ：正確・正月）。"
            },
            {
              "id": "k_ex_20_5_5",
              "number": 5,
              "mode": "kanji_write",
              "sentence": "【はじめて】<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>会話<rt>かいわ</rt></ruby>ができたときは、うれしかった。",
              "target": "はじめて",
              "answer": "初めて",
              "reading": "はじめて",
              "ruby_html": "<ruby>初<rt>はじ</rt></ruby>めて<ruby>日本語<rt>にほんご</rt></ruby>で<ruby>会話<rt>かいわ</rt></ruby>ができたときは、うれしかった。",
              "translation": "When I was able to have a conversation in Japanese for the first time, I was happy.",
              "explanation": "最初に経験することは「初めて（はじめて）」と書きます。"
            }
          ]
        }
      ]
    },
    {
      "lesson_number": "summary_7",
      "title": "まとめ問題 (7) (Review Quiz 7: Lessons 19-20)",
      "page_range": "86-87",
      "exercises": [
        {
          "exercise_id": "k_ex_matome7_1",
          "number": 1,
          "type": "multiple_choice",
          "instruction_ja": "＿＿の言葉の読み方として最もよいものを、1・2・3・4から一つ選びましょう。",
          "instruction_en": "Choose the best reading for the underlined word from 1, 2, 3, or 4.",
          "items": [
            {
              "id": "k_ex_matome7_1_1",
              "number": 1,
              "question_ja": "<ruby>平仮名<rt>ひらがな</rt></ruby>は<u>曲線</u>が<ruby>多<rt>おお</rt></ruby>い<ruby>文字<rt>もじ</rt></ruby>だ。",
              "target": "曲線",
              "options": ["きょっくせん", "きょくせん", "きょくぜん", "きょぐせん"],
              "correct_index": 1,
              "answer": "きょくせん",
              "ruby_html": "<ruby>平仮名<rt>ひらがな</rt></ruby>は<ruby>曲線<rt>きょくせん</rt></ruby>が<ruby>多<rt>おお</rt></ruby>い<ruby>文字<rt>もじ</rt></ruby>だ。",
              "translation": "Hiragana is a script with many curved lines.",
              "explanation": "曲線（きょくせん）は曲がった線のことです。"
            },
            {
              "id": "k_ex_matome7_1_2",
              "number": 2,
              "question_ja": "<u>地味</u>な<ruby>色<rt>いろ</rt></ruby>の<ruby>服<rt>ふく</rt></ruby>もよくお<ruby>似合<rt>にあ</rt></ruby>いですよ。",
              "target": "地味",
              "options": ["ぎみ", "ちみ", "しみ", "じみ"],
              "correct_index": 3,
              "answer": "じみ",
              "ruby_html": "<ruby>地味<rt>じみ</rt></ruby>な<ruby>色<rt>いろ</rt></ruby>の<ruby>服<rt>ふく</rt></ruby>もよくお<ruby>似合<rt>にあ</rt></ruby>いですよ。",
              "translation": "Subdued-colored clothes also suit you very well.",
              "explanation": "地味（じみ）の「地」は「ジ」と読みます。"
            },
            {
              "id": "k_ex_matome7_1_3",
              "number": 3,
              "question_ja": "<ruby>用事<rt>ようじ</rt></ruby>があったので、<ruby>子供<rt>こども</rt></ruby>を<ruby>隣<rt>となり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<u>預かって</u>もらった。",
              "target": "預かって",
              "options": ["かずあって", "あずかって", "さずかって", "かずさって"],
              "correct_index": 1,
              "answer": "あずかって",
              "ruby_html": "<ruby>用事<rt>ようじ</rt></ruby>があったので、<ruby>子供<rt>こども</rt></ruby>を<ruby>隣<rt>となり</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>に<ruby>預<rt>あず</rt></ruby>かってもらった。",
              "translation": "Because I had an errand, I had my neighbor look after my child.",
              "explanation": "預かる（あずかる）のテ形は「預かって（あずかって）」です。"
            },
            {
              "id": "k_ex_matome7_1_4",
              "number": 4,
              "question_ja": "<ruby>次<rt>つぎ</rt></ruby>の<u>体育</u>の<ruby>時間<rt>じかん</rt></ruby>は、テニスをします。",
              "target": "体育",
              "options": ["たいいく", "ていいく", "たいく", "ていく"],
              "correct_index": 0,
              "answer": "たいいく",
              "ruby_html": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>体育<rt>たいいく</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>は、テニスをします。",
              "translation": "In the next physical education class, we will play tennis.",
              "explanation": "体育（たいいく）は「い」が二つ続きます。"
            },
            {
              "id": "k_ex_matome7_1_5",
              "number": 5,
              "question_ja": "<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>仕事<rt>しごと</rt></ruby>を<ruby>減<rt>へ</rt></ruby>らしてくれるように<u>要求</u>した。",
              "target": "要求",
              "options": ["ようきゅ", "よきゅう", "ようきゅう", "よちゅう"],
              "correct_index": 2,
              "answer": "ようきゅう",
              "ruby_html": "<ruby>会社<rt>かいしゃ</rt></ruby>に<ruby>仕事<rt>しごと</rt></ruby>を<ruby>減<rt>へ</rt></ruby>らしてくれるように<ruby>要求<rt>ようきゅう</rt></ruby>した。",
              "translation": "I demanded that the company reduce my workload.",
              "explanation": "要求（ようきゅう）は両方とも長音です。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome7_2",
          "number": 2,
          "type": "multiple_choice",
          "instruction_ja": "＿＿の言葉を漢字で書くとき、最もよいものを、1・2・3・4から一つ選びましょう。",
          "instruction_en": "Choose the best kanji representation for the underlined word from 1, 2, 3, or 4.",
          "items": [
            {
              "id": "k_ex_matome7_2_1",
              "number": 1,
              "question_ja": "ぼんやりしていて、<ruby>降<rt>お</rt></ruby>りる<ruby>駅<rt>えき</rt></ruby>を<u>まちがえて</u>しまった。",
              "target": "まちがえて",
              "options": ["間遠えて", "間違えて", "間遅えて", "間還えて"],
              "correct_index": 1,
              "answer": "間違えて",
              "ruby_html": "ぼんやりしていて、<ruby>降<rt>お</rt></ruby>りる<ruby>駅<rt>えき</rt></ruby>を<ruby>間違<rt>まちが</rt></ruby>えてしまった。",
              "translation": "I was spacing out and got off at the wrong station by mistake.",
              "explanation": "間違える（まちがえる）は「間」と「違」を使います。"
            },
            {
              "id": "k_ex_matome7_2_2",
              "number": 2,
              "question_ja": "<ruby>頑張<rt>がんば</rt></ruby>ったのに、<ruby>優勝<rt>ゆうしょう</rt></ruby>できなくて<u>ざんねん</u>です。",
              "target": "ざんねん",
              "options": ["残念", "浅念", "浅感", "残感"],
              "correct_index": 0,
              "answer": "残念",
              "ruby_html": "<ruby>頑張<rt>がんば</rt></ruby>ったのに、<ruby>優勝<rt>ゆうしょう</rt></ruby>できなくて<ruby>残念<rt>ざんねん</rt></ruby>です。",
              "translation": "It is regrettable that we couldn't win the championship even though we tried hard.",
              "explanation": "心残りなことは「残念（ざんねん）」と書きます。"
            },
            {
              "id": "k_ex_matome7_2_3",
              "number": 3,
              "question_ja": "この<ruby>町<rt>まち</rt></ruby>の<u>しょくぶつ</u><ruby>園<rt>えん</rt></ruby>では、<ruby>珍<rt>めずら</rt></ruby>しい<ruby>花<rt>はな</rt></ruby>が<ruby>見<rt>み</rt></ruby>られる。",
              "target": "しょくぶつ",
              "options": ["植物", "直物", "食物", "殖物"],
              "correct_index": 0,
              "answer": "植物",
              "ruby_html": "この<ruby>町<rt>まち</rt></ruby>の<ruby>植物園<rt>しょくぶつえん</rt></ruby>では、<ruby>珍<rt>めずら</rt></ruby>しい<ruby>花<rt>はな</rt></ruby>が<ruby>見<rt>み</rt></ruby>られる。",
              "translation": "At this town's botanical garden, you can see rare flowers.",
              "explanation": "草や木などの総称は「植物（しょくぶつ）」です。"
            },
            {
              "id": "k_ex_matome7_2_4",
              "number": 4,
              "question_ja": "<ruby>留学生<rt>りゅうがくせい</rt></ruby>の<u>こうりゅう</u>パーティーに<ruby>参加<rt>さんか</rt></ruby>した。",
              "target": "こうりゅう",
              "options": ["行琉", "交留", "行流", "交流"],
              "correct_index": 3,
              "answer": "交流",
              "ruby_html": "<ruby>留学生<rt>りゅうがくせい</rt></ruby>の<ruby>交流<rt>こうりゅう</rt></ruby>パーティーに<ruby>参加<rt>さんか</rt></ruby>した。",
              "translation": "I participated in an international student exchange party.",
              "explanation": "異なる人や文化が交わることは「交流（こうりゅう）」と書きます。"
            },
            {
              "id": "k_ex_matome7_2_5",
              "number": 5,
              "question_ja": "この<ruby>机<rt>つくえ</rt></ruby>を<ruby>隣<rt>となり</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>へ<u>うつして</u>ください。",
              "target": "うつして",
              "options": ["写して", "移して", "動して", "運して"],
              "correct_index": 1,
              "answer": "移して",
              "ruby_html": "この<ruby>机<rt>つくえ</rt></ruby>を<ruby>隣<rt>となり</rt></ruby>の<ruby>教室<rt>きょうしつ</rt></ruby>へ<ruby>移<rt>うつ</rt></ruby>してください。",
              "translation": "Please move this desk to the classroom next door.",
              "explanation": "場所を変えるときは「移す（うつす）」と書きます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome7_3",
          "number": 3,
          "type": "sentence_completion",
          "instruction_ja": "［量・要・変・慣］から漢字を選んで、文を完成しましょう。読み方も書きましょう。",
          "instruction_en": "Choose a kanji from [量, 要, 変, 慣] to complete each sentence and write the reading of the compound.",
          "choices": ["量", "要", "変", "慣"],
          "items": [
            {
              "id": "k_ex_matome7_3_1",
              "number": 1,
              "sentence": "<ruby>来週<rt>らいしゅう</rt></ruby>までに、【必□】な<ruby>書類<rt>しょるい</rt></ruby>を<ruby>用意<rt>ようい</rt></ruby>しなければならない。",
              "answer": "要",
              "word": "必要",
              "reading": "ひつよう",
              "ruby_html": "<ruby>来週<rt>らいしゅう</rt></ruby>までに、<ruby>必要<rt>ひつよう</rt></ruby>な<ruby>書類<rt>しょるい</rt></ruby>を<ruby>用意<rt>ようい</rt></ruby>しなければならない。",
              "translation": "I must prepare the necessary documents by next week.",
              "explanation": "必要（ひつよう）＝なくてはならないこと。"
            },
            {
              "id": "k_ex_matome7_3_2",
              "number": 2,
              "sentence": "この2<ruby>種類<rt>しゅるい</rt></ruby>の<ruby>薬<rt>くすり</rt></ruby>を<ruby>混<rt>ま</rt></ruby>ぜると、<ruby>化学<rt>かがく</rt></ruby>【□化】を<ruby>起<rt>お</rt></ruby>こす。",
              "answer": "変",
              "word": "変化",
              "reading": "へんか",
              "ruby_html": "この2<ruby>種類<rt>しゅるい</rt></ruby>の<ruby>薬<rt>くすり</rt></ruby>を<ruby>混<rt>ま</rt></ruby>ぜると、<ruby>化学変化<rt>かがくへんか</rt></ruby>を<ruby>起<rt>お</rt></ruby>こす。",
              "translation": "Mixing these two kinds of chemicals causes a chemical reaction/change.",
              "explanation": "変化（へんか）＝性質や状態が変わること。"
            },
            {
              "id": "k_ex_matome7_3_3",
              "number": 3,
              "sentence": "<ruby>病気<rt>びょうき</rt></ruby>の<ruby>予防<rt>よぼう</rt></ruby>には、<ruby>正<rt>ただ</rt></ruby>しい<ruby>生活<rt>せいかつ</rt></ruby>【習□】も<ruby>大事<rt>だいじ</rt></ruby>だ。",
              "answer": "慣",
              "word": "習慣",
              "reading": "しゅうかん",
              "ruby_html": "<ruby>病気<rt>びょうき</rt></ruby>の<ruby>予防<rt>よぼう</rt></ruby>には、<ruby>正<rt>ただ</rt></ruby>しい<ruby>生活習慣<rt>せいかつしゅうかん</rt></ruby>も<ruby>大事<rt>だいじ</rt></ruby>だ。",
              "translation": "Good lifestyle habits are also important for preventing illness.",
              "explanation": "習慣（しゅうかん）＝日常の決まった行い。"
            },
            {
              "id": "k_ex_matome7_3_4",
              "number": 4,
              "sentence": "この<ruby>工場<rt>こうじょう</rt></ruby>は、<ruby>新<rt>あたら</rt></ruby>しい<ruby>機械<rt>きかい</rt></ruby>を<ruby>入<rt>い</rt></ruby>れたので、【大□】<ruby>生産<rt>せいさん</rt></ruby>が<ruby>可能<rt>かのう</rt></ruby>になった。",
              "answer": "量",
              "word": "大量",
              "reading": "たいりょう",
              "ruby_html": "この<ruby>工場<rt>こうじょう</rt></ruby>は、<ruby>新<rt>あたら</rt></ruby>しい<ruby>機械<rt>きかい</rt></ruby>を<ruby>入<rt>い</rt></ruby>れたので、<ruby>大量生産<rt>たいりょうせいさん</rt></ruby>が<ruby>可能<rt>かのう</rt></ruby>になった。",
              "translation": "Since this factory installed new machinery, mass production has become possible.",
              "explanation": "大量（たいりょう）＝非常に多い量。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome7_4",
          "number": 4,
          "type": "reading_recall",
          "instruction_ja": "＿＿の漢字の読み方を書きましょう。",
          "instruction_en": "Write the readings for the underlined words.",
          "items": [
            {
              "id": "k_ex_matome7_4_1a",
              "number": 1,
              "sub": "a",
              "sentence": "a【受験】の<ruby>案内<rt>あんない</rt></ruby>を b【受け取った】。",
              "target": "受験",
              "answer": "じゅけん",
              "reading": "じゅけん",
              "ruby_html": "<ruby>受験<rt>じゅけん</rt></ruby>の<ruby>案内<rt>あんない</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>った。",
              "translation": "I received the examination guide.",
              "explanation": "受験（じゅけん）は音読み、受け取る（うけとる）は訓読みです。"
            },
            {
              "id": "k_ex_matome7_4_1b",
              "number": 1,
              "sub": "b",
              "sentence": "<ruby>受験<rt>じゅけん</rt></ruby>の<ruby>案内<rt>あんない</rt></ruby>を b【受け取った】。",
              "target": "受け取った",
              "answer": "うけとった",
              "reading": "うけとった",
              "ruby_html": "<ruby>受験<rt>じゅけん</rt></ruby>の<ruby>案内<rt>あんない</rt></ruby>を<ruby>受<rt>う</rt></ruby>け<ruby>取<rt>と</rt></ruby>った。",
              "translation": "I received the examination guide.",
              "explanation": "受け取った（うけとった）は訓読みの複合動詞です。"
            },
            {
              "id": "k_ex_matome7_4_2a",
              "number": 2,
              "sub": "a",
              "sentence": "a【流行】に b【流されて】はいけない。",
              "target": "流行",
              "answer": "りゅうこう",
              "reading": "りゅうこう",
              "ruby_html": "<ruby>流行<rt>りゅうこう</rt></ruby>に<ruby>流<rt>なが</rt></ruby>されてはいけない。",
              "translation": "You must not be swept away by trends.",
              "explanation": "流行（りゅうこう）は音読み、流される（ながされる）は訓読みです。"
            },
            {
              "id": "k_ex_matome7_4_2b",
              "number": 2,
              "sub": "b",
              "sentence": "<ruby>流行<rt>りゅうこう</rt></ruby>に b【流されて】はいけない。",
              "target": "流されて",
              "answer": "ながされて",
              "reading": "ながされて",
              "ruby_html": "<ruby>流行<rt>りゅうこう</rt></ruby>に<ruby>流<rt>なが</rt></ruby>されてはいけない。",
              "translation": "You must not be swept away by trends.",
              "explanation": "流される（ながされる）は周囲の影響にそのまま従ってしまうことを表します。"
            },
            {
              "id": "k_ex_matome7_4_3a",
              "number": 3,
              "sub": "a",
              "sentence": "a【正しい】<ruby>情報<rt>じょうほう</rt></ruby>かどうか、b【正確には】<ruby>分<rt>わ</rt></ruby>からなかった。",
              "target": "正しい",
              "answer": "ただしい",
              "reading": "ただしい",
              "ruby_html": "<ruby>正<rt>ただ</rt></ruby>しい<ruby>情報<rt>じょうほう</rt></ruby>かどうか、<ruby>正確<rt>せいかく</rt></ruby>には<ruby>分<rt>わ</rt></ruby>からなかった。",
              "translation": "I could not tell for sure whether it was accurate information.",
              "explanation": "正しい（ただしい）は訓読み、正確（せいかく）は音読みです。"
            },
            {
              "id": "k_ex_matome7_4_3b",
              "number": 3,
              "sub": "b",
              "sentence": "<ruby>正<rt>ただ</rt></ruby>しい<ruby>情報<rt>じょうほう</rt></ruby>かどうか、b【正確には】<ruby>分<rt>わ</rt></ruby>からなかった。",
              "target": "正確には",
              "answer": "せいかくには",
              "reading": "せいかくには",
              "ruby_html": "<ruby>正<rt>ただ</rt></ruby>しい<ruby>情報<rt>じょうほう</rt></ruby>かどうか、<ruby>正確<rt>せいかく</rt></ruby>には<ruby>分<rt>わ</rt></ruby>からなかった。",
              "translation": "I could not tell for sure whether it was accurate information.",
              "explanation": "正確には（せいかくには）は「厳密に言うと」という意味でも使われます。"
            }
          ]
        },
        {
          "exercise_id": "k_ex_matome7_5",
          "number": 5,
          "type": "onyomi_grouping",
          "instruction_ja": "音読みが同じ漢字を選んで□に書きましょう。カッコには音読みを書きましょう。",
          "instruction_en": "Select kanji with the same onyomi from the pool and write their shared onyomi reading.",
          "choices_pool": ["曜", "求", "医", "以", "球", "注", "移", "法", "報", "違", "用", "方", "防", "要", "訪", "洋", "級", "休"],
          "items": [
            {
              "id": "k_ex_matome7_5_1",
              "number": 1,
              "prompt": "音読みが「イ」の漢字（4つ）",
              "answers": ["医", "以", "移", "違"],
              "reading": "イ",
              "explanation": "「医（医療）」「以（以外）」「移（移動）」「違（違反）」の音読みはすべて「イ」です。"
            },
            {
              "id": "k_ex_matome7_5_2",
              "number": 2,
              "prompt": "音読みが「ヨウ」の漢字（4つ）",
              "answers": ["曜", "用", "要", "洋"],
              "reading": "ヨウ",
              "explanation": "「曜（曜日）」「用（用意）」「要（必要）」「洋（洋服）」の音読みはすべて「ヨウ」です。"
            },
            {
              "id": "k_ex_matome7_5_3",
              "number": 3,
              "prompt": "音読みが「キュウ」の漢字（4つ）",
              "answers": ["求", "球", "級", "休"],
              "reading": "キュウ",
              "explanation": "「求（要求）」「球（地球）」「級（上級）」「休（休日）」の音読みはすべて「キュウ」です。"
            },
            {
              "id": "k_ex_matome7_5_4",
              "number": 4,
              "prompt": "音読みが「ホウ」の漢字（4つ）",
              "answers": ["法", "報", "方", "訪"],
              "reading": "ホウ",
              "explanation": "「法（方法）」「報（情報）」「方（方向）」「訪（訪問）」の音読みはすべて「ホウ」です（注＝チュウ、防＝ボウ）。"
            }
          ]
        }
      ]
    }
  ]
}

out_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "kanji", "exercises_part4.json")
out_path = os.path.abspath(out_path)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

total_items = sum(len(ex["items"]) for lesson in data["lessons"] for ex in lesson["exercises"])
print(f"Wrote {out_path} successfully with {len(data['lessons'])} lesson sections and {total_items} total exercise items.")
