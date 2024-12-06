from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product
from categories.models import Category
from shopping_cart.models import ShoppingCart, ShoppingCartItem
from shopping_cart.utility import ShoppingCartMechanism

User = get_user_model()

class ShoppingCartTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.category = Category.objects.create(title='Test Category')
        self.product = Product.objects.create(
            title='Test Product',
            price=10.00,
            is_available=True,
            available_quantity=10,  # Ensure available_quantity is set
            category=self.category
        )
        self.cart_mechanism = ShoppingCartMechanism(self.user)

    def test_add_to_cart(self):
        cart_item = self.cart_mechanism.add_to_cart(self.product.id)
        self.assertEqual(cart_item.quantity, 1)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.cart.user, self.user)

    def test_remove_from_cart(self):
        cart_item = self.cart_mechanism.add_to_cart(self.product.id)
        self.cart_mechanism.remove_from_cart(self.product.id)
        self.assertFalse(ShoppingCartItem.objects.filter(id=cart_item.id).exists())

    def test_clear_cart(self):
        self.cart_mechanism.add_to_cart(self.product.id)
        self.cart_mechanism.clear_cart()
        self.assertFalse(ShoppingCartItem.objects.filter(cart=self.cart_mechanism.get_cart()).exists())
