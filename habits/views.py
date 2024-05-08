from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import HabitSerializer
from .models import Habit
from .paginator import HabitPaginator
from .services import notification_schedule
from .permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()
        notification_schedule(habit.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().order_by('id')
    pagination_class = HabitPaginator
    permission_classes = [permissions.IsAuthenticated & IsOwner]


class PublishHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_publish=True).order_by('id')
    pagination_class = HabitPaginator
    permission_classes = [permissions.IsAuthenticated]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [permissions.IsAuthenticated & IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [permissions.IsAuthenticated & IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [permissions.IsAuthenticated & IsOwner]
