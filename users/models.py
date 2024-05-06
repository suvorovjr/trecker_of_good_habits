from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватар', **NULLABLE)
    telegram_id = models.CharField(max_length=35, verbose_name='ID Телеграм', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активация')
    email_confirmation_token = models.CharField(max_length=255, verbose_name='Токен', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
