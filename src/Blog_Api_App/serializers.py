from rest_framework import serializers
from django.contrib.auth.models import User
from .models.blog_model import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'date']

    def create(self, validated_data):
        user = self.context['request'].user if 'request' in self.context else None
        validated_data['author'] = user
        return super().create(validated_data)    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()