questions = [
                {"question":"扁桃","answer":"A"},
                {"question":"竜髭菜","answer":"C"},
                {"question":"牛油果","answer":"B"},
                {"question":"覆盆子","answer":"D"},
                {"question":"赤根草","answer":"A"},
                {"question":"虎魚","answer":"C"},
                {"question":"柳葉魚","answer":"B"},
                {"question":"銀口魚","answer":"D"},
                {"question":"翻車魚","answer":"A"},
                {"question":"麦魚","answer":"C"},
                {"question":"紅娘","answer":"B"},
                {"question":"螽斯","answer":"D"},
                {"question":"蟷螂","answer":"A"},
                {"question":"蜚蠊","answer":"C"},
                {"question":"蜻蛉","answer":"B"},
                {"question":"猟虎","answer":"D"},
                {"question":"鼯鼠","answer":"A"},
                {"question":"膃肭臍","answer":"C"},
                {"question":"長尾驢","answer":"B"},
                {"question":"樹獺","answer":"D"},
                {"question":"木菟","answer":"A"},
                {"question":"朱鷺","answer":"C"},
                {"question":"不如帰","answer":"B"},
                {"question":"翡翠","answer":"D"},
                {"question":"鸚鵡","answer":"A"},
                {"question":"霙","answer":"C"},
                {"question":"飄","answer":"B"},
                {"question":"俄雨","answer":"D"},
                {"question":"朏","answer":"A"},
                {"question":"極光","answer":"C"}
           ]


selections = [
                {"A":"アーモンド","B":"ピーナッツ","C":"スモモ","D":"マカデミアナッツ"},
                {"A":"キャベツ","B":"ナガネギ","C":"アスパラガス","D":"トウモロコシ"},
                {"A":"マンゴー","B":"アボカド","C":"ゴーヤ","D":"パパイヤ"},
                {"A":"リンゴ","B":"イチジク","C":"ブルーベリー","D":"イチゴ"},
                {"A":"ホウレンソウ","B":"ムラサキキャベツ","C":"サツマイモ","D":"セロリ"},
                {"A":"トラフグ","B":"アンコウ","C":"オコゼ","D":"ウツボ"},
                {"A":"イワシ","B":"シシャモ","C":"アジ","D":"サバ"},
                {"A":"イワナ","B":"フナ","C":"コイ","D":"アユ"},
                {"A":"マンボウ","B":"エイ","C":"フグ","D":"ミツクリザメ"},
                {"A":"オイカワ","B":"ウグイ","C":"メダカ","D":"ドジョウ"},
                {"A":"ホタル","B":"テントウムシ","C":"アゲハチョウ","D":"コガネムシ"},
                {"A":"コオロギ","B":"イナゴ","C":"スズムシ","D":"キリギリス"},
                {"A":"カマキリ","B":"クワガタムシ","C":"カブトムシ","D":"セミ"},
                {"A":"ゲンゴロウ","B":"コガネムシ","C":"ゴキブリ","D":"カメムシ"},
                {"A":"カゲロウ","B":"トンボ","C":"アブ","D":"ムカデ"},
                {"A":"イタチ","B":"タヌキ","C":"カワウソ","D":"ラッコ"},
                {"A":"ムササビ","B":"コウモリ","C":"モモンガ","D":"コアラ"},
                {"A":"アシカ","B":"アザラシ","C":"オットセイ","D":"セイウチ"},
                {"A":"シマリス","B":"カンガルー","C":"キツネザル","D":"シマウマ"},
                {"A":"アルマジロ","B":"アリクイ","C":"ビーバー","D":"ナマケモノ"},
                {"A":"ミミズク","B":"キツツキ","C":"カッコウ","D":"モズ"},
                {"A":"ツル","B":"カモ","C":"トキ","D":"サギ"},
                {"A":"ウグイス","B":"ホトトギス","C":"ヒバリ","D":"ツバメ"},
                {"A":"ハチドリ","B":"ミソサザイ","C":"ツグミ","D":"カワセミ"},
                {"A":"オウム","B":"ダチョウ","C":"クジャク","D":"カナリア"},
                {"A":"ヒョウ","B":"アラレ","C":"ミゾレ","D":"モヤ"},
                {"A":"タイフウ","B":"ツムジカゼ","C":"コガラシ","D":"ハヤテ"},
                {"A":"コサメ","B":"サミダレ","C":"ソバエ","D":"ニワカアメ"},
                {"A":"ミカヅキ","B":"ユミハリヅキ","C":"モチヅキ","D":"イザヨイ"},
                {"A":"イナズマ","B":"トモシビ","C":"オーロラ","D":"キラメキ"}
           ]
import random

def random_no(max,num):
    return random.sample(range(max), num)

print("\n難読漢字４択クイズ")

score = 0

list = random_no(30,10)

for i in range(10):
    index = list[i]

    question = questions[index]['question']

    selectionA = selections[index]['A']
    selectionB = selections[index]['B']
    selectionC = selections[index]['C']
    selectionD = selections[index]['D']

    print("\nQ{0} {1}".format((i+1),question))
    print("A:{0} B:{1} C:{2} D:{3}".format(selectionA,selectionB,selectionC,selectionD))

    userInput = input("回答を入力:")

    print("入力された値は {0} です".format(userInput))

    if userInput.upper() == questions[index]['answer']:
        print("正解です")

        score += 1
    else:
        print("不正解です")

print("\n{0}問中 {1}問正解でした".format(10,score))
