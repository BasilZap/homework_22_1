from django.shortcuts import render
from products.models import Product


# Формируем отображение продуктов на странице index
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'products/index.html', context)


# Формируем отображение продукта на странице product
def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'{product_item.product_name}'.capitalize()
    }
    return render(request, 'products/product.html', context)
