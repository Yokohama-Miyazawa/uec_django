import random
import time
from numpy import *

#くじの種類
def omikuji():
    omikuji = ["大吉", "吉", "中吉", "小吉", "凶"]

    print('これからあなたの今年の運勢を占います')
    time.sleep(2)

    #確率の設定
    print('1から5の中から好きな数字を入力してください')
    your_number = int(input())
    if your_number == 1:
        kakuritsu = [0.3, 0.2, 0.2, 0.2, 0.1]
    elif your_number == 2:
        kakuritsu = [0.2, 0.2, 0.2, 0.2, 0.2]
    elif your_number == 3:
        kakuritsu = [0.5, 0.0, 0.0, 0.0, 0.5]
    elif your_number == 4:
        kakuritsu = [0.1, 0.2, 0.2, 0.2, 0.3]
    else:
        kakuritsu = [0.1, 0.2, 0.4, 0.2, 0.1]

    #くじを引く
    your_fortune = random.choice(omikuji, p=kakuritsu)

    print("あなたの今年の運勢は・・・")
    time.sleep(3)
    print(your_fortune)
    time.sleep(1)

    #くじのコメント
    daikichi = ["おめでとう！\n自信を持っていろんなことに挑戦しよう！",
                "やったね！\n何をやっても成功しそう！"]
    kichi = ["金運up!\n勉強を頑張れば、お小遣いが増えるかも！？",
             "後半に運気up!\n今はコツコツやるべきことをしっかりやろう！",
             "運気upはあなた次第！\n家族や友人の言葉を素直に聞くと◎"]
    kyou = ["残念！\nでも大丈夫！しっかり勉学に励んで！\n部屋を片付けるといいよ！",
            "今は辛抱の時！\n時間を大切に過ごそう！\nいつもより10分早く起きてみよう！"]

    if your_fortune == "大吉":
        d = random.choice(daikichi)
        print(d)
    elif your_fortune == "凶":
        ky = random.choice(kyou)
        print(ky)
    else:
        ki = random.choice(kichi)
        print(ki)

#おみくじの実行
while True:
    omikuji()
    time.sleep(2)
    print("もう一度行いますか？ y or n?")
    play_again = input()
    if play_again != "y":
        break
