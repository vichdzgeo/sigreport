# Generated by Django 3.0.3 on 2021-02-25 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cap2', '0007_auto_20210225_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperficieObras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edificaciones', models.CharField(max_length=500, verbose_name='Edificaciones en obras provicionales')),
                ('superficie', models.IntegerField(verbose_name='Superficie m²')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Componente')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
            ],
            options={
                'verbose_name': 'Superficie de obras provisionales temporales ',
                'verbose_name_plural': 'Superficie de obras provisionales temporales',
                'ordering': ['-created'],
            },
        ),
    ]
