from django.shortcuts import render
from .schedule.week import WeekSchedule
from .models import Schedule
import datetime

def week(request):
    categories = {x.category.id:x.category.name for x in Schedule.objects.all()}
    schedule = WeekSchedule(categories)
    context = {
        'schedule': schedule.getSchedule(),
        'categories': categories
    }
    return render(request, 'scheduler/week.html', context)
