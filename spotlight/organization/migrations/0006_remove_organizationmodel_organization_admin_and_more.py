# Generated by Django 5.0.3 on 2024-03-25 16:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_alter_organizationmodel_organization_admin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationmodel',
            name='organization_admin',
        ),
        migrations.AddField(
            model_name='organizationmodel',
            name='organization_admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Администратор организации'),
        ),
    ]
