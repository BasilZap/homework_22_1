from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from my_blog.models import MyBlog
from django.urls import reverse_lazy


class ArticleCreateView(CreateView):
    model = MyBlog
    fields = ('title', 'body', 'creation_date', )
    success_url = reverse_lazy('my_blog:list')


class ArticleUpdateView(UpdateView):
    model = MyBlog
    fields = ('title', 'body', 'creation_date', )
    success_url = reverse_lazy('my_blog:list')


class ArticleListView(ListView):
    model = MyBlog


class ArticleDetailView(DetailView):
    model = MyBlog


class ArticleDeleteView(DeleteView):
    model = MyBlog
    success_url = reverse_lazy('my_blog:list')


