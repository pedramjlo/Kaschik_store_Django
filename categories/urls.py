from django.urls import path
from .views import MenCategoriesView, WomenCategoriesView

urlpatterns = [

    path("men/", MenCategoriesView.as_view(), name='men-categories'),
    path("wommen/", WomenCategoriesView.as_view(), name='men-categories'),
]
