from django.db import models
from django.core.validators import MinValueValidator

from django.contrib.auth import get_user_model 

from products.models import Product


User = get_user_model()


class ShoppingCart(models.Model):
    class CartStatusChoice(models.TextChoices):
        ACTIVE = 'active', 'Active'
        COMPLETED = 'completed', 'Completed'
        ABANDONED = 'abandoned', 'Abandoned'


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
    address = models.TextField()
    status = models.CharField(max_length=9, choices=CartStatusChoice.choices, default=CartStatusChoice.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)


    def update_total_price(self):
        total = sum(item.get_total_price() for item in self.cart_items.all())
        self.total_price = total
        self.save()
    


class ShoppingCartItem(models.Model):  
    cart = models.ForeignKey(ShoppingCart, related_name='cart_items', on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.title} {self.quantity}x"


    def get_total_price(self):
        return (self.product.price or 0) * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.update_total_price()