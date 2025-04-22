from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from .forms import FamiliaForm, TelefoneFormSet


def redirect_to_menu(request):
    """Redirect root URL to /menu."""
    return redirect("menu")

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

# @login_required(login_url='/login/')
def menu(request):
    return render(request, "menu.html")

# @login_required(login_url='/login/')
def cadastro_cestas(request):

    estoque_produtos = Produto.objects.all()
    items_cesta = ItemCesta.objects.all()

    context = {
        'range': range(30),
        'items_cesta': items_cesta,
        'estoque_produtos': estoque_produtos
    }
    return render(request, "cadastro_cestas.html", context)

# @login_required(login_url='/login/')
def lista_familias(request):
    order_field = request.GET.get('order_by', 'nome')

    valid_fields = ['nome', 'data_nascimento', '-nome', '-data_nascimento']
    if order_field not in valid_fields:
        order_field = 'nome'
        
    dados_familia = Familia.objects.all().prefetch_related('telefone_set').order_by(order_field)

    context = {
        'dados_familia': dados_familia,
        'range': range(20)
    }
    return render(request, "lista_familias.html", context)

# @login_required(login_url='/login/')
def lista_entregas(request):
    return render(request, "lista_entregas.html")

# @login_required(login_url='/login/')
def formulario_familias(request):

    dados_formulario = Familia.objects.all()

    context = {
        'dados_formulario': dados_formulario,
        'Familia': Familia
    }
    return render(request, "formulario_familias.html", context)

# @login_required(login_url='/login/')
def entregas(request):
    return render(request, "cadastro_entregas.html")

def atualizar_cestas(request):
    if request.method == 'POST':
        quantity = request.POST.get('doacao_quantidade')
        
        if quantity:
            quantity = int(quantity)

            produto = Produto.objects.get(pk=1)
            produto.qtd_estoque += quantity
            produto.save()

            doacao = Doacao.objects.create(
                produto=produto,
                quantidade=quantity,
                data_entrada=timezone.now()
            )
            doacao.save()

            messages.success(request, f'{quantity} cesta(s) cadastradas com sucesso!')

        return redirect('cadastro_cestas')
    
    return redirect('cadastro_cestas')

def criar_familia(request):
    if request.method == "POST":
        form = FamiliaForm(request.POST)
        formset = TelefoneFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            familia = form.save()
            formset.instance = familia
            formset.save()
            messages.success(request, "Família cadastrada com sucesso!")
            return redirect("lista_familias")
        else:
            messages.error(request, "Por favor, preencha todos os campos marcados com asterisco (*) .")
    else:
        form = FamiliaForm()
        formset = TelefoneFormSet()
    return render(request, "formulario_familias.html", {
        "form": form,
        "formset": formset,
    })

def editar_familia(request, pk):
    familia = get_object_or_404(Familia, pk=pk)
    if request.method == "POST":
        form = FamiliaForm(request.POST, instance=familia)
        formset = TelefoneFormSet(request.POST, instance=familia)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect("lista_familias")
        else:
            messages.error(request, "Por favor, preencha todos os campos marcados com asterisco (*) .")
    else:
        form = FamiliaForm(instance=familia)
        formset = TelefoneFormSet(instance=familia)
    return render(request, "formulario_familias.html", {
        "form": form,
        "formset": formset,
    })