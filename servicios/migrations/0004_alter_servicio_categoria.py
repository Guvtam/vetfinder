# Generated by Django 4.2.5 on 2023-09-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_alter_servicio_categoria_alter_servicio_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='categoria',
            field=models.CharField(choices=[('Veterinario', 'Veterinario'), ('Cuidado Dental', 'Cuidado Dental'), ('Servicios de Emergencia', 'Servicios de Emergencia'), ('Guarderías', 'Guarderías'), ('Paseo de Perros', 'Paseo de Perros'), ('Entrenamiento', 'Entrenamiento'), ('Parques para Perros', 'Parques para Perros'), ('Peluqueria', 'Peluqueria'), ('Adopciones', 'Adopciones')], max_length=100),
        ),
    ]
