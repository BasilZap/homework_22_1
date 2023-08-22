from django import template
from django.conf import settings

register = template.Library()


# Фильтр обрезает описание после 100 символов
@register.filter()
def cut_text(val: str):
    if len(val) > 100:
        return f'{val[:100]}...'
    else:
        return val


# Фильтр позволяет указывать путь к картинке в виде {{ object.image|mediapath }}
@register.filter()
def mediapath(val):
    if val:
        return f'{settings.MEDIA_URL}{val}'
    else:
        return '#'


# Тег позволяет указывать путь к картинке в виде {% mediapath object.image %}
@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return '#'
