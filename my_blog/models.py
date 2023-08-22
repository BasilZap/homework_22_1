from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Описание модели Блог
class MyBlog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    slug = models.CharField(max_length=200, verbose_name='Slug')
    body = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='product/', verbose_name='Фото', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} {self.is_published} {self.view_count}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
