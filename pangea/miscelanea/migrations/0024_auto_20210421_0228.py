# Generated by Django 3.0.3 on 2021-04-21 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0023_auto_20210421_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obraslineales',
            name='tipo',
            field=models.CharField(max_length=280, verbose_name='Tipo de obra lineal'),
        ),
    ]
