from rest_framework import serializers
from ..models.blog_model import Blogs

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'
        