from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField('Title', max_length=50)
    author = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    details = serializers.TextField('Details')
    likes = serializers.BooleanField('Likes')
