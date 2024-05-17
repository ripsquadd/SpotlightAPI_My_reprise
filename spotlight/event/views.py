from django.http import JsonResponse
from rest_framework import generics, permissions, filters
from event.models import EventModel
from event.permissions import IsUserEventOwner, IsUserHavePermissionCreateEvent
from event.serializers import CreateEventSerializer, ListEventSerializer, UpdateEventSerializer, \
    EventSerializer, AddMemberSerializer


class ListEventApiView(generics.ListAPIView):
    """Все события"""
    queryset = EventModel.objects.all()
    serializer_class = ListEventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAuthenticated,)


class EventByIdApiView(generics.RetrieveAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateEventApiView(generics.CreateAPIView):
    """Создание события"""
    serializer_class = CreateEventSerializer
    permission_classes = (IsUserHavePermissionCreateEvent,)

    def perform_create(self, serializer):
        print(self.request.user.organizations)
        serializer.save(event_admin=self.request.user)


class EventUpdate(generics.UpdateAPIView):
    """Обновление события """
    queryset = EventModel.objects.all()
    serializer_class = UpdateEventSerializer
    permission_classes = (IsUserEventOwner,)


class EventDelete(generics.DestroyAPIView):
    """Удаление события"""
    queryset = EventModel.objects.all()
    permission_classes = (IsUserEventOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'detail': 'Удаление успешно'})


class AddMember(generics.UpdateAPIView):
    """Добавление участника"""
    queryset = EventModel.objects.all()
    serializer_class = AddMemberSerializer
    permission_classes = (permissions.IsAuthenticated,)



