from ..models import Item, Category, CATEGORY_ICONSET
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

iconsets = Category.objects.filter(data_type = CATEGORY_ICONSET)

@register.simple_tag
def item(item):
    if not isinstance(item, Item):
        raise TypeError('Argument must be an Item')
    if _isIconsetItem(item):
        return _renderIconsetItem(item)
    else:
        return _renderEventItem(item)

@register.simple_tag
def splitlines(lines):
    return lines.splitlines()

def _isIconsetItem(item):
    return iconsets.filter(id = item.category.id).exists()

def _renderEventItem(item):
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

def _renderIconsetItem(item):
    return mark_safe('<img class="img-fluid" src="/static/scheduler/' + item.description + '" />')
    