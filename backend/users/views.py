from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.services.user_creator import UserCreateSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


