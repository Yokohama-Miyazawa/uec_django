from time import sleep  # timeモジュールインポートを追加

while True:
    try:
        パスワードを入力してください= int(input('パスワードを入力してください: '))

        result = パスワードを入力してください

    except:
             print('英語はパスワードの中に入れません')
    else:
             break


if result== 937:
    print('パスワードは合ってます。ゲームが始まります。')
    sleep(2)  # sleepを追加
    import turtle
    import random

    def hit_check(me,enemy,r):
        x = me.xcor() - enemy.xcor()
        y = me.ycor() - enemy.ycor()
        distance =  (x**2+y**2)**(1/2)
        return distance < r


    def create_bullet(base,list):
        new_b = base.clone()
        new_b.setx(random.randrange(-500,500))
        list.append(new_b)

    if __name__=="__main__":
        t = turtle.Pen()
        bullet_base = t.clone()
        t.shape('turtle')
        t.color('green')
        t.lt(90)
        t.up()

    bullet_base.speed(0)
    bullet_base.shape('circle')
    bullet_base.rt(90)
    bullet_base.up()
    bullet_base.color('blue')
    bullet_base.setpos(0,500)
    bullet_list = []
    running = True

    def loop():
        global bullet_base,t,bullet_list,running
        if(running):
            if(random.randrange(1)==0):
                create_bullet(bullet_base,bullet_list)

            for b in bullet_list:
                b.fd(20)
                if(hit_check(t,b,20)):
                    running = False
                    t.write("GAME\nOVER",font=("Arial",40,"bold"))
                if(b.ycor()<-500):
                    b.sety(500)
            s.ontimer(loop,32)

    s = t.getscreen()
    t_speed = 20


    s.onkey(lambda:t.fd(t_speed),"Up")
    s.onkey(lambda:t.back(t_speed),"Down")
    s.onkey(lambda:t.setx(t.xcor()+t_speed),"Right")
    s.onkey(lambda:t.setx(t.xcor()-t_speed),"Left")

    loop()
    s.listen()
    s.mainloop()

