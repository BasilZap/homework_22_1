from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from my_blog.models import MyBlog
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


# Создаем представление на создание статьи
class ArticleCreateView(CreateView):
    model = MyBlog
    fields = ('title', 'body', 'creation_date', 'is_published', 'image')
    success_url = reverse_lazy('my_blog:list')

    def form_valid(self, form):
        """
        Формируем поле slugify при создании статьи
        """
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


# Создаем представление на изменение статьи
class ArticleUpdateView(UpdateView):
    model = MyBlog
    fields = ('title', 'body', 'creation_date', 'is_published', 'image')

    def get_success_url(self):
        """
        Формируем возврат на просмотр статьи после редактирования
        """
        return reverse('my_blog:view', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        """
        Формируем поле slugify при изменении статьи
        """
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


# Создаем представление на вывод списка статей
class ArticleListView(ListView):
    model = MyBlog

    def get_queryset(self, *args, **kwargs):
        """
        Формирование условия на вывод статей только с признаком is_published
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


# Создаем представление на вывод статьи
class ArticleDetailView(DetailView):
    model = MyBlog

    def get_object(self, queryset=None):
        """
        Счетчик просмотров каждой статьи
        """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


# Создаем представление на удаление статьи
class ArticleDeleteView(DeleteView):
    model = MyBlog
    success_url = reverse_lazy('my_blog:list')


