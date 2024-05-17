from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenViewBase

from user.serializers import RegisterSerializer, LoginSerializer


class RegisterApiView(generics.CreateAPIView):
    """ Регистрация"""
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class LoginApiView(TokenViewBase):
    """Авторизация"""

    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
