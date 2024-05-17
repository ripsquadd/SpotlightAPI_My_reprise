# Generated by Django 5.0.2 on 2024-02-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='login',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Логин'),
        ),
    ]
