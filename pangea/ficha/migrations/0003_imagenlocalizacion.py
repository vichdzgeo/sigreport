# Generated by Django 3.0.3 on 2021-03-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0014_auto_20210322_1049'),
        ('ficha', '0002_remove_crearficha_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenLocalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Nombre')),
                ('pie', models.TextField(max_length=5000, verbose_name='Pie de figura')),
                ('image', models.ImageField(default='null', upload_to='figuras', verbose_name='Figura')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('modulo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Componente')),
            ],
            options={
                'verbose_name': 'Figura de localización',
                'verbose_name_plural': 'Figura de localización',
                'ordering': ['-created'],
            },
        ),
    ]
