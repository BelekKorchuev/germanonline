from django.contrib.auth.models import User
from django.db import models
from main_view.models import ListOfTheme


class Question(models.Model):
    theme_choice = models.ForeignKey(ListOfTheme, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    next_question = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question_choice = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ('question', 'user')
