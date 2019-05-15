from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    username = serializers.CharField(required=True, max_length=50)
    email = serializers.EmailField(required=True, max_length=150)
    password = serializers.CharField(style={'input_type': 'password'})

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
