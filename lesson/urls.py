from django.urls import path
from .views import quiz

app_name = 'lesson'
urlpatterns = [
    path('quiz/<int:question_id>/', quiz, name='quiz'),
]