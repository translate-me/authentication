from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class ValidateToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        token = data['token']
        obj = get_object_or_404(Token, key=token)
        if obj is not None:
            return JsonResponse({'status': True})

        message = "Token not found !"
        return JsonResponse({'status': False, 'message': message})
