class Student(object):
    student_number = 0  # クラス変数

    def __init__(self, name):  # インスタンス作成時に実行
        self.name = name  # インスタンス変数
        self.add()

    def myname(self):  # self.nameを出力するインスタンスメソッド
        print('私は'+self.name+'です。')

    @classmethod
    def add(cls):  # 生徒追加の際に呼び出されるクラスメソッド
        cls.student_number += 1
        print('生徒が追加されました。')

    @classmethod
    def members(cls):  # 現在の生徒数を返すクラスメソッド
        print(str(cls.student_number)+'人です。')
