from django.urls import path
from organization.views import ListOrganizationApiView, CreateOrganizationApiView, \
    OrganizationUpdate, OrganizationDelete, MultipleOrganizationAndEvents, OrganizationUpdateStatus

app_name = 'organization'

urlpatterns = [
    path('all-organizations/', ListOrganizationApiView.as_view()),
    path('create-organization/', CreateOrganizationApiView.as_view()),
    path('update-organization/<int:pk>/', OrganizationUpdate.as_view()),
    path('delete-organization/<int:pk>/', OrganizationDelete.as_view()),
    path('all/', MultipleOrganizationAndEvents.as_view()),
    path('update-status/<int:pk>/', OrganizationUpdateStatus.as_view())

]