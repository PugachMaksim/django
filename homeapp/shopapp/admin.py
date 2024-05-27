from django.contrib import admin
from .models import Client, Product, Order

admin.site.register(Client)
admin.site.register(Order)


@admin.action(description="Сбросить количество в 0")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']  # Выборка столбцов для отображения
    ordering = ['-quantity']  # сортировка по количеству
    list_filter = ['data_enter', 'price']  # Фильтр
    search_fields = ['description']
    search_help_text = "Поиск по полю Описание продукта"
    actions = [reset_quantity]  # добавление действия в список
    readonly_fields = ['data_enter']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара',
                'fields': ['description', 'image']
            },
        ),
        (
            'Money',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]


admin.site.register(Product, ProductAdmin)
