from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import BlogSerializer
from ..models import Blog


@api_view(['POST'])
def post_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)