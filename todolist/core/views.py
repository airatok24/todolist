from django.contrib.auth import login, logout
from rest_framework import generics, status, permissions

from core.models import User
from core.serializers import CreateUserSerializer, ProfileSerializer, \
    UpdatePasswordSerializer  # зачем тудулист

from core.serializers import LoginSerializer  # и тут
from rest_framework.response import Response


class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         login(request=request, user=serializer.save())
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdatePasswords(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def ger_object(self):
        return self.request.user