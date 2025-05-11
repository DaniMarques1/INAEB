from django import forms
from .models import Familia, Telefone, Parente, Entrega
from django.forms import inlineformset_factory, modelformset_factory
from django.forms import BaseModelFormSet
from django.core.exceptions import ValidationError
from collections import defaultdict

TelefoneFormSet = inlineformset_factory(
    Familia,
    Telefone,
    fields=('telefone',),
    extra=3,
    max_num=3,
    validate_max=True,
    can_delete=False
)

ParenteFormSet = inlineformset_factory(
    Familia,
    Parente,
    fields=(
        "nome",
        "data_nascimento",
        "parentesco",
        "instrucao",
        "profissao",
        "idade",
        "ocupacao",
    ),

    widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
    },

    extra=1,          
    can_delete=True,  
    validate_max=True,
    max_num=10,       
)

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia

        fields = "__all__" 

        widgets = {
            "status_atendimento": forms.RadioSelect(),  
            "inicio_atendimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "termino_atendimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "qtd_membros": forms.NumberInput(attrs={"min": 1}),
            "data_entrevista": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "data_nascimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "data_visita": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "obs_limpeza": forms.Textarea(attrs={"placeholder": "Observações sobre a limpeza da casa...", "rows": 6, "cols": 30,}),
            "obs_saneamento": forms.Textarea(attrs={"placeholder": "Observações sobre o saneamento da casa...", "rows": 6, "cols": 30,}),
            "obs_gerais": forms.Textarea(attrs={"placeholder": "Digite aqui..."}),
            'lixo': forms.RadioSelect(),
            'limpeza_casa': forms.RadioSelect(),
            'agua': forms.RadioSelect(),
            'esgoto': forms.RadioSelect(),
            'tipo_moradia': forms.RadioSelect(),
            'banheiro': forms.RadioSelect(),
            'construcao': forms.RadioSelect(),
            "televisor": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "geladeira": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "celular_smartphone_tablet": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "aparelho_som": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "maquina_lavar": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "carro_moto": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "dvd": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "computador_notebook": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "telefone_internet": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }

class BaseEntregaFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()

        if any(form.errors for form in self.forms):
            return

        requisicoes = defaultdict(int)

        for form in self.forms:
            if form.cleaned_data.get("DELETE"):
                continue

            produto    = form.cleaned_data["produto"]
            quantidade = form.cleaned_data["quantidade"]
            requisicoes[produto] += quantidade

        erros = []
        for produto, total in requisicoes.items():
            if produto.qtd_estoque < total:
                erros.append(
                    f"{produto.produto}: estoque disponível "
                    f"({produto.qtd_estoque}) < solicitado ({total})"
                )

        if erros:
            raise ValidationError(
                ["Cestas cadastradas insuficientes! Registre mais cestas."] + erros
            )
        
class EntregaForm(forms.ModelForm):
    data_doacao = forms.DateField(
        label="Data", widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Entrega
        fields = ["familia", "produto", "data_doacao", "quantidade"]
        widgets = {
            "familia": forms.Select(attrs={"class": "select-responsavel"}),
            "produto": forms.Select(),
            "data_doacao": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "quantidade": forms.NumberInput(attrs={"min": 1, "value": 1}),
        }
        error_messages = {            
            "familia":     {"required": "Preencha todos os campos"},
            "produto":     {"required": "Preencha todos os campos"},
            "data_doacao": {"required": "Preencha todos os campos"},
            "quantidade":  {"required": "Preencha todos os campos"},
        }
        
EntregaFormSet = modelformset_factory(
        Entrega,
        form=EntregaForm,
        formset=BaseEntregaFormSet,
        extra=0,          
        can_delete=True,  
        min_num=1,               
        validate_min=True,       
)