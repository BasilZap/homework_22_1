from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product, Version
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from products.forms import ProductForm, VersionForm


# формируем представление на создания продукта
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


# формируем представление на редактирование продукта
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    # Добавление представления с версиями продукта
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        """
        Обновляем страницу редактирования
        """
        return reverse('products:edit', args=[self.kwargs.get('pk')])


# формируем представление на просмотр списка продуктов
class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


# формируем представление на просмотр продукта
class ProductDetailView(DetailView):
    model = Product


# формируем представление на удаление продукта
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
