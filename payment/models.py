from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer