from django.core.cache import cache
from config.settings import CACHE_ENABLED
from products.models import Category


# Функция кэширования категорий продуктов
def get_cache_categories():
    if CACHE_ENABLED is True:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
