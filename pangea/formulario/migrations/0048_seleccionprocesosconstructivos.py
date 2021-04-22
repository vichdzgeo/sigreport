# Generated by Django 3.0.3 on 2021-04-21 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0030_auto_20210421_0227'),
        ('miscelanea', '0027_procconstructivo'),
        ('formulario', '0047_auto_20210421_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeleccionProcesosConstructivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('procesos', models.ManyToManyField(to='miscelanea.ProcConstructivo', verbose_name='Procesos construcitivos')),
            ],
            options={
                'verbose_name': 'Selección de sistemas constructivos',
                'verbose_name_plural': 'Selección de sistemas constructivos',
                'ordering': ['-created'],
            },
        ),
    ]