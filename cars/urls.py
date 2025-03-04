from django.urls import path
from .views import CarDetailView
from . import views

app_name = 'car'
urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]
