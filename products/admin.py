from django.contrib import admin
from products.models import Category, Product


# Настройка отображения для категорий в Админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


# Настройка отображения для продуктов в Админке
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)