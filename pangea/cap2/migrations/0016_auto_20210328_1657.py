# Generated by Django 3.0.3 on 2021-03-28 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0015_auto_20210328_1657'),
        ('formulario', '0011_auto_20210328_1657'),
        ('ficha', '0004_auto_20210328_1657'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Componente',
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
