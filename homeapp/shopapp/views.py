import datetime
import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order
from django.db.models import F


def index(response):
    return HttpResponse("Добро пожаловать")


def add_client(request):
    for i in range(50):
        client = Client(name=f'name{i}', mail=f'email{i}@mail.ru', tel_number=81234567890 + i,
                        adres=f'Спб, 3-я улица строителей д 12 кв {i}', data_registr=f'2024-05-12')
        client.save()
    return HttpResponse("Клиенты добавлены")


def add_product(request):
    for i in range(50):
        product = Product(product_name=f'name{i}', product_description=f'Товар № {1 + i}', price=random.random() * 100,
                          quantity=random.randint(1, 50), data_enter='2024-05-12')
        product.save()
    return HttpResponse("Товары добавлены")


def add_order(request):
    for i in range(20):
        # order = Order(customer=random.randint(1, 51), products=random.randint(1, 51), quantity=random.randint(1, 50),
        #               date_ordered='2024-05-12')
        order = Order(customer=Client.objects.filter(id=random.randint(1, 51)), products=Product.objects.filter(id=random.randint(1, 51)),
                      quantity=random.randint(1, 50),
                      date_ordered='2024-05-12')
        order.save()
    return HttpResponse("Заказы добавлены")
