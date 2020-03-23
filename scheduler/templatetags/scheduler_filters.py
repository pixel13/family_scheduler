from ..models import CATEGORY_ICONSET
from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    return dictionary.get(key)

@register.filter
def filter_iconset(categories):
    iconset = []
    for category in categories:
        if category.data_type == CATEGORY_ICONSET:
            iconset.append(category)
    return iconset

@register.filter
def first_key(dictionary):
    return list(dictionary.keys())[0]

@register.filter
def last_key(dictionary):
    return list(dictionary.keys())[len(dictionary) - 1]