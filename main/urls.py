from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('conversas/', views.conversas, name='conversas'),
    path('comunidades/', views.comunidades, name='comunidades'),
    path('busca/', views.busca, name='busca'),
]
