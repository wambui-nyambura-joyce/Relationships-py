from django.db import models
from addcart.models import Cart
from customersystem.models import CustomerSystem
from shipment.models import Delivery
# from payment.models import Payment
# Create your models here.
class Order(models.Model):
    # payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)
    order_number = models.IntegerField()
    order_total = models.IntegerField()
    customer = models.CharField(max_length=32)
    delivery_location = models.CharField(max_length=100)
    product_id = models.IntegerField()
    payment_options = models.CharField(max_length=100)
    order_date = models.DateField(auto_now=True)
    basket = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerSystem, null=True, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Delivery,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"Order {self.order_number}"