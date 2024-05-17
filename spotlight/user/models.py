from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    username = models.CharField(max_length=50, blank=False, null=False, unique=True,
                                verbose_name='Логин')
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True,
                              verbose_name='Почта')

    role = models.IntegerField(default=0, verbose_name='Тип профиля')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'{self.username}, {self.role}'
