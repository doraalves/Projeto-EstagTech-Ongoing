from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from ongoingfront.models import Usuario

def ver_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('name')
        respon = request.POST.get('responsibility')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(name=username).first()

        if user:
            return HttpResponse('Esse usuário ja existe')
        
        user = User.objects.create_user(name=username, responsibility=respon, email=email, password=password)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso')
        

def ver_login(request):
    # if request.method == "GET":
        return render(request, 'login.html')
    # else:
    #     email = request.POST.get("email")
    #     senha = request.POST.get("senha")

    #     user = authenticate(email=email, password=senha)

    #     if user:
    #         return HttpResponse("autenticado")
    #     return HttpResponse("Email ou senha invalido")


def ver_painel(request):
    return render(request, 'painel.html')
