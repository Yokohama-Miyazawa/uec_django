from django.test import TestCase


def func_hoge():  # テスト対象の関数その1
    return 1


def func_fuga():  # テスト対象の関数その2
    return 0


def func_piyo():  # テスト対象の関数その3
    return 1 == 1


def func_excep():  # 例外が発生する関数
    return 5 / 0


class PollsTest(TestCase):  # TestCaseの子クラス
    def test_func(self):  # テスト用のメソッド
        self.assertEqual(1, func_hoge())  # func_hogeは1を返すか確認
        self.assertNotEqual(1, func_fuga())  # func_fugaは1以外を返すか確認
        self.assertEqual(1, func_piyo())  # func_piyoはTrueを返すか確認

    def test_exception(self):  # 例外が発生するかテスト
        self.assertRaises(Exception, func_excep)  # 一行でOK
