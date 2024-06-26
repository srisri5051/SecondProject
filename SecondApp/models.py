

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class User(AbstractUser):
    dealer_details = models.CharField(max_length=100, blank=True, null=True)

    class Role(models.TextChoices):
        USERS = 'users', 'Users'
        DEALER = 'dealer', 'Dealer'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USERS)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.name



class Product(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  
    created_at = models.DateTimeField(default=timezone.now)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name





class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist: {self.product.name}"
    






class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def total_cost(self):
        return sum(item.product.price for item in self.cart_items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username