# comments/views.py
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после отправки комментария
    else:
        form = CommentForm()
    comments = Comment.objects.all()
    return render(request, 'main_view/home.html', {'form': form, 'comments': comments})
