from django import forms
from .models import Customer
class CustomerUploadForm(forms.ModelForm):
    class Meta:    #to inform the oarent class how the child behaves
        model = Customer
        fields = "__all__"
        