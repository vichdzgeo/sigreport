# Generated by Django 3.0.3 on 2021-03-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0006_especieflores_insumoslista_sustanciasquimicasp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaSisConstructivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema', models.CharField(max_length=1500, verbose_name='Sistema constructivo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Lista de sistemas constructivos',
                'verbose_name_plural': 'Lista de sistemas constructivos',
                'ordering': ['sistema'],
            },
        ),
        migrations.CreateModel(
            name='ListaTipoPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=1500, verbose_name='Tipo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Lista de tipos de personal',
                'verbose_name_plural': 'Lista de tipos de personal',
                'ordering': ['tipo'],
            },
        ),
        migrations.RenameModel(
            old_name='EspecieFlores',
            new_name='ListadoFloristico',
        ),
        migrations.AlterModelOptions(
            name='edificacionprovicional',
            options={'ordering': ['title'], 'verbose_name': 'Lista de obras provisionales temporales', 'verbose_name_plural': 'Lista de obras provisionales temporales'},
        ),
        migrations.AlterModelOptions(
            name='listadofloristico',
            options={'ordering': ['nombre'], 'verbose_name': 'Listado florísico', 'verbose_name_plural': 'Listado florísico'},
        ),
        migrations.AlterModelOptions(
            name='maquina',
            options={'ordering': ['title'], 'verbose_name': 'Lista de maquinaría', 'verbose_name_plural': 'Lista de maquinaría'},
        ),
        migrations.AlterModelOptions(
            name='sustanciasquimicasp',
            options={'ordering': ['title'], 'verbose_name': 'Lista de sustancias químicas peligrosas requeridas y almacenadas', 'verbose_name_plural': 'Lista de sustancias químicas peligrosas requeridas y almacenadas'},
        ),
    ]
