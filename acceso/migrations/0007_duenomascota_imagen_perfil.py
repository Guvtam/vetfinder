# Generated by Django 4.2.5 on 2023-10-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0006_duenomascota_tiene_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='duenomascota',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='dueno_img/'),
        ),
    ]
