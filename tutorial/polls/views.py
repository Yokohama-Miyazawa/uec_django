from django.shortcuts import render
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy  # reverse_lazy追加

from .models import Question, Choice

from django.views.generic import DetailView, ListView, FormView  # FormView追加
from .forms import MyForm, VoteForm


class FormTest(FormView):  # FormTest Class を作成。form_test関数は削除
    form_class = MyForm  # 使う Form Class を指定
    template_name = 'polls/form.html'  # 使うTemplateを指定
    success_url = reverse_lazy('polls:index')  # POST成功時に飛ぶ先を指定


def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = VoteForm(question=obj, data=request.POST)
        if form.is_valid():
            form.vote()
            return redirect('polls:results', pk)
    else:
        form = VoteForm(question=obj)
    return render(request, 'polls/detail.html', {
     'form': form,
     'question': obj
    })


class Index(ListView):
    template_name = 'polls/index.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'


class Results(DetailView):
    template_name = 'polls/results.html'
    model = Question
    context_object_name = 'question'

form_test = FormTest.as_view()  # form_test関数の代わりにこのメソッドの返り値を返す
index = Index.as_view()
results = Results.as_view()
