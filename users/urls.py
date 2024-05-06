from users.apps import UsersConfig
from django.urls import path
from .views import UserCreateAPIView, ConfirmEmailAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [
    path('auth/', UserCreateAPIView.as_view(), name='auth'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='destroy'),
    path('confirm_email/<str:token>/', ConfirmEmailAPIView.as_view(), name='confirm_email'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
