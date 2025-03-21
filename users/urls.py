from django.urls import path
from .views import register_view, login_view, logout_view, order_history, profile_view, profile_edit

app_name = 'user'
urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('orders/', order_history, name='order_history'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]
