from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.db import models
from organization.models import OrganizationModel
from user.models import UserModel


class EventModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    title = models.CharField(max_length=50, unique=True,
                             null=False, blank=False, verbose_name='название')
    descriptions = models.CharField(max_length=255, null=True, blank=True, verbose_name='описание')
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name='Адрес')
    coord_x = models.FloatField(null=False, blank=False, verbose_name='Координаты X')
    coord_y = models.FloatField(null=False, blank=False, verbose_name='Координаты Y')
    start_time = models.DateTimeField(default=datetime.today(), null=True, verbose_name='Дата')
    member_count = models.IntegerField(default=0, verbose_name='Колличество участников')

    organization = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE, null=False,
                                     blank=False, verbose_name='Организация')
    event_admin = models.ForeignKey(UserModel, null=True, blank=True,
                                    verbose_name='Администратор события', on_delete=models.CASCADE)
    members = models.ManyToManyField(UserModel, blank=True, verbose_name='Участники',
                                     related_name='events')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self) -> str:
        return f'{self.title}'


class EventImages(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    image = models.ImageField(upload_to='event/cover/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                              verbose_name='изображение')
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE,
                              related_name='images')

    def __str__(self) -> str:
        return f'{self.event.title}'
