from django.shortcuts import render
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import resolve_url
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages  # messagesを使う為にimport

from .models import Question, Choice

from django.views.generic import DetailView, ListView, FormView
from .forms import MyForm, VoteForm


class FormTest(FormView):
    form_class = MyForm
    template_name = 'polls/form.html'
    success_url = reverse_lazy('polls:index')


class Detail(SingleObjectMixin, FormView):
    model = Question
    form_class = VoteForm
    context_object_name = 'question'
    template_name = 'polls/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['question'] = self.object
        return kwargs

    def form_valid(self, form):  # このメソッドを変更
        form.vote()
        choice = form.cleaned_data['choice']  # 投票したデータを変数choiceに代入
        messages.success(self.request, '"%s"に投票しました' % choice)
        # choiceの内容をmessages.success関数で表示
        return super().form_valid(form)

    def get_success_url(self):
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
