import requests
from django.conf import settings
from users.services import send_message


def send_telegram_message(telegram_id, message):
    requests.post(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_API}/sendMessage',
        data={
            'chat_id': telegram_id,
            'text': message
        }
    )


def send_notification(habit):
    message = str(habit)
    user = habit.user
    if user.telegram_id:
        send_telegram_message(user.telegram_id, message)
    else:
        subject = f'Уведомление о {habit.action}'
        send_message(recipient_list=user.email, subject=subject, message=message)
