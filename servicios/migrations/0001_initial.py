# Generated by Django 4.2.5 on 2023-09-27 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
                ('horario', models.TextField()),
                ('descripcion', models.TextField(blank=True)),
                ('sitio_web', models.URLField(blank=True)),
                ('imagen', models.ImageField(blank=True, upload_to='servicios/')),
                ('calificacion_promedio', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('total_reseñas', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveIntegerField(choices=[(1, '1 Estrella'), (2, '2 Estrellas'), (3, '3 Estrellas'), (4, '4 Estrellas'), (5, '5 Estrellas')], default=0)),
                ('comentario', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
