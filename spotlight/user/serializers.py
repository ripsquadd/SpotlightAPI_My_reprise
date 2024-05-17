from django.contrib.auth.models import update_last_login
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from rest_framework.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import UserModel


class UserAdminEventSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id']


class RegisterSerializer(ModelSerializer):
    """ Сериалайзер для регистрации"""
    password = CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'role', 'password']


class LoginSerializer(TokenObtainSerializer):
    """Сериалайзер авторизации"""
    token_class = RefreshToken

    def validate(self, attrs: dict[str, any]) -> dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        user_id = self.user.id
        user_role = self.user.is_superuser

        data["user_id"] = str(user_id)
        data["user_role"] = str(user_role)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
