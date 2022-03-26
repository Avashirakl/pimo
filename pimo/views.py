from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostAPIView(APIView):
    def get(self, request):
        p = Post.object.all()
        return Response({'posts': PostSerializer(p, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Post.objects.create(
            title=request.data['title'],
            author=request.data['author'],
            details=request.data['details'],

        )
        return Response({'post': PostSerializer(post_new).data})


def orders_home(request):
    return render(request, 'Orders/orders_home.html')


def posts_home(request):
    return render(request, 'Posts/posts_home.html')


def offers_home(request):
    return render(request, 'Offers/offers_home.html')


def offers_home(request):
    return render(request, 'Offers/offers_home.html')


def users_home(request):
    return render(request, 'Users/users_home.html')


def grades_home(request):
    return render(request, 'Grades/grades_home.html')
=======
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
