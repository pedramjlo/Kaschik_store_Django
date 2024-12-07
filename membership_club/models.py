

"""
MEMBERSHIP CLUB' INSTRUCTIONS

THERE ARE 4 TYPES OF USER ACCOUNT ROLES:

    1 - REGULAR: FREE.
        -> No discount on shipping or order total price

    2 - BRONZE: CAN BE BOUGHT FOR; 59t a month, 173t for 3 months, 680t for a year. 
        -> 5% discount on every order fee.

    3 - SILVER: CAN BE BOUGHT FOR; 79t a month, 233t for 3 months, 980t for a year. 
        -> 12% discount on every order fee.

    4 - VIP: CAN BE BOUGHT FOR; 99.5 a month, 293.5t for 3 months, 1150t for a year. 
        -> 18% discount on every order + shipping fee.
"""

from django.db import models
from datetime import timedelta
from django.utils import timezone

class MembershipClub(models.Model):
    class MembershipTypes(models.TextChoices):
        REGULAR = 'regular', 'Regular'
        BRONZE = 'bronze', 'Bronze'
        SILVER = 'silver', 'Silver'
        VIP = 'vip', 'VIP'

    class MembershipLengthChoice(models.TextChoices):
        UNLIMITED = 'unlimited', 'Unlimited'
        ONE_MONTH = 'onemonth', 'OneMonth'
        THREE_MONTHS = 'threemonths', 'ThreeMonths'
        ONE_YEAR = 'oneyear', 'OneYear'

    type = models.CharField(max_length=11, choices=MembershipTypes.choices, null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    length = models.CharField(max_length=15, choices=MembershipLengthChoice.choices, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    discount_percentage = models.IntegerField(default=0, null=True, blank=False)

    def time_left(self):
        if self.end_date:
            return self.end_date - timezone.now().date()
        return None

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.start_date = timezone.now().date()

        if not self.end_date:
            if self.length == 'onemonth':
                self.end_date = self.start_date + timedelta(days=30)
            elif self.length == 'threemonths':
                self.end_date = self.start_date + timedelta(days=90)
            elif self.length == 'oneyear':
                self.end_date = self.start_date + timedelta(days=365)

        if self.type == 'regular':
            self.discount_percentage = 0
            self.price = None
            self.end_date = None
            self.length = 'unlimited'

        if self.type == 'bronze':
            self.discount_percentage = 5
            if self.length == 'onemonth':
                self.price = 59
            elif self.length == 'threemonths':
                self.price = 173
            elif self.length == 'oneyear':
                self.price = 680

        if self.type == 'silver':
            self.discount_percentage = 12
            if self.length == 'onemonth':
                self.price = 79
            elif self.length == 'threemonths':
                self.price = 233
            elif self.length == 'oneyear':
                self.price = 980

        if self.type == 'vip':
            self.discount_percentage = 18
            if self.length == 'onemonth':
                self.price = 99.5
            elif self.length == 'threemonths':
                self.price = 293.5
            elif self.length == 'oneyear':
                self.price = 1150

        # Check and update membership status
        if self.end_date and self.end_date <= timezone.now().date():
            self.type = self.MembershipTypes.REGULAR
            self.end_date = None
            self.discount_percentage = 0
            self.length = 'unlimited'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} membership"
