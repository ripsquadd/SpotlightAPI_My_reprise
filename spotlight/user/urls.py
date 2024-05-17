from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from user.views import RegisterApiView, LoginApiView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='profile-create'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-delete/', TokenBlacklistView.as_view(), name='token_blacklist'),
]