from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.ver_login, name="login"),
    path('painel/', views.ver_painel, name="ver_painel")
]