# Generated by Django 3.0.3 on 2021-03-28 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0015_auto_20210328_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superficieobrasc',
            name='modulo',
        ),
    ]