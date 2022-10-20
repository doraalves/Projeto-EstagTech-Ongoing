from pickletools import read_unicodestring1
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def ver_cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Esse usuário ja existe')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso')
        

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

@login_required
def ver_painel(request):
    return render(request, 'painel.html')
