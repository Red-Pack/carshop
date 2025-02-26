from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Order
from cars.models import Car

def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "shop/cart.html", {"cart": cart})

def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, car=car)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    referer = request.META.get('HTTP_REFERER')
    # Если referer существует и начинается с '/' или 'http', возвращаем его, иначе - главную страницу
    if referer and (referer.startswith('/') or referer.startswith('http')):
        return redirect(referer)
    else:
        return redirect('/')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.cart.user == request.user:
        item.delete()

    return redirect("cart:cart_view")

def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(user=request.user, total_price=cart.total_price())
    cart.items.all().delete()

    return redirect("order_history")
