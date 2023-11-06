# Generated by Django 4.2.5 on 2023-11-03 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('redsocial', '0004_alter_mensaje_emisor_alter_mensaje_receptor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_enviados', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_recibidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
