# Generated by Django 3.0.3 on 2021-04-21 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0025_auto_20210417_1434'),
        ('formulario', '0044_auto_20210420_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumoaguac',
            name='fase',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase'),
        ),
    ]
