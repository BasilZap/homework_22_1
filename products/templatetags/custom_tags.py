from django import template

register = template.Library()


@register.filter()
def cut_text(val: str):
    if len(val) > 100:
        return val[:100]
    else:
        return val
