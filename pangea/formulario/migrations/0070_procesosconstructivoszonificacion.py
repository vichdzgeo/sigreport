# Generated by Django 3.0.3 on 2022-02-15 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0033_auto_20210824_1221'),
        ('miscelanea', '0048_auto_20211005_1447'),
        ('formulario', '0069_auto_20210921_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcesosConstructivosZonificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_prot', models.IntegerField(default=0, verbose_name='PROT')),
                ('n_rest', models.IntegerField(default=0, verbose_name='REST')),
                ('n_apro', models.IntegerField(default=0, verbose_name='APRO')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('proceso', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.ProcConstructivo')),
            ],
            options={
                'verbose_name': 'Procesos constructivos por tipo de cobertura',
                'verbose_name_plural': 'Procesos constructivos por tipo de cobertura',
                'ordering': ['created'],
            },
        ),
    ]