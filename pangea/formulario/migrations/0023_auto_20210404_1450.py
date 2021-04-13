# Generated by Django 3.0.3 on 2021-04-04 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0022_auto_20210401_0237'),
        ('formulario', '0022_auto_20210401_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catform',
            name='tipo',
            field=models.CharField(choices=[('1', 'PNG'), ('2', 'Catálogo'), ('3', 'Catálogo de abreviaturas'), ('4', 'Catálogo por fase'), ('5', 'Formulario de datos'), ('6', 'Formulario de datos y abreviaturas'), ('7', 'Formulario de texto y figuras')], default='', max_length=100, verbose_name='tipo de formulario'),
        ),
        migrations.CreateModel(
            name='ImagenLocalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Nombre')),
                ('image', models.ImageField(default='null', upload_to='figuras', verbose_name='Figura')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('modulo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
            ],
            options={
                'verbose_name': 'Imagen de localización y tipos de aprovechamiento',
                'verbose_name_plural': 'Imagen de localización y tipos de aprovechamiento',
                'ordering': ['-created'],
            },
        ),
    ]