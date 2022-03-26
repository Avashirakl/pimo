from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from pimo.models import User
from pimo.serializers import UserSerializer, UserListSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        serializer = self.serializer_class

        if self.action == 'list':
            serializer = UserListSerializer
        elif self.action == 'update':
            serializer = UserUpdateSerializer

        return serializer
