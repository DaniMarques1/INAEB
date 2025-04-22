from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("", redirect_to_menu, name="home"),
    
    # Menu principal
    path("menu/", menu, name="menu"),

    # CESTAS
    path("cadastro/cestas/", cadastro_cestas, name="cadastro_cestas"),
    path("atualizar_cestas/", atualizar_cestas, name="atualizar_cestas"),

    # FAMÍLIAS
    path("cadastro/familias/", lista_familias, name="lista_familias"),            # listagem
    path("cadastro/familias/novo/", criar_familia, name="criar_familia"),         # formulário de criação
    path("cadastro/familias/<int:pk>/editar/", editar_familia, name="editar_familia"),

    # ENTREGAS
    path("cadastro/entregas/", entregas, name="cadastro_entregas"),
    path("cadastro/lista_entregas/", lista_entregas, name="lista_entregas"),
]
