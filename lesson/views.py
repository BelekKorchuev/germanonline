# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import QuizForm, AnswerForm
# from .models import Question


# def quiz(request, question_id):
#     question = Question.objects.get(pk=question_id)
#
#     if request.method == 'POST':
#         form = QuizForm(question, request.POST)
#         if form.is_valid():
#             selected_choice = form.cleaned_data['choices']
#             # Обработка выбранного варианта ответа
#             user_answer = UserAnswer(user_id=request.user.id, question=question_id, selected_choice=selected_choice)
#             user_answer.save()
#
#             # Перенаправление на следующий вопрос или результаты
#             next_question = question.get_next_question()
#             if next_question:
#                 return redirect('lesson:quiz', question_id=next_question.id)
#             else:
#                 return redirect('lesson:quiz_results', question_id=question_id)
#     else:
#         form = QuizForm(question)
#
#     return render(request, 'lesson/quiz.html', {'question': question, 'form': form})


# def quiz_results(request, question_id):
#     # Получаем вопрос по его идентификатору
#     question = Question.objects.get(pk=question_id)
#     # Получаем ответ пользователя из данных формы
#     user_choice_id = request.POST.get('choices')
#     # Получаем объект выбора пользователя
#     user_choice = Choice.objects.get(pk=user_choice_id)
#     # Определяем, правильный ли это ответ
#     is_correct = user_choice.correct
#     # Передаем данные в шаблон
#     context = {
#         'question': question,
#         'user_choice': user_choice,
#         'is_correct': is_correct,
#     }
#     return render(request, 'lesson/quiz_results.html', context)


# def quiz_results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     # Используйте get_object_or_404 для получения объекта Choice или возврата 404, если не найден
#     user_choice = get_object_or_404(Choice, pk=request.POST.get('choices'))
#
#     # Определяем, правильный ли это ответ
#     is_correct = user_choice.correct
#
#     # Передаем данные в шаблон
#     context = {
#         'question': question,
#         'user_choice': user_choice,
#         'is_correct': is_correct,
#     }
#
#     return render(request, 'lesson/quiz_results.html', context)


# def quiz_resultss(request, question_id):
#     # Получаем все ответы пользователя
#     user_answer = Choice.objects.filter(user=request.user, question=question_id)
#
#     # Вычисляем общий результат
#     total_correct = user_answer.filter(correct=True).count()
#     total_questions = Question.objects.count()
#     total_incorrect = total_questions - total_correct
#
#     # Передаем данные в шаблон
#     context = {
#         'total_correct': total_correct,
#         'total_incorrect': total_incorrect,
#         'total_questions': total_questions,
#     }
#
#     return render(request, 'lesson/quiz_results.html', context)


# Ваш views.py


# def view_question(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     answers = question.answer_set.all()
#
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             # Обработка ответа пользователя
#             answer = form.save(commit=False)
#             answer.question = question
#             answer.save()
#             # Перенаправление пользователя на следующий вопрос
#             # Здесь вы должны реализовать логику определения следующего вопроса
#             return redirect('next_question_view')  # Замените 'next_question_view' на ваш реальный URL
#
#     else:
#         form = AnswerForm()
#
#     return render(request, 'lesson/quiz.html', {'question': question, 'answers': answers, 'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuizForm
from .models import Question, UserAnswer


def view_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user_answer, created = UserAnswer.objects.get_or_create(question=question, user=request.user)

    if request.method == 'POST':
        form = QuizForm(question, request.POST)
        if form.is_valid():
            # Обновляем информацию о выбранном ответе
            user_answer.answer = form.cleaned_data['choices']
            user_answer.is_correct = user_answer.answer.is_correct
            user_answer.save()

        if user_answer.is_correct:
                print("Пользователь уже правильно ответил на вопрос")
                # Если пользователь уже правильно ответил на вопрос, перенаправляем его на следующий вопрос
                next_question = get_next_question(question)
                if next_question:
                    return redirect('lesson:view_question', question_id=next_question.id)
                else:
                    return redirect('lesson:quiz_completed')
        else:
            print("Пользователь ответил неправильно или впервые отвечает")
            # Перенаправляем пользователя на тот же вопрос после неправильного ответа
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
    # Получаем все ответы пользователя
    user_answers = UserAnswer.objects.all()

    # Получаем общее количество вопросов
    total_questions = Question.objects.count()

    # Получаем количество правильных ответов
    correct_answers = user_answers.filter(is_correct=True).count()

    # Вычисляем процент правильных ответов
    percentage_correct = (correct_answers / total_questions) * 100 if total_questions != 0 else 0

    # Возвращаем результаты в шаблон
    results = {
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'percentage_correct': round(percentage_correct, 2),
    }

    return render(request, 'lesson/quiz_completed.html', {'results': results})
