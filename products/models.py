from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Описание модели Категория
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Описание модели Продукт
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


# Описание модели Версия продукта
class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=20, verbose_name='Версия')
    version_name = models.CharField(max_length=50, verbose_name='Название версии', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.product_name} {self.version_number} {self.is_active}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
