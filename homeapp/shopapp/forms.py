from django import forms
from .models import Product, Client, Order


class OrderAdd(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products', 'quantity']


class AddUser(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
