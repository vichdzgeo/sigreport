# Generated by Django 3.0.3 on 2021-08-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0036_sustanciasquimicasp_fase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listatipovehiculo',
            name='descripcion',
            field=models.CharField(max_length=1500, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='listatipovehiculo',
            name='tipo',
            field=models.CharField(max_length=1200, verbose_name='Tipo de vehículo'),
        ),
    ]
