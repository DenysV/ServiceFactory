from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    url(r'^login/(?P<pk>\d+)/index/$', views.index, name = 'index'),
    url(r'^$/(?P<pk>\d+)/tareas/$', views.tarea, name = 'tarea'),
    url(r'^$/(?P<pk>\d+)/horas/$', views.horas, name = 'horas'),
]
