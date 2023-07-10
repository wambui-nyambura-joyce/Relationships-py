from django.db import models
from vendor.models import Vendor

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 32)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    Vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name