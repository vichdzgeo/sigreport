# Generated by Django 3.0.3 on 2021-09-10 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formulario', '0061_auto_20210910_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='catform',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
