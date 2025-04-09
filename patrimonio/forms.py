from django import forms
from .models import Patrimonio

class PatrimonioForm(forms.ModelForm):
    class Meta:
        model = Patrimonio
        fields = '__all__'
        widgets = {
            'pat_codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'pat_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'pat_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'pat_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'pat_nse': forms.TextInput(attrs={'class': 'form-control'}),
            'pat_data_registrado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pat_data_aquisicao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pat_valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'pat_descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pat_categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'pat_status': forms.Select(attrs={'class': 'form-control'}),
        }