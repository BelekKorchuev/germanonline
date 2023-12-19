from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuizForm
from .models import Question, UserAnswer
from main_view.models import ListOfTheme


def view_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user_answer, created = UserAnswer.objects.get_or_create(question=question, user=request.user)

    if request.method == 'POST':
        form = QuizForm(question, request.POST)
        if form.is_valid():
            user_answer.answer = form.cleaned_data['choices']
            user_answer.is_correct = user_answer.answer.is_correct
            user_answer.save()

        if user_answer.is_correct:
            print("Пользователь уже правильно ответил на вопрос")
            next_question = get_next_question(question)
            if next_question:
                return redirect('lesson:view_question', question_id=next_question.id)
            else:
                return redirect('lesson:quiz_completed')
        else:
            print("Пользователь ответил неправильно или впервые отвечает")
            return redirect('lesson:view_question', question_id=question.id)
    else:
        form = QuizForm(question)

    return render(request, 'lesson/quiz.html', {'question': question, 'form': form})


def get_next_question(question):
    try:
        next_question = Question.objects.filter(order__gt=question.order).order_by('order').first()
        return next_question
    except Question.DoesNotExist:
        return None


def quiz_completed(request):
    user_answers = UserAnswer.objects.all()
    total_questions = Question.objects.count()
    correct_answers = user_answers.filter(is_correct=True).count()
    percentage_correct = (correct_answers / total_questions) * 100 if total_questions != 0 else 0
    results = {
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'percentage_correct': round(percentage_correct, 2),
    }

    return render(request, 'lesson/quiz_completed.html', {'results': results})


def get_next_question_for_theme(theme):
    try:
        first_question = Question.objects.filter(theme_choice=theme, order=0).first()
        return first_question
    except Question.DoesNotExist:
        return None


def theory_view(request, theme_id):
    theme = get_object_or_404(ListOfTheme, pk=theme_id)
    theory_text = theme.theme_text
    first_question = get_next_question_for_theme(theme)

    return render(request, 'lesson/theory.html', {'theme': theme, 'theory_text': theory_text, 'first_question': first_question})
