from distutils.command.upload import upload
from venv import create
from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    price = models.IntegerField(null=True)
    img = models.ImageField(upload_to='products_img')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    