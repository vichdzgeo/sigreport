# Generated by Django 3.0.3 on 2021-04-21 22:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0026_auto_20210421_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcConstructivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Proceso constructivo')),
                ('content', ckeditor.fields.RichTextField(default='', verbose_name='Descipción del proceso constructivo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Descripción de procesos constructivos',
                'verbose_name_plural': 'Descripción de procesos constructivos',
                'ordering': ['title'],
            },
        ),
    ]
