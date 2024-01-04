from rest_framework import serializers
from ..models import Comment


class Comment_Serializer(serializers.Serializer):
    model = Comment
    fields = '__all__'