from django.contrib.auth.models import AbstractUser,  Group, Permission
from django.db import models

class DuenoMascota(AbstractUser):
    id = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fechaNac = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    tiene_mascota= models.BooleanField(default=False)
    imagen_perfil = models.ImageField(upload_to='dueno_img/', blank=True, null=True)

    def __str__(self):
        return self.username
    
    
class TipoUsuario(models.Model):
    TIPOS_USUARIO = [
        ('dueno', 'Dueño de Mascota'),
        ('servicios', 'Ofrece Servicios'),
    ]
    id = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    usuario = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_usuario
    
class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    dueno = models.ForeignKey(DuenoMascota, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    fecha_nacimiento_mascota = models.DateField(null=True, blank=True)
    genero_mascota = models.CharField(max_length=20, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    color = models.CharField(max_length=100, blank=True)
    historial_medico = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='mascotas_img/', blank=True)
    identificacion = models.CharField(max_length=50, blank=True)
    vacunacion = models.TextField(blank=True)
    comportamiento = models.TextField(blank=True)
    alimentacion = models.TextField(blank=True)
    entrenamiento = models.TextField(blank=True)
    otros_cuidados = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
