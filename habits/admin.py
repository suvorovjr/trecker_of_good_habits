from django.contrib import admin
from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('habit_place', 'habit_time', 'pk', 'regularity', 'execution_time', 'is_publish', 'is_pleasant')
