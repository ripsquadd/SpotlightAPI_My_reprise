# Generated by Django 5.0.4 on 2024-05-15 16:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0008_alter_organizationimages_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='название')),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True, verbose_name='описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('coord_x', models.FloatField(verbose_name='Координаты X')),
                ('coord_y', models.FloatField(verbose_name='Координаты Y')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organizationmodel', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('image', models.ImageField(upload_to='event/cover/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='изображение')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='place.placemodel')),
            ],
        ),
    ]