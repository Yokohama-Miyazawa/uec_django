from django.shortcuts import render
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Question, Choice

from django.views.generic import DetailView, ListView
from .forms import MyForm, VoteForm


def form_test(request):
    if request.method == "POST":
        form = MyForm(data=request.POST)
        if form.is_valid():
            message = '入力された内容は「'+form.cleaned_data['text']+'」です。'
        else:
            message = '無効なデータです。'
    else:
        form = MyForm()
        message = '文字を入力してください。'
    return render(request, 'polls/form.html', {
        'form': form,
        'message': message,
    })


def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = VoteForm(question=obj, data=request.POST)
        if form.is_valid():
            # 投票処理をここに書く
            return redirect('polls:results', pk)
    else:
        form = VoteForm(question=obj)
    return render(request, 'polls/detail.html', {
     'form': form,
     'question': obj
    })


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
         'question': question,
         'error_message': "選択肢が何も選ばれていません。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', pk)


class Index(ListView):
    template_name = 'polls/index.html'
    queryset = Question.objects.all()
    context_object_name = 'questions'


class Results(DetailView):
    template_name = 'polls/results.html'
    model = Question
    context_object_name = 'question'


index = Index.as_view()
results = Results.as_view()
