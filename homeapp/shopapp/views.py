import logging
import random
from datetime import timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView

from .forms import OrderAdd, AddUser
from .models import Client, Product, Order
from django.utils import timezone

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'shopapp/index.html')


def add_client(request):
    if request.method == 'POST':
        form = AddUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = AddUser()
    return render(request, 'shopapp/update_client.html', {'form': form})


def add_product(request):
    for i in range(50):
        product = Product(name=f'name{i}', description=f'Товар № {1 + i}', price=random.random() * 100,
                          quantity=random.randint(1, 50), data_enter='2024-05-12')
        product.save()
    return HttpResponse("Товары добавлены")


def add_order(request):
    if request.method == 'POST':
        form = OrderAdd(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()
        return redirect("index")
    else:
        form = OrderAdd()
    return render(request, 'shopapp/add_orders.html', {'form': form})


def client_orders(request, client_id):
    # client = Client.objects.get(pk=client_id)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Order.objects.filter(customer_id=client_id,
                                                     date_ordered__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Order.objects.filter(customer_id=client_id,
                                                      date_ordered__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Order.objects.filter(customer_id=client_id,
                                                       date_ordered__gte=last_365_days).distinct()

    return render(request, 'shopapp/client_orders.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })
