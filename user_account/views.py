from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny
from rest_framework import status 
from django.contrib.auth import get_user_model 

from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt

from .serializers import LoginSerializer, RegisterSerializer 
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch')
class AuthView(APIView):
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return User.objects.all() 

    def post(self, request): 
        if 'login' in request.path: 
            return self.login(request) 
        elif 'register' in request.path: 
            return self.register(request)


    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if not user.is_active:
                return Response({'error': 'Account is inactive'}, status=status.HTTP_400_BAD_REQUEST)
            refresh = RefreshToken.for_user(user)
            return Response({ 
                'refresh': str(refresh), 
                'access': str(refresh.access_token), 
                }, 
                status=status.HTTP_200_OK) 
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


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
