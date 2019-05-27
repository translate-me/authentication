from user.models import User
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from user.serializers import UserSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated)


class AddNewUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUser(generics.DestroyAPIView):
    authenticantion_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = "username"

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        queryset = User.objects.filter(username=username)
        return queryset

    def perform_destroy(self, instance):
        serializer = UserSerializer(data=self.get_queryset())
        serializer.is_valid()
        return instance.delete()
