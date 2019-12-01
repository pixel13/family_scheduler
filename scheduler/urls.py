from django.urls import path
from . import views

app_name = 'scheduler'
urlpatterns = [
    path('', views.week, name = 'week')
]