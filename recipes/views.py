from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):  # isso aqui é uma view /usuario solicita
    # aqui atribiu uma string no site
    return render(request, 'recipes/home.html', context={
        'name': 'Ropdrigo'
    })
# response é oque o servidor retorna


def contato(request):  # isso aqui é uma view /usuario solicita
    return render(request, 'recipes/contato.html')


def sobre(request):  # isso aqui é uma view /usuario solicita
    return HttpResponse('sobre')
