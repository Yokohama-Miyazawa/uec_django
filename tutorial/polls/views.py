from django.shortcuts import render
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy  # reverse_lazy追加
from django.shortcuts import resolve_url  # resolve_url追加
from django.views.generic.detail import SingleObjectMixin
# SingleObjectMixin追加。Modelのインスタンス取得に使う

from .models import Question, Choice

from django.views.generic import DetailView, ListView, FormView  # FormView追加
from .forms import MyForm, VoteForm


class FormTest(FormView):  # FormTest Class を作成。form_test関数は削除
    form_class = MyForm  # 使う Form Class を指定
    template_name = 'polls/form.html'  # 使うTemplateを指定
    success_url = reverse_lazy('polls:index')  # POST成功時に飛ぶ先を指定


class Detail(SingleObjectMixin, FormView):  # detail関数を置き換え
    model = Question  # 使うModelを指定
    form_class = VoteForm  # 使う Form Class を指定
    context_object_name = 'question'  # Templateに送ったデータが載る場所
    template_name = 'polls/detail.html'  # 使うTemplateを指定

    def get(self, request, *args, **kwargs):  # GET時に質問を取得
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # POST時に質問を取得
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):  # VoteFormに渡す引数(選択肢)を取得
        kwargs = super().get_form_kwargs()
        kwargs['question'] = self.object
        return kwargs

    def form_valid(self, form):  # POSTで受けたデータが正しい時の処理
        form.vote()
        return super().form_valid(form)

    def get_success_url(self):  # 正常にデータを受けた時飛ぶ先
        return resolve_url('polls:results', self.kwargs['pk'])


class Index(ListView):
    template_name = 'polls/index.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'


class Results(DetailView):
    template_name = 'polls/results.html'
    model = Question
    context_object_name = 'question'

form_test = FormTest.as_view()  # form_test関数の代わりにこのメソッドの返り値を返す
detail = Detail.as_view()  # detail関数の代わりにこのメソッドの返り値を返す
index = Index.as_view()
results = Results.as_view()
