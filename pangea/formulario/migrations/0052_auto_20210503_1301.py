# Generated by Django 3.0.3 on 2021-05-03 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0030_auto_20210503_0017'),
        ('cap2', '0032_auto_20210422_2055'),
        ('formulario', '0051_auto_20210503_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimientotierrazonificacion',
            old_name='zonificacion',
            new_name='tipo',
        ),
        migrations.AlterField(
            model_name='movimientotierrazonificacion',
            name='n_apro',
            field=models.IntegerField(default=0, verbose_name='APRO'),
        ),
        migrations.AlterField(
            model_name='movimientotierrazonificacion',
            name='n_prot',
            field=models.IntegerField(default=0, verbose_name='PROT'),
        ),
        migrations.AlterField(
            model_name='movimientotierrazonificacion',
            name='n_rest',
            field=models.IntegerField(default=0, verbose_name='REST'),
        ),
        migrations.CreateModel(
            name='ResiduosSolidosZonificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_prot', models.IntegerField(default=0, verbose_name='PROT')),
                ('n_rest', models.IntegerField(default=0, verbose_name='REST')),
                ('n_apro', models.IntegerField(default=0, verbose_name='APRO')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('componente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Modulo')),
                ('etapa', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Etapa')),
                ('fase', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cap2.Fase')),
                ('residuo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='miscelanea.ListaTipoResiduosSolidos')),
            ],
            options={
                'verbose_name': 'Generación de residuos sólidos por zonificación',
                'verbose_name_plural': 'Generación de residuos sólidos por zonificación',
                'ordering': ['created'],
            },
        ),
    ]
