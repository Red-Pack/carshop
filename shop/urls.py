from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, checkout

urlpatterns = [
    path("cart/", cart_view, name="cart_view"),
    path("cart/add/<int:car_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),
    path("checkout/", checkout, name="checkout"),
]
