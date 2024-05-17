from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from organization.models import OrganizationModel, OrganizationImages
from user.models import UserModel


class OrganizationImagesSerializer(ModelSerializer):

    class Meta:
        model = OrganizationImages
        fields = ['image']


class CreateOrganizationSerializer(ModelSerializer):
    """Сериалайзер Создания организации"""
    images = OrganizationImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = OrganizationModel
        fields = ['title', 'descriptions', 'address', 'images', 'uploaded_images', 'coord_x',
                  'coord_y']

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        organization = OrganizationModel.objects.create(**validated_data)
        for image in uploaded_images:
            OrganizationImages.objects.create(organization=organization, image=image)

        return organization


class UserAdminOrganization(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','username', 'email']


class ListOrganizationSerializer(ModelSerializer):
    """Сериалайзер вывода организаций"""
    organization_admin = UserAdminOrganization(read_only=True)
    images = OrganizationImagesSerializer(many=True)

    class Meta:
        model = OrganizationModel
        fields = ['id', 'title', 'status', 'descriptions', 'organization_admin', 'images', 'address', 'coord_x',
                  'coord_y']


class UpdateOrganizationSerializer(ModelSerializer):
    """Сериалайзер обновления организаций"""

    class Meta:
        model = OrganizationModel
        exclude = ['id']


class UpdateOrganizationStatusSerializer(ModelSerializer):
    """Сериалайзер обновления статуса организаций"""

    class Meta:
        model = OrganizationModel
        fields = ['status']