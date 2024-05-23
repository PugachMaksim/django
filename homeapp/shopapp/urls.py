from django.urls import path
from .views import index, add_client, add_product, client_orders, add_order, AddClient

urlpatterns = [
    path('', index, name='index'),
    path('add_user/', add_client, name='add_client'),
    path('add_product/', add_product, name='add_product'),
    path('order/add/', add_order, name='add_order'),
    path('order/client_orders/', client_orders, name='client_orders'),
    # path('order/update_client/', add_client_image, name='add_client_image'),
    # path('home/', client_image, name='client_image'),
    path('uspeh/', AddClient.as_view()),
]
