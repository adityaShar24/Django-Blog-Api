from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import UserSerializer , LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

    
@api_view(['POST'])
def login_user(request):
    data = request.data
    
    serializer = LoginSerializer(data=data)
    
    if serializer.is_valid(raise_exception=True):
        username = serializer.data['username']
        password = serializer.data['password']
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=400)
        
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        
        
    return Response(serializer.errors, status=400)
