from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('createUser', views.createUser, name='createuser'),
    path('signup', views.signup, name='signup')
]