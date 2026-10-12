import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def rb(base: str, rt: str) -> str:
    return f"<ruby>{base}<rt>{rt}</rt></ruby>"


def item_rw(
    item_id: str,
    target_kanji: str,
    target_word: str,
    reading: str,
    q_ja: str,
    q_en: str,
    ruby_html: str,
    answer: str,
    acceptable: list[str],
    explanation: str,
) -> dict:
    return {
        "id": item_id,
        "target_kanji": target_kanji,
        "target_word": target_word,
        "reading": reading,
        "question_ja": q_ja,
        "question_en": q_en,
        "ruby_html": ruby_html,
        "answer": answer,
        "acceptable_answers": acceptable,
        "explanation": explanation,
    }


def item_mc(
    item_id: str,
    target_kanji: str,
    target_word: str,
    reading: str,
    q_ja: str,
    q_en: str,
    ruby_html: str,
    options: list[dict],
    answer: str,
    explanation: str,
) -> dict:
    return {
        "id": item_id,
        "target_kanji": target_kanji,
        "target_word": target_word,
        "reading": reading,
        "question_ja": q_ja,
        "question_en": q_en,
        "ruby_html": ruby_html,
        "options": options,
        "answer": answer,
        "explanation": explanation,
    }


def build_data() -> dict:
    lessons = [
        # =====================================================================
        # LESSON 21: 第21回 二つ以上の訓読みを覚える漢字 (pp. 90-92)
        # =====================================================================
        {
            "lesson_id": 21,
            "title_ja": "第21回 二つ以上の訓読みを覚える漢字",
            "title_en": "Lesson 21: Kanji with Two or More Kun-readings",
            "page_range": "90-92",
            "target_kanji": ["上", "生", "空", "夜", "彼", "細", "冷", "汚", "転", "遅", "閉", "割", "覚", "降"],
            "exercises": [
                {
                    "exercise_id": "k_ex_21_1",
                    "type": "reading_recall",
                    "title_ja": "1. 絵を見て、読み方を書きましょう。",
                    "title_en": "1. Look at the pictures and write the readings.",
                    "items": [
                        item_rw(
                            "k_ex_21_1_1", "降", "降りる", "おりる",
                            "① バスを a. <u>降りる</u>。雨が降っている。",
                            "Get off the bus. It is raining.",
                            f"① バスを a. <u>{rb('降', 'お')}りる</u>。{rb('雨', 'あめ')}が{rb('降', 'ふ')}っている。",
                            "おりる", ["おりる", "降りる"],
                            "「降りる（おりる）」means to get off a vehicle or descend."
                        ),
                        item_rw(
                            "k_ex_21_1_2", "降", "降って", "ふって",
                            "① バスを降りる。雨が b. <u>降って</u>いる。",
                            "Get off the bus. It is raining.",
                            f"① バスを{rb('降', 'お')}りる。{rb('雨', 'あめ')}が b. <u>{rb('降', 'ふ')}って</u>いる。",
                            "ふって", ["ふって", "ふる", "降って"],
                            "「降る（ふる）」is used for precipitation falling (rain, snow)."
                        ),
                        item_rw(
                            "k_ex_21_1_3", "細", "細い", "ほそい",
                            "② この線は a. <u>細い</u>。細かい字だ。",
                            "This line is thin. The characters are small/detailed.",
                            f"② この{rb('線', 'せん')}は a. <u>{rb('細', 'ほそ')}い</u>。{rb('細', 'こま')}かい{rb('字', 'じ')}だ。",
                            "ほそい", ["ほそい", "細い"],
                            "「細い（ほそい）」means thin or slender in width."
                        ),
                        item_rw(
                            "k_ex_21_1_4", "細", "細かい", "こまかい",
                            "② この線は細い。b. <u>細かい</u>字だ。",
                            "This line is thin. The characters are small/fine.",
                            f"② この{rb('線', 'せん')}は{rb('細', 'ほそ')}い。b. <u>{rb('細', 'こま')}かい</u>{rb('字', 'じ')}だ。",
                            "こまかい", ["こまかい", "細かい"],
                            "「細かい（こまかい）」means fine, small, or detailed."
                        ),
                        item_rw(
                            "k_ex_21_1_5", "彼", "彼", "かれ",
                            "③ a. <u>彼</u>と彼女は友達だ。",
                            "He and she are friends.",
                            f"③ a. <u>{rb('彼', 'かれ')}</u>と{rb('彼女', 'かのじょ')}は{rb('友達', 'ともだち')}だ。",
                            "かれ", ["かれ", "彼"],
                            "「彼（かれ）」means he or boyfriend."
                        ),
                        item_rw(
                            "k_ex_21_1_6", "彼", "彼女", "かのじょ",
                            "③ 彼と b. <u>彼女</u>は友達だ。",
                            "He and she are friends.",
                            f"③ {rb('彼', 'かれ')}と b. <u>{rb('彼女', 'かのじょ')}</u>は{rb('友達', 'ともだち')}だ。",
                            "かのじょ", ["かのじょ", "彼女"],
                            "「彼女（かのじょ）」means she or girlfriend."
                        ),
                        item_rw(
                            "k_ex_21_1_7", "冷", "冷ます", "さます",
                            "④ お茶を a. <u>冷ます</u>。ビールを冷やす。",
                            "Let the tea cool down. Chill the beer.",
                            f"④ お{rb('茶', 'ちゃ')}を a. <u>{rb('冷', 'さ')}ます</u>。ビールを{rb('冷', 'ひ')}やす。",
                            "さます", ["さます", "冷ます"],
                            "「冷ます（さます）」means to let something hot cool down to normal temperature."
                        ),
                        item_rw(
                            "k_ex_21_1_8", "冷", "冷やす", "ひやす",
                            "④ お茶を冷ます。ビールを b. <u>冷やす</u>。",
                            "Let the tea cool down. Chill the beer.",
                            f"④ お{rb('茶', 'ちゃ')}を{rb('冷', 'さ')}ます。ビールを b. <u>{rb('冷', 'ひ')}やす</u>。",
                            "ひやす", ["ひやす", "冷やす"],
                            "「冷やす（ひやす）」means to chill or make cold (e.g., in a refrigerator)."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_21_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct option.",
                    "items": [
                        item_mc(
                            "k_ex_21_2_1", "細", "細長い", "ほそながい",
                            "① プレゼントは<u>細長い</u>（ a ほそながい　b こまながい ）箱に入っていた。",
                            "The present was in a long, thin box.",
                            f"① プレゼントは<u>{rb('細長', 'ほそなが')}い</u>{rb('箱', 'はこ')}に{rb('入', 'はい')}っていた。",
                            [{"id": "1", "text": "ほそながい"}, {"id": "2", "text": "こまながい"}],
                            "1",
                            "「細長い（ほそながい）」means long and narrow/slender."
                        ),
                        item_mc(
                            "k_ex_21_2_2", "閉", "閉じて", "とじて",
                            "② 父は目を<u>閉じて</u>（ a とじて　b しめて ）考えていた。",
                            "My father was thinking with his eyes closed.",
                            f"② {rb('父', 'ちち')}は{rb('目', 'め')}を<u>{rb('閉', 'と')}じて</u>{rb('考', 'かんが')}えていた。",
                            [{"id": "1", "text": "とじて"}, {"id": "2", "text": "しめて"}],
                            "1",
                            "For eyes, books, or umbrellas, 「閉じる（とじる）」is used."
                        ),
                        item_mc(
                            "k_ex_21_2_3", "空", "空いて", "あいて",
                            "③ 込んでいますね。<u>あいて</u>（ a 開いて　b 空いて ）いる席はあるでしょうか。",
                            "It's crowded, isn't it? I wonder if there are any vacant seats.",
                            f"③ {rb('込', 'こ')}んでいますね。<u>{rb('空', 'あ')}いて</u>いる{rb('席', 'せき')}はあるでしょうか。",
                            [{"id": "1", "text": "開いて"}, {"id": "2", "text": "空いて"}],
                            "2",
                            "「空いている（あいている）」is used for vacant seats, rooms, or free time."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_21_3",
                    "type": "radical_assembly",
                    "title_ja": "3. 漢字の部分を入れて、漢字を完成しましょう。読み方も書きましょう。",
                    "title_en": "3. Combine the parts to complete the kanji and write the reading.",
                    "items": [
                        item_rw(
                            "k_ex_21_3_1", "遅", "遅い", "おそい",
                            "① もう夜（ 辶 ＋ 犀 ＝ ？ ）いですから、車で送りましょうか。",
                            "Since it's already late at night, shall I drive you home?",
                            f"① もう{rb('夜', 'よる')}<u>{rb('遅', 'おそ')}</u>いですから、{rb('車', 'くるま')}で{rb('送', 'おく')}りましょうか。",
                            "遅（おそ）", ["遅", "おそい", "おそ", "遅い"],
                            "辶 + 犀 = 遅. 「夜遅い（よるおそい）」means late at night."
                        ),
                        item_rw(
                            "k_ex_21_3_2", "汚", "汚い", "きたない",
                            "② 掃除をしていないので、部屋が（ 氵 ＋ 夸 ＝ ？ ）い。",
                            "Because I haven't cleaned, the room is dirty.",
                            f"② {rb('掃除', 'そうじ')}をしていないので、{rb('部屋', 'へや')}が<u>{rb('汚', 'きたな')}</u>い。",
                            "汚（きたな）", ["汚", "きたない", "きたな", "汚い"],
                            "氵 + 夸 = 汚. 「汚い（きたない）」means dirty or messy."
                        ),
                        item_rw(
                            "k_ex_21_3_3", "転", "転がって", "ころがって",
                            "③ 打ったボールは、彼女の方に（ 車 ＋ 云 ＝ ？ ）がっていった。",
                            "The hit ball rolled toward her.",
                            f"③ {rb('打', 'う')}ったボールは、{rb('彼女', 'かのじょ')}の{rb('方', 'ほう')}に<u>{rb('転', 'ころ')}</u>がっていった。",
                            "転（ころ）", ["転", "ころがって", "ころ", "転がって"],
                            "車 + 云 = 転. 「転がる（ころがる）」means to roll."
                        ),
                        item_rw(
                            "k_ex_21_3_4", "閉", "閉めて", "しめて",
                            "④ 風が強いから、窓を（ 門 ＋ 才 ＝ ？ ）めてください。",
                            "Because the wind is strong, please close the window.",
                            f"④ {rb('風', 'かぜ')}が{rb('強', 'つよ')}いから、{rb('窓', 'まど')}を<u>{rb('閉', 'し')}</u>めてください。",
                            "閉（し）", ["閉", "しめて", "し", "閉めて"],
                            "門 + 才 = 閉. 「窓を閉める（まどをしめる）」means to close the window."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_21_4",
                    "type": "reading_writing",
                    "title_ja": "4. 下線の部分の漢字の読み方を書きましょう。",
                    "title_en": "4. Write the readings of the underlined kanji.",
                    "items": [
                        item_rw(
                            "k_ex_21_4_1", "夜", "今夜", "こんや",
                            "① a. <u>今夜</u>頑張れば、仕事は明日の夜中には終わるでしょう。",
                            "If I work hard tonight, the work will probably finish by midnight tomorrow.",
                            f"① a. <u>{rb('今夜', 'こんや')}</u>{rb('頑張', 'がんば')}れば、{rb('仕事', 'しごと')}は{rb('明日', 'あした')}の{rb('夜中', 'よなか')}には{rb('終', 'お')}わるでしょう。",
                            "こんや", ["こんや", "今夜"],
                            "「今夜（こんや）」uses the on-reading ヤ."
                        ),
                        item_rw(
                            "k_ex_21_4_2", "夜", "夜中", "よなか",
                            "① 今夜頑張れば、仕事は明日の b. <u>夜中</u>には終わるでしょう。",
                            "If I work hard tonight, the work will probably finish by midnight tomorrow.",
                            f"① {rb('今夜', 'こんや')}{rb('頑張', 'がんば')}れば、{rb('仕事', 'しごと')}は{rb('明日', 'あした')}の b. <u>{rb('夜中', 'よなか')}</u>には{rb('終', 'お')}わるでしょう。",
                            "よなか", ["よなか", "夜中"],
                            "「夜中（よなか）」uses the kun-reading よ (middle of the night)."
                        ),
                        item_rw(
                            "k_ex_21_4_3", "上", "上がった", "あがった",
                            "② 気温が a. <u>上がった</u>ので、上着を脱いだ。次の上りの電車は何時ですか。",
                            "Since the temperature rose, I took off my jacket. What time is the next inbound train?",
                            f"② {rb('気温', 'きおん')}が a. <u>{rb('上', 'あ')}がった</u>ので、{rb('上着', 'うわぎ')}を{rb('脱', 'ぬ')}いだ。{rb('次', 'つぎ')}の{rb('上', 'のぼ')}りの{rb('電車', 'でんしゃ')}は{rb('何時', 'なんじ')}ですか。",
                            "あがった", ["あがった", "あがる", "上がった"],
                            "「上がる（あがる）」means to rise or go up."
                        ),
                        item_rw(
                            "k_ex_21_4_4", "上", "上着", "うわぎ",
                            "② 気温が上がったので、b. <u>上着</u>を脱いだ。次の上りの電車は何時ですか。",
                            "Since the temperature rose, I took off my jacket. What time is the next inbound train?",
                            f"② {rb('気温', 'きおん')}が{rb('上', 'あ')}がったので、b. <u>{rb('上着', 'うわぎ')}</u>を{rb('脱', 'ぬ')}いだ。{rb('次', 'つぎ')}の{rb('上', 'のぼ')}りの{rb('電車', 'でんしゃ')}は{rb('何時', 'なんじ')}ですか。",
                            "うわぎ", ["うわぎ", "上着"],
                            "「上着（うわぎ）」uses the kun-reading うわ (outerwear/jacket)."
                        ),
                        item_rw(
                            "k_ex_21_4_5", "上", "上り", "のぼり",
                            "② 気温が上がったので、上着を脱いだ。次の c. <u>上り</u>の電車は何時ですか。",
                            "Since the temperature rose, I took off my jacket. What time is the next inbound train?",
                            f"② {rb('気温', 'きおん')}が{rb('上', 'あ')}がったので、{rb('上着', 'うわぎ')}を{rb('脱', 'ぬ')}いだ。{rb('次', 'つぎ')}の c. <u>{rb('上', 'のぼ')}り</u>の{rb('電車', 'でんしゃ')}は{rb('何時', 'なんじ')}ですか。",
                            "のぼり", ["のぼり", "上り"],
                            "「上り（のぼり）」means going up or an inbound train heading toward the capital."
                        ),
                        item_rw(
                            "k_ex_21_4_6", "空", "空", "そら",
                            "③ きれいな鳥が、a. <u>空</u>を飛んでいる。箱の中は空だった。",
                            "A beautiful bird is flying in the sky. The inside of the box was empty.",
                            f"③ きれいな{rb('鳥', 'とり')}が、a. <u>{rb('空', 'そら')}</u>を{rb('飛', 'と')}んでいる。{rb('箱', 'はこ')}の{rb('中', 'なか')}は{rb('空', 'から')}だった。",
                            "そら", ["そら", "空"],
                            "「空（そら）」means sky."
                        ),
                        item_rw(
                            "k_ex_21_4_7", "空", "空", "から",
                            "③ きれいな鳥が、空を飛んでいる。箱の中は b. <u>空</u>だった。",
                            "A beautiful bird is flying in the sky. The inside of the box was empty.",
                            f"③ きれいな{rb('鳥', 'とり')}が、{rb('空', 'そら')}を{rb('飛', 'と')}んでいる。{rb('箱', 'はこ')}の{rb('中', 'なか')}は b. <u>{rb('空', 'から')}</u>だった。",
                            "から", ["から", "空"],
                            "「空（から）」means empty."
                        ),
                        item_rw(
                            "k_ex_21_4_8", "生", "高校生", "こうこうせい",
                            "④ 私は a. <u>高校生</u>になるまで、生の魚が食べられなかった。生きている魚を思い出すからだ。",
                            "Until I became a high school student, I couldn't eat raw fish because it reminded me of living fish.",
                            f"④ {rb('私', 'わたし')}は a. <u>{rb('高校生', 'こうこうせい')}</u>になるまで、{rb('生', 'なま')}の{rb('魚', 'さかな')}が{rb('食', 'た')}べられなかった。{rb('生', 'い')}きている{rb('魚', 'さかな')}を{rb('思', 'おも')}い{rb('出', 'だ')}すからだ。",
                            "こうこうせい", ["こうこうせい", "高校生"],
                            "「高校生（こうこうせい）」uses the on-reading セイ."
                        ),
                        item_rw(
                            "k_ex_21_4_9", "生", "生", "なま",
                            "④ 私は高校生になるまで、b. <u>生</u>の魚が食べられなかった。生きている魚を思い出すからだ。",
                            "Until I became a high school student, I couldn't eat raw fish because it reminded me of living fish.",
                            f"④ {rb('私', 'わたし')}は{rb('高校生', 'こうこうせい')}になるまで、b. <u>{rb('生', 'なま')}</u>の{rb('魚', 'さかな')}が{rb('食', 'た')}べられなかった。{rb('生', 'い')}きている{rb('魚', 'さかな')}を{rb('思', 'おも')}い{rb('出', 'だ')}すからだ。",
                            "なま", ["なま", "生"],
                            "「生（なま）」means raw or fresh."
                        ),
                        item_rw(
                            "k_ex_21_4_10", "生", "生きて", "いきて",
                            "④ 私は高校生になるまで、生の魚が食べられなかった。c. <u>生きて</u>いる魚を思い出すからだ。",
                            "Until I became a high school student, I couldn't eat raw fish because it reminded me of living fish.",
                            f"④ {rb('私', 'わたし')}は{rb('高校生', 'こうこうせい')}になるまで、{rb('生', 'なま')}の{rb('魚', 'さかな')}が{rb('食', 'た')}べられなかった。c. <u>{rb('生', 'い')}きて</u>いる{rb('魚', 'さかな')}を{rb('思', 'おも')}い{rb('出', 'だ')}すからだ。",
                            "いきて", ["いきて", "いきる", "生きて"],
                            "「生きる（いきる）」means to live."
                        ),
                        item_rw(
                            "k_ex_21_4_11", "割", "割引", "わりびき",
                            "⑤ a. <u>割引</u>で買ったお皿が割れてしまった。",
                            "The plate I bought at a discount broke.",
                            f"⑤ a. <u>{rb('割引', 'わりびき')}</u>で{rb('買', 'か')}ったお{rb('皿', 'さら')}が{rb('割', 'わ')}れてしまった。",
                            "わりびき", ["わりびき", "割引"],
                            "「割引（わりびき）」means discount."
                        ),
                        item_rw(
                            "k_ex_21_4_12", "割", "割れて", "われて",
                            "⑤ 割引で買ったお皿が b. <u>割れて</u>しまった。",
                            "The plate I bought at a discount broke.",
                            f"⑤ {rb('割引', 'わりびき')}で{rb('買', 'か')}ったお{rb('皿', 'さら')}が b. <u>{rb('割', 'わ')}れて</u>しまった。",
                            "われて", ["われて", "われる", "割れて"],
                            "「割れる（われる）」means to break or smash."
                        ),
                        item_rw(
                            "k_ex_21_4_13", "覚", "覚めても", "さめても",
                            "⑥ 怖い夢だった。目が a. <u>覚めても</u>、はっきり覚えている。",
                            "It was a scary dream. Even after waking up, I clearly remember it.",
                            f"⑥ {rb('怖', 'こわ')}い{rb('夢', 'ゆめ')}だった。{rb('目', 'め')}が a. <u>{rb('覚', 'さ')}めても</u>、はっきり{rb('覚', 'おぼ')}えている。",
                            "さめても", ["さめても", "さめる", "覚めても"],
                            "「目が覚める（めがさめる）」means to wake up."
                        ),
                        item_rw(
                            "k_ex_21_4_14", "覚", "覚えて", "おぼえて",
                            "⑥ 怖い夢だった。目が覚めても、はっきり b. <u>覚えて</u>いる。",
                            "It was a scary dream. Even after waking up, I clearly remember it.",
                            f"⑥ {rb('怖', 'こわ')}い{rb('夢', 'ゆめ')}だった。{rb('目', 'め')}が{rb('覚', 'さ')}めても、はっきり b. <u>{rb('覚', 'おぼ')}えて</u>いる。",
                            "おぼえて", ["おぼえて", "おぼえる", "覚えて"],
                            "「覚える（おぼえる）」means to remember or memorize."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_21_5",
                    "type": "word_pairing",
                    "title_ja": "5. □には同じ漢字が入ります。[転、遅、汚、生、冷] から、漢字を選んで書きましょう。下線の部分の読み方も書きましょう。",
                    "title_en": "5. Fill in the blanks with the same kanji from [転, 遅, 汚, 生, 冷] and write the readings.",
                    "items": [
                        item_rw(
                            "k_ex_21_5_1", "生", "生まれた", "うまれた",
                            "① 去年 a. <u>[ 　 ]まれた</u>赤ちゃんに、歯が生えてきた。",
                            "Teeth have started growing in the baby born last year.",
                            f"① {rb('去年', 'きょねん')} a. <u>{rb('生', 'う')}まれた</u>{rb('赤', 'あか')}ちゃんに、{rb('歯', 'は')}が{rb('生', 'は')}えてきた。",
                            "生（うまれた）", ["生", "うまれた", "生まれた"],
                            "「生まれる（うまれる）」means to be born."
                        ),
                        item_rw(
                            "k_ex_21_5_2", "生", "生えて", "はえて",
                            "① 去年生まれた赤ちゃんに、歯が b. <u>[ 　 ]えて</u>きた。",
                            "Teeth have started growing in the baby born last year.",
                            f"① {rb('去年', 'きょねん')}{rb('生', 'う')}まれた{rb('赤', 'あか')}ちゃんに、{rb('歯', 'は')}が b. <u>{rb('生', 'は')}えて</u>きた。",
                            "生（はえて）", ["生", "はえて", "生えて"],
                            "「生える（はえる）」means to grow or sprout (teeth, hair, grass)."
                        ),
                        item_rw(
                            "k_ex_21_5_3", "汚", "汚れて", "よごれて",
                            "② 外で遊んで帰ってきた子供の手と足は、a. <u>[ 　 ]れて</u>汚くなっていた。",
                            "The hands and feet of the child who came back from playing outside had gotten stained and dirty.",
                            f"② {rb('外', 'そと')}で{rb('遊', 'あそ')}んで{rb('帰', 'かえ')}ってきた{rb('子供', 'こども')}の{rb('手', 'て')}と{rb('足', 'あし')}は、a. <u>{rb('汚', 'よご')}れて</u>{rb('汚', 'きたな')}くなっていた。",
                            "汚（よごれて）", ["汚", "よごれて", "汚れて"],
                            "「汚れる（よごれる）」means to become dirty."
                        ),
                        item_rw(
                            "k_ex_21_5_4", "汚", "汚く", "きたなく",
                            "② 外で遊んで帰ってきた子供の手と足は、汚れて b. <u>[ 　 ]く</u>なっていた。",
                            "The hands and feet of the child who came back from playing outside had gotten stained and dirty.",
                            f"② {rb('外', 'そと')}で{rb('遊', 'あそ')}んで{rb('帰', 'かえ')}ってきた{rb('子供', 'こども')}の{rb('手', 'て')}と{rb('足', 'あし')}は、{rb('汚', 'よご')}れて b. <u>{rb('汚', 'きたな')}く</u>なっていた。",
                            "汚（きたなく）", ["汚", "きたなく", "汚く"],
                            "「汚い（きたない）」adverbial form is 「汚く（きたなく）」."
                        ),
                        item_rw(
                            "k_ex_21_5_5", "冷", "冷たい", "つめたい",
                            "③ この料理は a. <u>[ 　 ]たい</u>ほうがおいしいので、よく冷やしてください。",
                            "Since this dish tastes better cold, please chill it well.",
                            f"③ この{rb('料理', 'りょうり')}は a. <u>{rb('冷', 'つめ')}たい</u>ほうがおいしいので、よく{rb('冷', 'ひ')}やしてください。",
                            "冷（つめたい）", ["冷", "つめたい", "冷たい"],
                            "「冷たい（つめたい）」means cold to the touch or taste."
                        ),
                        item_rw(
                            "k_ex_21_5_6", "冷", "冷やして", "ひやして",
                            "③ この料理は冷たいほうがおいしいので、よく b. <u>[ 　 ]やして</u>ください。",
                            "Since this dish tastes better cold, please chill it well.",
                            f"③ この{rb('料理', 'りょうり')}は{rb('冷', 'つめ')}たいほうがおいしいので、よく b. <u>{rb('冷', 'ひ')}やして</u>ください。",
                            "冷（ひやして）", ["冷", "ひやして", "冷やして"],
                            "「冷やす（ひやす）」means to chill."
                        ),
                        item_rw(
                            "k_ex_21_5_7", "転", "自転車", "じてんしゃ",
                            "④ a. <u>自[ 　 ]車</u>に乗っていて、転んでしまった。",
                            "While riding a bicycle, I fell down.",
                            f"④ a. <u>{rb('自転車', 'じてんしゃ')}</u>に{rb('乗', 'の')}っていて、{rb('転', 'ころ')}んでしまった。",
                            "転（じてんしゃ）", ["転", "じてんしゃ", "自転車"],
                            "「自転車（じてんしゃ）」means bicycle."
                        ),
                        item_rw(
                            "k_ex_21_5_8", "転", "転んで", "ころんで",
                            "④ 自転車に乗っていて、b. <u>[ 　 ]んで</u>しまった。",
                            "While riding a bicycle, I fell down.",
                            f"④ {rb('自転車', 'じてんしゃ')}に{rb('乗', 'の')}っていて、b. <u>{rb('転', 'ころ')}んで</u>しまった。",
                            "転（ころんで）", ["転", "ころんで", "転んで"],
                            "「転ぶ（ころぶ）」means to fall down or tumble."
                        ),
                        item_rw(
                            "k_ex_21_5_9", "遅", "遅い", "おそい",
                            "⑤ A：「約束の時間を30分過ぎていますよ。山下さん、a. <u>[ 　 ]い</u>ですね。」",
                            "A: 'It's 30 minutes past the promised time. Yamashita-san is late, isn't he?'",
                            f"⑤ A：「{rb('約束', 'やくそく')}の{rb('時間', 'じかん')}を30{rb('分', 'ぷん')}{rb('過', 'す')}ぎていますよ。{rb('山下', 'やました')}さん、a. <u>{rb('遅', 'おそ')}い</u>ですね。」",
                            "遅（おそい）", ["遅", "おそい", "遅い"],
                            "「遅い（おそい）」means late or slow."
                        ),
                        item_rw(
                            "k_ex_21_5_10", "遅", "遅れて", "おくれて",
                            "⑤ B：「事故で電車が b. <u>[ 　 ]れて</u>いるらしいですよ。」",
                            "B: 'I hear the train is delayed due to an accident.'",
                            f"⑤ B：「{rb('事故', 'じこ')}で{rb('電車', 'でんしゃ')}が b. <u>{rb('遅', 'おく')}れて</u>いるらしいですよ。」",
                            "遅（おくれて）", ["遅", "おくれて", "遅れて"],
                            "「遅れる（おくれる）」means to be delayed or late."
                        ),
                    ],
                },
            ],
        },
        # =====================================================================
        # LESSON 22: 第22回 二つめの音読みを覚える漢字 (pp. 94-95)
        # =====================================================================
        {
            "lesson_id": 22,
            "title_ja": "第22回 二つめの音読みを覚える漢字",
            "title_en": "Lesson 22: Kanji with a Second On-reading",
            "page_range": "94-95",
            "target_kanji": ["日", "男", "自", "去", "工", "間", "文", "作", "物", "便", "楽"],
            "exercises": [
                {
                    "exercise_id": "k_ex_22_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の漢字の読み方が同じものを線で結びましょう。読み方も書きましょう。",
                    "title_en": "1. Match the words with the same kanji reading and write the readings.",
                    "items": [
                        item_rw(
                            "k_ex_22_1_1", "便", "郵便局・宅配便", "ゆうびんきょく・たくはいびん",
                            "① a. 郵<u>便</u>局 ―― b. 宅配<u>便</u>",
                            "Post office — Home delivery service (both read ビン)",
                            f"① a. {rb('郵便局', 'ゆうびんきょく')} ―― b. {rb('宅配便', 'たくはいびん')}",
                            "ゆうびんきょく・たくはいびん", ["ゆうびんきょく", "たくはいびん", "びん", "ゆうびんきょく・たくはいびん"],
                            "When 「便」means mail or flight/service, it is read ビン."
                        ),
                        item_rw(
                            "k_ex_22_1_2", "便", "便利・不便", "べんり・ふべん",
                            "① c. <u>便</u>利 ―― d. 不<u>便</u>",
                            "Convenient — Inconvenient (both read ベン)",
                            f"① c. {rb('便利', 'べんり')} ―― d. {rb('不便', 'ふべん')}",
                            "べんり・ふべん", ["べんり", "ふべん", "べん", "べんり・ふべん"],
                            "When 「便」means convenience, it is read ベン."
                        ),
                        item_rw(
                            "k_ex_22_1_3", "工", "工場・工業", "こうじょう・こうぎょう",
                            "② a. <u>工</u>場 ―― d. <u>工</u>業",
                            "Factory — Manufacturing industry (both read コウ)",
                            f"② a. {rb('工場', 'こうじょう')} ―― d. {rb('工業', 'こうぎょう')}",
                            "こうじょう・こうぎょう", ["こうじょう", "こうぎょう", "こう", "こうじょう・こうぎょう"],
                            "In 「工場（こうじょう）」and 「工業（こうぎょう）」, 工 is read コウ."
                        ),
                        item_rw(
                            "k_ex_22_1_4", "工", "大工・工夫", "だいく・くふう",
                            "② c. 大<u>工</u> ―― b. <u>工</u>夫",
                            "Carpenter — Device/ingenuity (both read ク)",
                            f"② c. {rb('大工', 'だいく')} ―― b. {rb('工夫', 'くふう')}",
                            "だいく・くふう", ["だいく", "くふう", "く", "だいく・くふう"],
                            "In 「大工（だいく）」and 「工夫（くふう）」, 工 is read ク."
                        ),
                        item_rw(
                            "k_ex_22_1_5", "日", "日曜日・日時", "にちようび・にちじ",
                            "③ a. <u>日</u>曜日 ―― d. <u>日</u>時",
                            "Sunday — Date and time (both read ニチ)",
                            f"③ a. {rb('日曜日', 'にちようび')} ―― d. {rb('日時', 'にちじ')}",
                            "にちようび・にちじ", ["にちようび", "にちじ", "にち", "にちようび・にちじ"],
                            "In 「日曜日（にちようび）」and 「日時（にちじ）」, 日 is read ニチ."
                        ),
                        item_rw(
                            "k_ex_22_1_6", "日", "先日・平日", "せんじつ・へいじつ",
                            "③ c. 先<u>日</u> ―― b. 平<u>日</u>",
                            "The other day — Weekday (both read ジツ)",
                            f"③ c. {rb('先日', 'せんじつ')} ―― b. {rb('平日', 'へいじつ')}",
                            "せんじつ・へいじつ", ["せんじつ", "へいじつ", "じつ", "せんじつ・へいじつ"],
                            "In 「先日（せんじつ）」and 「平日（へいじつ）」, 日 is read ジツ."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_22_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct reading.",
                    "items": [
                        item_mc(
                            "k_ex_22_2_1", "日", "本日", "ほんじつ",
                            "① <u>本日</u>（ a ほんにち　b ほんじつ ）はお忙しい中、お集まりくださいまして、ありがとうございます。",
                            "Thank you very much for gathering today despite your busy schedules.",
                            f"① <u>{rb('本日', 'ほんじつ')}</u>はお{rb('忙', 'いそが')}しい{rb('中', 'なか')}、お{rb('集', 'あつ')}まりくださいまして、ありがとうございます。",
                            [{"id": "1", "text": "ほんにち"}, {"id": "2", "text": "ほんじつ"}],
                            "2",
                            "「本日（ほんじつ）」is formal for 'today'."
                        ),
                        item_mc(
                            "k_ex_22_2_2", "去", "過去", "かこ",
                            "② <u>過去</u>（ a かきょ　b かっきょ　c かこ ）の嫌な思い出は、話したくない。",
                            "I don't want to talk about unpleasant memories of the past.",
                            f"② <u>{rb('過去', 'かこ')}</u>の{rb('嫌', 'いや')}な{rb('思', 'おも')}い{rb('出', 'で')}は、{rb('話', 'はな')}したくない。",
                            [{"id": "1", "text": "かきょ"}, {"id": "2", "text": "かっきょ"}, {"id": "3", "text": "かこ"}],
                            "3",
                            "「過去（かこ）」means the past (去 is read コ here, unlike 去年 きょねん)."
                        ),
                        item_mc(
                            "k_ex_22_2_3", "作", "副作用", "ふくさよう",
                            "③ この薬は、眠くなるという<u>副作用</u>（ a ふくさくよう　b ふくさよう　c ふくっさよう ）がある。",
                            "This medicine has a side effect of making you sleepy.",
                            f"③ この{rb('薬', 'くすり')}は、{rb('眠', 'ねむ')}くなるという<u>{rb('副作用', 'ふくさよう')}</u>がある。",
                            [{"id": "1", "text": "ふくさくよう"}, {"id": "2", "text": "ふくさよう"}, {"id": "3", "text": "ふくっさよう"}],
                            "2",
                            "「作用（さよう）」and 「副作用（ふくさよう）」use the on-reading サ for 作."
                        ),
                        item_mc(
                            "k_ex_22_2_4", "男", "次男", "じなん",
                            "④ <u>次男</u>（ a じだん　b じなん ）は野菜が嫌いだ。",
                            "My second son dislikes vegetables.",
                            f"④ <u>{rb('次男', 'じなん')}</u>は{rb('野菜', 'やさい')}が{rb('嫌', 'きら')}いだ。",
                            [{"id": "1", "text": "じだん"}, {"id": "2", "text": "じなん"}],
                            "2",
                            "In birth order words like 「長男（ちょうなん）」and 「次男（じなん）」, 男 is read ナン."
                        ),
                        item_mc(
                            "k_ex_22_2_5", "文", "文字", "もじ",
                            "⑤ 日本語には、<u>文字</u>（ a もじ　b ぶんじ ）が3種類ある。",
                            "In Japanese, there are three types of characters/scripts.",
                            f"⑤ {rb('日本語', 'にほんご')}には、<u>{rb('文字', 'もじ')}</u>が3{rb('種類', 'しゅるい')}ある。",
                            [{"id": "1", "text": "もじ"}, {"id": "2", "text": "ぶんじ"}],
                            "1",
                            "「文字（もじ）」means letter or character."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_22_3",
                    "type": "word_pairing",
                    "title_ja": "3. □には同じ漢字が入ります。[文、間、自、物] から、漢字を選んで書きましょう。下線の部分の読み方も書きましょう。",
                    "title_en": "3. Fill in the blanks with the same kanji from [文, 間, 自, 物] and write the readings.",
                    "items": [
                        item_rw(
                            "k_ex_22_3_1", "自", "自分", "じぶん",
                            "① 他の人の考えを気にしないで、a. <u>[ 　 ]分</u>で考えることが大切だ。",
                            "It is important to think for yourself without worrying about what others think.",
                            f"① {rb('他', 'ほか')}の{rb('人', 'ひと')}の{rb('考', 'かんが')}えを{rb('気', 'き')}にしないで、a. <u>{rb('自分', 'じぶん')}</u>で{rb('考', 'かんが')}えることが{rb('大切', 'たいせつ')}だ。",
                            "自（じぶん）", ["自", "じぶん", "自分"],
                            "「自分（じぶん）」uses the on-reading ジ."
                        ),
                        item_rw(
                            "k_ex_22_3_2", "自", "自然", "しぜん",
                            "① きれいな川と山を残すために、b. <u>[ 　 ]然</u>を守る運動をしている。",
                            "In order to preserve clean rivers and mountains, we are campaigning to protect nature.",
                            f"① きれいな{rb('川', 'かわ')}と{rb('山', 'やま')}を{rb('残', 'のこ')}すために、b. <u>{rb('自然', 'しぜん')}</u>を{rb('守', 'まも')}る{rb('運動', 'うんどう')}をしている。",
                            "自（しぜん）", ["自", "しぜん", "自然"],
                            "「自然（しぜん）」uses the on-reading シ."
                        ),
                        item_rw(
                            "k_ex_22_3_3", "物", "見物", "けんぶつ",
                            "② a. <u>見[ 　 ]</u>に行くときは、荷物が少ないほうがいいですよ。",
                            "When going sightseeing, it's better to have less luggage.",
                            f"② a. <u>{rb('見物', 'けんぶつ')}</u>に{rb('行', 'い')}くときは、{rb('荷物', 'にもつ')}が{rb('少', 'すく')}ないほうがいいですよ。",
                            "物（けんぶつ）", ["物", "けんぶつ", "見物"],
                            "「見物（けんぶつ）」uses the on-reading ブツ."
                        ),
                        item_rw(
                            "k_ex_22_3_4", "物", "荷物", "にもつ",
                            "② 見物に行くときは、b. <u>荷[ 　 ]</u>が少ないほうがいいですよ。",
                            "When going sightseeing, it's better to have less luggage.",
                            f"② {rb('見物', 'けんぶつ')}に{rb('行', 'い')}くときは、b. <u>{rb('荷物', 'にもつ')}</u>が{rb('少', 'すく')}ないほうがいいですよ。",
                            "物（にもつ）", ["物", "にもつ", "荷物"],
                            "「荷物（にもつ）」uses the on-reading モツ."
                        ),
                        item_rw(
                            "k_ex_22_3_5", "間", "人間", "にんげん",
                            "③ a. <u>人[ 　 ]</u>が動物と違うのは、火を使うということだ。",
                            "What makes humans different from animals is that they use fire.",
                            f"③ a. <u>{rb('人間', 'にんげん')}</u>が{rb('動物', 'どうぶつ')}と{rb('違', 'ちが')}うのは、{rb('火', 'ひ')}を{rb('使', 'つか')}うということだ。",
                            "間（にんげん）", ["間", "にんげん", "人間"],
                            "「人間（にんげん）」uses the on-reading ゲン."
                        ),
                        item_rw(
                            "k_ex_22_3_6", "間", "期間", "きかん",
                            "③ 工事の b. <u>期[ 　 ]</u>は、10月15日から2週間です。",
                            "The construction period is two weeks starting from October 15.",
                            f"③ {rb('工事', 'こうじ')}の b. <u>{rb('期間', 'きかん')}</u>は、10{rb('月', 'がつ')}15{rb('日', 'にち')}から2{rb('週間', 'しゅうかん')}です。",
                            "間（きかん）", ["間", "きかん", "期間"],
                            "「期間（きかん）」uses the on-reading カン."
                        ),
                        item_rw(
                            "k_ex_22_3_7", "文", "文化", "ぶんか",
                            "④ a. <u>[ 　 ]化</u>が違っても、人は分かり合えると思う。",
                            "Even if cultures differ, I think people can understand each other.",
                            f"④ a. <u>{rb('文化', 'ぶんか')}</u>が{rb('違', 'ちが')}っても、{rb('人', 'ひと')}は{rb('分', 'わ')}かり{rb('合', 'あ')}えると{rb('思', 'おも')}う。",
                            "文（ぶんか）", ["文", "ぶんか", "文化"],
                            "「文化（ぶんか）」uses the on-reading ブン."
                        ),
                        item_rw(
                            "k_ex_22_3_8", "文", "注文", "ちゅうもん",
                            "④ この店は、b. <u>注[ 　 ]</u>を受けてから3分以内に料理を出す。",
                            "This restaurant serves dishes within 3 minutes of receiving an order.",
                            f"④ この{rb('店', 'みせ')}は、b. <u>{rb('注文', 'ちゅうもん')}</u>を{rb('受', 'う')}けてから3{rb('分以内', 'ぷんいない')}に{rb('料理', 'りょうり')}を{rb('出', 'だ')}す。",
                            "文（ちゅうもん）", ["文", "ちゅうもん", "注文"],
                            "「注文（ちゅうもん）」uses the on-reading モン."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_22_4",
                    "type": "reading_writing",
                    "title_ja": "4. 下線の部分の漢字には読み方を、平仮名には漢字を書きましょう。",
                    "title_en": "4. Write the readings for the underlined kanji and kanji for the underlined hiragana.",
                    "items": [
                        item_rw(
                            "k_ex_22_4_1", "楽", "楽", "らく",
                            "① 今の仕事は、決して a. <u>楽</u>ではないが、好きな仕事なので、とても楽しい。",
                            "My current job is by no means easy, but because it's a job I like, it's very enjoyable.",
                            f"① {rb('今', 'いま')}の{rb('仕事', 'しごと')}は、{rb('決', 'けっ')}して a. <u>{rb('楽', 'らく')}</u>ではないが、{rb('好', 'す')}きな{rb('仕事', 'しごと')}なので、とても{rb('楽', 'たの')}しい。",
                            "らく", ["らく", "楽"],
                            "「楽（らく）」means easy or comfortable."
                        ),
                        item_rw(
                            "k_ex_22_4_2", "楽", "楽しい", "たのしい",
                            "① 今の仕事は、決して楽ではないが、好きな仕事なので、とても b. <u>楽しい</u>。",
                            "My current job is by no means easy, but because it's a job I like, it's very enjoyable.",
                            f"① {rb('今', 'いま')}の{rb('仕事', 'しごと')}は、{rb('決', 'けっ')}して{rb('楽', 'らく')}ではないが、{rb('好', 'す')}きな{rb('仕事', 'しごと')}なので、とても b. <u>{rb('楽', 'たの')}しい</u>。",
                            "たのしい", ["たのしい", "楽しい"],
                            "「楽しい（たのしい）」means fun or enjoyable."
                        ),
                        item_rw(
                            "k_ex_22_4_3", "作", "作品", "さくひん",
                            "② この a. <u>作品</u>を作るのには、非常に細かい作業が必要だっただろう。",
                            "Creating this work of art must have required extremely detailed work.",
                            f"② この a. <u>{rb('作品', 'さくひん')}</u>を{rb('作', 'つく')}るのには、{rb('非常', 'ひじょう')}に{rb('細', 'こま')}かい{rb('作業', 'さぎょう')}が{rb('必要', 'ひつよう')}だっただろう。",
                            "さくひん", ["さくひん", "作品"],
                            "「作品（さくひん）」uses the on-reading サク."
                        ),
                        item_rw(
                            "k_ex_22_4_4", "作", "作業", "さぎょう",
                            "② この作品を作るのには、非常に細かい b. <u>作業</u>が必要だっただろう。",
                            "Creating this work of art must have required extremely detailed work.",
                            f"② この{rb('作品', 'さくひん')}を{rb('作', 'つく')}るのには、{rb('非常', 'ひじょう')}に{rb('細', 'こま')}かい b. <u>{rb('作業', 'さぎょう')}</u>が{rb('必要', 'ひつよう')}だっただろう。",
                            "さぎょう", ["さぎょう", "作業"],
                            "「作業（さぎょう）」uses the on-reading サ."
                        ),
                        item_rw(
                            "k_ex_22_4_5", "日", "休日", "きゅうじつ",
                            "③ a. <u>きゅうじつ</u>は、ひあたりのいい部屋で好きな本を読む。",
                            "On holidays, I read my favorite books in a sunny room.",
                            f"③ a. <u>{rb('休日', 'きゅうじつ')}</u>は、{rb('日当', 'ひあ')}たりのいい{rb('部屋', 'へや')}で{rb('好', 'す')}きな{rb('本', 'ほん')}を{rb('読', 'よ')}む。",
                            "休日", ["休日", "きゅうじつ"],
                            "「休日（きゅうじつ）」means holiday or day off."
                        ),
                        item_rw(
                            "k_ex_22_4_6", "日", "日当たり", "ひあたり",
                            "③ きゅうじつは、b. <u>ひあたり</u>のいい部屋で好きな本を読む。",
                            "On holidays, I read my favorite books in a sunny room.",
                            f"③ {rb('休日', 'きゅうじつ')}は、b. <u>{rb('日当', 'ひあ')}たり</u>のいい{rb('部屋', 'へや')}で{rb('好', 'す')}きな{rb('本', 'ほん')}を{rb('読', 'よ')}む。",
                            "日当たり", ["日当たり", "ひあたり"],
                            "「日当たり（ひあたり）」means exposure to the sun."
                        ),
                    ],
                },
            ],
        },
        # =====================================================================
        # LESSON 23: 第23回 二つの音読みを覚える新しい漢字 (pp. 96-97)
        # =====================================================================
        {
            "lesson_id": 23,
            "title_ja": "第23回 二つの音読みを覚える新しい漢字",
            "title_en": "Lesson 23: New Kanji with Two On-readings",
            "page_range": "96-97",
            "target_kanji": ["由", "再", "判", "定", "券", "則", "規", "評"],
            "exercises": [
                {
                    "exercise_id": "k_ex_23_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。",
                    "title_en": "1. Write the readings of the underlined words.",
                    "items": [
                        item_rw(
                            "k_ex_23_1_1", "再", "再来週", "さらいしゅう",
                            "① テストの点が59点以下だった人は、a. <u>再来週</u>、再試験を受けてください。",
                            "Those who scored 59 points or below on the test, please take the re-examination the week after next.",
                            f"① テストの{rb('点', 'てん')}が59{rb('点以下', 'てんいか')}だった{rb('人', 'ひと')}は、a. <u>{rb('再来週', 'さらいしゅう')}</u>、{rb('再試験', 'さいしけん')}を{rb('受', 'う')}けてください。",
                            "さらいしゅう", ["さらいしゅう", "再来週"],
                            "In 「再来週（さらいしゅう）」「再来月」「再来年」, 再 is read サ."
                        ),
                        item_rw(
                            "k_ex_23_1_2", "再", "再試験", "さいしけん",
                            "① テストの点が59点以下だった人は、再来週、b. <u>再試験</u>を受けてください。",
                            "Those who scored 59 points or below on the test, please take the re-examination the week after next.",
                            f"① テストの{rb('点', 'てん')}が59{rb('点以下', 'てんいか')}だった{rb('人', 'ひと')}は、{rb('再来週', 'さらいしゅう')}、b. <u>{rb('再試験', 'さいしけん')}</u>を{rb('受', 'う')}けてください。",
                            "さいしけん", ["さいしけん", "再試験"],
                            "「再試験（さいしけん）」means re-examination (再 is read サイ)."
                        ),
                        item_rw(
                            "k_ex_23_1_3", "判", "評判", "ひょうばん",
                            "② お医者さんを選ぶときは、近所の a. <u>評判</u>を聞いたり、インターネットで調べたりしてから、判断するようにしている。",
                            "When choosing a doctor, I make a judgment after hearing the neighborhood reputation and checking the internet.",
                            f"② お{rb('医者', 'いしゃ')}さんを{rb('選', 'えら')}ぶときは、{rb('近所', 'きんじょ')}の a. <u>{rb('評判', 'ひょうばん')}</u>を{rb('聞', 'き')}いたり、インターネットで{rb('調', 'しら')}べたりしてから、{rb('判断', 'はんだん')}するようにしている。",
                            "ひょうばん", ["ひょうばん", "評判"],
                            "「評判（ひょうばん）」means reputation or popularity (判 is voiced as バン)."
                        ),
                        item_rw(
                            "k_ex_23_1_4", "判", "判断", "はんだん",
                            "② お医者さんを選ぶときは、近所の評判を聞いたり、インターネットで調べたりしてから、b. <u>判断</u>するようにしている。",
                            "When choosing a doctor, I make a judgment after hearing the neighborhood reputation and checking the internet.",
                            f"② お{rb('医者', 'いしゃ')}さんを{rb('選', 'えら')}ぶときは、{rb('近所', 'きんじょ')}の{rb('評判', 'ひょうばん')}を{rb('聞', 'き')}いたり、インターネットで{rb('調', 'しら')}べたりしてから、b. <u>{rb('判断', 'はんだん')}</u>するようにしている。",
                            "はんだん", ["はんだん", "判断"],
                            "「判断（はんだん）」means judgment or decision."
                        ),
                        item_rw(
                            "k_ex_23_1_5", "由", "経由", "けいゆ",
                            "③ 20時のパリ a. <u>経由</u>ロンドン行きの飛行機に乗ります。それまで、自由に町を観光してください。",
                            "We will board the 20:00 flight to London via Paris. Until then, please sightsee around the town freely.",
                            f"③ 20{rb('時', 'じ')}のパリ a. <u>{rb('経由', 'けいゆ')}</u>ロンドン{rb('行', 'ゆ')}きの{rb('飛行機', 'ひこうき')}に{rb('乗', 'の')}ります。それまで、{rb('自由', 'じゆう')}に{rb('町', 'まち')}を{rb('観光', 'かんこう')}してください。",
                            "けいゆ", ["けいゆ", "経由"],
                            "「経由（けいゆ）」means via or by way of (short ゆ)."
                        ),
                        item_rw(
                            "k_ex_23_1_6", "由", "自由", "じゆう",
                            "③ 20時のパリ経由ロンドン行きの飛行機に乗ります。それまで、b. <u>自由</u>に町を観光してください。",
                            "We will board the 20:00 flight to London via Paris. Until then, please sightsee around the town freely.",
                            f"③ 20{rb('時', 'じ')}のパリ{rb('経由', 'けいゆ')}ロンドン{rb('行', 'ゆ')}きの{rb('飛行機', 'ひこうき')}に{rb('乗', 'の')}ります。それまで、b. <u>{rb('自由', 'じゆう')}</u>に{rb('町', 'まち')}を{rb('観光', 'かんこう')}してください。",
                            "じゆう", ["じゆう", "自由"],
                            "「自由（じゆう）」means freedom or freely (long ゆう)."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_23_2",
                    "type": "multiple_choice",
                    "title_ja": "2. 正しいものを選びましょう。",
                    "title_en": "2. Choose the correct option.",
                    "items": [
                        item_mc(
                            "k_ex_23_2_1", "定", "決定", "けってい",
                            "① 会議で<u>決定</u>（ a けつてい　b けってい ）したことを、お知らせします。",
                            "We will inform you of what was decided at the meeting.",
                            f"① {rb('会議', 'かいぎ')}で<u>{rb('決定', 'けってい')}</u>したことを、お{rb('知', 'し')}らせします。",
                            [{"id": "1", "text": "けつてい"}, {"id": "2", "text": "けってい"}],
                            "2",
                            "「決定（けってい）」has a geminate consonant (っ)."
                        ),
                        item_mc(
                            "k_ex_23_2_2", "規", "定規", "じょうぎ",
                            "② 線は、<u>定規</u>（ a じょうぎ　b ていぎ　c じょうき ）を使って、きれいに引いてください。",
                            "Please draw the lines neatly using a ruler.",
                            f"② {rb('線', 'せん')}は、<u>{rb('定規', 'じょうぎ')}</u>を{rb('使', 'つか')}って、きれいに{rb('引', 'ひ')}いてください。",
                            [{"id": "1", "text": "じょうぎ"}, {"id": "2", "text": "ていぎ"}, {"id": "3", "text": "じょうき"}],
                            "1",
                            "「定規（じょうぎ）」means ruler (定 is read ジョウ and 規 is voiced as ギ)."
                        ),
                        item_mc(
                            "k_ex_23_2_3", "券", "定期券", "ていきけん",
                            "③ <u>定期券</u>（ a じょうきけん　b ていきけん　c てえきけん ）を買うときに、証明書が要りますか。",
                            "Do I need a certificate when buying a commuter pass?",
                            f"③ <u>{rb('定期券', 'ていきけん')}</u>を{rb('買', 'か')}うときに、{rb('証明書', 'しょうめいしょ')}が{rb('要', 'い')}りますか。",
                            [{"id": "1", "text": "じょうきけん"}, {"id": "2", "text": "ていきけん"}, {"id": "3", "text": "てえきけん"}],
                            "2",
                            "「定期券（ていきけん）」means commuter pass."
                        ),
                        item_mc(
                            "k_ex_23_2_4", "由", "理由", "りゆう",
                            "④ あなたが反対する<u>りゆう</u>（ a 理曲　b 理田　c 理由 ）を言ってください。",
                            "Please state the reason why you oppose.",
                            f"④ あなたが{rb('反対', 'はんたい')}する<u>{rb('理由', 'りゆう')}</u>を{rb('言', 'い')}ってください。",
                            [{"id": "1", "text": "理曲"}, {"id": "2", "text": "理田"}, {"id": "3", "text": "理由"}],
                            "3",
                            "「理由（りゆう）」means reason."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_23_3",
                    "type": "radical_assembly",
                    "title_ja": "3. 漢字の部分を入れて、漢字を完成しましょう。読み方も書きましょう。",
                    "title_en": "3. Combine the parts to complete the kanji and write the reading.",
                    "items": [
                        item_rw(
                            "k_ex_23_3_1", "定", "定休日", "ていきゅうび",
                            "① あの店は、水曜日が（ 宀 ＋ 疋 ＝ ？ ）休日だから、今日はやっていないはずだ。",
                            "Since Wednesday is that shop's regular holiday, it shouldn't be open today.",
                            f"① あの{rb('店', 'みせ')}は、{rb('水曜日', 'すいようび')}が<u>{rb('定休日', 'ていきゅうび')}</u>だから、{rb('今日', 'きょう')}はやっていないはずだ。",
                            "定（ていきゅうび）", ["定", "ていきゅうび", "てい", "定休日"],
                            "宀 + 疋 = 定. 「定休日（ていきゅうび）」means regular closing day."
                        ),
                        item_rw(
                            "k_ex_23_3_2", "則", "規則", "きそく",
                            "② このマンションは、動物を飼ってはいけない規（ 貝 ＋ 刂 ＝ ？ ）になっている。",
                            "This apartment building has a rule that you must not keep pets.",
                            f"② このマンションは、{rb('動物', 'どうぶつ')}を{rb('飼', 'か')}ってはいけない<u>{rb('規則', 'きそく')}</u>になっている。",
                            "則（きそく）", ["則", "きそく", "そく", "規則"],
                            "貝 + 刂 = 則. 「規則（きそく）」means rule or regulation."
                        ),
                        item_rw(
                            "k_ex_23_3_3", "評", "評判", "ひょうばん",
                            "③ 新しい製品の（ 言 ＋ 平 ＝ ？ ）判は大変よくて、よく売れています。",
                            "The reputation of the new product is very good, and it is selling well.",
                            f"③ {rb('新', 'あたら')}しい{rb('製品', 'せいひん')}の<u>{rb('評判', 'ひょうばん')}</u>は{rb('大変', 'たいへん')}よくて、よく{rb('売', 'う')}れています。",
                            "評（ひょうばん）", ["評", "ひょうばん", "ひょう", "評判"],
                            "言 + 平 = 評. 「評判（ひょうばん）」means reputation."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_23_4",
                    "type": "reading_writing",
                    "title_ja": "4. 下線の部分の平仮名に漢字を書きましょう。",
                    "title_en": "4. Write the underlined hiragana in kanji.",
                    "items": [
                        item_rw(
                            "k_ex_23_4_1", "定", "定価", "ていか",
                            "① 新しいかばんを、<u>ていか</u>の70％で買った。",
                            "I bought a new bag at 70% of the regular price.",
                            f"① {rb('新', 'あたら')}しいかばんを、<u>{rb('定価', 'ていか')}</u>の70％で{rb('買', 'か')}った。",
                            "定価", ["定価", "ていか"],
                            "「定価（ていか）」means list price or regular price."
                        ),
                        item_rw(
                            "k_ex_23_4_2", "券", "券", "けん",
                            "② 映画の<u>けん</u>が2枚あります。",
                            "I have two movie tickets.",
                            f"② {rb('映画', 'えいが')}の<u>{rb('券', 'けん')}</u>が2{rb('枚', 'まい')}あります。",
                            "券", ["券", "けん"],
                            "「券（けん）」means ticket or voucher."
                        ),
                        item_rw(
                            "k_ex_23_4_3", "再", "再利用", "さいりよう",
                            "③ 瓶を<u>さいりよう</u>することで、ごみが減らせます。",
                            "By reusing bottles, we can reduce trash.",
                            f"③ {rb('瓶', 'びん')}を<u>{rb('再利用', 'さいりよう')}</u>することで、ごみが{rb('減', 'へ')}らせます。",
                            "再利用", ["再利用", "さいりよう"],
                            "「再利用（さいりよう）」means reuse."
                        ),
                    ],
                },
            ],
        },
        # =====================================================================
        # LESSON 24: 第24回 三つ以上の読み方を覚える漢字 (1) 音訓 (pp. 98-99)
        # =====================================================================
        {
            "lesson_id": 24,
            "title_ja": "第24回 三つ以上の読み方を覚える漢字 (1) 音訓",
            "title_en": "Lesson 24: Kanji with Three or More Readings (1) On & Kun",
            "page_range": "98-99",
            "target_kanji": ["下", "子", "土", "外", "行", "言", "後", "重", "度", "伝", "様", "菓"],
            "exercises": [
                {
                    "exercise_id": "k_ex_24_1",
                    "type": "reading_recall",
                    "title_ja": "1. 絵を見て、読み方を書きましょう。",
                    "title_en": "1. Look at the pictures and write the readings.",
                    "items": [
                        item_rw(
                            "k_ex_24_1_1", "重", "重い", "おもい",
                            "① a. <u>重い</u>本を重ねる。",
                            "Stack heavy books.",
                            f"① a. <u>{rb('重', 'おも')}い</u>{rb('本', 'ほん')}を{rb('重', 'かさ')}ねる。",
                            "おもい", ["おもい", "重い"],
                            "「重い（おもい）」means heavy."
                        ),
                        item_rw(
                            "k_ex_24_1_2", "重", "重ねる", "かさねる",
                            "① 重い本を b. <u>重ねる</u>。",
                            "Stack heavy books.",
                            f"① {rb('重', 'おも')}い{rb('本', 'ほん')}を b. <u>{rb('重', 'かさ')}ねる</u>。",
                            "かさねる", ["かさねる", "重ねる"],
                            "「重ねる（かさねる）」means to pile up or stack."
                        ),
                        item_rw(
                            "k_ex_24_1_3", "子", "女の子", "おんなのこ",
                            "② a. <u>女の子</u>の様子が変だ。",
                            "The girl's appearance/behavior is strange.",
                            f"② a. <u>{rb('女', 'おんな')}の{rb('子', 'こ')}</u>の{rb('様子', 'ようす')}が{rb('変', 'へん')}だ。",
                            "おんなのこ", ["おんなのこ", "こ", "女の子"],
                            "In 「女の子（おんなのこ）」, 子 is read こ."
                        ),
                        item_rw(
                            "k_ex_24_1_4", "子", "様子", "ようす",
                            "② 女の子の b. <u>様子</u>が変だ。",
                            "The girl's appearance/behavior is strange.",
                            f"② {rb('女', 'おんな')}の{rb('子', 'こ')}の b. <u>{rb('様子', 'ようす')}</u>が{rb('変', 'へん')}だ。",
                            "ようす", ["ようす", "様子"],
                            "In 「様子（ようす）」, 子 is read ス."
                        ),
                        item_rw(
                            "k_ex_24_1_5", "行", "行事", "ぎょうじ",
                            "③ a. <u>行事</u>が行われる。",
                            "An event is held.",
                            f"③ a. <u>{rb('行事', 'ぎょうじ')}</u>が{rb('行', 'おこな')}われる。",
                            "ぎょうじ", ["ぎょうじ", "行事"],
                            "「行事（ぎょうじ）」means event or function (on-reading ギョウ)."
                        ),
                        item_rw(
                            "k_ex_24_1_6", "行", "行われる", "おこなわれる",
                            "③ 行事が b. <u>行われる</u>。",
                            "An event is held.",
                            f"③ {rb('行事', 'ぎょうじ')}が b. <u>{rb('行', 'おこな')}われる</u>。",
                            "おこなわれる", ["おこなわれる", "おこなう", "行われる"],
                            "「行われる（おこなわれる）」means to be held or carried out."
                        ),
                        item_rw(
                            "k_ex_24_1_7", "土", "土地", "とち",
                            "④ この a. <u>土地</u>は土がいい。",
                            "This land has good soil.",
                            f"④ この a. <u>{rb('土地', 'とち')}</u>は{rb('土', 'つち')}がいい。",
                            "とち", ["とち", "土地"],
                            "「土地（とち）」means land or plot of land (on-reading ト)."
                        ),
                        item_rw(
                            "k_ex_24_1_8", "土", "土", "つち",
                            "④ この土地は b. <u>土</u>がいい。",
                            "This land has good soil.",
                            f"④ この{rb('土地', 'とち')}は b. <u>{rb('土', 'つち')}</u>がいい。",
                            "つち", ["つち", "土"],
                            "「土（つち）」means soil or earth."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_24_2",
                    "type": "word_pairing",
                    "title_ja": "2. 二つの言葉がだいたい同じ意味になるように、[伝、後、度、重] の中の漢字を使って、言葉を完成しましょう。読み方も書きましょう。",
                    "title_en": "2. Complete the pairs of expressions with similar meanings using [伝, 後, 度, 重] and write their readings.",
                    "items": [
                        item_rw(
                            "k_ex_24_2_1", "伝", "伝えて・伝言して", "つたえて・でんごんして",
                            "① 今日は休むと a. <u>[ 　 ]えて</u>ください。＝ 今日は休むと b. <u>[ 　 ]言して</u>ください。",
                            "Please tell them / leave a message that I am taking today off.",
                            f"① {rb('今日', 'きょう')}は{rb('休', 'やす')}むと a. <u>{rb('伝', 'つた')}えて</u>ください。＝ {rb('今日', 'きょう')}は{rb('休', 'やす')}むと b. <u>{rb('伝言', 'でんごん')}して</u>ください。",
                            "伝（つたえて・でんごんして）", ["伝", "つたえて", "でんごん", "でんごんして", "つたえて・でんごんして"],
                            "「伝える（つたえる）」and 「伝言する（でんごんする）」both mean to convey a message."
                        ),
                        item_rw(
                            "k_ex_24_2_2", "度", "何度も・度々", "なんども・たびたび",
                            "② 彼は a. <u>何[ 　 ]も</u>電話してきた。＝ 彼は b. <u>[ 　 ]々</u>電話してきた。",
                            "He called many times. = He called repeatedly.",
                            f"② {rb('彼', 'かれ')}は a. <u>{rb('何度', 'なんど')}も</u>{rb('電話', 'でんわ')}してきた。＝ {rb('彼', 'かれ')}は b. <u>{rb('度々', 'たびたび')}</u>{rb('電話', 'でんわ')}してきた。",
                            "度（なんども・たびたび）", ["度", "なんども", "たびたび", "なんども・たびたび"],
                            "「何度も（なんども）」and 「度々（たびたび）」both mean many times / repeatedly."
                        ),
                        item_rw(
                            "k_ex_24_2_3", "後", "後ろ・後半", "うしろ・こうはん",
                            "③ 来週の a. <u>真ん中より[ 　 ]</u>は晴れるでしょう。＝ 来週の b. <u>[ 　 ]半</u>は晴れるでしょう。",
                            "The latter part of next week will probably be sunny. = The second half of next week will probably be sunny.",
                            f"③ {rb('来週', 'らいしゅう')}の a. <u>{rb('真', 'ま')}ん{rb('中', 'なか')}より{rb('後', 'あと')}</u>は{rb('晴', 'は')}れるでしょう。＝ {rb('来週', 'らいしゅう')}の b. <u>{rb('後半', 'こうはん')}</u>は{rb('晴', 'は')}れるでしょう。",
                            "後（あと・こうはん）", ["後", "あと", "うしろ", "こうはん", "あと・こうはん", "うしろ・こうはん"],
                            "「後（あと／うしろ）」and 「後半（こうはん）」refer to the latter part / second half."
                        ),
                        item_rw(
                            "k_ex_24_2_4", "重", "重さ・体重", "おもさ・たいじゅう",
                            "④ ここで a. <u>体の[ 　 ]さ</u>を量ります。＝ ここで b. <u>体[ 　 ]</u>を量ります。",
                            "We measure the weight of your body here. = We measure your body weight here.",
                            f"④ ここで a. <u>{rb('体', 'からだ')}の{rb('重', 'おも')}さ</u>を{rb('量', 'はか')}ります。＝ ここで b. <u>{rb('体重', 'たいじゅう')}</u>を{rb('量', 'はか')}ります。",
                            "重（おもさ・たいじゅう）", ["重", "おもさ", "からだのおもさ", "たいじゅう", "おもさ・たいじゅう"],
                            "「体の重さ（からだのおもさ）」equals 「体重（たいじゅう）」(body weight)."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_24_3",
                    "type": "multiple_choice",
                    "title_ja": "3. 正しいものを選びましょう。",
                    "title_en": "3. Choose the correct option.",
                    "items": [
                        item_mc(
                            "k_ex_24_3_1", "後", "後", "のち",
                            "① 今日の天気は、晴れ<u>後</u>（ a ご　b あと　c のち ）曇りです。",
                            "Today's weather is sunny, then cloudy later.",
                            f"① {rb('今日', 'きょう')}の{rb('天気', 'てんき')}は、{rb('晴', 'は')}れ<u>{rb('後', 'のち')}</u>{rb('曇', 'くも')}りです。",
                            [{"id": "1", "text": "ご"}, {"id": "2", "text": "あと"}, {"id": "3", "text": "のち"}],
                            "3",
                            "In weather forecasts, 「後」is read のち (sunny, later cloudy)."
                        ),
                        item_mc(
                            "k_ex_24_3_2", "下", "下宿", "げしゅく",
                            "② 学生のとき、この辺りに<u>下宿</u>（ a げっしゅく　b げしゅく　c けじゅく ）していた。",
                            "When I was a student, I lodged in this area.",
                            f"② {rb('学生', 'がくせい')}のとき、この{rb('辺', 'あた')}りに<u>{rb('下宿', 'げしゅく')}</u>していた。",
                            [{"id": "1", "text": "げっしゅく"}, {"id": "2", "text": "げしゅく"}, {"id": "3", "text": "けじゅく"}],
                            "2",
                            "「下宿（げしゅく）」means lodging or boarding house (on-reading ゲ)."
                        ),
                        item_mc(
                            "k_ex_24_3_3", "度", "支度", "したく",
                            "③ そろそろ出かける<u>支度</u>（ a したく　b しど　c したび ）をしなければなりません。",
                            "It is about time I got ready to go out.",
                            f"③ そろそろ{rb('出', 'で')}かける<u>{rb('支度', 'したく')}</u>をしなければなりません。",
                            [{"id": "1", "text": "したく"}, {"id": "2", "text": "しど"}, {"id": "3", "text": "したび"}],
                            "1",
                            "「支度（したく）」means preparation (度 is read タク here)."
                        ),
                        item_mc(
                            "k_ex_24_3_4", "菓", "お菓子", "おかし",
                            "④ <u>おかし</u>（ a お果子　b お菓子　c お菓予 ）を作るのが趣味だ。",
                            "Making sweets is my hobby.",
                            f"④ <u>お{rb('菓子', 'かし')}</u>を{rb('作', 'つく')}るのが{rb('趣味', 'しゅみ')}だ。",
                            [{"id": "1", "text": "お果子"}, {"id": "2", "text": "お菓子"}, {"id": "3", "text": "お菓予"}],
                            "2",
                            "「お菓子（おかし）」means sweets or confections."
                        ),
                        item_mc(
                            "k_ex_24_3_5", "外", "外科", "げか",
                            "⑤ けがをして血が止まらないので、<u>外科</u>（ a げか　b がか　c がいか ）に行った。",
                            "Since I got injured and the bleeding wouldn't stop, I went to the surgery department.",
                            f"⑤ けがをして{rb('血', 'ち')}が{rb('止', 'と')}まらないので、<u>{rb('外科', 'げか')}</u>に{rb('行', 'い')}った。",
                            [{"id": "1", "text": "げか"}, {"id": "2", "text": "がか"}, {"id": "3", "text": "がいか"}],
                            "1",
                            "「外科（げか）」means surgery department (外 is read ゲ)."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_24_4",
                    "type": "reading_recall",
                    "title_ja": "4. 下線の部分の読み方を書きましょう。",
                    "title_en": "4. Write the readings of the underlined words.",
                    "items": [
                        item_rw(
                            "k_ex_24_4_1", "下", "下りる", "おりる",
                            "① 駅の階段を a. <u>下りる</u>と、ちょうど下りの電車が来るところだった。",
                            "When I went down the station stairs, the outbound train was just arriving.",
                            f"① {rb('駅', 'えき')}の{rb('階段', 'かいだん')}を a. <u>{rb('下', 'お')}りる</u>と、ちょうど{rb('下', 'くだ')}りの{rb('電車', 'でんしゃ')}が{rb('来', 'く')}るところだった。",
                            "おりる", ["おりる", "下りる"],
                            "「階段を下りる（かいだんをおりる）」means to go down the stairs."
                        ),
                        item_rw(
                            "k_ex_24_4_2", "下", "下り", "くだり",
                            "① 駅の階段を下りると、ちょうど b. <u>下り</u>の電車が来るところだった。",
                            "When I went down the station stairs, the outbound train was just arriving.",
                            f"① {rb('駅', 'えき')}の{rb('階段', 'かいだん')}を{rb('下', 'お')}りると、ちょうど b. <u>{rb('下', 'くだ')}り</u>の{rb('電車', 'でんしゃ')}が{rb('来', 'く')}るところだった。",
                            "くだり", ["くだり", "下り"],
                            "「下り（くだり）」refers to an outbound train heading away from the capital."
                        ),
                        item_rw(
                            "k_ex_24_4_3", "下", "下がって", "さがって",
                            "① 「線の内側に c. <u>下がって</u>ください」という駅員さんの声が聞こえた。",
                            "I heard the station attendant's voice saying, 'Please step back behind the line.'",
                            f"① 「{rb('線', 'せん')}の{rb('内側', 'うちがわ')}に c. <u>{rb('下', 'さ')}がって</u>ください」という{rb('駅員', 'えきいん')}さんの{rb('声', 'こえ')}が{rb('聞', 'き')}こえた。",
                            "さがって", ["さがって", "さがる", "下がって"],
                            "「下がる（さがる）」means to step back or move down."
                        ),
                        item_rw(
                            "k_ex_24_4_4", "言", "言う", "いう",
                            "② 何を a. <u>言う</u>か、どんな言葉を使うかよく考えてから発言する。",
                            "Think carefully about what to say and what words to use before speaking up.",
                            f"② {rb('何', 'なに')}を a. <u>{rb('言', 'い')}う</u>か、どんな{rb('言葉', 'ことば')}を{rb('使', 'つか')}うかよく{rb('考', 'かんが')}えてから{rb('発言', 'はつげん')}する。",
                            "いう", ["いう", "言う"],
                            "「言う（いう）」means to say."
                        ),
                        item_rw(
                            "k_ex_24_4_5", "言", "言葉", "ことば",
                            "② 何を言うか、どんな b. <u>言葉</u>を使うかよく考えてから発言する。",
                            "Think carefully about what to say and what words to use before speaking up.",
                            f"② {rb('何', 'なに')}を{rb('言', 'い')}うか、どんな b. <u>{rb('言葉', 'ことば')}</u>を{rb('使', 'つか')}うかよく{rb('考', 'かんが')}えてから{rb('発言', 'はつげん')}する。",
                            "ことば", ["ことば", "言葉"],
                            "「言葉（ことば）」uses the kun-reading こと."
                        ),
                        item_rw(
                            "k_ex_24_4_6", "言", "発言", "はつげん",
                            "② 何を言うか、どんな言葉を使うかよく考えてから c. <u>発言</u>する。",
                            "Think carefully about what to say and what words to use before speaking up.",
                            f"② {rb('何', 'なに')}を{rb('言', 'い')}うか、どんな{rb('言葉', 'ことば')}を{rb('使', 'つか')}うかよく{rb('考', 'かんが')}えてから c. <u>{rb('発言', 'はつげん')}</u>する。",
                            "はつげん", ["はつげん", "発言"],
                            "「発言（はつげん）」means statement or speaking out (on-reading ゲン)."
                        ),
                        item_rw(
                            "k_ex_24_4_7", "子", "下の子", "したのこ",
                            "③ a. <u>下の子</u>のおなかの調子が悪い。様子を見て、あした医者に連れて行こう。",
                            "My younger child's stomach is in bad shape. I'll watch their condition and take them to the doctor tomorrow.",
                            f"③ a. <u>{rb('下', 'した')}の{rb('子', 'こ')}</u>のおなかの{rb('調子', 'ちょうし')}が{rb('悪', 'わる')}い。{rb('様子', 'ようす')}を{rb('見', 'み')}て、あした{rb('医者', 'いしゃ')}に{rb('連', 'つ')}れて{rb('行', 'い')}こう。",
                            "したのこ", ["したのこ", "下の子"],
                            "「下の子（したのこ）」means younger child."
                        ),
                        item_rw(
                            "k_ex_24_4_8", "子", "調子", "ちょうし",
                            "③ 下の子のおなかの b. <u>調子</u>が悪い。様子を見て、あした医者に連れて行こう。",
                            "My younger child's stomach is in bad shape. I'll watch their condition and take them to the doctor tomorrow.",
                            f"③ {rb('下', 'した')}の{rb('子', 'こ')}のおなかの b. <u>{rb('調子', 'ちょうし')}</u>が{rb('悪', 'わる')}い。{rb('様子', 'ようす')}を{rb('見', 'み')}て、あした{rb('医者', 'いしゃ')}に{rb('連', 'つ')}れて{rb('行', 'い')}こう。",
                            "ちょうし", ["ちょうし", "調子"],
                            "「調子（ちょうし）」means condition or state (on-reading シ)."
                        ),
                        item_rw(
                            "k_ex_24_4_9", "様", "様子", "ようす",
                            "③ 下の子のおなかの調子が悪い。c. <u>様子</u>を見て、あした医者に連れて行こう。",
                            "My younger child's stomach is in bad shape. I'll watch their condition and take them to the doctor tomorrow.",
                            f"③ {rb('下', 'した')}の{rb('子', 'こ')}のおなかの{rb('調子', 'ちょうし')}が{rb('悪', 'わる')}い。c. <u>{rb('様子', 'ようす')}</u>を{rb('見', 'み')}て、あした{rb('医者', 'いしゃ')}に{rb('連', 'つ')}れて{rb('行', 'い')}こう。",
                            "ようす", ["ようす", "様子"],
                            "「様子（ようす）」means state or appearance (子 is read ス)."
                        ),
                        item_rw(
                            "k_ex_24_4_10", "行", "行ったら", "いったら",
                            "④ 駅へ a. <u>行ったら</u>、交通機関を利用する人の行動について、調査を行っていた。",
                            "When I went to the station, they were conducting a survey on the behavior of public transit users.",
                            f"④ {rb('駅', 'えき')}へ a. <u>{rb('行', 'い')}ったら</u>、{rb('交通機関', 'こうつうきかん')}を{rb('利用', 'りよう')}する{rb('人', 'ひと')}の{rb('行動', 'こうどう')}について、{rb('調査', 'ちょうさ')}を{rb('行', 'おこな')}っていた。",
                            "いったら", ["いったら", "いく", "行ったら"],
                            "「行く（いく）」means to go."
                        ),
                        item_rw(
                            "k_ex_24_4_11", "行", "行動", "こうどう",
                            "④ 駅へ行ったら、交通機関を利用する人の b. <u>行動</u>について、調査を行っていた。",
                            "When I went to the station, they were conducting a survey on the behavior of public transit users.",
                            f"④ {rb('駅', 'えき')}へ{rb('行', 'い')}ったら、{rb('交通機関', 'こうつうきかん')}を{rb('利用', 'りよう')}する{rb('人', 'ひと')}の b. <u>{rb('行動', 'こうどう')}</u>について、{rb('調査', 'ちょうさ')}を{rb('行', 'おこな')}っていた。",
                            "こうどう", ["こうどう", "行動"],
                            "「行動（こうどう）」means action or behavior (on-reading コウ)."
                        ),
                        item_rw(
                            "k_ex_24_4_12", "行", "行って", "おこなって",
                            "④ 駅へ行ったら、交通機関を利用する人の行動について、調査を c. <u>行って</u>いた。",
                            "When I went to the station, they were conducting a survey on the behavior of public transit users.",
                            f"④ {rb('駅', 'えき')}へ{rb('行', 'い')}ったら、{rb('交通機関', 'こうつうきかん')}を{rb('利用', 'りよう')}する{rb('人', 'ひと')}の{rb('行動', 'こうどう')}について、{rb('調査', 'ちょうさ')}を c. <u>{rb('行', 'おこな')}って</u>いた。",
                            "おこなって", ["おこなって", "おこなう", "行って"],
                            "「調査を行う（ちょうさをおこなう）」means to conduct a survey."
                        ),
                        item_rw(
                            "k_ex_24_4_13", "外", "外出", "がいしゅつ",
                            "⑤ a. <u>外出</u>する前に天気予報を調べたのに、予報が外れて大雪になった。",
                            "Even though I checked the weather forecast before going out, the forecast was wrong and it snowed heavily.",
                            f"⑤ a. <u>{rb('外出', 'がいしゅつ')}</u>する{rb('前', 'まえ')}に{rb('天気予報', 'てんきよほう')}を{rb('調', 'しら')}べたのに、{rb('予報', 'よほう')}が{rb('外', 'はず')}れて{rb('大雪', 'おおゆき')}になった。",
                            "がいしゅつ", ["がいしゅつ", "外出"],
                            "「外出（がいしゅつ）」means going out (on-reading ガイ)."
                        ),
                        item_rw(
                            "k_ex_24_4_14", "外", "外れて", "はずれて",
                            "⑤ 外出する前に天気予報を調べたのに、予報が b. <u>外れて</u>大雪になった。",
                            "Even though I checked the weather forecast before going out, the forecast was wrong and it snowed heavily.",
                            f"⑤ {rb('外出', 'がいしゅつ')}する{rb('前', 'まえ')}に{rb('天気予報', 'てんきよほう')}を{rb('調', 'しら')}べたのに、{rb('予報', 'よほう')}が b. <u>{rb('外', 'はず')}れて</u>{rb('大雪', 'おおゆき')}になった。",
                            "はずれて", ["はずれて", "はずれる", "外れて"],
                            "「外れる（はずれる）」means to be off-target, miss, or come undone."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_24_5",
                    "type": "reading_writing",
                    "title_ja": "5. 下線の部分の平仮名に漢字を書きましょう。",
                    "title_en": "5. Write the underlined hiragana in kanji.",
                    "items": [
                        item_rw(
                            "k_ex_24_5_1", "様", "お客様", "おきゃくさま",
                            "① <u>おきゃくさま</u>がいらっしゃいました。",
                            "A guest/customer has arrived.",
                            f"① <u>お{rb('客様', 'きゃくさま')}</u>がいらっしゃいました。",
                            "お客様", ["お客様", "おきゃくさま"],
                            "「お客様（おきゃくさま）」means guest or customer."
                        ),
                        item_rw(
                            "k_ex_24_5_2", "重", "重要な", "じゅうような",
                            "② <u>じゅうような</u>問題について話し合う。",
                            "Discuss an important issue.",
                            f"② <u>{rb('重要', 'じゅうよう')}な</u>{rb('問題', 'もんだい')}について{rb('話', 'はな')}し{rb('合', 'あ')}う。",
                            "重要な", ["重要な", "重要", "じゅうような"],
                            "「重要な（じゅうような）」means important."
                        ),
                        item_rw(
                            "k_ex_24_5_3", "子", "男子・女子", "だんし・じょし",
                            "③ 体育の授業は、a. <u>だんし</u>と b. <u>じょし</u>に分かれて行います。",
                            "Physical education classes are held separately for boys and girls.",
                            f"③ {rb('体育', 'たいいく')}の{rb('授業', 'じゅぎょう')}は、a. <u>{rb('男子', 'だんし')}</u>と b. <u>{rb('女子', 'じょし')}</u>に{rb('分', 'わ')}かれて{rb('行', 'おこな')}います。",
                            "男子・女子", ["男子・女子", "男子", "女子", "だんし・じょし"],
                            "「男子（だんし）」and 「女子（じょし）」mean boys/men and girls/women."
                        ),
                    ],
                },
            ],
        },
        # =====================================================================
        # LESSON 25: 第25回 三つ以上の読み方を覚える漢字 (2) 音訓 (pp. 100-101)
        # =====================================================================
        {
            "lesson_id": 25,
            "title_ja": "第25回 三つ以上の読み方を覚える漢字 (2) 音訓",
            "title_en": "Lesson 25: Kanji with Three or More Readings (2) On & Kun",
            "page_range": "100-101",
            "target_kanji": ["守", "形", "苦", "指", "相", "神", "消", "留", "無", "数"],
            "exercises": [
                {
                    "exercise_id": "k_ex_25_1",
                    "type": "reading_recall",
                    "title_ja": "1. 下線の部分の読み方を書きましょう。",
                    "title_en": "1. Write the readings of the underlined words.",
                    "items": [
                        item_rw(
                            "k_ex_25_1_1", "形", "人形", "にんぎょう",
                            "① a. <u>人形</u>",
                            "Doll",
                            f"① a. <u>{rb('人形', 'にんぎょう')}</u>",
                            "にんぎょう", ["にんぎょう", "人形"],
                            "In 「人形（にんぎょう）」, 形 is read ギョウ."
                        ),
                        item_rw(
                            "k_ex_25_1_2", "形", "形", "かたち",
                            "① 魚の b. <u>形</u>の雲",
                            "A fish-shaped cloud",
                            f"① {rb('魚', 'さかな')}の b. <u>{rb('形', 'かたち')}</u>の{rb('雲', 'くも')}",
                            "かたち", ["かたち", "形"],
                            "The kun-reading of 形 is 「かたち」(shape, form)."
                        ),
                        item_rw(
                            "k_ex_25_1_3", "形", "三角形", "さんかくけい",
                            "① c. <u>三角形</u>",
                            "Triangle",
                            f"① c. <u>{rb('三角形', 'さんかくけい')}</u>",
                            "さんかくけい", ["さんかくけい", "さんかっけい", "三角形"],
                            "In geometric shapes like 「三角形（さんかくけい）」, 形 is read ケイ."
                        ),
                        item_rw(
                            "k_ex_25_1_4", "数", "数字", "すうじ",
                            "② a. <u>数字</u>",
                            "Number / numeral",
                            f"② a. <u>{rb('数字', 'すうじ')}</u>",
                            "すうじ", ["すうじ", "数字"],
                            "「数字（すうじ）」uses the on-reading スウ."
                        ),
                        item_rw(
                            "k_ex_25_1_5", "数", "数", "かず",
                            "② b. <u>数</u>を数える。",
                            "Count the number.",
                            f"② b. <u>{rb('数', 'かず')}</u>を{rb('数', 'かぞ')}える。",
                            "かず", ["かず", "数"],
                            "As a standalone noun, 「数」is read かず."
                        ),
                        item_rw(
                            "k_ex_25_1_6", "数", "数える", "かぞえる",
                            "② 数を c. <u>数える</u>。",
                            "Count the number.",
                            f"② {rb('数', 'かず')}を c. <u>{rb('数', 'かぞ')}える</u>。",
                            "かぞえる", ["かぞえる", "数える"],
                            "The verb 'to count' is 「数える（かぞえる）」."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_25_2",
                    "type": "reading_recall",
                    "title_ja": "2. 下線の部分の読み方を書きましょう。",
                    "title_en": "2. Write the readings of the underlined words.",
                    "items": [
                        item_rw(
                            "k_ex_25_2_1", "苦", "苦しい", "くるしい",
                            "① 胸が a. <u>苦しい</u>。苦い薬を飲む。苦労をする。",
                            "My chest feels tight/painful. Take bitter medicine. Go through hardships.",
                            f"① {rb('胸', 'むね')}が a. <u>{rb('苦', 'くる')}しい</u>。{rb('苦', 'にが')}い{rb('薬', 'くすり')}を{rb('飲', 'の')}む。{rb('苦労', 'くろう')}をする。",
                            "くるしい", ["くるしい", "苦しい"],
                            "「苦しい（くるしい）」means painful, agonizing, or hard to breathe."
                        ),
                        item_rw(
                            "k_ex_25_2_2", "苦", "苦い", "にがい",
                            "① 胸が苦しい。b. <u>苦い</u>薬を飲む。苦労をする。",
                            "My chest feels tight/painful. Take bitter medicine. Go through hardships.",
                            f"① {rb('胸', 'むね')}が{rb('苦', 'くる')}しい。b. <u>{rb('苦', 'にが')}い</u>{rb('薬', 'くすり')}を{rb('飲', 'の')}む。{rb('苦労', 'くろう')}をする。",
                            "にがい", ["にがい", "苦い"],
                            "「苦い（にがい）」means bitter in taste."
                        ),
                        item_rw(
                            "k_ex_25_2_3", "苦", "苦労", "くろう",
                            "① 胸が苦しい。苦い薬を飲む。c. <u>苦労</u>をする。",
                            "My chest feels tight/painful. Take bitter medicine. Go through hardships.",
                            f"① {rb('胸', 'むね')}が{rb('苦', 'くる')}しい。{rb('苦', 'にが')}い{rb('薬', 'くすり')}を{rb('飲', 'の')}む。c. <u>{rb('苦労', 'くろう')}</u>をする。",
                            "くろう", ["くろう", "苦労"],
                            "「苦労（くろう）」means hardship or trouble (on-reading ク)."
                        ),
                        item_rw(
                            "k_ex_25_2_4", "消", "消火器", "しょうかき",
                            "② a. <u>消火器</u>で火を消す。火が消えた。",
                            "Extinguish the fire with a fire extinguisher. The fire went out.",
                            f"② a. <u>{rb('消火器', 'しょうかき')}</u>で{rb('火', 'ひ')}を{rb('消', 'け')}す。{rb('火', 'ひ')}が{rb('消', 'き')}えた。",
                            "しょうかき", ["しょうかき", "消火器"],
                            "「消火器（しょうかき）」means fire extinguisher (on-reading ショウ)."
                        ),
                        item_rw(
                            "k_ex_25_2_5", "消", "消す", "けす",
                            "② 消火器で火を b. <u>消す</u>。火が消えた。",
                            "Extinguish the fire with a fire extinguisher. The fire went out.",
                            f"② {rb('消火器', 'しょうかき')}で{rb('火', 'ひ')}を b. <u>{rb('消', 'け')}す</u>。{rb('火', 'ひ')}が{rb('消', 'き')}えた。",
                            "けす", ["けす", "消す"],
                            "「消す（けす）」is transitive (to put out / turn off)."
                        ),
                        item_rw(
                            "k_ex_25_2_6", "消", "消えた", "きえた",
                            "② 消火器で火を消す。火が c. <u>消えた</u>。",
                            "Extinguish the fire with a fire extinguisher. The fire went out.",
                            f"② {rb('消火器', 'しょうかき')}で{rb('火', 'ひ')}を{rb('消', 'け')}す。{rb('火', 'ひ')}が c. <u>{rb('消', 'き')}えた</u>。",
                            "きえた", ["きえた", "きえる", "消えた"],
                            "「消える（きえる）」is intransitive (to go out / disappear)."
                        ),
                        item_rw(
                            "k_ex_25_2_7", "指", "指", "ゆび",
                            "③ 欲しいものを a. <u>指</u>で指す。仕事の指示をする。",
                            "Point at what you want with your finger. Give work instructions.",
                            f"③ {rb('欲', 'ほ')}しいものを a. <u>{rb('指', 'ゆび')}</u>で{rb('指', 'さ')}す。{rb('仕事', 'しごと')}の{rb('指示', 'しじ')}をする。",
                            "ゆび", ["ゆび", "指"],
                            "「指（ゆび）」means finger or toe."
                        ),
                        item_rw(
                            "k_ex_25_2_8", "指", "指す", "さす",
                            "③ 欲しいものを指で b. <u>指す</u>。仕事の指示をする。",
                            "Point at what you want with your finger. Give work instructions.",
                            f"③ {rb('欲', 'ほ')}しいものを{rb('指', 'ゆび')}で b. <u>{rb('指', 'さ')}す</u>。{rb('仕事', 'しごと')}の{rb('指示', 'しじ')}をする。",
                            "さす", ["さす", "指す"],
                            "「指す（さす）」means to point at or indicate."
                        ),
                        item_rw(
                            "k_ex_25_2_9", "指", "指示", "しじ",
                            "③ 欲しいものを指で指す。仕事の c. <u>指示</u>をする。",
                            "Point at what you want with your finger. Give work instructions.",
                            f"③ {rb('欲', 'ほ')}しいものを{rb('指', 'ゆび')}で{rb('指', 'さ')}す。{rb('仕事', 'しごと')}の c. <u>{rb('指示', 'しじ')}</u>をする。",
                            "しじ", ["しじ", "指示"],
                            "「指示（しじ）」means instruction or direction (on-reading シ)."
                        ),
                        item_rw(
                            "k_ex_25_2_10", "無", "無くす", "なくす",
                            "④ 鍵を a. <u>無くす</u>。無事だと聞いて安心した。この電話は無料で使える。",
                            "Lose a key. I was relieved to hear they are safe. This phone can be used for free.",
                            f"④ {rb('鍵', 'かぎ')}を a. <u>{rb('無', 'な')}くす</u>。{rb('無事', 'ぶじ')}だと{rb('聞', 'き')}いて{rb('安心', 'あんしん')}した。この{rb('電話', 'でんわ')}は{rb('無料', 'むりょう')}で{rb('使', 'つか')}える。",
                            "なくす", ["なくす", "無くす"],
                            "「無くす（なくす）」means to lose something."
                        ),
                        item_rw(
                            "k_ex_25_2_11", "無", "無事", "ぶじ",
                            "④ 鍵を無くす。b. <u>無事</u>だと聞いて安心した。この電話は無料で使える。",
                            "Lose a key. I was relieved to hear they are safe. This phone can be used for free.",
                            f"④ {rb('鍵', 'かぎ')}を{rb('無', 'な')}くす。b. <u>{rb('無事', 'ぶじ')}</u>だと{rb('聞', 'き')}いて{rb('安心', 'あんしん')}した。この{rb('電話', 'でんわ')}は{rb('無料', 'むりょう')}で{rb('使', 'つか')}える。",
                            "ぶじ", ["ぶじ", "無事"],
                            "「無事（ぶじ）」means safe and sound (on-reading ブ)."
                        ),
                        item_rw(
                            "k_ex_25_2_12", "無", "無料", "むりょう",
                            "④ 鍵を無くす。無事だと聞いて安心した。この電話は c. <u>無料</u>で使える。",
                            "Lose a key. I was relieved to hear they are safe. This phone can be used for free.",
                            f"④ {rb('鍵', 'かぎ')}を{rb('無', 'な')}くす。{rb('無事', 'ぶじ')}だと{rb('聞', 'き')}いて{rb('安心', 'あんしん')}した。この{rb('電話', 'でんわ')}は c. <u>{rb('無料', 'むりょう')}</u>で{rb('使', 'つか')}える。",
                            "むりょう", ["むりょう", "無料"],
                            "「無料（むりょう）」means free of charge (on-reading ム)."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_25_3",
                    "type": "multiple_choice",
                    "title_ja": "3. 正しいものを選びましょう。",
                    "title_en": "3. Choose the correct option.",
                    "items": [
                        item_mc(
                            "k_ex_25_3_1", "相", "首相", "しゅしょう",
                            "① <u>首相</u>（ a しゅうそう　b しゅしょう ）は、ヨーロッパの国々を訪問した。",
                            "The Prime Minister visited European countries.",
                            f"① <u>{rb('首相', 'しゅしょう')}</u>は、ヨーロッパの{rb('国々', 'くにぐに')}を{rb('訪問', 'ほうもん')}した。",
                            [{"id": "1", "text": "しゅうそう"}, {"id": "2", "text": "しゅしょう"}],
                            "2",
                            "「首相（しゅしょう）」means Prime Minister (相 is read ショウ)."
                        ),
                        item_mc(
                            "k_ex_25_3_2", "指", "目指して", "めざして",
                            "② 来年の春の完成を<u>目指して</u>（ a めさして　b めざして ）、橋の建設を急いでいる。",
                            "Aiming for completion next spring, they are hurrying the construction of the bridge.",
                            f"② {rb('来年', 'らいねん')}の{rb('春', 'はる')}の{rb('完成', 'かんせい')}を<u>{rb('目指', 'めざ')}して</u>、{rb('橋', 'はし')}の{rb('建設', 'けんせつ')}を{rb('急', 'いそ')}いでいる。",
                            [{"id": "1", "text": "めさして"}, {"id": "2", "text": "めざして"}],
                            "2",
                            "「目指す（めざす）」has sequential voicing (ざ)."
                        ),
                        item_mc(
                            "k_ex_25_3_3", "留", "書留", "かきとめ",
                            "③ 大事な手紙なので、<u>書留</u>（ a かきどめ　b かきとめ　c かきどまり ）で送った。",
                            "Because it is an important letter, I sent it by registered mail.",
                            f"③ {rb('大事', 'だいじ')}な{rb('手紙', 'てがみ')}なので、<u>{rb('書留', 'かきとめ')}</u>で{rb('送', 'おく')}った。",
                            [{"id": "1", "text": "かきどめ"}, {"id": "2", "text": "かきとめ"}, {"id": "3", "text": "かきどまり"}],
                            "2",
                            "「書留（かきとめ）」means registered mail (unvoiced とめ)."
                        ),
                        item_mc(
                            "k_ex_25_3_4", "数", "数学", "すうがく",
                            "④ 私は<u>すうがく</u>（ a 数学　b 教学　c 類学 ）が得意です。",
                            "I am good at mathematics.",
                            f"④ {rb('私', 'わたし')}は<u>{rb('数学', 'すうがく')}</u>が{rb('得意', 'とくい')}です。",
                            [{"id": "1", "text": "数学"}, {"id": "2", "text": "教学"}, {"id": "3", "text": "類学"}],
                            "1",
                            "「数学（すうがく）」means mathematics."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_25_4",
                    "type": "radical_assembly",
                    "title_ja": "4. 漢字の部分を入れて、漢字を完成しましょう。読み方も書きましょう。",
                    "title_en": "4. Combine the parts to complete the kanji and write the reading.",
                    "items": [
                        item_rw(
                            "k_ex_25_4_1", "守", "守る", "まもる",
                            "① 彼は約束を必ず（ 宀 ＋ 寸 ＝ ？ ）る。",
                            "He always keeps his promises.",
                            f"① {rb('彼', 'かれ')}は{rb('約束', 'やくそく')}を{rb('必', 'かなら')}ず<u>{rb('守', 'まも')}</u>る。",
                            "守（まも）", ["守", "まもる", "まも", "守る"],
                            "宀 + 寸 = 守. 「約束を守る（やくそくをまもる）」means to keep a promise."
                        ),
                        item_rw(
                            "k_ex_25_4_2", "相", "相手", "あいて",
                            "② 電話で話していた（ 木 ＋ 目 ＝ ？ ）手は、誰ですか。",
                            "Who was the person you were talking with on the phone?",
                            f"② {rb('電話', 'でんわ')}で{rb('話', 'はな')}していた<u>{rb('相手', 'あいて')}</u>は、{rb('誰', 'だれ')}ですか。",
                            "相（あいて）", ["相", "あいて", "あい", "相手"],
                            "木 + 目 = 相. 「相手（あいて）」means partner or the other party."
                        ),
                        item_rw(
                            "k_ex_25_4_3", "消", "消えなかった", "きえなかった",
                            "③ 水をかけても、火はなかなか（ 氵 ＋ 肖 ＝ ？ ）えなかった。",
                            "Even when water was poured on it, the fire did not go out easily.",
                            f"③ {rb('水', 'みず')}をかけても、{rb('火', 'ひ')}はなかなか<u>{rb('消', 'き')}</u>えなかった。",
                            "消（き）", ["消", "きえなかった", "き", "消えなかった"],
                            "氵 + 肖 = 消. 「火が消える（ひがきえる）」means the fire goes out."
                        ),
                        item_rw(
                            "k_ex_25_4_4", "苦", "苦しそう", "くるしそう",
                            "④ 弟は、高い熱が出て、（ 艹 ＋ 古 ＝ ？ ）しそうだった。",
                            "My younger brother had a high fever and looked like he was in pain.",
                            f"④ {rb('弟', 'おとうと')}は、{rb('高', 'たか')}い{rb('熱', 'ねつ')}が{rb('出', 'で')}て、<u>{rb('苦', 'くる')}</u>しそうだった。",
                            "苦（くる）", ["苦", "くるしそう", "くる", "苦しそう"],
                            "艹 + 古 = 苦. 「苦しそう（くるしそう）」means seeming to suffer/be in pain."
                        ),
                    ],
                },
                {
                    "exercise_id": "k_ex_25_5",
                    "type": "word_pairing",
                    "title_ja": "5. □には同じ漢字が入ります。[数、神、留、相] から漢字を選んで書きましょう。下線の部分の読み方も書きましょう。",
                    "title_en": "5. Fill in the blanks with the same kanji from [数, 神, 留, 相] and write the readings.",
                    "items": [
                        item_rw(
                            "k_ex_25_5_1", "相", "相談", "そうだん",
                            "① 進学について、先生に a. <u>[ 　 ]談</u>した。",
                            "I consulted with my teacher about going on to higher education.",
                            f"① {rb('進学', 'しんがく')}について、{rb('先生', 'せんせい')}に a. <u>{rb('相談', 'そうだん')}</u>した。",
                            "相（そうだん）", ["相", "そうだん", "相談"],
                            "「相談（そうだん）」uses the on-reading ソウ."
                        ),
                        item_rw(
                            "k_ex_25_5_2", "相", "相手", "あいて",
                            "① 結婚する b. <u>[ 　 ]手</u>を両親に紹介した。",
                            "I introduced my marriage partner to my parents.",
                            f"① {rb('結婚', 'けっこん')}する b. <u>{rb('相手', 'あいて')}</u>を{rb('両親', 'りょうしん')}に{rb('紹介', 'しょうかい')}した。",
                            "相（あいて）", ["相", "あいて", "相手"],
                            "「相手（あいて）」uses the kun-reading あい."
                        ),
                        item_rw(
                            "k_ex_25_5_3", "相", "首相", "しゅしょう",
                            "① 新しい c. <u>首[ 　 ]</u>は、大臣の中でいちばん若い。",
                            "The new Prime Minister is the youngest among the cabinet ministers.",
                            f"① {rb('新', 'あたら')}しい c. <u>{rb('首相', 'しゅしょう')}</u>は、{rb('大臣', 'だいじん')}の{rb('中', 'なか')}でいちばん{rb('若', 'わか')}い。",
                            "相（しゅしょう）", ["相", "しゅしょう", "首相"],
                            "「首相（しゅしょう）」uses the on-reading ショウ."
                        ),
                        item_rw(
                            "k_ex_25_5_4", "神", "神社", "じんじゃ",
                            "② お正月は、a. <u>[ 　 ]社</u>に行って、いい年になるようにと神様にお願いする。",
                            "On New Year's, we go to a shrine and pray to God for a good year.",
                            f"② お{rb('正月', 'しょうがつ')}は、a. <u>{rb('神社', 'じんじゃ')}</u>に{rb('行', 'い')}って、いい{rb('年', 'とし')}になるようにと{rb('神様', 'かみさま')}にお{rb('願', 'ねが')}いする。",
                            "神（じんじゃ）", ["神", "じんじゃ", "神社"],
                            "「神社（じんじゃ）」uses the on-reading ジン."
                        ),
                        item_rw(
                            "k_ex_25_5_5", "神", "神様", "かみさま",
                            "② お正月は、神社に行って、いい年になるようにと b. <u>[ 　 ]様</u>にお願いする。",
                            "On New Year's, we go to a shrine and pray to God for a good year.",
                            f"② お{rb('正月', 'しょうがつ')}は、{rb('神社', 'じんじゃ')}に{rb('行', 'い')}って、いい{rb('年', 'とし')}になるようにと b. <u>{rb('神様', 'かみさま')}</u>にお{rb('願', 'ねが')}いする。",
                            "神（かみさま）", ["神", "かみさま", "神様"],
                            "「神様（かみさま）」uses the kun-reading かみ."
                        ),
                        item_rw(
                            "k_ex_25_5_6", "神", "神経", "しんけい",
                            "② 痛いと感じるのは、c. <u>[ 　 ]経</u>があるからだ。",
                            "The reason we feel pain is because we have nerves.",
                            f"② {rb('痛', 'いた')}いと{rb('感', 'かん')}じるのは、c. <u>{rb('神経', 'しんけい')}</u>があるからだ。",
                            "神（しんけい）", ["神", "しんけい", "神経"],
                            "「神経（しんけい）」uses the on-reading シン."
                        ),
                        item_rw(
                            "k_ex_25_5_7", "留", "留学", "りゅうがく",
                            "③ 英語の勉強のために、オーストラリアに a. <u>[ 　 ]学</u>した。",
                            "I studied abroad in Australia to study English.",
                            f"③ {rb('英語', 'えいご')}の{rb('勉強', 'べんきょう')}のために、オーストラリアに a. <u>{rb('留学', 'りゅうがく')}</u>した。",
                            "留（りゅうがく）", ["留", "りゅうがく", "留学"],
                            "「留学（りゅうがく）」uses the on-reading リュウ."
                        ),
                        item_rw(
                            "k_ex_25_5_8", "留", "留守番", "るすばん",
                            "③ 両親が旅行に出かけたので、b. <u>[ 　 ]守番</u>をしている。",
                            "Since my parents went on a trip, I am house-sitting.",
                            f"③ {rb('両親', 'りょうしん')}が{rb('旅行', 'りょこう')}に{rb('出', 'で')}かけたので、b. <u>{rb('留守番', 'るすばん')}</u>をしている。",
                            "留（るすばん）", ["留", "るすばん", "留守番"],
                            "「留守番（るすばん）」uses the on-reading ル."
                        ),
                        item_rw(
                            "k_ex_25_5_9", "留", "書留", "かきとめ",
                            "③ お金を郵便で送るときは、c. <u>書[ 　 ]</u>で送ってください。",
                            "When sending money by mail, please send it by registered mail.",
                            f"③ お{rb('金', 'かね')}を{rb('郵便', 'ゆうびん')}で{rb('送', 'おく')}るときは、c. <u>{rb('書留', 'かきとめ')}</u>で{rb('送', 'おく')}ってください。",
                            "留（かきとめ）", ["留", "かきとめ", "書留"],
                            "「書留（かきとめ）」uses the kun-reading とめ."
                        ),
                        item_rw(
                            "k_ex_25_5_10", "数", "数える", "かぞえる",
                            "④ 英語で1から10まで a. <u>[ 　 ]える</u>。",
                            "Count from 1 to 10 in English.",
                            f"④ {rb('英語', 'えいご')}で1から10まで a. <u>{rb('数', 'かぞ')}える</u>。",
                            "数（かぞえる）", ["数", "かぞえる", "数える"],
                            "「数える（かぞえる）」means to count."
                        ),
                        item_rw(
                            "k_ex_25_5_11", "数", "点数", "てんすう",
                            "④ 先週の試験の b. <u>点[ 　 ]</u>が発表された。",
                            "The scores of last week's exam were announced.",
                            f"④ {rb('先週', 'せんしゅう')}の{rb('試験', 'しけん')}の b. <u>{rb('点数', 'てんすう')}</u>が{rb('発表', 'はっぴょう')}された。",
                            "数（てんすう）", ["数", "てんすう", "点数"],
                            "「点数（てんすう）」uses the on-reading スウ."
                        ),
                        item_rw(
                            "k_ex_25_5_12", "数", "数", "かず",
                            "④ コップが足りません。c. <u>[ 　 ]</u>をよく確かめてください。",
                            "There aren't enough cups. Please check the number carefully.",
                            f"④ コップが{rb('足', 'た')}りません。c. <u>{rb('数', 'かず')}</u>をよく{rb('確', 'たし')}かめてください。",
                            "数（かず）", ["数", "かず"],
                            "「数（かず）」means number or quantity."
                        ),
                    ],
                },
            ],
        },
    ]

    return {
        "metadata": {
            "source": "新完全マスター漢字 日本語能力試験 N3 (Shin Kanzen Master Kanji N3)",
            "part": 5,
            "title_ja": "第5部 いろいろな読み方のある漢字（第21回〜第25回）",
            "title_en": "Part 5: Kanji with Multiple Readings (Lessons 21–25)",
            "lessons": [21, 22, 23, 24, 25],
            "note": "Part 5 concludes at Lesson 25 (p. 101); there is no まとめ問題 5 in the textbook (followed directly by 実力テスト 1 & 2 on pp. 103–107).",
        },
        "lessons": lessons,
        "reviews": [],
    }


def main() -> None:
    data = build_data()
    out_dir = os.path.join("nihongo-intermediate", "data", "kanji")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "exercises_part5.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total_exercises = sum(len(lesson["exercises"]) for lesson in data["lessons"])
    total_items = sum(
        len(ex["items"])
        for lesson in data["lessons"]
        for ex in lesson["exercises"]
    )
    print(f"Wrote {out_path}: {len(data['lessons'])} lessons, {total_exercises} exercises, {total_items} items.")


if __name__ == "__main__":
    main()
