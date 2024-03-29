# Generated by Django 3.0.3 on 2021-08-23 08:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0032_auto_20210422_2055'),
        ('miscelanea', '0040_auto_20210823_0036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListaFrecAct_scrc',
            new_name='ListActVisitantes',
        ),
        migrations.AddField(
            model_name='listaactividades',
            name='fase',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='cap2.Fase'),
        ),
        migrations.AddField(
            model_name='listatiporesiduossolidos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listatiporesiduossolidos',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='listatiporesiduos',
            name='tipo',
            field=models.CharField(max_length=300, verbose_name='Tipo'),
        ),
        migrations.CreateModel(
            name='ResiduosPeligrosos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residuo', models.CharField(max_length=1500, verbose_name='Residuo peligroso')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('ins_especial', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='miscelanea.ListInsEsp', verbose_name='Instalación especial')),
                ('unidad', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.Unidad')),
            ],
            options={
                'verbose_name': 'Lista de residuos peligrosos por instalación especial',
                'verbose_name_plural': 'Lista de residuos peligrosos por instalación especial',
                'ordering': ['residuo'],
            },
        ),
        migrations.CreateModel(
            name='ListaAreasManejo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=1500, verbose_name='Área de manejo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('ins_especial', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='miscelanea.ListInsEsp', verbose_name='Instalación especial')),
            ],
            options={
                'verbose_name': 'Lista de áreas de manejo de sustancias peligrosas',
                'verbose_name_plural': 'Lista de áreas de manejo de sustancias peligrosas',
            },
        ),
        migrations.CreateModel(
            name='ListaActInsEsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=1500, verbose_name='Actividad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('ins_especial', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='miscelanea.ListInsEsp', verbose_name='Instalación especial')),
            ],
            options={
                'verbose_name': 'Lista de actividades en instalaciones especiales',
                'verbose_name_plural': 'Lista de actividades en instalaciones especiales',
            },
        ),
    ]
