# Generated by Django 3.0.3 on 2021-03-09 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0006_ficha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superficieobras',
            name='etapa',
        ),
        migrations.DeleteModel(
            name='Ficha',
        ),
    ]
