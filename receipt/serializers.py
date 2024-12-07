from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Receipt

User = get_user_model()



class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'