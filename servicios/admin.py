from django.contrib import admin
from .models import Servicio

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'direccion', 'telefono', 'calificacion_promedio', 'total_reseñas']
    list_filter = ['categoria']
    search_fields = ['nombre', 'direccion']