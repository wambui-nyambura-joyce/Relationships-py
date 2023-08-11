from django import forms
from .models import Product
class ProductUploadForm(forms.ModelForm):
    class Meta:    #to inform the oarent class how the child behaves
        model = Product
        fields = "__all__"
        