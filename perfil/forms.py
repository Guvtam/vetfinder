from django import forms
from django.contrib.auth.forms import UserChangeForm
from acceso.models import DuenoMascota, Mascota
from servicios.models import Servicio

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
            ('','Seleccionar Genero'),
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
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




class EditarServicioForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
    )
    categoria = forms.ChoiceField(
        choices=Servicio.CATEGORIAS,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
    )
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
    )
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
    )
    horario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horario'}),
    )
    descripcion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        required=False,  
    )
    sitio_web = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Sitio web'}),
        required=False,  
    )
    imagen = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False,  
    )

    class Meta:
        model = Servicio
        fields = ['nombre', 'categoria', 'direccion', 'telefono', 'horario', 'descripcion', 'sitio_web', 'imagen']




class EditarMascotaForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
    )
    especie = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especie'}),
    )
    raza = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza'}),
    )
    fecha_nacimiento_mascota = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de Nacimiento'}),
        required=False,
    )
    genero_mascota = forms.ChoiceField(
        choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')],
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Género'}),
    )
    color = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
        required=False,
    )
    
    imagen = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False,
    )

    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento_mascota', 'genero_mascota', 'color', 'imagen']
