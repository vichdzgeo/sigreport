# Generated by Django 3.0.3 on 2021-04-01 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0022_auto_20210401_0237'),
        ('formulario', '0020_auto_20210401_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='catform',
            name='etapa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa'),
        ),
    ]
