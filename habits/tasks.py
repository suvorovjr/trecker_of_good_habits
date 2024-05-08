from .models import Habit
from .services import send_notification


def notification_of_action(habit_id):
    habit = Habit.objects.get(id=habit_id)
    message = str(habit)
    action = habit.action
    email = habit.user.email
    telegram_id = habit.user.telegram_id
    send_notification(message=message, action=action, email=email, telegram_id=telegram_id)
