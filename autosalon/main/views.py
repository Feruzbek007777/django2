from django.shortcuts import render
from .models import Brand, Car

def home(request):
    return render(request, 'main/home.html')

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'main/brands.html', {'brands': brands})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'main/cars.html', {'cars': cars})