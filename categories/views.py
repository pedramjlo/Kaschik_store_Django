from django.shortcuts import render

from .serializers import CategorySerializer
from .models import Category

from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework import status 

from django.contrib.auth import get_user_model 



User = get_user_model()


class AllCollectionsView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny,]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No categories were found")
        return queryset


class WomenCategoriesView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        categories = Category.objects.filter(type="female")
        return categories

        
class MenCategoriesView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        categories = Category.objects.filter(type="male")
        return categories
    


