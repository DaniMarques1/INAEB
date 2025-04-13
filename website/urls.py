from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("", redirect_to_menu, name="home"),
    
    path("menu/", menu, name="menu"),
    path("cadastro/cestas/", cadastro_cestas, name="cadastro_cestas"),
    path("cadastro/lista_familias/", lista_familias, name="lista_familias"),
    path("cadastro/formulario_familias/", formulario_familias, name="formulario_familias"),
    path("cadastro/entregas/", entregas, name="cadastro_entregas"),
    path("cadastro/lista_entregas/", lista_entregas, name="lista_entregas"),

    path('atualizar_cestas/', atualizar_cestas, name='atualizar_cestas'),
]
