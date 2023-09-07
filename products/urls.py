from django.urls import path
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
    CategoryCreateView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('', ProductListView.as_view(), name='list'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('category/', CategoryCreateView.as_view(), name='category')
]