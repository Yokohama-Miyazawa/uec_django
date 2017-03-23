import tkinter as tk
from random import choice


class Game():
    WIDTH = 300
    HEIGHT = 500

    def start(self):
        self.speed = 150
        self.new_game = True

        self.root = tk.Tk()
        self.root.title("Tetris")

        self.canvas = tk.Canvas(
            self.root,
            width=Game.WIDTH,
            height=Game.HEIGHT
        )
        self.canvas.pack()#表示される

        self.timer()
        self.root.mainloop()

    def timer(self):
        if self.new_game == True:#最初の図形を作るため
            self.current_shape = Shape(self.canvas)
            self.new_game = False

        if not self.current_shape.fall():
            self.current_shape = Shape(self.canvas)#新しく図形を作る

        self.root.after(self.speed,self.timer)#.speedミリ秒後.timerを起動


class Shape:
    BOX_SIZE = 20
    START_POINT = Game.WIDTH / 2 / BOX_SIZE * BOX_SIZE - BOX_SIZE#画面の真ん中のブロックの位置
    SHAPES = (
            ((0, 0), (1, 0), (0, 1), (1, 1)), # 四角
            ((0, 0), (1, 0), (2, 0), (3, 0)), # 棒
            ((2, 0), (0, 1), (1, 1), (2, 1)), # L字
    )
    def __init__(self,canvas):
        #ランダムにブロックを選び、windowにブロックを表示する
        self.boxes = []
        self.shape = choice(Shape.SHAPES)#ランダムに形を選ぶ
        self.canvas = canvas

        for point in self.shape:
            #point => テトリス画面上の座標
            box = canvas.create_rectangle(#ブロックの１つ１つの形成
                point[0] * Shape.BOX_SIZE + Shape.START_POINT,
                point[1] * Shape.BOX_SIZE,
                point[0] * Shape.BOX_SIZE + Shape.BOX_SIZE + Shape.START_POINT,
                point[1] * Shape.BOX_SIZE + Shape.BOX_SIZE
            )
            self.boxes.append(box)#boxesにブロックを入れる

    def fall(self):#図形を下に移動
        if not self.can_move_shape(0, 1):
            return False
        else:
            for box in self.boxes:
                self.canvas.move(box, 0 * Shape.BOX_SIZE, 1 * Shape.BOX_SIZE)
            return True

    def can_move_box(self, box, x, y):#ボックスが動けるかチェック
        x = x * Shape.BOX_SIZE
        y = y * Shape.BOX_SIZE
        coords = self.canvas.coords(box)

        # 画面からブロックが行き過ぎるとFalse
        if coords[3] + y > Game.HEIGHT: return False
        if coords[0] + x < 0: return False
        if coords[2] + x > Game.WIDTH: return False

        # 他のボックスに重なるとFalse
        overlap = set(self.canvas.find_overlapping(
                (coords[0] + coords[2]) / 2 - x,
                (coords[1] + coords[3]) / 2 - y,
                (coords[0] + coords[2]) / 2 + x,
                (coords[1] + coords[3]) / 2 + y
                ))
        other_items = set(self.canvas.find_all()) - set(self.boxes)
        # print(other_items)
        # print(overlap)
        if overlap & other_items:
            return False
        return True

    def can_move_shape(self, x, y):#図形が移動できるかチェック
        for box in self.boxes:
            if not self.can_move_box(box, x, y): return False
        return True

if __name__ == "__main__":
    game = Game()
    game.start()
