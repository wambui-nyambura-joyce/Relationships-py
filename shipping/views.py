from django.shortcuts import render,redirect
from .forms import ShippingUploadForm
from .models import Shipping

# Create your views here.

def upload_shipping(request):
    if request.method == 'POST':
        form = ShippingUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
      form = ShippingUploadForm()
     
    return render(request,'shipping/shipping_upload.html',{'form':form})
   
def shipping_list(request):
    shipping=Shipping.objects.all()
    return render(request,'shipping/shipping_list.html',{'shippings':shipping})
def  shipping_detail(request,id):
    shipping=Shipping.objects.get(id=id)
    return render(request,'shipping/shipping_detail.html',{'shipping':shipping})

def edit_shipping_view(request,id):
    shipping=Shipping.objects.get(id=id)
    if request.method == 'POST':
        form=ShippingUploadForm(request.POST,instance=shipping)
        if form.is_valid():
            form.save()
        return redirect('shipping_detail_view,id=id')     
    else:
        form=ShippingUploadForm(request.POST,instance=shipping)
        return render(request,'shipping/edit_shipping.html',{'form':form  })     





