import datetime
from django.db import models
from django.utils import timezone


class QuestionQuerySet(models.query.QuerySet):  # QuerySet拡張用のクラス
    def is_published(self):
        return self.filter(pub_date__lte=timezone.now())


class Question(models.Model):
    class Meta:
        verbose_name = '質問'
        verbose_name_plural = '質問の複数形'
        ordering = ['question_text', 'pub_date']

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 拡張されたQuerySetを使う様に変更
    objects = models.Manager.from_queryset(QuestionQuerySet)()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_discription = '24時間以内の公開'

    @classmethod
    def get_published_data(cls):  # 新たに追加したメソッド1
        return cls.objects.filter(pub_date__lte=timezone.now())

    @classmethod
    def get_published_data_extend_queryset(cls):  # 新たに追加したメソッド2
        return cls.objects.is_published()


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
