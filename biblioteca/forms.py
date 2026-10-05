from django import forms

from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "ano_publicacao", "disponivel"]
        widgets = {
            "ano_publicacao": forms.NumberInput(attrs={"min": 0}),
        }
