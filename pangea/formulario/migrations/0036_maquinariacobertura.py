# Generated by Django 3.0.3 on 2021-04-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0018_listatiposaprovechamiento_listatiposcobertura_listatiposconsedif_listazonificacion_movimientotierra'),
        ('cap2', '0025_auto_20210417_1434'),
        ('formulario', '0035_auto_20210417_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaquinariaCobertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas', models.IntegerField(default=0, verbose_name='Número de horas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('cobertura', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.ListaTiposCobertura')),
                ('componente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('maquinaria', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.Maquina')),
            ],
            options={
                'verbose_name': 'Maquinaria por cobertura y zonificación',
                'verbose_name_plural': 'Maquinarias por cobertura y zonificación',
                'ordering': ['created'],
            },
        ),
    ]
