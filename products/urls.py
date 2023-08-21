from django.urls import path
from products.views import ProductsListView, ProductDetailView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),

]