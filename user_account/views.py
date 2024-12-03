from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from django.contrib.auth import get_user_model 

from .serializers import LoginSerializer, RegisterSerializer 
from rest_framework_simplejwt.tokens import RefreshToken


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        if 'login' in request.path:
            pass


    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({ 
                'refresh': str(refresh), 
                'access': str(refresh.access_token), 
                }, 
                status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def register(self, request): 
        serializer = RegisterSerializer(data=request.data) 
        if serializer.is_valid(): 
            user = serializer.save() 
            refresh = RefreshToken.for_user(user) 
            return Response({ 
            'user': RegisterSerializer(user).data, 
            'refresh': str(refresh), 
            'access': str(refresh.access_token), 
            }, 
            status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)