from django import forms
from .models import ShoppingCart

class ShoppingUploadForm(forms.ModelForm): 
    
    class Meta:
        model = ShoppingCart
        fields = "__all__"
