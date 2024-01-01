from rest_framework.decorators import api_view, permission_classes , authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST , HTTP_200_OK 
from ..serializers import BlogSerializer
from ..models import Blog
from ..utils.constants import BLOG_POST_SUCCESS_MESSAGE , ALL_BLOGS_FETCHED_MESSAGE , UPDATED_BLOG_SUCCESSFULLY , PERMISSION_DENIED_MESSAGE

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def post_blog(request):
    
    response = None
        
    data = {
        "title": request.data.get("title"),
        "author": request.data.get("author"),
        "content": request.data.get("content"),
        "user": request.user.id
    }
    
    serializer = BlogSerializer(data= data)
    
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


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog(request , pk):

    response = None
    
    blog = Blog.objects.get(id = pk)
    serializer = BlogSerializer(instance=blog , data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        response_data = {
            "message": UPDATED_BLOG_SUCCESSFULLY,
            "data" : serializer.data
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
    
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response
    
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_blogs(request):
    
    response = None
    
    blogs = Blog.objects.filter(user = request.user.id)
    
    serializer = BlogSerializer(instnance = blogs , many= True)   
    
    response_data = {
        "message": ALL_BLOGS_FETCHED_MESSAGE,
        "data": serializer.data
    }
    
    response = Response(response_data , status= HTTP_200_OK)
    
    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_id(request, pk):
    
    response = None
    
    blog = Blog.objects.get(id = pk)
    
    print(blog.user.id)
    
    if blog.user.id != request.user.id:
        response = {
                "message": PERMISSION_DENIED_MESSAGE
            }
    else:
        serializer = BlogSerializer(instance= blog)
        
        data = {
            "message": ALL_BLOGS_FETCHED_MESSAGE,
            "data": serializer.data
        }
        
        response = Response(data , status=HTTP_200_OK)
        
    return response
    