from django.urls import path
from .views import ReceiptView

urlpatterns = [
    path("order_receipt/<inti:d>/<str:user>", ReceiptView.as_view(), name='order_receipt'),
]
