from django.db import models
from django.utils import timezone
from categories.models import Category
from avatars.models import Avatar

class ShoeSize(models.Model):
    class ShoeSizeChoices(models.IntegerChoices):
        SIZE_35 = 35, '35' 
        SIZE_36 = 36, '36' 
        SIZE_37 = 37, '37' 
        SIZE_38 = 38, '38' 
        SIZE_39 = 39, '39' 
        SIZE_40 = 40, '40' 
        SIZE_41 = 41, '41' 
        SIZE_42 = 42, '42' 
        SIZE_43 = 43, '43' 
        SIZE_44 = 44, '44' 
        SIZE_45 = 45, '45'

    size = models.IntegerField(choices=ShoeSizeChoices.choices)  # Use IntegerField here

    def __str__(self):
        return str(self.size)

class ClotheSize(models.Model):
    class ClotheSizeChoices(models.TextChoices):
        S = 'S', 'Small'
        M = 'M', 'Medium'
        L = 'L', 'Large'

    size = models.CharField(max_length=1, choices=ClotheSizeChoices.choices)

    def __str__(self):
        return str(self.size)

class Hue(models.Model):
    hue = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return self.hue if self.hue else 'No Hue'

class Product(models.Model):
    class GenderChoice(models.TextChoices):
        FEMALE = 'female', 'Female'
        MALE = 'male', 'Male'
        NEUTRAL = 'neutral', 'Neutral'
        
    image = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GenderChoice.choices, null=True)
    is_available = models.BooleanField(default=True)
    on_discount = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    hue = models.OneToOneField(Hue, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def get_price_after_discount(self):
        if self.on_discount: 
            discount = (self.discount_percentage / 100) * self.price 
            return self.price - discount 
        return self.price
    

    def save(self, *args, **kwargs):
        if not self.on_discount:
            self.discount_percentage = None
        super().save(*args, **kwargs)


class ShoeProduct(Product):
    sizes = models.ManyToManyField(ShoeSize, related_name='shoe_products')

class ClotheProduct(Product):
    sizes = models.ManyToManyField(ClotheSize, related_name='clothe_products')
