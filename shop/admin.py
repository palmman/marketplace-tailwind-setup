from .models import Product
from django.contrib import admin

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('name', 'created', 'updated')


admin.site.register(Product,ProductAdmin)