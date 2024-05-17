from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
from user.models import UserModel


class OrganizationModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    title = models.CharField(max_length=50, unique=True,
                             null=False, blank=False, verbose_name='название')
    descriptions = models.CharField(max_length=255, null=True, blank=True, verbose_name='описание')
    address = models.CharField(max_length=255, null=False, blank=False, verbose_name='Адрес')

    status = models.IntegerField(default=1, validators=[MaxValueValidator(2)],
                                 verbose_name="Статус одобрения")

    organization_admin = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True,
                                           blank=False, verbose_name='Администратор организации',
                                           related_name="organizations")

    coord_x = models.FloatField(null=False, blank=False, verbose_name='Координаты X')
    coord_y = models.FloatField(null=False, blank=False, verbose_name='Координаты Y')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self) -> str:
        return f'{self.title}'


class OrganizationImages(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    image = models.ImageField(upload_to='organization/cover/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                              verbose_name='изображение')
    organization = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE,
                                     related_name='images')

    def __str__(self) -> str:
        return f'{self.organization.title}'