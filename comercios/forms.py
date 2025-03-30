
from django import forms
from .models import Comercio


class RegistroComercio(forms.ModelForm):
    
    class Meta:
        model = Comercio
        fields = '__all__'
        widgets = {
            'nombre_comercio': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
