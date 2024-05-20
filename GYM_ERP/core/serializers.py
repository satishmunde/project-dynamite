from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 
from djoser.serializers import UserSerializer as BaseUserSerializer
# from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import LoginSystem
class LoginSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginSystem
        fields = ['id', 'username','first_name', 'email','user_type', 'phone_number']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        ref_name = "UserCreate"  # Set a distinct ref_name for UserCreateSerializer
        fields = ['username', 'first_name','last_name', 'email', 'user_type', 'phone_number']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = "BaseUser"  # Set a distinct ref_name for UserSerializer
        fields = ['username', 'first_name','last_name', 'email', 'user_type', 'phone_number']
