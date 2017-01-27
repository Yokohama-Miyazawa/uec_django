from django.http import HttpResponse


def index(request):
    return HttpResponse("テストです。Viewがレスポンスを直接返してます。")
