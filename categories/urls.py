from django.urls import path
from .views import AllCollectionsView, MenCategoriesView, WomenCategoriesView

urlpatterns = [
    path("all_collections/", AllCollectionsView.as_view(), name='all-collections'),
    path("men/", MenCategoriesView.as_view(), name='men-categories'),
    path("women/", WomenCategoriesView.as_view(), name='men-categories'),
]
