# Generated by Django 4.2.5 on 2023-11-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0002_mensaje_tipo_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentariousuario',
            name='tipo_mensaje',
            field=models.CharField(choices=[('Publico', 'Publico'), ('Privado', 'Privado')], default=None, max_length=20),
        ),
    ]
