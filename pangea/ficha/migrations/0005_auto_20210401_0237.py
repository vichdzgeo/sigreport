# Generated by Django 3.0.3 on 2021-04-01 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0004_auto_20210328_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crearficha',
            old_name='modulo',
            new_name='componente',
        ),
    ]