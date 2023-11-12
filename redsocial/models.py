from django.db import models
from acceso.models import DuenoMascota, Mascota


class Publicacion(models.Model):
    TIPOS_ACTIVIDAD = [
        ('comida', 'Comida'),
        ('ejercicio', 'Ejercicio'),
        ('viaje', 'Viaje'),
        ('otros', 'Otros'),
    ]
    autor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    contenido = models.TextField()
    tipo_actividad = models.CharField(max_length=10, choices=TIPOS_ACTIVIDAD, default=None)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

#modelo para guardar las fotos
class GaleriaMascota(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    autor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='mascota_galeria/', blank=True, null=True)
    video = models.FileField(upload_to='mascota_galeria/', blank=True, null=True)
    descripcion = models.TextField()
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
   
    
    #modelo comentario imagenes 
class Comentario(models.Model):
    autor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    contenido = models.TextField(default=None)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ForeignKey(GaleriaMascota, default=None,on_delete=models.CASCADE)
    
    




'''class Mensaje(models.Model):
    emisor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.emisor.username} a {self.receptor.nombre}"
    '''


class Mensaje(models.Model):
    TIPO_MENSAJE = [
        ('Publico', 'Publico'),
        ('Privado', 'Privado'),
    ]
    emisor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    tipo_mensaje = models.CharField(max_length=20, choices=TIPO_MENSAJE, default=None)  

    def __str__(self):
        return f"mensaje de {self.emisor.username} a {self.receptor.nombre}"

    
class ComentarioUsuario(models.Model):
    emisor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE, related_name='comentarios_enviados')
    receptor = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE, related_name='comentarios_recibidos')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.emisor.username} a {self.receptor.username}"
    