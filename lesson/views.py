from django.shortcuts import render, redirect
from .models import Question
from .forms import QuizForm

def quiz(request, question_id):
    question = Question.objects.get(pk=question_id)

    if request.method == 'POST':
        form = QuizForm(question, request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choices']
            # Обработка выбранного варианта ответа

            # Перенаправление на следующий вопрос или результаты
            next_question = question.get_next_question()
            if next_question:
                return redirect('quiz', question_id=next_question.id)
            else:
                return redirect('quiz_results')
    else:
        form = QuizForm(question)

    return render(request, 'quiz/quiz.html', {'question': question, 'form': form})
