from django.db import models
from django.contrib.auth.models import User

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre