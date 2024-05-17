# Generated by Django 5.0.3 on 2024-03-21 07:54

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('organization', '0004_organizationmodel_organization_admin_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='event_admin',
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organizationmodel', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 21, 14, 54, 13, 949043), null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='event_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Администратор события'),
        ),
    ]