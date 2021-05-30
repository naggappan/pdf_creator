from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<str:customer_name>/pdf/', views.getpdf, name = 'getpdf'),
    path('customer/<str:customer_name>/', views.detail, name='detail'),
   
]
