from django.contrib import admin
from .models import Mensaje, Comentario, Publicacion, GaleriaMascota, ComentarioUsuario

# Register your models here.
admin.site.register(Mensaje)
admin.site.register(Comentario)
admin.site.register(GaleriaMascota)
admin.site.register(Publicacion)
admin.site.register(ComentarioUsuario)