from django.contrib import admin
from .models import Product, ShoeProduct, ShoeSize


admin.site.register(Product)
admin.site.register(ShoeProduct)
admin.site.register(ShoeSize)
