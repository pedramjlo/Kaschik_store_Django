from django.db import models


from django.contrib.auth import get_user_model 
from shopping_cart.models import ShoppingCart

User = get_user_model()


class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True) # will be set to current time once is_paid is True



