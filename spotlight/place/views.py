from rest_framework import generics, filters, permissions
from place.permissions import IsUserPlaceOwner, IsUserHavePermissionCreatePlace
from place.serializers import ListPlaceSerializer, PlaceSerializer, CreatePlaceSerializer, \
    UpdatePlaceSerializer
from place.models import PlaceModel


class ListPlaceApiView(generics.ListAPIView):
    """Все места"""
    queryset = PlaceModel.objects.all()
    serializer_class = ListPlaceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class PlaceByIdApiView(generics.RetrieveAPIView):
    queryset = PlaceModel.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreatePlaceApiView(generics.CreateAPIView):
    """Создание места"""
    serializer_class = CreatePlaceSerializer
    permission_classes = (IsUserHavePermissionCreatePlace,)

    def perform_create(self, serializer):
        serializer.save(place_admin=self.request.user)


class PlaceUpdate(generics.UpdateAPIView):
    """Обновление места """
    queryset = PlaceModel.objects.all()
    serializer_class = UpdatePlaceSerializer
    permission_classes = (IsUserPlaceOwner, IsUserHavePermissionCreatePlace,)
