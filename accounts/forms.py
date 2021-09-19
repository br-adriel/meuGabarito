from django import forms
from django.contrib.auth.models import User
from django.forms import fields


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'last_name' : 'Sobrenome'
        }
        help_texts = {
            'email' : 'Adiocione um endereço de email para poder recuperar sua senha caso a esqueça.'
        }
