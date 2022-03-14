from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>', views.add_cart, name='add_cart'),
    path('deleat_item/<int:product_id>', views.delete_cart_item, name='deleat_item'),
]