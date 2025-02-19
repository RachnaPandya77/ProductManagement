from django.urls import path
from .views import welcome, register, product_list, add_product, order_product

urlpatterns = [
    path('', welcome, name='welcome'),
    path('register/', register, name='register'),
    path('products/', product_list, name='product_list'),
    path('add_product/', add_product, name='add_product'),
    path('order_product/<int:product_id>/', order_product, name='order_product'),
] 