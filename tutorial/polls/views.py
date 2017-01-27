from django.shortcuts import render
from django.utils.html import mark_safe


def index(request):
    return render(request, 'polls/index.html', {
        'hoge': 'Tokyo',
        'fuga': 'Chofu<br><br><br>UEC',
        'piyo': mark_safe('Chofu<br><br><br>UEC'),
    })
