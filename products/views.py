from django.shortcuts import render


from .serializers import ProductSerializer
from .models import ShoeProduct

from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound


from django.contrib.auth import get_user_model 



User = get_user_model()


class MenShoesPagination(PageNumberPagination): 
    page_size = 10


class MenShoesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ShoeProduct.objects.filter(gender='male', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = MenShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No men shoes product was found")
        return queryset

