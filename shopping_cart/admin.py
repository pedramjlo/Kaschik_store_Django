from django.contrib import admin
from .models import ShoppingCart

from iranian_cities.admin import IranianCitiesAdmin


@admin.register(ShoppingCart)
class TestModelAdmin(IranianCitiesAdmin):
    pass