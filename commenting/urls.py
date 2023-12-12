# comments/urls.py
from django.urls import path
from .views import comments

urlpatterns = [
    path('comments/', comments, name='comments'),
]