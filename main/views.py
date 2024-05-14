from django.shortcuts import render, redirect
from .models import Main


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def tarefas(request):
    return render(request, 'main/tarefas.html')


def conversas(request):
    grupos = Main.objects.all()
    return render(request, 'main/conversas.html', {'grupos': grupos})


def comunidades(request):
    return render(request, 'main/comunidades.html')


def busca(request):
    return render(request, 'main/busca.html')

