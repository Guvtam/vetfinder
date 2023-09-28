from django import forms
from .models import Servicio  # Importa el modelo Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'categoria', 'direccion', 'telefono', 'horario', 'descripcion', 'sitio_web', 'imagen']

