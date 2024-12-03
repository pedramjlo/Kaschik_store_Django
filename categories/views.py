from django.shortcuts import render

from .serializers import MenCategoriesSerializer, WomenCategoriesSerializer
from .models import Category

from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny
from rest_framework import status 
from django.contrib.auth import get_user_model 



User = get_user_model()



class WomenCategoriesView(ListAPIView):
    serializer_class = WomenCategoriesSerializer

    def get_queryset(self):
        categories = Category.objects.filter(type="female")
        return categories

        
class MenCategoriesView(ListAPIView):
    serializer_class = MenCategoriesSerializer

    def get_queryset(self):
        categories = Category.objects.filter(type="male")
        return categories

