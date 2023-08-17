from django import template

register = template.Library()


@register.filter()
def cut_text(val: str):
    if len(val) > 100:
        return val[:100]
    else:
        return val


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return '#'


@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'
    else:
        return '#'
