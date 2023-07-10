from django.contrib import admin
from .models import CustomerSystem

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone_number","address")
admin.site.register(CustomerSystem,CustomerAdmin)