from django.urls import path
from .views import index, add_product, client_orders, add_order, add_client

urlpatterns = [
    path('', index, name='index'),
    path('add_user/', add_client, name='add_client'),
    path('add_product/', add_product, name='add_product'),
    path('order/add_order/', add_order, name='add_order'),
    path('order/client_orders/<int:client_id>', client_orders, name='client_orders'),
    # path('order/update_client/', add_client_image, name='add_client_image'),
    # path('home/', client_image, name='client_image'),
    # path('add_user/', AddClient.as_view()),
]
