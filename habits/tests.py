from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from .models import Habit


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user@test.ru')
        self.user.set_password('testpassword')
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            habit_place='Дома',
            habit_time='08:00:00',
            action='Выпить стакан воды',
            regularity=1,
            award='Сьесть десерт'
        )

    def test_create_habit(self):
        """Тест создания привычки"""

        data = {
            'habit_place': 'Дома',
            'habit_time': '08:00:00',
            'action': 'Почитать книгу',
            'regularity': 1,
            'award': 'Сьесть десерт',
            "is_pleasant": True
        }

        response = self.client.post(
            '/habit/create/',
            data=data
        )

        body = {
            "non_field_errors": [
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            ]
        }

        self.assertEquals(
            response.json(),
            body
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_list_habit(self):
        """Тест вывода списка привычек"""

        response = self.client.get(
            '/habit/list/',
        )

        body = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.id,
                    'habit_place': 'Дома',
                    'habit_time': '08:00:00',
                    'action': 'Выпить стакан воды',
                    'award': 'Сьесть десерт',
                    "execution_time": "00:02:00",
                    "regularity": 1,
                    "is_publish": False,
                    "is_pleasant": False,
                    "user": self.user.id,
                    "related_habit": None
                }
            ]
        }

        self.assertEquals(
            response.json(),
            body
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_publish_list_habit(self):
        """Тест вывода списка публичных привычке"""

        response = self.client.get(
            '/habit/publish/list/',
        )

        body = {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        }

        self.assertEquals(
            response.json(),
            body
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_habit(self):
        """Тест вывода одной привычки"""

        response = self.client.get(
            reverse('habit:retrieve', args=[str(self.habit.id)])
        )

        body = {
            "id": self.habit.id,
            'habit_place': 'Дома',
            'habit_time': '08:00:00',
            'action': 'Выпить стакан воды',
            'award': 'Сьесть десерт',
            "execution_time": "00:02:00",
            "regularity": 1,
            "is_publish": False,
            "is_pleasant": False,
            "user": self.user.id,
            "related_habit": None
        }

        self.assertEquals(
            response.json(),
            body
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """Тест редактирования привычки"""

        data = {
            'habit_place': 'Не дома',
            'habit_time': '10:00:00',
        }

        response = self.client.patch(
            reverse('habit:update', args=[str(self.habit.id)]),
            data=data
        )

        body = {
            "id": self.habit.id,
            'habit_place': 'Не дома',
            'habit_time': '10:00:00',
            'action': 'Выпить стакан воды',
            'award': 'Сьесть десерт',
            "execution_time": "00:02:00",
            "regularity": 1,
            "is_publish": False,
            "is_pleasant": False,
            "user": self.user.id,
            "related_habit": None
        }

        self.assertEquals(
            response.json(),
            body
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_destroy_habit(self):
        """Тест удаления привычки"""

        response = self.client.delete(reverse('habit:destroy', args=[str(self.habit.id)]))

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
