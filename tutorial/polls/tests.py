from django.test import TestCase


def func_hoge():  # テスト対象の関数その1
    return 1


class PollsTest(TestCase):  # TestCaseの子クラス
    def test_func(self):  # テスト用のメソッド
        self.assertEqual(1, func_hoge())  # func_hogeは1を返すか確認
