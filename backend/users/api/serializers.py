
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'get_full_name',
            'email',
            'phone'
        ]


class UserSafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id'
            'first_name',
            'last_name',
        ]
