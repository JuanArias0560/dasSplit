# Generated by Django 4.0.4 on 2022-05-12 21:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('split', '0004_porfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Porfile',
            new_name='Profile',
        ),
    ]
