from django.urls import path
from .views import MenShoesView

urlpatterns = [
    path("men_shoes/", MenShoesView.as_view(), name='men-shoes'),

]
