from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phoneNumber", "delivery_time", "is_delivered")
admin.site.register(Delivery, DeliveryAdmin)