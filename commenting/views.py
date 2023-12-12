# comments/views.py
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def home(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после отправки комментария
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    return render(request, 'commenting/htmlka.html', {'form': form, 'comments': comments})
