# Generated by Django 3.0.3 on 2021-09-14 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0063_auto_20210913_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frecuenciaactcom',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='Jornadas/etapa'),
        ),
    ]