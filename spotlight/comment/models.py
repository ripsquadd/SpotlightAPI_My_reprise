from django.db import models
import event.models
from user.models import UserModel


class EventCommentModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
    title = models.CharField(max_length=50, unique=True,
                             null=False, blank=False, verbose_name='название')
    descriptions = models.CharField(max_length=255, null=False, blank=False,
                                    verbose_name='описание')

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Автор')
    event = models.ForeignKey("event.EventModel", on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = 'Комментарий к событию'
        verbose_name_plural = 'Комментарии к событиям'

    def __str__(self) -> str:
        return f'{self.title}'
