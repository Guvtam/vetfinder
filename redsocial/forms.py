from django import forms
from .models import Publicacion, GaleriaMascota, Comentario, Mensaje , ComentarioUsuario

class PublicacionForm(forms.ModelForm):
    # Define un campo de elección para el tipo de actividad
    tipo_actividad = forms.ChoiceField(
        choices=Publicacion.TIPOS_ACTIVIDAD,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    contenido = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comparte algo...'}),
    )

    class Meta:
        model = Publicacion
        fields = ['tipo_actividad', 'contenido']
        labels = {
            'tipo_actividad': 'Tipo de Actividad',
            'contenido': 'Contenido',
        }




class BusquedaAmigoForm(forms.Form):
    OPTIONS = [
        ('usuario', 'Nombre de Usuario'),
        ('mascota', 'Nombre de Mascota'),
    ]

    query = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingresa nombre de usuario o mascota'}),
    )

    search_by = forms.ChoiceField(
        choices=OPTIONS,
        widget=forms.RadioSelect,
        required=True,
        initial='usuario',  # Puedes establecer el valor inicial aquí
    )
    
class GaleriaMascotaForm(forms.ModelForm):
    class Meta:
        model = GaleriaMascota
        fields = ['imagen', 'descripcion']
        widgets = {
        'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrega una descripción'}),
    }
        



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario  # Asocia el formulario con el modelo Comentario
        fields = ['contenido']  # Especifica los campos que se mostrarán en el formulario

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control','placeholder':'Agrega un comentario aquí..'}),
        }
        labels = {
            'contenido': 'Comentario',
        }

'''class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí...'}),
        }'''

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido', 'tipo_mensaje']  # Agrega el campo 'tipo_mensaje' al formulario

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí...'}),
            'tipo_mensaje': forms.Select(attrs={'class': 'form-control'}),  # Agrega un widget para el campo 'tipo_mensaje'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_mensaje'].widget.choices = Mensaje.TIPO_MENSAJE  # Configura las opciones para el campo 'tipo_mensaje'



class ComentarioUsuarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioUsuario
        fields = ['contenido']

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribele un mensaje aquí...'}),
        }

