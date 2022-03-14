from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('add_order/', views.add_order, name='add_order'),
]