# Generated by Django 3.0.3 on 2021-09-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0059_auto_20210908_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aforoalmacenamientovehicular',
            name='porcion_almacenada',
            field=models.CharField(choices=[('n/a', 'n/a'), ('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], default='0%', max_length=10, verbose_name='Porción almacenada'),
        ),
    ]
