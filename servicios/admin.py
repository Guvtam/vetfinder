from django.contrib import admin
from .models import Servicio, Calificacion

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'direccion', 'telefono', 'calificacion_promedio', 'total_reseñas']
    list_filter = ['categoria']
    search_fields = ['nombre', 'direccion']
    
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['servicio', 'usuario', 'calificacion', 'comentario']
    list_filter = ['servicio', 'usuario', 'calificacion']
    search_fields = ['servicio__nombre', 'usuario__username', 'comentario']