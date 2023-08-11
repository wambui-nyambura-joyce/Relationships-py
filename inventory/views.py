from django.shortcuts import render

from inventory.models import Product
from .forms import ProductUploadForm
# Create your views here.
def upload_product(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product-upload.html',{"form":form})
def products_list(request):
    products = Product.objects.all()
    return render (request, "inventory/products_list.html", {"products": products})
def product_detail_view(request, id):
    product = Product.objects.get(id = id)
    return render(request, "inventory/product_details.html", {"product":product})