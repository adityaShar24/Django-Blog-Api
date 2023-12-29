from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , HTTP_200_OK 
from ..serializers import BlogSerializer
from ..models import Blog
from ..utils.constants import BLOG_POST_SUCCESS_MESSAGE , ALL_BLOGS_FETCHED_MESSAGE

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_blog(request):
    
    response = None
    
    serializer = BlogSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        
        response_data = {
            "message": BLOG_POST_SUCCESS_MESSAGE,
            "data": serializer.data
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
    
    else:
        response = Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
        
    return response
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_blogs(request):
    
    blogs = Blog.objects.all()
    
    serializer = BlogSerializer(blogs, many=True)
    
    
    response_data = {
        "message": ALL_BLOGS_FETCHED_MESSAGE,
        "data": serializer.data
    }
    
    return Response(response_data , status= HTTP_200_OK)