from django.shortcuts import get_object_or_404

from .models import ShoppingCart, ShoppingCartItem
from products.models import Product


class ShoppingCartMechanism:
    def __init__(self, user, status='active'):
        self.user = user
        self.cart, created = ShoppingCart.objects.get_or_create(user=user, status=status)


    def get_cart(self):
        return self.cart


    def add_to_cart(self, product_id):
        product = get_object_or_404(Product, id=product_id, is_available=True)
        cart_item, created = ShoppingCartItem.objects.get_or_create(cart=self.cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        self.cart.update_total_price()
        return cart_item


    def remove_from_cart(self, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item = get_object_or_404(ShoppingCartItem, product=product, cart=self.cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        self.cart.update_total_price()
        return cart_item


    def clear_cart(self):
        cart_items = ShoppingCartItem.objects.filter(cart=self.cart)
        for item in cart_items:
            item.delete()
        self.cart.update_total_price()
        return cart_items
    
