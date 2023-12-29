from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import UserSerializer , LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken
from ..utils.constants import USER_REGISTERED_MESSAGE , USER_LOGGEDIN_MESSAGE , INVAID_CREDENTIALS_MESSAGE
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST



@api_view(['POST'])
def register_user(request):
    response = None
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        
        respone_data = {
            "message": USER_REGISTERED_MESSAGE,
            "data": serializer.data
        }
        
        
        response = Response( respone_data , status= HTTP_201_CREATED)
    else:
        response = Response(serializer.errors , status= HTTP_400_BAD_REQUEST) 
    
    return response

    
@api_view(['POST'])
def login_user(request):
    response = None
    
    serializer = LoginSerializer(data = request.data)
    
    if serializer.is_valid():
        password = serializer.data['password']
        username = serializer.data['username']
        
        user = authenticate( request, username= username , password = password )
        
        if user is None:
            response = Response({"message": INVAID_CREDENTIALS_MESSAGE } , status= HTTP_400_BAD_REQUEST)
    
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        response =  Response(
            {
                'message': USER_LOGGEDIN_MESSAGE.format(username = username) ,
                'refresh': str(refresh),
                'access': str(access)
            }
        )
        
    else:
        response = Response( serializer.errors , status= HTTP_400_BAD_REQUEST)
        
    return response 
    