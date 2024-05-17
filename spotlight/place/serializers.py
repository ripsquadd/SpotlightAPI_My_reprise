from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from place.models import PlaceModel, PlaceImages, OrganizationModel


class PlaceImagesSerializer(ModelSerializer):

    class Meta:
        model = PlaceImages
        fields = ['image']


class CreatePlaceSerializer(ModelSerializer):
    """Сериалайзер Создания места"""

    images = PlaceImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = PlaceModel
        fields = ["title", 'descriptions', 'images', 'uploaded_images', 'address', 'coord_x',
                  'coord_y', 'organization']

    def create(self, validated_data):
        organization = self.validated_data.pop('organization')
        user = self.context['request'].user.id
        organization = OrganizationModel.objects.get(pk=organization.id)
        if organization.status == 1 or organization.organization_admin.id != user:
            raise APIException(detail = 'Организация не одобрена или вы не её владелец',
                                code=status.HTTP_403_FORBIDDEN)

        uploaded_images = validated_data.pop("uploaded_images")
        place = PlaceModel.objects.create(**validated_data)
        for image in uploaded_images:
            PlaceImages.objects.create(place=place, image=image)

        return place


class PlaceSerializer(ModelSerializer):
    """Сериалайзер вывода места"""
    images = PlaceImagesSerializer(many=True, read_only=True)

    class Meta:
        model = PlaceModel
        fields = ['id', 'title', 'descriptions', 'address', 'coord_x', 'images', 'coord_y',
                  'organization', 'place_admin']


class ListPlaceSerializer(ModelSerializer):
    """Сериалайзер вывода мест"""
    images = PlaceImagesSerializer(many=True, read_only=True)

    class Meta:
        model = PlaceModel
        fields = "__all__"


class UpdatePlaceSerializer(ModelSerializer):
    """Сериалайзер обновления места"""

    class Meta:
        model = PlaceModel
        fields = ['title','descriptions', 'address', 'coord_x', 'coord_y', 'images']
