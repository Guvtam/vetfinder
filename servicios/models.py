from django.db import models

from acceso.models import DuenoMascota

class Servicio(models.Model):
    CATEGORIAS = [
        ('Veterinario', 'Veterinario'),
        ('Cuidado Dental', 'Cuidado Dental'),
        ('Servicios de Emergencia', 'Servicios de Emergencia'),
        ('Guarderías', 'Guarderías'),
        ('Paseo de Perros', 'Paseo de Perros'),
        ('Entrenamiento', 'Entrenamiento'),
        ('Parques para Perros', 'Parques para Perros'),
        ('Peluqueria', 'Peluqueria'),
        ('Adopciones', 'Adopciones'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    horario = models.TextField()
    descripcion = models.TextField(blank=True)
    sitio_web = models.URLField(blank=True)
    imagen = models.ImageField(upload_to='servicios_img/', blank=True)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_reseñas = models.PositiveIntegerField(default=0)
    usuario=models.ForeignKey(DuenoMascota,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(choices=[(1, '1 Estrella'), (2, '2 Estrellas'), (3, '3 Estrellas'), (4, '4 Estrellas'), (5, '5 Estrellas')])
    comentario = models.TextField()

    def __str__(self):
        return f"Calificación de {self.servicio.nombre} por {self.usuario.username}"
    