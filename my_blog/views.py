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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleDeleteView(DeleteView):
    model = MyBlog
    success_url = reverse_lazy('my_blog:list')


