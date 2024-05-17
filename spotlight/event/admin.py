from django.contrib import admin
from event.models import EventModel


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    pass
