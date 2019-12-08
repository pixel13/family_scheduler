from django.urls import path
from . import views

app_name = 'scheduler'
urlpatterns = [
    path('', views.week, name = 'week'),
    path('item', views.save_item, name = 'save_item')
]