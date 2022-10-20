from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ver_login, name="ver_login"),
    path('painel/', views.ver_painel, name="ver_painel"),
    path('cadastro/', views.ver_cadastro, name="ver_cadastro"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]