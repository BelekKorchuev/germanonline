from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    def get_next_question(self):
        # Получаем следующий вопрос с увеличенным значением поля order
        next_question = Question.objects.filter(order__gt=self.order).order_by('order').first()
        return next_question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
