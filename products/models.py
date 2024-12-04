from django.db import models

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

    size = models.CharField(max_length=2, choices=ShoeSizeChoices.choices)

    def __str__(self):
        return str(self.size)
    

class ClotheSize(models.Model):
    class ClotheSizeChoices(models.TextChoices):
        S = 's', 'S'
        M = 'm', 'M'
        L = 'l', 'L'

    size = models.CharField(max_length=1, choices=ClotheSizeChoices.choices)

    def __str__(self):
        return str(self.size)
    





class Product(models.Model):
    image = models.ForeignKey(Avatar, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    on_discount = models.BooleanField(default=False)
    # is available on couples?
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def __str__(self):
        return self.title
    


class ShoeProduct(Product):
    size = models.ManyToManyField(ShoeSize, related_name='shoe_sizes')



class ClotheProduct(Product):
    size = models.ManyToManyField(ClotheSize, related_name='clothe_sizes')
    





    
