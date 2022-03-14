from django.shortcuts import render, redirect
from orders.forms import CheckOutForms

import datetime
from .models import OrderItem, Order
from shop.models import Product

from carts.models import CartItem

# Create your views here.


def order(request, total=0, quantity=0,):
    
    current_user= request.user
    cart_items = CartItem.objects.filter(buyer=current_user)
    
    
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    grand_total = total
    
    if request.method == "POST":
       form = CheckOutForms(request.POST, request.FILES)
       if form.is_valid():
            add_order = form.save(commit=False)
            add_order.buyer = current_user
            add_order.order_total = grand_total
            add_order.save()
            
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(add_order.id)
            add_order.order_number = order_number
            add_order.save()
            

            return redirect('profile')      
    else:
        form = CheckOutForms()
    
        
    

                
    context = {
        'form':form,
    }
    
    return render(request, 'checkout.html', context)

def add_order(request):
    
    order = Order.objects.filter(buyer=request.user, status=False)
    cart_items = CartItem.objects.filter(buyer=request.user)
    
    print(order.first_name)
    
    
    # for item in cart_items:
    #     orderproduct = OrderItem()
    #     orderproduct.order = order.order_number
    #     orderproduct.seller = request.user.id
    #     orderproduct.product = item.product_id
    #     orderproduct.quantity = item.quantity
    #     orderproduct.product_price = item.product.price
    #     orderproduct.ordered = True
    #     orderproduct.save()
    
    # CartItem.objects.filter(user=request.user).delete()
    
    context = {
    }
    
    return render(request, 'checkout.html', context)

