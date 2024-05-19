import logging
import random
from datetime import timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from .forms import OrderAdd
from .models import Client, Product, Order
from django.utils import timezone

logger = logging.getLogger(__name__)


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
        product = Product(name=f'name{i}', description=f'Товар № {1 + i}', price=random.random() * 100,
                          quantity=random.randint(1, 50), data_enter='2024-05-12')
        product.save()
    return HttpResponse("Товары добавлены")


"""def add_order(request):
    if request.method == 'POST':
        form = OrderAdd(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            total_price = form.cleaned_data['total_price']
            order = Order(customer=customer, quantity=quantity, total_price=total_price)
            # form.save()
            order.save()
            order.product.add(product)
            logger.info(f'Получили {customer=}, {product=}, {quantity=}, {total_price=}.')
            return redirect("/")
    else:
        form = OrderAdd()
    return render(request, 'shopapp/add_orders.html', {'form': form})"""



def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client, order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client, order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client, order__order_date__gte=last_365_days).distinct()

    return render(request, 'hw3_app/client_orders.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })
