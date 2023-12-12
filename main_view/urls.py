from django.urls import path
from .views import AboutUs, LevelList, ThemesForLevel

app_name = 'main_view'

urlpatterns = [
    path('about/', AboutUs.as_view(), name='about'),
    path('levels/', LevelList.as_view(), name='levels'),
    path('level_detail/<int:level_id>/', ThemesForLevel.as_view(), name='level_detail'),
]