import json
import requests
from .models import Habit
from django.conf import settings
from users.services import send_message
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def notification_schedule(habit_id):
    habit = Habit.objects.get(id=habit_id)
    habit_time = habit.habit_time
    regularity = f'1-31/{habit.regularity}'
    schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit_time.minute, hour=habit_time.hour,
                                                        day_of_month=regularity)
    PeriodicTask.objects.create(
        crontab=schedule,
        name=f'Notification of an action № {habit_id}',
        task='habits.tasks.notification_of_action',
        args=json.dumps([habit_id])
    )


def send_telegram_message(telegram_id, message):
    requests.post(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_API}/sendMessage',
        data={
            'chat_id': telegram_id,
            'text': message
        }
    )


def send_notification(message, action, email, telegram_id):
    if not telegram_id:
        send_telegram_message(telegram_id, message)
    else:
        subject = f'Уведомление о {action}'
        send_message(recipient_list=email, subject=subject, message=message)
