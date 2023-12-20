from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main_view.models import ListOfTheme


class ThemeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(ListOfTheme, on_delete=models.CASCADE)  # Замените ListOfTheme на вашу модель тем
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.theme.theme} - Completed: {self.is_completed}"


@receiver(post_save, sender=User)
def create_user_theme_progress(sender, instance, created, **kwargs):
    if created:
        create_theme_progress_for_user(instance)


def create_theme_progress_for_user(user):
    themes = ListOfTheme.objects.all()

    # Создаем записи прогресса для каждой темы
    for theme in themes:
        ThemeProgress.objects.create(user=user, theme=theme)
