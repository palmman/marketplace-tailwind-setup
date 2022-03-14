from re import T
from statistics import mode
from django.db import models

# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
