# Generated by Django 3.0.3 on 2021-03-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0017_auto_20210328_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='tipo',
            field=models.CharField(choices=[('Tipo 1', 'Tipo 1'), ('Tipo 2', 'Tipo 2'), ('Tipo 3', 'Tipo 3')], max_length=500, verbose_name='Tipo de módulo'),
        ),
    ]
