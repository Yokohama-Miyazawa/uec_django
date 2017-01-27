from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html', {
        'hoge': 'Tokyo',
        'fuga': 'Chofu<br><br><br>UEC',
    })
