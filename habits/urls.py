from habits.apps import HabitsConfig
from django.urls import path
from .views import HabitCreateAPIView, HabitListAPIView, PublishHabitListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('list/', HabitListAPIView.as_view(), name='list'),
    path('publish/list/', PublishHabitListAPIView.as_view(), name='publish_list'),
    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='destroy')
]
