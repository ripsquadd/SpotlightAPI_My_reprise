# Generated by Django 5.0.4 on 2024-05-15 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_alter_eventmodel_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 16, 0, 4, 20, 165108), null=True, verbose_name='Дата'),
        ),
    ]
