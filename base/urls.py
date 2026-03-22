from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.all_products, name='all_products'),
    path('products/<int:pk>/', views.machine_detail, name='machine_detail'),
    path('machine-info/', views.machine_info, name='machine_detail'),
    path('product-detail/', views.machine_detail, name='machine_detail'),
]