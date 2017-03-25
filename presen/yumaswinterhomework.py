print("これから、日本人がよくわかるキロメートルを、アメリカ人がよくわかるマイルにして差し上げましょう！！！！（整数でお願いします。）")
while True:
    try:
        km= int(input('km: '))
        result = km * 0.62137119
    except:
        print('エラーが発生しました。')
    else:
        break

print("mi:",result)
