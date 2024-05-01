from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')
    avatar = models.ImageField(upload_to='/avatars', verbose_name='Аватар', **NULLABLE)
    telegram_id = models.CharField(max_length=35, unique=True, verbose_name='ID Телеграм')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
