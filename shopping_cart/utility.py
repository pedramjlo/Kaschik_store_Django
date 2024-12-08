from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .models import ShoppingCart, ShoppingCartItem
from products.models import Product

class ShoppingCartMechanism:
    def __init__(self, user, status='active'):
        self.user = user
        self.cart, created = ShoppingCart.objects.get_or_create(user=user, status=status)

    def get_cart(self):
        return self.cart

    def update_cart_status(self):
        if ShoppingCart.objects.count() >= 1:
            self.cart.status = 'active'
            self.cart.save()
        elif self.cart.status == 'active' and self.user.last_login:
            time_since_last_login = timezone.now() - self.user.last_login
            if time_since_last_login > timedelta(hours=72):
                self.cart.status = 'abandoned'
                self.cart.save()

    def add_to_cart(self, product_id):
        product = get_object_or_404(Product, id=product_id, is_available=True)
        if product.available_quantity > 0:
            cart_item, created = ShoppingCartItem.objects.get_or_create(cart=self.cart, product=product)
            self.update_cart_status()
            if product.available_quantity > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()
                product.available_quantity -= 1
                product.save()
                self.cart.update_total_price()
                return cart_item
            else:
                raise ValueError("There are no more of this product available")
        else:
            raise ValueError("Product is out of stock")

    def remove_from_cart(self, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item = get_object_or_404(ShoppingCartItem, product=product, cart=self.cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        
        product.available_quantity += 1
        product.save()
        self.cart.update_total_price()
        return cart_item

    def clear_cart(self):
        cart_items = ShoppingCartItem.objects.filter(cart=self.cart)
        for item in cart_items:
            item.product.available_quantity += item.quantity
            item.product.save()
            item.delete()
        self.cart.update_total_price()
        return cart_items
