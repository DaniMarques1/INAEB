from django import forms
from .models import Familia, Telefone, Parente
from django.forms import inlineformset_factory

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

    extra=1,          # 1 formulário em branco exibido
    can_delete=True,  # permite remover
    validate_max=True,
    max_num=10,       # ajuste como quiser
)

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia

        fields = "__all__" 

        widgets = {
            "status_atendimento": forms.RadioSelect(),  # força <input type="radio">
            "inicio_atendimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "termino_atendimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
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