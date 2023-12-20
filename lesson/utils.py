from .models import ListOfTheme, Question, UserAnswer
from user_profile.models import ThemeProgress

def get_level_progress(user, level):
    themes_in_level = ListOfTheme.objects.filter(choose_level=level)
    completed_themes = ThemeProgress.objects.filter(user=user, theme__in=themes_in_level, is_completed=True).count()
    total_themes = themes_in_level.count()

    if total_themes == 0:
        return 0

    progress_percentage = (completed_themes / total_themes) * 100
    return int(progress_percentage)


def get_next_question(theme, question):
    try:
        next_question = Question.objects.filter(theme_choice=theme, id=question.next_question_id).first()
        return next_question
    except Question.DoesNotExist:
        return None


def complete_level(user, theme):
    theme_progress, created = ThemeProgress.objects.get_or_create(user=user, theme=theme)

    if not theme_progress.is_completed:
        theme_progress.is_completed = True
        theme_progress.save()

    if all(theme_progress.is_completed for theme_progress in ThemeProgress.objects.filter(user=user)):
        pass


def get_or_create_user_answer(user, question):
    user_answer, created = UserAnswer.objects.get_or_create(user=user, question=question)
    return user_answer, created


def get_next_question_for_theme(theme):
    try:
        first_question = Question.objects.filter(theme_choice=theme).first()
        return first_question
    except Question.DoesNotExist:
        return None


def complete_and_get_next_question(user, question, form):
    user_answer, created = get_or_create_user_answer(user, question)

    user_answer.answer = form.cleaned_data['choices']
    user_answer.is_correct = user_answer.answer.is_correct
    user_answer.save()

    if user_answer.is_correct:
        next_question = get_next_question(question.theme_choice, question)
        if next_question:
            return next_question, True  # Возвращаем следующий вопрос и флаг успешного завершения
        else:
            complete_level(user, question.theme_choice)
            return None, True  # Все вопросы пройдены, флаг успешного завершения

    return question, False  # Пользователь ответил неправильн
# что делает эта фукнция
# Проверка и сохранение ответа пользователя.
# Проверка, был ли ответ правильным.
# Получение следующего вопроса.
# При необходимости завершение уровня.

