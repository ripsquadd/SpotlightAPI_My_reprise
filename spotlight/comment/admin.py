from django.contrib import admin
from comment.models import EventCommentModel


@admin.register(EventCommentModel)
class EventCommentAdmin(admin.ModelAdmin):
    pass
