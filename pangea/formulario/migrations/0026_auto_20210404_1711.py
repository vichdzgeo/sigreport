# Generated by Django 3.0.3 on 2021-04-04 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0022_auto_20210401_0237'),
        ('formulario', '0025_auto_20210404_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catform',
            name='fase',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase'),
        ),
        migrations.AlterField(
            model_name='superficieobrasc',
            name='fase',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase'),
        ),
    ]
