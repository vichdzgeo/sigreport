# Generated by Django 3.0.3 on 2021-02-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap2', '0003_auto_20210224_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='componente',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]