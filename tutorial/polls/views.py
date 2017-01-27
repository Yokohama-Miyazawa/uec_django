from django.shortcuts import render
from django.utils.html import mark_safe

from .models import Question


def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all()
    })
