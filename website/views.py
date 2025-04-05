from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('menu')
    
    if 'next' in request.GET:
        messages.warning(request, "Você deve fazer login para acessar a página desejada.")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') or 'menu')
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")
    
    return render(request, 'login.html')

def redirect_to_menu(request):
    """Redirect root URL to /menu."""
    return redirect("menu")

# @login_required(login_url='/login/')
def menu(request):
    return render(request, "menu.html")

# @login_required(login_url='/login/')
def cadastro_cestas(request):
    return render(request, "cadastro_cestas.html")

# @login_required(login_url='/login/')
def lista_familias(request):
    context = {
        'range': range(20)  # This creates a list of integers from 0 to 19
    }
    return render(request, "lista_familias.html", context)

# @login_required(login_url='/login/')
def lista_entregas(request):
    return render(request, "lista_entregas.html")

# @login_required(login_url='/login/')
def formulario_familias(request):
    return render(request, "formulario_familias.html")

# @login_required(login_url='/login/')
def entregas(request):
    return render(request, "cadastro_entregas.html")
