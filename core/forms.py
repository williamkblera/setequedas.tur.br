from django import forms

from .models import News

class CadastroNewsletter(forms.Form):
    email = forms.EmailField(
        label='Email'
    )
