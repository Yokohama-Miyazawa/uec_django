from django.test import TestCase


def func_hoge():  # テスト対象の関数その1
    return 1


def func_fuga():  # テスト対象の関数その2
    return 0


class PollsTest(TestCase):  # TestCaseの子クラス
    def test_func(self):  # テスト用のメソッド
        self.assertEqual(1, func_hoge())  # func_hogeは1を返すか確認
        self.assertEqual(1, func_fuga())  # func_fugaは1を返すか確認
