

from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    dealer_details = models.CharField(max_length=100, blank=True, null=True)

    class Role(models.TextChoices):
        USERS = 'users', 'Users'
        DEALER = 'dealer', 'Dealer'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USERS)

    def __str__(self):
        return self.username

    
class Product(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=300,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

