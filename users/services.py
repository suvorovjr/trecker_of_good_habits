import jwt
from datetime import timedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings


def get_confirmation_token(user):
    print(user.email, user.pk)
    action_time = timezone.now() + timedelta(hours=24)
    token_payload = {
        'id': user.id,
        'exp': int(action_time.timestamp()),
        'email': user.email,
    }

    token = jwt.encode(payload=token_payload, key=settings.SECRET_KEY, algorithm='HS256')
    # decode_token = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
    return token


def send_confirm_link(recipient_list, confirm_link):
    send_mail(
        subject='Подтвердите аккаунт',
        message=f'Для подтверждения аккаунта перейдите по ссылке {confirm_link}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list
    )
