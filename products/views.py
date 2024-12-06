from django.shortcuts import render


from .serializers import ProductSerializer
from .models import Product, ShoeProduct, ClotheProduct, AccessoryProduct

from shopping_cart.utility import ShoppingCartMechanism
from shopping_cart.serializers import ShoppingCartItemSerializer


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



class MenShoesView(APIView): 
    serializer_class = ProductSerializer 
    permission_classes = [AllowAny] 
    pagination_class = ShoesPagination 
    
    def get_queryset(self): 
        queryset = ShoeProduct.objects.filter(gender='male', is_available=True) 
        if not queryset.exists(): 
            raise NotFound(detail="No men shoes product was found") 
        return queryset 
    
    def get(self, request, *args, **kwargs): 
        queryset = self.get_queryset() 
        page = self.paginate_queryset(queryset) 
        
        if page is not None: 
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data) 
        else: 
            serializer = self.serializer_class(queryset, many=True) 
        return Response(serializer.data) 
    
    def post(self, request, *args, **kwargs): 
        if 'add_to_cart' in request.data: 
            cart_mechanism = ShoppingCartMechanism(request.user) 
            cart_item = cart_mechanism.add_to_cart(request.data['product_id']) 
            return Response({'status': 'item added to cart', 'cart_item': ShoppingCartItemSerializer(cart_item).data}, status=status.HTTP_200_OK) 
        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, *args, **kwargs): 
        if 'remove_from_cart' in request.data: 
            cart_mechanism = ShoppingCartMechanism(request.user) 
            cart_item = cart_mechanism.remove_from_cart(request.data['product_id']) 
            return Response({'status': 'item removed from cart', 'cart_item': ShoppingCartItemSerializer(cart_item).data}, status=status.HTTP_200_OK) 
        if 'clear_cart' in request.data: 
            cart_mechanism = ShoppingCartMechanism(request.user) 
            cart_items = cart_mechanism.clear_cart() 
            return Response({'status': 'cart cleared', 'cart_items': []}, status=status.HTTP_200_OK) 
        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    

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



class WomenShoesView(APIView): 
    serializer_class = ProductSerializer 
    permission_classes = [AllowAny] 
    pagination_class = ShoesPagination 
    
    def get_queryset(self): 
        queryset = ShoeProduct.objects.filter(gender='female', is_available=True) 
        if not queryset.exists(): 
            raise NotFound(detail="No men shoes product was found") 
        return queryset 
    
    def get(self, request, *args, **kwargs): 
        queryset = self.get_queryset() 
        page = self.paginate_queryset(queryset) 
        
        if page is not None: 
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data) 
        else: 
            serializer = self.serializer_class(queryset, many=True) 
        return Response(serializer.data) 
   



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







    