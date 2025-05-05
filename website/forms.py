from django import forms
from .models import Familia, Telefone
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
        }