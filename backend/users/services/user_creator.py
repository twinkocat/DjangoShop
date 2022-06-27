from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
        ]

    def validate_username(self, value):
        """Check in db username"""
        try:
            User.objects.get(username=value.lower())
        except ObjectDoesNotExist:
            pass
        else:
            raise serializers.ValidationError('User with that username exists in the database')

        return value

    def validate_email(self, value):
        """Check in db email"""
        try:
            User.objects.get(email=value.lower())
        except ObjectDoesNotExist:
            pass
        else:
            raise serializers.ValidationError('User with that email exists in the database')

        return value


class UserCreator:
    """Service object for creating a user"""

    def __init__(self, email: str, name: Optional[str] = None):
        email = email.lower()
        print(email)
        self.data = {
            'email': email,
            'username': email,
            **User.parse_name(name or ''),
        }

    def __call__(self) -> User:
        self.resulting_user = self.get() or self.create()
        return self.resulting_user

    def get(self) -> Optional[User]:
        return User.objects.filter(is_active=True).filter(email=self.data['email']).first()

    def create(self) -> User:
        serializer = UserCreateSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return serializer.instance

