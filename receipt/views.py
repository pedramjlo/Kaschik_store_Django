from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model

from .models import Receipt
from shipping.models import Shipping
from .serializers import ReceiptSerializer
from shopping_cart.models import ShoppingCart

User = get_user_model()

class ReceiptView(APIView):
    permission_classes = [IsAuthenticated]

    def vip_membership_total_cost(self, shopping_cart, user):
        order_fee = shopping_cart.total_price
        vip_discount = user.membership.discount_percentage
        discount_amount = (vip_discount / 100) * order_fee
        return order_fee - discount_amount

    def get_queryset(self, request, cart_id):
        user = request.user
        shopping_cart, created = ShoppingCart.objects.get_or_create(id=cart_id, status='active', defaults={'user': user})
        return shopping_cart

    def get(self, request, cart_id):
        user = request.user

        available_shipping_methods = ['post', 'tipax']
        membership_discount_message = ""

        if user.membership and user.membership.type == 'vip':
            available_shipping_methods.append('aircargo')
            membership_discount_message += f"{user.membership.discount_percentage}% discount will be applied to your total order + shipping fee"

        elif user.membership and user.membership.type == 'silver':
            membership_discount_message += f"{user.membership.discount_percentage}% discount will be applied to your total order fee"

        elif user.membership and user.membership.type == 'bronze':
            membership_discount_message += f"{user.membership.discount_percentage}% discount will be applied to your total order fee"
        else:
            membership_discount_message += "no discount will be applied to your total order fee"

        return Response({
            'available_shipping_methods': available_shipping_methods,
            'membership_discount_message': membership_discount_message
        }, status=status.HTTP_200_OK)

    def post(self, request, cart_id):
        user = request.user
        shopping_cart = self.get_queryset(request, cart_id)
        shipping = shopping_cart.shipping  # Assuming a one-to-one relationship

        receipt = Receipt.objects.create(
            user=user,
            shopping_cart=shopping_cart,
            shipping=shipping
        )
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



