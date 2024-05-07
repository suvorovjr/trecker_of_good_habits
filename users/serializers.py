from django.urls import reverse
from rest_framework import serializers
from .services import get_confirmation_token, send_message
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(email=validated_data['email'], telegram_id=validated_data.get('telegram_id'))
        user.set_password(validated_data['password'])
        user.save()
        confirmation_token = get_confirmation_token(user)
        user.email_confirmation_token = confirmation_token
        user.save()
        confirmation_url = reverse('users:confirm_email', kwargs={'token': confirmation_token})
        request = self.context.get('request')
        full_confirmation_url = request.build_absolute_uri(confirmation_url)
        subject = 'Подтверждение почты'
        message = f'Для подтверждения аккаунта перейдите по ссылке {full_confirmation_url}'
        send_message(user.email, subject, message)
        return user

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
