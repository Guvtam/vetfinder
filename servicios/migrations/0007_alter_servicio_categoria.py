# Generated by Django 4.2.5 on 2023-10-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_remove_servicio_calificacion_promedio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='categoria',
            field=models.CharField(choices=[('Veterinario', 'Veterinario'), ('Cuidado Dental', 'Cuidado Dental'), ('Servicios de Emergencia', 'Servicios de Emergencia'), ('Guarderías', 'Guarderías'), ('Paseo de Perros', 'Paseo de Perros'), ('Entrenamiento', 'Entrenamiento'), ('Parques para Perros', 'Parques para Perros'), ('Peluqueria', 'Peluqueria'), ('Adopciones', 'Adopciones'), ('Alimentos Mascotas', 'Alimentos Mascotas')], max_length=100),
        ),
    ]
