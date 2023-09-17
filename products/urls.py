from django.urls import path
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
    CategoryCreateView, categories_list, categories_products
from products.apps import ProductsConfig
from django.views.decorators.cache import cache_page

app_name = ProductsConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('', ProductListView.as_view(), name='list'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('category/', CategoryCreateView.as_view(), name='category'),
    path('products/categories_list', categories_list, name='categories_list'),
    path('<int:pk>/products', categories_products, name='categories_products'),
]
