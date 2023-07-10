from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=("product","image","quantity","price")
admin.site.register(Cart,CartAdmin)
        
