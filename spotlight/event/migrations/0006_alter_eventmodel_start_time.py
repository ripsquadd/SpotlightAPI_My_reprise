# Generated by Django 5.0.3 on 2024-05-01 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_eventmodel_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 22, 16, 5, 823337), null=True, verbose_name='Дата'),
        ),
    ]
