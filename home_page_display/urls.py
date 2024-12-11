from django.urls import path, include
from .views import HomePageView


urlpatterns = [
    path('home/', HomePageView.as_view(), name='homepage'),  # Define a separate path for the API view
]
