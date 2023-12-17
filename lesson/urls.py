from django.urls import path
from .views import view_question, quiz_completed

app_name = 'lesson'
urlpatterns = [
    path('question/<int:question_id>/', view_question, name='view_question'),
    path('quiz_completed/', quiz_completed, name='quiz_completed'),

]
