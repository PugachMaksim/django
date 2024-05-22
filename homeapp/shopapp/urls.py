from django.urls import path
from .views import index, add_client, add_product, client_orders, add_order

urlpatterns = [
    path('', index, name='index'),
    path('add_client/', add_client, name='add_client'),
    path('add_product/', add_product, name='add_product'),
    path('order/add/', add_order, name='add_order'),
    path('order/client_orders/', client_orders, name='client_orders'),
]
