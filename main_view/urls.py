from django.urls import path
from .views import AboutUs, LevelList

app_name = 'main_view'

urlpatterns = [
    path('about/', AboutUs.as_view(), name='about'),
    path('levels/', LevelList.as_view(), name='levels'),
]