# Generated by Django 3.0.3 on 2021-04-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0037_obraslinealeslongitudes'),
    ]

    operations = [
        migrations.AddField(
            model_name='catform',
            name='orden',
            field=models.IntegerField(default=0, verbose_name='orden'),
        ),
    ]