from django.urls import path
from .views import AboutUs, LevelList, themes_for_level

app_name = 'main_view'

urlpatterns = [
    path('about/', AboutUs.as_view(), name='about'),
    path('levels/', LevelList.as_view(), name='levels'),
    path('level_detail/<int:level_id>/', themes_for_level, name='level_detail'),
]