from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerSystem(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.name