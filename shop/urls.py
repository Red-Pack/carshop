from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, checkout, pay_order, cancel_order

app_name = 'cart'
urlpatterns = [
    path("", cart_view, name="cart_view"),
    path("add/<int:car_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),
    path("checkout/", checkout, name="checkout"),
    path('pay/<int:order_id>/', pay_order, name='pay_order'),
    path('cancel/<int:order_id>/', cancel_order, name='cancel_order'),

]
