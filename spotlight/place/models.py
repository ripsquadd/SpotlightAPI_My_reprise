from django.core.validators import FileExtensionValidator
from django.db import models
from organization.models import OrganizationModel
from user.models import UserModel


class PlaceModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    title = models.CharField(max_length=50, unique=True,
                             null=False, blank=False, verbose_name='название')
    descriptions = models.CharField(max_length=255, null=True, blank=True, verbose_name='описание')
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name='Адрес')
    coord_x = models.FloatField(null=False, blank=False, verbose_name='Координаты X')
    coord_y = models.FloatField(null=False, blank=False, verbose_name='Координаты Y')

    place_admin = models.ForeignKey(UserModel, null=True, blank=True,
                                    verbose_name='Администратор места', on_delete=models.CASCADE)
    organization = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE, null=False,
                                     blank=False, verbose_name='Организация')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self) -> str:
        return f'{self.title}'


class PlaceImages(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    image = models.ImageField(upload_to='event/cover/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                              verbose_name='изображение')
    place = models.ForeignKey(PlaceModel, on_delete=models.CASCADE,
                              related_name='images')

    def __str__(self) -> str:
        return f'{self.place.title}'
