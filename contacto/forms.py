from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tu nombre aquí..'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Tu email..'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí..','class': 'form-control', 'rows': 4}),
        }
