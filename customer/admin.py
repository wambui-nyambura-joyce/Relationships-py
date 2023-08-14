from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone_number","address")
admin.site.register(Customer, CustomerAdmin)