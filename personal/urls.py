from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^projects/$', views.tutorials, name = 'projects'),
    url(r'^resume/$', views.resume, name = 'resume'),
    ]
