from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название')
    product_description = models.TextField(verbose_name='Описание')
    image_preview = models.ImageField(upload_to='product/', verbose_name='Фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена за покупку')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    change_date = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} {self.price} {self.creation_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
