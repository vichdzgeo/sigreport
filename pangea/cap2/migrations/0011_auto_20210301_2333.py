# Generated by Django 3.0.3 on 2021-03-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0010_imagen_referencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='referencia',
            field=models.TextField(default='Figura<built-in function id>', verbose_name='ID para referenciar en el texto'),
        ),
    ]