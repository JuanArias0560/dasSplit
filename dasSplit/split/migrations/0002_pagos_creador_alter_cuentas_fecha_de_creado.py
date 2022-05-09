# Generated by Django 4.0.4 on 2022-05-09 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('split', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='fecha_de_creado',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
