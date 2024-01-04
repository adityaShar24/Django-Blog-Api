from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from rest_framework.response import Response 
from ..serializers.comment_serializer import Comment_Serializer 
from ..utils.constants import COMMENT_SUCCESS_MESSAGE , COMMENT_UPDATED_MESSAGE
from ..models.comment_model import Comment

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_comment(request):
    
    response = None
    
    data = {
        'comment': request.data.get('comment'),
        'parent_comment' : request.data.get('parent_comment'),
        'blog': request.data.get('blog'),
        'user': request.user.id
    }
    
    serializer = Comment_Serializer(data = data)
    
    if serializer.is_valid():
        serializer.save()
        
        response_data = {
            "message": COMMENT_SUCCESS_MESSAGE,
            "data": serializer.data
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
    
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response



@api_view(["PUT"])
@permission_classes([JWTAuthentication])
def update_comment(request, pk):
    
    response = None
    
    comment = Comment.objects.get(id, pk)
    serializer = Comment_Serializer(instance= comment , data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        
        response_data = {
            "message": COMMENT_UPDATED_MESSAGE,
            "data": serializer.data 
        }
        
        response = Response(response_data , status= HTTP_201_CREATED)
        
    else:
        response = Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
        
    return response
    
    