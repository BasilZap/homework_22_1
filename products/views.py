from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product
from django.urls import reverse_lazy, reverse
from products.forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        """
        Формируем возврат на просмотр продукта после редактирования
        """
        return reverse('products:view', args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
