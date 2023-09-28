from django import forms
from .models import Servicio, Calificacion

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'categoria', 'direccion', 'telefono', 'horario', 'descripcion', 'sitio_web', 'imagen']


class BusquedaForm(forms.Form):
    query = forms.CharField(max_length=100, label='Buscar por nombre')
    
class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['calificacion', 'comentario']
