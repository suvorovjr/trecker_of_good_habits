from rest_framework.validators import ValidationError


class IsPleasantValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field):
            if value.get('award') or value.get('related_habit'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class RelatedHabit:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)
        if related_habit and not related_habit.is_pleasant:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')
        elif related_habit and value.get('award'):
            raise ValidationError('Не может быть заполнено и поле вознаграждения, и поле связанной привычки.')
