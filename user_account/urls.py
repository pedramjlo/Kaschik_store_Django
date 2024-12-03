from django.urls import path

from .views import AuthView


urlpatterns = [ 
    path('api/auth/login/', AuthView.as_view(), name='login'), 
    path('api/auth/register/', AuthView.as_view(), name='register'), 
]
