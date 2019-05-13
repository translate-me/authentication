from user.models import User
from rest_framework import generics
from user.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from datetime import date as dt


class AddNewUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
