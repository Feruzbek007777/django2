from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brands/', views.brand_list, name='brands'),
    path('cars/', views.car_list, name='cars'),
]