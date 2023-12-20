from django.urls import path
from .views import profile, ProfileUser

app_name = 'user_profile'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile_update/', ProfileUser.as_view(), name='profile_update'),

]
