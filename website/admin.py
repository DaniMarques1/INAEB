from django.contrib import admin
from .models import *

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    pass

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('familia', 'telefone')
    pass

@admin.register(Parente)
class ParenteAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'qtd_estoque')
    pass

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data_entrada')
    pass

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'familia', 'quantidade', 'data_doacao')
    pass

@admin.register(ItemCesta)
class ItemCestaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade')
    pass