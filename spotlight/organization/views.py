from django.http import JsonResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import generics, permissions, filters
from organization.models import OrganizationModel
from organization.permissions import OrganizationUserOwner
from organization.serializers import CreateOrganizationSerializer, ListOrganizationSerializer, \
    UpdateOrganizationSerializer, UpdateOrganizationStatusSerializer
from event.serializers import ListEventSerializer
from event.models import EventModel
from place.models import PlaceModel
from place.serializers import ListPlaceSerializer


class ListOrganizationApiView(generics.ListAPIView):
    """Все организации"""
    queryset = OrganizationModel.objects.all()
    serializer_class = ListOrganizationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class CreateOrganizationApiView(generics.CreateAPIView):
    """Создание организации"""
    serializer_class = CreateOrganizationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(organization_admin=self.request.user)


class OrganizationUpdate(generics.UpdateAPIView):
    """Обновление организации """
    queryset = OrganizationModel.objects.all()
    serializer_class = UpdateOrganizationSerializer
    permission_classes = (OrganizationUserOwner,)


class OrganizationUpdateStatus(generics.UpdateAPIView):
    """Обновление статуса организации """
    queryset = OrganizationModel.objects.all()
    serializer_class = UpdateOrganizationStatusSerializer
    permission_classes = (permissions.IsAdminUser,)


class OrganizationDelete(generics.DestroyAPIView):
    queryset = OrganizationModel.objects.all()
    permission_classes = (OrganizationUserOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'detail': 'Удаление успешно'})


class MultipleOrganizationAndEvents(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': OrganizationModel.objects.all(), 'serializer_class':
            ListOrganizationSerializer, 'label': "organization"},
        {'queryset': EventModel.objects.all(), 'serializer_class': ListEventSerializer, 'label':
            "events"},
        {'queryset': PlaceModel.objects.all(), 'serializer_class': ListPlaceSerializer, 'label':
            "places"},
    ]
