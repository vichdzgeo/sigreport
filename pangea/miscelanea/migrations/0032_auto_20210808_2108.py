# Generated by Django 3.0.3 on 2021-08-09 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0032_auto_20210422_2055'),
        ('miscelanea', '0031_auto_20210808_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaActividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=1500, verbose_name='Actividad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Lista de actividades en instalaciones especiales',
                'verbose_name_plural': 'Lista de actividades en instalaciones especiales',
                'ordering': ['actividad'],
            },
        ),
        migrations.CreateModel(
            name='ListaAreasManejoPeligrosas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_area', models.CharField(max_length=1500, verbose_name='Área de manejo de sustancias peligrosas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Lista de áreas de manejo de sustancias peligrosas',
                'verbose_name_plural': 'Lista de áreas de manejo de sustancias peligrosas',
                'ordering': ['n_area'],
            },
        ),
        migrations.CreateModel(
            name='ListaPTAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planta', models.CharField(max_length=1500, verbose_name='Planta de tratamiento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Lista de plantas de tratamiento',
                'verbose_name_plural': 'Lista de plantas de tratamiento',
                'ordering': ['planta'],
            },
        ),
        migrations.AddField(
            model_name='listafrecact_scrc',
            name='fase',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.PROTECT, to='cap2.Fase'),
        ),
        migrations.AddField(
            model_name='maquina',
            name='fase',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='cap2.Fase'),
        ),
    ]
