from django.contrib.auth.models import User
from django.db import models
from main_view.models import ListOfTheme


class Question(models.Model):
    theme_choice = models.ForeignKey(ListOfTheme, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    order = models.PositiveIntegerField(unique=True, default=0)
    is_answered = models.BooleanField(default=False)

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

    def __str__(self):
        return f"{self.question.question_text} - {'Correct' if self.is_correct else 'Incorrect'}"


class Theory(models.Model):
    theme_choice = models.ForeignKey(ListOfTheme, on_delete=models.CASCADE)
    theory = models.TextField()

    def __str__(self):
        return self.theory
