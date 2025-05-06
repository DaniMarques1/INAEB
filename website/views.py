from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from .forms import FamiliaForm, TelefoneFormSet, ParenteFormSet
from django.db.models import Value
from django.db.models.functions import Lower
from django.db.models import Count


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
    order_field   = request.GET.get('order_by', 'nome')
    status_filtro = request.GET.get('status')

    valid_fields = ['nome', 'data_nascimento', '-nome', '-data_nascimento']
    if order_field not in valid_fields:
        order_field = 'nome'

    queryset = (
        Familia.objects
        .annotate(total_membros=Count('parente'))     
    )

    if status_filtro in ['Ativa', 'Suspensa', 'Aguardando Vaga']:
        queryset = queryset.filter(status_atendimento=status_filtro)

    if 'nome' in order_field:
        descending = order_field.startswith('-')
        queryset = queryset.annotate(nome_lower=Lower('nome'))
        queryset = queryset.order_by('-nome_lower' if descending else 'nome_lower')
    else:
        queryset = queryset.order_by(order_field)

    queryset = queryset.prefetch_related('telefone_set')

    context = {
        'dados_familia': queryset,
        'range': range(20),
        'total_familias': Familia.objects.count(),
        'total_ativas': Familia.objects.filter(status_atendimento="Ativa").count(),
        'total_aguardando': Familia.objects.filter(status_atendimento="Aguardando Vaga").count(),
        'total_suspensas': Familia.objects.filter(status_atendimento="Suspensa").count(),
        'status_filtro': status_filtro,
    }
    return render(request, "lista_familias.html", context)

# @login_required(login_url='/login/')
def lista_entregas(request):
    return render(request, "lista_entregas.html")

# @login_required(login_url='/login/')
def entregas(request):
    return render(request, "cadastro_entregas.html")

# @login_required(login_url='/login/')
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

# @login_required(login_url='/login/')
def criar_familia(request):
    if request.method == "POST":
        form        = FamiliaForm(request.POST)
        telefones   = TelefoneFormSet(request.POST)
        parentes    = ParenteFormSet(request.POST)

        if form.is_valid() and telefones.is_valid() and parentes.is_valid():
            familia = form.save()

            telefones.instance = familia
            telefones.save()

            parentes.instance = familia
            parentes.save()

            messages.success(request, "Família cadastrada com sucesso!")
            return redirect("lista_familias")
        messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form      = FamiliaForm()
        telefones = TelefoneFormSet()
        parentes  = ParenteFormSet()

    return render(
        request,
        "formulario_familias.html",
        {"form": form, "formset": telefones, "parente_formset": parentes},
    )


# @login_required(login_url='/login/')
def editar_familia(request, pk):
    familia = get_object_or_404(Familia, pk=pk)

    if request.method == "POST":
        form      = FamiliaForm(request.POST, instance=familia)
        telefones = TelefoneFormSet(request.POST, instance=familia)
        parentes  = ParenteFormSet(request.POST, instance=familia)

        if form.is_valid() and telefones.is_valid() and parentes.is_valid():
            form.save()
            telefones.save()
            parentes.save()
            messages.success(request, "Dados atualizados com sucesso!")
            return redirect("lista_familias")
        messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form      = FamiliaForm(instance=familia)
        telefones = TelefoneFormSet(instance=familia)
        parentes  = ParenteFormSet(instance=familia)

    return render(
        request,
        "formulario_familias.html",
        {"form": form, "formset": telefones, "parente_formset": parentes},
    )