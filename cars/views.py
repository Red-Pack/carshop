from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.prefetch_related('images').all()
    return render(request, 'cars/car_list.html', {'cars': cars})
