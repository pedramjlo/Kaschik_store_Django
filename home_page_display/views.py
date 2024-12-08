from django.shortcuts import render, get_object_or_404

from products.models import Product

from shopping_cart.models import ShoppingCart
from shopping_cart.serializers import ShoppingCartSerializer

from products.serializers import ProductSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status



class HomePageView(APIView):
    permission_classes = [AllowAny, IsAuthenticated]
    
    def get(self, request):
        shopping_cart = get_object_or_404(ShoppingCart, status='active', user=request.user)
        shopping_cart_serializer = ShoppingCartSerializer(shopping_cart)
        
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)


        data = { 
        'shopping_cart': shopping_cart_serializer.data, 
        'products': products_serializer.data 
        } 
        
        return Response(data, status=status.HTTP_200_OK)