from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("", redirect_to_menu, name="home"),
    
    path("menu/", menu, name="menu"),
    path("cadastro/cestas/", cadastro_cestas, name="cadastro_cestas"),
    path("cadastro/familias/", cadastro_familias, name="cadastro_familias"),
    path("cadastro/produtos/", cadastro_produtos, name="cadastro_produtos"),
]
