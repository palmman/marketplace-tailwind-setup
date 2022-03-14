from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('shop/<slug:category_slug>/', views.category, name='category_product'),
    
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    
    path('profile/', views.profile, name='profile'),
    path('profile/addproduct/', views.add_product, name='add_product'),
]
