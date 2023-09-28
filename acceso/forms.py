from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DuenoMascota, Mascota

class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(widget=forms.Textarea)
    fechaNac = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    genero = forms.ChoiceField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])

    class Meta:
        model = DuenoMascota
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'direccion', 'fechaNac', 'genero', 'password1', 'password2']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento_mascota', 'genero_mascota', 'color',  'imagen', 'identificacion', ]
