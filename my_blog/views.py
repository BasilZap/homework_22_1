from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from my_blog.models import MyBlog
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class ArticleCreateView(CreateView):
    model = MyBlog
    fields = ('title', 'body', 'creation_date', 'is_published', 'image')
    success_url = reverse_lazy('my_blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = MyBlog
    fields = ('title', 'body', 'creation_date', 'is_published', 'image')
    #success_url = reverse_lazy('my_blog:list')

    def get_success_url(self):
        return reverse('my_blog:view', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleListView(ListView):
    model = MyBlog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = MyBlog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleDeleteView(DeleteView):
    model = MyBlog
    success_url = reverse_lazy('my_blog:list')


