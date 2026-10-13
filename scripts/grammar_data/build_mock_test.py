"""
Builds nihongo-intermediate/data/grammar/mock_test.json
Combines Mock Test 1 and Mock Test 2 (46 questions total)
with full questions, star arrangements, passage cloze texts, answers, and explanations.
"""
import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.append(os.path.dirname(__file__))
from G4_extracted.mock_test_1_and_2 import get_mock_tests

def build_mock_test():
    test1_q, test2_q = get_mock_tests()

    # Passage texts with full HTML ruby tags
    passage1_text = (
        "わたしは<ruby>毎日<rt>まいにち</rt></ruby><ruby>昼<rt>ひる</rt></ruby>ごはんにはおにぎりを<ruby>食<rt>た</rt></ruby>べます。"
        "おにぎりを<ruby>食<rt>た</rt></ruby>べると、<ruby>元気<rt>げんき</rt></ruby>が<ruby>出<rt>で</rt></ruby>るような<ruby>気<rt>き</rt></ruby>がします。"
        "おにぎりを<ruby>食<rt>た</rt></ruby>べながら、<ruby>米<rt>こめ</rt></ruby>について［ 19 ］。\n\n"
        "<ruby>米作<rt>こめづく</rt></ruby>りは<ruby>大昔<rt>おおむかし</rt></ruby>、アジアの<ruby>暖<rt>あたた</rt></ruby>かい<ruby>地方<rt>ちほう</rt></ruby>で<ruby>始<rt>はじ</rt></ruby>まったと<ruby>考<rt>かんが</rt></ruby>えられています。"
        "そして、<ruby>今<rt>いま</rt></ruby>、<ruby>米<rt>こめ</rt></ruby>は［ 20 ］<ruby>食<rt>た</rt></ruby>べられています。"
        "エネルギーの<ruby>素<rt>もと</rt></ruby>になり、また、<ruby>栄養<rt>えいよう</rt></ruby>のバランスがいいということも<ruby>主食<rt>しゅしょく</rt></ruby>になっている<ruby>理由<rt>りゆう</rt></ruby>の<ruby>一<rt>ひと</rt></ruby>つだと<ruby>思<rt>おも</rt></ruby>います。\n\n"
        "［ 21 ］<ruby>今<rt>いま</rt></ruby>、<ruby>日本<rt>にほん</rt></ruby>では、<ruby>若<rt>わか</rt></ruby>い<ruby>人<rt>ひと</rt></ruby>たちを<ruby>中心<rt>ちゅうしん</rt></ruby>に<ruby>米<rt>こめ</rt></ruby>を<ruby>食<rt>た</rt></ruby>べる<ruby>人<rt>ひと</rt></ruby>が<ruby>減<rt>へ</rt></ruby>っていると<ruby>聞<rt>き</rt></ruby>きました。"
        "ご<ruby>飯<rt>はん</rt></ruby>を<ruby>炊<rt>た</rt></ruby>いておかずを<ruby>作<rt>つく</rt></ruby>るより、パン、うどん、ラーメンなどの<ruby>方<rt>ほう</rt></ruby>が<ruby>簡単<rt>かんたん</rt></ruby>に<ruby>食<rt>た</rt></ruby>べられるからでしょう。"
        "もちろんいろいろな<ruby>種類<rt>しゅるい</rt></ruby>の<ruby>食事<rt>しょくじ</rt></ruby>ができることはとても<ruby>楽<rt>たの</rt></ruby>しいことですが、わたしは<ruby>米<rt>こめ</rt></ruby>のよさがもっと［ 22 ］と<ruby>思<rt>おも</rt></ruby>います。"
        "<ruby>日本<rt>にほん</rt></ruby>の<ruby>気候<rt>きこう</rt></ruby>は<ruby>米作<rt>こめづく</rt></ruby>りに<ruby>合<rt>あ</rt></ruby>っているので、<ruby>国内<rt>こくない</rt></ruby>でおいしい<ruby>米<rt>こめ</rt></ruby>ができます。"
        "わたしはその<ruby>土地<rt>とち</rt></ruby>で<ruby>昔<rt>むかし</rt></ruby>から<ruby>作<rt>つく</rt></ruby>られてきたものを<ruby>食<rt>た</rt></ruby>べるのがいちばん<ruby>体<rt>からだ</rt></ruby>に<ruby>合<rt>あ</rt></ruby>っていて<ruby>健康的<rt>けんこうてき</rt></ruby>だと<ruby>考<rt>かんが</rt></ruby>えています。"
        "そういう<ruby>意味<rt>いみ</rt></ruby>で、<ruby>米<rt>こめ</rt></ruby>は<ruby>日本人<rt>にほんじん</rt></ruby>にとって<ruby>最<rt>もっと</rt></ruby>も<ruby>健康的<rt>けんこうてき</rt></ruby>な<ruby>食品<rt>しょくひん</rt></ruby>［ 23 ］。"
    )

    passage2_text = (
        "わたしが<ruby>生<rt>う</rt></ruby>まれたのは、<ruby>海<rt>うみ</rt></ruby>のそばの<ruby>小<rt>ちい</rt></ruby>さな［ 19 ］。"
        "<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>はだいたい<ruby>海<rt>うみ</rt></ruby>に<ruby>関係<rt>かんけい</rt></ruby>がある<ruby>仕事<rt>しごと</rt></ruby>をしています。"
        "わたしの<ruby>父<rt>ちち</rt></ruby>と<ruby>祖父<rt>そふ</rt></ruby>は<ruby>船<rt>ふね</rt></ruby>に<ruby>乗<rt>の</rt></ruby>って<ruby>遠<rt>とお</rt></ruby>くの<ruby>海<rt>うみ</rt></ruby>まで<ruby>魚<rt>さかな</rt></ruby>を<ruby>捕<rt>と</rt></ruby>りに<ruby>行<rt>い</rt></ruby>っていますし、"
        "<ruby>母<rt>はは</rt></ruby>は<ruby>港<rt>みなと</rt></ruby>の<ruby>近<rt>ちか</rt></ruby>くの<ruby>工場<rt>こうじょう</rt></ruby>で<ruby>貝<rt>かい</rt></ruby>をむいています。"
        "<ruby>小<rt>ちい</rt></ruby>さな<ruby>町<rt>まち</rt></ruby>なので、<ruby>大<rt>おお</rt></ruby>きい<ruby>病院<rt>びょういん</rt></ruby>やデパートなどはありません。"
        "<ruby>必要<rt>ひつよう</rt></ruby>なときは<ruby>車<rt>くるま</rt></ruby>で<ruby>遠<rt>とお</rt></ruby>くまで<ruby>行<rt>い</rt></ruby>かなければなりません。"
        "ですから、<ruby>大人<rt>おとな</rt></ruby>になると、みんな<ruby>町<rt>まち</rt></ruby>を<ruby>出<rt>で</rt></ruby>ていってしまいます。［ 20 ］。\n\n"
        "<ruby>子<rt>こ</rt></ruby>どものころは、わたしの<ruby>町<rt>まち</rt></ruby>はどの<ruby>都市<rt>とし</rt></ruby>からも<ruby>遠<rt>とお</rt></ruby>くて、"
        "どこにも<ruby>簡単<rt>かんたん</rt></ruby>に<ruby>行<rt>い</rt></ruby>けないさびしい<ruby>町<rt>まち</rt></ruby>だと<ruby>思<rt>おも</rt></ruby>っていました。"
        "［ 21 ］、<ruby>今<rt>いま</rt></ruby>では<ruby>考<rt>かんが</rt></ruby>えが<ruby>変<rt>か</rt></ruby>わりました。"
        "この<ruby>町<rt>まち</rt></ruby>の<ruby>人<rt>ひと</rt></ruby>は、<ruby>小<rt>ちい</rt></ruby>さい<ruby>子<rt>こ</rt></ruby>どもでも、"
        "<ruby>世界<rt>せかい</rt></ruby>のいろいろな<ruby>港<rt>みなと</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>やそこでどんなものが<ruby>捕<rt>と</rt></ruby>れるかをよく<ruby>知<rt>し</rt></ruby>っています。"
        "<ruby>子<rt>こ</rt></ruby>どものときから、<ruby>周<rt>まわ</rt></ruby>りの<ruby>大人<rt>おとな</rt></ruby>に<ruby>世界中<rt>せかいじゅう</rt></ruby>の<ruby>海<rt>うみ</rt></ruby>の<ruby>話<rt>はなし</rt></ruby>を［ 22 ］<ruby>育<rt>そだ</rt></ruby>つからです。"
        "わたしたちは<ruby>海<rt>うみ</rt></ruby>の<ruby>様子<rt>ようす</rt></ruby>や<ruby>捕<rt>と</rt></ruby>れた<ruby>魚<rt>さかな</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、"
        "<ruby>地球<rt>ちきゅう</rt></ruby>の<ruby>反対側<rt>はんたいがわ</rt></ruby>の<ruby>海<rt>うみ</rt></ruby>の<ruby>温度<rt>おんど</rt></ruby>や、<ruby>海水<rt>かいすい</rt></ruby>の<ruby>流<rt>なが</rt></ruby>れなどを<ruby>想像<rt>そうぞう</rt></ruby>することができます。"
        "どこからも<ruby>離<rt>はな</rt></ruby>れていると<ruby>思<rt>おも</rt></ruby>っていたわたしの<ruby>町<rt>まち</rt></ruby>は、"
        "<ruby>実<rt>じつ</rt></ruby>は、<ruby>海<rt>うみ</rt></ruby>の<ruby>向<rt>む</rt></ruby>こうの<ruby>世界<rt>せかい</rt></ruby>と［ 23 ］。"
    )

    # Attach passage texts to the respective cloze questions
    for q in test1_q[18:]:
        q["passage_full_text"] = passage1_text
    for q in test2_q[18:]:
        q["passage_full_text"] = passage2_text

    mock_tests_structured = [
        {
            "test_number": 1,
            "title": "<ruby>模擬試験<rt>もぎしけん</rt></ruby> <ruby>第<rt>だい</rt></ruby>1<ruby>回<rt>かい</rt></ruby>",
            "title_en": "JLPT N3 Grammar Mock Test 1",
            "source_pages": "P148 ~ P151 (Images 149 ~ 152)",
            "total_questions": len(test1_q),
            "sections": [
                {
                    "section_number": 1,
                    "section_name": "<ruby>問題<rt>もんだい</rt></ruby>1",
                    "section_title": "<ruby>文法形式<rt>ぶんぽうけいしき</rt></ruby>の<ruby>判断<rt>はんだん</rt></ruby>",
                    "section_title_en": "Grammar Form Judgment",
                    "instruction": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の（\u3000）に<ruby>入<rt>はい</rt></ruby>るものとして<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                    "questions": test1_q[:13]
                },
                {
                    "section_number": 2,
                    "section_name": "<ruby>問題<rt>もんだい</rt></ruby>2",
                    "section_title": "<ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>て",
                    "section_title_en": "Sentence Composition (Star Arrangement)",
                    "instruction": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の★に<ruby>入<rt>はい</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                    "questions": test1_q[13:18]
                },
                {
                    "section_number": 3,
                    "section_name": "<ruby>問題<rt>もんだい</rt></ruby>3",
                    "section_title": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>",
                    "section_title_en": "Text Grammar (Passage Cloze)",
                    "instruction": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで、<ruby>文章全体<rt>ぶんしょうぜんたい</rt></ruby>の<ruby>内容<rt>ないよう</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>えて、［ 19 ］から［ 23 ］の<ruby>中<rt>なか</rt></ruby>に<ruby>入<rt>はい</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                    "passage_title": "<ruby>米<rt>こめ</rt></ruby>",
                    "passage_author": "リー リサ",
                    "passage_text": passage1_text,
                    "questions": test1_q[18:23]
                }
            ]
        },
        {
            "test_number": 2,
            "title": "<ruby>模擬試験<rt>もぎしけん</rt></ruby> <ruby>第<rt>だい</rt></ruby>2<ruby>回<rt>かい</rt></ruby>",
            "title_en": "JLPT N3 Grammar Mock Test 2",
            "source_pages": "P152 ~ P155 (Images 153 ~ 156)",
            "total_questions": len(test2_q),
            "sections": [
                {
                    "section_number": 1,
                    "section_name": "<ruby>問題<rt>もんだい</rt></ruby>1",
                    "section_title": "<ruby>文法形式<rt>ぶんぽうけいしき</rt></ruby>の<ruby>判断<rt>はんだん</rt></ruby>",
                    "section_title_en": "Grammar Form Judgment",
                    "instruction": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の（\u3000）に<ruby>入<rt>はい</rt></ruby>るものとして<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                    "questions": test2_q[:13]
                },
                {
                    "section_number": 2,
                    "section_name": "<ruby>問題<rt>もんだい</rt></ruby>2",
                    "section_title": "<ruby>文<rt>ぶん</rt></ruby>の<ruby>組<rt>く</rt></ruby>み<ruby>立<rt>た</rt></ruby>て",
                    "section_title_en": "Sentence Composition (Star Arrangement)",
                    "instruction": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文<rt>ぶん</rt></ruby>の★に<ruby>入<rt>はい</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                    "questions": test2_q[13:18]
                },
                {
                    "section_number": 3,
                    "section_name": "<ruby>問題<rt>もんだい</rt></ruby>3",
                    "section_title": "<ruby>文章<rt>ぶんしょう</rt></ruby>の<ruby>文法<rt>ぶんぽう</rt></ruby>",
                    "section_title_en": "Text Grammar (Passage Cloze)",
                    "instruction": "<ruby>次<rt>つぎ</rt></ruby>の<ruby>文章<rt>ぶんしょう</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで、<ruby>文章全体<rt>ぶんしょうぜんたい</rt></ruby>の<ruby>内容<rt>ないよう</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>えて、［ 19 ］から［ 23 ］の<ruby>中<rt>なか</rt></ruby>に<ruby>入<rt>はい</rt></ruby>る<ruby>最<rt>もっと</rt></ruby>もよいものを、1・2・3・4から<ruby>一<rt>ひと</rt></ruby>つ<ruby>選<rt>えら</rt></ruby>びなさい。",
                    "passage_title": "「わたしが<ruby>生<rt>う</rt></ruby>まれた<ruby>町<rt>まち</rt></ruby>」",
                    "passage_text": passage2_text,
                    "questions": test2_q[18:23]
                }
            ]
        }
    ]

    all_questions_flat = test1_q + test2_q

    output_data = {
        "metadata": {
            "title": "<ruby>模擬試験<rt>もぎしけん</rt></ruby>",
            "title_en": "JLPT N3 Grammar Mock Tests (Full Practice Exams 1 & 2)",
            "description": "Complete mock tests for JLPT N3 Grammar from Shin Kanzen Master. Features Test 1 and Test 2, each with 23 exam-formatted questions across Mondai 1 (Grammar Form Judgment), Mondai 2 (Sentence Arrangement / Star Questions), and Mondai 3 (Passage Cloze Reading), complete with answers, full reconstructed sentences, and explanations.",
            "total_mock_tests": 2,
            "total_questions": len(all_questions_flat),
            "test_1_questions": len(test1_q),
            "test_2_questions": len(test2_q),
            "source_pages": "P148 ~ P155 (Images 148 ~ 156)"
        },
        "mock_tests": mock_tests_structured,
        "questions": all_questions_flat
    }

    out_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "grammar", "mock_test.json")
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {out_path}")
    print(f"Total mock tests: {len(mock_tests_structured)}, Total questions: {len(all_questions_flat)}")

if __name__ == "__main__":
    build_mock_test()
