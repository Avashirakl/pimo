from rest_framework import serializers
from .models import Post
from pimo.models import User


class PostSerializer(serializers.Serializer):
    title = serializers.CharField('Title', max_length=50)
    author = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    details = serializers.TextField('Details')
    likes = serializers.BooleanField('Likes')

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['username']
