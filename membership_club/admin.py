from django.contrib import admin
from .models import MembershipClub


class MembershipClubAdmin(admin.ModelAdmin): 
    readonly_fields = ('price', 'discount_percentage', 'end_date') 
    
    def save_model(self, request, obj, form, change): 
        obj.save()


admin.site.register(MembershipClub, MembershipClubAdmin)
