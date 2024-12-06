from django.urls import path
from .views import MenShoesView, WomenShoesView, MenSuitsView, WomenDressesView, MenAccessoriesView, WomenAccessoriesView, CoupleCollectionView

urlpatterns = [
    path("men_shoes/", MenShoesView.as_view(), name='men-shoes'),
    path("women_shoes/", WomenShoesView.as_view(), name='women-shoes'),
    path("men_suits/", MenSuitsView.as_view(), name='men-suits'),
    path("women_dresses/", WomenDressesView.as_view(), name='women-dresses'),
    path("men_accessories/", MenAccessoriesView.as_view(), name='men-accessories'),
    path("women_accessories/", WomenAccessoriesView.as_view(), name='women-accessories'),
    path("couples_collections/", CoupleCollectionView.as_view(), name='couples-collections'),
]
