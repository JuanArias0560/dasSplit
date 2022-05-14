# Generated by Django 4.0.4 on 2022-05-12 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('split', '0007_alter_pagos_cuentas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ManyToManyField(related_name='pocket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='creador',
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='cuentas',
        ),
        migrations.DeleteModel(
            name='Cuentas',
        ),
        migrations.DeleteModel(
            name='Pagos',
        ),
        migrations.AddField(
            model_name='payment',
            name='pockets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='split.pocket'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL),
        ),
    ]