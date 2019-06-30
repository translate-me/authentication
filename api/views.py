from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from user.models import User
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from user.serializers import UserSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated)


class ValidateToken(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return JsonResponse({'status': False,
                             'message': "Método get não permitido"})

    def post(self, request):
        data = request.data
        token = data['token']
        obj = get_object_or_404(Token, key=token)
        if obj is not None:
            return JsonResponse({'status': True})

        message = "Token not found !"
        return JsonResponse({'status': False, 'message': message})


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
