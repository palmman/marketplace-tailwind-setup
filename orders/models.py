from distutils.command.upload import upload
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User

from shop.models import Product


# Create your models here.


class Order(models.Model):
    
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    bank_slip = models.ImageField(upload_to="bank_slip", blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField(blank=True, null=True)
    order_total = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name
    
class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    