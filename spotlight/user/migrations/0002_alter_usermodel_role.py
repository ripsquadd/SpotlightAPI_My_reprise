# Generated by Django 5.0.2 on 2024-02-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='role',
            field=models.IntegerField(default=0, verbose_name='Тип профиля'),
        ),
    ]
