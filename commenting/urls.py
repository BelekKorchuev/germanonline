# comments/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('comments/', home, name='home'),
]