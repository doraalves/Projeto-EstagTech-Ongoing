from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_login, name='user_login'),
    path('esqueci_senha/', views.esqueci_senha, name='esqueci_senha')
]