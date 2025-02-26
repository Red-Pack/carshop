from django.urls import path
from . import views

app_name = 'car'
urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]
