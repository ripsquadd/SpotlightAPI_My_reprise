from rest_framework.serializers import ModelSerializer
from comment.models import EventCommentModel


class CreateEventCommentSerializer(ModelSerializer):
    """Сериалайзер Создания комментария к событию"""

    class Meta:
        model = EventCommentModel
        fields = ['title', 'descriptions', 'event']


class EventCommentSerializer(ModelSerializer):

    class Meta:
        model = EventCommentModel
        fields = "__all__"


class UpdateEventCommentSerializer(ModelSerializer):

    class Meta:
        model = EventCommentModel
        exclude = ['id', 'user', 'event']
