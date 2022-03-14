from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    
    cart_id = models.CharField(max_length=225, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    
class CartItem(models.Model):
    
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return str(self.product)