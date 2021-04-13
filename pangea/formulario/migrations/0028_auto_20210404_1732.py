# Generated by Django 3.0.3 on 2021-04-04 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0022_auto_20210401_0237'),
        ('miscelanea', '0008_auto_20210330_1202'),
        ('formulario', '0027_superficieobrasc_etapa'),
    ]

    operations = [
        migrations.CreateModel(
            name='AguasResidualesC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad en m³')),
                ('unidad', models.CharField(default='m³', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('tipo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.TipoAgua')),
            ],
            options={
                'verbose_name': 'Generación de aguas residuales - Construcción',
                'verbose_name_plural': 'Generación de aguas residuales - Construcción',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ConsumoAguaC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad en m³')),
                ('unidad', models.CharField(default='m³', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('tipo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.TipoAgua')),
            ],
            options={
                'verbose_name': 'Consumo de agua - Construcción',
                'verbose_name_plural': 'Consumo de agua - Construcción',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='FrecuenciaActividadesC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas', models.IntegerField(verbose_name='Jornadas/fase')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('actividades', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.ActividadProvicional')),
                ('componente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
            ],
            options={
                'verbose_name': 'Frecuencia de actividades de obras provisionales - Construcción',
                'verbose_name_plural': 'Frecuencia de actividades de obras provisionales  - Construcción',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImagenLocalizacionC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Nombre')),
                ('image', models.ImageField(default='null', upload_to='figuras', verbose_name='Figura')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
            ],
            options={
                'verbose_name': 'Imagen de localización y tipos de aprovechamiento',
                'verbose_name_plural': 'Imagen de localización y tipos de aprovechamiento',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='ImagenLocalizacion',
        ),
    ]