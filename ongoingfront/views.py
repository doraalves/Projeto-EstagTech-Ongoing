from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

def ver_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user = authenticate(email=email, password=senha)

        if user:
            return HttpResponse("autenticado")
        else:
            return HttpResponse("Email ou senha invalido")


def ver_painel(request):
    return render(request, 'painel.html')

