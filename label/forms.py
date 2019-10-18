from django.forms import ModelForm, TextInput, Select, Textarea

from .models import FolhaEtiqueta, FolhaEtiquetaItens


class FolhaEtiquetaForm(ModelForm):
    class Meta:
        model = FolhaEtiqueta
        fields = ['nome', 'modelo', ]

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'modelo': Select(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
        }


class FolhaEtiquetaItensForm(ModelForm):
    class Meta:
        model = FolhaEtiquetaItens
        fields = ['nome', 'descricao', 'docura']

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'descricao': Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'docura': Select(attrs={'class': 'form-control', 'placeholder': 'Doçura'}),
        }
