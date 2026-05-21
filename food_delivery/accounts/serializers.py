from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'email',
            'password',
            'role',
            'phone_number',
        ]

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [
            'id',
            'username',
            'email',
            'role',
            'phone_number',
            'profile_image',
        ]
