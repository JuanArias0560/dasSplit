# Generated by Django 4.0.4 on 2022-05-10 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('split', '0002_remove_cuentas_pagos_cuentas_pagos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentas',
            name='pagos',
        ),
        migrations.AddField(
            model_name='pagos',
            name='cuentas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='split.cuentas'),
        ),
    ]