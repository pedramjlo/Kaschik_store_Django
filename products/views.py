from django.shortcuts import render


from .serializers import ProductSerializer
from .models import Product, ShoeProduct, ClotheProduct, AccessoryProduct

from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound


from django.contrib.auth import get_user_model 



User = get_user_model()


class ShoesPagination(PageNumberPagination): 
    page_size = 10


class MenShoesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ShoeProduct.objects.filter(gender='male', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No men shoes product was found")
        return queryset


class WomenShoesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ShoeProduct.objects.filter(gender='female', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No women shoes product was found")
        return queryset
    



class MenSuitsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ClotheProduct.objects.filter(gender='male', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No men suits product was found")
        return queryset
    


class WomenDressesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = ClotheProduct.objects.filter(gender='female', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No women dresses product was found")
        return queryset


class MenAccessoriesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = AccessoryProduct.objects.filter(gender='male', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No men accessory product was found")
        return queryset
    

class WomenAccessoriesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = AccessoryProduct.objects.filter(gender='female', is_available=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No women accessory product was found")
        return queryset


class CoupleCollectionView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(for_couples=True)
    permission_classes = [AllowAny,]
    pagination_class = ShoesPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No couple collections were found")
        return queryset



class AllCategoriesView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny,]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not queryset.exists():
            raise NotFound(detail="No categories were found")
        return queryset



    