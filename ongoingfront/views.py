from django.shortcuts import render
from django.http import HttpResponse

def ver_login(request):
    return render(request, 'login.html')

def ver_painel(request):
    return render(request, 'painel.html')

def ver_cadastro(request):
    return render(request, 'cadastro.html')