elif result==973:
    print('パスワードは合ってます。ゲームが始まります。')
    sleep(2)  # sleepを追加
    from tkinter import *
    import random
    import time

    class Widget(object): #画面上で動く物の基本となるクラス
        def __init__(self, window, size, color, pos, speed=0):
            self.window = window
            self.size = size
            self.color = color
            self.pos = pos
            self.speed = speed
        def acty(self): #インスタンスを動かす
            self.window.move(self.id, self.speed[0], self.speed[1])
        def xturn(self): #横軸の方向転換
            self.speed[0] *= -1
        def yturn(self): #縦軸の方向転換
            self.speed[1] *= -1
        def current_speed(self): #現在の速度
            return self.speed

    class Ball(Widget): #Widgetを継承する、ボールのためのクラス
        def __init__(self, window, size, color, pos, speed):
            super().__init__(window, size, color, pos, speed)
            self.id = self.window.create_oval(self.pos[0], self.pos[1], \
                self.pos[0]+self.size, self.pos[1]+self.size, fill=self.color)
        def current_place(self): #今いる場所
            return self.window.coords(self.id)
        def hit_check(self, obj): #当たったかどうかのチェック
            own_pos = self.current_place()
            obj_pos = obj.current_place()
            if (own_pos[0]+25 > obj_pos[0] and own_pos[2]-25 < obj_pos[2]) \
                    and (own_pos[1] <= obj_pos[3] and own_pos[3] >= obj_pos[1]):
                return 1
            else:
                return 0

    class Var(Widget): #Widgetを継承する、ラケット用のクラス
        def __init__(self, window, size, color, pos):
            super().__init__(window, size, color, pos)
            self.point = 0
            self.id = self.window.create_rectangle(self.pos[0], self.pos[1], \
                self.pos[0]+self.size[0], self.pos[1]+self.size[1], fill=self.color)
        def current_place(self): #今いる場所
                return self.window.coords(self.id)

    class Player_Var(Var): #Varを継承する、プレイヤーラケット用のクラス
        def __init__(self, window, size, color, pos, step=10):
            super().__init__(window, size, color, pos)
            self.step = step
            self.window.bind_all('<Key>', self.control)
        def control(self, event): #操作設定
            if event.keysym == "Right":
                self.speed = [self.step, 0]
            elif event.keysym == "Left":
                self.speed = [-self.step, 0]
            self.acty()

    #ウィンドウの設定
    tk = Tk()
    canvas_size = [500, 400]
    canvas = Canvas(tk, width=canvas_size[0], height=canvas_size[1])
    tk.title("球打ちゲーム(仮)")
    canvas.pack()

    #ボールとラケットの設定
    ball_radius = 50
    ball_start = [random.randrange(50, 400), random.randrange(50, 100)]
    ball_init_speed = [7,6]
    var_size = [100,10]
    player_start = [230, 340]
    #ボールとラケットのインスタンス作成
    ball = Ball(canvas, ball_radius, 'blue', ball_start, ball_init_speed)
    my_var = Player_Var(canvas, var_size, 'red', pos=player_start)


    while True:
        ball.acty() #ボールを動かす
        ball_pos = ball.current_place()
        ball_speed = ball.current_speed()

        if ball_pos[2] >= canvas_size[0] or ball_pos[0] <= 0:
            ball.xturn()
        if ball_pos[3] >= canvas_size[1]:
            break
        elif ball_pos[1] <= 0:
            ball.yturn()
        elif ball.hit_check(my_var) == 1 and ball_speed[1] > 0: #ラケットに当たったら
            ball.yturn()

        tk.update()
        time.sleep(0.01)

    #ゲームオーバー
    judge_text = 'GAME OVER'
    canvas.create_text(250, 200, text=judge_text, fill='blue', font=('メイリオ', 30))
    tk.update()
    time.sleep(5)  # sleep時間を修正

elif result== 793:
    print('パスワードは合ってます。タートルで書いた絵が出てきます。')
    sleep(2)  # sleepを追加
    import turtle
    t = turtle.Pen()
    sleep(2)  # sleepを追加
    t.speed(0)
    r = t.clone()
    g = t.clone()
    a = t.clone()
    b = t.clone()
    t.up()
    t.goto(0,200)
    t.down()
    t.fd(230)
    t.lt(200)
    t.fd(160)
    t.lt(160)
    t.fd(160)
    t.lt(200)
    t.fd(260)
    t.lt(70)
    t.fd(50)
    t.lt(90)
    t.fd(300)
    t.lt(200)
    t.fd(230)
    t.lt(70)
    t.fd(100)
    t.lt(270)
    t.fd(50)
    t.lt(90)
    g.up()
    g.lt(180)
    g.fd(30)
    g.lt(90)
    g.down()
    g.fd(172)
    g.lt(90)
    g.fd(60)
    g.lt(90)
    g.fd(130)
    r.up()
    r.lt(180)
    r.fd(30)
    r.down()
    r.fd(90)
    r.lt(325)
    r.fd(70)
    r.lt(35)
    r.fd(50)
    r.lt(220)
    r.fd(85)
    r.lt(80)
    r.lt(50)
    r.fd(70)
    r.lt(220)
    r.fd(70)
    r.lt(330)
    r.fd(103)
    r.lt(320)
    r.fd(50)
    r.lt(40)
    r.fd(30)
    r.lt(90)
    r.fd(90)
    a.up()
    a.goto(-170,110)
    a.down()
    a.circle(10)
    b.up()
    b.goto(-65,140)
    b.lt(70)
    b.down()
    b.fd(90)
    b.lt(290)
    b.fd(180)
    b.lt(250)
    b.fd(30)


else:
    print('パスワードは間違っています。　ヒント--９と３と７の数字が一つずつ使われています')


s = input()
