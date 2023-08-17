from django.urls import path
from products.views import index, product
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/product/', product, name='product'),

]