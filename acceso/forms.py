from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DuenoMascota, Mascota, TipoUsuario
from captcha.fields import ReCaptchaField



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )
    
    
    
    

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,  
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Apellido'}),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
    )
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '999999999'}),
    )
    direccion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Dirección'}),
    )
    fechaNac = forms.DateField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control','type': 'date', 'placeholder': 'Fecha de Nacimiento'}),
    )
    genero = forms.ChoiceField(
        required=False,
        choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), 
        ('No especificar', 'No especificar'),
        ('Prefiero no decirlo', 'Prefiero no decirlo'),('Otro', 'Otro'),],
        widget=forms.Select(attrs={'class': 'form-control','placeholder': 'Selecciona tu género'}),
    )
  
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
    )
    imagen_perfil = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )
    captcha = ReCaptchaField()
    
    
    class Meta:
        model = DuenoMascota
        fields = ['username', 'first_name', 'last_name', 'email','telefono', 'imagen_perfil', 'password1', 'password2',]



class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = ['tipo_usuario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_usuario'].widget = forms.RadioSelect(choices=TipoUsuario.TIPOS_USUARIO)




class MascotaForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=150,  
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de mascota'}),
    )
    especie = forms.CharField(
        max_length=150,  
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especie'}),
    )
    raza = forms.CharField(
        max_length=150,  
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza'}),
    )
    fecha_nacimiento_mascota = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control','type': 'date', 'placeholder': 'Fecha de Nacimiento'}),
    )
    genero_mascota = forms.ChoiceField(
        choices=[('Macho', 'Macho'), ('Hembra', 'Hembra'), 
        ],
        widget=forms.Select(attrs={'class': 'form-control','placeholder': 'Selecciona el género de tu mascota'}),
    )
    color = forms.CharField(
        max_length=150,  
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
    )
    identificacion = forms.CharField(
        max_length=150,  
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identificación'}),
    )
    imagen = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento_mascota', 'genero_mascota', 'color',  'imagen', 'identificacion', ]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        label=''
    )