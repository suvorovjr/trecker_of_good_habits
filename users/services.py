import jwt
import pytz
from datetime import timedelta
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from .models import User


def get_confirmation_token(user):
    print(user.email, user.pk)
    action_time = timezone.now() + timedelta(hours=24)
    token_payload = {
        'id': user.id,
        'exp': int(action_time.timestamp()),
        'email': user.email,
    }

    token = jwt.encode(payload=token_payload, key=settings.SECRET_KEY, algorithm='HS256')
    return token


def send_message(recipient_list, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list.split()
    )


def validate_token(token):
    try:
        decode_token = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms='HS256')
        user_id = decode_token.get('id')
        user = User.objects.get(pk=user_id, is_active=False)
        if user.email_confirmation_token != token:
            return False
        current_time = timezone.now()
        moscow_tz = pytz.timezone('Europe/Moscow')
        expiration_date = timezone.datetime.fromtimestamp(decode_token.get('exp'), tz=moscow_tz)
        if expiration_date < current_time:
            return False
        user.is_active = True
        user.save()
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        return False
    return True
