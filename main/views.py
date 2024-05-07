from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def tarefas(request):
    return render(request, 'main/tarefas.html')


def conversas(request):
    return render(request, 'main/conversas.html')


def comunidades(request):
    return render(request, 'main/comunidades.html')


def busca(request):
    return render(request, 'main/busca.html')
