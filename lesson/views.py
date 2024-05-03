from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuizForm
from .models import Question, UserAnswer
from main_view.models import ListOfTheme
from .utils import complete_and_get_next_question, get_first_question_for_theme, get_or_create_user_answer


def view_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = QuizForm(question, request.POST)
        if form.is_valid():
            user_answer, created = get_or_create_user_answer(request.user, question)
            next_question, completed = complete_and_get_next_question(request.user, question, form)
            if completed:
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


def quiz_completed(request):
    return render(request, 'lesson/quiz_completed.html')

def theory_view(request, theme_id):
    theme = get_object_or_404(ListOfTheme, pk=theme_id)
    theory_text = ListOfTheme.objects.filter(theme_text=theme_id)
    first_question = get_first_question_for_theme(theme)

    return render(request, 'lesson/theory.html', {'theme': theme, 'theory_text': theory_text, 'first_question': first_question})

