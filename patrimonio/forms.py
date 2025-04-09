from django import forms
from .models import Patrimonio
from .models import Emprestimo

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

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        widgets = {
            'emp_pessoa': forms.Select(attrs={'class': 'form-control'}),
            'emp_criado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'emp_efetivado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'emp_prazo': forms.NumberInput(attrs={'class': 'form-control'}),
            'emp_devolvido': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'emp_status': forms.Select(attrs={'class': 'form-control'}),
            'emp_anotacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }