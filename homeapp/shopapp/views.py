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


def index(response):
    return HttpResponse("Добро пожаловать")


# def add_client(request):
#     for i in range(50):
#         client = Client(name=f'name{i}', mail=f'email{i}@mail.ru', tel_number=81234567890 + i,
#                         adres=f'Спб, 3-я улица строителей д 12 кв {i}', data_registr=f'2024-05-12')
#         client.save()
#     return HttpResponse("Клиенты добавлены")


def add_client(request):
    if request.method == 'POST':
        form = AddUser(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
        return redirect('index')
    else:
        form = AddUser()
    return render(request, 'shopapp/update_client.html', {'form': form})


# def client_image(request):
#     if request.method == 'POST' and request.FILES:
#         file = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(file.name, file)
#         file_url = fs.url(filename)
#         return render(request, 'home.html', {'file_url': file_url})
#     return render(request, 'shopapp/home.html')


class AddClient(CreateView):
    model = Client
    form_class = AddUser
    extra_context = {"clients": Client.objects.all()}  #Вывод всех записей
    template_name = 'add_user.html' # Шаблон на ввод данных
    success_url = '/uspeh/' #Куда перенаправляется после успешной записи



# def add_client_image(request, client_id):
#     client = Client.objects.get(id=client_id)
#     if request.method == 'POST':
#         form = AddUser(request.POST, request.FILES, instance=client)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = AddUser(instance=client)
#     return render(request, 'update_client.html', {'form': form, 'client': client})


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


# def add_order(request):
#     if request.method == 'POST':
#         form = OrderAdd(request.POST)
#         if form.is_valid():
#             customer = form.cleaned_data['customer']
#             product = form.cleaned_data['products']
#             quantity = form.cleaned_data['quantity']
#             # total_price = form.cleaned_data['total_price']
#             order = Order(customer=customer, quantity=quantity)
#             # form.save()
#             order.save()
#             # prod = get_object_or_404(Product, name=product)
#             prod = Product.objects.get(id=product)
#             order.products.add(prod)
#             return redirect("/")
#     else:
#         form = OrderAdd()
#     return render(request, 'shopapp/add_orders.html', {'form': form})


def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client,
                                                       order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client,
                                                        order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client,
                                                         order__order_date__gte=last_365_days).distinct()

    return render(request, 'hw3_app/client_orders.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })
