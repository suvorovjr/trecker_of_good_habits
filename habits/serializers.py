from rest_framework import serializers
from .models import Habit
from .validators import IsPleasantValidator, RelatedHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [IsPleasantValidator(field='is_pleasant'), RelatedHabit(field='related_habit')]



