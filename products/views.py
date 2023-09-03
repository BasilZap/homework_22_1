from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product
from django.urls import reverse_lazy, reverse


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'image_preview', 'category', 'price', 'creation_date',
              'change_date')
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'image_preview', 'category', 'price', 'creation_date',
              'change_date')

    def get_success_url(self):
        """
        Формируем возврат на просмотр статьи после редактирования
        """
        return reverse('products:view', args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
