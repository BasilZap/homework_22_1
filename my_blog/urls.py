from django.urls import path
from my_blog.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from my_blog.apps import MyBlogConfig

app_name = MyBlogConfig.name

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('', ArticleListView.as_view(), name='list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),

]