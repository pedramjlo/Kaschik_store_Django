from django.shortcuts import render, get_object_or_404
from categories.models import Category
from products.models import Product
from shopping_cart.models import ShoppingCart
from shopping_cart.serializers import ShoppingCartSerializer
from products.serializers import ProductSerializer
from categories.serializers import CategorySerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

class HomePageView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        try:
            shopping_cart = get_object_or_404(ShoppingCart, status='active', user=request.user)
            shopping_cart_serializer = ShoppingCartSerializer(shopping_cart)
        except:
            shopping_cart_serializer = None

        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)

        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)

        data = { 
            'shopping_cart': shopping_cart_serializer.data if shopping_cart_serializer else None, 
            'products': products_serializer.data,
            'categories': categories_serializer.data  
        } 
        
        return Response(data, status=status.HTTP_200_OK)
