from multiprocessing import context
from pickletools import read_unicodestring1
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ongoingfront.models import Usuario

def ver_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request, 'Usuário já possui cadastro!')
            return HttpResponseRedirect('http://127.0.0.1:8000/cadastro')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso! Faça login abaixo')
        return HttpResponseRedirect('http://127.0.0.1:8000/')
        
        

def ver_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('/painel')
        else:
            messages.error(request, 'Usuário ou senha incorreto!')
    return HttpResponseRedirect('http://127.0.0.1:8000/')

@login_required(login_url='/')
def ver_painel(request):
    
    # print(Usuario.objects.filter(turno="T1")[0].nome)

    list_t1 = Usuario.objects.all()

    context = {
        'list_t1': list_t1
    }

    return render(request, 'painel.html', context)
