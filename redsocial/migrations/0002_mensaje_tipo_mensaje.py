# Generated by Django 4.2.5 on 2023-11-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='tipo_mensaje',
            field=models.CharField(choices=[('Publico', 'Publico'), ('Privado', 'Privado')], default=None, max_length=20),
        ),
    ]
