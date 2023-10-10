from django import forms
from django.contrib.auth.forms import UserChangeForm
from acceso.models import DuenoMascota

class EditarPerfilForm(UserChangeForm):
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
    )
    direccion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
    )
    fechaNac = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de Nacimiento'}),
    )
    genero = forms.ChoiceField(
        required=False,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No especificar', 'No especificar'),
            ('Prefiero no decirlo', 'Prefiero no decirlo'),
            ('Otro', 'Otro'),
        ],
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona tu género'}),
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    imagen_perfil = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )
    

    class Meta:
        model = DuenoMascota
        fields = ('telefono', 'direccion', 'fechaNac', 'genero', 'first_name', 'last_name', 'email', 'imagen_perfil')
