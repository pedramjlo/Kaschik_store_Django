from rest_framework import serializers

from .models import ShoppingCart, ShoppingCartItem


class ShoppingCart(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = '__all__'