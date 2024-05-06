from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import User
from .services import validate_token
from .permissions import IsAccountOwner


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ConfirmEmailAPIView(APIView):
    def get(self, request, token, *args, **kwargs):
        if validate_token(token):
            return Response({'message': 'Email успешно подтвержден.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Ссылка для активации недействительна или устарела.'},
                            status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAccountOwner]

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        new_password = request.data.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.save()
        return Response({'message': 'Учетная запись цспешно изменена'}, status=status.HTTP_200_OK)


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAccountOwner]
