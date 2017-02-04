from django.shortcuts import render
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import resolve_url  # resolve_url追加
from django.core.urlresolvers import reverse_lazy  # reverse_lazy追加
from django.views.generic.detail import SingleObjectMixin  # SingleObjectMixin

from .models import Question, Choice

from django.views.generic import DetailView, ListView, FormView  # FormView追加
from .forms import MyForm, VoteForm


class FormTest(FormView):  # 現在検討中の FormTest Class
    form_class = MyForm
    template_name = 'polls/form.html'

    def get_success_url(self):  # 正常にデータを受けた時飛ぶ先
        self.kwargs['pk'] = self.message
        return resolve_url('polls:forms', self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        self.message = self.kwargs['pk']  # urlに含まれている入力文字列を代入
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.message = request.POST['text']  # 入力文字列を代入
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = self.message
        return context

    def dispatch(self, request, *args, **kwargs):
        self.message = None  # 入力データ保持用のアトリビュート
        return super(FormTest, self).dispatch(request, *args, **kwargs)


class Detail(SingleObjectMixin, FormView):  # detail関数を置き換え
    model = Question
    form_class = VoteForm
    context_object_name = 'question'
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):  # GET時に質問を取得
        self.object = self.get_object()
        print(**kwargs)
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


form_test = FormTest.as_view()
detail = Detail.as_view()
index = Index.as_view()
results = Results.as_view()
