# Generated by Django 4.2.5 on 2023-09-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0004_alter_duenomascota_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='mascotas_img/'),
        ),
    ]
