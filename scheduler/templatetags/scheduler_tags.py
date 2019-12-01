from ..models import Item
from django import template

register = template.Library()

@register.simple_tag
def item(item):
    if not isinstance(item, Item):
        raise TypeError('Argument must be an Item')
    result = ""
    if item.start:
        result = result + item.start.strftime("%H:%M")
    if item.start and item.end:
        result = result + "-"
    if item.end:
        result = result + item.end.strftime("%H:%M")
    if item.start or item.end:
        result = result + " "
    result = result + item.description
    return result