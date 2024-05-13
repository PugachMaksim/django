import math

from django.db import models

"""
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

Допишите несколько функций CRUD для работы с моделями ОБЯЗАТЕЛЬНО"""


class Client(models.Model):
    name = models.CharField(blank=False, max_length=52)
    mail = models.EmailField(blank=False)
    tel_number = models.IntegerField(blank=False)
    adres = models.CharField(max_length=200)
    data_registr = models.DateTimeField(blank=False)


class Product(models.Model):
    product_name = models.CharField(blank=False, max_length=30)
    product_description = models.TextField(blank=False, default=None)
    price = models.DecimalField(blank=False, default=0, decimal_places=2, max_digits=10)
    quantity = models.IntegerField(blank=False, default=0)
    data_enter = models.DateTimeField(blank=False)


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(blank=False, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def calculate_total_price(self):
        return self.quantity * self.products.price

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super(Order, self).save(*args, **kwargs)
