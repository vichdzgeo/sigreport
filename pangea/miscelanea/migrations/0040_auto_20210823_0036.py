# Generated by Django 3.0.3 on 2021-08-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0039_auto_20210820_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListInsEsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Instalación especial')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Abreviatura')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Lista de instalaciones especiales y abreviaturas',
                'verbose_name_plural': 'Lista de instalaciones especiales y abreviaturas',
                'ordering': ['tipo'],
            },
        ),
        migrations.AlterField(
            model_name='listafrecact_scrc',
            name='descripcion',
            field=models.CharField(max_length=3000, verbose_name='Descripcion'),
        ),
    ]
