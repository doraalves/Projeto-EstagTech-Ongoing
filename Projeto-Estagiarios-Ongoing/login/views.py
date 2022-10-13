from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_login(request):
    return render(request, 'index.html')

def esqueci_senha (request):
    return HttpResponse('Esqueci a senha')