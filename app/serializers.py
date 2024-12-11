from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny] 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password','email','phone']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone=validated_data['phone'],

        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)