# Generated by Django 3.0.3 on 2021-04-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0028_auto_20210420_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='title',
            field=models.PositiveIntegerField(default=1, verbose_name='Etapa'),
        ),
    ]
