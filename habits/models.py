from django.db import models
from datetime import timedelta
from django.conf import settings
from django.core.validators import MaxValueValidator

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    EXECUTION_CHOICES = (
        (1, 'Ежедневно'),
        (2, 'Каждые 2 дня'),
        (3, 'Каждые 3 дня'),
        (4, 'Каждые 4 дня'),
        (5, 'Каждые 5 дней'),
        (6, 'Каждые 6 дней'),
        (7, 'Еженедельно')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             **NULLABLE)
    habit_place = models.CharField(max_length=100, verbose_name='Место привычки')
    habit_time = models.TimeField(verbose_name='Время привычки')
    action = models.CharField(max_length=255, verbose_name='Действие')
    award = models.CharField(max_length=255, verbose_name='Вознаграждение', **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    execution_time = models.DurationField(default=timedelta(minutes=2), verbose_name='Продолжительность выполнения',
                                          validators=[MaxValueValidator(timedelta(minutes=2))])
    regularity = models.CharField(max_length=1, choices=EXECUTION_CHOICES)
    is_publish = models.BooleanField(default=False, verbose_name='Публичная привычка')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')

    def __str__(self):
        raise f'Я буду {self.action} в {self.habit_time} в {self.habit_place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
