from django.db import models

# Create your models here.
class Cart(models.Model):
    product=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=10, decimal_places=2 )
    quantity=models.PositiveIntegerField()
    image=models.ImageField()
    def __str__(self):
        return self.product
