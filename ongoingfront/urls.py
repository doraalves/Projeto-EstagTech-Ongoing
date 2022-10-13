from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.ver_login, name="ver_ver_login"),
    path('painel/', views.ver_painel, name="ver_painel")
]