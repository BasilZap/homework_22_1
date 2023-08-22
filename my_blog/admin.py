from django.contrib import admin
from my_blog.models import MyBlog


# Настройка отображения для категорий в Админке
@admin.register(MyBlog)
class MyBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'creation_date', 'is_published')
