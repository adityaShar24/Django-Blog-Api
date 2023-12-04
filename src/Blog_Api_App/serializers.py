from rest_framework import serializers
from django.contrib.auth.models import User
from .models.blog_model import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()