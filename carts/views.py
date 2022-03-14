from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from carts.models import CartItem, Cart

# Create your views here.


def _cart_id(request):
    
    cart = request.session.session_key
    
    if not cart:
        
        cart = request.session.create()
    
    print(cart)
    
    return cart

def add_cart(request, product_id):
    
    user = request.user
    product = Product.objects.get(id=product_id)
    
    if user.is_authenticated:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart by cart_id present the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()
        
        try:
            cart_item = CartItem.objects.get(product=product, buyer=request.user)
            #if cart_item.quantity<cart_item.product.stock :
            cart_item.quantity+=1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product,
                buyer=request.user,
                quantity=1
            )
            cart_item.save()
            
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart by cart_id present the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()

        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            #if cart_item.quantity<cart_item.product.stock :
            cart_item.quantity+=1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=1
            )
            cart_item.save()

        return redirect('cart')


        # is_cart_item_exists = CartItem.objects.filter(product=product, buyer=user).exists()
        # if is_cart_item_exists:
        #     cart_item = CartItem.objects.filter(product=product, buyer=user)

    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(buyer=request.user, is_active=True)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
    for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
            
    
        
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'total':total,
        'quantity':quantity,
    }
    return render(request, 'cart.html', context)


def delete_cart_item(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.get(product=product, buyer = request.user)
    else:
        cart = Cart.objects.filter(cart_id = _cart_id(request))
        cart_items = CartItem.objects.get(product=product)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
        
    
    return redirect('cart')