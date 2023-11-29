from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer


@api_view(['POST'])
def post_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
