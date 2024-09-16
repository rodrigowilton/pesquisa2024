from django import forms
from .models import Pesquisa

class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = ['data', 'pesquisadora', 'bairro', 'sexo', 'idade', 'voto_espontaneo', 'voto_atual',  'avaliacao_prefeitura']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pesquisadora': forms.Select(attrs={'class': 'form-control'}),
            'bairro': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'idade': forms.Select(attrs={'class': 'form-control'}),
            'voto_espontaneo': forms.TextInput(attrs={'class': 'form-control'}),
            'voto_atual': forms.Select(attrs={'class': 'form-control'}),
            'avaliacao_prefeitura': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make voto_espontaneo optional
        self.fields['voto_espontaneo'].required = False
        # Add custom styles or attributes to form fields if needed
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
