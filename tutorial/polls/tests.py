from datetime import timedelta  # 時間差を測る為に追加

from django.test import TestCase
from django.utils import timezone  # 現在時刻確認の為追加

from .models import Question  # Question Modelに対しテストを実行する。


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

    def test_was_published_recently(self):
        # 一日よりも少しだけ古い
        obj = Question(pub_date=timezone.now() - timedelta(days=1, minutes=1))
        self.assertFalse(obj.was_published_recently(), '一日と1分前に公開')
        # 一日よりも少しだけ新しい
        obj = Question(pub_date=timezone.now() -
                       timedelta(days=1) + timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), '一日と1分後に公開')
        # つい最近公開
        obj = Question(pub_date=timezone.now() - timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), '1分前に公開')
        # もうすぐ公開
        obj = Question(pub_date=timezone.now() + timedelta(minutes=1))
        self.assertFalse(obj.was_published_recently(), '1分後に公開')
