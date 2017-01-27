from django.shortcuts import render
from django.utils.html import mark_safe
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Question, Choice

from django.views.generic import DetailView, ListView


def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {
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
