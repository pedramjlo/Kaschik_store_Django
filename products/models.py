from django.db import models

from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    on_discount = models.BooleanField(default=False)
    # is available on couples?
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    available_sizes = models.JSONField(blank=True, default=list)
    available_hues = models.JSONField(blank=True, default=list)


    def __str__(self):
        return self.title
    





    
