# Generated by Django 3.0.3 on 2021-04-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0022_auto_20210401_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='abreviatura',
            field=models.CharField(default='', max_length=10, verbose_name='Abreviatura'),
        ),
    ]
