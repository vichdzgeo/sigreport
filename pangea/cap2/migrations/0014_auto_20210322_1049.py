# Generated by Django 3.0.3 on 2021-03-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0013_auto_20210308_2331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componente',
            options={'ordering': ['-created'], 'verbose_name': 'Modulo', 'verbose_name_plural': 'Modulos'},
        ),
        migrations.AddField(
            model_name='fase',
            name='descripcion',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='fase',
            name='fin',
            field=models.PositiveIntegerField(default=99, verbose_name='fin'),
        ),
        migrations.AddField(
            model_name='fase',
            name='inicio',
            field=models.PositiveIntegerField(default=1, verbose_name='Inicio'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
    ]