from django.urls import path
from .views import AllCategoriesView, MenCategoriesView, WomenCategoriesView

urlpatterns = [
    path("all_categories/", AllCategoriesView.as_view(), name='all-categories'),
    path("men/", MenCategoriesView.as_view(), name='men-categories'),
    path("women/", WomenCategoriesView.as_view(), name='men-categories'),
]
