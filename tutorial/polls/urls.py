from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'(?P<pk>\d+)/results$', views.results, name='results'),
    url(r'^form/(?P<pk>(\w|\W)*)$', views.form_test, name='forms'),
    # urlに入力文字列が入る
]
