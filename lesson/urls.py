from django.urls import path
from .views import view_question, quiz_completed, theory_view


app_name = 'lesson'
urlpatterns = [
    path('question/<int:question_id>/', view_question, name='view_question'),
    path('quiz_completed/', quiz_completed, name='quiz_completed'),
    path('theory/<int:theme_id>/', theory_view, name='theory_view'),
]
