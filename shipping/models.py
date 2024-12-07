from django.db import models
from datetime import timedelta
from django.utils import timezone


class Shipping(models.Model):
    class ShippingChoices(models.TextChoices):
        AIRCARGO = 'aircargo', 'AirCargo'
        POST = 'post', 'Post'
        TIPAX = 'tipax', 'Tipax'


    shipping_choice = models.CharField(max_length=8, choices=ShippingChoices.choices, default='tipax')
    # shipping fee is basically a percentage value of the total order fee 
    fee = models.DecimalField(max_digits=10, decimal_places=1)
    delivery_on = models.DateField()

    def save(self, *args, **kwargs):
        if not self.delivery_on:
            if self.shipping_choice == 'aircargo':
                self.fee = 12  # % of the total order fee (+products+)
                self.delivery_on = timezone.now() + timedelta(hours=12)
            elif self.shipping_choice == 'post':
                self.fee = 8
                self.delivery_on = timezone.now() + timedelta(days=5)
            elif self.shipping_choice == 'tipax':
                self.fee = 6
                self.delivery_on = timezone.now() + timedelta(days=4)
        super().save(*args, **kwargs)
