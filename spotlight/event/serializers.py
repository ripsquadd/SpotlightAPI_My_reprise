from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from comment.serializers import EventCommentSerializer
from event.models import EventModel, EventImages, OrganizationModel


class EventImagesSerializer(ModelSerializer):

    class Meta:
        model = EventImages
        fields = ['image']


class CreateEventSerializer(ModelSerializer):
    """Сериалайзер Создания события"""

    images = EventImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = EventModel
        fields = ["title", 'descriptions', 'images', 'uploaded_images', 'address', 'coord_x',
                  'coord_y', 'start_time', 'organization']

    def create(self, validated_data):
        organization = self.validated_data.pop('organization')
        user = self.context['request'].user.id
        organization = OrganizationModel.objects.get(pk=organization.id)
        if organization.status == 1 or organization.organization_admin.id != user:
            raise APIException(detail = 'Организация не одобрена или вы не её владелец',
                              code=status.HTTP_403_FORBIDDEN)

        uploaded_images = validated_data.pop("uploaded_images")
        event = EventModel.objects.create(**validated_data)
        for image in uploaded_images:
            EventImages.objects.create(event=event, image=image)

        return event


class EventSerializer(ModelSerializer):
    """Сериалайзер вывода события"""
    images = EventImagesSerializer(many=True, read_only=True)
    comments = EventCommentSerializer(many=True, read_only=True)

    class Meta:
        model = EventModel
        fields = ['id', 'title', 'descriptions', 'address', 'coord_x', 'images', 'coord_y',
                  'start_time', 'organization', 'event_admin', 'comments']


class ListEventSerializer(ModelSerializer):
    """Сериалайзер вывода событий"""
    member_count = serializers.SerializerMethodField()
    images = EventImagesSerializer(many=True, read_only=True)
    comments = EventCommentSerializer(many=True, read_only=True)

    class Meta:
        model = EventModel
        fields = "__all__"

    @staticmethod
    def get_member_count(obj):
        return obj.members.count()


class UpdateEventSerializer(ModelSerializer):
    """Сериалайзер обновления события"""

    class Meta:
        model = EventModel
        fields = ['title', 'descriptions', 'address', 'start_time', 'members']


class AddMemberSerializer(ModelSerializer):
    """Добавление участника"""

    class Meta:
        model = EventModel
        fields = ['members']
