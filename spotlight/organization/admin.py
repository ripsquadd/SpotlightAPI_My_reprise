from django.contrib import admin
from organization.models import OrganizationModel


@admin.register(OrganizationModel)
class OrganizationAdmin(admin.ModelAdmin):
    pass
