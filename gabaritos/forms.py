from django import forms
from .models import Gabarito


class CriarGabaritoForm(forms.ModelForm):
    class Meta:
        model = Gabarito
        fields = ('nome', 'tamanho', 'indice')
        help_texts = {
            'tamanho' : 'Número de questões do seu gabarito.',
            'indice' : 'O número da primeira questão.',
        }


class RenomearGabaritoForm(forms.ModelForm):
    class Meta:
        model = Gabarito
        fields = ('nome',)
        labels = {
            'nome' : 'Novo nome',
        }
