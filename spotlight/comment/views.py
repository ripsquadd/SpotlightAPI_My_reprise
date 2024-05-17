from django.http import JsonResponse
from rest_framework import generics, permissions, filters
from comment.models import EventCommentModel
from comment.serializers import EventCommentSerializer, CreateEventCommentSerializer, \
    UpdateEventCommentSerializer
from permissions import IsUserEventCommentOwner


class ListEventCommentApiView(generics.ListAPIView):
    """Все комментарии к событиям"""
    queryset = EventCommentModel.objects.all()
    serializer_class = EventCommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (permissions.IsAdminUser,)


class EventCommentByIdApiView(generics.RetrieveAPIView):
    """Комментарий события по ID"""
    queryset = EventCommentModel.objects.all()
    serializer_class = EventCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateEventCommentApiView(generics.CreateAPIView):
    """Создание комментария события"""
    serializer_class = CreateEventCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventCommentUpdate(generics.UpdateAPIView):
    """Обновление комментария события"""
    queryset = EventCommentModel.objects.all()
    serializer_class = UpdateEventCommentSerializer
    permission_classes = (IsUserEventCommentOwner,)


class EventCommentDelete(generics.DestroyAPIView):
    queryset = EventCommentModel.objects.all()
    permission_classes = (IsUserEventCommentOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'detail': 'Удаление успешно'})


