from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .schedule.week import WeekSchedule
from .models import Schedule, Item, Category
import datetime

@ensure_csrf_cookie
def week(request):
    categories = [c.category for c in Schedule.objects.all()]
    schedule = WeekSchedule(categories)
    context = {
        'schedule': schedule.getSchedule(),
        'categories': categories
    }
    return render(request, 'scheduler/week.html', context)

def save_item(request):
    if request.method != 'POST':
        raise HttpResponseNotAllowed('POST')

    item = request.POST
    i = Item(day = item['day'], category = Category(id = item['category']), description = item['description'])
    i.save()
    return JsonResponse({})
