from django import forms
from .models import Servicio, Calificacion

class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del servicio'}),
    )
    categoria = forms.ChoiceField(
        choices=Servicio.CATEGORIAS,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona la categoría'}),
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

    class Meta:
        model = Servicio
        fields = ['nombre', 'categoria', 'direccion', 'telefono', 'horario', 'descripcion', 'sitio_web', 'imagen']



class BusquedaForm(forms.Form):
    CATEGORIAS = [('', 'Cualquier categoría')] + Servicio.CATEGORIAS
    CALIFICACIONES = [('', 'Cualquier calificación'), (1, '1 Estrella'), (2, '2 Estrellas'), (3, '3 Estrellas'), (4, '4 Estrellas'), (5, '5 Estrellas')]

    query = forms.CharField(
    max_length=100,
    label='Buscar por nombre',
    required=False,
    widget=forms.TextInput(attrs={'placeholder': 'Busca tu servicio'}),
)
    categoria = forms.ChoiceField(choices=CATEGORIAS, label='Filtrar por categoría', required=False)
    calificacion = forms.ChoiceField(choices=CALIFICACIONES, label='Filtrar por calificación', required=False)
    
   


    
class CalificacionForm(forms.ModelForm):
    calificacion = forms.ChoiceField(
        choices=[(1, '1 Estrella'), (2, '2 Estrellas'), (3, '3 Estrellas'), (4, '4 Estrellas'), (5, '5 Estrellas')],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        required=False,
    )
    class Meta:
        model = Calificacion
        fields = ['calificacion', 'comentario']
        
