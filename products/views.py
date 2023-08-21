from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView, DetailView


class ProductsListView(ListView):
    model = Product
    template_name = 'products/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
